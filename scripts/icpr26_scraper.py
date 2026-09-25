#!/usr/bin/env python3
"""
ICPR 2026 COMPLETE paper scraper
--------------------------------
Official list: https://icpr2026.org/acceptedPapersTrack.html  (710 papers + 5 competition papers,
6 tracks incl. Track 5 = Document Analysis and Recognition). Each row links to the Springer chapter
(LNCS 16812-16827), which gives the DOI. Abstracts: Crossref by DOI, then OpenAlex for the rest.

Output: ICPR26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python icpr26_scraper.py          # ~2-3 minutes
"""
import re, sys, time
import requests
import pandas as pd
from bs4 import BeautifulSoup

PAGE = "https://icpr2026.org/acceptedPapersTrack.html"
OFFICIAL = 715
CROSSREF = "https://api.crossref.org/works"
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
    r"\btable|formula|math(?:ematical)? expression|key information|information extraction|"
    r"retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG|late interaction|multi-vector",
    re.I)


def get_json(url, params, tries=5):
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=HEAD, timeout=60)
            if r.status_code == 200:
                return r.json()
            print(f"  HTTP {r.status_code} from {url}")
        except (requests.RequestException, ValueError) as e:
            print("  error:", e)
        time.sleep(5 * (i + 1))
    return None


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for h in soup.find_all(["h2", "h3"]):
        ht = " ".join(h.get_text(" ", strip=True).split())
        m = re.match(r"Track\s+(T?\d+|Competition)\s*:?\s*(.*)", ht, re.I)
        if not m:
            continue
        track = f"T{m.group(1).lstrip('Tt')}: {m.group(2)}" if m.group(1)[-1].isdigit() else "Competition"
        table = h.find_next("table")
        if table is None:
            continue
        for tr in table.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 2:
                continue
            pid = re.search(r"[A-Za-z]?\d+", tds[0].get_text(" ", strip=True))
            if not pid:
                continue
            rr = "yes" if tds[0].find("img") else ""
            lines = [l.strip() for l in tds[1].get_text("\n", strip=True).split("\n") if l.strip()]
            lines = [l for l in lines if not re.match(r"presented by|slides$", l, re.I)]
            if len(lines) == 1:                       # title and authors in one text node
                parts = re.split(r"\s{3,}", lines[0])
                lines = parts if len(parts) > 1 else lines
            title = lines[0] if lines else ""
            authors = lines[1] if len(lines) > 1 else ""
            sess, doi, pdf = "", "", ""
            for a in tr.find_all("a", href=True):
                href = a["href"]
                if "/sessions/" in href and not sess:
                    sess = a.get_text(strip=True)
                d = re.search(r"(10\.1007/[\w.\-]+_\d+)", href)
                if d:
                    doi, pdf = d.group(1), href
            rows.append({"Paper_ID": pid.group(), "Track": track, "Title": title,
                         "Authors": authors,
                         "Presentation": "Oral" if sess.upper().startswith("O") else ("Poster" if sess else ""),
                         "Session": sess, "RR_Label": rr, "DOI": doi.lower(),
                         "Paper_Link": f"https://doi.org/{doi}" if doi else "", "PDF_Link": pdf})
        # the same table must not be read twice by a later heading
    df = pd.DataFrame(rows).drop_duplicates(subset=["Paper_ID", "Track"])
    df["_k"] = df["DOI"].where(df["DOI"] != "", df["Track"] + "|" + df["Paper_ID"])
    return df.drop_duplicates(subset="_k").drop(columns="_k").reset_index(drop=True)


def crossref_abstracts(dois):
    out = {}
    for k in range(0, len(dois), 40):
        chunk = dois[k:k + 40]
        j = get_json(CROSSREF, {"filter": ",".join("doi:" + d for d in chunk), "rows": 40})
        for w in (j or {}).get("message", {}).get("items", []):
            ab = re.sub(r"<[^>]+>", " ", w.get("abstract", "") or "")
            ab = re.sub(r"^\s*Abstract\s*", "", " ".join(ab.split()), flags=re.I)
            if ab:
                out[w["DOI"].lower()] = ab
        time.sleep(0.5)
    return out


def openalex_abstracts(dois):
    out = {}
    for k in range(0, len(dois), 50):
        j = get_json(OPENALEX, {"filter": "doi:" + "|".join(dois[k:k + 50]), "per-page": 50})
        for w in (j or {}).get("results", []):
            inv = w.get("abstract_inverted_index") or {}
            pos = sorted((p, word) for word, ps in inv.items() for p in ps)
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            if d and pos:
                out[d] = " ".join(word for _, word in pos)
        time.sleep(0.3)
    return out


def main():
    print("Step 1: official accepted-paper list ...")
    r = requests.get(PAGE, headers=HEAD, timeout=60)
    if r.status_code != 200:
        sys.exit(f"HTTP {r.status_code} for {PAGE} -> send a screenshot.")
    df = parse_page(r.text)
    if df.empty:
        open("icpr_debug.html", "w", encoding="utf-8").write(r.text)
        sys.exit("0 papers parsed (page saved as icpr_debug.html) -> upload it here.")
    print("  " + str(df["Track"].value_counts().to_dict()))
    print(f"  total {len(df)} (official {OFFICIAL}); without DOI: {int(df['DOI'].eq('').sum())}")

    dois = [d for d in df["DOI"] if d]
    print("Step 2: abstracts from Crossref ...")
    abs_map = crossref_abstracts(dois)
    rest = [d for d in dois if d not in abs_map]
    if rest:
        print(f"Step 3: {len(rest)} missing -> OpenAlex ...")
        abs_map.update(openalex_abstracts(rest))
    df["Abstract"] = df["DOI"].map(abs_map).fillna("")

    df["Match_Reason"] = df["Title"].apply(lambda t: "title" if TITLE_KW.search(t) else "")
    m = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
    df.loc[m, "Match_Reason"] = "abstract"
    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW, na=False) |
              df["Track"].str.startswith("T5")].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda x: "Dataset" if x else "Method"))
    cand = cand.reset_index(drop=True)
    for t in (ds, other, cand):
        t.index += 1

    tc = df["Track"].value_counts()
    summary = pd.DataFrame({
        "Item": ["Total papers", "Official total"] + [f"  {k}" for k in tc.index] +
                ["Oral", "Poster", "Dataset/Benchmark papers", "Other papers",
                 "VDU/RAG candidates (all of Track 5 + keywords)", "Papers WITHOUT abstract", "Source"],
        "Value": [len(df), OFFICIAL] + list(tc.values) +
                 [int((df.Presentation == "Oral").sum()), int((df.Presentation == "Poster").sum()),
                  len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()), PAGE]})
    with pd.ExcelWriter("ICPR26_papers.xlsx", engine="openpyxl") as xw:
        ds.to_excel(xw, sheet_name="Dataset_Papers", index_label="No")
        other.to_excel(xw, sheet_name="Other_Papers", index_label="No")
        cand.to_excel(xw, sheet_name="VDU_RAG_Candidates", index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(
                    max(len(str(c.value or "")) for c in col) + 2, 70)
    print("\nDONE\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
