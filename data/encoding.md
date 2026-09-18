# What encoder families preserve and destroy

Every cell here is a **judgement**, so every cell carries the work it
rests on. A cell we could not ground is left blank rather than filled by
inference — an uncited judgement in a table like this is the easiest thing
in a survey to challenge and the hardest to defend afterwards.

| Family | Preserves | Destroys |
|---|---|---|
| **OCR → text** | reading text; word order within a block An Overview of the Tesseract OCR Engine TrOCR: Transformer-Based Optical Charact | column order; cell adjacency; anything non-textual [Defining the Problem: The Impact of OCR ](https://doi.org/10.1016/j.ipm.2025.104368) [When Good OCR Is Not Enough: Benchmarkin](https://doi.org/10.18653/v1/2026.acl-industry.60) OCR Hinders RAG: Evaluating the Cascadin |
| **Structured parsing** | text, layout, tables, formulas and reading order, **each reported separately** [PaddleOCR-VL: Boosting Multilingual Docu](https://arxiv.org/abs/2510.14528) [dots.ocr: Multilingual Document Layout P](https://arxiv.org/abs/2512.02498) | typography; stamps; figure content beyond a caption |
| **Layout-aware LM** | bounding boxes; reading order LayoutLM: Pre-training of Text and Layou A Bounding Box is Worth One Token: Inter | content **type**: it knows where a block is, not that the block is a table |
| **Screenshot, single vector** | global page appearance Unifying Multimodal Retrieval via Docume VisRAG: Vision-based Retrieval-augmented | fine text; cell adjacency; anything below the pooled resolution |
| **Multi-vector visual** | patch-level appearance ColPali: Efficient Document Retrieval wi | channel identity: matching is spatial rather than semantic [Reproducibility, Replicability, and Insi](https://doi.org/10.1145/3726302.3730285) |
| **Compressed visual** | whatever survives the pruning budget DocKylin: A Large Multimodal Model for V [DocPruner: A Storage-Efficient Framework](https://arxiv.org/abs/2509.23883) | **unreported** — no work states which channels are dropped Token Pruning in Multimodal Large Langua Are We Using the Right Benchmark: An Eva |
| **Graph-structured** | relations the parser emitted Graph-based Document Structure Analysis [MonkeyOCR: Document Parsing with a Struc](https://arxiv.org/abs/2506.05218) | relations it did not; the pixels behind every node |
| **Parse-informed multi-vector** | the **units** the parser returns [Beyond the Grid: Layout-Informed Multi-V](https://arxiv.org/abs/2603.01666) [LMS-Retrieval: Layout-Aware, Modality-Aw](https://doi.org/10.1007/978-3-032-36039-7_8) | the label on them: the index stores a vector, not a type |

---

## Two rows that should be read together

**Structured parsing** reports text, tables, formulas and reading order
*separately*. That establishes per-channel reporting is practical rather
than aspirational, and it is what makes the channel-aware score of the
survey a proposal rather than a wish.

**Compressed visual** reports nothing at the channel level at all. Five
compression papers, and not one states which channels survive a given
budget — so a scheme that destroys seals and preserves body text is
indistinguishable, under current evaluation, from one that does the
reverse.

## The last row was corrected after verification

It previously read *structural labels carried into the index*, which would
have contradicted the survey's own claim on the facing page. ColParse runs
a parser and embeds the **regions** the parser returns, fusing those
sub-image embeddings with a global page vector: parsing output reaches the
index as a choice of *units*, not as a label riding alongside them.

The parser knows the region is a table; the index stores a vector.
