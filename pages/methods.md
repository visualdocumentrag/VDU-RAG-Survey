# Methods (73)

All visual document RAG methods tracked by the survey, ordered by venue as in the paper (Tables 4-5). Cut-off: 24 September 2026.

*Objective*: what the method optimizes. *Index / Unit*: vectors stored per unit and what is returned. *Datasets*: benchmarks named at least three times in the paper's full text (or its abstract). **new** = added from the 2025-2026 venue lists. Source: [`data/methods.csv`](../data/methods.csv).

## CVPR

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|Evo-Retriever **new**|CVPR'26|Retriever training||ViDoRe V2, MMEB, ViDoRe|LLM-guided curriculum for multimodal document retrieval.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html)||
|RobustVisRAG **new**|CVPR'26|Robustness|||Causality-aware vision RAG under visual degradations.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_RobustVisRAG_Causality-Aware_Vision-Based_Retrieval-Augmented_Generation_under_Visual_Degradations_CVPR_2026_paper.html)|[code](https://robustvisrag.github.io/)|
|M3DocDep **new**|CVPR'26|Chunking|chunk|DUDE, MP-DocVQA|Dependency-aware chunking across pages and documents.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shin_M3DocDep_Multi-modal_Multi-page_Multi-document_Dependency_Chunking_with_Large_Vision-Language_Models_CVPR_2026_paper.html)||
|MARS-RL **new**|CVPR'26F|RL reasoning||ViDoSeek|Multi-agent RAG on multimodal documents, trained with RL.|[paper](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_MARS-RL_Enhancing_Multi-Agent_RAG_Systems_for_Multi-Modal_Documents_via_Strategic_CVPRF_2026_paper.html)||
|Evidence-sparsity agent **new**|CVPR'26|Long-doc QA||LongDocURL, MMLongBench-Doc, PaperTab, FetaTab, ChartQA|Agentic context engineering for long documents.|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Resolving_Evidence_Sparsity_Agentic_Context_Engineering_for_Long-Document_Understanding_CVPR_2026_paper.html)||
|VDocRAG|CVPR'25|Retrieval + QA|single / page|OpenDocVQA, InfoVQA, SlideVQA, ChartQA, DocVQA, DUDE|One image format for retrieval and QA.|[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Tanaka_VDocRAG_Retrieval-Augmented_Generation_over_Visually-Rich_Documents_CVPR_2025_paper.html)|[code](https://vdocrag.github.io/)|

## ECCV

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|LightSTAR **new**|ECCV'26|Efficiency||ViDoRe|Lightweight selection with vision-adaptive refinement.|[paper](https://eccv.ecva.net/virtual/2026/poster/4839)|[code](https://github.com/bokufa/LightSTAR)|
|UOT-VDR **new**|ECCV'26|Efficiency||ViDoRe|Unbalanced optimal transport for efficient matching.|[paper](https://eccv.ecva.net/virtual/2026/poster/4715)|[code](https://github.com/shhhhhyy/Unbalanced-Optimal-Transport-for-EVDR)|
|MG2-RAG **new**|ECCV'26|Multimodal RAG|graph||Multi-granularity graph for multimodal RAG.|[paper](https://eccv.ecva.net/virtual/2026/poster/3411)|[code](https://github.com/Daboolu/MG2-RAG)|
|MMAgent-R2 **new**|ECCV'26|Re-rank / reject||E-VQA, InfoSeek|Agentic mRAG that learns to rerank and reject.|[paper](https://eccv.ecva.net/virtual/2026/poster/4250)||

## ICDAR

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|LMS-Retrieval|ICDAR'26|Region retrieval|multi, typed / region||Type embedding on token vectors.|[paper](https://doi.org/10.1007/978-3-032-36039-7_8)|[code](https://github.com/Lumanman9/LMS-Retrieval)|

