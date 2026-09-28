# Metrics

[Back to README](../README.md#metrics-and-reported-scores) · [Scores](scores.md) · [Datasets](datasets.md) · [Paper Table 8 (HD)](figures_tables.md#table-8)

## Metrics of the channel-audited benchmarks (paper Table 8)

Every metric that appears in the Metric column of paper Table 8, with the benchmarks that use it.

|Metric|What it measures|Used by|
|---|---|---|
|nDCG@5|Normalized discounted cumulative gain over the top 5 pages|ViDoRe v1, ViDoRe v2, ViDoSeek|
|R@5|Recall at 5|ViDoRe v2, ViDoRe v3, ViDoSeek|
|nDCG@10|Normalized discounted cumulative gain over the top 10 pages|ViDoRe v3|
|R@1|Recall at 1|ViDoRe v3, ViDoSeek|
|mAP|Mean average precision|ViDoRe v3, MMDocIR, DocLayNet|
|nDCG@1/3/5|nDCG at cut-off 1, 3 and 5|MMDocIR|
|R@1/3/5|Recall at 1, 3 and 5|MMDocIR|
|BLEU|n-gram overlap of the generated answer|MMDocRAG, SPIQA|
|ROUGE-L|Longest-common-subsequence overlap of the generated answer|MMDocRAG|
|ANLS|Average normalized Levenshtein similarity (introduced with ST-VQA)|M3DocVQA, DocVQA, InfographicVQA, MTVQA|
|F1|Harmonic mean of precision and recall|M3DocVQA, SciEGQA, TAT-DQA, FUNSD, VRDU, SPODS, ReST, DKDS, TexTAR|
|P@10|Precision at 10|UniDoc-Bench|
|R@10|Recall at 10|UniDoc-Bench|
|relaxed acc.|Numeric answers correct within a small relative tolerance|ChartQA|
|EM|Exact match with the gold answer|TAT-DQA|
|ROUGE|n-gram recall overlap of the generated answer|SPIQA|
|BERTScore|Embedding similarity of generated and gold answers|SPIQA|
|L3Score|LLM-judged answer score|SPIQA|
|Accuracy|Share of answers judged correct|LongDocURL, MTVQA, ReST|
|AP|Average precision of detected tables|PubTables-1M|
|GriTS|Grid table similarity of predicted and gold cell grids|PubTables-1M|
|CDM|Character detection matching for formula recognition|UniMER|
|P|Precision|TexTAR|
|R|Recall|TexTAR|

## Blind spots (paper Sec. 10.4)

nDCG takes the *page* as the unit of relevance; ANLS takes the *string* as the unit of correctness. Neither can say which content on the page was responsible. Two formula metrics (BLEU and CDM) order the same pair of systems in opposite directions, relevance labels correlate only weakly with downstream utility, and "ViDoRe V2 average" covers four, seven or nine subsets depending on the paper.

## CARS: the channel-aware retrieval score (paper Eq. 7)

Let a retrieved region $r$ carry graded relevance $g(r)$ to the query $q$ and a channel $c(r)$. For each channel $c$:

$$\mathrm{CARS}_c(q)=\frac{\sum_{r\in\mathcal{R}_K(q)}\mathbf{1}[c(r)=c]\,g(r)}{\sum_{r\in\mathcal{R}^{*}_{c,K}(q)}g(r)}$$

where $\mathcal{R}^{*}_{c,K}(q)$ holds the $K$ most relevant regions of channel $c$, so $\mathrm{CARS}_c\in[0,1]$; queries with no relevant region of channel $c$ are left out of its average. CARS is reported per channel, beside nDCG, not summed. If each query also carries the channel it requires, averaging over queries grouped by that channel gives an $8\times 8$ matrix whose off-diagonal entries show which channel a system retrieved in place of the one asked for. ViDoRe v3 labels the content type of its evidence boxes, so CARS can already be computed on it for text, tables and figures.

[Back to README](../README.md#metrics-and-reported-scores)
