# Metrics

Metrics used by the benchmarks and methods tracked in the survey. Values reported with each metric are in [scores](scores.md) and [datasets](datasets.md).

|Metric|Task|What it measures|Used by|
|---|---|---|---|
|nDCG@k|Retrieval|Normalized discounted cumulative gain of the top-k ranked pages; the ViDoRe benchmarks report k=5 (V1, V2) and k=10 (V3).|ViDoRe v1, v2, v3|
|Recall@k / R@k|Retrieval|Share of queries whose relevant page is in the top k.|ViDoSeek, RegionRAG results|
|MRR@k|Retrieval|Mean reciprocal rank of the first relevant page within the top k.|VisRAG evaluation sets|
|ANLS|Question answering|Average normalized Levenshtein similarity between predicted and gold answers; introduced with ST-VQA.|DocVQA, InfographicVQA, MMLongBench-Doc (SCoPE VLM)|
|Accuracy|Question answering|Share of questions answered correctly; generalized accuracy on MMLongBench-Doc and LongDocURL.|MMLongBench-Doc, LongDocURL, SlideVQA|
|Relaxed accuracy|Question answering|Numeric answers counted correct within a small relative tolerance.|ChartQA|
|EM, F1|Question answering|Exact match and token-level F1 against the gold answer.|TAT-DQA|
|F1 (entity linking)|Form understanding|F1 over key-value entities and links.|FUNSD|
|GriTS|Table structure|Grid table similarity between predicted and gold cell grids.|PubTables-1M|
|mAP|Layout analysis|Mean average precision of detected layout regions.|DocLayNet|
|CARS (proposed)|Channel-aware retrieval|Channel-aware retrieval score proposed in the survey (Eq. 7): retrieval quality reported per channel beside nDCG.|proposed in the paper|

Caveat from the paper: averages with the same name are not always comparable. For example, "ViDoRe V2 average" covers four, seven or nine subsets depending on the paper, and end-to-end accuracy depends mostly on the reader model.