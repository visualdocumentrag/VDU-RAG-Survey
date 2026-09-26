# Plain Text

The characters and their reading order; since order belongs to the layout, perfect character accuracy can still yield an unreadable stream. Four families recognize text: engineered recognizers, sequence models, OCR-free models that generate structured output from pixels, and compact vision-language models that emit markdown, layout and reading order together. Parsing converged on emitting structure just as retrieval converged on vectors that keep none.

## Coverage in the channel x paradigm matrix (paper Table 7)

|OCR -> LLM|MLLM-native|Text RAG|Visual RAG|
|:-:|:-:|:-:|:-:|
|✓|✓|✓|✓|

✓ results reported; ○ established task, but no method of that paradigm reports on it; ✗ nothing reported.

## Benchmarks that annotate this channel

- [ViDoRe v1](https://openreview.net/forum?id=ogjBpZ8uSi) (2025)
- [ViDoRe v2](https://arxiv.org/abs/2505.17166) (2025)
- [ViDoRe v3](https://aclanthology.org/2026.acl-long.755/) (2026)
- [MMDocIR](https://aclanthology.org/2025.emnlp-main.1576/) (2025)
- [MMDocRAG](https://scholar.google.com/scholar?q=Benchmarking+Retrieval-Augmented+Multimodal+Generation+for+Document+Question+Answering) (2025)
- [M3DocVQA](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html) (2025)
- [ViDoSeek](https://aclanthology.org/2025.emnlp-main.464/) (2025)
- [UniDoc-Bench](https://arxiv.org/abs/2510.03663) (2025)
- [SciEGQA](https://yuwenhan07.github.io/SciEGQA-project/) (2025)
- [DocVQA](https://doi.org/10.1109/WACV48630.2021.00225) (2021)
- [InfographicVQA](https://scholar.google.com/scholar?q=InfographicVQA) (2022)
- [TAT-DQA](https://scholar.google.com/scholar?q=Towards+Complex+Document+Understanding+by+Discrete+Reasoning) (2022)
- [SPIQA](https://scholar.google.com/scholar?q=SPIQA%3A+A+Dataset+for+Multimodal+Question+Answering+on+Scientific+Papers) (2024)
- [LongDocURL](https://aclanthology.org/2025.acl-long.57/) (2025)
- [MTVQA](https://aclanthology.org/2025.findings-acl.404/) (2025)
- [FUNSD](https://scholar.google.com/scholar?q=FUNSD%3A+A+Dataset+for+Form+Understanding+in+Noisy+Scanned+Documents) (2019)
- [VRDU](https://doi.org/10.1145/3580305.3599929) (2023)
- [DocLayNet](https://doi.org/10.1145/3534678.3539043) (2022)
- [TexTAR](https://doi.org/10.1007/978-3-032-04614-7_16) (2025)

## Benchmarks where the channel is present but not annotated

- [ChartQA](https://scholar.google.com/scholar?q=ChartQA%3A+A+Benchmark+for+Question+Answering+about+Charts+with+Visual+and+Logical+Reasoning) (2022)
- [PubTables-1M](https://scholar.google.com/scholar?q=PubTables-1M%3A+Towards+Comprehensive+Table+Extraction+from+Unstructured+Documents) (2022)
- [UniMER](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_UniMERNet_A_Universal_Network_for_Real-World_Mathematical_Expression_Recognition_CVPR_2026_paper.html) (2026)
- [SPODS](https://doi.org/10.1007/978-3-319-68124-5_19) (2017)
- [ReST](https://scholar.google.com/scholar?q=ICDAR+2023+Competition+on+Reading+the+Seal+Title) (2023)
- [DKDS](https://doi.org/10.1007/s10032-026-00595-5) (2026)

## Works cited for this channel in the paper

|Paper|Venue|Year|
|---|---|---|
|[An Overview of the Tesseract OCR Engine](https://scholar.google.com/scholar?q=An+Overview+of+the+Tesseract+OCR+Engine)|Proc. Int. Conf. Document Analysis and Recognition (ICDAR)|2007|
|[TrOCR: Transformer-Based Optical Character Recognition with Pre-trained Models](https://scholar.google.com/scholar?q=TrOCR%3A+Transformer-Based+Optical+Character+Recognition+with+Pre-trained+Models)|Proc. AAAI Conf. Artificial Intelligence|2023|
|[OCR-free Document Understanding Transformer](https://scholar.google.com/scholar?q=OCR-free+Document+Understanding+Transformer)|Proc. Eur. Conf. Comput. Vis. (ECCV)|2022|
|[End-to-End Document Recognition and Understanding with Dessurt](https://scholar.google.com/scholar?q=End-to-End+Document+Recognition+and+Understanding+with+Dessurt)|Proc. Eur. Conf. Comput. Vis. Workshops (ECCVW)|2022|
|[DocParser: End-to-End OCR-free Information Extraction from Visually Rich Documents](https://arxiv.org/abs/2304.12484)|Proc. Int. Conf. Document Analysis and Recognition (ICDAR)|2023|
|[TextMonkey: An OCR-free Large Multimodal Model for Understanding Document](https://doi.org/10.1109/tpami.2026.3653415)|IEEE Trans. Pattern Anal. Mach. Intell.|2026|
|[dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model](https://arxiv.org/abs/2512.02498)|arXiv preprint arXiv:2512.02498|2025|
|[MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm](https://arxiv.org/abs/2506.05218)|arXiv preprint arXiv:2506.05218|2025|
|[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://arxiv.org/abs/2510.14528)|arXiv preprint arXiv:2510.14528|2025|

[Back to the channels](../../README.md#the-eight-channels)