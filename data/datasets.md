# Datasets and benchmarks

Laid out as a dataset table, with one column that is the reason it
exists: where a survey of this kind usually has **Categories**, this
has the eight **content channels**.

**●** annotated &nbsp;·&nbsp; **○** present but unannotated &nbsp;·&nbsp; **–** absent

`Scale` is **P** where the query and document counts were read from the
introducing paper's own abstract, and **S** where they came from a
downstream table and are unverified. Three widely circulated figures
were checked against their source and all three disagreed; one of them
reached our own first-pass record from a competing survey's table.

| Dataset (Year) | Venue | Task | Queries / Docs | Unit | Scale | Txt | Lay | Tab | Fig | Eqn | Frm | Stp | Typ | Language | Link |
|---|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|:-:|
| **PlotQA** (2020) | IEEE/CVF Winter Conf.  | QA | 28.9M / 224K | images | S | – | – | – | ● | – | – | – | – | English | – · [data](https://github.com/NiteshMethani/PlotQA) |
| **DocVQA** (2021) | IEEE/CVF Winter Conf.  | QA | 50K / 12,767 | pages | P | ● | ○ | ○ | ○ | – | ○ | – | – | English | [paper](https://doi.org/10.1109/WACV48630.2021.00225) · [data](https://rrc.cvc.uab.es/?ch=17) |
| **VisualMRC** (2021) | AAAI Conf. Artificial  | QA | 30,562 / 10,197 | pages | S | ● | ● | ○ | ○ | – | – | – | – | English | – · [data](https://github.com/nttmdlab-nlp/VisualMRC) |
| **TAT-DQA** (2022) | ACM Int. Conf. Multime | QA | 16,558 / 2,758 | docs | S | ● | ○ | ● | – | – | – | – | – | English | – · [data](https://nextplusplus.github.io/TAT-DQA/) |
| **InfographicVQA** (2022) | IEEE/CVF Winter Conf.  | QA | 30K / 5.4K | images | P | ● | ○ | ○ | ● | – | – | – | – | English | – · [data](https://rrc.cvc.uab.es/?ch=17) |
| **ChartQA** (2022) | Findings of ACL | QA | 23.1K / 17.1K | charts | S | ○ | – | – | ● | – | – | – | – | English | – · [data](https://github.com/vis-nlp/ChartQA) |
| **DUDE** (2023) | IEEE/CVF Int. Conf. Co | QA | 41,491 / 4,974 | docs | S | ● | ○ | ○ | ○ | ○ | ○ | – | – | English | – · [data](https://rrc.cvc.uab.es/?ch=23) |
| **SlideVQA** (2023) | AAAI Conf. Artificial  | QA | 52K / 14.5K | slides | S | ● | ● | ○ | ● | – | – | – | – | English | – · [data](https://github.com/nttmdlab-nlp/SlideVQA) |
| **ArXivQA** (2024) | preprint arXiv:2403.00 | QA | 100K / 16.6K | figures | S | ● | ○ | ○ | ● | ○ | – | – | – | English | [paper](https://arxiv.org/abs/2403.00231) · [data](https://github.com/taesiri/ArXivQA) |
| **SPIQA** (2024) | Adv. Neural Inf. Proce | QA | 27K / 25.5K | figures | S | ● | ○ | ● | ● | ○ | – | – | – | English | – · [data](https://github.com/google/spiqa) |
| **MMLongBench-Doc** (2024) | Adv. Neural Inf. Proce | QA | 1,082 / 135 | PDFs | P | ● | ● | ● | ● | ○ | – | – | – | English | – · [data](https://mayubo2333.github.io/MMLongBench-Doc/) |
| **LongDocURL** (2024) | preprint arXiv:2412.18 | QA+loc | 2,325 / 396 | docs | S | ● | ● | ● | ● | – | – | – | – | English | [paper](https://arxiv.org/abs/2412.18424) · [data](https://longdoccurl.github.io/) |
| **ViDoRe v1** (2025) | Int. Conf. Learning Re | Retrieval | 3.8K / 8.3K | pages | S | ● | ○ | ● | ● | ○ | – | – | – | English, French | – · [data](https://huggingface.co/vidore) |
| **ViDoRe v2** (2025) | preprint arXiv:2505.17 | Retrieval | - / - | pages | S | ● | ○ | ● | ● | ○ | – | – | – | multi | [paper](https://arxiv.org/abs/2505.17166) · [data](https://huggingface.co/vidore) |
| **ViDoRe v3** (2026) | Annu. Meeting Assoc. C | Retrieval+loc | 3,099 / 26K | pages | P | ● | ● | ● | ● | ○ | ○ | – | – | 6 languages | [paper](https://arxiv.org/abs/2601.08620) · [data](https://huggingface.co/vidore) |
| **M3DocVQA** (2024) | preprint arXiv:2411.04 | Retrieval+QA | 2,441 / 3,368 | docs | S | ● | ○ | ○ | ○ | – | – | – | – | English | [paper](https://arxiv.org/abs/2411.04952) · [data](https://github.com/bloomberg/m3docrag) |
| **VisDoMBench** (2025) | Conf. North American C | Retrieval+QA | 2,271 / 1,277 | docs | S | ● | ○ | ● | ● | – | – | – | – | English | – · [data](https://github.com/manancv/VisDoM) |
| **OpenDocVQA** (2025) | IEEE/CVF Conf. Comput. | Retrieval+QA | 206K / 43K | pages | S | ● | ○ | ● | ● | ○ | ○ | – | – | English | – · [data](https://github.com/nttmdlab-nlp/VDocRAG) |
| **UniDoc-Bench** (2025) | preprint arXiv:2510.03 | Retrieval+QA | 1.6K / 70K | pages | S | ● | ○ | ● | ● | ○ | – | – | – | English | [paper](https://arxiv.org/abs/2510.03663) |
| **VisR-Bench** (2025) | preprint arXiv:2508.07 | Retrieval | 35K / 1,200 | docs | P | ● | ○ | ● | ● | ○ | – | – | – | 16 languages | [paper](https://arxiv.org/abs/2508.07493) |
| **MMDocRAG** (2025) | Adv. Neural Inf. Proce | Retrieval+QA | 4,055 / - | pages | P | ● | ● | ● | ● | ○ | – | – | – | English | [paper](https://arxiv.org/abs/2505.16470) · [data](https://mmdocrag.github.io/MMDocRAG/) |
| **BBox-DocVQA** (2025) | preprint arXiv:2511.15 | Grounding | 32K / 4.4K | docs | S | ● | ● | ○ | ○ | – | ○ | – | – | English | [paper](https://arxiv.org/abs/2511.15090) |
| **MMDocIR** (2025) | Conf. Empirical Method | Retrieval | - / - | pages | S | ● | ● | ● | ● | ○ | – | – | – | English | – · [data](https://mmdocir.github.io/) |
| **ViDoSeek** (2025) | preprint arXiv:2502.18 | Agentic retrieval | 1,142 / 300 | docs | S | ● | ○ | ● | ● | ○ | – | – | – | English | [paper](https://arxiv.org/abs/2502.18017) · [data](https://github.com/Alibaba-NLP/ViDoRAG) |
| **irpapers** (2026) | preprint arXiv:2602.17 | Retrieval+QA | - / - | pages | S | ● | ○ | ● | ● | ● | – | – | – | English | [paper](https://arxiv.org/abs/2602.17687) |
| **FUNSD** (2019) | ICDAR Workshops | KIE | - / 199 | forms | P | ● | ● | – | – | – | ● | – | – | English | – · [data](https://guillaumejaume.github.io/FUNSD/) |
| **XFUND** (2022) | Findings of ACL | KIE | - / - | forms | P | ● | ● | – | – | – | ● | – | – | 7 languages | – · [data](https://github.com/doc-analysis/XFUND) |
| **PubTabNet** (2020) | Eur. Conf. Comput. Vis | Table recog. | - / 568K | tables | P | ○ | ○ | ● | – | – | – | – | – | English | – · [data](https://github.com/ibm-aur-nlp/PubTabNet) |
| **UniMER-Test** (2024) | preprint arXiv:2404.15 | Formula recog. | 23,757 / - | exprs | P | – | – | – | – | ● | – | – | – | - | [paper](https://arxiv.org/abs/2404.15254) · [data](https://github.com/opendatalab/UniMERNet) |
| **SPODS** (2017) | ICVGIP Satellite Works | Seal detection | - / - | docs | S | ○ | ○ | – | – | – | – | ● | – | English, Indic | [paper](https://doi.org/10.1007/978-3-319-68124-5_19) |
| **DKDS** (2025) | preprint arXiv:2511.09 | Seal detection | - / - | docs | S | ○ | ○ | – | – | – | – | ● | – | Chinese | [paper](https://arxiv.org/abs/2511.09117) |
| **MMTAD (TexTAR)** (2025) | preprint arXiv:2509.13 | Typography attr. | - / - | docs | P | ● | ○ | – | – | – | – | – | ● | multi-script | [paper](https://arxiv.org/abs/2509.13151) |
| **MTVQA** (2025) | Findings of ACL | QA | 6,778 / 2,116 | images | P | ● | ○ | ○ | ○ | – | – | – | – | 9 languages | [paper](https://arxiv.org/abs/2405.11985) · [data](https://github.com/bytedance/MTVQA) |
| **MIRACL-VISION** (2025) | preprint arXiv:2505.11 | Retrieval | - / - | pages | S | ● | ○ | ○ | ○ | – | – | – | – | 18 languages | [paper](https://arxiv.org/abs/2505.11651) · [data](https://github.com/NVIDIA/MIRACL-VISION) |

---

## What the two rightmost columns show

**Stp** and **Typ** carry no ● in any retrieval benchmark above. The
only resources annotating either are channel-specific datasets built
for other purposes — two for stamps, one for typography — and no
retrieval system in [`methods.md`](methods.md) evaluates on any of the
three.

A channel that no benchmark annotates cannot be measured, and a channel
that cannot be measured will not improve. The four well-served channels
are also the four on which saturation is observed, which is what one
would expect: a benchmark saturates on what it measures.

## Adding a dataset

Add a row to [`datasets.csv`](datasets.csv). Take the query and document
counts **from the introducing paper's own abstract** and mark the row
`PRIMARY`; if you take them from anywhere else, mark it `SECONDARY` and
say where in the commit message. The flag exists so that no reader has
to take a number on trust.
