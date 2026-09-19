# Channel × paradigm matrix

Table 5 of the survey. A method counts in a cell only if it **reports a result on that channel**; being able to handle the channel in principle is not enough.

**●** results reported · **○** the task exists but no method of that paradigm reports against it · **—** nothing reported

| Channel | OCR → LLM | MLLM-native | Text RAG | Visual / multi-modal RAG |
|---|:-:|:-:|:-:|:-:|
| **Plain text** | ● | ● | ● | ● |
| **Layout** | ● | ● | ● | ● |
| **Tables** | ● | ● | ● | ● |
| **Figures** | ● | ● | ● | ● |
| **Equations** | ● | ● | ● | ○ |
| **Form fields** | ● | ● | ● | ● |
| **Stamps** | — | — | — | — |
| **Typography** | — | — | — | — |

## Reading the matrix

* **Dense — plain text × visual RAG.** Where the field has worked; best scores fall each time the benchmark is made harder (ViDoRe v1 → v3).
* **Reachable — equations × visual RAG.** Formula retrieval has a decade of task definitions (NTCIR) and recognition benchmarks, but no visual document retriever reports against them.
* **Empty — stamps and typography × every paradigm.** Seal detection and font recognition exist, but neither reports a retrieval or question-answering result. These cells name experiments that need a resource to be built first.

The works behind each row are listed in the channel sections of the [README](../README.md#the-eight-channels).
