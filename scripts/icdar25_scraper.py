#!/usr/bin/env python3
"""
ICDAR 2025 COMPLETE paper scraper (Wuhan, Sept 16-21, 2025)
-----------------------------------------------------------
Official proceedings: LNCS 16023-16027, 5 volumes, 142 full papers (+ competition reports in Part V).
Workshops: LNCS 16225-16226 (46 papers) -> add --workshops.
Springer blocks Colab, so every chapter DOI (<volume DOI>_1, _2, ...) is read from Crossref,
which holds title, authors, pages and (usually) the abstract. OpenAlex fills missing abstracts.

Output: ICDAR25_papers.xlsx -> Dataset_Papers | Other_Papers | VDU_RAG_Candidates | Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python icdar25_scraper.py               # main conference (~3 min)
  !python icdar25_scraper.py --workshops   # + workshop papers
"""
import re, sys, time, argparse
import requests
import pandas as pd

MAIN = {  # eBook DOIs, verified on the official ICDAR 2025 proceedings page
    "Part I (LNCS 16023)":   "10.1007/978-3-032-04614-7",
    "Part II (LNCS 16024)":  "10.1007/978-3-032-04617-8",
    "Part III (LNCS 16025)": "10.1007/978-3-032-04624-6",
    "Part IV (LNCS 16026)":  "10.1007/978-3-032-04627-7",
    "Part V (LNCS 16027)":   "10.1007/978-3-032-04630-7",
}
WORKSHOPS = {
    "Workshops I (LNCS 16225)":  "10.1007/978-3-032-09368-4",
    "Workshops II (LNCS 16226)": "10.1007/978-3-032-09371-4",
}
OFFICIAL_FULL_PAPERS = 142
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


def read_volume(part, vdoi):
    rows, n, misses, failed = [], 1, 0, []
    while misses < 3 and n < 120:
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--workshops", action="store_true")
    args = ap.parse_args()
    vols = dict(MAIN, **(WORKSHOPS if args.workshops else {}))

    print("Reading chapters from Crossref ...")
    rows, failed = [], []
    for part, vdoi in vols.items():
        r, f = read_volume(part, vdoi)
        rows += r; failed += f
    if not rows:
        sys.exit("0 chapters -> send a screenshot.")
    df = pd.DataFrame(rows).drop_duplicates(subset="DOI").reset_index(drop=True)
    df["Kind"] = df.apply(lambda r: "Workshop" if r.Part.startswith("Workshops")
                          else ("Competition" if re.search(r"\bcompetition\b", r.Title, re.I) else "Full paper"), axis=1)

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
                ["Official full papers (main conf.)", "Dataset/Benchmark/Competition", "Other papers",
                 "VDU/RAG candidates (check by hand)", "Papers WITHOUT abstract", "Chapters FAILED", "Source"],
        "Value": [len(df)] + list(kc.values) +
                 [OFFICIAL_FULL_PAPERS, len(ds), len(other), len(cand), int(df["Abstract"].eq("").sum()),
                  len(failed), "Crossref (Springer chapter DOIs) + OpenAlex"]})
    with pd.ExcelWriter("ICDAR25_papers.xlsx", engine="openpyxl") as xw:
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
