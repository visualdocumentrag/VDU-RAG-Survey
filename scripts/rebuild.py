#!/usr/bin/env python3
"""Regenerate README.md and docs/groups.json from data/references.csv.

Run after editing the CSV by hand, or let scripts/add_paper.py call it.
The paper list, the venue coverage table and the searchable site are all
derived from that one file, so they cannot drift apart.
"""
import csv, json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT, 'data', 'references.csv'))))

SECTIONS = [
 ('surveys', 'Surveys', 'Surveys',
  "Every survey of this literature or its neighbours, with the axis each organises by. Read them down: pipeline stage, role of the MLLM, LLM capability, task family, modality, QA task. **None is page content.**",
  ['Surveys'], {}),
 ('channels', 'Channels', 'Channels',
  "The eight content types a page carries. They are not a partition: they overlap, and the overlap is what the survey formalises.",
  ['Plain text', 'Layout structure', 'Tables', 'Figures and charts', 'Equations',
   'Form fields', 'Stamps and seals', 'Typography'],
  {'Stamps and seals': "**Roughly ten papers across forty years, one dataset released in 2025, and no retrieval system that evaluates on this channel at all.** The thinness is not an artefact of our search; it is the state of the field.",
   'Typography': "**One annotated corpus exists.** One is a sharper finding than none — the channel *is* annotatable, and has never been retrieved over.",
   'Equations': "Two metrics return **opposite verdicts** on the same pair of formula-recognition systems."}),
 ('lineage', 'Pre-2024 lineage', 'Lineage',
  "Retrieval over document images is two decades older than the current literature suggests, and the unit throughout was the word, the formula or the region — never the page.",
  ['Pre-2024 lineage'],
  {'Pre-2024 lineage': "Question answering over a document *collection* was posed at ICDAR in 2021 — **four years before the visual-RAG literature rediscovered the task**."}),
 ('methods', 'Methods', 'Methods',
  "Grouped by paradigm. Read the years down the region-level group: every system there appeared in 2025 or later, against a page-level literature beginning in 2024.",
  ['Screenshot embedding', 'Late interaction', 'End-to-end visual RAG',
   'Region- and layout-level', 'Agentic', 'Query rewriting and reranking'],
  {'Region- and layout-level': "Every system here appeared in 2025 or later. Retrieval granularity coarsened to the page in 2024 and has only begun to return."}),
 ('indexing', 'Encoding and indexing', 'Indexing',
  "What happens to a page between parsing and the index, and what it costs to store.",
  ['Chunking and text encoding', 'Storage, pruning, compression', 'Graph-structured indexes'],
  {'Storage, pruning, compression': "Two halves measuring different quantities: pruning reports **storage** against accuracy, hybrid retrieval reports **compute**. No work reports both with accuracy."}),
 ('ocr', 'Does OCR still matter?', 'OCR',
  "Four groups, four venues that do not usually read each other, reported the same thing between 2025 and 2026.",
  ['OCR quality and robustness', 'Long context vs retrieval'],
  {'OCR quality and robustness': "The agreement is not that OCR is bad — every one reports accurate recognition. It is that **character-level accuracy is the wrong measurement**, because what breaks retrieval is what recognition *discards*."}),
 ('benchmarks', 'Benchmarks and datasets', 'Benchmarks',
  "Every benchmark in the record. Per-channel coverage is in [`data/datasets.md`](data/datasets.md).",
  ['Benchmarks and datasets', 'Multilingual and script coverage'],
  {'Benchmarks and datasets': "**Stamps and typography are absent from every retrieval benchmark here.** A channel no benchmark annotates cannot be measured, and a channel that cannot be measured will not improve."}),
 ('evaluation', 'Metrics and evaluation', 'Metrics',
  "The instruments the field measures with, and the work questioning whether they measure the right thing.",
  ['Metrics and evaluation'], {}),
 ('adjacent', 'Adjacent work', 'Adjacent',
  "Knowledge-based VQA over natural images: the corpus is external world knowledge rather than the document collection, so we treat it as adjacent rather than in scope.",
  ['Adjacent: knowledge-based VQA'], {}),
]

CHANNEL_OF = {
 'Plain text': 'Text', 'Layout structure': 'Layout', 'Tables': 'Tables',
 'Figures and charts': 'Figures', 'Equations': 'Equations',
 'Form fields': 'Forms', 'Stamps and seals': 'Stamps', 'Typography': 'Typography',
}

JOURNAL_TAGS = {"IEEE TPAMI", "TPAMI", "IJCV", "IEEE TIP", "TIP", "IEEE TMM",
                "TMM", "CVIU", "Pattern Recognition", "ACM TOIS", "IP&M",
                "TACL", "JMLR", "AIJ", "IEEE TNNLS", "KBS",
                "Information Sciences", "ACM TIST", "ESWA", "IEEE Access",
                "IJDAR", "MTAP", "AI Review", "FnT", "IJPRAI"}

by = {}
for r in rows:
    by.setdefault(r['group'], []).append(r)

def link(r):
    if r.get('arxiv'):
        return f"https://arxiv.org/abs/{r['arxiv']}"
    if r.get('doi'):
        return f"https://doi.org/{r['doi'].strip('{}')}"
    return ''

