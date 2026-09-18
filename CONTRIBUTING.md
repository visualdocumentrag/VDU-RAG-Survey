# Contributing

## Reporting an error in the record

Open an issue. Include the file, the row, and the source you checked
against — ideally the introducing paper's own abstract or the
publisher's record rather than a downstream table.

Errors of this kind are the reason the record exists. Three widely
circulated dataset figures were checked against their sources and all
three disagreed; one of them had reached our own first-pass record
from a competing survey's table. A correction is more useful to us
than a citation.

## Adding a paper

Open a pull request against `data/screened_pool.csv` with the row
filled in, and add the entry to the matching section of `README.md`.

The inclusion criteria are in §III-C of the paper:

- **C1** the retrieval corpus is a document collection and the
  retrieval unit is a page or page region
- **C2** the work reports a quantitative result on a named benchmark,
  or contributes a benchmark, dataset or metric
- **C3** peer-reviewed, or an archival preprint cited by a
  peer-reviewed work already in the pool
- **C4** published between 2020 and 2026

A paper that fails one of these is not a worse paper. It is a
different paper, and the criteria are stated so that its absence is a
selection rather than an oversight.

## Adding a result

`data/results_record.csv` needs the `REPORTED_IN` field filled: the
paper you read the value from, which is not always the paper that
produced it. A row without it cannot be used for the disagreement
analysis, which is the whole reason the file exists.
