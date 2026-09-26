#!/usr/bin/env python3
"""
Fill the "Dataset" column of tab_methods_v2.tex from the papers themselves.
For each method: find the paper on arXiv by title (official arXiv API), download its PDF,
extract the text, and count how often each known benchmark name occurs.
Output: method_datasets.xlsx  (key, title, arXiv id, title match score, benchmarks with counts,
        suggested Dataset cell = benchmarks mentioned >= MIN_HITS times).
Review the suggestions before pasting them into the table.
Usage (Colab):
  !pip install requests pymupdf pandas openpyxl
  !python method_datasets.py
"""
import re, time, difflib, io
import xml.etree.ElementTree as ET
import requests, fitz, pandas as pd

MIN_HITS = 3
NS = {"a": "http://www.w3.org/2005/Atom"}
BENCH = ["ViDoRe V3","ViDoRe V2","ViDoRe","ViDoSeek","MMLongBench-Doc","LongDocURL","SlideVQA","MP-DocVQA",
 "DocVQA","InfoVQA","InfographicVQA","ChartQA","M3DocVQA","MMDocIR","MMDocRAG","OpenDocVQA","VisR-Bench",
 "PaperTab","FetaTab","PaperText","TAT-DQA","DUDE","DocBench","Wiki-SS","VisDoMBench","UniDoc-Bench",
 "MRAG-Bench","WebQA","Dyn-VQA","InfoSeek","E-VQA","FinRAGBench-V","REAL-MM-RAG","ArxivQA","TabFQuAD",
 "MMEB","M-BEIR","SPIQA","VisualMRC","TextVQA","2WikiMultiHopQA","HotpotQA","MuSiQue","LongBench",
 "FinQA","ChartMRAG","MultiHaystack","CRAG-MM","DocHaystack","InfoHaystack","BRIGHT","MIRACL-Vision",
 "Jina-VDR","BBox-DocVQA","SciEGQA","LongDocBench","MMVQA","PDF-MVQA","SciMMIR","OmniDocBench"]
BENCH = sorted(set(BENCH), key=len, reverse=True)
PAT = re.compile(r"(?<![\w-])(" + "|".join(re.escape(b) for b in BENCH) + r")(?![\w-])", re.I)
CANON = {b.lower(): b for b in BENCH}