## AAAI

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|URaG **new**|AAAI'26|Long-doc QA||SlideVQA, MMLongBench-Doc, DUDE, LongDocURL|Unified retrieval and generation inside one MLLM.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|[code](https://github.com/shi-yx/URaG)|
|RegionRAG|AAAI'26|Region retrieval|multi, grouped / region|InfoVQA, DocVQA, ArxivQA, SlideVQA, TextVQA, ViDoRe|Indexes and returns sub-page regions.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37597)|[code](https://github.com/Aeryn666/RegionRAG)|
|Look as You Think **new**|AAAI'26|Evidence attribution|||Reasoning with visual evidence attribution.|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40488)||

## WACV

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|GlobalDoc **new**|WACV'25|Retrieval + classification|||Cross-modal framework for real-world document image retrieval and classification.|[paper](https://openaccess.thecvf.com/content/WACV2025/html/Bakkali_GlobalDoc_A_Cross-Modal_Vision-Language_Framework_for_Real-World_Document_Image_Retrieval_WACV_2025_paper.html)||

## NeurIPS

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|VRAG-RL **new**|NeurIPS'25|RL reasoning||SlideVQA, ViDoSeek|Vision-perception RAG trained with RL, iterative reasoning.|[paper](https://openreview.net/forum?id=EeAHhNwXPV)|[code](https://github.com/Alibaba-NLP/VRAG)|

## EMNLP

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ColMate|EMNLP'25|Retriever training|multi / page|ViDoRe, ViDoRe V2|Document-adapted training objective.|[paper](https://aclanthology.org/2025.emnlp-industry.145/)||
|Serval|EMNLP'25|Zero-shot retrieval||ViDoRe, MIRACL-Vision|Zero-shot, no task-specific training.|[paper](https://aclanthology.org/2025.emnlp-main.1568/)|[code](https://github.com/thongnt99/serval)|
|LILaC **new**|EMNLP'25|Multihop retrieval|multi|SlideVQA, MP-DocVQA, InfoVQA|Late interaction over a layered component graph, multihop.|[paper](https://aclanthology.org/2025.emnlp-main.1037/)|[code](https://github.com/joohyung00/lilac)|
|DocAgent|EMNLP'25|Long-doc QA|||Outline-guided agents for long documents.|[paper](https://doi.org/10.18653/v1/2025.emnlp-main.893)|[code](https://github.com/lisun-ai/DocAgent)|
|MoLoRAG|EMNLP'25|Long-doc QA||LongDocURL, PaperTab, FetaTab|Logic-aware retrieval over page relations.|[paper](https://aclanthology.org/2025.emnlp-main.708/)|[code](https://github.com/WxxShirley/MoLoRAG)|
|SimpleDoc **new**|EMNLP'25|Long-doc QA|page|DocVQA, LongDocURL, FetaTab|Dual-cue page retrieval and iterative refinement.|[paper](https://aclanthology.org/2025.emnlp-main.1443/)|[code](https://github.com/ag2ai/SimpleDoc)|
|ViDoRAG|EMNLP'25|Agentic QA|hybrid / page|ViDoSeek, SlideVQA|Multi-agent iterative refinement.|[paper](https://aclanthology.org/2025.emnlp-main.464/)|[code](https://github.com/Alibaba-NLP/ViDoRAG)|
|DSE|EMNLP'24|Page retrieval|single / page|Wiki-SS, SlideVQA|Rendered page as one dense vector.|[paper](https://arxiv.org/pdf/2406.11251)||

