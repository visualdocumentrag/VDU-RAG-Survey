#!/usr/bin/env python3
"""
arXiv 2026 preprints for Visual Document Understanding + Document RAG (official arXiv API)
------------------------------------------------------------------------------------------
Searches TITLE + ABSTRACT with topic-specific phrase queries, for papers first submitted in <year>.
Each paper is tagged with every topic it matched, deduplicated by arXiv ID (latest version kept),
and the author "comments" / journal_ref are kept -> shows "Accepted at CVPR 2026" etc.

Output: arXiv26_VDU_RAG.xlsx -> one sheet per topic + All_Unique + Dataset_Papers + Summary
Usage (Colab):
  !pip install requests pandas openpyxl
  !python arxiv_scraper.py                 # 2026, ~5-10 min (arXiv asks for 3 s between calls)
  !python arxiv_scraper.py --year 2025
"""
import re, sys, time, argparse
import xml.etree.ElementTree as ET
import requests
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

API = "https://export.arxiv.org/api/query"
HEAD = {"User-Agent": "academic-survey-script (mailto:survey@example.org)"}
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/"}
PAGE = 500
CATS = "(cat:cs.CV OR cat:cs.CL OR cat:cs.IR OR cat:cs.AI OR cat:cs.LG OR cat:cs.MM)"

TOPICS = {  # phrase lists; each phrase is searched in title AND abstract
    "1_VisualDoc_RAG": ["visual document retrieval", "visually rich document retrieval", "document RAG",
                        "multimodal document RAG", "visual RAG", "vision-based RAG", "VisRAG", "ColPali",
                        "ColQwen", "ViDoRe", "multimodal retrieval-augmented generation document",
                        "retrieval-augmented generation visually rich"],
    "2_VDU_DocQA": ["visually rich document", "visually-rich document", "document understanding",
                    "document visual question answering", "DocVQA", "document question answering",
                    "multi-page document", "long document understanding", "text-rich image",
                    "OCR-free document", "document VQA"],
    "3_Doc_Parsing_Layout_OCR": ["document parsing", "document layout analysis", "layout analysis document",
                                 "document image", "key information extraction", "visual information extraction",
                                 "PDF parsing", "document OCR", "table structure recognition"],
    "4_Chart_Table_Slide_Infographic": ["chart understanding", "chart question answering", "ChartQA",
                                        "infographic", "table image understanding", "slide understanding",
                                        "scientific figure understanding"],
    "5_MultiVector_LateInteraction": ["late interaction retrieval", "multi-vector retrieval",
                                      "ColBERT multimodal", "visual token pruning retrieval"],
}
TITLE_KW = re.compile(r"\b(?:dataset|datasets|benchmark|benchmarks|benchmarking|corpus)\b|\w+bench\b|\bbench\w*", re.I)
ABSTRACT_KW = re.compile(
    r"(?:we (?:introduce|present|propose|release|construct|build|curate|collect)[^.]{0,80}\b(?:dataset|benchmark|corpus)\b)|"
    r"(?:new|novel|large-scale|first)[^.]{0,40}\b(?:dataset|benchmark|corpus)\b", re.I)
VENUE = re.compile(r"\b(?:CVPR|ICCV|ECCV|WACV|ACCV|BMVC|NeurIPS|ICLR|ICML|AAAI|IJCAI|ACL|EMNLP|NAACL|EACL|COLING|"
                   r"SIGIR|KDD|WWW|CIKM|WSDM|MM|ICDAR|ICPR|TPAMI|IJCV|TIP|IJDAR|Pattern Recognition)\b[^,;.]{0,20}", re.I)


def fetch(query, start):
    params = {"search_query": query, "start": start, "max_results": PAGE,
              "sortBy": "submittedDate", "sortOrder": "descending"}
    for i in range(5):
        try:
            r = requests.get(API, params=params, headers=HEAD, timeout=120)
            if r.status_code == 200:
                return r.text
            print(f"    HTTP {r.status_code}, retry")
        except requests.RequestException as e:
            print("    error:", e)
        time.sleep(10 * (i + 1))
    return None