METHODS = [
 [
  "ma2024dse",
  "Unifying Multimodal Retrieval via Document Screenshot Embedding",
  "Wiki-SS, SlideVQA"
 ],
 [
  "yuvisrag2025",
  "VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents",
  ""
 ],
 [
  "sun2025visrag2",
  "VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation",
  ""
 ],
 [
  "any1shot2025acl",
  "Any Information Is Just Worth One Single Screenshot: Unifying Search With Visualized Information Retrieval",
  ""
 ],
 [
  "globaldoc2025wacv",
  "GlobalDoc: A Cross-Modal Vision-Language Framework for Real-World Document Image Retrieval and Classification",
  ""
 ],
 [
  "fayssecolpali2025",
  "ColPali: Efficient Document Retrieval with Vision Language Models",
  "ViDoRe"
 ],
 [
  "masry2025colflor",
  "ColFlor: Towards BERT-Size Vision-Language Document Retrieval Models",
  ""
 ],
 [
  "masry2025colmate",
  "ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval",
  "ViDoRe V2"
 ],
 [
  "teiletche2025modernvbert",
  "ModernVBERT: Towards Smaller Visual Document Retrievers",
  ""
 ],
 [
  "meng2025vlm2vecv2",
  "VLM2Vec-V2: Advancing Multimodal Embedding for Videos, Images, and Visual Documents",
  ""
 ],
 [
  "nguyen2025serval",
  "SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models",
  ""
 ],
 [
  "xiaometaembed2026",
  "MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction",
  ""
 ],
 [
  "moreira2026nemotroncolembed",
  "Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval",
  "ViDoRe V3"
 ],
 [
  "lilac2025emnlp",
  "LILaC: Late Interacting in Layered Component Graph for Open-domain Multimodal Multihop Retrieval",
  ""
 ],
 [
  "evoretriever2026cvpr",
  "Evo-Retriever: LLM-Guided Curriculum Evolution with Viewpoint-Pathway Collaboration for Multimodal Document Retrieval",
  "MMEB, ViDoRe V2"
 ],
 [
  "realign2026sigir",
  "ReAlign: Optimizing the Visual Document Retriever with Reasoning-Guided Fine-Grained Alignment",
  ""
 ],
 [
  "agree2026sigir",
  "Attention Grounded Enhancement for Visual Document Retrieval",
  "ViDoRe V2"
 ],
 [
  "poqd2025icml",
  "POQD: Performance-Oriented Query Decomposer for Multi-vector retrieval",
  ""
 ],
 [
  "hybridvector2025",
  "Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy",
  ""
 ],
 [
  "storageeff2025acl",
  "Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings",
  ""
 ],
 [
  "prunemerge2026acl",
  "Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework",
  ""
 ],
 [
  "lightstar2026eccv",
  "LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement",
  ""
 ],
 [
  "uotvdr2026eccv",
  "Unbalanced Optimal Transport for Efficient Visual Document Retrieval",
  "ViDoRe"
 ],
 [
  "tilepool2026sigir",
  "Visual RAG at Scale: Tile-Level Spatial Pooling for Efficient Multi-Vector Document Retrieval",
  ""
 ],
 [
  "mvcompress2026sigir",
  "Multi-Vector Index Compression in Any Modality",
  ""
 ],
 [
  "cho2024m3docvqa",
  "M3DocVQA: Multi-modal Multi-page Multi-document Understanding",
  "M3DocVQA, MMLongBench-Doc, MP-DocVQA"
 ],
 [
  "chensvrag2025",
  "SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding",
  ""
 ],
 [
  "tanakavdocrag2025",
  "VDocRAG: Retrieval-Augmented Generation over Visually-Rich Documents",
  "OpenDocVQA"
 ],
 [
  "sun2025docagent",
  "DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding",
  ""
 ],
 [
  "suri2025visdom",
  "VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation",
  "VisDoMBench"
 ],
 [
  "cmrag2025",
  "CMRAG: Co-modality-based visual document retrieval and question answering",
  ""
 ],
 [
  "wu2025molorag",
  "MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval",
  ""
 ],
 [
  "hkrag2025",
  "HKRAG: Holistic Knowledge Retrieval-Augmented Generation Over Visually-Rich Documents",
  ""
 ],
 [
  "hikey2026",
  "HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question Answering",
  ""
 ],
 [
  "vragrl2025neurips",
  "VRAG-RL: Empower Vision-Perception-Based RAG for Visually Rich Information Understanding via Iterative Reasoning with Reinforcement Learning",
  ""
 ],
 [
  "urag2026aaai",
  "URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding",
  ""
 ],
 [
  "rap2025icml",
  "Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG",
  ""
 ],
 [
  "mg2rag2026eccv",
  "MG2-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation",
  ""
 ],
 [
  "robustvisrag2026cvpr",
  "RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations",
  ""
 ],
 [
  "simpledoc2025emnlp",
  "SimpleDoc: Multi‐Modal Document Understanding with Dual‐Cue Page Retrieval and Iterative Refinement",
  ""
 ],
 [
  "neusymrag2025acl",
  "NeuSym-RAG: Hybrid Neural Symbolic Retrieval with Multiview Structuring for PDF Question Answering",
  ""
 ],
 [
  "docreact2025acl",
  "Doc-React: Multi-page Heterogeneous Document Question-answering",
  ""
 ],
 [
  "mmhierrag2026kdd",
  "Multi-Modal Hierarchical Retrieval-Augmented Generation for Document Question Answering",
  ""
 ],
 [
  "mixedmodal2026sigir",
  "Towards Mixed-Modal Retrieval for Universal Retrieval-Augmented Generation",
  ""
 ],
 [
  "m3docdep2026cvpr",
  "M3DocDep: Multi-modal, Multi-page, Multi-document Dependency Chunking with Large Vision-Language Models",
  ""
 ],
 [
  "ma-etal-2025-visa",
  "VISA: Retrieval Augmented Generation with Visual Source Attribution",
  ""
 ],
 [
  "lfrag2026",
  "LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding",
  ""
 ],
 [
  "liregionrag2026",
  "RegionRAG: Region-level Retrieval-Augmented Generation for Visual Document Understanding",
  ""
 ],
 [
  "wangregionslm2026",
  "RegionSLM: Region-aware Question Answering on Document Screenshots",
  ""
 ],
 [
  "sourati-etal-2026-lad",
  "LAD-RAG: Layout-aware Dynamic RAG for Visually-Rich Document Understanding",
  "DUDE, LongDocURL, MMLongBench-Doc, MP-DocVQA"
 ],
 [
  "qin2026lmsretrieval",
  "LMS-Retrieval: Layout-Aware, Modality-Aware, Structure-Aware Document Retrieval",
  ""
 ],
 [
  "beyondgrid2026",
  "Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations",
  ""
 ],
 [
  "scan2026eacl",
  "SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation",
  ""
 ],
 [
  "lookthink2026aaai",
  "Look as You Think: Unifying Reasoning and Visual Evidence Attribution for Verifiable Document RAG via Reinforcement Learning",
  ""
 ],
 [
  "chainevidence2026sigir",
  "Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation",
  "2WikiMultiHopQA, SlideVQA"
 ],
 [
  "fragment2026sigir",
  "Purifying Multimodal Retrieval: Fragment-Level Evidence Selection for RAG",
  ""
 ],
 [
  "megrag2026sigir",
  "MEG-RAG: Quantifying Multi-modal Evidence Grounding for Evidence Selection in RAG",
  ""
 ],
 [
  "ansrerank2026sigir",
  "Good Ranks Follow Good Answers: Unsupervised Answer-Driven Reranking for Multimodal Document QA",
  ""
 ],
 [
  "utilitymrag2026acl",
  "Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented Generation",
  "MRAG-Bench"
 ],
 [
  "scopevlm2026eacl",
  "SCoPE VLM: Selective Context Processing for Efficient Document Navigation in Vision-Language Models",
  ""
 ],
 [
  "wang-etal-2025-vidorag",
  "ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents",
  "ViDoSeek"
 ],
 [
  "han2025mdocagent",
  "MDocAgent: A Multi-Modal Multi-Agent Framework for Document Understanding",
  ""
 ],
 [
  "jin2025slideagent",
  "SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding",
  ""
 ],
 [
  "zhu2025doclens",
  "DocLens: A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding",
  "FinRAGBench-V, MMLongBench-Doc"
 ],
 [
  "chen2026mardoc",
  "MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA",
  "MMLongBench-Doc, DocBench"
 ],
 [
  "mmagentr22026eccv",
  "MMAgent-R2: Learning to Rerank and Reject for Agentic mRAG",
  "E-VQA, InfoSeek"
 ],
 [
  "marsrl2026cvpr",
  "MARS-RL: Enhancing Multi-Agent RAG Systems for Multi-Modal Documents via Strategic Reasoning with Reinforcement Learning",
  "ViDoSeek"
 ],
 [
  "evsparsity2026cvpr",
  "Resolving Evidence Sparsity: Agentic Context Engineering for Long-Document Understanding",
  ""
 ],
 [
  "tracedoc2026acl",
  "TRACE: Traversal Retrieval-Augmented Chain of Evidence for Document Understanding",
  ""
 ],
 [
  "alden2026acl",
  "ALDEN: Reinforcement Learning for Active Navigation and Evidence Gathering in Long Documents",
  ""
 ],
 [
  "mdocragrl2026acl",
  "MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning",
  ""
 ],
 [
  "mmdocr12026acl",
  "MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning",
  "MMLongBench-Doc"
 ],
 [
  "docvstar2026acl",
  "Doc-V^*: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA",
  ""
 ]
]