def table(g):
    rs = sorted(by.get(g, []), key=lambda r: (-int(r['year'] or 0), r['title']))
    if not rs:
        return "*No entries yet.* **[➕ Add the first](../../issues/new?template=add-paper.yml)**"
    cat = CHANNEL_OF.get(g, '')
    head = ("| Paper | Venue | Type | Year |"
            + (" Channel |" if cat else "") + " Link |")
    sep = "|---|:-:|:-:|:-:|" + (":-:|" if cat else "") + ":-:|"
    out = [head, sep]
    for r in rs:
        u = link(r)
        t = f"[{r['title']}]({u})" if u else r['title']
        v = r.get('venue_tag') or '–'
        kind = ("preprint" if v == 'preprint'
                else "journal" if v in JOURNAL_TAGS else "conf.")
        c = f" {cat} |" if cat else ""
        l = f"[link]({u})" if u else "–"
        out.append(f"| {t} | {v} | {kind} | {r['year']} |{c} {l} |")
    return '\n'.join(out)

# ---- venue coverage: every venue searched, and what it yielded ----
VENUES = [
 "CVPR", "ICCV", "ECCV", "ACM MM", "WACV", "ACL", "EMNLP", "NAACL",
 "SIGIR", "CIKM", "The Web Conference", "COLING", "NeurIPS", "ICLR",
 "AAAI", "IJCAI", "ICDAR", "KDD", "DAS", "RecSys", "IEEE TPAMI", "IJCV",
 "JMLR", "AIJ", "IEEE TIP", "IJDAR", "IEEE TMM", "ACM TOIS",
 "Pattern Recognition", "IP&M", "TACL", "Computational Linguistics",
 "IEEE TNNLS", "Neural Networks", "KBS", "CVIU", "Information Sciences",
 "ACM TIST", "ESWA", "IEEE Access",
]
seen = Counter(r['venue_tag'] for r in rows)
JOURNALS = {"IEEE TPAMI", "IJCV", "IEEE TIP", "IEEE TMM", "CVIU",
            "Pattern Recognition", "ACM TOIS", "IP&M", "TACL",
            "Computational Linguistics", "JMLR", "AIJ", "IEEE TNNLS",
            "Neural Networks", "KBS", "Information Sciences", "ACM TIST",
            "ESWA", "IEEE Access", "IJDAR"}
vt = ["| # | Venue | Type | Papers | Add |", "|:-:|---|:-:|:-:|:-:|"]
for i, v in enumerate(VENUES, 1):
    n = seen.get(v, 0)
    kind = "journal" if v in JOURNALS else "conference"
    mark = f"**{n}**" if n else "—"
    vt.append(f"| {i} | {v} | {kind} | {mark} | "
              f"[➕](../../issues/new?template=add-paper.yml) |")
other = sum(n for k, n in seen.items() if k not in set(VENUES) and k != 'preprint')
vt.append(f"| | Other venues | mixed | {other} | "
          f"[➕](../../issues/new?template=add-paper.yml) |")
vt.append(f"| | Preprints | preprint | {seen.get('preprint', 0)} | "
          f"[➕](../../issues/new?template=add-paper.yml) |")
venue_table = '\n'.join(vt)

# ---- groups.json for the site ----
secs = []
for sid, title, short, note, groups, find in SECTIONS:
    gg = []
    for g in groups:
        ks = [r['key'] for r in sorted(by.get(g, []),
              key=lambda r: (-int(r['year'] or 0), r['title']))]
        d = {'title': g, 'keys': ks}
        if g in find:
            d['finding'] = find[g]
        gg.append(d)
    secs.append({'id': sid, 'title': title, 'short': short, 'note': note, 'groups': gg})
json.dump({'sections': secs}, open(os.path.join(ROOT, 'docs', 'groups.json'), 'w'), indent=1)

# ---- menu ----
def slug(s):
    return re.sub(r'[^a-z0-9 -]', '', s.lower()).replace(' ', '-')

menu = []
for sid, title, short, note, groups, find in SECTIONS:
    menu.append(f"- [{title}](#{slug(title)})")
    if len(groups) > 1:
        for g in groups:
            menu.append(f"  - [{g}](#{slug(g)})")
menu.append("- [Venue coverage](#venue-coverage)")
menu.append("- [The released record](#the-released-record)")

# ---- body ----
body = ''
for sid, title, short, note, groups, find in SECTIONS:
    body += f"\n## {title}\n\n{note}\n"
    for g in groups:
        if len(groups) > 1:
            body += f"\n### {g}\n"
        if g in find:
            body += f"\n> {find[g]}\n"
        body += f"\n{table(g)}\n\n**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**\n"

n = len(rows)
recent = sum(1 for r in rows if r['year'] in ('2025', '2026'))

readme = open(os.path.join(ROOT, 'README.md')).read()
for tag, new in [('MENU', '\n'.join(menu)), ('PAPERS', body), ('VENUES', venue_table)]:
    a = readme.index(f'<!-- {tag}:START -->')
    b = readme.index(f'<!-- {tag}:END -->')
    readme = readme[:a] + f'<!-- {tag}:START -->\n' + new + '\n' + readme[b:]
readme = re.sub(r'\*\*\d+ papers, \d+ of them from 2025–26\.\*\*',
                f'**{n} papers, {recent} of them from 2025–26.**', readme)
open(os.path.join(ROOT, 'README.md'), 'w').write(readme)
print(f"rebuilt: {n} papers, {recent} from 2025-26, {len(VENUES)} venues listed")
