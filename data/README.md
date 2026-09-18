# The record

Three files. The third column of `results_record.csv` is the one that
does not exist anywhere else.

## `screened_pool.csv`

Every record retained after title-and-abstract screening, with the
decision and, where excluded at full text, the criterion it failed.
286 rows.

Criteria are defined in §III-C of the paper:

- **C1** retrieval corpus is a document collection, retrieval unit is a
  page or page region
- **C2** reports a quantitative result on a named benchmark, or
  contributes a benchmark, dataset or metric
- **C3** peer-reviewed, or an archival preprint cited by a
  peer-reviewed work in the pool
- **C4** published 2020–2026

## `results_record.csv`

One row per (method, benchmark, metric, value) tuple.

**`REPORTED_IN` is the point of this file.** It records the paper the
value was *read from*, which is not always the paper that produced it.
No comparable table carries this field, and it is the reason the
disagreement in Fig. 7 has never been measured before.

Two conventions that matter:

- `benchmark_version` is a separate column because ViDoRe v1, v2 and v3
  are three benchmarks, not one. Version drift within a name is a real
  hazard here.
- Blank cells are values the reporting paper **did not state**, not
  values we failed to transcribe. That distinction is what §XI-E
  measures.

## `datasets.csv`

The benchmark registry behind Table 6.

**`scale_provenance` is either PRIMARY or SECONDARY.** PRIMARY means
the query and document counts were read from the introducing paper's
own abstract. SECONDARY means they came from a downstream table and
have not been checked.

Three widely circulated figures were checked against their source and
all three disagreed. One of them — a benchmark circulating as 471
queries over 226 documents against its own abstract's 35,000 over
1,200 — reached this survey's first-pass record from a competing
survey's table, and was caught only on returning to the abstract.
The flag exists so that no reader has to take a number on trust.

---

## Reporting an error

Open an issue. The record is meant to be checked, and a correction is
more useful to us than a citation.
