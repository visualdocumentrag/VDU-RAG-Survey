# Configuration settings, and how often they are disclosed

The argument here is the **pairing**, not either column alone.

- A setting that moves scores and is usually disclosed is fine: the field
  knows about it.
- A setting that moves scores little and goes unreported is harmless.
- A setting that **moves scores a lot and is disclosed rarely** is the
  field's largest reporting defect.

The two columns are not equally solid, and we mark which is which.
*Disclosure* is a count: did the reporting paper state this setting, yes
or no. *Association* is a reading of a record in which settings covary
with everything else — either an observed range across otherwise
comparable rows (†, ours, weak but ours) or an ablation the cited paper
ran (‡, stronger, but theirs).

We deliberately report ranges and counts rather than correlation
coefficients: an $r$ with no stated model would assume an independence
this record does not have.

| Setting | Assoc. with score | Disclosed |
|---|:-:|--:|
| **Retrieval** | | |
| Backbone / model size | | |
| Retrieval depth $K$ | | |
| Index type | | |
| Reranking stage | | |
| **Input** | | |
| Page resolution | | |
| OCR / parsing engine | | |
| Chunk size | | |
| **Generation and evaluation** | | |
| Reader model | | |
| Prompt template | | |
| Evaluation code version | | |
| Runs averaged | | |

---

## The two rows nobody reports

**Evaluation code version** and **runs averaged** are almost never stated,
and both bear directly on whether a reported difference is a method
difference or measurement noise. If a paper reports nothing else from this
list, those two are the ones to report.

A zero in the right-hand column for either is the most quotable number in
the table, and it should be published as a zero rather than dropped.

## Filling this table

The association can be estimated wherever a setting varies across
otherwise comparable rows of [`results_record.csv`](results_record.csv);
disclosure is a straightforward count over the same file. Sort within each
block by disclosure ascending once the numbers exist, so a reader can read
down the right-hand column and watch the reporting standard degrade.
