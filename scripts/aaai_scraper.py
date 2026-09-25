#!/usr/bin/env python3
"""
AAAI COMPLETE paper scraper, any year: --year 2025 (Vol. 39) / --year 2026 (Vol. 40)  (source: ojs.aaai.org)
-----------------------------------------------------------------------------------
Output:
  AAAI26_papers.xlsx  -> Sheet 1 "Dataset_Papers", Sheet 2 "Other_Papers", Sheet 3 "Summary"
  AAAI26_dataset_papers.csv
  AAAI26_other_papers.csv

Usage:
  pip install requests beautifulsoup4 pandas openpyxl
  python aaai_scraper.py --year 2025              # fast: title-based classification
  python aaai_scraper.py --year 2025 --abstract   # thorough: title + abstract (4000+ extra requests, slow)
"""
import re, sys, time, argparse
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

BASE = "https://ojs.aaai.org/index.php/AAAI"
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}
DELAY = 1.0  # polite delay (seconds) between requests

# Dataset / benchmark keywords (case-insensitive)
TITLE_KW = re.compile(
    r"\b(dataset|data set|datasets|benchmark|benchmarks|benchmarking|corpus|corpora|"
    r"testbed|test suite|leaderboard)\b|\w+bench\b|\bbench\w*",
    re.I)
ABSTRACT_KW = re.compile(
    r"(we (introduce|present|propose|release|construct|build|curate|collect)"
    r"[^.]{0,80}\b(dataset|benchmark|corpus)\b)|"
    r"(new|novel|large-scale|first)[^.]{0,40}\b(dataset|benchmark|corpus)\b",
    re.I)


def get(url, tries=4):
    for i in range(tries):
        try:
            r = requests.get(url, headers=HEAD, timeout=40)
            if r.status_code == 200:
                return r.text
            if r.status_code == 404:   # page does not exist -> no retry
                return None
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    print(f"  !! FAILED: {url}")
    return None


def find_vol_issues(vol, first_id, scan_to):
    """
    Scan issue IDs directly (archive-page layout is unreliable).
    Vol. 40 No. 1 = issue 683 (verified). Keep every issue whose page title says 'Vol. 40'.
    """
    issues, misses_after_last = {}, 0
    for iid in range(first_id, scan_to + 1):
        html = get(f"{BASE}/issue/view/{iid}", tries=2)
        title = ""
        if html:
            t = BeautifulSoup(html, "html.parser").find("title")
            title = " ".join(t.get_text(" ", strip=True).split("|")[0].split()) if t else ""
        if re.search(r"Vol\.?\s*%d\b" % vol, title):
            issues[str(iid)] = title
            misses_after_last = 0
            print(f"  + {iid}: {title}")
        elif issues:
            misses_after_last += 1
            if misses_after_last >= 15:   # 15 non-matching IDs in a row -> finished
                break
        time.sleep(DELAY)
    return issues


def parse_issue(issue_id, issue_title):
    html = get(f"{BASE}/issue/view/{issue_id}")
    if not html:
        return [], False
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    track = ""
    # Walk the document in order so every paper keeps its track (section) name
    for el in soup.find_all(["h2", "h3"]):
        if el.name == "h2":
            track = el.get_text(" ", strip=True)
            continue
        a = el.find("a", href=re.compile(r"/article/view/\d+$"))
        if not a:
            continue
        summary = el.find_parent("div", class_=re.compile("obj_article_summary")) or el.parent
        authors = summary.find(class_=re.compile("authors"))
        pages = summary.find(class_=re.compile("pages"))
        pdf = summary.find("a", class_=re.compile("pdf"))
        if pdf is None:  # fallback: first galley link whose text is PDF
            pdf = next((g for g in summary.find_all("a", href=re.compile(r"/article/view/\d+/\d+"))
                        if "pdf" in g.get_text(strip=True).lower()), None)
        rows.append({
            "Title": " ".join(a.get_text(" ", strip=True).split()),
            "Authors": " ".join(authors.get_text(" ", strip=True).split()) if authors else "",
            "Track": track,
            "Issue": issue_title,
            "Pages": pages.get_text(strip=True) if pages else "",
            "Paper_Link": a["href"],
            "PDF_Link": pdf["href"] if pdf else "",
        })
    return rows, True


