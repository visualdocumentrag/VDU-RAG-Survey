#!/usr/bin/env python3
"""
ICDAR 2026 COMPLETE paper scraper (official source: SpringerLink, LNCS 16972-16975)
-----------------------------------------------------------------------------------
Expected: 140 full papers + 8 competition reports = 148 (from the official book page).

Output: ICDAR26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python icdar26_scraper.py          # ~3-5 minutes, title + abstract
"""
import re, time
import requests
import pandas as pd
from bs4 import BeautifulSoup

VOLUMES = {  # verified DOIs of the 4 volumes
    "Part I (LNCS 16972)":   "978-3-032-36023-6",
    "Part II (LNCS 16973)":  "978-3-032-36033-5",
    "Part III (LNCS 16974)": "978-3-032-36039-7",
    "Part IV (LNCS 16975)":  "978-3-032-36042-7",
}
BOOK = "https://link.springer.com/book/10.1007/{}?page={}"
HEAD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
EXPECTED = 148

TITLE_KW = re.compile(r"\b(dataset|datasets|benchmark|benchmarks|corpus|corpora)\b|\w+bench\b", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)"
    r"[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(
    r"visually[- ]rich|document understanding|document question|document VQA|DocVQA|"
    r"long document|multi-?page|retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|"
    r"vision[- ]language model|\bVLMs?\b|\bMLLMs?\b|\bLVLMs?\b|multimodal (?:large|reasoning|document)|"
    r"information extraction|key information|document parsing|layout analysis|"
    r"\btable|\bchart|infographic|OCR-free", re.I)

s = requests.Session(); s.headers.update(HEAD)


def get(url, tries=4):
    for i in range(tries):
        try:
            r = s.get(url, timeout=40)
            if r.status_code == 200:
                return r.text
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    return None


def parse_toc(html, doi, part):
    """Find every chapter link of this volume anywhere on the page (query strings allowed)."""
    soup = BeautifulSoup(html, "html.parser")
    pat = re.compile(r"/chapter/10\.1007/" + re.escape(doi) + r"_(\d+)")
    rows, seen = [], set()
    for a in soup.find_all("a", href=pat):
        n = pat.search(a["href"]).group(1)
        title = " ".join(a.get_text(" ", strip=True).split())
        if n in seen or not title or title.lower().startswith(("download", "view")):
            continue
        seen.add(n)
        sec = ""
        for h in a.find_all_previous(["h2", "h3"]):
            t = h.get_text(" ", strip=True)
            if t and not h.find("a", href=pat) and t not in ("Front Matter", "Back Matter"):
                sec = t
                break
        rows.append({"Title": title, "Part": part, "Section": sec,
                     "Paper_Link": f"https://link.springer.com/chapter/10.1007/{doi}_{n}"})
    return rows


def probe_chapters(doi, part):
    """Fallback: chapters are numbered {doi}_1, _2, ... -> open them one by one until 2 misses."""
    rows, n, miss = [], 1, 0
    while miss < 2 and n < 200:
        url = f"https://link.springer.com/chapter/10.1007/{doi}_{n}"
        html = get(url, tries=2)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            t = soup.find("meta", attrs={"name": "citation_title"})
            if t and t.get("content"):
                rows.append({"Title": t["content"].strip(), "Part": part, "Section": "",
                             "Paper_Link": url})
                miss = 0
            else:
                miss += 1
        else:
            miss += 1
        n += 1
        time.sleep(0.7)
    return rows


def chapter_details(url):
    html = get(url)
    if not html:
        return None
    soup = BeautifulSoup(html, "html.parser")
    authors = [m["content"] for m in soup.find_all("meta", attrs={"name": "citation_author"})]
    pages = "-".join(filter(None, [
        (soup.find("meta", attrs={"name": "citation_firstpage"}) or {}).get("content", ""),
        (soup.find("meta", attrs={"name": "citation_lastpage"}) or {}).get("content", "")]))
    ab = soup.find(id=re.compile(r"^Abs1-content$")) or soup.find("section", attrs={"data-title": "Abstract"})
    abstract = " ".join(ab.get_text(" ", strip=True).split()) if ab else ""
    if not abstract:
        m = soup.find("meta", attrs={"name": "dc.description"}) or soup.find("meta", attrs={"name": "description"})
        abstract = m["content"].strip() if m and m.get("content") else ""
    kw = [k.get_text(" ", strip=True) for k in soup.select("li.c-article-subject-list__subject")]
    return {"Authors": ", ".join(authors), "Pages": pages, "Keywords": "; ".join(kw),
            "Abstract": abstract}


def main():
    rows = []
    for part, doi in VOLUMES.items():
        seen, vol = set(), []
        for page in range(1, 10):
            html = get(BOOK.format(doi, page))
            if page == 1 and html is not None and not parse_toc(html, doi, part):
                open(f"debug_{doi}.html", "w", encoding="utf-8").write(html)
            got = [r for r in (parse_toc(html, doi, part) if html else []) if r["Paper_Link"] not in seen]
            if not got:
                break
            seen.update(r["Paper_Link"] for r in got)
            vol.extend(got)
            time.sleep(1)
        if not vol:
            print(f"{part}: table of contents not readable -> opening chapters one by one ...")
            vol = probe_chapters(doi, part)
        print(f"{part}: {len(vol)} papers")
        rows.extend(vol)

    if not rows:
        raise SystemExit("0 papers: Springer is blocking this connection. Send a screenshot.")
    df = pd.DataFrame(rows).drop_duplicates(subset="Paper_Link").reset_index(drop=True)
    print(f"TOTAL: {len(df)} (expected {EXPECTED})" + ("" if len(df) == EXPECTED else "  !! CHECK"))

    details, failed = [], []
    for i, u in enumerate(df["Paper_Link"], 1):
        d = chapter_details(u)
        if d is None:
            failed.append(u); d = {"Authors": "", "Pages": "", "Keywords": "", "Abstract": ""}
        details.append(d)
        if i % 20 == 0:
            print(f"  details {i}/{len(df)}")
        time.sleep(0.7)
    df = pd.concat([df, pd.DataFrame(details)], axis=1)
    df["DOI"] = df["Paper_Link"].str.extract(r"(10\.1007/.+)$")

    df["Match_Reason"] = ""
    df.loc[df["Section"].str.contains("Benchmarks and Datasets", na=False), "Match_Reason"] = "section"
    m = (df["Match_Reason"] == "") & df["Title"].str.contains(TITLE_KW)
    df.loc[m, "Match_Reason"] = "title"
    m = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
    df.loc[m, "Match_Reason"] = "abstract"

    cols = ["Title", "Authors", "Part", "Section", "Pages", "DOI", "Paper_Link", "Keywords", "Abstract"]
    ds = df[df["Match_Reason"] != ""][cols + ["Match_Reason"]].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""][cols].reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW, na=False)].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda x: "Dataset" if x else "Method"))
    cand = cand[["Type"] + cols].reset_index(drop=True)
    for t in (ds, other, cand):
        t.index += 1

    summary = pd.DataFrame({"Item": ["Total papers", "Expected", "Dataset/Benchmark papers", "Other papers",
                                     "VDU/RAG candidates (check by hand)", "Chapter pages FAILED", "Source"],
                            "Value": [len(df), EXPECTED, len(ds), len(other), len(cand), len(failed),
                                      "SpringerLink LNCS 16972-16975"]})
    with pd.ExcelWriter("ICDAR26_papers.xlsx", engine="openpyxl") as xw:
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
    if failed:
        print("!! Failed pages:", *failed, sep="\n  ")


if __name__ == "__main__":
    main()