def parse(xml):
    root = ET.fromstring(xml)
    total = int(root.findtext("os:totalResults", "0", NS))
    out = []
    for e in root.findall("a:entry", NS):
        aid = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1]
        base = re.sub(r"v\d+$", "", aid)
        pdf = next((l.get("href") for l in e.findall("a:link", NS) if l.get("title") == "pdf"), "")
        out.append({"arXiv_ID": base, "Version": aid,
                    "Title": " ".join(e.findtext("a:title", "", NS).split()),
                    "Authors": ", ".join(a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)),
                    "First_Submitted": e.findtext("a:published", "", NS)[:10],
                    "Updated": e.findtext("a:updated", "", NS)[:10],
                    "Primary_Cat": (e.find("arxiv:primary_category", NS).get("term")
                                    if e.find("arxiv:primary_category", NS) is not None else ""),
                    "Comment": " ".join((e.findtext("arxiv:comment", "", NS) or "").split()),
                    "Journal_Ref": " ".join((e.findtext("arxiv:journal_ref", "", NS) or "").split()),
                    "Abstract": " ".join(e.findtext("a:summary", "", NS).split()),
                    "Paper_Link": f"https://arxiv.org/abs/{base}", "PDF_Link": pdf or f"https://arxiv.org/pdf/{base}"})
    return total, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2026)
    Y = ap.parse_args().year
    date = f"submittedDate:[{Y}01010000 TO {Y}12312359]"
    rows, log = [], []
    for topic, phrases in TOPICS.items():
        ors = " OR ".join(f'ti:"{p}" OR abs:"{p}"' for p in phrases)
        q = f"({ors}) AND {CATS} AND {date}"
        start, total, got = 0, None, 0
        print(f"== {topic}")
        while True:
            xml = fetch(q, start)
            if xml is None:
                print("  !! FAILED, rest of this topic skipped"); log.append((topic, "FAILED", got)); break
            total, items = parse(xml)
            for it in items:
                it["Topic"] = topic
            rows += items; got += len(items)
            print(f"  {got}/{total}")
            start += PAGE
            time.sleep(3.5)
            if not items or start >= total:
                break
        log.append((topic, total, got))
    if not rows:
        sys.exit("0 results -> send a screenshot.")

    df = pd.DataFrame(rows)
    df = df[df["First_Submitted"].str.startswith(str(Y))]
    topics = df.groupby("arXiv_ID")["Topic"].apply(lambda s: "; ".join(sorted(set(s))))
    uniq = df.sort_values("Updated").drop_duplicates("arXiv_ID", keep="last").drop(columns="Topic")
    uniq = uniq.merge(topics.rename("Topics"), left_on="arXiv_ID", right_index=True)
    uniq["Venue_Hint"] = (uniq["Comment"] + " " + uniq["Journal_Ref"]).map(
        lambda t: "; ".join(sorted(set(m.group(0).strip() for m in VENUE.finditer(t)))) if t.strip() else "")
    uniq["Type"] = "Method"
    uniq.loc[uniq.Title.str.contains(TITLE_KW) | uniq.Abstract.str.contains(ABSTRACT_KW), "Type"] = "Dataset"
    uniq = uniq.sort_values("First_Submitted", ascending=False).reset_index(drop=True)
    clean = lambda t: t.map(lambda v: ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v)
    uniq = clean(uniq)
    cols = ["Type", "Topics", "Title", "Authors", "First_Submitted", "Venue_Hint", "Comment", "Journal_Ref",
            "Primary_Cat", "Paper_Link", "PDF_Link", "arXiv_ID", "Abstract"]

    summary = pd.DataFrame({"Item": [f"Unique arXiv papers first submitted in {Y}"] +
                                    [f"  {t} (arXiv total / fetched)" for t, _, _ in log] +
                                    ["Dataset/Benchmark", "With a venue hint (accepted somewhere)", "Source"],
                            "Value": [len(uniq)] + [f"{a} / {b}" for _, a, b in log] +
                                     [int((uniq.Type == "Dataset").sum()), int(uniq.Venue_Hint.ne("").sum()),
                                      "export.arxiv.org API (cs.CV/CL/IR/AI/LG/MM), title+abstract phrase search"]})
    with pd.ExcelWriter(f"arXiv{Y % 100}_VDU_RAG.xlsx", engine="openpyxl") as xw:
        summary.to_excel(xw, sheet_name="Summary", index=False)
        uniq[cols].rename(lambda i: i + 1).to_excel(xw, sheet_name="All_Unique", index_label="No")
        uniq[uniq.Type == "Dataset"][cols].reset_index(drop=True).rename(lambda i: i + 1).to_excel(
            xw, sheet_name="Dataset_Papers", index_label="No")
        for t in TOPICS:
            sub = uniq[uniq.Topics.str.contains(t, regex=False)][cols].reset_index(drop=True)
            sub.rename(lambda i: i + 1).to_excel(xw, sheet_name=t[:31], index_label="No")
        for ws in xw.book.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = min(max(len(str(c.value or "")) for c in col) + 2, 70)
    print("\nDONE\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