## ACL

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|HEAVEN|ACL'26|Efficiency|single, then multi / page|OpenDocVQA, M3DocVQA, LongDocURL, ViDoSeek, VisR-Bench, MMDocIR|Single- then multi-vector stage.|[paper](https://aclanthology.org/2026.findings-acl.54/)|[code](https://github.com/juyeonnn/HEAVEN)|
|Prune-then-Merge **new**|ACL'26|Index size|multi, merged / page|ViDoRe, REAL-MM-RAG, MMLongBench-Doc, ViDoSeek, InfoVQA, TabFQuAD|Prunes, then merges patch vectors.|[paper](https://aclanthology.org/2026.findings-acl.1247/)||
|HiKEY|ACL'26|Open-domain QA||M3DocVQA|Hierarchical open-domain retrieval.|[paper](https://aclanthology.org/2026.acl-long.818/)||
|LAD-RAG|ACL'26|Layout-aware QA|graph / region|LongDocURL, MMLongBench-Doc, DUDE, MP-DocVQA|Layout-aware graph retrieval.|[paper](https://aclanthology.org/2026.acl-long.724/)||
|Utility-oriented selection **new**|ACL'26|Evidence selection||MRAG-Bench|Selects visual evidence by utility, not relevance.|[paper](https://aclanthology.org/2026.acl-long.1620/)|[code](https://github.com/Hcnaeg/utility-mrag)|
|SlideAgent|ACL'26|Slide QA||SlideVQA, InfoVQA, REAL-MM-RAG|Hierarchical multi-page navigation.|[paper](https://doi.org/10.18653/v1/2026.acl-long.677)|[code](https://slideagent.github.io/)|
|DocLens|ACL'26|Long-doc QA||MMLongBench-Doc, FinRAGBench-V|Tool-augmented agents on regions.|[paper](https://aclanthology.org/2026.acl-long.1234/)|[code](https://dwzhu-pku.github.io/DocLens/)|
|TRACE **new**|ACL'26|Evidence chain|||Traversal retrieval with a chain of evidence.|[paper](https://aclanthology.org/2026.acl-long.445/)|[code](https://github.com/shimurenhlq/TRACE)|
|ALDEN **new**|ACL'26|RL navigation||DUDE, SlideVQA, PaperText, LongDocURL, PaperTab, DocVQA|RL for active navigation and evidence gathering.|[paper](https://aclanthology.org/2026.acl-long.611/)||
|MDocRAG-RL **new**|ACL'26|RL reasoning|||Multimodal document RAG with RL-trained visual reasoning.|[paper](https://aclanthology.org/2026.findings-acl.420/)||
|MM-Doc-R1 **new**|ACL'26|RL reasoning||MMLongBench-Doc, DocVQA|Multi-turn RL for long-document VQA agents.|[paper](https://aclanthology.org/2026.findings-acl.1488/)||
|Doc-V* **new**|ACL'26|Multi-page QA||DUDE, MMLongBench-Doc, SlideVQA, DocVQA, LongDocURL, MP-DocVQA|Coarse-to-fine interactive visual reasoning.|[paper](https://aclanthology.org/2026.acl-long.2129/)|[code](https://github.com/SeerRay-Lab/Doc-V)|
|One-Screenshot retrieval **new**|ACL'25|Unified search|screenshot||Any content rendered as one screenshot for unified search.|[paper](https://aclanthology.org/2025.acl-long.943/)||
|Storage-efficient VDR **new**|ACL'25|Index size|multi, reduced / page|ViDoRe, DocVQA, InfoVQA, MMLongBench-Doc, ChartQA|Empirical study of reducing patch-level embeddings.|[paper](https://aclanthology.org/2025.findings-acl.1003/)||
|NeuSym-RAG **new**|ACL'25|PDF QA|hybrid||Neural-symbolic retrieval over PDFs.|[paper](https://aclanthology.org/2025.acl-long.311/)||
|Doc-React **new**|ACL'25|Multi-page QA|||Multi-page heterogeneous document QA.|[paper](https://aclanthology.org/2025.acl-short.6/)||
|VISA|ACL'25|Source attribution|page + box||Page retrieval with evidence box.|[paper](https://aclanthology.org/2025.acl-long.1456/)||

