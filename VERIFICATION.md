# Verification

Literature cut-off: **24 September 2026**. Every check below can be re-run with `python scripts/verify_repo.py` (add `--online` to open every GitHub link). [Back to README](README.md#verification)

## Paper and repository

| Check | Result |
|---|---|
| Works cited in the paper | 217, each in [data/references.csv](data/references.csv) with `CitedInPaper = yes` and in [data/vdu_rag.bib](data/vdu_rag.bib) |
| Works collected but not cited (page limit) | 74, listed in [pages/further_reading.md](pages/further_reading.md) and Part B of the [master list PDF](supplementary/Master_List.pdf) |
| Methods (paper Tables 4-5) | 73; name, venue, year, objective, index / unit, datasets, printed link and code equal to the paper tables ([pages/methods.md](pages/methods.md)) |
| Benchmarks (paper Table 8) | 25 channel-audited benchmarks; venue, year, language, scope, size, queries, metric, the eight channel marks, public flag and link equal to the paper table ([pages/datasets.md](pages/datasets.md)); 36 further benchmarks from 2025-2026 venues |
| EIOAR (paper Table 6) | 9 systems; encoder, index unit, operator, aggregator, reasoner and code equal to the paper table ([data/eioar.md](data/eioar.md)) |
| Scores (paper Table 9) | every value, footnote letter and printed link equal to the paper table ([pages/scores.md](pages/scores.md)) |
| Channel x paradigm matrix (paper Table 7) | equal to the [channel table](README.md#the-eight-channels) |
| Abstract and channel descriptions | word for word equal to the final paper text (abstract and Sec. 5) |
| Citations inside figures and tables | every work cited in Tables 1-9 and Figs. 1-11 is linked on the matching clickable page (including the notes of Tables 7 and 9) |
| Fig. 1 and Fig. 3 values | works per year (2020-2026: 5, 8, 14, 10, 19, 73, 67) and every PRISMA count equal to the data files |
| Reference numbers | [pages/paper_references.md](pages/paper_references.md) lists [1]-[217] exactly as numbered in the paper, and the works each section cites |
| Benchmarks cited only in the text | 21, listed with links in [pages/datasets.md](pages/datasets.md#3-other-benchmarks-and-datasets-cited-in-the-paper-21) |
| Figures 1-11 and Tables 1-9 | rendered at 400 dpi from the paper source, with the paper's citation numbers ([pages/figures_tables.md](pages/figures_tables.md)) |
| Counts stated in the paper | 42 venue-year lists, 78,352 records, 2,014 related, 73 methods, 61 benchmarks: equal to the data files |

## Venue lists

| Check | Result |
|---|---|
| Records per venue-year | equal to [data/venues/index.csv](data/venues/index.csv) for all 42 lists |
| Duplicate titles within a venue-year | none |
| Related papers | every one is in its complete list |
| Link domain | matches the venue in every complete list (CVF, ACL Anthology, AAAI, OpenReview, PMLR, ECVA, IJCAI, JMLR, DOI, Springer) |
| Complete-list pages | 78,352 rows, every title clickable |
| BMVC 2025, BMVC 2026, ICDAR 2026 | BMVC publishes no per-paper URL, and 119 of the 160 ICDAR 2026 papers had no Springer page at the cut-off; these titles open an arXiv title search, with a Google Scholar search beside them |

## Links

| Check | Result |
|---|---|
| Relative links and section anchors in all Markdown files | all resolve |
| GitHub code and project links | all open |
| References without a stable open page | 22 open a Google Scholar search and are labelled `Scholar search` in [data/references.csv](data/references.csv) |
| Publisher pages (CVF, ACL Anthology, OpenReview, AAAI, DOI, Springer, ACM) | checked for form, venue and year |

Please open an [issue](.github/ISSUE_TEMPLATE/correction.md) for any link or value that is wrong.
