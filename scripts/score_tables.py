#!/usr/bin/env python3
"""
Collect the RESULT TABLES of every method paper, so reported scores can be read into a
VLM-survey-style performance table (methods x benchmarks).
Input : method_datasets.xlsx (from method_datasets.py; gives the arXiv id of each method)
Output: score_tables.xlsx
   - Index         : one row per extracted table (method key, arXiv id, page, caption, benchmarks seen)
   - T001, T002 ...: each table as a grid, exactly as extracted from the PDF
Only tables that mention at least one target benchmark are kept.
Usage (Colab):
  !pip install requests pymupdf pandas openpyxl
  !python score_tables.py
"""
import re, io, time
import requests, pandas as pd
import pymupdf

TARGET = ["ViDoRe", "ViDoSeek", "MMLongBench-Doc", "MMLongBench", "LongDocURL", "SlideVQA", "MP-DocVQA",
          "DUDE", "M3DocVQA", "PaperTab", "FetaTab", "PaperText", "OpenDocVQA", "VisR-Bench", "MMDocIR",
          "REAL-MM-RAG", "InfoVQA", "ChartQA", "ArxivQA", "TabFQuAD", "DocVQA", "VisDoMBench", "FinRAGBench-V",
          "DocBench", "MRAG-Bench", "MIRACL-Vision", "MMEB"]
TPAT = re.compile("|".join(re.escape(t) for t in sorted(TARGET, key=len, reverse=True)), re.I)
CAP = re.compile(r"^\s*(Table|TABLE)\s*[\dIVX]+[.:]", re.M)


def caption_near(page, bbox):
    """Text block right above (or below) the table that starts with 'Table N'."""
    best = ""
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, txt = b[:5]
        if CAP.search(txt) and (abs(y1 - bbox[1]) < 120 or abs(y0 - bbox[3]) < 60):
            best = " ".join(txt.split())[:300]
    return best


def main():
    meta = pd.read_excel("method_datasets.xlsx")
    meta = meta[meta["arxiv_id"].notna() & (meta["title_match"] >= 0.8)]
    index, grids, n = [], {}, 0
    for i, r in enumerate(meta.itertuples(), 1):
        try:
            pdf = requests.get(f"https://arxiv.org/pdf/{r.arxiv_id}", timeout=120).content
            doc = pymupdf.open(stream=io.BytesIO(pdf), filetype="pdf")
        except Exception as e:
            print(f"[{i}] {r.key}: download failed ({e})"); continue
        kept = 0
        for pno, page in enumerate(doc, 1):
            try:
                tabs = page.find_tables()
            except Exception:
                continue
            for t in tabs.tables:
                grid = t.extract()
                flat = " ".join(" ".join(str(c or "") for c in row) for row in grid)
                cap = caption_near(page, t.bbox)
                seen = sorted(set(m.group(0) for m in TPAT.finditer(flat + " " + cap)))
                if not seen:
                    continue
                n += 1; kept += 1
                tid = f"T{n:03d}"
                grids[tid] = pd.DataFrame(grid)
                index.append({"table_id": tid, "key": r.key, "title": r.title, "arxiv_id": r.arxiv_id,
                              "page": pno, "caption": cap, "benchmarks_seen": ", ".join(seen),
                              "rows": len(grid), "cols": len(grid[0]) if grid else 0})
        print(f"[{i}/{len(meta)}] {r.key}: {kept} result tables")
        time.sleep(3)
    with pd.ExcelWriter("score_tables.xlsx", engine="openpyxl") as xw:
        pd.DataFrame(index).to_excel(xw, sheet_name="Index", index=False)
        for tid, g in grids.items():
            g.to_excel(xw, sheet_name=tid, index=False, header=False)
    print(f"DONE -> score_tables.xlsx ({n} tables)")


if __name__ == "__main__":
    main()
