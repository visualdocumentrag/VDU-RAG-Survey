#!/usr/bin/env python3
"""
ICPR 2024 COMPLETE paper scraper (Kolkata, Dec 1-5, 2024)  -- there is NO ICPR 2025 (ICPR is biennial)
------------------------------------------------------------------------------------------------------
Official: LNCS 15301-15333 (33 volumes), 963 papers from 2,106 submissions.
Step 1: find all 33 volume DOIs on Crossref (search + 5 verified seeds).
Step 2: read every chapter DOI (<volume DOI>_1, _2, ...) from Crossref; OpenAlex fills abstracts.
Output: ICPR24_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Volumes | Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python icpr24_scraper.py        # ~10-15 minutes (about 1,000 chapter look-ups)
"""
import re, sys, time
import requests
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

SEEDS = {  # verified on SpringerLink
    "10.1007/978-3-031-78183-4": "Part VII", "10.1007/978-3-031-78383-8": "Part XXIV",
    "10.1007/978-3-031-78398-2": "Part XXVII", "10.1007/978-3-031-78104-9": "Part XXVIII",
    "10.1007/978-3-031-78125-4": "Part XXXII",
}
EXPECTED_VOLUMES = 33
OFFICIAL_FULL_PAPERS = 963
CROSSREF = "https://api.crossref.org/works/"
OPENALEX = "https://api.openalex.org/works"
HEAD = {"User-Agent": "Mozilla/5.0 (academic literature survey; mailto:survey@example.org)"}

TITLE_KW = re.compile(r"\b(?:dataset|datasets|benchmark|benchmarks|corpus|corpora)\b|\w+bench\b", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)"
    r"[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VDU_RAG_KW = re.compile(
    r"visually[- ]rich|document understanding|document question|document VQA|DocVQA|"
    r"long document|multi-?page|retrieval[- ]augmented|(?-i:\bRAG\b|[A-Za-z]RAG\b)|"
    r"vision[- ]language model|\bVLMs?\b|\bMLLMs?\b|\bLVLMs?\b|large multimodal|"
    r"information extraction|key information|document parsing|layout analysis|"
    r"\btable|\bchart|infographic|OCR-free|retrieval", re.I)


def get(url, params=None, tries=4):
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=HEAD, timeout=60)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404:
                return None
            print(f"  HTTP {r.status_code} {url}")
        except (requests.RequestException, ValueError) as e:
            print("  error:", e)
        time.sleep(4 * (i + 1))
    return "FAILED"


def find_volumes():
    vols = dict(SEEDS)
    for q in ["27th International Conference ICPR 2024 Kolkata India Proceedings Part",
              "Pattern Recognition ICPR 2024 Kolkata Proceedings"]:
        for offset in (0, 100):
            j = get("https://api.crossref.org/works",
                    {"query.bibliographic": q, "filter": "prefix:10.1007,from-pub-date:2024-10-01,until-pub-date:2025-03-31",
                     "rows": 100, "offset": offset})
            for w in (j if isinstance(j, dict) else {}).get("message", {}).get("items", []):
                sub = " ".join(w.get("subtitle") or [])
                doi = w.get("DOI", "").lower()
                m = re.search(r"ICPR 2024, Kolkata.*Proceedings, (Part [IVXL]+)", sub)
                if m and "_" not in doi:
                    vols[doi] = m.group(1)
            time.sleep(1)
    return vols


def read_volume(part, vdoi):
    rows, n, misses, failed = [], 1, 0, []
    while misses < 3 and n < 80:
        doi = f"{vdoi}_{n}"
        j = get(CROSSREF + doi)
        if j == "FAILED":
            failed.append(doi); misses = 0
        elif j is None:
            misses += 1
        else:
            misses = 0
            w = j.get("message", {})
            ab = re.sub(r"<[^>]+>", " ", w.get("abstract", "") or "")
            ab = re.sub(r"^\s*Abstract\s*", "", " ".join(ab.split()), flags=re.I)
            rows.append({"Part": part, "Chapter": n,
                         "Title": " ".join(" ".join(w.get("title") or [""]).split()),
                         "Authors": ", ".join(" ".join(filter(None, [a.get("given"), a.get("family")]))
                                              for a in w.get("author", [])),
                         "Pages": w.get("page", ""), "DOI": doi.lower(),
                         "Paper_Link": f"https://doi.org/{doi}", "Abstract": ab})
        n += 1
        time.sleep(0.3)
    print(f"  {part}: {len(rows)} chapters" + (f", FAILED {len(failed)}" if failed else ""))
    return rows, failed


