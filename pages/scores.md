# Reported scores (paper Table 9)

[Paper Table 9 (HD)](figures_tables.md#table-9) · [Fig. 6 (HD)](figures_tables.md#fig-6)

[Back to README](../README.md#metrics-and-reported-scores) · [Metrics](metrics.md) · [Raw file](../data/scores.csv)

Scores as reported by each paper for itself, copied from its own result table and not re-run or rescaled. ViDoRe V2 averages cover different subsets across papers (letters), so V2 values compare only within a letter. In the end-to-end part the reader model differs by row and dominates the score. "-" = not reported.

## Retrieval (nDCG@5; ViDoRe V3: nDCG@10)

|Retriever|Backbone|ViDoRe V1|ViDoRe V2|ViDoRe V3|Link in paper|
|---|---|:-:|:-:|:-:|:-:|
|[ColPali](https://openreview.net/forum?id=ogjBpZ8uSi)|PaliGemma-3B|81.3|-|-|[code](https://huggingface.co/vidore)|
|[ColMate](https://aclanthology.org/2025.emnlp-industry.145/)|ColPali-3B|85.14|57.61 (a)|-|[link](https://arxiv.org/pdf/2511.00903)|
|[ColModernVBERT](https://openreview.net/forum?id=TyVJlSHke2)|0.25B|81.2|56.0 (b)|-|[code](https://huggingface.co/ModernVBERT)|
|[VLM2Vec-V2](https://arxiv.org/abs/2507.04590)||75.5 (c)|44.9 (c)|-|[code](https://tiger-ai-lab.github.io/VLM2Vec/)|
|[ColParse](https://arxiv.org/abs/2603.01666)|GME-7B|89.56|62.12 (d)|-|[link](https://arxiv.org/pdf/2603.01666)|
|[LightSTAR](https://eccv.ecva.net/virtual/2026/poster/4839)|2B|89.1 (e)|-|-|[code](https://github.com/bokufa/LightSTAR)|
|[MetaEmbed](https://openreview.net/forum?id=yKDqg9HwZX)|7B / 3B|-|61.3 / 60.3 (f)|-|[code](https://github.com/facebookresearch/MetaEmbed)|
|[Evo-Retriever](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html)|7B / 3B|-|65.2 / 63.3 (d)|-|[link](https://arxiv.org/pdf/2603.16455)|
|[AGREE](https://doi.org/10.1145/3805712.3809532)|Qwen2.5-VL|-|61.54 (d)|-|[link](https://arxiv.org/pdf/2511.13415)|
|[SERVAL](https://aclanthology.org/2025.emnlp-main.1568/)|Qwen2.5-VL-32B|-|63.4 (g)|-|[code](https://github.com/thongnt99/serval)|
|[AGC](https://doi.org/10.1145/3805712.3809589)|64 tokens|-|56.7 (h)|-|[code](https://github.com/hanxiangqin/omni-col-press)|
|[Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)|8B|-|-|63.42|[link](https://arxiv.org/pdf/2602.03992)|

## End-to-end accuracy (%)

|Pipeline|Reader|MMLongBench-Doc|LongDocURL|Link in paper|
|---|---|:-:|:-:|:-:|
|[SV-RAG](https://openreview.net/forum?id=FDaHjwInXO)|InternVL2|23.0|-|[link](https://arxiv.org/pdf/2411.01106)|
|[MDocAgent](https://arxiv.org/pdf/2503.13964)|best setting|31.5|57.8|[link](https://arxiv.org/pdf/2503.13964)|
|[CMRAG](https://arxiv.org/abs/2509.02123)|top-3|31.05|48.18 (i)|[code](https://github.com/WangWarrenChen/CMRAG)|
|[ALDEN](https://aclanthology.org/2026.acl-long.611/)||38.5|54.2|[link](https://arxiv.org/pdf/2510.25668)|
|[Doc-V*](https://aclanthology.org/2026.acl-long.2129/)|Qwen2.5-VL|42.1|56.3|[code](https://github.com/SeerRay-Lab/Doc-V)|
|[LAD-RAG](https://aclanthology.org/2026.acl-long.724/)|InternVL2-8B|44.8|47.7|[link](https://arxiv.org/pdf/2510.07233)|
|[MM-Doc-R1](https://aclanthology.org/2026.findings-acl.1488/)|Qwen3-8B|45.7|-|-|
|[URaG](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|7B|-|52.2|[code](https://github.com/shi-yx/URaG)|
|[MARDoc](https://arxiv.org/abs/2606.05749)|Qwen3-VL-30B|57.1|-|[link](https://arxiv.org/pdf/2606.05749)|
|[MARDoc](https://arxiv.org/abs/2606.05749)|Qwen3-VL-8B|52.7|-|[link](https://arxiv.org/pdf/2606.05749)|
|[DocLens](https://aclanthology.org/2026.acl-long.1234/)|Gemini-2.5-Pro|67.6|-|[code](https://dwzhu-pku.github.io/DocLens/)|

ViDoRe V2 subsets: (a) nine incl. multilingual; (b) English; (c) MMEB-V2 protocol; (d) four English; (f) seven; (g) nine, zero-shot; (h) multilingual. (e) eight of the ten V1 subsets. (i) filtered subset.

**Also reported** (paper Table 9 notes): ColParse ViDoSeek 84.12; HEAVEN ViDoSeek R@1 75.04; ReAlign 75.4 avg. nDCG@5 on six VisRAG sets; VisDoMRAG 44.11 / 63.28 / 67.22 on PaperTab / FetaTab / SlideVQA; HKRAG SlideVQA 74.0, DUDE 68.8; SlideAgent SlideVQA 84.9; SCoPE VLM MMLongBench-Doc ANLS 17.90.

**Relative gains reported over each paper's own baselines**: [DSE](https://arxiv.org/abs/2406.11251) +17 points top-1 over BM25 on Wiki-SS; [VisRAG](https://openreview.net/forum?id=zG459X3Xge) 20-40% end-to-end over text-based RAG; [VisDoMRAG](https://arxiv.org/abs/2412.10704) 12-20% on VisDoMBench; [ViDoRAG](https://aclanthology.org/2025.emnlp-main.464/) over 10% on ViDoSeek; [MDocAgent](https://arxiv.org/pdf/2503.13964) +12.1% on average over five benchmarks; [RegionRAG](https://ojs.aaai.org/index.php/AAAI/article/view/37597) +10.02% R@1 and +3.56% accuracy with 71.42% of the visual tokens.

## Every value with its source table

|Method|Paper|Values as reported|Source table|
|---|---|---|---|
|ColPali|[paper](https://openreview.net/forum?id=ogjBpZ8uSi)|ViDoRe V1 nDCG@5: 81.3 (PaliGemma-3B)|T016|
|ColMate|[paper](https://aclanthology.org/2025.emnlp-industry.145/)|ViDoRe V1 nDCG@5: 85.14; ViDoRe V2 (nine domains incl. multilingual): 57.61 (ColPali-3B base)|T021/T022|
|ColModernVBERT|[paper](https://openreview.net/forum?id=TyVJlSHke2)|ViDoRe V1 nDCG@5: 81.2; ViDoRe V2 (English subsets): 56.0 (0.25B)|T027|
|VLM2Vec-V2|[paper](https://arxiv.org/abs/2507.04590)|MMEB-V2 visual-document protocol: ViDoRe V1 75.5; ViDoRe V2 44.9|T032|
|ColParse (GME-7B)|[paper](https://arxiv.org/abs/2603.01666)|ViDoRe V1 nDCG@5: 89.56; ViDoRe V2 (four English subsets): 62.12; ViDoSeek: 84.12 (GME-7B backbone)|T197/T198|
|LightSTAR|[paper](https://eccv.ecva.net/virtual/2026/poster/4839)|ViDoRe V1 nDCG@5: 89.1 (eight of the ten V1 subsets; TabFQuAD and Shift not reported) (2B)|T098|
|MetaEmbed|[paper](https://openreview.net/forum?id=yKDqg9HwZX)|ViDoRe V2 (seven tasks) nDCG@5: 61.3 (7B), 60.3 (3B)|T043|
|Evo-Retriever|[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Evo-Retriever_LLM-Guided_Curriculum_Evolution_with_Viewpoint-Pathway_Collaboration_for_Multimodal_Document_CVPR_2026_paper.html)|ViDoRe V2 (four English subsets) nDCG@5: 65.2 (7B), 63.3 (3B)|T052|
|AGREE|[paper](https://doi.org/10.1145/3805712.3809532)|ViDoRe V2 (four English subsets) nDCG@5: 61.54 (Qwen2.5-VL backbone), 57.75 (PaliGemma backbone)|T066|
|SERVAL|[paper](https://aclanthology.org/2025.emnlp-main.1568/)|ViDoRe V2 (nine subsets, zero-shot) nDCG@5: 63.4 (Qwen2.5-VL-32B + inf-7B)|T037|
|AGC|[paper](https://doi.org/10.1145/3805712.3809589)|ViDoRe V2 (multilingual subsets) nDCG@5: 56.7 (64-token budget)|T105|
|Nemotron ColEmbed V2 8B|[paper](https://arxiv.org/abs/2602.03992)|ViDoRe V3 nDCG@10: 63.42 (8B)|T045|
|ReAlign|[paper](https://doi.org/10.1145/3805712.3809602)|Average nDCG@5 on six VisRAG evaluation sets: 75.4 (Phi-3-V, pre-trained)|T064|
|HEAVEN|[paper](https://aclanthology.org/2026.findings-acl.54/)|ViDoSeek R@1: 75.04|T071|
|SV-RAG|[paper](https://openreview.net/forum?id=FDaHjwInXO)|Accuracy (%): MMLongBench-Doc 23.0 (InternVL2 reader)|T110|
|MDocAgent|[paper](https://arxiv.org/pdf/2503.13964)|Accuracy (%), best reported setting: MMLongBench-Doc 31.5, LongDocURL 57.8, PaperTab 27.8, PaperText 48.7, FetaTab 67.5|T219|
|CMRAG|[paper](https://arxiv.org/abs/2509.02123)|Accuracy (%): MMLongBench-Doc 31.05; LongDocURL (filtered subset) 48.18 (top-3)|T127|
|ALDEN|[paper](https://aclanthology.org/2026.acl-long.611/)|Accuracy (%): MMLongBench-Doc 38.5, LongDocURL 54.2, DUDE subset 65.3|T247/T248|
|Doc-V*|[paper](https://aclanthology.org/2026.acl-long.2129/)|Accuracy (%): MMLongBench-Doc 42.1; LongDocURL 56.3 (Qwen2.5-VL, GRPO)|T253|
|LAD-RAG|[paper](https://aclanthology.org/2026.acl-long.724/)|Accuracy (%) with InternVL2-8B reader: MMLongBench-Doc 44.8, LongDocURL 47.7|T191|
|MM-Doc-R1|[paper](https://aclanthology.org/2026.findings-acl.1488/)|Accuracy (%): MMLongBench-Doc 45.7 (Qwen3-8B)|T251|
|URaG|[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39729)|Accuracy (%): LongDocURL 52.2 (7B)|T152|
|MARDoc|[paper](https://arxiv.org/abs/2606.05749)|Accuracy (%): MMLongBench-Doc 57.1 (Qwen3-VL-30B-A3B reader), 52.7 (Qwen3-VL-8B reader)|T237|
|DocLens|[paper](https://aclanthology.org/2026.acl-long.1234/)|Accuracy (%): MMLongBench-Doc 67.6 (Gemini-2.5-Pro reader)|T233|
|SCoPE VLM|[paper](https://aclanthology.org/2026.eacl-long.6/)|MMLongBench-Doc ANLS: 17.90 (3B, EGRPO)|T209/T213|
|VisDoMRAG|[paper](https://arxiv.org/abs/2412.10704)|VisDoMBench: PaperTab 44.11, FetaTab 63.28, SlideVQA 67.22|T122|
|HKRAG|[paper](https://arxiv.org/pdf/2511.20227)|OpenDocVQA setting: SlideVQA 74.0, DUDE 68.8|T147|
|SlideAgent|[paper](https://doi.org/10.18653/v1/2026.acl-long.677)|SlideVQA overall: 84.9 (proprietary reader)|T224|
