# Methods

Laid out as a performance table: what the system *does*, what it was
measured on, and why it matters.

The **Gran.** column is the one that argues. Read it downward: page,
page, page for the whole first half, and **region** only from 2025
onward.

**† marks a value we believe but did not verify against the paper's own
text.** Unmarked values were stated by the paper or its repository; a
dash means we have not filled it. Sixteen of the rows are still largely
unfilled and are [listed by name](#what-is-missing) rather than left
quietly blank — a survey that measures how often other papers omit
their configuration cannot do the same itself.

**Scores are deliberately absent.** They belong in
[`results_record.csv`](results_record.csv) with the paper each was read
from, because a number without that field cannot be compared.

## Screenshot embedding — one vector per page

| Method | Venue | Year | Backbone | Train-free | OCR | Index | Gran. | Brief description | Highlight |
|---|---|:-:|---|:-:|:-:|:-:|:-:|---|---|
| DSE | Conf. Empirical Meth | 2024 | Phi-3-vision 4.2B | no | no | single | page | Bi-encoder over the rendered page screenshot; one dense vector per page | First to show a page image can be embedded for retrieval without OCR |
| VisRAG | Int. Conf. Learning  | 2025 | MiniCPM-V 2.0 | no | no | single | page | VLM-based embedder plus generator; end-to-end pipeline over page images | First end-to-end vision-based RAG over documents |
| [VisRAG 2.0](https://arxiv.org/abs/2510.09733) | preprint | 2025 | – | no | no | single | page | Successor generation with multi-image reasoning | Successor to the first end-to-end line |

## Late interaction — many vectors per page

| Method | Venue | Year | Backbone | Train-free | OCR | Index | Gran. | Brief description | Highlight |
|---|---|:-:|---|:-:|:-:|:-:|:-:|---|---|
| ColPali | Int. Conf. Learning  | 2025 | PaliGemma-3B | no | no | multi | page | PaliGemma patch embeddings at D=128, late-interaction MaxSim scoring | Dominant formulation; 257.5 KB index per page |
| ColFlor | IEEE Int. Workshop M | 2025 | Florence-2 0.17B | no | no | multi | page | BERT-size vision-language retriever | Efficiency end of the ColPali line |
| ColMate | Conf. Empirical Meth | 2025 | – | no | no | multi | page | Contrastive late interaction with masked text pretraining | Training-objective contribution to the same family |
| [ModernVBERT](https://arxiv.org/abs/2510.01149) | preprint | 2025 | ModernBERT + SigLIP † | no † | no † | multi † | page | Compact bidirectional vision-language encoder | Smaller backbone at comparable accuracy |
| [VLM2Vec-V2](https://arxiv.org/abs/2507.04590) | preprint | 2025 | Qwen2-VL † | no † | no † | multi † | page | Unified embedder treating pages as one modality among several | Document pages inside a general multimodal embedder |
| [Serval](https://arxiv.org/abs/2509.15432) | preprint | 2025 | – | yes † | no † | multi † | page | Zero-shot visual document retrieval with no task-specific training | Same group as the SIGIR reproducibility study |
| [MetaEmbed](https://arxiv.org/abs/2509.18095) | Int. Conf. Learning  | 2026 | – | no | no | multi | page | Test-time control over how many vectors are retained | Makes the storage-accuracy trade-off a runtime choice |
| [Nemotron ColEmbed](https://arxiv.org/abs/2602.03992) | preprint | 2026 | Llama/Nemotron VL † | no † | no † | multi † | page | Industrial multi-vector retriever | Tops current leaderboards; industrial report, not peer-reviewed |

## End-to-end visual document RAG

| Method | Venue | Year | Backbone | Train-free | OCR | Index | Gran. | Brief description | Highlight |
|---|---|:-:|---|:-:|:-:|:-:|:-:|---|---|
| [M3DocRAG](https://arxiv.org/abs/2411.04952) | preprint | 2024 | ColPali + Qwen2-VL † | no † | no † | multi † | page | Multi-modal multi-page retrieval and generation over document collections | First multi-document visual RAG |
| SV-RAG | Int. Conf. Learning  | 2025 | LoRA adapters on an MLLM † | no † | no † | – | page | Self-adaptive MLLM with LoRA adapters for evidence page retrieval | Adapts the reader rather than the retriever |
| VDocRAG | IEEE/CVF Conf. Compu | 2025 | Phi-3-vision † | no † | no † | – | page | Unified image format for retrieval and generation without parsing | Contributes the largest open retrieval+QA corpus |
| VisDoMRAG | Conf. North American | 2025 | – | no † | partial † | – | page | Parallel textual and visual pipelines with consistency-constrained fusion | Makes paradigm disagreement visible rather than silent |
| [CMRAG](https://arxiv.org/abs/2509.02123) | preprint | 2025 | – | – | partial | – | page | Co-modality RAG combining explicit text and page pixels | States the routing question from the architecture side |
| MoLoRAG | Conf. Empirical Meth | 2025 | – | – | – | – | page | Logic-aware multimodal retrieval bootstrapping document understanding | Retrieval guided by reasoning structure |
| [HKRAG](https://arxiv.org/abs/2511.20227) | preprint | 2025 | – | – | – | – | - | Holistic knowledge construction over documents | - |
| [HEAVEN](https://arxiv.org/abs/2510.22215) | preprint | 2026 | DSE + ColQwen2.5 | no | no | hybrid | page | Two-stage: single-vector first stage, multi-vector second, layout-guided | Reports compute against accuracy, not storage |
| [HiKEY](https://arxiv.org/abs/2605.29606) | preprint | 2026 | – | – | – | – | - | Hierarchical multimodal retrieval for open-domain document QA | Hierarchical retrieval, Sec. VI-C granularity |

## Region- and layout-level retrieval

| Method | Venue | Year | Backbone | Train-free | OCR | Index | Gran. | Brief description | Highlight |
|---|---|:-:|---|:-:|:-:|:-:|:-:|---|---|
| VISA | Annu. Meeting Assoc. | 2025 | – | no † | no † | – | **region** | Retrieves the page and returns the bounding box of the supporting evidence | Attribution at the region while indexing the page |
| [LFRAG](https://arxiv.org/abs/2605.22829) | preprint | 2026 | – | – | – | – | **region** | Layout-oriented fine-grained retrieval | Layout as the retrieval unit |
| RegionRAG | AAAI Conf. Artificia | 2026 | – | no | no | – | **region** | Indexes and returns sub-page regions directly | Retrieval unit below the page |
| [RegionSLM](https://doi.org/10.1145/3805712.3809603) | Int. ACM SIGIR Conf. | 2026 | – | – | – | – | **region** | Region-level retrieval for screenshot-based readers | Region unit with a small reader |
| LAD-RAG | Annu. Meeting Assoc. | 2026 | – | – | – | graph | graph | Layout-aware dynamic retrieval with a document graph | Structure carried into retrieval as a graph |
| [LMS-Retrieval](https://doi.org/10.1007/978-3-032-36039-7_8) | Document Analysis an | 2026 | – | – | – | – | **region** | Layout-, modality- and structure-aware document retrieval | Closest prior work on the taxonomy side |
| [ColParse](https://arxiv.org/abs/2603.01666) | preprint | 2026 | parser + multi-vector | – | yes | multi | **region** | Parser selects the regions to embed; sub-image vectors fused with a page vector | Parsing output reaches the index as UNITS, not as a label |

## Agentic

| Method | Venue | Year | Backbone | Train-free | OCR | Index | Gran. | Brief description | Highlight |
|---|---|:-:|---|:-:|:-:|:-:|:-:|---|---|
| ViDoRAG | Conf. Empirical Meth | 2025 | – | no † | no † | – | page | Multi-agent iterative refinement with Gaussian mixture retrieval | First agentic visual document RAG |
| DocAgent | – | 2025 | – | – | – | – | - | Multimodal agent for long document understanding | - |
| [MDocAgent](https://arxiv.org/abs/2503.13964) | preprint | 2025 | – | – | – | – | - | Division of labour across specialised text and image agents | Specialised agents per modality |
| SlideAgent | Annu. Meeting Assoc. | 2026 | – | – | – | – | - | Hierarchical agentic framework for multi-page visual documents | Hierarchical navigation of long documents |
| DocLens | Annu. Meeting Assoc. | 2026 | – | – | – | – | **region** | Tool-augmented multi-agent framework for long visual documents | Tool use over page regions |
| [MARDoc](https://arxiv.org/abs/2606.05749) | preprint | 2026 | – | – | – | – | - | Memory-aware refinement agent for multimodal long document QA | - |

---

## Reading the granularity column

Era I retrieved regions, Era II words and formulas, Era IV whole pages.
Over four decades in which model capacity grew by orders of magnitude,
the unit of retrieval became *coarser*.

The regression was not argued for. It followed from an engineering
convenience — the page is what an image encoder naturally accepts — and
has been treated since as the natural unit rather than as a choice.

---

## What is missing

These rows need their backbone, index type and artefact fields read
from the paper itself:

| Method | Venue | Year |
|---|---|:-:|
| [VisRAG 2.0](https://arxiv.org/abs/2510.09733) | preprint | 2025 |
| ColMate | Conf. Empirical Meth | 2025 |
| [CMRAG](https://arxiv.org/abs/2509.02123) | preprint | 2025 |
| MoLoRAG | Conf. Empirical Meth | 2025 |
| [HKRAG](https://arxiv.org/abs/2511.20227) | preprint | 2025 |
| DocAgent | – | 2025 |
| [MetaEmbed](https://arxiv.org/abs/2509.18095) | Int. Conf. Learning  | 2026 |
| [HiKEY](https://arxiv.org/abs/2605.29606) | preprint | 2026 |
| [LFRAG](https://arxiv.org/abs/2605.22829) | preprint | 2026 |
| RegionRAG | AAAI Conf. Artificia | 2026 |
| [RegionSLM](https://doi.org/10.1145/3805712.3809603) | Int. ACM SIGIR Conf. | 2026 |
| LAD-RAG | Annu. Meeting Assoc. | 2026 |
| [LMS-Retrieval](https://doi.org/10.1007/978-3-032-36039-7_8) | Document Analysis an | 2026 |
| SlideAgent | Annu. Meeting Assoc. | 2026 |
| DocLens | Annu. Meeting Assoc. | 2026 |
| [MARDoc](https://arxiv.org/abs/2606.05749) | preprint | 2026 |

**[➕ Fill one](../../../issues/new?template=add-paper.yml)** — from the
paper, not from another survey's table. A correction to a † is just as
welcome as a new row.
