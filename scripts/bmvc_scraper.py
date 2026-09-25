#!/usr/bin/env python3
"""
BMVC COMPLETE accepted-paper list (official source: bmvc<year>.bmva.org/programme/accepted_papers/)
---------------------------------------------------------------------------------------------------
BMVC 2026 (Lancaster, 23-26 Nov 2026): 406 accepted of 1,448 submissions. The official page gives
only ID + title (papers/abstracts are published by BMVA around the conference), so this script adds
Google Scholar / arXiv search links and flags dataset/benchmark and document/RAG papers by title.

Output: BMVC26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | All | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python bmvc_scraper.py --year 2026
"""
import re, sys, argparse, urllib.parse as up
import requests
import pandas as pd
from bs4 import BeautifulSoup

HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}
TITLE_KW = re.compile(r"\b(?:dataset|datasets|benchmark|benchmarks|benchmarking|corpus)\b|\w+bench\b", re.I)
VDU_RAG_KW = re.compile(
    r"document|\bdoc|\bPDF\b|\bOCR\b|layout|\btable|\bchart|infographic|slide|screenshot|text[- ]rich|"
    r"handwrit|scene text|text spotting|script recognition|tamper|forgery|retriev|\bRAG\b|[A-Za-z]RAG\b", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2026)
    Y = ap.parse_args().year
    url = f"https://bmvc{Y}.bmva.org/programme/accepted_papers/"
    r = requests.get(url, headers=HEAD, timeout=60)
    if r.status_code != 200:
        sys.exit(f"HTTP {r.status_code} for {url} -> send a screenshot.")
    soup = BeautifulSoup(r.text, "html.parser")
    rows = []
    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        if len(td) >= 2 and td[0].get_text(strip=True).isdigit():
            t = " ".join(td[1].get_text(" ", strip=True).split())
            rows.append({"ID": int(td[0].get_text(strip=True)), "Title": t})
    if not rows:
        open("bmvc_debug.html", "w", encoding="utf-8").write(r.text)
        sys.exit("0 papers parsed (page saved as bmvc_debug.html) -> upload it here.")
    stated = re.search(r"of which\s+(\d+)\s+papers were accepted", soup.get_text(" "))
    df = pd.DataFrame(rows).drop_duplicates("ID").sort_values("ID").reset_index(drop=True)
    df["Scholar_Search"] = df.Title.map(lambda t: "https://scholar.google.com/scholar?q=" + up.quote_plus(f'"{t}"'))
    df["arXiv_Search"] = df.Title.map(lambda t: "https://arxiv.org/search/?searchtype=title&query=" + up.quote_plus(t))
    df["Type"] = df.Title.map(lambda t: "Dataset" if TITLE_KW.search(t) else "Method")
    ds, other = df[df.Type == "Dataset"], df[df.Type == "Method"]
    cand = df[df.Title.str.contains(VDU_RAG_KW)]
    summary = pd.DataFrame({"Item": ["Papers on official page", "Official number stated on page",
                                     "Dataset/Benchmark (title)", "Other", "VDU/RAG candidates (title)", "Source"],
                            "Value": [len(df), stated.group(1) if stated else "n/a", len(ds), len(other),
                                      len(cand), url]})
    with pd.ExcelWriter(f"BMVC{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
        for name, t in [("Dataset_Papers", ds), ("Other_Papers", other), ("VDU_RAG_Candidates", cand), ("All", df)]:
            t.reset_index(drop=True).rename(lambda i: i + 1).to_excel(xw, sheet_name=name, index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(max(len(str(c.value or "")) for c in col) + 2, 70)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
