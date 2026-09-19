# Reporting checklist (18 items)

Copy this block into your paper or supplementary material and answer every line. Each item is a column of [`results_record.csv`](results_record.csv), so a paper that answers it can be compared with its predecessors directly.

```markdown
## Retrieval
- [ ] Backbone and parameter count
- [ ] Retrieval depth (top-K)
- [ ] Index type: single-vector, multi-vector, graph or hybrid
- [ ] Input page resolution
## Parsing
- [ ] OCR or parsing engine, with version
- [ ] Structural output used, or character stream only
- [ ] Chunking strategy and chunk size
## Evaluation
- [ ] Metric, with its exact definition or implementation link
- [ ] Benchmark version (v1, v2 and v3 are different benchmarks)
- [ ] Split, and whether it is the public one
- [ ] Number of runs averaged
- [ ] Variance across runs
## Corpus
- [ ] Source and license
- [ ] Size, in pages or in documents, stated as one or the other
- [ ] Channel composition, if known
## Artifacts
- [ ] Public code
- [ ] Released weights
- [ ] Explicit license on both
```