## ICLR

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|MetaEmbed|ICLR'26|Adaptive cost|multi, adaptive / page|MMEB, ViDoRe, ViDoRe V2|Test-time choice of vector count.|[paper](https://openreview.net/forum?id=yKDqg9HwZX)|[code](https://github.com/facebookresearch/MetaEmbed)|
|VisRAG|ICLR'25|Retrieval + QA|single / page|ArxivQA, DocVQA, ChartQA, SlideVQA, InfoVQA, MP-DocVQA|VLM embedder and reader, no parsing.|[paper](https://openreview.net/forum?id=zG459X3Xge)|[code](https://github.com/openbmb/visrag)|
|ColPali|ICLR'25|Page retrieval|multi / page|ViDoRe, TabFQuAD, DocVQA, ArxivQA, InfoVQA|Patch vectors scored by MaxSim.|[paper](https://openreview.net/forum?id=ogjBpZ8uSi)|[code](https://github.com/illuin-tech/colpali)|
|SV-RAG|ICLR'25|Long-doc QA||MMLongBench-Doc, SlideVQA, VisR-Bench, DocVQA, DUDE|Adapts the reader as retriever.|[paper](https://openreview.net/forum?id=FDaHjwInXO)|[code](https://github.com/puar-playground/Self-Visual-RAG)|

## ICML

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ModernVBERT|ICML'26|Small retriever||ViDoRe|Compact bidirectional encoder.|[paper](https://openreview.net/forum?id=TyVJlSHke2)|[code](https://github.com/illuin-tech/modernvbert)|
|POQD **new**|ICML'25|Query decomposition|multi|WebQA|Performance-oriented query decomposition.|[paper](https://proceedings.mlr.press/v267/liu25ag.html)|[code](https://github.com/PKU-SDS-lab/POQD-ICML25)|
|RAP **new**|ICML'25|High-res perception|||Visual RAG for high-resolution image perception.|[paper](https://proceedings.mlr.press/v267/wang25at.html)|[code](https://github.com/DreamMr/RAP)|

## KDD

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|MM hierarchical RAG **new**|KDD'26|Document QA|||Hierarchical multimodal RAG for document QA.|[paper](https://doi.org/10.1145/3770855.3819034)||

## EACL

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|SCAN **new**|EACL'26|Layout chunking|||Semantic layout analysis for text and visual RAG.|[paper](https://aclanthology.org/2026.findings-eacl.82/)||
|SCoPE VLM **new**|EACL'26|Efficient navigation||M3DocVQA, SlideVQA, MP-DocVQA, DUDE, DocVQA, MMLongBench-Doc|Selective context processing for document navigation.|[paper](https://aclanthology.org/2026.eacl-long.6/)||

## SIGIR

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ReAlign **new**|SIGIR'26|Retriever training||DocVQA, InfoVQA, SlideVQA, ChartQA, ArxivQA, VisualMRC|Reasoning-guided fine-grained alignment of the retriever.|[paper](https://doi.org/10.1145/3805712.3809602)|[code](https://github.com/NEUIR/ReAlign)|
|AGREE **new**|SIGIR'26|Retriever training||ViDoRe, ViDoRe V2|Attention-grounded enhancement of visual document retrieval.|[paper](https://doi.org/10.1145/3805712.3809532)|[code](https://github.com/VickiCui/AGREE)|
|Tile-level pooling **new**|SIGIR'26|Index size|multi, pooled / page||Spatial pooling of patch vectors into tiles.|[paper](https://doi.org/10.1145/3805712.3808383)||
|MV index compression **new**|SIGIR'26|Index size|multi, compressed|ViDoRe, ViDoRe V2|Multi-vector index compression across modalities.|[paper](https://doi.org/10.1145/3805712.3809589)|[code](https://github.com/hanxiangqin/omni-col-press)|
|Mixed-modal retrieval **new**|SIGIR'26|Universal RAG||MuSiQue, MMEB|Mixed-modal retrieval for universal RAG.|[paper](https://doi.org/10.1145/3805712.3809716)|[code](https://github.com/SnowNation101/Nyx)|
|RegionSLM|SIGIR'26|Region QA|region||Region unit with a small reader.|[paper](https://doi.org/10.1145/3805712.3809603)||
|Chain of Evidence **new**|SIGIR'26|Evidence attribution||SlideVQA, 2WikiMultiHopQA|Pixel-level visual attribution for iterative RAG.|[paper](https://doi.org/10.1145/3805712.3809540)|[code](https://github.com/PeiYangLiu/CoE)|
|Fragment-level selection **new**|SIGIR'26|Evidence selection|fragment||Evidence selection below the page.|[paper](https://doi.org/10.1145/3805712.3809692)||
|MEG-RAG **new**|SIGIR'26|Evidence selection|||Quantifies multimodal evidence grounding for selection.|[paper](https://doi.org/10.1145/3805712.3809947)|[code](https://anonymous.4open.science/r/anonym-9QM02BD/README.md)|
|Answer-driven reranking **new**|SIGIR'26|Re-ranking|||Unsupervised reranking from candidate answers.|[paper](https://doi.org/10.1145/3805712.3809664)||

