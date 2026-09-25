#!/usr/bin/env python3
"""
CVPR COMPLETE paper scraper, any year (official source: openaccess.thecvf.com)
-------------------------------------------------------------------------
Covers: Main conference (CVPR2026) + Findings track (CVPR2026_findings).

Output:
  CVPR26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
  CVPR26_dataset_papers.csv, CVPR26_other_papers.csv

Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python cvpr_scraper.py --year 2025 --abstract   # thorough (parallel, ~20-40 min)
  !python cvpr_scraper.py --year 2025              # fast: title only (~2 min)
"""
import re, sys, time, argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
import requests
import pandas as pd
from bs4 import BeautifulSoup

ROOT = "https://openaccess.thecvf.com/"
TRACKS = {}   # filled in main() from --year
HEAD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
WORKERS = 4          # parallel downloads for abstracts (keep it moderate)
DELAY = 0.3          # pause per request inside each worker

TITLE_KW = re.compile(
    r"\b(dataset|data set|datasets|benchmark|benchmarks|benchmarking|corpus|corpora|"
    r"testbed|test suite|leaderboard)\b|\w+bench\b|\bbench\w*", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)"
    r"[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(
    r"\bdocument|\bDoc[A-Z0-9]|\bPDF\b|\bOCR\b|\blayout analysis|\blayout detection|"
    r"\btable (?:understanding|recognition|question|structure)|\bchart|\binfographic|"
    r"(?<!whole )\bslide|\bvisually[- ]rich|\btext[- ]rich|\bmulti-?page|\bscanned|"
    r"\bhandwrit|\bscene text|\btext recognition|\bformula recognition|\bmathematical expression|"
    r"\bscreenshot|\bGUI\b|retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|ColPali|ColQwen|"
    r"multimodal retrieval|visual retrieval", re.I)

session = requests.Session()
session.headers.update(HEAD)


def get(url, tries=4):
    for i in range(tries):
        try:
            r = session.get(url, timeout=40)
            if r.status_code == 200:
                return r.text
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    return None


def list_pages(track_dir):
    """Return every listing URL for a track: day=all first, else each day page."""
    landing = get(ROOT + track_dir)
    pages = [ROOT + track_dir + "?day=all"]
    if landing:
        soup = BeautifulSoup(landing, "html.parser")
        for a in soup.find_all("a", href=True):
            if "day=" in a["href"] and "day=all" not in a["href"]:
                pages.append(urljoin(ROOT, a["href"]))
    return list(dict.fromkeys(pages))


def parse_listing(html, track):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for dt in soup.find_all("dt", class_="ptitle"):
        a = dt.find("a", href=True)
        if not a:
            continue
        html_url = urljoin(ROOT, a["href"])
        dd1 = dt.find_next_sibling("dd")
        dd2 = dd1.find_next_sibling("dd") if dd1 else None
        authors = ""
        if dd1:
            names = [f.find("a").get_text(strip=True) for f in dd1.find_all("form") if f.find("a")]
            authors = ", ".join(names) if names else " ".join(dd1.get_text(" ", strip=True).split())
        pdf = supp = arxiv = ""
        if dd2:
            for l in dd2.find_all("a", href=True):
                t = l.get_text(strip=True).lower()
                if t == "pdf":
                    pdf = urljoin(ROOT, l["href"])
                elif t == "supp":
                    supp = urljoin(ROOT, l["href"])
                elif t == "arxiv":
                    arxiv = l["href"]
        rows.append({"Title": " ".join(a.get_text(" ", strip=True).split()),
                     "Authors": authors, "Track": track, "Paper_Link": html_url,
                     "PDF_Link": pdf, "Supp_Link": supp, "arXiv_Link": arxiv})
    return rows


