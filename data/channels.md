# Channels

One table per channel: what the work *does*, what it was measured on,
and why it matters.

`Brief description` and `Highlight` are our reading of each paper, not
quotations. **Scores are deliberately absent**: a number without the
exact benchmark version, split and metric is not comparable, and the
survey's own meta-analysis is about precisely that. Reported values
live in [`results_record.csv`](results_record.csv) with the paper each
was read from.

## Plain text

The characters and their reading order. Reading order is a property of layout, not of the glyphs, so perfect character accuracy can still yield an unreadable stream.

**Pooling destroys** not the characters but the order and block boundaries that make them a document.

| Literature | Year | Brief description | Dataset / Protocol | Highlight |
|---|:-:|---|---|---|
| Tesseract | 2007 | Engineered recogniser: connected components, adaptive classifier | — | The baseline every later system is measured against |
| CRNN | 2017 | CNN features into a recurrent sequence model, CTC loss | ICDAR, SVT | Era II text recognition, and a TPAMI paper |
| TrOCR | 2023 | Transformer encoder-decoder, pretrained on synthetic lines | SROIE, IAM | Sequence modelling without a CNN stem |
| Donut | 2022 | Reads the page image end to end, emits structured output | DocVQA, CORD | The OCR-free lineage origin |
| Dessurt | 2022 | End-to-end recognition and understanding in one pass | DocVQA, FUNSD | Recognition and understanding jointly |
| [DocParser](https://arxiv.org/abs/2304.12484) | 2023 | OCR-free parsing to a structured representation | CORD | Structure as the output, not text |
| Vary | 2024 | Scales the vision vocabulary for dense document text | DocVQA | The predecessor of the OCR-2.0 line |
| [TextMonkey](https://arxiv.org/abs/2403.04473) | 2026 | OCR-free multimodal model with shifted-window attention | Doc benchmarks | A TPAMI paper on OCR-free document understanding |
| [TokenFD](https://arxiv.org/abs/2503.02304) | 2025 | **Token-level** text image foundation model | Doc benchmarks | Token-level rather than page-level representation |
| [dots.ocr](https://arxiv.org/abs/2512.02498) | 2025 | Compact model emitting markdown, layout and reading order | OmniDocBench | Structure emitted, not inferred |
| [MonkeyOCR](https://arxiv.org/abs/2506.05218) | 2025 | Structure-recognition-relation triplet parsing | OmniDocBench | Parsing as relation prediction |
| [PaddleOCR-VL](https://arxiv.org/abs/2510.14528) | 2025 | Coarse-to-fine visual processing for parsing | OmniDocBench | **Reports text, tables, formulas and reading order separately** |
| [olmOCR](https://arxiv.org/abs/2502.18443) | 2025 | Open pipeline for PDF-to-token conversion at scale | olmOCR-Bench | Contributes its own benchmark |
| [Docling](https://arxiv.org/abs/2501.17887) | 2025 | Open toolkit for AI-driven document conversion | — | What practitioners actually run |

## Layout structure

Columns, blocks, headers, captions, reading order and containment. Layout resists encoding because it is *relational*: a block's meaning depends on its neighbours.

**Pooling destroys containment**: a caption inside a figure box and one beside it become the same caption.

| Literature | Year | Brief description | Dataset / Protocol | Highlight |
|---|:-:|---|---|---|
| X-Y tree | 1984 | Recursive horizontal and vertical cuts on projection profiles | — | Era I origin point |
| Docstrum | 1993 | Nearest-neighbour angles and distances between components | — | Era I layout, and a TPAMI paper |
| Area Voronoi | 1998 | Segmentation from the area Voronoi diagram of components | — | Geometry without parameters tuned per page |
| PubLayNet | 2019 | Large annotated corpus; detection becomes the method | PubLayNet | Detection replaced geometry once data existed |
| [DocLayout-YOLO](https://arxiv.org/abs/2410.12628) | 2024 | Real-time detection with synthetic pretraining | DocLayNet | Speed at detection-level accuracy |
| LayoutLLM | 2024 | Layout instruction tuning for an LLM | DocVQA, FUNSD | Layout as instruction rather than as input |
| LayTextLLM | 2025 | A bounding box interleaved as **one token** | FUNSD, CORD | Layout without long coordinate sequences |
| Layout token | 2025 | A single layout token added to the LLM vocabulary | Doc benchmarks | The smallest possible layout injection |
| DocLayLLM | 2025 | Multimodal extension with layout-aware pretraining | DocVQA | Layout in the pretraining objective |
| Group position | 2025 | Group position embedding for document structure | Doc benchmarks | Position at the group rather than token level |
| GraphMLLM | 2024 | Multi-level, language-independent graph over layout | FUNSD, XFUND | Layout **and** script independence together |
| Graph DSA | 2025 | Document structure analysis as graph prediction | DocLayNet | Structure as a first-class target |
| DocHieNet | 2024 | Hierarchy prediction over document elements | DocHieNet | Hierarchy, not flat boxes |

---

## The remaining six channels

Tables, figures and charts, equations, form fields, stamps and seals,
and typography follow the same layout and are being filled in the same
way. Their papers are already in [`references.csv`](references.csv)
and in the [main list](../README.md#channels); what is being added
here is the *Brief description* and *Highlight* for each, which is a
reading rather than a lookup and is done one paper at a time.

**[➕ Help fill one](../../../issues/new?template=add-paper.yml)** — a
one-line description of what a paper does, for a channel you know, is
more useful than a new citation.
