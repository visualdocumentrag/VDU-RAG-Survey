# Comparison with existing surveys

The **organising axis** column does the work here, not the ticks. Read it
downward: pipeline stage, pipeline stage, role of the MLLM, LLM
capability, task family, modality, QA task. **Seven axes, and none of them
is what the page contains.**

● treated in depth · ○ partial · – not treated

*Chan.* organises by content type on the page · *Interf.* formalises
interaction between co-located types · *Audit* measures the consistency of
the record rather than tabulating it · *Metric* contributes an evaluation
instrument · *Mult.* reports coverage by script or language.

### Direct competitors: multimodal RAG for document understanding

| Survey | Venue | Year | Organising axis | Chan. | Interf. | Audit | Metric | Mult. |
|---|---|:-:|---|:-:|:-:|:-:|:-:|:-:|
| [Gao et al.](https://arxiv.org/abs/2510.15253) | ACL | 2026 | pipeline stage: parse, retrieve, generate | – | – | – | – | ○ |
| [Yan et al.](https://arxiv.org/abs/2602.19961) | preprint | 2026 | pipeline stage: benchmark, embed, rerank, agent | – | – | – | – | – |
| [Zhang](https://arxiv.org/abs/2601.03262) | AACL | 2025 | role of the MLLM: captioner, embedder, representer | – | – | – | – | – |
| — | TOIS | 2026 | LLM capability applied to document tasks | – | – | – | – | ○ |

### Adjacent: visually rich document understanding, without retrieval

| Survey | Venue | Year | Organising axis | Chan. | Interf. | Audit | Metric | Mult. |
|---|---|:-:|---|:-:|:-:|:-:|:-:|:-:|
| Ding et al. | ACL | 2026 | MLLM framework capability | – | – | – | – | ○ |
| [Ding et al.](https://arxiv.org/abs/2408.01287) | AI Rev. | 2026 | task family: extraction, VQA, layout | – | – | – | – | – |
| Fu et al. | ACL | 2025 | model architecture for text-rich images | – | – | – | – | – |
| [Zhang et al.](https://arxiv.org/abs/2410.21169) | preprint | 2024 | parsing technique | – | – | – | – | – |
| [Wang et al.](https://arxiv.org/abs/2510.13366) | preprint | 2025 | document task taxonomy | – | – | – | – | – |
| Nandi & Sathya | CVIP | 2024 | method family | – | – | – | – | – |
| [—](https://arxiv.org/abs/2501.02235) | preprint | 2025 | question-answering task | – | – | – | – | – |
| [—](https://arxiv.org/abs/2601.12318) | preprint | 2026 | data-generation method | – | – | – | – | – |

### Adjacent: multimodal or general retrieval-augmented generation

| Survey | Venue | Year | Organising axis | Chan. | Interf. | Audit | Metric | Mult. |
|---|---|:-:|---|:-:|:-:|:-:|:-:|:-:|
| Abootorabi et al. | ACL | 2025 | retrieval modality | – | – | – | – | ○ |
| [Mei et al.](https://arxiv.org/abs/2504.08748) | preprint | 2025 | retrieval modality | – | – | – | – | – |
| [Zhao et al.](https://arxiv.org/abs/2503.18016) | preprint | 2025 | vision task | – | – | – | – | – |
| [Gao et al.](https://arxiv.org/abs/2312.10997) | preprint | 2023 | RAG paradigm: naive, advanced, modular | – | – | – | – | – |

### Not a survey; the only prior re-examination of this record

| Survey | Venue | Year | Organising axis | Chan. | Interf. | Audit | Metric | Mult. |
|---|---|:-:|---|:-:|:-:|:-:|:-:|:-:|
| [Qiao et al.](https://doi.org/10.1145/3726302.3730285) | SIGIR | 2025 | reproducibility of late interaction | – | – | ● | – | – |

### This survey

| Survey | Venue | Year | Organising axis | Chan. | Interf. | Audit | Metric | Mult. |
|---|---|:-:|---|:-:|:-:|:-:|:-:|:-:|
| **This survey** | — | 2026 | **content channel on the page** | ● | ● | ● | ● | ● |

---

## Why Qiao et al. is in the table

It is not a survey, and it is the only prior work that shares the **Audit**
column: it re-examines reported results for visual document retrieval
rather than tabulating them. They re-ran a small number of systems under
one protocol; we analyse the reported record at scale. Complementary, not
competing — and a reviewer who knows that paper will look for exactly this
row.
