# Checklist: designing and reporting a VDU-RAG system (paper Fig. 10)

[Paper Fig. 10 (HD)](figures_tables.md#fig-10)

[Back to README](../README.md#paper-to-repository-map)

## Design (paper Sec. 9.4 and 6.3)

- [ ] Which channels do the queries need? Parse for text, tables, formulas and reading order; use pixels for stamps, typography and non-chart figures.
- [ ] Tens of pages: place them in context. Thousands: retrieve.
- [ ] Choose the unit per query: page, region or element.
- [ ] Budget the index: multi-vector costs about *v* times a single vector (*v* = vectors per page).
- [ ] Is the script covered by the retriever's training data?
- [ ] Return an evidence box with every answer.

## Report (18 items, paper Sec. 11)

|Group|Items|
|---|---|
|**R** Retrieval|backbone and size; depth K; index type; page resolution|
|**P** Parsing|parser and version; structure used or characters only; chunking|
|**E** Evaluation|metric implementation; benchmark version; split; runs; variance|
|**C** Corpus|source and license; size in pages; channel composition|
|**A** Artifacts|code; weights; license on both|

## Evaluate

Report CARS per channel (paper Eq. 7; see [metrics](metrics.md)) beside nDCG.

[Back to README](../README.md#paper-to-repository-map)
