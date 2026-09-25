#!/usr/bin/env python3
"""
JMLR COMPLETE paper scraper (official source: jmlr.org/papers/v<volume>)
------------------------------------------------------------------------
JMLR has no DOIs, so the official volume pages are read directly.
Year 2026 = end of Volume 26 (completed 2 Mar 2026) + Volume 27 (began 2 Mar 2026):
both volumes are read and only papers stamped ", 2026." are kept.

Output: JMLR26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python jmlr_scraper.py                 # JMLR 2026 (with abstracts, ~3-5 min)
  !python jmlr_scraper.py --year 2025
"""
import re, sys, time, argparse
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

BASE = "https://www.jmlr.org"
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}
TITLE_KW = re.compile(r"\b(?:dataset|datasets|benchmark|benchmarks|benchmarking|corpus)\b|\w+bench\b", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(r"document|\bOCR\b|layout|\bchart|\btable|retriev|(?-i:\bRAG\b)|multimodal|vision[- ]language|"
                        r"text[- ]rich|information extraction|late interaction|multi-vector", re.I)
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


def parse_volume(vol):
    html = get(f"{BASE}/papers/v{vol}/")
    if not html:
        print(f"  Volume {vol}: page not readable"); return []
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        info = " ".join(dd.get_text(" ", strip=True).split())
        m = re.search(r"\((\d+)\)\s*:\s*([\d\s\-−–]+),\s*(\d{4})", info)
        links = {a.get_text(strip=True).lower(): urljoin(BASE + f"/papers/v{vol}/", a["href"])
                 for a in dd.find_all("a", href=True)}
        au = dd.find("i") or dd.find("b")
        rows.append({"Title": " ".join(dt.get_text(" ", strip=True).split()),
                     "Authors": " ".join(au.get_text(" ", strip=True).split()) if au else info.split(";")[0],
                     "Volume": vol, "Paper_No": int(m.group(1)) if m else None,
                     "Pages": m.group(2).strip() if m else "", "Year": int(m.group(3)) if m else None,
                     "Paper_Link": links.get("abs", ""), "PDF_Link": links.get("pdf", ""),
                     "Code_Link": links.get("code", "")})
    print(f"  Volume {vol}: {len(rows)} papers on page")
    return rows


def abstract(url):
    if not url:
        return url, ""
    html = get(url, tries=3)
    if html is None:
        return url, None
    soup = BeautifulSoup(html, "html.parser")
    el = soup.select_one("p.abstract") or soup.select_one("#abstract") or soup.select_one(".abstract")
    if el is None:
        h = soup.find(lambda t: t.name in ("h3", "h2") and "abstract" in t.get_text(strip=True).lower())
        el = h.find_next("p") if h else None
    return url, " ".join(el.get_text(" ", strip=True).split()) if el else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2026)
    Y = ap.parse_args().year
    vols = [Y - 2000, Y - 1999]          # 2026 -> Vol. 26 (tail) + Vol. 27
    rows = []
    for v in vols:
        rows += parse_volume(v)
    df = pd.DataFrame(rows)
    if df.empty:
        sys.exit("0 papers -> send a screenshot.")
    no_year = int(df["Year"].isna().sum())
    df = df[df["Year"] == Y].drop_duplicates(subset=["Title", "Volume"]).reset_index(drop=True)
    print(f"Papers stamped {Y}: {len(df)}  (rows without a readable year: {no_year})")

    print("Reading abstracts ...")
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
    vc = df["Volume"].value_counts().sort_index()
    summary = pd.DataFrame({
        "Item": [f"Papers published in {Y}"] + [f"  from Volume {k}" for k in vc.index] +
                ["Dataset/Benchmark", "Other", "VDU/RAG candidates (check by hand)",
                 "Papers WITHOUT abstract", "Abstract pages FAILED", "Rows without readable year", "Source"],
        "Value": [len(df)] + list(vc.values) +
                 [len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()), failed, no_year,
                  f"{BASE}/papers/v{vols[0]}/ + v{vols[1]}/"]})
    with pd.ExcelWriter(f"JMLR{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
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
