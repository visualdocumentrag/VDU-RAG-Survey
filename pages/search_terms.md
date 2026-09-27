# Search and screening terms (paper Table 2)

[Back to README](../README.md#paper-to-repository-map)

Venue-year lists were retrieved in full, not by query; groups D, R and E only flag records for manual reading (a record is flagged if its title or abstract matches any term, D OR R OR E). arXiv was queried directly with the phrase groups A1-A5.

|Group|Terms|
|---|---|
|D (document)|visually rich, document, DocVQA, multi-page, PDF, OCR, layout, chart, infographic, slide, screenshot, text-rich, scanned, table understanding / question / recognition / structure, handwriting, scene text, formula, key information, information extraction|
|R (retrieval)|retrieval-augmented, RAG (incl. \*RAG, GraphRAG), ColPali, ColQwen, late interaction, multi-vector, multimodal retrieval, visual retrieval, document retrieval|
|E (efficiency)|visual token, token pruning / compression / reduction, high-resolution|
|Dataset flag|title: dataset, benchmark, corpus, \*Bench; abstract: we introduce / present / propose / release / construct / curate … dataset / benchmark / corpus|
|Excluded matches|whole-slide (pathology), tabular machine learning, lookup tables, drag, storage, leverage (substring false positives)|
|**arXiv group**|**Phrases (title OR abstract)**|
|A1 visual doc. RAG|"visual document retrieval", "visually rich document retrieval", "document RAG", "multimodal document RAG", "visual RAG", "vision-based RAG", VisRAG, ColPali, ColQwen, ViDoRe, "multimodal retrieval-augmented generation document", "retrieval-augmented generation visually rich"|
|A2 VDU / DocQA|"visually rich document", "visually-rich document", "document understanding", "document visual question answering", DocVQA, "document question answering", "multi-page document", "long document understanding", "text-rich image", "OCR-free document", "document VQA"|
|A3 parsing|"document parsing", "document layout analysis", "layout analysis document", "document image", "key information extraction", "visual information extraction", "PDF parsing", "document OCR", "table structure recognition"|
|A4 charts, tables|"chart understanding", "chart question answering", ChartQA, infographic, "table image understanding", "slide understanding", "scientific figure understanding"|
|A5 multi-vector|"late interaction retrieval", "multi-vector retrieval", "ColBERT multimodal", "visual token pruning retrieval"|
|arXiv filter|each A1-A5 AND categories cs.CV, cs.CL, cs.IR, cs.AI, cs.LG or cs.MM AND submitted between 1 January and 31 December 2026; all five result lists read to the end (paper Sec. 3.3)|

The scripts that ran these queries are in [`scripts/`](../scripts/) (for arXiv: [`arxiv_scraper.py`](../scripts/arxiv_scraper.py)).

[Back to README](../README.md#paper-to-repository-map)
