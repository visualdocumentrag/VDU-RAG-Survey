# Methods

The 33 methods of Table 4, grouped by retrieval family.


## Screenshot embedding (one vector per page)

| Method | Venue | Index | Unit | Distinguishing idea | Link |
|---|---|:-:|:-:|---|---|
| **DSE** | EMNLP 2024 | single | page | rendered page as one dense vector | [[DOI](https://doi.org/10.18653/v1/2024.emnlp-main.373)] |
| **VisRAG** | ICLR 2025 | single | page | VLM embedder and reader, no parsing | [[arXiv](https://arxiv.org/abs/2410.10594)] |
| **VisRAG 2.0** | arXiv 2025 | – | page | successor with multi-image reasoning | [[arXiv](https://arxiv.org/abs/2510.09733)] |

## Late interaction (many vectors per page)

| Method | Venue | Index | Unit | Distinguishing idea | Link |
|---|---|:-:|:-:|---|---|
| **ColPali** | ICLR 2025 | multi | page | patch vectors scored by MaxSim | [[arXiv](https://arxiv.org/abs/2407.01449)] |
| **ColFlor** | MLSP 2025 | multi | page | BERT-size retriever | [[DOI](https://doi.org/10.1109/mlsp62443.2025.11204231)] |
| **ColMate** | EMNLP 2025 | multi | page | document-adapted training objective | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-industry.145)] |
| **ModernVBERT** | arXiv 2025 | multi | page | compact bidirectional encoder | [[arXiv](https://arxiv.org/abs/2510.01149)] |
| **VLM2Vec-V2** | arXiv 2025 | – | page | general multimodal embedder | [[arXiv](https://arxiv.org/abs/2507.04590)] |
| **Serval** | arXiv 2025 | – | page | zero-shot, no task-specific training | [[arXiv](https://arxiv.org/abs/2509.15432)] |
| **MetaEmbed** | ICLR 2026 | multi | page | test-time choice of vector count | [[arXiv](https://arxiv.org/abs/2509.18095)] |
| **Nemotron ColEmbed V2** | arXiv 2026 | multi | page | industrial report, not peer-reviewed | [[arXiv](https://arxiv.org/abs/2602.03992)] |

## End-to-end visual document RAG

| Method | Venue | Index | Unit | Distinguishing idea | Link |
|---|---|:-:|:-:|---|---|
| **M3DocRAG** | arXiv 2024 | multi | page | multi-page, multi-document RAG | [[arXiv](https://arxiv.org/abs/2411.04952)] |
| **SV-RAG** | ICLR 2025 | – | page | adapts the reader as retriever | [[arXiv](https://arxiv.org/abs/2411.01106)] |
| **VDocRAG** | CVPR 2025 | – | page | one image format for retrieval and QA | [[DOI](https://doi.org/10.1109/cvpr52734.2025.02312)] |
| **DocAgent** | EMNLP 2025 | – | page | agentic long-context understanding | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-main.893)] |
| **VisDoMRAG** | NAACL 2025 | – | page | text and visual paths made to agree | [[DOI](https://doi.org/10.18653/v1/2025.naacl-long.310)] |
| **CMRAG** | arXiv 2025 | – | page | co-modality text and pixels | [[arXiv](https://arxiv.org/abs/2509.02123)] |
| **MoLoRAG** | EMNLP 2025 | – | page | logic-aware retrieval over page relations | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-main.708)] |
| **HKRAG** | arXiv 2025 | – | – | holistic knowledge construction | [[arXiv](https://arxiv.org/abs/2511.20227)] |
| **HEAVEN** | arXiv 2025 | hybrid | page | single-vector then multi-vector stage | [[arXiv](https://arxiv.org/abs/2510.22215)] |
| **HiKEY** | arXiv 2026 | – | – | hierarchical open-domain retrieval | [[arXiv](https://arxiv.org/abs/2605.29606)] |

## Region- and layout-level retrieval

| Method | Venue | Index | Unit | Distinguishing idea | Link |
|---|---|:-:|:-:|---|---|
| **VISA** | ACL 2025 | – | region | page retrieval with evidence box | [[DOI](https://doi.org/10.18653/v1/2025.acl-long.1456)] |
| **LFRAG** | arXiv 2026 | – | region | layout-oriented fine-grained retrieval | [[arXiv](https://arxiv.org/abs/2605.22829)] |
| **RegionRAG** | AAAI 2026 | – | region | indexes and returns sub-page regions | [[DOI](https://doi.org/10.1609/aaai.v40i8.37597)] |
| **RegionSLM** | SIGIR 2026 | – | region | region unit with a small reader | [[DOI](https://doi.org/10.1145/3805712.3809603)] |
| **LAD-RAG** | ACL 2026 | graph | graph | layout-aware graph retrieval | [[DOI](https://doi.org/10.18653/v1/2026.acl-long.724)] |
| **LMS-Retrieval** | ICDAR 2026 | – | region | layout-, modality-, structure-aware | [[DOI](https://doi.org/10.1007/978-3-032-36039-7_8)] |
| **ColParse** | arXiv 2026 | multi | region | parser chooses the regions to embed | [[arXiv](https://arxiv.org/abs/2603.01666)] |

## Agentic document RAG

| Method | Venue | Index | Unit | Distinguishing idea | Link |
|---|---|:-:|:-:|---|---|
| **ViDoRAG** | EMNLP 2025 | – | page | multi-agent iterative refinement | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-main.464)] |
| **MDocAgent** | arXiv 2025 | – | page | text and image agents in parallel | [[arXiv](https://arxiv.org/abs/2503.13964)] |
| **SlideAgent** | ACL 2026 | – | – | hierarchical multi-page navigation | [[DOI](https://doi.org/10.18653/v1/2026.acl-long.677)] |
| **DocLens** | arXiv 2025 | – | region | tool-augmented agents on regions | [[arXiv](https://arxiv.org/abs/2511.11552)] |
| **MARDoc** | arXiv 2026 | – | – | memory-aware refinement | [[arXiv](https://arxiv.org/abs/2606.05749)] |
