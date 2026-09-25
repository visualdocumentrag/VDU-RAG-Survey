# Reported scores

Every value is copied from the paper that reports it, read from the arXiv HTML version of its own result table, and not re-run or rescaled (paper Table 9). See [metrics](metrics.md) for the comparison caveats.

|Method|Paper|Values as reported|Source table id|
|---|---|---|---|
|ColPali|[ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi)|ViDoRe V1 nDCG@5: 81.3 (PaliGemma-3B)|T016|
|ColMate|[ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval](https://aclanthology.org/2025.emnlp-industry.145/)|ViDoRe V1 nDCG@5: 85.14; ViDoRe V2 (nine domains incl. multilingual): 57.61 (ColPali-3B base)|T021/T022|
|ColModernVBERT|[ModernVBERT: Towards Smaller Visual Document Retrievers](https://openreview.net/forum?id=TyVJlSHke2)|ViDoRe V1 nDCG@5: 81.2; ViDoRe V2 (English subsets): 56.0 (0.25B)|T027|
|VLM2Vec-V2|[VLM2Vec-V2: Advancing Multimodal Embedding for Videos, Images, and Visual Documents](https://arxiv.org/abs/2507.04590)|MMEB-V2 visual-document protocol: ViDoRe V1 75.5; ViDoRe V2 44.9|T032|
|ColParse (GME-7B)|[Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations](https://arxiv.org/abs/2603.01666)|ViDoRe V1 nDCG@5: 89.56; ViDoRe V2 (four English subsets): 62.12; ViDoSeek: 84.12 (GME-7B backbone)|T197/T198|
|LightSTAR|[LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement](https://eccv.ecva.net/virtual/2026/poster/4839)|ViDoRe V1 nDCG@5: 89.1 (eight of the ten V1 subsets; TabFQuAD and Shift not reported) (2B)|T098|
|MetaEmbed|[MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction](https://openreview.net/forum?id=yKDqg9HwZX)|ViDoRe V2 (seven tasks) nDCG@5: 61.3 (7B), 60.3 (3B)|T043|
|Evo-Retriever|[Evo-Retriever: LLM-Guided Curriculum Evolution with Viewpoint-Pathway Collaboration for Multimodal Document Retrieval](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html)|ViDoRe V2 (four English subsets) nDCG@5: 65.2 (7B), 63.3 (3B)|T052|
|AGREE|[Attention Grounded Enhancement for Visual Document Retrieval](https://doi.org/10.1145/3805712.3809532)|ViDoRe V2 (four English subsets) nDCG@5: 61.54 (Qwen2.5-VL backbone), 57.75 (PaliGemma backbone)|T066|
|SERVAL|[Serval: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models](https://aclanthology.org/2025.emnlp-main.1568/)|ViDoRe V2 (nine subsets, zero-shot) nDCG@5: 63.4 (Qwen2.5-VL-32B + inf-7B)|T037|
|AGC|[Multi-Vector Index Compression in Any Modality](https://doi.org/10.1145/3805712.3809589)|ViDoRe V2 (multilingual subsets) nDCG@5: 56.7 (64-token budget)|T105|
|Nemotron ColEmbed V2 8B|[Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992)|ViDoRe V3 nDCG@10: 63.42 (8B)|T045|
|ReAlign|[ReAlign: Optimizing the Visual Document Retriever with Reasoning-Guided Fine-Grained Alignment](https://doi.org/10.1145/3805712.3809602)|Average nDCG@5 on six VisRAG evaluation sets: 75.4 (Phi-3-V, pre-trained)|T064|
|HEAVEN|[Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy](https://aclanthology.org/2026.findings-acl.54/)|ViDoSeek R@1: 75.04|T071|
|SV-RAG|[SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://openreview.net/forum?id=FDaHjwInXO)|Accuracy (%): MMLongBench-Doc 23.0 (InternVL2 reader)|T110|
|MDocAgent|[MDocAgent: A Multi-Modal Multi-Agent Framework for Document Understanding](https://arxiv.org/abs/2503.13964)|Accuracy (%), best reported setting: MMLongBench-Doc 31.5, LongDocURL 57.8, PaperTab 27.8, PaperText 48.7, FetaTab 67.5|T219|
|CMRAG|[CMRAG: Co-modality-based Visual Document Retrieval and Question Answering](https://arxiv.org/abs/2509.02123)|Accuracy (%): MMLongBench-Doc 31.05; LongDocURL (filtered subset) 48.18 (top-3)|T127|
|ALDEN|[ALDEN: Reinforcement Learning for Active Navigation and Evidence Gathering in Long Documents](https://aclanthology.org/2026.acl-long.611/)|Accuracy (%): MMLongBench-Doc 38.5, LongDocURL 54.2, DUDE subset 65.3|T247/T248|
|Doc-V*|[Doc-V*: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA](https://aclanthology.org/2026.acl-long.2129/)|Accuracy (%): MMLongBench-Doc 42.1; LongDocURL 56.3 (Qwen2.5-VL, GRPO)|T253|
|LAD-RAG|[LAD-RAG: Layout-aware Dynamic RAG for Visually-Rich Document Understanding](https://aclanthology.org/2026.acl-long.724/)|Accuracy (%) with InternVL2-8B reader: MMLongBench-Doc 44.8, LongDocURL 47.7|T191|
|MM-Doc-R1|[MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning](https://aclanthology.org/2026.findings-acl.1488/)|Accuracy (%): MMLongBench-Doc 45.7 (Qwen3-8B)|T251|
|URaG|[URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|Accuracy (%): LongDocURL 52.2 (7B)|T152|
|MARDoc|[MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA](https://arxiv.org/abs/2606.05749)|Accuracy (%): MMLongBench-Doc 57.1 (Qwen3-VL-30B-A3B reader), 52.7 (Qwen3-VL-8B reader)|T237|
|DocLens|[DocLens: A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding](https://aclanthology.org/2026.acl-long.1234/)|Accuracy (%): MMLongBench-Doc 67.6 (Gemini-2.5-Pro reader)|T233|
|SCoPE VLM|[SCoPE VLM: Selective Context Processing for Efficient Document Navigation in Vision-Language Models](https://aclanthology.org/2026.eacl-long.6/)|MMLongBench-Doc ANLS: 17.90 (3B, EGRPO)|T209/T213|
|VisDoMRAG|[VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://scholar.google.com/scholar?q=VisDoM%3A+Multi-Document+QA+with+Visually+Rich+Elements+Using+Multimodal+Retrieval-Augmented+Generation)|VisDoMBench: PaperTab 44.11, FetaTab 63.28, SlideVQA 67.22|T122|
|HKRAG|[HKRAG: Holistic Knowledge Retrieval-Augmented Generation over Visually-Rich Documents](https://arxiv.org/abs/2511.20227)|OpenDocVQA setting: SlideVQA 74.0, DUDE 68.8|T147|
|SlideAgent|[SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding](https://doi.org/10.18653/v1/2026.acl-long.677)|SlideVQA overall: 84.9 (proprietary reader)|T224|