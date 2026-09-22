# Contributing

Thank you for helping keep this list complete and correct.

## Adding a paper

1. Fork the repository and create a branch.
2. Add one row to the right section of `README.md` (and of the matching page under `pages/`) in this format:

   ```
   |[Title](Paper link)|Venue Year|[Code](Code link)|
   ```

3. If the paper reports results on a specific content channel (text, layout, tables, figures, equations, forms, stamps, typography), add it to that channel's page under `pages/channels/`.
4. Add the matching row to the CSV in `data/`.
5. Open a pull request that states the channel(s) and the benchmark the paper reports on.

## Inclusion criteria

A paper is added when it (C1) retrieves from a document collection or a region of a document page, (C2) reports a quantitative result on a named benchmark or contributes a benchmark, dataset or metric, and (C3) is peer-reviewed or an archival preprint. Works before 2020 are added only as lineage for a channel (C4).

## Corrections

Every field must trace to the original paper. If a link, venue or number is wrong, open an issue with the source.
