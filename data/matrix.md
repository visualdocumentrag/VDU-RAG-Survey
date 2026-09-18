# The channel × paradigm matrix

Eight channels against four system paradigms. **A blank cell means no
reported work**, not that the combination is impossible.

The inclusion rule matters more than the cell contents: *a method counts
in a cell only if it reports a result on that channel*. Not if it could in
principle, not if its benchmark happens to contain such content, not if
the authors mention it in passing. Under a looser rule every cell fills,
and the empty ones would mean nothing.

| Channel | OCR → LLM | MLLM-native | Text RAG | Visual / MM RAG |
|---|---|---|---|---|
| Plain text |   |   |   |   |
| Layout structure |   |   |   |   |
| Tables |   |   |   |   |
| Figures and charts |   |   |   |   |
| Equations |   |   |   | *(blank)* |
| Form fields |   |   |   |   |
| Stamps and seals | detection only, not retrieval | *(blank)* | *(blank)* | *(blank)* |
| Typography | recognition only, not retrieval | *(blank)* | *(blank)* | *(blank)* |

---

## The empty cells

**Stamps and seals** and **typography** are blank across all three
retrieval columns. What stands in the fourth is detection and recognition
— work that identifies a seal on a page, not work that finds the page
given a query about the seal.

Those rows are also the least explicable by difficulty: stamps have
detection systems going back to the 1990s and typography optical font
recognition going back further, and neither is hard in the sense that
formula structure is hard. What they lack is not technique but a
benchmark that annotates them.

Each blank names a channel, a paradigm, and therefore a specific
experiment: take a system of that paradigm, evaluate it on a resource
annotating that channel, and report what happens.
