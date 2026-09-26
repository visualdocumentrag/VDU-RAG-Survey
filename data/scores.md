# Reported scores

Values as reported by each paper for itself (paper Table 9). The method name links to the paper.

Raw file: [`scores.csv`](scores.csv) · [Back to README](../README.md)

|Method|Key|Source table in score_tables_html.xlsx|Values|
|---|---|---|---|
|[ColPali](https://openreview.net/forum?id=ogjBpZ8uSi)|fayssecolpali2025|T016|ViDoRe V1 nDCG@5: 81.3 (PaliGemma-3B)|
|[ColMate](https://aclanthology.org/2025.emnlp-industry.145/)|masry2025colmate|T021/T022|ViDoRe V1 nDCG@5: 85.14; ViDoRe V2 (nine domains incl. multilingual): 57.61 (ColPali-3B base)|
|[ColModernVBERT](https://openreview.net/forum?id=TyVJlSHke2)|teiletche2025modernvbert|T027|ViDoRe V1 nDCG@5: 81.2; ViDoRe V2 (English subsets): 56.0 (0.25B)|
|[VLM2Vec-V2](https://arxiv.org/abs/2507.04590)|meng2025vlm2vecv2|T032|MMEB-V2 visual-document protocol: ViDoRe V1 75.5; ViDoRe V2 44.9|
|[ColParse (GME-7B)](https://arxiv.org/abs/2603.01666)|beyondgrid2026|T197/T198|ViDoRe V1 nDCG@5: 89.56; ViDoRe V2 (four English subsets): 62.12; ViDoSeek: 84.12 (GME-7B backbone)|
|[LightSTAR](https://eccv.ecva.net/virtual/2026/poster/4839)|lightstar2026eccv|T098|ViDoRe V1 nDCG@5: 89.1 (eight of the ten V1 subsets; TabFQuAD and Shift not reported) (2B)|
|[MetaEmbed](https://openreview.net/forum?id=yKDqg9HwZX)|xiaometaembed2026|T043|ViDoRe V2 (seven tasks) nDCG@5: 61.3 (7B), 60.3 (3B)|
|[Evo-Retriever](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html)|evoretriever2026cvpr|T052|ViDoRe V2 (four English subsets) nDCG@5: 65.2 (7B), 63.3 (3B)|
|[AGREE](https://doi.org/10.1145/3805712.3809532)|agree2026sigir|T066|ViDoRe V2 (four English subsets) nDCG@5: 61.54 (Qwen2.5-VL backbone), 57.75 (PaliGemma backbone)|
|[SERVAL](https://aclanthology.org/2025.emnlp-main.1568/)|nguyen2025serval|T037|ViDoRe V2 (nine subsets, zero-shot) nDCG@5: 63.4 (Qwen2.5-VL-32B + inf-7B)|
|[AGC](https://doi.org/10.1145/3805712.3809589)|mvcompress2026sigir|T105|ViDoRe V2 (multilingual subsets) nDCG@5: 56.7 (64-token budget)|
|[Nemotron ColEmbed V2 8B](https://arxiv.org/abs/2602.03992)|moreira2026nemotroncolembed|T045|ViDoRe V3 nDCG@10: 63.42 (8B)|
|[ReAlign](https://doi.org/10.1145/3805712.3809602)|realign2026sigir|T064|Average nDCG@5 on six VisRAG evaluation sets: 75.4 (Phi-3-V, pre-trained)|
|[HEAVEN](https://aclanthology.org/2026.findings-acl.54/)|hybridvector2025|T071|ViDoSeek R@1: 75.04|
|[SV-RAG](https://openreview.net/forum?id=FDaHjwInXO)|chensvrag2025|T110|Accuracy (%): MMLongBench-Doc 23.0 (InternVL2 reader)|
|[MDocAgent](https://arxiv.org/abs/2503.13964)|han2025mdocagent|T219|Accuracy (%), best reported setting: MMLongBench-Doc 31.5, LongDocURL 57.8, PaperTab 27.8, PaperText 48.7, FetaTab 67.5|
|[CMRAG](https://arxiv.org/abs/2509.02123)|cmrag2025|T127|Accuracy (%): MMLongBench-Doc 31.05; LongDocURL (filtered subset) 48.18 (top-3)|
|[ALDEN](https://aclanthology.org/2026.acl-long.611/)|alden2026acl|T247/T248|Accuracy (%): MMLongBench-Doc 38.5, LongDocURL 54.2, DUDE subset 65.3|
|[Doc-V*](https://aclanthology.org/2026.acl-long.2129/)|docvstar2026acl|T253|Accuracy (%): MMLongBench-Doc 42.1; LongDocURL 56.3 (Qwen2.5-VL, GRPO)|
|[LAD-RAG](https://aclanthology.org/2026.acl-long.724/)|sourati-etal-2026-lad|T191|Accuracy (%) with InternVL2-8B reader: MMLongBench-Doc 44.8, LongDocURL 47.7|
|[MM-Doc-R1](https://aclanthology.org/2026.findings-acl.1488/)|mmdocr12026acl|T251|Accuracy (%): MMLongBench-Doc 45.7 (Qwen3-8B)|
|[URaG](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|urag2026aaai|T152|Accuracy (%): LongDocURL 52.2 (7B)|
|[MARDoc](https://arxiv.org/abs/2606.05749)|chen2026mardoc|T237|Accuracy (%): MMLongBench-Doc 57.1 (Qwen3-VL-30B-A3B reader), 52.7 (Qwen3-VL-8B reader)|
|[DocLens](https://aclanthology.org/2026.acl-long.1234/)|zhu2025doclens|T233|Accuracy (%): MMLongBench-Doc 67.6 (Gemini-2.5-Pro reader)|
|[SCoPE VLM](https://aclanthology.org/2026.eacl-long.6/)|scopevlm2026eacl|T209/T213|MMLongBench-Doc ANLS: 17.90 (3B, EGRPO)|
|[VisDoMRAG](https://scholar.google.com/scholar?q=VisDoM%3A+Multi-Document+QA+with+Visually+Rich+Elements+Using+Multimodal+Retrieval-Augmented+Generation)|suri2025visdom|T122|VisDoMBench: PaperTab 44.11, FetaTab 63.28, SlideVQA 67.22|
|[HKRAG](https://arxiv.org/abs/2511.20227)|hkrag2025|T147|OpenDocVQA setting: SlideVQA 74.0, DUDE 68.8|
|[SlideAgent](https://doi.org/10.18653/v1/2026.acl-long.677)|jin2025slideagent|T224|SlideVQA overall: 84.9 (proprietary reader)|
