#!/usr/bin/env python3
"""
Result tables from the arXiv HTML version of each paper (clean rows/columns, real headers),
instead of the PDF (where merged cells and multi-row headers break apart).
Input : method_datasets.xlsx   Output: score_tables_html.xlsx
   Index sheet: table_id, method key, arXiv id, caption, benchmarks seen
   T001...    : each table with its real header rows
Usage (Colab):
  !pip install requests pandas lxml openpyxl beautifulsoup4
  !python score_tables_html.py
"""
import re, io, time
import requests, pandas as pd
from bs4 import BeautifulSoup

TARGET = ["ViDoRe", "ViDoSeek", "MMLongBench", "LongDocURL", "SlideVQA", "MP-DocVQA", "DUDE", "M3DocVQA",
          "PaperTab", "FetaTab", "PaperText", "OpenDocVQA", "VisR-Bench", "MMDocIR", "REAL-MM-RAG", "InfoVQA",
          "ChartQA", "ArxivQA", "TabFQuAD", "DocVQA", "VisDoMBench", "FinRAGBench-V", "DocBench", "MRAG-Bench",
          "MIRACL-Vision", "MMEB", "nDCG"]
TPAT = re.compile("|".join(re.escape(t) for t in TARGET), re.I)
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}


def main():
    meta = pd.read_excel("method_datasets.xlsx")
    meta = meta[meta["arxiv_id"].notna() & (meta["title_match"] >= 0.8)]
    index, grids, n, nohtml = [], {}, 0, []
    for i, r in enumerate(meta.itertuples(), 1):
        base = re.sub(r"v\d+$", "", str(r.arxiv_id))
        html = None
        for url in (f"https://arxiv.org/html/{r.arxiv_id}", f"https://arxiv.org/html/{base}"):
            try:
                resp = requests.get(url, headers=HEAD, timeout=90)
                if resp.status_code == 200 and "<table" in resp.text:
                    html = resp.text; break
            except requests.RequestException:
                pass
        if html is None:
            nohtml.append(r.key); print(f"[{i}] {r.key}: no HTML version"); continue
        soup = BeautifulSoup(html, "lxml")
        kept = 0
        for fig in soup.select("figure.ltx_table"):
            cap = " ".join(fig.find("figcaption").get_text(" ", strip=True).split()) if fig.find("figcaption") else ""
            for tab in fig.find_all("table"):
                try:
                    df = pd.read_html(io.StringIO(str(tab)), header=None)[0]
                except Exception:
                    continue
                flat = cap + " " + " ".join(df.astype(str).fillna("").values.ravel())
                seen = sorted(set(m.group(0) for m in TPAT.finditer(flat)))
                if not seen:
                    continue
                n += 1; kept += 1; tid = f"T{n:03d}"
                cols = df.columns
                hdr = [list(l) for l in zip(*cols)] if isinstance(cols, pd.MultiIndex) else [list(cols)]
                if all(isinstance(c, int) for c in hdr[0]):
                    hdr = []                                   # no real header row
                body = df.astype(object).where(df.notna(), "").values.tolist()
                grids[tid] = pd.DataFrame(hdr + body)
                index.append({"table_id": tid, "key": r.key, "title": r.title, "arxiv_id": r.arxiv_id,
                              "caption": cap[:500], "benchmarks_seen": ", ".join(seen)})
        print(f"[{i}/{len(meta)}] {r.key}: {kept} tables")
        time.sleep(3)
    with pd.ExcelWriter("score_tables_html.xlsx", engine="openpyxl") as xw:
        pd.DataFrame(index).to_excel(xw, sheet_name="Index", index=False)
        pd.DataFrame({"no_html_version": nohtml}).to_excel(xw, sheet_name="No_HTML", index=False)
        for tid, g in grids.items():
            g.to_excel(xw, sheet_name=tid, index=False, header=False)
    print(f"DONE -> score_tables_html.xlsx ({n} tables; {len(nohtml)} papers without HTML)")


if __name__ == "__main__":
    main()
