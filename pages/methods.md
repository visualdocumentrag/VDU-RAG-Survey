# Methods (73)

[Paper Table 4 (HD)](figures_tables.md#table-4) · [Table 5 (HD)](figures_tables.md#table-5)

All visual document RAG methods tracked by the survey, grouped and ordered by venue exactly as in paper Tables 4-5. Cut-off: 24 September 2026.

*Objective*: what the method optimizes. *Index / Unit*: vectors stored per unit and what is returned. *Datasets*: benchmarks named at least three times in the paper's full text (or its abstract); the paper shows at most four and "+n" for the rest. **new** = added from the 2025-2026 venue lists. *Paper* opens the paper page; *link in paper* is the link printed in the paper table. Source: [`data/methods.csv`](../data/methods.csv).

[Back to README](../README.md#visual-document-rag-methods)

## CVPR

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|Evo-Retriever **new**|2026|Retriever training|document page image|ViDoRe V2, MMEB, ViDoRe|LLM-guided curriculum for multimodal document retrieval.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html) · [link in paper](https://arxiv.org/pdf/2603.16455)||
|RobustVisRAG **new**|2026|Robustness|document page image|Distortion-VisRAG|Causality-aware vision RAG under visual degradations.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_RobustVisRAG_Causality-Aware_Vision-Based_Retrieval-Augmented_Generation_under_Visual_Degradations_CVPR_2026_paper.html)|[code](https://robustvisrag.github.io/)|
|M3DocDep **new**|2026|Chunking|chunk|DUDE, MP-DocVQA|Dependency-aware chunking across pages and documents.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shin_M3DocDep_Multi-modal_Multi-page_Multi-document_Dependency_Chunking_with_Large_Vision-Language_Models_CVPR_2026_paper.html) · [link in paper](https://arxiv.org/pdf/2605.18774)||
|MARS-RL **new**|2026 Findings|RL reasoning|document page image|ViDoSeek|Multi-agent RAG on multimodal documents, trained with RL.|[paper](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_MARS-RL_Enhancing_Multi-Agent_RAG_Systems_for_Multi-Modal_Documents_via_Strategic_CVPRF_2026_paper.html)||
|Evidence-sparsity agent **new**|2026|Long-doc QA|document page image|LongDocURL, MMLongBench-Doc, PaperTab, FetaTab, ChartQA|Agentic context engineering for long documents.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Resolving_Evidence_Sparsity_Agentic_Context_Engineering_for_Long-Document_Understanding_CVPR_2026_paper.html) · [link in paper](https://arxiv.org/pdf/2511.22850)||
|VDocRAG|2025|Retrieval + QA|single / page|OpenDocVQA, InfoVQA, SlideVQA, ChartQA, DocVQA, DUDE|One image format for retrieval and QA.|[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Tanaka_VDocRAG_Retrieval-Augmented_Generation_over_Visually-Rich_Documents_CVPR_2025_paper.html)|[code](https://vdocrag.github.io/)|

## ECCV

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|LightSTAR **new**|2026|Efficiency|document page image|ViDoRe|Lightweight selection with vision-adaptive refinement.|[paper](https://eccv.ecva.net/virtual/2026/poster/4839)|[code](https://github.com/bokufa/LightSTAR)|
|UOT-EVDR **new**|2026|Efficiency|document page image|ViDoRe|Unbalanced optimal transport for efficient matching.|[paper](https://eccv.ecva.net/virtual/2026/poster/4715)|[code](https://github.com/shhhhhyy/Unbalanced-Optimal-Transport-for-EVDR)|
|MG²-RAG **new**|2026|Multimodal RAG|graph|E-VQA, InfoSeek|Multi-granularity graph for multimodal RAG.|[paper](https://eccv.ecva.net/virtual/2026/poster/3411)|[code](https://github.com/Daboolu/MG2-RAG)|
|MMAgent-R2 **new**|2026|Re-rank / reject|visual entity / candidate image|E-VQA, InfoSeek|Agentic mRAG that learns to rerank and reject.|[paper](https://eccv.ecva.net/virtual/2026/poster/4250) · [link in paper](https://arxiv.org/html/2607.07383v1)||

## ICDAR

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|LMS-Retrieval|2026|Region retrieval|multi, typed / region||Type embedding on token vectors.|[paper](https://doi.org/10.1007/978-3-032-36039-7_8)|[code](https://github.com/Lumanman9/LMS-Retrieval)|

## AAAI

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|URaG **new**|2026|Long-doc QA||SlideVQA, MMLongBench-Doc, DUDE, LongDocURL|Unified retrieval and generation inside one MLLM.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|[code](https://github.com/shi-yx/URaG)|
|RegionRAG|2026|Region retrieval|multi, grouped / region|InfoVQA, DocVQA, ArxivQA, SlideVQA, TextVQA, ViDoRe|Indexes and returns sub-page regions.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37597)|[code](https://github.com/Aeryn666/RegionRAG)|
|Look as You Think **new**|2026|Evidence attribution|document page image|VISA|Reasoning with visual evidence attribution.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40488) · [link in paper](https://arxiv.org/pdf/2511.12003)||

## WACV

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|GlobalDoc **new**|2025|Retrieval + classification|document page image|IIT-CDIP, RVL-CDIP|Cross-modal framework for real-world document image retrieval and classification.|[paper](https://openaccess.thecvf.com/content/WACV2025/html/Bakkali_GlobalDoc_A_Cross-Modal_Vision-Language_Framework_for_Real-World_Document_Image_Retrieval_WACV_2025_paper.html) · [link in paper](https://arxiv.org/pdf/2309.05756)||

## NeurIPS

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|VRAG-RL **new**|2025|RL reasoning|multimodal graph node / interleaved block|SlideVQA, ViDoSeek|Vision-perception RAG trained with RL, iterative reasoning.|[paper](https://openreview.net/forum?id=EeAHhNwXPV)|[code](https://github.com/Alibaba-NLP/VRAG)|

## EMNLP

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ColMate|2025|Retriever training|multi / page|ViDoRe, ViDoRe V2|Document-adapted training objective.|[paper](https://aclanthology.org/2025.emnlp-industry.145/) · [link in paper](https://arxiv.org/pdf/2511.00903)||
|Serval|2025|Zero-shot retrieval|textual description of document page image|ViDoRe, MIRACL-Vision|Zero-shot, no task-specific training.|[paper](https://aclanthology.org/2025.emnlp-main.1568/)|[code](https://github.com/thongnt99/serval)|
|LILaC **new**|2025|Multihop retrieval|multi|SlideVQA, MP-DocVQA, InfoVQA|Late interaction over a layered component graph, multihop.|[paper](https://aclanthology.org/2025.emnlp-main.1037/)|[code](https://github.com/joohyung00/lilac)|
|DocAgent|2025|Long-doc QA|hierarchical document outline node / tree section|MMLongBench-Doc, DocBench|Outline-guided agents for long documents.|[paper](https://doi.org/10.18653/v1/2025.emnlp-main.893)|[code](https://github.com/lisun-ai/DocAgent)|
|MoLoRAG|2025|Long-doc QA|document page node|LongDocURL, PaperTab, FetaTab|Logic-aware retrieval over page relations.|[paper](https://aclanthology.org/2025.emnlp-main.708/)|[code](https://github.com/WxxShirley/MoLoRAG)|
|SimpleDoc **new**|2025|Long-doc QA|page|DocVQA, LongDocURL, FetaTab|Dual-cue page retrieval and iterative refinement.|[paper](https://aclanthology.org/2025.emnlp-main.1443/)|[code](https://github.com/ag2ai/SimpleDoc)|
|ViDoRAG|2025|Agentic QA|hybrid / page|ViDoSeek, SlideVQA|Multi-agent iterative refinement.|[paper](https://aclanthology.org/2025.emnlp-main.464/)|[code](https://github.com/Alibaba-NLP/ViDoRAG)|
|DSE|2024|Page retrieval|single / page|Wiki-SS, SlideVQA|Rendered page as one dense vector.|[paper](https://arxiv.org/abs/2406.11251) · [link in paper](https://arxiv.org/pdf/2406.11251)||

## ACL

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|HEAVEN|2026|Efficiency|single, then multi / page|OpenDocVQA, M3DocVQA, LongDocURL, ViDoSeek, VisR-Bench, MMDocIR|Single- then multi-vector stage.|[paper](https://aclanthology.org/2026.findings-acl.54/)|[code](https://github.com/juyeonnn/HEAVEN)|
|Prune-then-Merge **new**|2026|Index size|multi, merged / page|ViDoRe, REAL-MM-RAG, MMLongBench-Doc, ViDoSeek, InfoVQA, TabFQuAD|Prunes, then merges patch vectors.|[paper](https://aclanthology.org/2026.findings-acl.1247/) · [link in paper](https://arxiv.org/pdf/2602.19549)||
|HiKEY|2026|Open-domain QA|multimodal evidence unit annotated with section paths|M3DocVQA|Hierarchical open-domain retrieval.|[paper](https://aclanthology.org/2026.acl-long.818/) · [link in paper](https://arxiv.org/pdf/2605.29606)||
|LAD-RAG|2026|Layout-aware QA|graph / region|LongDocURL, MMLongBench-Doc, DUDE, MP-DocVQA|Layout-aware graph retrieval.|[paper](https://aclanthology.org/2026.acl-long.724/) · [link in paper](https://arxiv.org/pdf/2510.07233)||
|utility-mrag **new**|2026|Evidence selection|candidate visual evidence / multimodal chunk|MRAG-Bench|Selects visual evidence by utility, not relevance.|[paper](https://aclanthology.org/2026.acl-long.1620/)|[code](https://github.com/Hcnaeg/utility-mrag)|
|SlideAgent|2026|Slide QA|hierarchical multimodal node|SlideVQA, InfoVQA, REAL-MM-RAG|Hierarchical multi-page navigation.|[paper](https://doi.org/10.18653/v1/2026.acl-long.677)|[code](https://slideagent.github.io/)|
|DocLens|2026|Long-doc QA|hierarchical document unit|MMLongBench-Doc, FinRAGBench-V|Tool-augmented agents on regions.|[paper](https://aclanthology.org/2026.acl-long.1234/)|[code](https://dwzhu-pku.github.io/DocLens/)|
|TRACE **new**|2026|Evidence chain|graph node / document page image|M5BookVQA|Traversal retrieval with a chain of evidence.|[paper](https://aclanthology.org/2026.acl-long.445/)|[code](https://github.com/shimurenhlq/TRACE)|
|ALDEN **new**|2026|RL navigation|document page image|DUDE, SlideVQA, PaperText, LongDocURL, PaperTab, DocVQA|RL for active navigation and evidence gathering.|[paper](https://aclanthology.org/2026.acl-long.611/) · [link in paper](https://arxiv.org/pdf/2510.25668)||
|MDocRAG-RL **new**|2026|RL reasoning|compressed page image / coarse-to-fine visual crops|DocStruct4M, OpenDocVQA, SlideVQA, ViDoSeek, +1|Multimodal document RAG with RL-trained visual reasoning.|[paper](https://aclanthology.org/2026.findings-acl.420/)||
|MM-Doc-R1 **new**|2026|RL reasoning|document page image|MMLongBench-Doc, DocVQA|Multi-turn RL for long-document VQA agents.|[paper](https://aclanthology.org/2026.findings-acl.1488/) · [link in paper](https://arxiv.org/pdf/2604.13579)||
|Doc-V* **new**|2026|Multi-page QA|document page image|DUDE, MMLongBench-Doc, SlideVQA, DocVQA, LongDocURL, MP-DocVQA|Coarse-to-fine interactive visual reasoning.|[paper](https://aclanthology.org/2026.acl-long.2129/)|[code](https://github.com/SeerRay-Lab/Doc-V)|
|One-Screenshot retrieval **new**|2025|Unified search|screenshot||Any content rendered as one screenshot for unified search.|[paper](https://aclanthology.org/2025.acl-long.943/) · [link in paper](https://arxiv.org/pdf/2502.11431)||
|Storage-efficient VDR **new**|2025|Index size|multi, reduced / page|ViDoRe, DocVQA, InfoVQA, MMLongBench-Doc, ChartQA|Empirical study of reducing patch-level embeddings.|[paper](https://aclanthology.org/2025.findings-acl.1003/) · [link in paper](https://arxiv.org/pdf/2506.04997)||
|NeuSym-RAG **new**|2025|PDF QA|hybrid|AirQA-Real, M3SciQA, SciDQA|Neural-symbolic retrieval over PDFs.|[paper](https://aclanthology.org/2025.acl-long.311/) · [link in paper](https://arxiv.org/pdf/2505.19754)||
|Doc-React **new**|2025|Multi-page QA|document page image / multimodal page or chunk vector|MMLongBench-Doc, SlideVQA|Multi-page heterogeneous document QA.|[paper](https://aclanthology.org/2025.acl-short.6/) · [link in paper](https://aclanthology.org/2025.acl-short.6.pdf)||
|VISA|2025|Source attribution|page + box|Wiki-VISA, Paper-VISA, FineWeb-VISA|Page retrieval with evidence box.|[paper](https://aclanthology.org/2025.acl-long.1456/) · [link in paper](https://aclanthology.org/2025.acl-long.1456.pdf)||

## ICLR

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|MetaEmbed|2026|Adaptive cost|multi, adaptive / page|MMEB, ViDoRe, ViDoRe V2|Test-time choice of vector count.|[paper](https://openreview.net/forum?id=yKDqg9HwZX)|[code](https://github.com/facebookresearch/MetaEmbed)|
|VisRAG|2025|Retrieval + QA|single / page|ArxivQA, DocVQA, ChartQA, SlideVQA, InfoVQA, MP-DocVQA|VLM embedder and reader, no parsing.|[paper](https://openreview.net/forum?id=zG459X3Xge)|[code](https://github.com/openbmb/visrag)|
|ColPali|2025|Page retrieval|multi / page|ViDoRe, TabFQuAD, DocVQA, ArxivQA, InfoVQA|Patch vectors scored by MaxSim.|[paper](https://openreview.net/forum?id=ogjBpZ8uSi)|[code](https://github.com/illuin-tech/colpali)|
|SV-RAG|2025|Long-doc QA|page|MMLongBench-Doc, SlideVQA, VisR-Bench, DocVQA, DUDE|Adapts the reader as retriever.|[paper](https://openreview.net/forum?id=FDaHjwInXO)|[code](https://github.com/puar-playground/Self-Visual-RAG)|

## ICML

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ModernVBERT|2026|Small retriever|page|ViDoRe|Compact bidirectional encoder.|[paper](https://openreview.net/forum?id=TyVJlSHke2)|[code](https://github.com/illuin-tech/modernvbert)|
|POQD **new**|2025|Query decomposition|multi|WebQA|Performance-oriented query decomposition.|[paper](https://proceedings.mlr.press/v267/liu25ag.html)|[code](https://github.com/PKU-SDS-lab/POQD-ICML25)|
|RAP **new**|2025|High-res perception|image crops|MME-RealWorld|Visual RAG for high-resolution image perception.|[paper](https://proceedings.mlr.press/v267/wang25at.html)|[code](https://github.com/DreamMr/RAP)|

## KDD

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|MM hierarchical RAG **new**|2026|Document QA|hierarchical tree node|MMLongBench-Doc, LongDocURL, PaperTab, PaperText, +1|Hierarchical multimodal RAG for document QA.|[paper](https://doi.org/10.1145/3770855.3819034) · [link in paper](https://dl.acm.org/doi/epdf/10.1145/3770855.3819034)||

## ICCVW

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|M3DocRAG|2025|Multi-doc QA|multi / page|M3DocVQA, MMLongBench-Doc, MP-DocVQA|Multi-page, multi-document RAG.|[paper](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html)|[code](https://github.com/bloomberg/m3docrag)|

## SIGIR

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ReAlign **new**|2026|Retriever training|document page image|DocVQA, InfoVQA, SlideVQA, ChartQA, ArxivQA, VisualMRC|Reasoning-guided fine-grained alignment of the retriever.|[paper](https://doi.org/10.1145/3805712.3809602)|[code](https://github.com/NEUIR/ReAlign)|
|AGREE **new**|2026|Retriever training|document page image|ViDoRe, ViDoRe V2|Attention-grounded enhancement of visual document retrieval.|[paper](https://doi.org/10.1145/3805712.3809532)|[code](https://github.com/VickiCui/AGREE)|
|Tile-level pooling **new**|2026|Index size|multi, pooled / page|ViDoRe V2|Spatial pooling of patch vectors into tiles.|[paper](https://doi.org/10.1145/3805712.3808383) · [link in paper](https://arxiv.org/pdf/2602.12510)||
|MV index compression **new**|2026|Index size|multi, compressed|ViDoRe, ViDoRe V2|Multi-vector index compression across modalities.|[paper](https://doi.org/10.1145/3805712.3809589)|[code](https://github.com/hanxiangqin/omni-col-press)|
|Mixed-modal retrieval **new**|2026|Universal RAG|mixed-modal block|MuSiQue, MMEB|Mixed-modal retrieval for universal RAG.|[paper](https://doi.org/10.1145/3805712.3809716)|[code](https://github.com/SnowNation101/Nyx)|
|RegionSLM|2026|Region QA|region|ReDoc|Region unit with a small reader.|[paper](https://doi.org/10.1145/3805712.3809603) · [link in paper](https://dl.acm.org/doi/epdf/10.1145/3805712.3809603)||
|Chain of Evidence **new**|2026|Evidence attribution|document page image|SlideVQA, 2WikiMultiHopQA|Pixel-level visual attribution for iterative RAG.|[paper](https://doi.org/10.1145/3805712.3809540)|[code](https://github.com/PeiYangLiu/CoE)|
|Fragment-level selection **new**|2026|Evidence selection|fragment|M2RAG|Evidence selection below the page.|[paper](https://doi.org/10.1145/3805712.3809692) · [link in paper](https://arxiv.org/pdf/2604.27600)||
|MEG-RAG **new**|2026|Evidence selection|multimodal document / chunk|M2RAG|Quantifies multimodal evidence grounding for selection.|[paper](https://doi.org/10.1145/3805712.3809947)|[code](https://anonymous.4open.science/r/anonym-9QM02BD/README.md)|
|Answer-driven reranking **new**|2026|Re-ranking|multimodal document page|MP-DocVQA, PaperTab, PaperText, FetaTab, +1|Unsupervised reranking from candidate answers.|[paper](https://doi.org/10.1145/3805712.3809664) · [link in paper](https://dl.acm.org/doi/epdf/10.1145/3805712.3809664)||

## EACL

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|SCAN **new**|2026|Layout chunking|coarse-grained semantic chunk|BizMMRAG, Allganize|Semantic layout analysis for text and visual RAG.|[paper](https://aclanthology.org/2026.findings-eacl.82/) · [link in paper](https://arxiv.org/pdf/2505.14381)||
|SCoPE VLM **new**|2026|Efficient navigation|document segment / viewport|M3DocVQA, SlideVQA, MP-DocVQA, DUDE, DocVQA, MMLongBench-Doc|Selective context processing for document navigation.|[paper](https://aclanthology.org/2026.eacl-long.6/) · [link in paper](https://arxiv.org/pdf/2510.21850)||

## NAACL

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|VisDoMRAG|2025|Multi-doc QA|text + visual / chunk, page|PaperTab, SPIQA, VisDoMBench, FetaTab, SlideVQA, LongBench|Text and visual paths made to agree.|[paper](https://arxiv.org/abs/2412.10704)|[code](https://github.com/MananSuri27/VisDoM)|

## IEEE MLSP

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ColFlor|2025|Small retriever|multi / page|ViDoRe|BERT-size retriever.|[paper](https://scholar.google.com/scholar?q=ColFlor%3A+Towards+BERT-Size+Vision-Language+Document+Retrieval+Models)|[code](https://github.com/AhmedMasryKU/colflor)|

## ICLR Workshops

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|CMRAG|2026|Retrieval + QA|document page|LongDocURL|Co-modality text and pixels.|[paper](https://arxiv.org/abs/2509.02123)|[code](https://github.com/WangWarrenChen/CMRAG)|

## arXiv preprints

|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|Nemotron ColEmbed|2026|Page retrieval|multi / page|ViDoRe V3, ViDoRe, MIRACL-Vision|Industrial report.|[paper](https://arxiv.org/abs/2602.03992) · [link in paper](https://arxiv.org/pdf/2602.03992)||
|LFRAG|2026|Fine-grained retrieval|semantically coherent fine-grained block|PaperTab, ViDoRe, DocVQA, VisDoMBench, ArxivQA, InfoVQA|Layout-oriented fine-grained retrieval.|[paper](https://arxiv.org/abs/2605.22829) · [link in paper](https://arxiv.org/pdf/2605.22829)||
|ColParse|2026|Region retrieval|regions + page / region|ViDoRe, ViDoSeek, OmniDocBench|Parser chooses the regions to embed.|[paper](https://arxiv.org/abs/2603.01666) · [link in paper](https://arxiv.org/pdf/2603.01666)||
|MARDoc|2026|Long-doc QA|structured document outline|MMLongBench-Doc, DocBench|Memory-aware refinement.|[paper](https://arxiv.org/abs/2606.05749) · [link in paper](https://arxiv.org/pdf/2606.05749)||
|VisRAG 2.0|2025|Multi-image reasoning|document page snapshot|ChartQA, InfoVQA, DocVQA, SlideVQA, +1|Successor with evidence-guided multi-image reasoning.|[paper](https://arxiv.org/abs/2510.09733)|[code](https://github.com/OpenBMB/VisRAG)|
|VLM2Vec-V2|2025|General embedding|document page image|ViDoRe, MMEB, MMLongBench-Doc, ViDoSeek, InfoVQA, ChartQA|General multimodal embedder.|[paper](https://arxiv.org/abs/2507.04590)|[code](https://tiger-ai-lab.github.io/VLM2Vec/)|
|HKRAG|2025|Fine-print evidence|document page image|ChartQA, InfoVQA, DUDE, SlideVQA, OpenDocVQA|Holistic knowledge construction.|[paper](https://arxiv.org/pdf/2511.20227)||
|MDocAgent|2025|Agentic QA|text + image / page|LongDocURL, PaperText, PaperTab, FetaTab|Text and image agents in parallel.|[paper](https://arxiv.org/pdf/2503.13964)|[code](https://github.com/aiming-lab/MDocAgent)|
