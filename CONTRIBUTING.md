# Contributing

Thank you for helping keep this list complete and correct.

## Add a paper

Open a pull request that adds one line to the right section of `README.md`, using this format:

```
* [Venue Year] **Title** [[arXiv](https://arxiv.org/abs/XXXX.XXXXX)][[DOI](https://doi.org/...)]
```

Please follow three rules, which the survey itself follows.

1. **Real links only.** Every entry needs an arXiv, DOI or proceedings link that resolves.
2. **Venue as published.** Use the peer-reviewed venue if the paper has one; otherwise write `arXiv`.
3. **Channels are claims.** A method is placed under a channel, or in a cell of [`data/matrix.md`](data/matrix.md), only if the paper **reports a result** on that channel.

## Add a result

Add a row to [`data/results_record.csv`](data/results_record.csv). Read each value from the paper that reports it, never from another paper's table, and fill `reported_in` and `source_location` so the value can be checked.

## Correct an entry

Open an issue with the entry, what is wrong, and the source that shows the correct value.
