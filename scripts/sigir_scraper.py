#!/usr/bin/env python3
"""
SIGIR 2026 COMPLETE paper scraper via Crossref (Melbourne, 20-24 Jul 2026)
-----------------------------------------------------------------------------------
Default: CIKM 2025 (Seoul). Usage: !python acm_scraper.py --acronym "CIKM '25" --query "Information and Knowledge Management"
(ACM DL blocks scripts; Crossref holds every ACM DOI + usually the abstract.)
Steps: 1) find the conference's proceedings volume(s) on Crossref by event acronym
       2) every paper of each volume (+ abstract)   3) OpenAlex fills missing abstracts
Output: <ACRONYM><yy>_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python acm_scraper.py                 # CIKM 2025 (default)
  !python acm_scraper.py --acronym "SIGIR '26" --query "SIGIR Conference on Research and Development in Information Retrieval" --from-date 2026-01-01 --seed 10.1145/3805712
  !python acm_scraper.py --acronym "KDD '26" --query "SIGKDD Conference on Knowledge Discovery and Data Mining"
"""
import re, sys, time, argparse
import requests
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

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
    r"visually[- ]rich|document image|document understanding|DocVQA|document VQA|"
    r"document question answering|multi-?page|long[- ]document|\bPDF\b|\bOCR\b|layout|\bchart|"
    r"infographic|\bslides?\b|screenshot|text[- ]rich|scanned|ColPali|visual document|"
    r"multimodal document|document parsing|document retrieval|retrieval[- ]augmented|"
    r"(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG|late interaction|multi-vector|\btable", re.I)


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


CROSSREF = "https://api.crossref.org/works"
KNOWN_VOLUMES = []


FROM_DATE = "2025-06-01"


def crossref_volumes(acronym, query):
    """Return {proceedings DOI: (title, [ISBNs])} for every volume of the conference."""
    vols = {}
    j = get(CROSSREF, {"filter": f"type:proceedings,prefix:10.1145,from-pub-date:{FROM_DATE}",
                       "query.bibliographic": query,
                       "rows": 50})
    for w in (j or {}).get("message", {}).get("items", []):
        ev = w.get("event", {}) or {}
        if acronym in (ev.get("acronym") or "") or acronym in (ev.get("name") or ""):
            vols[w["DOI"].lower()] = ((w.get("title") or [""])[0], w.get("ISBN", []))
    for d in KNOWN_VOLUMES:
        if d not in vols:
            w = (get(CROSSREF + "/" + d, {}) or {}).get("message", {})
            if w:
                vols[d] = ((w.get("title") or [""])[0], w.get("ISBN", []))
    return vols


def parse_items(items, vol_doi, seen, rows):
    for w in items:
        doi = w.get("DOI", "").lower()
        if not doi.startswith(vol_doi + ".") or doi in seen:
            continue
        seen.add(doi)
        au = ", ".join(" ".join(filter(None, [a.get("given"), a.get("family")]))
                       for a in w.get("author", []))
        ab = re.sub(r"<[^>]+>", " ", w.get("abstract", "") or "")
        ab = re.sub(r"^\s*Abstract\s*", "", " ".join(ab.split()), flags=re.I)
        rows.append({"Title": " ".join(" ".join(w.get("title") or [""]).split()),
                     "Authors": au, "Volume": vol_doi, "Pages": w.get("page", ""),
                     "DOI": doi, "Paper_Link": "https://doi.org/" + doi, "Abstract": ab})


def crossref_papers(vol_doi, isbns, vol_title):
    """Try several Crossref queries; keep only DOIs that start with '<volume DOI>.'"""
    strategies = [("isbn " + i, {"filter": f"isbn:{i}"}) for i in isbns]
    strategies.append(("container-title", {"filter": f"container-title:{vol_title}"}))
    strategies.append(("container search", {"query.container-title": vol_title,
                                            "filter": f"prefix:10.1145,from-pub-date:{FROM_DATE}"}))
    rows, seen = [], set()
    for name, params in strategies:
        before, cursor, pages = len(rows), "*", 0
        while True:
            j = get(CROSSREF, dict(params, rows=1000, cursor=cursor))
            msg = (j or {}).get("message", {})
            items = msg.get("items", [])
            n0 = len(rows)
            parse_items(items, vol_doi, seen, rows)
            pages += 1
            hits = sum(1 for w in items if w.get("DOI", "").lower().startswith(vol_doi + "."))
            if len(items) < 1000 or not msg.get("next-cursor"):
                break
            if name == "container search" and (hits == 0 or pages >= 15):
                break         # relevance search: stop once pages no longer contain this volume
            cursor = msg["next-cursor"]
            time.sleep(1)
        print(f"    via {name}: +{len(rows) - before}")
        if len(rows) - before > 0 and name.startswith(("isbn", "container-title")):
            continue          # still run the others: they can only add missing papers
    return rows


