#!/usr/bin/env python3
"""
IJCV COMPLETE paper scraper via Crossref (default: IJCV 2026; --year for other years)
-----------------------------------------------------------------------------------
Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence (ISSN 0162-8828 / e-ISSN 1939-3539).
IEEE Xplore blocks scripts, so the list comes from Crossref (IEEE deposits every TPAMI DOI there).
"<year> papers" = every TPAMI article whose Crossref publication date is in that year
(issues of that volume + Early Access). Papers first online in <year> but printed in the next
year's issue can appear in BOTH years' lists (their DOI shows it).
Abstracts: Crossref, then OpenAlex for missing ones.

Output: TPAMI26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python ijcv_scraper.py              # IJCV 2026
  !python ijcv_scraper.py --year 2025  # IJCV 2025
  !python journal_scraper.py --journal PR --year 2025 --volumes 157-168   # by volume numbers
  !python journal_scraper.py --journal TPAMI --year 2025
  !python journal_scraper.py --journal CVIU --year 2026
"""
import re, sys, time, argparse
import requests
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

ISSNS = []          # set in main() from --journal / --issn
JOURNALS = {
    "TPAMI": ("IEEE TPAMI", ["0162-8828", "1939-3539"]),
    "PR":    ("Pattern Recognition (Elsevier)", ["0031-3203", "1873-5142"]),
    "IJCV":  ("International Journal of Computer Vision", ["0920-5691", "1573-1405"]),
    "TIP":   ("IEEE Transactions on Image Processing", ["1057-7149", "1941-0042"]),
    "IJDAR": ("Int. J. Document Analysis and Recognition", ["1433-2833", "1433-2825"]),
    "CVIU":  ("Computer Vision and Image Understanding (Elsevier)", ["1077-3142", "1090-235X"]),
}
CROSSREF = "https://api.crossref.org/journals/{}/works"
OPENALEX = "https://api.openalex.org/works"
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey; mailto:survey@example.org)"}

TITLE_KW = re.compile(
    r"\b(dataset|data set|datasets|benchmark|benchmarks|benchmarking|corpus|corpora|"
    r"testbed|test suite|leaderboard)\b|\w+bench\b|\bbench\w*", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)"
    r"[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(
    r"visually[- ]rich|document|DocVQA|multi-?page|\bPDF\b|\bOCR\b|layout|\bchart|infographic|"
    r"\bslides?\b|screenshot|text[- ]rich|scanned|handwrit|text recognition|scene text|"
    r"\btable (?:recognition|structure|understanding|question)|formula|key information|"
    r"retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG|late interaction|multi-vector|"
    r"cross-modal retrieval|multimodal retrieval|token (?:pruning|compression|reduction)", re.I)
SKIP = re.compile(r"^(?:Front Cover|Back Cover|Table of Contents|IEEE Transactions on Pattern|"
                  r"Information for Authors|Editorial|Corrections? to|Correction:|Erratum|Retraction(?:\s|:)|"
                  r"Guest Editorial|Introduction to the Special)", re.I)


def get(url, params, tries=5):
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=HEAD, timeout=60)
            if r.status_code == 200:
                return r.json()
            print(f"  HTTP {r.status_code} from {url}")
            if r.status_code == 404:
                return None
        except (requests.RequestException, ValueError) as e:
            print("  error:", e)
        time.sleep(5 * (i + 1))
    return None


def fetch_crossref(year, y_from=None, y_to=None):
    rows, seen = [], set()
    for issn in ISSNS:
        cursor, n0 = "*", len(rows)
        while True:
            j = get(CROSSREF.format(issn), {"filter": f"from-pub-date:{y_from or year}-01-01,until-pub-date:{y_to or year}-12-31",
                                            "rows": 1000, "cursor": cursor})
            msg = (j or {}).get("message", {})
            items = msg.get("items", [])
            for w in items:
                doi = w.get("DOI", "").lower()
                if not doi or doi in seen:
                    continue
                seen.add(doi)
                title = " ".join(" ".join(w.get("title") or [""]).split())
                au = ", ".join(" ".join(filter(None, [a.get("given"), a.get("family")]))
                               for a in w.get("author", []))
                ab = re.sub(r"<[^>]+>", " ", w.get("abstract", "") or "")
                ab = re.sub(r"^\s*Abstract\s*", "", " ".join(ab.split()), flags=re.I)
                dp = (w.get("published") or w.get("issued") or {}).get("date-parts", [[None]])[0]
                rows.append({"Title": title, "Authors": au,
                             "Volume": w.get("volume", ""), "Issue": w.get("issue", ""),
                             "Pages": w.get("page", ""),
                             "Status": "Issue/Volume" if (w.get("issue") or w.get("volume")) else "Early Access / In Press",
                             "Published": "-".join(str(x) for x in dp if x),
                             "Type_Crossref": w.get("type", ""), "DOI": doi,
                             "Paper_Link": "https://doi.org/" + doi, "Abstract": ab})
            if len(items) < 1000 or not msg.get("next-cursor"):
                break
            cursor = msg["next-cursor"]
            time.sleep(1)
        print(f"  ISSN {issn}: +{len(rows) - n0}")
    return rows