def get_abstract(url):
    time.sleep(DELAY)
    html = get(url)
    if not html:
        return url, None
    div = BeautifulSoup(html, "html.parser").find(id="abstract")
    return url, (" ".join(div.get_text(" ", strip=True).split()) if div else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abstract", action="store_true")
    ap.add_argument("--year", type=int, default=2026)
    args = ap.parse_args()
    Y = args.year
    TRACKS.update({"Main": f"CVPR{Y}", "Findings": f"CVPR{Y}_findings"})  # Findings exists only from 2026

    all_rows, page_log = [], []
    for track, d in TRACKS.items():
        print(f"== {track} ({d}) ==")
        got_all = False
        for p in list_pages(d):
            if got_all and "day=all" not in p:
                break   # day=all already gave the full list
            html = get(p)
            rows = parse_listing(html, track) if html else []
            page_log.append((p, len(rows)))
            print(f"  {p} -> {len(rows)} papers")
            all_rows.extend(rows)
            if "day=all" in p and rows:
                got_all = True
            time.sleep(1)

    if not all_rows:
        sys.exit("No papers found. Site may be blocking requests -> try again later or run on your own PC.")

    df = pd.DataFrame(all_rows).drop_duplicates(subset="Paper_Link").reset_index(drop=True)
    print(f"\nUnique papers: {len(df)}  " + str(df['Track'].value_counts().to_dict()))

    df["Match_Reason"] = df["Title"].apply(lambda t: "title" if TITLE_KW.search(t) else "")
    failed = 0
    if args.abstract:
        print(f"Downloading {len(df)} abstracts with {WORKERS} parallel workers ...")
        abs_map = {}
        todo = list(df["Paper_Link"])
        for rnd in range(3):                      # up to 3 rounds for failed pages
            if not todo:
                break
            nxt = []
            with ThreadPoolExecutor(WORKERS) as ex:
                futs = [ex.submit(get_abstract, u) for u in todo]
                for k, f in enumerate(as_completed(futs), 1):
                    u, ab = f.result()
                    if ab is None:
                        nxt.append(u)
                    else:
                        abs_map[u] = ab
                    if k % 200 == 0:
                        print(f"  round {rnd+1}: {k}/{len(todo)}")
            todo = nxt
            if todo:
                print(f"  {len(todo)} failed, retrying after 30s ...")
                time.sleep(30)
        failed = len(todo)
        df["Abstract"] = df["Paper_Link"].map(abs_map).fillna("")
        mask = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
        df.loc[mask, "Match_Reason"] = "abstract"

    text = df["Title"] + " " + (df["Abstract"] if "Abstract" in df else "")
    cand = df[text.str.contains(VDU_RAG_KW, na=False)].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda m: "Dataset" if m else "Method"))

    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    for t in (ds, other):
        t.index += 1
    cand = cand.reset_index(drop=True); cand.index += 1

    ds.to_csv(f"CVPR{Y % 100}_dataset_papers.csv", index_label="No")
    other.to_csv(f"CVPR{Y % 100}_other_papers.csv", index_label="No")

    summary = pd.DataFrame({
        "Item": ["Total papers", "Main track", "Findings track", "Dataset/Benchmark papers",
                 "Other papers", "VDU/RAG candidates (keyword, check by hand)",
                 "Abstract download FAILED", "Classification mode", "Source"],
        "Value": [len(df), int((df.Track == "Main").sum()), int((df.Track == "Findings").sum()),
                  len(ds), len(other), len(cand),
                  failed if args.abstract else "n/a",
                  "title + abstract" if args.abstract else "title only",
                  f"https://openaccess.thecvf.com/CVPR{Y} (+ _findings if it exists)"]})
    with pd.ExcelWriter(f"CVPR{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
        ds.to_excel(xw, sheet_name="Dataset_Papers", index_label="No")
        other.to_excel(xw, sheet_name="Other_Papers", index_label="No")
        cand.to_excel(xw, sheet_name="VDU_RAG_Candidates", index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                w = min(max(len(str(c.value or "")) for c in col) + 2, 70)
                ws.column_dimensions[col[0].column_letter].width = w

    print("\nDONE")
    print(summary.to_string(index=False))
    if failed:
        print("\n!! Some abstracts failed — re-run with --abstract to fill the gap.")


if __name__ == "__main__":
    main()
