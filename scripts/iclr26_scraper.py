#!/usr/bin/env python3
"""
ICLR 2026 COMPLETE accepted-paper scraper (official source: OpenReview API v2)
------------------------------------------------------------------------------
One request per 1000 papers, abstracts included -> finishes in about 1 minute.

Output: ICLR26_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python iclr26_scraper.py
  (If OpenReview answers 403, the script asks for your OpenReview email + password;
   the password is typed hidden and is only sent to api2.openreview.net.)
"""
import re, sys, time
import requests
import pandas as pd

API = "https://api2.openreview.net/notes"
VENUE_ID = "ICLR.cc/2026/Conference"          # accepted papers carry exactly this venueid
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey)"}

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
    r"(?-i:\bRAG\b|[A-Za-z]RAG\b)|GraphRAG", re.I)


def val(content, key):
    v = content.get(key, {})
    v = v.get("value", "") if isinstance(v, dict) else v
    return ", ".join(v) if isinstance(v, list) else (v or "")


TOKEN = {}


def api_get(params):
    h = dict(HEAD)
    if TOKEN.get("t"):
        h["Authorization"] = "Bearer " + TOKEN["t"]
    return requests.get(API, params=params, headers=h, timeout=60)


def login():
    """OpenReview blocks anonymous API calls from cloud servers (HTTP 403) -> log in."""
    import os, getpass
    user = os.environ.get("OR_USER") or input("OpenReview email: ").strip()
    pw = os.environ.get("OR_PASS") or getpass.getpass("OpenReview password (hidden): ")
    r = requests.post("https://api2.openreview.net/login", json={"id": user, "password": pw},
                      headers=HEAD, timeout=60)
    if r.status_code != 200 or "token" not in r.json():
        print("  OpenReview says:", r.text[:300])
        sys.exit("Login failed. If you normally sign in with Google, first set a password at "
                 "https://openreview.net/reset , then run again.")
    TOKEN["t"] = r.json()["token"]
    print("  logged in OK")


def fetch_all():
    notes, offset, logged = [], 0, False
    while True:
        for attempt in range(4):
            try:
                r = api_get({"content.venueid": VENUE_ID, "limit": 1000, "offset": offset})
                if r.status_code == 200:
                    break
                print(f"  HTTP {r.status_code}")
                if r.status_code in (401, 403) and not logged:
                    print("  OpenReview needs a login from this server.")
                    login(); logged = True
                    continue
            except requests.RequestException as e:
                print("  network error:", e)
            time.sleep(5 * (attempt + 1))
        else:
            sys.exit(f"FAILED at offset {offset}. Send a screenshot.")
        batch = r.json().get("notes", [])
        notes.extend(batch)
        print(f"  offset {offset}: +{len(batch)}  (total {len(notes)})")
        if len(batch) < 1000:
            return notes
        offset += 1000
        time.sleep(1)



VIRTUAL_JSON = "https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json"


def from_virtual_site():
    """Source 1 (no login): the official ICLR virtual-site data file."""
    try:
        r = requests.get(VIRTUAL_JSON, headers=HEAD, timeout=120)
        if r.status_code != 200:
            print(f"  virtual site: HTTP {r.status_code}")
            return None
        items = r.json().get("results", [])
    except Exception as e:
        print("  virtual site not usable:", e)
        return None
    rows, seen = [], set()
    for it in items:
        et = str(it.get("eventtype") or it.get("event_type") or "")
        if et and not re.search(r"poster|oral|spotlight", et, re.I):
            continue
        url = it.get("paper_url") or it.get("sourceurl") or ""
        m = re.search(r"id=([\w-]+)", url)
        key = m.group(1) if m else (it.get("name") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        au = it.get("authors") or []
        au = ", ".join(a.get("fullname", "") if isinstance(a, dict) else str(a) for a in au)
        kw = it.get("keywords") or []
        rows.append({
            "Title": " ".join(str(it.get("name", "")).split()),
            "Authors": au,
            "Decision": it.get("decision") or et,
            "Primary_Area": it.get("topic") or "",
            "Keywords": ", ".join(kw) if isinstance(kw, list) else str(kw),
            "Paper_Link": f"https://openreview.net/forum?id={key}" if m else (it.get("virtualsite_url") or ""),
            "PDF_Link": f"https://openreview.net/pdf?id={key}" if m else "",
            "Abstract": " ".join(str(it.get("abstract") or "").split()),
        })
    print(f"  virtual site: {len(rows)} papers")
    return rows or None


def main():
    print("Source 1: ICLR virtual site (no login) ...")
    rows = from_virtual_site()
    SRC = VIRTUAL_JSON
    if not rows:
        print("Source 2: OpenReview API ...")
        SRC = f"OpenReview API v2, content.venueid={VENUE_ID}"
        rows = []
        for n in fetch_all():
            c = n.get("content", {})
            pdf = val(c, "pdf")
            rows.append({
                "Title": " ".join(val(c, "title").split()),
                "Authors": val(c, "authors"),
                "Decision": val(c, "venue"),
                "Primary_Area": val(c, "primary_area"),
                "Keywords": val(c, "keywords"),
                "Paper_Link": f"https://openreview.net/forum?id={n.get('forum') or n.get('id')}",
                "PDF_Link": ("https://openreview.net" + pdf) if pdf.startswith("/") else
                            f"https://openreview.net/pdf?id={n.get('id')}",
                "Abstract": " ".join(val(c, "abstract").split()),
            })
    df = pd.DataFrame(rows).drop_duplicates(subset="Paper_Link").reset_index(drop=True)
    if df.empty:
        sys.exit("0 papers returned. Send a screenshot.")

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
    summary = pd.DataFrame({
        "Item": ["Total accepted papers"] + [f"  {k}" for k in dec.index] +
                ["Dataset/Benchmark papers", "Other papers", "VDU/RAG candidates (check by hand)",
                 "Papers without abstract", "Source"],
        "Value": [len(df)] + list(dec.values) +
                 [len(ds), len(other), len(cand), int((df["Abstract"] == "").sum()),
                  SRC]})
    with pd.ExcelWriter("ICLR26_papers.xlsx", engine="openpyxl") as xw:
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