def openalex_abstracts(dois):
    out = {}
    for k in range(0, len(dois), 50):
        j = get(OPENALEX, {"filter": "doi:" + "|".join(dois[k:k + 50]), "per-page": 50})
        for w in (j or {}).get("results", []):
            inv = w.get("abstract_inverted_index") or {}
            pos = sorted((p, word) for word, ps in inv.items() for p in ps)
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            if d and pos:
                out[d] = " ".join(word for _, word in pos)
        time.sleep(0.3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2026)
    ap.add_argument("--journal", default="IJCV", choices=sorted(JOURNALS))
    ap.add_argument("--volumes", default="", help="e.g. 157-168: keep exactly these volumes (searches year-2 .. year+1)")
    args = ap.parse_args()
    YEAR, J = args.year, args.journal
    NAME, issns = JOURNALS[J]
    ISSNS[:] = issns
    print(f"Step 1: {NAME} {YEAR} articles from Crossref ...")
    if args.volumes:
        v1, v2 = (int(x) for x in args.volumes.split("-"))
        print(f"  volume mode: keeping Vol. {v1}-{v2} (dates {YEAR-2}-{YEAR+1} searched)")
        rows = [r for r in fetch_crossref(YEAR, YEAR - 2, YEAR + 1)
                if str(r["Volume"]).isdigit() and v1 <= int(r["Volume"]) <= v2]
    else:
        rows = fetch_crossref(YEAR)
    if not rows:
        sys.exit("0 articles -> send a screenshot.")
    df = pd.DataFrame(rows)
    removed = df[df["Title"].str.contains(SKIP) | df["Title"].eq("")]
    df = df.drop(removed.index).reset_index(drop=True)
    print(f"  {len(df)} articles kept, {len(removed)} non-paper items removed (covers, editorials, corrections)")

    miss = df["Abstract"].eq("")
    if miss.any():
        print(f"Step 2: {int(miss.sum())} abstracts missing -> OpenAlex ...")
        m = openalex_abstracts(list(df.loc[miss, "DOI"]))
        df.loc[miss, "Abstract"] = df.loc[miss, "DOI"].map(m).fillna("")

    df["Match_Reason"] = df["Title"].apply(lambda t: "title" if TITLE_KW.search(t) else "")
    k = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
    df.loc[k, "Match_Reason"] = "abstract"
    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW, na=False)].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda x: "Dataset" if x else "Method"))
    cand = cand.reset_index(drop=True)
    for t in (ds, other, cand):
        t.index += 1

    summary = pd.DataFrame({
        "Item": [f"Total articles ({NAME}, {YEAR})", "  in an issue / volume", "  Early Access / In Press", "Removed non-paper items",
                 "Dataset/Benchmark papers", "Other papers", "VDU/RAG candidates (check by hand)",
                 "Papers WITHOUT abstract", "Source"],
        "Value": [len(df), int((df.Status == "Issue/Volume").sum()), int((df.Status != "Issue/Volume").sum()),
                  len(removed), len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()),
                  f"Crossref (ISSN {' / '.join(ISSNS)}, pub-date {YEAR}) + OpenAlex"]})
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other, cand, removed = clean(ds), clean(other), clean(cand), clean(removed)
    with pd.ExcelWriter(f"{J}{YEAR % 100}_papers.xlsx", engine="openpyxl") as xw:
        ds.to_excel(xw, sheet_name="Dataset_Papers", index_label="No")
        other.to_excel(xw, sheet_name="Other_Papers", index_label="No")
        cand.to_excel(xw, sheet_name="VDU_RAG_Candidates", index_label="No")
        removed.to_excel(xw, sheet_name="Removed_items", index=False)
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(
                    max(len(str(c.value or "")) for c in col) + 2, 70)
    print("\nDONE\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