## ICCVW

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|M3DocRAG|ICCVW'25|Multi-doc QA|multi / page|M3DocVQA, MMLongBench-Doc, MP-DocVQA|Multi-page, multi-document RAG.|[paper](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html)|[code](https://github.com/bloomberg/m3docrag)|

## NAACL

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|VisDoMRAG|NAACL'25|Multi-doc QA|text + visual / chunk, page|PaperTab, SPIQA, VisDoMBench, FetaTab, SlideVQA, LongBench|Text and visual paths made to agree.|[scholar](https://scholar.google.com/scholar?q=VisDoM%3A+Multi-Document+QA+with+Visually+Rich+Elements+Using+Multimodal+Retrieval-Augmented+Generation)|[code](https://github.com/MananSuri27/VisDoM)|

## MLSP

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|ColFlor|MLSP'25|Small retriever|multi / page||BERT-size retriever.|[scholar](https://scholar.google.com/scholar?q=ColFlor%3A+Towards+BERT-Size+Vision-Language+Document+Retrieval+Models)|[code](https://github.com/AhmedMasryKU/colflor)|

## ICLRW

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|CMRAG|ICLRW'26|Retrieval + QA||LongDocURL|Co-modality text and pixels.|[arxiv](https://arxiv.org/abs/2509.02123)|[code](https://github.com/WangWarrenChen/CMRAG)|

## arXiv

|Method|Venue|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|
|---|---|---|---|---|---|---|---|
|Nemotron ColEmbed|arXiv'26|Page retrieval|multi / page|ViDoRe V3, ViDoRe, MIRACL-Vision|Industrial report.|[paper](https://arxiv.org/abs/2602.03992)||
|LFRAG|arXiv'26|Fine-grained retrieval||PaperTab, ViDoRe, DocVQA, VisDoMBench, ArxivQA, InfoVQA|Layout-oriented fine-grained retrieval.|[paper](https://arxiv.org/abs/2605.22829)||
|ColParse|arXiv'26|Region retrieval|regions + page / region|ViDoRe, ViDoSeek, OmniDocBench|Parser chooses the regions to embed.|[paper](https://arxiv.org/abs/2603.01666)||
|MARDoc|arXiv'26|Long-doc QA||MMLongBench-Doc, DocBench|Memory-aware refinement.|[paper](https://arxiv.org/abs/2606.05749)||
|VisRAG 2.0|arXiv'25|Multi-image reasoning|||Successor with evidence-guided multi-image reasoning.|[arxiv](https://arxiv.org/abs/2510.09733)|[code](https://github.com/OpenBMB/VisRAG)|
|VLM2Vec-V2|arXiv'25|General embedding||ViDoRe, MMEB, MMLongBench-Doc, ViDoSeek, InfoVQA, ChartQA|General multimodal embedder.|[arxiv](https://arxiv.org/abs/2507.04590)|[code](https://tiger-ai-lab.github.io/VLM2Vec/)|
|HKRAG|arXiv'25|Fine-print evidence||ChartQA, InfoVQA, DUDE, SlideVQA, OpenDocVQA|Holistic knowledge construction.|[paper](https://arxiv.org/pdf/2511.20227)||
|MDocAgent|arXiv'25|Agentic QA|text + image / page|LongDocURL, PaperText, PaperTab, FetaTab|Text and image agents in parallel.|[paper](https://arxiv.org/pdf/2503.13964)|[code](https://github.com/aiming-lab/MDocAgent)|