def get_abstract(url):
    html = get(url)
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    ab = soup.find(class_=re.compile(r"item abstract|abstract"))
    return " ".join(ab.get_text(" ", strip=True).split()) if ab else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abstract", action="store_true", help="also check abstracts (slow)")
    ap.add_argument("--year", type=int, default=2026)
    args = ap.parse_args()

    Y = args.year; VOL = Y - 1986                       # AAAI-25 = Vol. 39, AAAI-26 = Vol. 40
    START = {2025: 615, 2026: 683}.get(Y, 560)          # verified: Vol.39 No.13 = issue 636, Vol.40 No.1 = 683
    EXPECT = {2025: 28, 2026: 48}.get(Y)                # official number of issues
    print(f"Finding AAAI-{Y % 100} (Vol. {VOL}) issues ...")
    issues = find_vol_issues(VOL, START, START + 160)
    if not issues:
        sys.exit(f"No Vol. {VOL} issues found — check internet / site layout.")
    print(f"  {len(issues)} issues found (official: {EXPECT})."
          + ("" if len(issues) == EXPECT else f"  !! NOT {EXPECT} — check before trusting the list!"))

    all_rows, failed = [], []
    for n, (iid, ititle) in enumerate(sorted(issues.items(), key=lambda x: int(x[0])), 1):
        print(f"[{n}/{len(issues)}] {ititle}")
        rows, ok = parse_issue(iid, ititle)
        if not ok:
            failed.append(ititle)
        print(f"     -> {len(rows)} papers")
        all_rows.extend(rows)
        time.sleep(DELAY)

    df = pd.DataFrame(all_rows).drop_duplicates(subset="Paper_Link").reset_index(drop=True)

    df["Match_Reason"] = df["Title"].apply(lambda t: "title" if TITLE_KW.search(t) else "")
    if args.abstract:
        print("Checking abstracts (this takes a while) ...")
        abstracts = []
        for i, url in enumerate(df["Paper_Link"], 1):
            abstracts.append(get_abstract(url))
            if i % 100 == 0:
                print(f"  {i}/{len(df)}")
            time.sleep(DELAY)
        df["Abstract"] = abstracts
        mask = (df["Match_Reason"] == "") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
        df.loc[mask, "Match_Reason"] = "abstract"

    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    ds.index += 1
    other.index += 1

    ds.to_csv(f"AAAI{Y % 100}_dataset_papers.csv", index_label="No")
    other.to_csv(f"AAAI{Y % 100}_other_papers.csv", index_label="No")

    summary = pd.DataFrame({
        "Item": ["Issues scraped", "Issues FAILED", "Total papers", "Dataset/Benchmark papers",
                 "Other papers", "Classification mode", "Source"],
        "Value": [len(issues), ", ".join(failed) or "None", len(df), len(ds), len(other),
                  "title + abstract" if args.abstract else "title only",
                  f"https://ojs.aaai.org/index.php/AAAI/issue/archive (Vol. {VOL})"],
    })
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other = clean(ds), clean(other)
    with pd.ExcelWriter(f"AAAI{Y % 100}_papers.xlsx", engine="openpyxl") as xw:
        ds.to_excel(xw, sheet_name="Dataset_Papers", index_label="No")
        other.to_excel(xw, sheet_name="Other_Papers", index_label="No")
        summary.to_excel(xw, sheet_name="Summary", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                width = min(max(len(str(c.value or "")) for c in col) + 2, 80)
                ws.column_dimensions[col[0].column_letter].width = width

    print("\nDONE")
    print(summary.to_string(index=False))
    if failed:
        print("\n!! Some issues failed — re-run the script to fill the gap.")


if __name__ == "__main__":
    main()
