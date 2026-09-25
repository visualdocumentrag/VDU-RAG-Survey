# Layout Structure

Columns, blocks, headers, captions, reading order and containment. Layout is *relational*: a block's meaning depends on its neighbors. Geometric decomposition came first, detection followed large annotated corpora, and reading order and hierarchy became learnable targets. Another family injects layout into language models as tokens, positions or supervision.

## Coverage in the channel x paradigm matrix (paper Table 7)

|OCR -> LLM|MLLM-native|Text RAG|Visual RAG|
|:-:|:-:|:-:|:-:|
|✓|✓|✓|✓|

✓ results reported; ○ established task, but no method of that paradigm reports on it; ✗ nothing reported.

## Benchmarks that annotate this channel

- [ViDoRe v3](https://aclanthology.org/2026.acl-long.755/) (2026)
- [MMDocIR](https://aclanthology.org/2025.emnlp-main.1576/) (2025)
- [UniDoc-Bench](https://arxiv.org/abs/2510.03663) (2025)
- [BBox-DocVQA](https://arxiv.org/abs/2511.15090) (2025)
- [InfographicVQA](https://scholar.google.com/scholar?q=InfographicVQA) (2022)
- [LongDocURL](https://aclanthology.org/2025.acl-long.57/) (2025)
- [DocLayNet](https://doi.org/10.1145/3534678.3539043) (2022)

## Benchmarks where the channel is present but not annotated

- [ViDoRe v1](https://openreview.net/forum?id=ogjBpZ8uSi) (2025)
- [ViDoRe v2](https://arxiv.org/abs/2505.17166) (2025)
- [MMDocRAG](https://scholar.google.com/scholar?q=Benchmarking+Retrieval-Augmented+Multimodal+Generation+for+Document+Question+Answering) (2025)
- [M3DocVQA](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html) (2025)
- [ViDoSeek](https://aclanthology.org/2025.emnlp-main.464/) (2025)
- [DocVQA](https://doi.org/10.1109/WACV48630.2021.00225) (2021)
- [TAT-DQA](https://scholar.google.com/scholar?q=Towards+Complex+Document+Understanding+by+Discrete+Reasoning) (2022)
- [SPIQA](https://scholar.google.com/scholar?q=SPIQA%3A+A+Dataset+for+Multimodal+Question+Answering+on+Scientific+Papers) (2024)
- [MTVQA](https://aclanthology.org/2025.findings-acl.404/) (2025)
- [FUNSD](https://scholar.google.com/scholar?q=FUNSD%3A+A+Dataset+for+Form+Understanding+in+Noisy+Scanned+Documents) (2019)
- [VRDU](https://doi.org/10.1145/3580305.3599929) (2023)
- [PubTables-1M](https://scholar.google.com/scholar?q=PubTables-1M%3A+Towards+Comprehensive+Table+Extraction+from+Unstructured+Documents) (2022)
- [SPODS](https://doi.org/10.1007/978-3-319-68124-5_19) (2017)
- [DKDS](https://doi.org/10.1007/s10032-026-00595-5) (2026)
- [TexTAR](https://doi.org/10.1007/978-3-032-04614-7_16) (2025)

## Works cited for this channel in the paper

|Paper|Venue|Year|
|---|---|---|
|[The Document Spectrum for Page Layout Analysis](https://scholar.google.com/scholar?q=The+Document+Spectrum+for+Page+Layout+Analysis)|IEEE Trans. Pattern Anal. Mach. Intell.|1993|
|[Segmentation of Page Images Using the Area Voronoi Diagram](https://scholar.google.com/scholar?q=Segmentation+of+Page+Images+Using+the+Area+Voronoi+Diagram)|Computer Vision and Image Understanding|1998|
|[PubLayNet: Largest Dataset Ever for Document Layout Analysis](https://scholar.google.com/scholar?q=PubLayNet%3A+Largest+Dataset+Ever+for+Document+Layout+Analysis)|Proc. Int. Conf. Document Analysis and Recognition (ICDAR)|2019|
|[DocLayNet: A Large Human-Annotated Dataset for Document-Layout Segmentation](https://doi.org/10.1145/3534678.3539043)|Proc. ACM SIGKDD Conf. Knowledge Discovery and Data Mining (KDD)|2022|
|[LayoutReader: Pre-training of Text and Layout for Reading Order Detection](https://doi.org/10.18653/v1/2021.emnlp-main.389)|Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)|2021|
|[Graph-based Document Structure Analysis](https://openreview.net/forum?id=Fu0aggezN9)|Proc. Int. Conf. Learning Representations (ICLR)|2025|
|[A Bounding Box is Worth One Token: Interleaving Layout and Text in a Large Language Model for Document Understanding](https://aclanthology.org/2025.findings-acl.379/)|Findings Assoc. Comput. Linguistics: ACL|2025|
|[A Simple yet Effective Layout Token in Large Language Models for Document Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_A_Simple_yet_Effective_Layout_Token_in_Large_Language_Models_CVPR_2025_paper.html)|Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR)|2025|
|[DocLayLLM: An Efficient Multi-modal Extension of Large Language Models for Text-rich Document Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_DocLayLLM_An_Efficient_Multi-modal_Extension_of_Large_Language_Models_for_CVPR_2025_paper.html)|Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR)|2025|

[Back to the channels](../../README.md#the-eight-channels)