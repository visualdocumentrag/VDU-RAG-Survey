# Datasets and benchmarks (61)

Cut-off: 24 September 2026. Source: [`data/datasets.csv`](../data/datasets.csv).

## 1. Channel coverage of key benchmarks (paper Table 8)

● annotated, ○ present but not annotated, – absent; a blank cell is not reported in a form we could verify.

|Task|Dataset|Venue|Year|Lang.|Size|Queries|Metric|Text|Layout|Tables|Figures|Equations|Forms|Stamps|Typography|Public|Paper|Data|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Retrieval & RAG|ViDoRe v1|ICLR|2025|EN, FR|||nDCG@5|●|○|○|○|○|○|–|–|yes|[paper](https://openreview.net/forum?id=ogjBpZ8uSi)|[link](https://huggingface.co/collections/vidore/vidore-benchmark)|
|Retrieval & RAG|ViDoRe v2|arXiv|2025|multi||||●|○|○|○|○|○|–|–|yes|[paper](https://arxiv.org/abs/2505.17166)|[link](https://huggingface.co/collections/vidore/vidore-benchmark-v2)|
|Retrieval & RAG|ViDoRe v3|ACL|2026|6 langs||||●|●|●|●|○|○|–|–|yes|[paper](https://aclanthology.org/2026.acl-long.755/)|[link](https://huggingface.co/collections/vidore/vidore-benchmark-v3)|
|Retrieval & RAG|MMDocIR|EMNLP|2025|EN||||●|●|●|●|○|○|–|–|yes|[paper](https://aclanthology.org/2025.emnlp-main.1576/)|[link](https://huggingface.co/MMDocIR)|
|Retrieval & RAG|MMDocRAG|NeurIPS|2025|EN||||●|○|●|●|○|○|–|–|yes|[paper](https://scholar.google.com/scholar?q=Benchmarking+Retrieval-Augmented+Multimodal+Generation+for+Document+Question+Answering)|[link](https://github.com/MMDocRAG/MMDocRAG)|
|Retrieval & RAG|M3DocVQA|ICCVW|2025|EN|40K+ pages|||●|○|○|●|○|○|–|–|yes|[paper](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html)|[link](https://github.com/bloomberg/m3docrag)|
|Retrieval & RAG|ViDoSeek|EMNLP|2025|EN||||●|○|○|○|○|○|–|–|yes|[paper](https://aclanthology.org/2025.emnlp-main.464/)|[link](https://github.com/Alibaba-NLP/ViDoRAG)|
|Retrieval & RAG|UniDoc-Bench|arXiv|2025|EN|70K pages|||●|●|●|○|○|○|–|–|yes|[paper](https://arxiv.org/abs/2510.03663)|[link](https://github.com/SalesforceAIResearch/UniDOC-Bench)|
|Retrieval & RAG|SciEGQA|arXiv|2025|EN|3.6K docs|32K||●|●|○|○|○|○|–|–|no|[paper](https://yuwenhan07.github.io/SciEGQA-project/)|[link](https://yuwenhan07.github.io/SciEGQA-project/)|
|Document QA|DocVQA|WACV|2021|EN|12,767 images|50,000|ANLS|●|○|○|–|–|○|–|–|yes|[paper](https://doi.org/10.1109/WACV48630.2021.00225)|[link](https://www.docvqa.org)|
|Document QA|InfographicVQA|WACV|2022|EN|5,485 images|30,035|ANLS|●|●|○|●|–|–|–|–|yes|[paper](https://scholar.google.com/scholar?q=InfographicVQA)|[link](https://www.docvqa.org)|
|Document QA|ChartQA|ACL Find.|2022|EN|20,882 charts|32,719|relaxed acc.|○|–|–|●|–|–|–|–|yes|[paper](https://scholar.google.com/scholar?q=ChartQA%3A+A+Benchmark+for+Question+Answering+about+Charts+with+Visual+and+Logical+Reasoning)|[link](https://github.com/vis-nlp/ChartQA)|
|Document QA|TAT-DQA|ACM MM|2022|EN|2,758 docs|16,558|EM, F1|●|○|●|–|–|–|–|–|yes|[paper](https://scholar.google.com/scholar?q=Towards+Complex+Document+Understanding+by+Discrete+Reasoning)|[link](https://github.com/NExTplusplus/TAT-DQA)|
|Document QA|SPIQA|NeurIPS|2024|EN||270K||●|○|●|●|○|–|–|–|yes|[paper](https://scholar.google.com/scholar?q=SPIQA%3A+A+Dataset+for+Multimodal+Question+Answering+on+Scientific+Papers)|[link](https://huggingface.co/datasets/google/spiqa)|
|Document QA|LongDocURL|ACL|2025|EN|396 docs|2,325||●|●|●|●|○|○|–|–|yes|[paper](https://aclanthology.org/2025.acl-long.57/)|[link](https://github.com/dengc2023/LongDocURL)|
|Document QA|MTVQA|ACL Find.|2025|9 langs||||●|○|○|○|–|○|–|–|yes|[paper](https://aclanthology.org/2025.findings-acl.404/)|[link](https://github.com/bytedance/MTVQA)|
|Channel-specific|FUNSD|ICDARW|2019|EN|199 forms||F1|●|○|–|–|–|●|–|–|yes|[paper](https://scholar.google.com/scholar?q=FUNSD%3A+A+Dataset+for+Form+Understanding+in+Noisy+Scanned+Documents)|[link](https://guillaumejaume.github.io/FUNSD/)|
|Channel-specific|VRDU|KDD|2023|EN||||●|○|–|–|–|●|–|–|yes|[paper](https://doi.org/10.1145/3580305.3599929)|[link](https://github.com/google-research-datasets/vrdu)|
|Channel-specific|DocLayNet|KDD|2022|EN|80,863 pages||mAP|●|●|●|●|●|–|–|–|yes|[paper](https://doi.org/10.1145/3534678.3539043)|[link](https://github.com/DS4SD/DocLayNet)|
|Channel-specific|PubTables-1M|CVPR|2022|EN|||GriTS|○|○|●|–|–|–|–|–|yes|[paper](https://scholar.google.com/scholar?q=PubTables-1M%3A+Towards+Comprehensive+Table+Extraction+from+Unstructured+Documents)|[link](https://github.com/microsoft/table-transformer)|
|Channel-specific|UniMER|CVPR|2026|||||○|–|–|–|●|–|–|–|yes|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_UniMERNet_A_Universal_Network_for_Real-World_Mathematical_Expression_Recognition_CVPR_2026_paper.html)|[link](https://github.com/opendatalab/UniMERNet)|
|Channel-specific|SPODS|ICVGIP-W|2017|||||○|○|–|–|–|–|●|–|yes|[paper](https://doi.org/10.1007/978-3-319-68124-5_19)|[link](https://facweb.iitkgp.ac.in/~jay/spods/index.html)|
|Channel-specific|ReST|ICDAR|2023|ZH||||○|–|–|–|–|–|●|–|no|[paper](https://scholar.google.com/scholar?q=ICDAR+2023+Competition+on+Reading+the+Seal+Title)||
|Channel-specific|DKDS|IJDAR|2026|JA||||○|○|–|–|–|–|●|–|yes|[paper](https://doi.org/10.1007/s10032-026-00595-5)|[link](https://github.com/RuiyangJu/DKDS)|
|Channel-specific|TexTAR|ICDAR|2025|multi||||●|○|–|–|–|–|–|●|yes|[paper](https://doi.org/10.1007/978-3-032-04614-7_16)|[link](https://github.com/tex-tar/tex-tar)|

## 2. Benchmarks released at 2025-2026 venues (36)

Found in the venue lists of the survey; not yet channel-annotated. *Focus* follows the paper title; links are those stated in the paper.

|Group|Dataset|Venue|Focus|Paper|Data / code|
|---|---|---|---|---|---|
|Retrieval & RAG|REAL-MM-RAG|ACL'25|Real-world multimodal retrieval|[paper](https://aclanthology.org/2025.acl-long.1528/)||
|Retrieval & RAG|MRAG-Bench|ICLR'25|Vision-centric evaluation of retrieval-augmented multimodal models|[paper](https://openreview.net/forum?id=Usklli4gMc)||
|Retrieval & RAG|OHR-Bench|ICCV'25|Cascading impact of OCR errors on RAG|[paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html)|[link](https://github.com/opendatalab/OHR-Bench)|
|Retrieval & RAG|DocMMIR|EMNLP'25|Document multimodal information retrieval|[paper](https://aclanthology.org/2025.findings-emnlp.705/)||
|Retrieval & RAG|Chart-MRAG|ACL'26|Multimodal RAG on charts|[paper](https://aclanthology.org/2026.acl-long.1164/)||
|Retrieval & RAG|FinMRAGBench|ACL'26|Multimodal RAG in finance|[paper](https://aclanthology.org/2026.findings-acl.187/)|[link](https://github.com/sqyangit/FinMRAGBench)|
|Retrieval & RAG|T2-RAGBench|EACL'26|Text-and-table RAG|[paper](https://aclanthology.org/2026.eacl-long.8/)|[link](https://github.com/uhh-hcds/g4kmu-paper)|
|Retrieval & RAG|DocRetriever|KDD'26|Multimodal document retrieval|[paper](https://doi.org/10.1145/3770855.3817680)||
|Retrieval & RAG|CRAG-MM|KDD'26|Multimodal, multi-turn comprehensive RAG|[paper](https://doi.org/10.1145/3770855.3817544)|[link](https://huggingface.co/crag-mm-2025)|
|Retrieval & RAG|RAViG-Bench|KDD'26|Retrieval-augmented visually-rich generation|[paper](https://doi.org/10.1145/3770855.3817479)|[link](https://github.com/antgroup/ravig-bench)|
|Retrieval & RAG|Fix Before Search|ICML'26|Agentic visual query pre-processing for multimodal retrieval|[paper](https://openreview.net/forum?id=c6KQjNRo1m)|[link](https://github.com/phycholosogy/VQQP_Bench)|
|Retrieval & RAG|CMDR|ECCV'26|Contextual multimodal document retrieval|[paper](https://eccv.ecva.net/virtual/2026/poster/5332)||
|Retrieval & RAG|MultiHaystack|ECCV'26|Retrieval and reasoning over 40K images, videos and documents|[paper](https://eccv.ecva.net/virtual/2026/poster/3784)||
|Long-document QA and reasoning|Document Haystacks|CVPR'25|Reasoning over piles of 1000+ documents|[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Document_Haystacks__Vision-Language_Reasoning_Over_Piles_of_1000_Documents_CVPR_2025_paper.html)||
|Long-document QA and reasoning|M-LongDoc|EMNLP'25|Multimodal super-long documents|[paper](https://aclanthology.org/2025.emnlp-main.469/)||
|Long-document QA and reasoning|PaperScope|ACL'26|Multi-modal, multi-document agentic deep research|[paper](https://aclanthology.org/2026.findings-acl.394/)||
|Long-document QA and reasoning|SciMDR|ACL'26|Scientific multimodal document reasoning|[paper](https://aclanthology.org/2026.acl-long.2070/)||
|Long-document QA and reasoning|Doc-PP|ACL'26|Document policy preservation in LVLMs|[paper](https://aclanthology.org/2026.findings-acl.832/)||
|Long-document QA and reasoning|DocHop|ICML'26|Out-of-domain multi-hop reasoning in information-dense documents|[paper](https://openreview.net/forum?id=PQFkScoGqz)||
|Long-document QA and reasoning|Strategic Navigation|ICML'26|How agents and humans reason over document collections|[paper](https://openreview.net/forum?id=ds3ZOevkwx)||
|Long-document QA and reasoning|VinQA|CVPR'26|Long-form answers interleaved with visual elements|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jang_VinQA_Visual_Elements_Interleaved_Long-form_Answer_Generation_for_Real-World_Multimodal_CVPR_2026_paper.html)||
|Long-document QA and reasoning|EviFiVQA|ICDAR'25|Evidence-grounded multi-hop reasoning in finance|[paper](https://doi.org/10.1007/978-3-032-04627-7_34)||
|Grounding, parsing and OCR|BoundingDocs|IJDAR'25|Document QA with spatial annotations|[paper](https://doi.org/10.1007/s10032-025-00563-5)||
|Grounding, parsing and OCR|DoCoG|ECCV'26|Multi-type grounded chain-of-thought for document QA|[paper](https://eccv.ecva.net/virtual/2026/poster/3695)||
|Grounding, parsing and OCR|M3Grounder|CVPR'26|Multi-span, multi-granular grounding for document QA|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Venna_M3Grounder_Mask-Based_Multi-Span_and_Multi-Granular_Grounding_for_Document_QA_CVPR_2026_paper.html)||
|Grounding, parsing and OCR|Uni-DocRobust|ICML'26|Robustness of multimodal document understanding|[paper](https://openreview.net/forum?id=ErZRlWv8kZ)||
|Grounding, parsing and OCR|OmniDocBench|CVPR'25|PDF document parsing|[paper](https://doi.org/10.1109/CVPR52734.2025.02313)|[link](https://github.com/opendatalab/OmniDocBench)|
|Grounding, parsing and OCR|Real5-OmniDocBench|ECCV'26|Physical reconstruction benchmark for robust parsing|[paper](https://eccv.ecva.net/virtual/2026/poster/5777)||
|Grounding, parsing and OCR|BigDocs|ICLR'25|Open training data for document and code tasks|[paper](https://openreview.net/forum?id=b1ivBPLb1n)||
|Grounding, parsing and OCR|CC-OCR|ICCV'25|OCR ability of large multimodal models|[paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_CC-OCR_A_Comprehensive_and_Challenging_OCR_Benchmark_for_Evaluating_Large_ICCV_2025_paper.html)||
|Grounding, parsing and OCR|OCR or Not?|EACL'26|Document information extraction in the MLLM era|[paper](https://aclanthology.org/2026.eacl-industry.28/)||
|Multilingual and Indic|SEA-Vision|CVPR'26|Multilingual document and scene text understanding|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yue_SEA-Vision_A_Multilingual_Benchmark_for_Comprehensive_Document_and_Scene_Text_CVPR_2026_paper.html)||
|Multilingual and Indic|BaFCo|ECCV'26|Complex Bangla form comprehension|[paper](https://eccv.ecva.net/virtual/2026/poster/5793)|[link](https://huggingface.co/datasets/Mausul/bafco)|
|Multilingual and Indic|HW-MLVQA|IJDAR'25|Handwritten multilingual VQA|[paper](https://doi.org/10.1007/s10032-025-00560-8)||
|Multilingual and Indic|IndicDLP|ICDAR'25|Multilingual, multi-domain Indic layout parsing|[paper](https://doi.org/10.1007/978-3-032-04614-7_2)||
|Multilingual and Indic|IndianPCL|IJDAR'26|Multimodal legal document understanding|[paper](https://doi.org/10.1007/s10032-026-00601-w)||