#!/usr/bin/env python3
"""Add a paper to the record and rebuild the tables.

    python3 scripts/add_paper.py

Asks for the fields one at a time, appends to data/references.csv, and
regenerates README.md and docs/groups.json so the site and the list stay
in step. Nothing is invented: the venue, the year and the identifier are
what you type, and the script refuses a row with a missing one.
"""
import csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(ROOT, 'data', 'references.csv')

GROUPS = [
 ('Surveys','surveys'),
 ('Plain text','channels'), ('Layout structure','channels'),
 ('Tables','channels'), ('Figures and charts','channels'),
 ('Equations','channels'), ('Form fields','channels'),
 ('Stamps and seals','channels'), ('Typography','channels'),
 ('Pre-2024 lineage','lineage'),
 ('Screenshot embedding','methods'), ('Late interaction','methods'),
 ('End-to-end visual RAG','methods'), ('Region- and layout-level','methods'),
 ('Agentic','methods'), ('Query rewriting and reranking','methods'),
 ('Chunking and text encoding','indexing'),
 ('Storage, pruning, compression','indexing'),
 ('Graph-structured indexes','indexing'),
 ('OCR quality and robustness','ocr'), ('Long context vs retrieval','ocr'),
 ('Benchmarks and datasets','benchmarks'),
 ('Multilingual and script coverage','benchmarks'),
 ('Metrics and evaluation','evaluation'),
 ('Adjacent: knowledge-based VQA','adjacent'),
]

def ask(label, required=True):
    while True:
        v = input(f"  {label}: ").strip()
        if v or not required: return v
        print("    required")

def main():
    rows = list(csv.DictReader(open(REFS)))
    keys = {r['key'] for r in rows}
    print(f"\n{len(rows)} papers in the record.\n")

    title  = ask("Title")
    author = ask("Authors  (Surname, Given and Surname, Given)")
    venue  = ask("Venue    (CVPR, ICDAR, TPAMI, or 'arXiv preprint')")
    year   = ask("Year")
    if not re.fullmatch(r'(19|20)\d\d', year):
        sys.exit("  a four-digit year, please")
    ident  = ask("DOI or arXiv id")
    arxiv  = ident if re.fullmatch(r'\d{4}\.\d{4,5}', ident) else ''
    doi    = '' if arxiv else ident
    pages  = ask("Pages    (blank if none)", required=False)

    print()
    for i,(g,_) in enumerate(GROUPS, 1): print(f"  {i:>2}. {g}")
    g, sec = GROUPS[int(ask("\n  Section number")) - 1]

    # key: first surname + year + first title word
    surname = re.split(r'[,\s]', author.strip())[0].lower()
    word = re.sub(r'[^a-z]', '', title.split()[0].lower())[:10]
    key = f"{surname}{year}{word}"
    n = 2
    while key in keys:
        key = f"{surname}{year}{word}{n}"; n += 1

    rows.append(dict(key=key, title=title, authors=author, venue=venue,
                     year=year, pages=pages, doi=doi, arxiv=arxiv,
                     preprint='yes' if 'arXiv preprint' in venue else 'no',
                     group=g, section=sec))
    with open(REFS, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"\n  added as {key}  ({len(rows)} papers)")

    os.system(f'python3 {os.path.join(ROOT,"scripts","rebuild.py")}')

if __name__ == '__main__':
    main()
