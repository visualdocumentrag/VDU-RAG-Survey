# Benchmarks and datasets

[← Back to the main list](../README.md)

Scope: ML = multilingual, MD = multi-domain, MT = multi-type, MM = multi-modality (only when stated by the dataset's authors). A blank Size, Queries or Metric cell is not reported in a form we could verify. Channels: ● annotated, ○ present but not annotated, – absent.

## Retrieval & RAG

|Dataset|Year|Lang.|Scope|Size|Queries|Metric|Txt|Lay|Tab|Fig|Eqn|Frm|Stp|Typ|Link|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[ViDoRe v1](https://arxiv.org/abs/2407.01449)|2025|EN, FR|ML, MD, MT, MM| | |nDCG@5|●|○|○|○|○|○|–|–|[link](https://huggingface.co/collections/vidore/vidore-benchmark)|
|[ViDoRe v2](https://arxiv.org/abs/2505.17166)|2025|multi|ML, MD| | | |●|○|○|○|○|○|–|–|[link](https://huggingface.co/collections/vidore/vidore-benchmark-v2)|
|[ViDoRe v3](https://arxiv.org/abs/2601.08620)|2026|6 langs|ML, MM| | | |●|●|●|●|○|○|–|–|[link](https://huggingface.co/collections/vidore/vidore-benchmark-v3)|
|MMDocIR|2025|EN|MM| | | |●|●|●|●|○|○|–|–|[link](https://huggingface.co/MMDocIR)|
|[MMDocRAG](https://arxiv.org/abs/2505.16470)|2025|EN|MM| | | |●|○|●|●|○|○|–|–|[link](https://github.com/MMDocRAG/MMDocRAG)|
|[M3DocVQA](https://arxiv.org/abs/2411.04952)|2025|EN|MM|40K+ pages| | |●|○|○|●|○|○|–|–|[link](https://github.com/bloomberg/m3docrag)|
|[ViDoSeek](https://aclanthology.org/2025.emnlp-main.464)|2025|EN|–| | | |●|○|○|○|○|○|–|–|[link](https://github.com/Alibaba-NLP/ViDoRAG)|
|[UniDoc-Bench](https://arxiv.org/abs/2510.03663)|2025|EN|MD, MM|70K pages| | |●|●|●|○|○|○|–|–|[link](https://github.com/SalesforceAIResearch/UniDOC-Bench)|
|[BBox-DocVQA](https://arxiv.org/abs/2511.15090)|2025|EN|MD, MM|3.6K docs|32K| |●|●|○|○|○|○|–|–|–|

## Document QA

|Dataset|Year|Lang.|Scope|Size|Queries|Metric|Txt|Lay|Tab|Fig|Eqn|Frm|Stp|Typ|Link|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[DocVQA](https://doi.org/10.1109/WACV48630.2021.00225)|2021|EN|MT|12,767 images|50,000|ANLS|●|○|○|–|–|○|–|–|[link](https://www.docvqa.org)|
|InfographicVQA|2022|EN|MM|5,485 images|30,035|ANLS|●|●|○|●|–|–|–|–|[link](https://www.docvqa.org)|
|ChartQA|2022|EN|–|20,882 charts|32,719|relaxed acc.|○|–|–|●|–|–|–|–|[link](https://github.com/vis-nlp/ChartQA)|
|TAT-DQA|2022|EN|MM|2,758 docs|16,558|EM, F1|●|○|●|–|–|–|–|–|[link](https://github.com/NExTplusplus/TAT-DQA)|
|SPIQA|2024|EN|MM| |270K| |●|○|●|●|○|–|–|–|[link](https://huggingface.co/datasets/google/spiqa)|
|[LongDocURL](https://arxiv.org/abs/2412.18424)|2024|EN|MM|396 docs|2,325| |●|●|●|●|○|○|–|–|[link](https://github.com/dengc2023/LongDocURL)|
|[MTVQA](https://arxiv.org/abs/2405.11985)|2025|9 langs|ML| | | |●|○|○|○|–|○|–|–|[link](https://github.com/bytedance/MTVQA)|

## Channel-specific

|Dataset|Year|Lang.|Scope|Size|Queries|Metric|Txt|Lay|Tab|Fig|Eqn|Frm|Stp|Typ|Link|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|FUNSD|2019|EN|–|199 forms| |F1|●|○|–|–|–|●|–|–|[link](https://guillaumejaume.github.io/FUNSD/)|
|[VRDU](https://doi.org/10.1145/3580305.3599929)|2023|EN|–| | | |●|○|–|–|–|●|–|–|[link](https://github.com/google-research-datasets/vrdu)|
|[DocLayNet](https://doi.org/10.1145/3534678.3539043)|2022|EN|MD, MT, MM|80,863 pages| |mAP|●|●|●|●|●|–|–|–|[link](https://github.com/DS4SD/DocLayNet)|
|PubTables-1M|2022|EN|–| | |GriTS|○|○|●|–|–|–|–|–|[link](https://github.com/microsoft/table-transformer)|
|[UniMER](https://arxiv.org/abs/2404.15254)|2024|not stated|–| | | |○|–|–|–|●|–|–|–|[link](https://github.com/opendatalab/UniMERNet)|
|[SPODS](https://doi.org/10.1007/978-3-319-68124-5_19)|2017|not stated|–| | | |○|○|–|–|–|–|●|–|[link](https://facweb.iitkgp.ac.in/~jay/spods/index.html)|
|ReST|2023|ZH|–| | | |○|–|–|–|–|–|●|–|–|
|[DKDS](https://arxiv.org/abs/2511.09117)|2025|JA|–| | | |○|○|–|–|–|–|●|–|[link](https://github.com/RuiyangJu/DKDS)|
|[TexTAR](https://doi.org/10.1007/978-3-032-04614-7_16)|2026|multi|ML, MD| | | |●|○|–|–|–|–|–|●|[link](https://github.com/tex-tar/tex-tar)|