def arxiv_find(title):
    q = 'ti:"' + re.sub(r'[^\w\s-]', ' ', title)[:200] + '"'
    for i in range(4):
        try:
            r = requests.get("https://export.arxiv.org/api/query", params={"search_query": q, "max_results": 5}, timeout=60)
            if r.status_code == 200: break
        except requests.RequestException: pass
        time.sleep(8 * (i + 1))
    else: return None, 0
    best, score = None, 0
    for e in ET.fromstring(r.text).findall("a:entry", NS):
        t = " ".join(e.findtext("a:title", "", NS).split())
        s = difflib.SequenceMatcher(None, t.lower(), title.lower()).ratio()
        if s > score:
            best, score = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1], s
    return best, round(score, 2)

def pdf_text(aid):
    r = requests.get(f"https://arxiv.org/pdf/{aid}", timeout=120)
    if r.status_code != 200: return ""
    with fitz.open(stream=io.BytesIO(r.content), filetype="pdf") as doc:
        return " ".join(p.get_text() for p in doc)

rows = []
for i, (key, title, known) in enumerate(METHODS, 1):
    aid, score = arxiv_find(title)
    text = pdf_text(aid) if aid and score >= 0.8 else ""
    counts = {}
    for m in PAT.finditer(text):
        b = CANON[m.group(1).lower()]; counts[b] = counts.get(b, 0) + 1
    hits = sorted(counts.items(), key=lambda x: -x[1])
    sugg = ", ".join(b for b, c in hits if c >= MIN_HITS)
    rows.append({"key": key, "title": title, "arxiv_id": aid, "title_match": score,
                 "found_in_abstract": known, "benchmarks_with_counts": "; ".join(f"{b} ({c})" for b, c in hits),
                 "suggested_dataset_cell": sugg,
                 "note": "" if text else "no arXiv PDF matched (check manually)"})
    print(f"[{i}/{len(METHODS)}] {key}: {sugg or '-'}")
    time.sleep(3.5)
pd.DataFrame(rows).to_excel("method_datasets.xlsx", index=False)
print("DONE -> method_datasets.xlsx")
