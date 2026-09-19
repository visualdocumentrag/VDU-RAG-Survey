# Datasets and benchmarks: channel coverage

Table 6 of the survey. **●** annotated · **○** present but not annotated · **–** absent. Annotation, not presence, is what permits a channel-specific result.

Scale is given only where we read it from the introducing paper itself; ViDoRe v3 comprises about 26,000 pages and 3,099 human-verified queries, each in six languages, across ten datasets.


## Retrieval benchmarks

| Benchmark | Venue | Txt | Lay | Tab | Fig | Eqn | Frm | Stp | Typ | Link |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **ViDoRe v1** | ICLR 2025 | ● | ○ | ○ | ○ | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2407.01449)] |
| **ViDoRe v2** | arXiv 2025 | ● | ○ | ○ | ○ | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2505.17166)] |
| **ViDoRe v3** | ACL 2026 | ● | ● | ● | ● | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2601.08620)] |
| **MMDocIR** | EMNLP 2025 | ● | ● | ● | ● | ○ | ○ | – | – | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1576)] |
| **MMDocRAG** | NeurIPS 2025 | ● | ○ | ● | ● | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2505.16470)] |
| **M3DocVQA** | arXiv 2024 | ● | ○ | ○ | ● | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2411.04952)] |
| **ViDoSeek** | EMNLP 2025 | ● | ○ | ○ | ○ | ○ | ○ | – | – | [[DOI](https://doi.org/10.18653/v1/2025.emnlp-main.464)] |
| **BBox-DocVQA** | arXiv 2025 | ● | ● | ○ | ○ | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2511.15090)] |
| **UniDoc-Bench** | arXiv 2025 | ● | ● | ● | ○ | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2510.03663)] |

## Question-answering datasets

| Benchmark | Venue | Txt | Lay | Tab | Fig | Eqn | Frm | Stp | Typ | Link |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **DocVQA** | WACV 2021 | ● | ○ | ○ | – | – | ○ | – | – | [[DOI](https://doi.org/10.1109/WACV48630.2021.00225)] |
| **InfographicVQA** | WACV 2022 | ● | ● | ○ | ● | – | – | – | – | [[DOI](https://doi.org/10.1109/wacv51458.2022.00264)] |
| **ChartQA** | Findings ACL 2022 | ○ | – | – | ● | – | – | – | – | [[DOI](https://doi.org/10.18653/v1/2022.findings-acl.177)] |
| **TAT-DQA** | ACM MM 2022 | ● | ○ | ● | – | – | – | – | – | [[DOI](https://doi.org/10.1145/3503161.3548422)] |
| **SPIQA** | NeurIPS 2024 | ● | ○ | ● | ● | ○ | – | – | – | [[DOI](https://doi.org/10.52202/079017-3773)] |
| **LongDocURL** | arXiv 2024 | ● | ● | ● | ● | ○ | ○ | – | – | [[arXiv](https://arxiv.org/abs/2412.18424)] |
| **MTVQA** | Findings ACL 2025 | ● | ○ | ○ | ○ | – | ○ | – | – | [[arXiv](https://arxiv.org/abs/2405.11985)] |

## Channel-specific resources (used by no retrieval system)

| Benchmark | Venue | Txt | Lay | Tab | Fig | Eqn | Frm | Stp | Typ | Link |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **FUNSD** | ICDAR-W 2019 | ● | ○ | – | – | – | ● | – | – | [[DOI](https://doi.org/10.1109/icdarw.2019.10029)] |
| **PubTables-1M** | CVPR 2022 | ○ | ○ | ● | – | – | – | – | – | [[DOI](https://doi.org/10.1109/cvpr52688.2022.00459)] |
| **UniMER** | arXiv 2024 | ○ | – | – | – | ● | – | – | – | [[arXiv](https://arxiv.org/abs/2404.15254)] |
| **SPODS** | ICVGIP-W 2017 | ○ | ○ | – | – | – | – | ● | – | [[DOI](https://doi.org/10.1007/978-3-319-68124-5_19)] |
| **DKDS** | arXiv 2025 | ○ | ○ | – | – | – | – | ● | – | [[arXiv](https://arxiv.org/abs/2511.09117)] |
| **TexTAR** | ICDAR 2026 | ● | ○ | – | – | – | – | – | ● | [[arXiv](https://arxiv.org/abs/2509.13151)][[DOI](https://doi.org/10.1007/978-3-032-04614-7_16)] |

## What the two rightmost columns show

No retrieval benchmark annotates stamps (**Stp**) or typography (**Typ**). The only resources that do are two stamp and seal datasets and one typography corpus, built for detection and recognition, and no method in [`methods.md`](methods.md) evaluates on any of them.

