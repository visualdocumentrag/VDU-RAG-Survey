#!/usr/bin/env python3
"""
NeurIPS COMPLETE accepted-paper scraper (official source: neurips.cc virtual site), any year
-------------------------------------------------------------------------------------------
Same system that worked for ICML 2026 / ICLR 2026. Use --year 2025 (NeurIPS 2026 papers are
not public before its virtual site opens; author notification was 24 Sep 2026).

Steps: 1) download the official data file (no login)
       2) remove duplicate Oral/Spotlight event rows (same paper listed twice)
       3) if the file has no abstracts, read each paper's neurips.cc page (parallel, ~15-25 min)
Output: NeurIPS25_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests beautifulsoup4 pandas openpyxl
  !python neurips_scraper.py --year 2025        # full (with abstracts)
  !python neurips_scraper.py --year 2025 --no-abstract
"""
import re, sys, json, time, argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

SITE = "https://neurips.cc"
DATA = SITE + "/static/virtual/data/neurips-{}-orals-posters.json"   # year filled in main()
OFFICIAL_TOTAL = "check official blog"
HEAD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
WORKERS = 6

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
    r"(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG|late interaction|multi-vector|token (?:pruning|compression)",
    re.I)

S = requests.Session(); S.headers.update(HEAD)


def get(url, tries=4):
    for i in range(tries):
        try:
            r = S.get(url, timeout=60)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    return None


def rank(decision):
    d = decision.lower()
    return 3 if "oral" in d else 2 if "spotlight" in d else 1


def load_rows():
    r = get(DATA)
    if r is None:
        sys.exit("Could not download " + DATA + "  -> send a screenshot.")
    raw = r.json()
    json.dump(raw, open("neurips_raw.json", "w"))
    items = raw.get("results", raw if isinstance(raw, list) else [])
    if items:
        print("  fields in data file:", sorted(items[0].keys()))
    papers = {}
    for it in items:
        et = str(it.get("eventtype") or it.get("event_type") or "")
        if et and not re.search(r"poster|oral|spotlight", et, re.I):
            continue
        title = " ".join(str(it.get("name") or "").split())
        if not title:
            continue
        url = str(it.get("paper_url") or it.get("sourceurl") or "")
        m = re.search(r"openreview\.net/forum\?id=([\w-]+)", url)
        orid = m.group(1) if m else ""
        if re.match(r"20\d\d-", orid):      # placeholder id used for Oral/Spotlight events
            orid = ""
        key = re.sub(r"\W", "", title.lower())
        dec = str(it.get("decision") or et)
        vs = str(it.get("virtualsite_url") or "")
        vs = SITE + vs if vs.startswith("/") else vs
        abstract = ""
        for k, v in it.items():
            if "abstract" in k.lower() and isinstance(v, str) and len(v) > len(abstract):
                abstract = v
        au = it.get("authors") or []
        au = ", ".join(a.get("fullname", "") if isinstance(a, dict) else str(a) for a in au)
        new = {"Title": title, "Authors": au, "Decision": dec,
               "Topic": str(it.get("topic") or ""),
               "Paper_Link": f"https://openreview.net/forum?id={orid}" if orid else vs,
               "PDF_Link": f"https://openreview.net/pdf?id={orid}" if orid else "",
               "NeurIPS_Page": vs, "Abstract": " ".join(BeautifulSoup(abstract, "html.parser")
                                                      .get_text(" ").split())}
        old = papers.get(key)
        if old is None:
            papers[key] = new
        else:  # merge duplicate event rows: keep real OpenReview id, best decision, longest abstract
            if not old["PDF_Link"] and new["PDF_Link"]:
                old["Paper_Link"], old["PDF_Link"] = new["Paper_Link"], new["PDF_Link"]
            if rank(new["Decision"]) > rank(old["Decision"]):
                old["Decision"] = new["Decision"]
            if len(new["Abstract"]) > len(old["Abstract"]):
                old["Abstract"] = new["Abstract"]
            if not old["NeurIPS_Page"]:
                old["NeurIPS_Page"] = new["NeurIPS_Page"]
    return list(papers.values()), len(items)


def page_abstract(url):
    time.sleep(0.2)
    r = get(url, tries=3)
    if r is None:
        return url, None
    soup = BeautifulSoup(r.text, "html.parser")
    for sel in ["#abstractExample", "#abstract", "div.abstract-text-inner", "div.abstract",
                "[id*=abstract]", "[class*=abstract]"]:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 80:
            return url, " ".join(el.get_text(" ", strip=True).split())
    for name in ["citation_abstract", "description", "og:description"]:
        m = soup.find("meta", attrs={"name": name}) or soup.find("meta", attrs={"property": name})
        if m and m.get("content") and len(m["content"]) > 80:
            return url, " ".join(m["content"].split())
    return url, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-abstract", action="store_true")
    ap.add_argument("--year", type=int, default=2025)
    args = ap.parse_args()
    global DATA
    DATA = DATA.format(args.year)
    Y = args.year

    print(f"Downloading NeurIPS {Y} data file: {DATA}")
    rows, n_items = load_rows()
    df = pd.DataFrame(rows)
    print(f"  {n_items} event rows -> {len(df)} unique papers (official: {OFFICIAL_TOTAL})")

    missing = df["Abstract"].eq("")
    failed = 0
    if missing.any() and not args.no_abstract:
        todo = [u for u in df.loc[missing, "NeurIPS_Page"] if u]
        print(f"Reading {len(todo)} paper pages for abstracts ({WORKERS} parallel) ...")
        got = {}
        for rnd in range(2):
            nxt = []
            with ThreadPoolExecutor(WORKERS) as ex:
                for k, f in enumerate(as_completed([ex.submit(page_abstract, u) for u in todo]), 1):
                    u, ab = f.result()
                    (nxt.append(u) if ab is None else got.__setitem__(u, ab))
                    if k % 300 == 0:
                        print(f"  round {rnd+1}: {k}/{len(todo)}")
            todo = nxt
            if not todo:
                break
            print(f"  {len(todo)} failed, retrying in 30s ...")
            time.sleep(30)
        failed = len(todo)
        df.loc[missing, "Abstract"] = df.loc[missing, "NeurIPS_Page"].map(got).fillna("")

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

    dec = df["Decision"].value_counts()
    no_abs = int(df["Abstract"].eq("").sum())
    summary = pd.DataFrame({
        "Item": ["Unique accepted papers", "Official total"] + [f"  {k}" for k in dec.index] +
                ["Dataset/Benchmark papers", "Other papers", "VDU/RAG candidates (check by hand)",
                 "Papers WITHOUT abstract", "Abstract pages FAILED", "Source"],
        "Value": [len(df), OFFICIAL_TOTAL] + list(dec.values) +
                 [len(ds), len(other), len(cand), no_abs, failed, DATA]})
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other, cand = clean(ds), clean(other), clean(cand)
    with pd.ExcelWriter(f"NeurIPS{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
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
