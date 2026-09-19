# What encoder families preserve and lose

Table 3 of the survey.

| Family | Preserves | Loses | Evidence |
|---|---|---|---|
| **OCR → text** | reading text; word order within a block | column order; table cell adjacency; anything non-textual | An Overview of the Tesseract OCR Engine (ICDAR 2007); TrOCR (AAAI 2023); Defining the Problem (IP&M 2026); When Good OCR Is Not Enough (ACL 2026); OCR Hinders RAG (ICCV 2025) |
| **Structured parsing** | text, layout, tables, formulas, reading order, each reported separately | typography; stamps; figures other than charts | PaddleOCR-VL (arXiv 2025); dots.ocr (arXiv 2025) |
| **Layout-aware LM** | bounding boxes; reading order | typography; pixel content of figures and stamps | LayoutLM (KDD 2020); A Bounding Box is Worth One Token (Findings ACL 2025) |
| **Screenshot, single vector** | global page appearance | fine text; cell adjacency; anything below the pooled resolution | Unifying Multimodal Retrieval via Document Screenshot Embedding (EMNLP 2024); VisRAG (ICLR 2025) |
| **Multi-vector visual** | patch-level appearance | channel identity: matching follows appearance and position | ColPali (ICLR 2025); Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction (SIGIR 2025) |
| **Compressed visual** | whatever survives the pruning budget | unreported: no work states which channels are dropped | DocKylin (AAAI 2025); DocPruner (arXiv 2025); Token Pruning in Multimodal Large Language Models (Findings ACL 2025); Are We Using the Right Benchmark (ACL 2026) |
| **Graph-structured** | relations the parser emitted | relations it did not; the pixels behind every node | Graph-based Document Structure Analysis (ICLR 2025); MonkeyOCR (arXiv 2025) |
| **Parse-informed multi-vector** | the units the parser returns | the content-type label: units are kept, the label is not indexed | Beyond the Grid (arXiv 2026); LMS-Retrieval (ICDAR 2026) |
