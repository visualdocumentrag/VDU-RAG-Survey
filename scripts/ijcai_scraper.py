#!/usr/bin/env python3
"""
IJCAI COMPLETE paper scraper (official source: ijcai.org/proceedings/<year>/)
-----------------------------------------------------------------------------
IJCAI-ECAI 2026: Bremen, 15-21 Aug 2026. The official proceedings page lists every paper with its
track (Main Track, Survey, Demo, AI for Good, Special Track ...); each paper's detail page has the abstract.

Output: IJCAI26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python ijcai_scraper.py               # IJCAI 2026 (~10-15 min with abstracts)
  !python ijcai_scraper.py --year 2025
"""
import re, sys, time, argparse
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}
TITLE_KW = re.compile(r"\b(?:dataset|datasets|benchmark|benchmarks|benchmarking|corpus|corpora)\b|\w+bench\b|\bbench\w*", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(
    r"visually[- ]rich|document|DocVQA|multi-?page|\bPDF\b|\bOCR\b|layout|\bchart|infographic|\bslides?\b|"
    r"screenshot|text[- ]rich|table (?:understanding|question|reasoning|recognition)|ColPali|late interaction|"
    r"multi-vector|retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG", re.I)
S = requests.Session(); S.headers.update(HEAD)


def get(url, tries=4):
    for i in range(tries):
        try:
            r = S.get(url, timeout=60)
            if r.status_code == 200:
                return r.text
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    return None


def parse_index(html, base):
    soup = BeautifulSoup(html, "html.parser")
    rows, section, sub = [], "", ""
    for el in soup.find_all(["div", "h2", "h3", "h4"]):
        cls = " ".join(el.get("class") or [])
        if "subsection_title" in cls:
            sub = " ".join(el.get_text(" ", strip=True).split()); continue
        if "section_title" in cls or (el.name in ("h2", "h3") and not el.find_parent(class_="section_title")):
            t = " ".join(el.get_text(" ", strip=True).split())
            if t and not el.find(class_="paper_wrapper"):
                section, sub = t, ""
            continue
        track = section + (" > " + sub if sub else "")
        if "paper_wrapper" not in cls:
            continue
        title = el.find(class_="title")
        authors = el.find(class_="authors")
        pdf = det = ""
        for a in el.find_all("a", href=True):
            txt = a.get_text(" ", strip=True).lower()
            if a["href"].lower().endswith(".pdf") and not pdf:
                pdf = urljoin(base, a["href"])
            elif "detail" in txt and not det:
                det = urljoin(base, a["href"])
        rows.append({"Track": track,
                     "Title": " ".join(title.get_text(" ", strip=True).split()) if title else "",
                     "Authors": " ".join(authors.get_text(" ", strip=True).split()) if authors else "",
                     "Paper_Link": det, "PDF_Link": pdf})
    return [r for r in rows if r["Title"]]


def abstract(url):
    if not url:
        return url, ""
    html = get(url, tries=3)
    if html is None:
        return url, None
    soup = BeautifulSoup(html, "html.parser")
    m = soup.find("meta", attrs={"name": "citation_abstract"}) or soup.find("meta", attrs={"name": "description"})
    if m and m.get("content") and len(m["content"]) > 150:
        return url, " ".join(m["content"].split())
    best = ""
    for el in soup.select("div.col-md-12, div.abstract, p"):
        t = " ".join(el.get_text(" ", strip=True).split())
        if 150 < len(t) < 4000 and len(t) > len(best) and not el.find(class_="paper_wrapper"):
            best = t
    return url, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2026)
    ap.add_argument("--no-abstract", action="store_true")
    args = ap.parse_args()
    Y = args.year
    base = f"https://www.ijcai.org/proceedings/{Y}/"
    html = get(base)
    if not html:
        sys.exit(f"Could not open {base} -> proceedings may not be online yet, or send a screenshot.")
    df = pd.DataFrame(parse_index(html, base))
    if df.empty:
        open("ijcai_debug.html", "w", encoding="utf-8").write(html)
        sys.exit("0 papers parsed (page saved as ijcai_debug.html) -> upload it here.")
    df = df.drop_duplicates(subset=["Title", "PDF_Link"]).reset_index(drop=True)
    print(f"{len(df)} papers on the proceedings page")
    print(df["Track"].value_counts().head(20).to_string())

    failed = 0
    if args.no_abstract:
        df["Abstract"] = ""
    else:
        print("Reading abstracts (4 parallel) ...")
        with ThreadPoolExecutor(4) as ex:
            res = dict(ex.map(abstract, df["Paper_Link"]))
        failed = sum(1 for v in res.values() if v is None)
        df["Abstract"] = df["Paper_Link"].map(lambda u: res.get(u) or "")

    df["Match_Reason"] = df["Title"].map(lambda t: "title" if TITLE_KW.search(t) else "")
    k = df["Match_Reason"].eq("") & df["Abstract"].str.contains(ABSTRACT_KW)
    df.loc[k, "Match_Reason"] = "abstract"
    ds = df[df.Match_Reason != ""].reset_index(drop=True)
    other = df[df.Match_Reason == ""].drop(columns="Match_Reason").reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW)].reset_index(drop=True)
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other, cand = clean(ds), clean(other), clean(cand)
    tc = df["Track"].value_counts()
    summary = pd.DataFrame({
        "Item": ["Total papers"] + [f"  {k}" for k in tc.index] +
                ["Dataset/Benchmark", "Other", "VDU/RAG candidates (check by hand)",
                 "Papers WITHOUT abstract", "Abstract pages FAILED", "Source"],
        "Value": [len(df)] + list(tc.values) +
                 [len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()), failed, base]})
    with pd.ExcelWriter(f"IJCAI{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
        for name, t in [("Dataset_Papers", ds), ("Other_Papers", other), ("VDU_RAG_Candidates", cand)]:
            t.rename(lambda i: i + 1).to_excel(xw, sheet_name=name, index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(max(len(str(c.value or "")) for c in col) + 2, 70)
    print("\nDONE\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
