# Eight Channels, One Vector

### A survey of retrieval-augmented visual document understanding

**286 papers, 158 of them from 2025–26.**
Paper list and released record for the survey (under review).

---

Surveys of this literature organise it by **where computation happens** —
parsing, retrieval, generation. This one organises it by **what the page
contains**: eight content channels that co-occur, and overlap, on the same
page.

Two of those eight have no retrieval literature at all. That is the
finding, and it is visible in the tables below before you read a word of
the paper.

---

## ➕ Add a paper

Every table below ends with an **➕ Add a paper here** link, and the
[venue table](#venue-coverage) has one on each row. All three routes open
the same short form: title, authors, venue, year, identifier, section.

| | |
|---|---|
| **[Open the form](../../issues/new?template=add-paper.yml)** | title, authors, venue, year, identifier, section — nothing else |
| **Run the script** | `python3 scripts/add_paper.py` — asks the same questions, appends the row, rebuilds the list and the site |
| **Edit and rebuild** | add a row to [`data/references.csv`](data/references.csv), then `python3 scripts/rebuild.py` |

The list is not everything published; it is what meets the criteria in
Sec. 3.3 of the survey — the corpus is a document collection, the unit is
a page or page region, and there is a quantitative result or a
contributed resource. A paper that fails one of those is not a worse
paper. It is a different paper, and the criteria are stated so that its
absence reads as a selection rather than an oversight.

**[Found an error? →](../../issues/new?template=correction.yml)**
Three widely circulated dataset figures were checked against their
sources and all three disagreed; one had reached our own first-pass
record from a competing survey's table. A correction is more useful to us
than a citation.

---

## Menu

<!-- MENU:START -->
- [Surveys](#surveys)
- [Channels](#channels)
  - [Plain text](#plain-text)
  - [Layout structure](#layout-structure)
  - [Tables](#tables)
  - [Figures and charts](#figures-and-charts)
  - [Equations](#equations)
  - [Form fields](#form-fields)
  - [Stamps and seals](#stamps-and-seals)
  - [Typography](#typography)
- [Pre-2024 lineage](#pre-2024-lineage)
- [Methods](#methods)
  - [Screenshot embedding](#screenshot-embedding)
  - [Late interaction](#late-interaction)
  - [End-to-end visual RAG](#end-to-end-visual-rag)
  - [Region- and layout-level](#region--and-layout-level)
  - [Agentic](#agentic)
  - [Query rewriting and reranking](#query-rewriting-and-reranking)
- [Encoding and indexing](#encoding-and-indexing)
  - [Chunking and text encoding](#chunking-and-text-encoding)
  - [Storage, pruning, compression](#storage-pruning-compression)
  - [Graph-structured indexes](#graph-structured-indexes)
- [Does OCR still matter?](#does-ocr-still-matter)
  - [OCR quality and robustness](#ocr-quality-and-robustness)
  - [Long context vs retrieval](#long-context-vs-retrieval)
- [Benchmarks and datasets](#benchmarks-and-datasets)
  - [Benchmarks and datasets](#benchmarks-and-datasets)
  - [Multilingual and script coverage](#multilingual-and-script-coverage)
- [Metrics and evaluation](#metrics-and-evaluation)
- [Adjacent work](#adjacent-work)
- [Venue coverage](#venue-coverage)
- [The released record](#the-released-record)
<!-- MENU:END -->

---
<!-- PAPERS:START -->

## Surveys

Every survey of this literature or its neighbours, with the axis each organises by. Read them down: pipeline stage, role of the MLLM, LLM capability, task family, modality, QA task. **None is page content.**

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends | ACL | conf. | 2026 | – |
| [Beyond Human Annotation: Recent Advances in Data Generation Methods for Document Intelligence](https://arxiv.org/abs/2601.12318) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2601.12318) |
| [Deep Learning based Visually Rich Document Content Understanding: A Survey](https://arxiv.org/abs/2408.01287) | AI Review | journal | 2026 | [link](https://arxiv.org/abs/2408.01287) |
| [Large Language Models in Document Intelligence: A Comprehensive Survey, Recent Advances, Challenges, and Future Trends](https://doi.org/10.1145/3768156) | ACM TOIS | journal | 2026 | [link](https://doi.org/10.1145/3768156) |
| [Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding](https://arxiv.org/abs/2510.15253) | ACL | conf. | 2026 | [link](https://arxiv.org/abs/2510.15253) |
| [Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval](https://arxiv.org/abs/2602.19961) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2602.19961) |
| [A Survey of Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2504.08748) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2504.08748) |
| Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation | ACL | conf. | 2025 | – |
| [Document Intelligence in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2510.13366) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2510.13366) |
| Multimodal Large Language Models for Text-rich Image Understanding: A Comprehensive Review | ACL | conf. | 2025 | – |
| [Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction](https://doi.org/10.1145/3726302.3730285) | SIGIR | conf. | 2025 | [link](https://doi.org/10.1145/3726302.3730285) |
| [Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook](https://arxiv.org/abs/2503.18016) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2503.18016) |
| [Roles of MLLMs in Visually Rich Document Retrieval for RAG: A Survey](https://arxiv.org/abs/2601.03262) | ACL | conf. | 2025 | [link](https://arxiv.org/abs/2601.03262) |
| [Survey on Question Answering over Visually Rich Documents: Methods, Challenges, and Trends](https://arxiv.org/abs/2501.02235) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2501.02235) |
| [VRD-IU: Lessons from Visually Rich Document Intelligence and Understanding](https://arxiv.org/abs/2506.01388) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2506.01388) |
| [Document Parsing Unveiled: Techniques, Challenges and Prospects for Structured Information Extraction](https://arxiv.org/abs/2410.21169) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2410.21169) |
| Visual Document Understanding: A Comparative Review of Modern Methods | Int. Conf. Computer Vision | conf. | 2024 | – |
| [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) | preprint | preprint | 2023 | [link](https://arxiv.org/abs/2312.10997) |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Channels

The eight content types a page carries. They are not a partition: they overlap, and the overlap is what the survey formalises.

### Plain text

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| [TextMonkey: An OCR-free Large Multimodal Model for Understanding Document](https://arxiv.org/abs/2403.04473) | TPAMI | journal | 2026 | Text | [link](https://arxiv.org/abs/2403.04473) |
| [A Token-level Text Image Foundation Model for Document Understanding](https://arxiv.org/abs/2503.02304) | ICCV | conf. | 2025 | Text | [link](https://arxiv.org/abs/2503.02304) |
| [DeepSeek-OCR: Contexts Optical Compression](https://arxiv.org/abs/2510.18234) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2510.18234) |
| [Docling: An Efficient Open-Source Toolkit for AI-Driven Document Conversion](https://arxiv.org/abs/2501.17887) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2501.17887) |
| [MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm](https://arxiv.org/abs/2506.05218) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2506.05218) |
| [PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://arxiv.org/abs/2510.14528) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2510.14528) |
| [dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model](https://arxiv.org/abs/2512.02498) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2512.02498) |
| [olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models](https://arxiv.org/abs/2502.18443) | preprint | preprint | 2025 | Text | [link](https://arxiv.org/abs/2502.18443) |
| Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models | ECCV | conf. | 2024 | Text | – |
| [DocParser: End-to-End OCR-free Information Extraction from Visually Rich Documents](https://arxiv.org/abs/2304.12484) | ICDAR | conf. | 2023 | Text | [link](https://arxiv.org/abs/2304.12484) |
| TrOCR: Transformer-Based Optical Character Recognition with Pre-trained Models | AAAI | conf. | 2023 | Text | – |
| End-to-End Document Recognition and Understanding with Dessurt | ECCV | conf. | 2022 | Text | – |
| OCR-free Document Understanding Transformer | ECCV | conf. | 2022 | Text | – |
| An End-to-End Trainable Neural Network for Image-Based Sequence Recognition and Its Application to Scene Text Recognition | TPAMI | journal | 2017 | Text | – |
| An Overview of the Tesseract OCR Engine | ICDAR | conf. | 2007 | Text | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Layout structure

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| A Bounding Box is Worth One Token: Interleaving Layout and Text in a Large Language Model for Document Understanding | ACL | conf. | 2025 | Layout | – |
| A Simple yet Effective Layout Token in Large Language Models for Document Understanding | CVPR | conf. | 2025 | Layout | – |
| DocLayLLM: An Efficient Multi-modal Extension of Large Language Models for Text-rich Document Understanding | CVPR | conf. | 2025 | Layout | – |
| Enhancing Document Understanding with Group Position Embedding | ICLR | conf. | 2025 | Layout | – |
| Graph-based Document Structure Analysis | ICLR | conf. | 2025 | Layout | – |
| DocHieNet: A Large and Diverse Dataset for Document Hierarchy Parsing | EMNLP | conf. | 2024 | Layout | – |
| [DocLayout-YOLO: Enhancing Document Layout Analysis through Diverse Synthetic Data and Global-to-Local Adaptive Perception](https://arxiv.org/abs/2410.12628) | preprint | preprint | 2024 | Layout | [link](https://arxiv.org/abs/2410.12628) |
| GraphMLLM: A Graph-Based Multi-Level Layout Language- Independent Model for Document Understanding | ICDAR | conf. | 2024 | Layout | – |
| LayoutLLM: Layout Instruction Tuning with Large Language Models for Document Understanding | CVPR | conf. | 2024 | Layout | – |
| Unifying Vision, Text, and Layout for Universal Document Processing | CVPR | conf. | 2023 | Layout | – |
| ERNIE-Layout: Layout Knowledge Enhanced Pre-training for Visually-rich Document Understanding | EMNLP | conf. | 2022 | Layout | – |
| LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking | ACM MM | conf. | 2022 | Layout | – |
| LiLT: A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding | ACL | conf. | 2022 | Layout | – |
| Going Full-Tilt Boogie on Document Understanding with Text-Image-Layout Transformer | ICDAR | conf. | 2021 | Layout | – |
| LayoutLMv2: Multi-modal Pre-training for Visually-Rich Document Understanding | ACL | conf. | 2021 | Layout | – |
| LayoutLM: Pre-training of Text and Layout for Document Image Understanding | KDD | conf. | 2020 | Layout | – |
| PubLayNet: Largest Dataset Ever for Document Layout Analysis | ICDAR | conf. | 2019 | Layout | – |
| Performance Evaluation and Benchmarking of Six-Page Segmentation Algorithms | TPAMI | journal | 2008 | Layout | – |
| Performance Comparison of Six Algorithms for Page Segmentation | DAS | conf. | 2006 | Layout | – |
| Two Geometric Algorithms for Layout Analysis | DAS | conf. | 2002 | Layout | – |
| Segmentation of Page Images Using the Area Voronoi Diagram | CVIU | journal | 1998 | Layout | – |
| Background Structure in Document Images | IJPRAI | journal | 1994 | Layout | – |
| The Document Spectrum for Page Layout Analysis | TPAMI | journal | 1993 | Layout | – |
| Hierarchical Representation of Optically Scanned Documents | Pattern Recognition | journal | 1984 | Layout | – |
| Document Analysis System | IBM Journal of Research an | conf. | 1982 | Layout | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Tables

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy | NeurIPS | conf. | 2025 | Tables | – |
| [Deep Learning for Table Detection and Structure Recognition: A Survey](https://doi.org/10.1145/3657281) | ACM Comput. Surv. | conf. | 2024 | Tables | [link](https://doi.org/10.1145/3657281) |
| Multimodal Table Understanding | ACL | conf. | 2024 | Tables | – |
| PubTables-1M: Towards Comprehensive Table Extraction from Unstructured Documents | CVPR | conf. | 2022 | Tables | – |
| Table Structure Recognition and Form Parsing by End-to-End Object Detection and Relation Parsing | Pattern Recognition | journal | 2022 | Tables | – |
| TableFormer: Table Structure Understanding with Transformers | CVPR | conf. | 2022 | Tables | – |
| Image-Based Table Recognition: Data, Model, and Evaluation | ECCV | conf. | 2020 | Tables | – |
| Rethinking Table Recognition Using Graph Neural Networks | ICDAR | conf. | 2019 | Tables | – |
| Table-Processing Paradigms: A Research Survey | IJDAR | journal | 2006 | Tables | – |
| A Survey of Table Recognition: Models, Observations, Transformations, and Inferences | IJDAR | journal | 2004 | Tables | – |
| TINTIN: A System for Retrieval in Text Tables | ACM Int. Conf. Digital Lib | conf. | 1997 | Tables | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Figures and charts

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| [Chart-HQA: A Benchmark for Hypothetical Question Answering in Charts](https://doi.org/10.1145/3746027.3758288) | ACM MM | conf. | 2025 | Figures | [link](https://doi.org/10.1145/3746027.3758288) |
| ChartMoE: Mixture of Diversely Aligned Expert Connector for Chart Understanding | ICLR | conf. | 2025 | Figures | – |
| Unmasking Deceptive Visuals: Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering | EMNLP | conf. | 2025 | Figures | – |
| CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs | NeurIPS | conf. | 2024 | Figures | – |
| ChartInstruct: Instruction Tuning for Chart Comprehension and Reasoning | ACL | conf. | 2024 | Figures | – |
| OneChart: Purify the Chart Structural Extraction via One Auxiliary Token | ACM MM | conf. | 2024 | Figures | – |
| ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning | ACL | conf. | 2022 | Figures | – |
| PlotQA: Reasoning over Scientific Plots | WACV | conf. | 2020 | Figures | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Equations

> Two metrics return **opposite verdicts** on the same pair of formula-recognition systems.

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| [Image Over Text: Transforming Formula Recognition Evaluation with Character Detection Matching](https://arxiv.org/abs/2409.03643) | CVPR | conf. | 2025 | Equations | [link](https://arxiv.org/abs/2409.03643) |
| Mathematical Information Retrieval: Search and Question Answering | FnT | journal | 2025 | Equations | – |
| Nougat: Neural Optical Understanding for Academic Documents | ICLR | conf. | 2024 | Equations | – |
| [UniMERNet: A Universal Network for Real-World Mathematical Expression Recognition](https://arxiv.org/abs/2404.15254) | preprint | preprint | 2024 | Equations | [link](https://arxiv.org/abs/2404.15254) |
| Multi-Stage Math Formula Search: Using Appearance-Based Similarity Metrics at Scale | SIGIR | conf. | 2016 | Equations | – |
| NTCIR-12 MathIR Task Overview | NTCIR | conf. | 2016 | Equations | – |
| NTCIR-10 Math Pilot Task Overview | NTCIR | conf. | 2013 | Equations | – |
| Recognition and Retrieval of Mathematical Expressions | IJDAR | journal | 2012 | Equations | – |
| [Mathematical Expression Recognition: A Survey](https://doi.org/10.1007/PL00013549) | IJDAR | journal | 2000 | Equations | [link](https://doi.org/10.1007/PL00013549) |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Form fields

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| UNIKIE-BENCH: Benchmarking Large Multimodal Models for Key Information Extraction in Visual Documents | ACL | conf. | 2026 | Forms | – |
| LMDX: Language Model-based Document Information Extraction and Localization | ACL | conf. | 2024 | Forms | – |
| SRFUND: A Multi-Granularity Hierarchical Structure Reconstruction Benchmark in Form Understanding | NeurIPS | conf. | 2024 | Forms | – |
| ICL-D3IE: In-Context Learning with Diverse Demonstrations Updating for Document Information Extraction | ICCV | conf. | 2023 | Forms | – |
| FormNet: Structural Encoding beyond Sequential Modeling in Form Document Information Extraction | ACL | conf. | 2022 | Forms | – |
| XFUND: A Benchmark Dataset for Multilingual Visually Rich Form Understanding | ACL | conf. | 2022 | Forms | – |
| FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents | ICDAR | conf. | 2019 | Forms | – |
| ICDAR2019 Competition on Scanned Receipt OCR and Information Extraction | ICDAR | conf. | 2019 | Forms | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Stamps and seals

> **Roughly ten papers across forty years, one dataset released in 2025, and no retrieval system that evaluates on this channel at all.** The thinness is not an artefact of our search; it is the state of the field.

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| [DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization](https://arxiv.org/abs/2511.09117) | preprint | preprint | 2025 | Stamps | [link](https://arxiv.org/abs/2511.09117) |
| [D-StaR: A Generic Method for Stamp Segmentation from Document Images](https://doi.org/10.1109/ICDAR.2017.49) | ICDAR | conf. | 2017 | Stamps | [link](https://doi.org/10.1109/ICDAR.2017.49) |
| [SPODS: A Dataset of Color-Official Documents and Detection of Logo, Stamp, and Signature](https://doi.org/10.1007/978-3-319-68124-5_19) | ICVGIP Satellite Workshops | conf. | 2017 | Stamps | [link](https://doi.org/10.1007/978-3-319-68124-5_19) |
| [Logo and Seal Based Administrative Document Image Retrieval: A Survey](https://doi.org/10.1016/j.cosrev.2016.09.002) | Computer Science Review | conf. | 2016 | Stamps | [link](https://doi.org/10.1016/j.cosrev.2016.09.002) |
| [Text-Graphics Separation to Detect Logo and Stamp from Color Document Images: A Spectral Approach](https://doi.org/10.1109/ICDAR.2015.7333826) | ICDAR | conf. | 2015 | Stamps | [link](https://doi.org/10.1109/ICDAR.2015.7333826) |
| [Signature Segmentation from Machine Printed Documents Using Conditional Random Field](https://doi.org/10.1109/ICDAR.2011.236) | ICDAR | conf. | 2011 | Stamps | [link](https://doi.org/10.1109/ICDAR.2011.236) |
| Stamp Detection in Color Document Images | ICDAR | conf. | 2011 | Stamps | – |
| Extraction of Signature and Seal Imprint from Bankchecks Using Color Information | ICDAR | conf. | 1995 | Stamps | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Typography

> **One annotated corpus exists.** One is a sharper finding than none — the channel *is* annotatable, and has never been retrieved over.

| Paper | Venue | Type | Year | Channel | Link |
|---|:-:|:-:|:-:|:-:|:-:|
| [TexTAR: Textual Attribute Recognition in Multi-domain and Multi-lingual Document Images](https://arxiv.org/abs/2509.13151) | preprint | preprint | 2026 | Typography | [link](https://arxiv.org/abs/2509.13151) |
| [Analyzing Font Style Usage and Contextual Factors in Real Images](https://doi.org/10.1007/978-3-031-41682-8_21) | ICDAR | conf. | 2023 | Typography | [link](https://doi.org/10.1007/978-3-031-41682-8_21) |
| Using Robust Regression to Find Font Usage Trends | ICDAR | conf. | 2021 | Typography | – |
| [DeepFont: Identify Your Font from an Image](https://doi.org/10.1145/2733373.2806219) | ACM MM | conf. | 2015 | Typography | [link](https://doi.org/10.1145/2733373.2806219) |
| Font Adaptive Word Indexing of Modern Printed Documents | TPAMI | journal | 2006 | Typography | – |
| Optical Font Recognition Using Typographical Features | TPAMI | journal | 1998 | Typography | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Pre-2024 lineage

Retrieval over document images is two decades older than the current literature suggests, and the unit throughout was the word, the formula or the region — never the page.

> Question answering over a document *collection* was posed at ICDAR in 2021 — **four years before the visual-RAG literature rediscovered the task**.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| Multi-Page Document VQA with Recurrent Memory Transformer | DAS | conf. | 2024 | – |
| Multi-Page Document Visual Question Answering Using Self-Attention Scoring Mechanism | ICDAR | conf. | 2024 | – |
| End-to-End Learning of Representations for Instance-Level Document Image Retrieval | Applied Soft Computing | conf. | 2023 | – |
| Hierarchical Multimodal Transformers for Multipage DocVQA | Pattern Recognition | journal | 2023 | – |
| [Document Collection Visual Question Answering](https://doi.org/10.1007/978-3-030-86331-9_50) | ICDAR | conf. | 2021 | [link](https://doi.org/10.1007/978-3-030-86331-9_50) |
| [A Survey of Document Image Word Spotting Techniques](https://doi.org/10.1016/j.patcog.2017.02.023) | Pattern Recognition | journal | 2017 | [link](https://doi.org/10.1016/j.patcog.2017.02.023) |
| Neural Ctrl-F: Segmentation-Free Query-by-String Word Spotting | ICCV | conf. | 2017 | – |
| PHOCNet: A Deep CNN for Word Spotting in Handwritten Documents | Int. Conf. Frontiers in Ha | conf. | 2016 | – |
| Efficient Segmentation-Free Keyword Spotting in Historical Document Collections | Pattern Recognition | journal | 2015 | – |
| Evaluation of Deep Convolutional Nets for Document Image Classification and Retrieval | ICDAR | conf. | 2015 | – |
| [Word Spotting and Recognition with Embedded Attributes](https://doi.org/10.1109/TPAMI.2014.2339814) | TPAMI | journal | 2014 | [link](https://doi.org/10.1109/TPAMI.2014.2339814) |
| Mobile Retriever: Access to Digital Documents from Their Physical Source | IJDAR | journal | 2008 | – |
| Word Spotting for Historical Documents | IJDAR | journal | 2007 | – |
| Information Retrieval in Document Image Databases | IEEE Trans. Knowledge and  | conf. | 2004 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Methods

Grouped by paradigm. Read the years down the region-level group: every system there appeared in 2025 or later, against a page-level literature beginning in 2024.

### Screenshot embedding

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation](https://arxiv.org/abs/2510.09733) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2510.09733) |
| VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents | ICLR | conf. | 2025 | – |
| Unifying Multimodal Retrieval via Document Screenshot Embedding | EMNLP | conf. | 2024 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Late interaction

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction](https://arxiv.org/abs/2509.18095) | ICLR | conf. | 2026 | [link](https://arxiv.org/abs/2509.18095) |
| [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2602.03992) |
| Any Information Is Just Worth One Single Screenshot: Unifying Search with Visualized Information Retrieval | ACL | conf. | 2025 | – |
| Bridging Modalities: Improving Universal Multimodal Retrieval by Multimodal Large Language Models | CVPR | conf. | 2025 | – |
| ColFlor: Towards BERT-Size Vision-Language Document Retrieval Models | IEEE Int. Workshop Machine | conf. | 2025 | – |
| ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval | EMNLP | conf. | 2025 | – |
| ColPali: Efficient Document Retrieval with Vision Language Models | ICLR | conf. | 2025 | – |
| DocVLM: Make Your VLM an Efficient Reader | CVPR | conf. | 2025 | – |
| LaMRA: Large Multimodal Model as Your Advanced Retrieval Assistant | CVPR | conf. | 2025 | – |
| [ModernVBERT: Towards Smaller Visual Document Retrievers](https://arxiv.org/abs/2510.01149) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2510.01149) |
| [Serval: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models](https://arxiv.org/abs/2509.15432) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2509.15432) |
| [VLM2Vec-V2: Advancing Multimodal Embedding for Videos, Images, and Visual Documents](https://arxiv.org/abs/2507.04590) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2507.04590) |
| Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding | Int. Conf. Mach. Learn. (I | conf. | 2023 | – |
| [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://arxiv.org/abs/2112.01488) | preprint | preprint | 2021 | [link](https://arxiv.org/abs/2112.01488) |
| ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT | SIGIR | conf. | 2020 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### End-to-end visual RAG

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering](https://arxiv.org/abs/2605.29606) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2605.29606) |
| [LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding](https://arxiv.org/abs/2605.22829) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2605.22829) |
| [CMRAG: Co-Modality-Based Visual Document Retrieval and Question Answering](https://arxiv.org/abs/2509.02123) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2509.02123) |
| CoRe-MMRAG: Cross-Source Knowledge Reconciliation for Multimodal RAG | ACL | conf. | 2025 | – |
| Enhancing Multimodal Retrieval via Complementary Information Extraction and Alignment | ACL | conf. | 2025 | – |
| [HKRAG: Holistic Knowledge Retrieval-Augmented Generation over Visually-Rich Documents](https://arxiv.org/abs/2511.20227) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2511.20227) |
| [Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy](https://arxiv.org/abs/2510.22215) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2510.22215) |
| MIRe: Enhancing Multimodal Queries Representation via Fusion-Free Modality Interaction for Multimodal Retrieval | ACL | conf. | 2025 | – |
| MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval | EMNLP | conf. | 2025 | – |
| SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding | ICLR | conf. | 2025 | – |
| VDocRAG: Retrieval-Augmented Generation over Visually-Rich Documents | CVPR | conf. | 2025 | – |
| VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation | ACL | conf. | 2025 | – |
| [M3DocRAG: Multi-modal Retrieval is What You Need for Multi-page Multi-document Understanding](https://arxiv.org/abs/2411.04952) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2411.04952) |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Region- and layout-level

> Every system here appeared in 2025 or later. Retrieval granularity coarsened to the page in 2024 and has only begun to return.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations](https://arxiv.org/abs/2603.01666) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2603.01666) |
| LAD-RAG: Layout-aware Dynamic RAG for Visually-Rich Document Understanding | ACL | conf. | 2026 | – |
| [LMS-Retrieval: Layout-Aware, Modality-Aware, Structure-Aware Document Retrieval](https://doi.org/10.1007/978-3-032-36039-7_8) | ICDAR | conf. | 2026 | [link](https://doi.org/10.1007/978-3-032-36039-7_8) |
| M3Grounder: Mask-Based Multi-Span and Multi-Granular Grounding for Document QA | CVPR | conf. | 2026 | – |
| RegionRAG: Region-level Retrieval-Augmented Generation for Visual Document Understanding | AAAI | conf. | 2026 | – |
| [RegionSLM: Region-aware Question Answering on Document Screenshots](https://doi.org/10.1145/3805712.3809603) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3809603) |
| [ARIAL: An Agentic Framework for Document VQA with Precise Answer Localization](https://arxiv.org/abs/2511.18192) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2511.18192) |
| VISA: Retrieval Augmented Generation with Visual Source Attribution | ACL | conf. | 2025 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Agentic

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| DocLens: A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding | ACL | conf. | 2026 | – |
| Look as You Think: Unifying Reasoning and Visual Evidence Attribution for Verifiable Document RAG via Reinforcement Learning | AAAI | conf. | 2026 | – |
| [MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA](https://arxiv.org/abs/2606.05749) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2606.05749) |
| SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding | ACL | conf. | 2026 | – |
| Visual Document Understanding and Reasoning: A Multi-Agent Collaboration Framework with Agent-Wise Adaptive Test-Time Scaling | CVPR | conf. | 2026 | – |
| [MDocAgent: A Multi-Modal Multi-Agent Framework for Document Understanding](https://arxiv.org/abs/2503.13964) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2503.13964) |
| ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents | EMNLP | conf. | 2025 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Query rewriting and reranking

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [Good Ranks Follow Good Answers: Unsupervised Answer-Driven Reranking for Multimodal Document QA](https://doi.org/10.1145/3805712.3809664) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3809664) |
| Guided Query Refinement: Multimodal Hybrid Retrieval with Test-Time Optimization | ICLR | conf. | 2026 | – |
| Suit the Remedy to the Retriever: Interpretable Query Optimization with Retriever Preference Alignment for Vision-Language Retrieval | AAAI | conf. | 2026 | – |
| Boosting Retrieval-Augmented Generation with Generation-Augmented Retrieval: A Co-Training Approach | SIGIR | conf. | 2025 | – |
| DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | NeurIPS | conf. | 2025 | – |
| InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering | EMNLP | conf. | 2025 | – |
| MaFeRw: Query Rewriting with Multi-Aspect Feedbacks for Retrieval-Augmented Large Language Models | AAAI | conf. | 2025 | – |
| RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs | NeurIPS | conf. | 2024 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Encoding and indexing

What happens to a page between parsing and the index, and what it costs to store.

### Chunking and text encoding

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [Beyond Chunk-Then-Embed: A Comprehensive Taxonomy and Evaluation of Document Chunking Strategies for Information Retrieval](https://doi.org/10.1145/3805712.3808575) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3808575) |
| [Enhancing RAG System Performance Through Semantic Layout Chunking](https://doi.org/10.1007/978-981-95-4969-6_3) | IJCAI | conf. | 2026 | [link](https://doi.org/10.1007/978-981-95-4969-6_3) |
| [Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval](https://arxiv.org/abs/2604.10167) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2604.10167) |
| [HiChunk: Hierarchical Document Chunking](https://arxiv.org/abs/2509.11552) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2509.11552) |
| On the Effectiveness of Semantic Chunking | ACL | conf. | 2025 | – |
| [Vision-Guided Chunking Is All You Need](https://arxiv.org/abs/2506.16035) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2506.16035) |
| An Analysis of Fusion Functions for Hybrid Retrieval | ACM TOIS | journal | 2024 | – |
| [Financial Report Chunking for Effective Retrieval Augmented Generation](https://arxiv.org/abs/2402.05131) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2402.05131) |
| [Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models](https://arxiv.org/abs/2409.04701) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2409.04701) |
| [LumberChunker: Long-Form Narrative Document Segmentation](https://arxiv.org/abs/2406.17526) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2406.17526) |
| Dense Passage Retrieval for Open-Domain Question Answering | EMNLP | conf. | 2020 | – |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | NeurIPS | conf. | 2020 | – |
| Billion-Scale Similarity Search with GPUs | IEEE Trans. Big Data | conf. | 2019 | – |
| The Probabilistic Relevance Framework: BM25 and Beyond | FnT | journal | 2009 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Storage, pruning, compression

> Two halves measuring different quantities: pruning reports **storage** against accuracy, hybrid retrieval reports **compute**. No work reports both with accuracy.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [A Replicability Study of Joint Product Quantisation for Effective Space-Efficient Dense Retrieval](https://doi.org/10.1145/3805712.3808565) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3808565) |
| [A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3809726) |
| Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods | ACL | conf. | 2026 | – |
| [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://doi.org/10.1145/3805712.3809920) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3809920) |
| [Comparing Token Pruning Approaches for Multi-Vector Retrieval](https://doi.org/10.1145/3805712.3808564) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3808564) |
| [Look in the Middle: Structural Anchor Pruning for Scalable Visual RAG Indexing](https://arxiv.org/abs/2601.20107) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2601.20107) |
| [CRISP: Clustering Multi-Vector Representations for Denoising and Pruning](https://arxiv.org/abs/2505.11471) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2505.11471) |
| DocKylin: A Large Multimodal Model for Visual Document Understanding with Efficient Visual Slimming | AAAI | conf. | 2025 | – |
| [DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning](https://arxiv.org/abs/2509.23883) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2509.23883) |
| SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors | COLING | conf. | 2025 | – |
| Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? | ACL | conf. | 2025 | – |
| [Towards Lossless Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3726302.3730100) | SIGIR | conf. | 2025 | [link](https://doi.org/10.1145/3726302.3730100) |
| Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings | ACL | conf. | 2025 | – |
| [WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | SIGIR | conf. | 2025 | [link](https://doi.org/10.1145/3726302.3729904) |
| Efficient Large Multi-modal Models via Visual Context Compression | NeurIPS | conf. | 2024 | – |
| Hierarchical Visual Feature Aggregation for OCR-Free Document Understanding | NeurIPS | conf. | 2024 | – |
| MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encoding | NeurIPS | conf. | 2024 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Graph-structured indexes

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921) | ACM TOIS | journal | 2026 | [link](https://arxiv.org/abs/2408.08921) |
| Iterative Multi-Granular RAG with Contextual Hierarchical Graph | AAAI | conf. | 2026 | – |
| When to Use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation | ICLR | conf. | 2026 | – |
| [BookRAG: A Hierarchical Structure-Aware Index-Based Approach for Retrieval-Augmented Generation on Complex Documents](https://arxiv.org/abs/2512.03413) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2512.03413) |
| [MMGraphRAG: Bridging Vision and Language with Interpretable Multimodal Knowledge Graphs](https://arxiv.org/abs/2507.20804) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2507.20804) |
| SuperRAG: Beyond RAG with Layout-Aware Graph Modeling | ACL | conf. | 2025 | – |
| [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2404.16130) |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Does OCR still matter?

Four groups, four venues that do not usually read each other, reported the same thing between 2025 and 2026.

### OCR quality and robustness

> The agreement is not that OCR is bad — every one reports accurate recognition. It is that **character-level accuracy is the wrong measurement**, because what breaks retrieval is what recognition *discards*.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| Benchmarking Visual LLMs Resilience to Unanswerable Questions on Visually Rich Documents | AAAI | conf. | 2026 | – |
| [Can OCR-VLMs Read Devanagari? A Stress-Test Benchmark and Post-Correction Study](https://arxiv.org/abs/2606.29213) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2606.29213) |
| [Defining the Problem: The Impact of OCR Quality on Retrieval-Augmented Generation Performance and Strategies for Improvement](https://doi.org/10.1016/j.ipm.2025.104368) | IP&M | journal | 2026 | [link](https://doi.org/10.1016/j.ipm.2025.104368) |
| EmoRAG: Evaluating RAG Robustness to Symbolic Perturbations | KDD | conf. | 2026 | – |
| [ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts](https://arxiv.org/abs/2603.09392) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2603.09392) |
| [QE-RAG: A Robust Retrieval-Augmented Generation Benchmark for Query Entry Errors](https://doi.org/10.1145/3805712.3808610) | SIGIR | conf. | 2026 | [link](https://doi.org/10.1145/3805712.3808610) |
| SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation | WACV | conf. | 2026 | – |
| StruNRAG: Evaluation of OCR-Induced Structural Noise on RAG Robustness | ACL | conf. | 2026 | – |
| [When Good OCR Is Not Enough: Benchmarking OCR Robustness for Retrieval-Augmented Generation](https://doi.org/10.18653/v1/2026.acl-industry.60) | ACL | conf. | 2026 | [link](https://doi.org/10.18653/v1/2026.acl-industry.60) |
| [Enhancing Document VQA Models via Retrieval-Augmented Generation](https://doi.org/10.1007/978-3-032-09368-4_6) | ICDAR | conf. | 2025 | [link](https://doi.org/10.1007/978-3-032-09368-4_6) |
| [Lost in OCR Translation? Vision-Based Approaches to Robust Document Retrieval](https://arxiv.org/abs/2505.05666) | ACM Symp. Document Enginee | conf. | 2025 | [link](https://arxiv.org/abs/2505.05666) |
| [MultiOCR-QA: A Multilingual Dataset for Question Answering on OCR-Processed Text](https://arxiv.org/abs/2502.16781) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2502.16781) |
| OCR Hinders RAG: Evaluating the Cascading Impact of OCR | ICCV | conf. | 2025 | – |
| [OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations](https://doi.org/10.1109/CVPR52734.2025.02313) | CVPR | conf. | 2025 | [link](https://doi.org/10.1109/CVPR52734.2025.02313) |
| READoc: A Unified Benchmark for Realistic Document Structured Extraction | ACL | conf. | 2025 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Long context vs retrieval

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| Inference Scaling for Long-Context Retrieval Augmented Generation | ICLR | conf. | 2025 | – |
| [Long Context vs. RAG: Strategies for Processing Long Documents in LLMs](https://doi.org/10.1145/3726302.3731690) | SIGIR | conf. | 2025 | [link](https://doi.org/10.1145/3726302.3731690) |
| Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG | ICLR | conf. | 2025 | – |
| More Documents, Same Length: Isolating the Challenge of Multiple Documents in RAG | EMNLP | conf. | 2025 | – |
| Lost in the Middle: How Language Models Use Long Contexts | Trans. Assoc. Comput. Ling | conf. | 2024 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Benchmarks and datasets

Every benchmark in the record. Per-channel coverage is in [`data/datasets.md`](data/datasets.md).

### Benchmarks and datasets

> **Stamps and typography are absent from every retrieval benchmark here.** A channel no benchmark annotates cannot be measured, and a channel that cannot be measured will not improve.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/abs/2601.08620) | ACL | conf. | 2026 | [link](https://arxiv.org/abs/2601.08620) |
| [irpapers: A Visual Document Benchmark for Scientific Retrieval and Question Answering](https://arxiv.org/abs/2602.17687) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2602.17687) |
| [pdfQA: Diverse, Challenging, and Realistic Question Answering over PDFs](https://arxiv.org/abs/2601.02285) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2601.02285) |
| [BBox-DocVQA: A Large-Scale Bounding-Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answering](https://arxiv.org/abs/2511.15090) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2511.15090) |
| [Benchmarking Retrieval-Augmented Multimodal Generation for Document Question Answering](https://arxiv.org/abs/2505.16470) | NeurIPS | conf. | 2025 | [link](https://arxiv.org/abs/2505.16470) |
| [FinRAGBench-V: A Benchmark for Multimodal RAG in Finance](https://arxiv.org/abs/2505.17471) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2505.17471) |
| MMDocIR: Benchmarking Multimodal Retrieval for Long Documents | EMNLP | conf. | 2025 | – |
| REAL-MM-RAG: A Real-World Multi-Modal Retrieval Benchmark | ACL | conf. | 2025 | – |
| [UniDoc-Bench: A Unified Benchmark for Document-Centric Multimodal RAG](https://arxiv.org/abs/2510.03663) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2510.03663) |
| [ViDoRe Benchmark v2: Raising the Bar for Visual Retrieval](https://arxiv.org/abs/2505.17166) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2505.17166) |
| [ViDoSeek: A Benchmark for Visual Document Retrieval and Reasoning](https://arxiv.org/abs/2502.18017) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2502.18017) |
| VisDoMBench: A Benchmark for Multi-Document QA with Visually Rich Elements | ACL | conf. | 2025 | – |
| [VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding](https://arxiv.org/abs/2508.07493) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2508.07493) |
| CRAG: Comprehensive RAG Benchmark | NeurIPS | conf. | 2024 | – |
| [Document Haystacks: Vision-Language Reasoning over Piles of 1000+ Documents](https://arxiv.org/abs/2411.16740) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2411.16740) |
| [LongDocURL: A Comprehensive Multimodal Long Document Benchmark Integrating Understanding, Reasoning and Locating](https://arxiv.org/abs/2412.18424) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2412.18424) |
| MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations | NeurIPS | conf. | 2024 | – |
| [Multimodal ArXiv: A Dataset for Improving Scientific Comprehension of Large Vision-Language Models](https://arxiv.org/abs/2403.00231) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2403.00231) |
| SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers | NeurIPS | conf. | 2024 | – |
| UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis | NeurIPS | conf. | 2024 | – |
| Document Understanding Dataset and Evaluation (DUDE) | ICCV | conf. | 2023 | – |
| [PDF-VQA: A New Dataset for Real-World VQA on PDF Documents](https://arxiv.org/abs/2304.06447) | preprint | preprint | 2023 | [link](https://arxiv.org/abs/2304.06447) |
| SlideVQA: A Dataset for Document Visual Question Answering on Multiple Images | AAAI | conf. | 2023 | – |
| InfographicVQA | WACV | conf. | 2022 | – |
| Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering | NeurIPS | conf. | 2022 | – |
| Towards Complex Document Understanding by Discrete Reasoning | ACM MM | conf. | 2022 | – |
| [DocVQA: A Dataset for VQA on Document Images](https://doi.org/10.1109/WACV48630.2021.00225) | WACV | conf. | 2021 | [link](https://doi.org/10.1109/WACV48630.2021.00225) |
| VisualMRC: Machine Reading Comprehension on Document Images | AAAI | conf. | 2021 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

### Multilingual and script coverage

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| IndicVisionBench: A Multimodal Benchmark for Indic Languages | ICLR | conf. | 2026 | – |
| M$^3$D: A Multimodal, Multilingual and Multitask Dataset for Grounded Document-Level Information Extraction | TPAMI | journal | 2026 | – |
| M4-RAG: A Massive-Scale Multilingual Multi-Cultural Multimodal RAG | CVPR | conf. | 2026 | – |
| SEA-Vision: A Multilingual Benchmark for Comprehensive Document and Scene Text Understanding in Southeast Asia | CVPR | conf. | 2026 | – |
| IndicDLP: A Foundational Dataset for Multi-lingual and Multi-domain Document Layout Parsing | ICDAR | conf. | 2025 | – |
| [MIRACL-VISION: A Large, Multilingual, Visual Document Retrieval Benchmark](https://arxiv.org/abs/2505.11651) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2505.11651) |
| [MTVQA: Benchmarking Multilingual Text-Centric Visual Question Answering](https://arxiv.org/abs/2405.11985) | ACL | conf. | 2025 | [link](https://arxiv.org/abs/2405.11985) |
| Scene Text Recognition: An Indic Perspective | IJDAR | journal | 2025 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Metrics and evaluation

The instruments the field measures with, and the work questioning whether they measure the right thing.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence](https://arxiv.org/abs/2605.12882) | preprint | preprint | 2026 | [link](https://arxiv.org/abs/2605.12882) |
| [Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?](https://arxiv.org/abs/2508.03644) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2508.03644) |
| Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse | ICLR | conf. | 2025 | – |
| [RAG-Check: Evaluating Multimodal Retrieval Augmented Generation Performance](https://arxiv.org/abs/2501.03995) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2501.03995) |
| ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability | ICLR | conf. | 2025 | – |
| [Evaluating Retrieval Quality in Retrieval-Augmented Generation](https://doi.org/10.1145/3626772.3657957) | SIGIR | conf. | 2024 | [link](https://doi.org/10.1145/3626772.3657957) |
| RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models | ACL | conf. | 2024 | – |
| [The Power of Noise: Redefining Retrieval for RAG Systems](https://doi.org/10.1145/3626772.3657834) | SIGIR | conf. | 2024 | [link](https://doi.org/10.1145/3626772.3657834) |
| [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71) | BMJ | conf. | 2021 | [link](https://doi.org/10.1136/bmj.n71) |
| Scene Text Visual Question Answering | ICCV | conf. | 2019 | – |
| Cumulated Gain-Based Evaluation of IR Techniques | ACM TOIS | journal | 2002 | – |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

## Adjacent work

Knowledge-based VQA over natural images: the corpus is external world knowledge rather than the document collection, so we treat it as adjacent rather than in scope.

| Paper | Venue | Type | Year | Link |
|---|:-:|:-:|:-:|:-:|
| [MRAG-Bench: Vision-Centric Evaluation for Retrieval-Augmented Multimodal Models](https://arxiv.org/abs/2410.08182) | ICLR | conf. | 2025 | [link](https://arxiv.org/abs/2410.08182) |
| [Visual-RAG: Benchmarking Text-to-Image Retrieval Augmented Generation for Visual Knowledge Intensive Queries](https://arxiv.org/abs/2502.16636) | preprint | preprint | 2025 | [link](https://arxiv.org/abs/2502.16636) |
| [RoRA-VLM: Robust Retrieval Augmentation for Vision Language Models](https://arxiv.org/abs/2410.08876) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2410.08876) |
| SURf: Teaching Large Vision-Language Models to Selectively Utilize Retrieved Information | EMNLP | conf. | 2024 | – |
| [UniRAG: Universal Retrieval Augmentation for Large Vision Language Models](https://arxiv.org/abs/2405.10311) | preprint | preprint | 2024 | [link](https://arxiv.org/abs/2405.10311) |

**[➕ Add a paper here](../../issues/new?template=add-paper.yml)**

<!-- PAPERS:END -->

---

## Venue coverage

Every venue searched in the review, and how many of its papers are in the
record. A dash is not an omission: it means the venue was searched and
nothing met the inclusion criteria. Sec. 3.2 of the survey reports the
negative venues explicitly, because a survey that lists only where it
found things cannot be checked.

<!-- VENUES:START -->
| # | Venue | Type | Papers | Add |
|:-:|---|:-:|:-:|:-:|
| 1 | CVPR | conference | **16** | [➕](../../issues/new?template=add-paper.yml) |
| 2 | ICCV | conference | **6** | [➕](../../issues/new?template=add-paper.yml) |
| 3 | ECCV | conference | **4** | [➕](../../issues/new?template=add-paper.yml) |
| 4 | ACM MM | conference | **5** | [➕](../../issues/new?template=add-paper.yml) |
| 5 | WACV | conference | **4** | [➕](../../issues/new?template=add-paper.yml) |
| 6 | ACL | conference | **37** | [➕](../../issues/new?template=add-paper.yml) |
| 7 | EMNLP | conference | **12** | [➕](../../issues/new?template=add-paper.yml) |
| 8 | NAACL | conference | — | [➕](../../issues/new?template=add-paper.yml) |
| 9 | SIGIR | conference | **17** | [➕](../../issues/new?template=add-paper.yml) |
| 10 | CIKM | conference | — | [➕](../../issues/new?template=add-paper.yml) |
| 11 | The Web Conference | conference | — | [➕](../../issues/new?template=add-paper.yml) |
| 12 | COLING | conference | **1** | [➕](../../issues/new?template=add-paper.yml) |
| 13 | NeurIPS | conference | **15** | [➕](../../issues/new?template=add-paper.yml) |
| 14 | ICLR | conference | **16** | [➕](../../issues/new?template=add-paper.yml) |
| 15 | AAAI | conference | **10** | [➕](../../issues/new?template=add-paper.yml) |
| 16 | IJCAI | conference | **1** | [➕](../../issues/new?template=add-paper.yml) |
| 17 | ICDAR | conference | **21** | [➕](../../issues/new?template=add-paper.yml) |
| 18 | KDD | conference | **2** | [➕](../../issues/new?template=add-paper.yml) |
| 19 | DAS | conference | **3** | [➕](../../issues/new?template=add-paper.yml) |
| 20 | RecSys | conference | — | [➕](../../issues/new?template=add-paper.yml) |
| 21 | IEEE TPAMI | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 22 | IJCV | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 23 | JMLR | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 24 | AIJ | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 25 | IEEE TIP | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 26 | IJDAR | journal | **7** | [➕](../../issues/new?template=add-paper.yml) |
| 27 | IEEE TMM | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 28 | ACM TOIS | journal | **4** | [➕](../../issues/new?template=add-paper.yml) |
| 29 | Pattern Recognition | journal | **5** | [➕](../../issues/new?template=add-paper.yml) |
| 30 | IP&M | journal | **1** | [➕](../../issues/new?template=add-paper.yml) |
| 31 | TACL | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 32 | Computational Linguistics | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 33 | IEEE TNNLS | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 34 | Neural Networks | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 35 | KBS | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 36 | CVIU | journal | **1** | [➕](../../issues/new?template=add-paper.yml) |
| 37 | Information Sciences | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 38 | ACM TIST | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 39 | ESWA | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| 40 | IEEE Access | journal | — | [➕](../../issues/new?template=add-paper.yml) |
| | Other venues | mixed | 29 | [➕](../../issues/new?template=add-paper.yml) |
| | Preprints | preprint | 69 | [➕](../../issues/new?template=add-paper.yml) |
<!-- VENUES:END -->

---

## Every table in the survey, in full

The paper carries compact versions because it is bound by a twenty-page
limit; the full ones live here, and the paper points at them by name.

| Table | What it holds |
|---|---|
| **[Surveys](data/surveys.md)** | all competing and adjacent surveys with the axis each organises by |
| **[Channels](data/channels.md)** | per-channel tables: what each work does, what it was measured on, why it matters |
| **[What encoders keep and lose](data/encoding.md)** | eight encoder families against what they preserve and destroy, every judgement cited |
| **[Methods](data/methods.md)** | systems by paradigm, with backbone, index type and granularity |
| **[The matrix](data/matrix.md)** | channels × paradigms; the blanks are the finding |
| **[Datasets](data/datasets.md)** | benchmarks against the eight channels, with a PRIMARY/SECONDARY flag on every scale figure |
| **[Venues](data/venues.md)** | every venue searched and its yield, including the ones that yielded nothing |
| **[Notation](data/notation.md)** | every symbol, and the three terms this literature uses inconsistently |
| **[Variance](data/variance.md)** | configuration settings against how often they are disclosed |
| **[Checklist](data/checklist.md)** | the 18 reporting items, copyable |

## The released record

| File | What it is |
|---|---|
| [`data/references.csv`](data/references.csv) | all 286 references with venue, year, pages, DOI, arXiv id, venue tag and channel group |
| [`data/screened_pool.csv`](data/screened_pool.csv) | the retained pool with screening decisions |
| [`data/results_record.csv`](data/results_record.csv) | one row per (method, benchmark, metric, value), **with the paper the value was read from** |

### Four fields that do not exist elsewhere

**`REPORTED_IN`** in the results record names the paper a value was *read
from*, which is not always the paper that produced it. No comparable
table carries this field, and it is the reason the reporting disagreement
measured in the survey has never been measured before.

**`scale_provenance`** in the dataset registry marks whether a query or
document count came from the introducing paper's own abstract (PRIMARY)
or from a downstream table (SECONDARY).

**`unit`** records whether a count is in pages or in documents. Some
benchmarks count a multi-page file as one document, and the two are not
interchangeable when corpus sizes are compared.

**A blank cell in the matrix** means no work in the pool reports a result
for that channel under that paradigm. It does not mean the combination is
impossible; under a looser inclusion rule every cell would fill.

The method table applies the same discipline to itself: values we believe
but did not verify against the paper's own text carry a †, and the rows
still missing a backbone are [listed by
name](data/methods.md#what-is-missing) rather than left quietly blank.

---

## Citation

```bibtex
@article{anon2026channels,
  title   = {Eight Channels, One Vector: A Survey of Retrieval-Augmented
             Visual Document Understanding},
  author  = {Anonymous},
  journal = {under review},
  year    = {2026}
}
```

## Licence

[CC BY 4.0](LICENSE). The cited papers remain under their publishers' terms.