def openalex_abstracts(dois):
    out = {}
    for k in range(0, len(dois), 50):
        j = get(OPENALEX, {"filter": "doi:" + "|".join(dois[k:k + 50]), "per-page": 50})
        for w in (j if isinstance(j, dict) else {}).get("results", []):
            inv = w.get("abstract_inverted_index") or {}
            pos = sorted((p, word) for word, ps in inv.items() for p in ps)
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            if d and pos:
                out[d] = " ".join(word for _, word in pos)
        time.sleep(0.3)
    return out


def main():
    print("Step 1: finding the 33 ICPR 2024 volumes on Crossref ...")
    vols = find_volumes()
    print(f"  {len(vols)} volumes found (official: {EXPECTED_VOLUMES})" +
          ("" if len(vols) == EXPECTED_VOLUMES else "  !! NOT 33 -> send a screenshot"))
    print("Step 2: reading chapters ...")
    rows, failed = [], []
    for vdoi, part in sorted(vols.items(), key=lambda x: x[1]):
        r, f = read_volume(part, vdoi)
        rows += r; failed += f
    if not rows:
        sys.exit("0 chapters -> send a screenshot.")
    df = pd.DataFrame(rows).drop_duplicates(subset="DOI").reset_index(drop=True)
    df["Kind"] = df["Title"].map(lambda t: "Competition" if re.search(r"\bcompetition\b", t, re.I) else "Paper")

    miss = df["Abstract"].eq("")
    if miss.any():
        print(f"{int(miss.sum())} abstracts missing -> OpenAlex ...")
        m = openalex_abstracts(list(df.loc[miss, "DOI"]))
        df.loc[miss, "Abstract"] = df.loc[miss, "DOI"].map(m).fillna("")

    df["Match_Reason"] = ""
    df.loc[df["Kind"].eq("Competition"), "Match_Reason"] = "competition"
    k = df["Match_Reason"].eq("") & df["Title"].str.contains(TITLE_KW)
    df.loc[k, "Match_Reason"] = "title"
    k = df["Match_Reason"].eq("") & df["Abstract"].str.contains(ABSTRACT_KW, na=False)
    df.loc[k, "Match_Reason"] = "abstract"

    ds = df[df["Match_Reason"] != ""].reset_index(drop=True)
    other = df[df["Match_Reason"] == ""].drop(columns=["Match_Reason"]).reset_index(drop=True)
    cand = df[(df["Title"] + " " + df["Abstract"]).str.contains(VDU_RAG_KW, na=False)].copy()
    cand.insert(0, "Type", cand["Match_Reason"].apply(lambda x: "Dataset" if x else "Method"))
    cand = cand.reset_index(drop=True)
    for t in (ds, other, cand):
        t.index += 1

    kc = df["Kind"].value_counts()
    summary = pd.DataFrame({
        "Item": ["Total chapters"] + [f"  {k}" for k in kc.index] +
                ["Official papers (963)", "Dataset/Benchmark/Competition", "Other papers",
                 "VDU/RAG candidates (check by hand)", "Papers WITHOUT abstract", "Chapters FAILED", "Source"],
        "Value": [len(df)] + list(kc.values) +
                 [OFFICIAL_FULL_PAPERS, len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()),
                  len(failed), "Crossref (Springer chapter DOIs) + OpenAlex"]})
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    ds, other, cand = clean(ds), clean(other), clean(cand)
    vol_df = pd.DataFrame([(p, d, int((df.Part == p).sum())) for d, p in vols.items()], columns=["Part", "Volume_DOI", "Chapters"]).sort_values("Part")
    with pd.ExcelWriter("ICPR24_papers.xlsx", engine="openpyxl") as xw:
        vol_df.to_excel(xw, sheet_name="Volumes", index=False)
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
        print("!! Failed chapter DOIs (run again):", *failed, sep="\n  ")


if __name__ == "__main__":
    main()