def openalex_abstracts(dois):
    out = {}
    for k in range(0, len(dois), 50):
        chunk = dois[k:k + 50]
        j = get(OPENALEX, {"filter": "doi:" + "|".join(chunk), "per-page": 50})
        for w in (j or {}).get("results", []):
            inv = w.get("abstract_inverted_index") or {}
            pos = sorted((p, word) for word, ps in inv.items() for p in ps)
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            if d:
                out[d] = " ".join(word for _, word in pos)
        if (k // 50) % 10 == 0:
            print(f"  abstracts {min(k+50, len(dois))}/{len(dois)}")
        time.sleep(0.3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--acronym", default="SIGIR '26")
    ap.add_argument("--query", default="SIGIR Conference on Research and Development in Information Retrieval")
    ap.add_argument("--from-date", default="2026-01-01")
    ap.add_argument("--seed", nargs="*", default=["10.1145/3805712"], help="known proceedings DOI(s), always included")
    args = ap.parse_args()
    ACR = args.acronym
    global FROM_DATE
    FROM_DATE = args.from_date
    KNOWN_VOLUMES[:] = [d.lower() for d in args.seed]
    print(f"Step 1: {ACR} proceedings volumes (Crossref) ...")
    vols = crossref_volumes(ACR, args.query)
    for d, (t, i) in vols.items():
        print(f"  {d}  ISBN {i}  {t[:90]}")
    if not vols:
        sys.exit(f"No {ACR} volume found on Crossref -> proceedings not out yet, or send a screenshot.")
    print("Step 2: papers + abstracts (Crossref) ...")
    rows = []
    for d, (t, isbns) in vols.items():
        r = crossref_papers(d, isbns, t)
        print(f"  {d}: {len(r)} papers")
        rows.extend(r)
    if not rows:
        sys.exit("0 papers -> send a screenshot.")
    df = pd.DataFrame(rows).drop_duplicates(subset="DOI").reset_index(drop=True)
    miss = df["Abstract"].eq("")
    if miss.any():
        print(f"Step 3: {int(miss.sum())} abstracts missing -> OpenAlex ...")
        abs_map = openalex_abstracts(list(df.loc[miss, "DOI"]))
        df.loc[miss, "Abstract"] = df.loc[miss, "DOI"].map(abs_map).fillna("")

    df["Match_Reason"] = df["Title"].apply(lambda t: "title" if TITLE_KW.search(t) else "")
    m = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
    df.loc[m, "Match_Reason"] = "abstract"

    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW, na=False)].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda x: "Dataset" if x else "Method"))
    cand = cand.reset_index(drop=True)
    for t in (ds, other, cand):
        t.index += 1

    vc = df["Volume"].value_counts()
    summary = pd.DataFrame({
        "Item": ["Total papers"] + [f"  volume {k}" for k in vc.index] +
                ["Dataset/Benchmark papers", "Other papers", "VDU/RAG candidates (check by hand)",
                 "Papers WITHOUT abstract", "Sources"],
        "Value": [len(df)] + list(vc.values) +
                 [len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()),
                  "Crossref (list + abstracts) + OpenAlex (missing abstracts); DOI link = official ACM DL page"]})
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other, cand = clean(ds), clean(other), clean(cand)
    fname = re.sub(r"\W", "", ACR.split()[0]) + re.sub(r"\D", "", ACR) + "_papers.xlsx"
    with pd.ExcelWriter(fname, engine="openpyxl") as xw:
        ds.to_excel(xw, sheet_name="Dataset_Papers", index_label="No")
        other.to_excel(xw, sheet_name="Other_Papers", index_label="No")
        cand.to_excel(xw, sheet_name="VDU_RAG_Candidates", index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(
                    max(len(str(c.value or "")) for c in col) + 2, 70)
    print(f"\nDONE -> {fname}\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
