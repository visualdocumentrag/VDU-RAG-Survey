# Reporting checklist

Eighteen items in five clusters. Copy this into your submission and answer
every line; a blank is a finding about the paper, not about the checklist.

The threshold that motivates it: **independent reports of the same method,
on the same benchmark and metric, differ by more than the margins
separating successive publications.** A claimed improvement below that
spread is not thereby false, but it is not established by the record
either, and a reader has no way to tell which.

## Retrieval configuration

- [ ] Backbone and parameter count
- [ ] Retrieval depth (top-$K$)
- [ ] Index type: single-vector, multi-vector, graph, hybrid
- [ ] Input page resolution

## Parsing configuration

- [ ] OCR or parsing engine, **with version**
- [ ] Whether structural output was used, or only the character stream
- [ ] Chunking strategy and chunk size

## Evaluation

- [ ] Metric, with its exact definition or an implementation link
- [ ] Benchmark **version** — v1, v2 and v3 are three benchmarks
- [ ] Split, and whether it is the public one
- [ ] Number of runs averaged
- [ ] Variance across runs

## Corpus

- [ ] Source and licence
- [ ] Size, in **pages** or in documents, stated as one or the other
- [ ] Channel composition, if known

## Artefacts

- [ ] Public code
- [ ] Released weights
- [ ] Explicit licence on both

---

**The last two evaluation items are the ones almost nobody reports**, and
both bear directly on whether a reported difference is a method difference
or measurement noise. If you report nothing else from this list, report
those.
