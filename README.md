# Awesome Visual Document RAG: *Eight Channels, One Vector* [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<img src="./images/fig03_taxonomy.png" width="96%">

This is the companion repository of **Eight Channels, One Vector: A Survey of Retrieval-Augmented Generation for Visual Document Understanding**, a survey that organizes visual document retrieval by *what a page contains* rather than by pipeline stage.

*Under double-blind review at IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI). Author names and the paper link will be added after the review.*

![Papers](https://img.shields.io/badge/papers-194-blue) ![Methods](https://img.shields.io/badge/methods-33-orange) ![Cut-off](https://img.shields.io/badge/cut--off-31%20Aug%202026-lightgrey) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Menu

Every item opens its own page.

| Section | Page | Papers |
|---|---|:-:|
| **Start here** | [2026 highlights (peer-reviewed)](pages/2026-highlights.md) | 27 |
| | [Existing surveys](pages/surveys.md) | 17 |
| **Methods** | [Screenshot embedding (one vector per page)](pages/methods-1-screenshot-embedding.md) | 3 |
| **Methods** | [Late interaction (many vectors per page)](pages/methods-2-late-interaction.md) | 8 |
| **Methods** | [End-to-end visual document RAG](pages/methods-3-end-to-end-visual-document-rag.md) | 10 |
| **Methods** | [Region- and layout-level retrieval](pages/methods-4-region-and-layout-level-retrieval.md) | 7 |
| **Methods** | [Agentic document RAG](pages/methods-5-agentic-document-rag.md) | 5 |
| **History** | [Historical foundations (before 2020)](pages/history.md) | 17 |
| **Channel 1** | [Plain text and reading order](pages/channel-1-plain-text.md) | 12 |
| **Channel 2** | [Layout structure](pages/channel-2-layout.md) | 10 |
| **Channel 3** | [Tables](pages/channel-3-tables.md) | 6 |
| **Channel 4** | [Figures and charts](pages/channel-4-figures-and-charts.md) | 7 |
| **Channel 5** | [Equations](pages/channel-5-equations.md) | 4 |
| **Channel 6** | [Form fields](pages/channel-6-form-fields.md) | 5 |
| **Channel 7** | [Stamps and seals](pages/channel-7-stamps-and-seals.md) | 4 |
| **Channel 8** | [Typography](pages/channel-8-typography.md) | 5 |
| **Topics** | [Encoding, chunking, indexing and efficiency](pages/encoding-indexing-efficiency.md) | 8 |
| **Topics** | [Attribution, grounding and compression](pages/attribution-and-compression.md) | 8 |
| **Topics** | [Does OCR still matter?](pages/ocr-and-robustness.md) | 17 |
| **Topics** | [Datasets and benchmarks](pages/datasets-and-benchmarks.md) | 22 |
| **Topics** | [Metrics and evaluation](pages/metrics-and-evaluation.md) | 4 |
| **Topics** | [RAG and retrieval foundations](pages/foundations.md) | 13 |
| **Topics** | [Adjacent work (out of scope)](pages/adjacent-work.md) | 2 |
| **All papers** | [Full bibliography by year (2026 → 1984)](data/bibliography.md) | 194 |

## The eight channels

A page carries up to eight kinds of content at once, and they overlap. Retrieval encoders pool page regions without recording which channel each came from. Click a channel to open its paper list.

<img src="./images/fig01_channels.png" width="38%" align="right">

| # | Channel | Not required to survive pooling |
|:-:|---|---|
| 1 | [**Plain text and reading order**](pages/channel-1-plain-text.md) | reading order and block boundaries |
| 2 | [**Layout structure**](pages/channel-2-layout.md) | containment and neighbor relations |
| 3 | [**Tables**](pages/channel-3-tables.md) | cell adjacency and header scope |
| 4 | [**Figures and charts**](pages/channel-4-figures-and-charts.md) | the mapping from position to value |
| 5 | [**Equations**](pages/channel-5-equations.md) | nesting and operator scope |
| 6 | [**Form fields**](pages/channel-6-form-fields.md) | key–value binding |
| 7 | [**Stamps and seals**](pages/channel-7-stamps-and-seals.md) | authority and provenance; the content they overprint |
| 8 | [**Typography**](pages/channel-8-typography.md) | weight, slope and emphasis |

<br clear="right"/>

## Abstract

Document collections have outgrown what any model can read at once, so retrieval now decides what a model ever sees. Since 2024, visual document retrieval has made the page image the unit of retrieval, and existing surveys organize the resulting literature by where computation happens: pipeline stage, retrieval modality or task. None asks what the page contains. We organize the field by content channel. A page carries up to eight channels at once (text, layout, tables, figures, equations, form fields, stamps and typography), and they overlap rather than partition it, as when a stamp crosses a table. Retrieval encoders pool page regions without recording which channel each came from. We formalize the resulting loss as channel interference, a second-order interaction between channels, and show that late-interaction scoring produces it even between channels that do not overlap. A channel-by-paradigm matrix over 33 methods and a channel-coverage audit of retrieval benchmarks yield three findings. Stamps and typography have never been evaluated under any retrieval paradigm, and no retrieval benchmark annotates them. Work on OCR-based pipelines reaches the same failure from the other side: accurate recognition still harms retrieval when it discards structure. Page-level metrics can register neither. We therefore propose a channel-aware retrieval score and an 18-item reporting checklist, derive open problems directly from the empty cells of the matrix, and release every table, drawn from a pool of 1,778 records across 39 venues, with source-level provenance in this repository.

<img src="./images/fig02_timeline.png" width="96%">

*Four decades of document understanding and retrieval. The retrieved unit coarsened from words and formulas to whole pages; region-level retrieval returned only in 2026.*

## Data files

| File | Paper | Contents |
|---|---|---|
| [`datasets.md`](data/datasets.md) | Table 6 | channel coverage of 22 benchmarks and datasets |
| [`matrix.md`](data/matrix.md) | Table 5 | channel × paradigm matrix |
| [`methods.md`](data/methods.md) | Table 4 | the 33 methods |
| [`surveys.md`](data/surveys.md) | Table 1 | existing surveys and their axes |
| [`encoding.md`](data/encoding.md) | Table 3 | what encoder families preserve and lose |
| [`notation.md`](data/notation.md) | Table 2 | notation and the interference definition |
| [`checklist.md`](data/checklist.md) | Table 7 | 18-item reporting checklist, ready to copy |
| [`results_record.csv`](data/results_record.csv) | Sec. 11 | result file: one row per (method, benchmark, metric, value) with its source |
| [`venues.md`](data/venues.md) | Sec. 3 | per-venue screening counts |
| [`bibliography.md`](data/bibliography.md) | — | all references, by year |
| [`references.bib`](data/references.bib) | — | BibTeX of all references |

## News

* **2026-09** Repository released with the submission: 194 cited works, 33 methods, the channel × paradigm matrix, benchmark channel coverage, a result file with source for every value, and the 18-item reporting checklist.

## Contributing

Pull requests and issues are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md); every entry needs a real arXiv, DOI or proceedings link.

## Citation

```bibtex
@article{eightchannels2026,
  title   = {Eight Channels, One Vector: A Survey of Retrieval-Augmented Generation for Visual Document Understanding},
  author  = {Anonymous},
  journal = {Under review at IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2026}
}
```

## License

The lists and data files are released under [CC BY 4.0](LICENSE).
