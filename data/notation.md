# Notation and terminology

Every symbol used in the survey, in one place, in the order the paper
introduces them. Terms marked † are used differently elsewhere in this
literature; the usage below is normative within the survey.

**No symbol is reused.** Notation consistency is checked at review and it
is the cheapest thing in a survey to get wrong.

## Corpus and retrieval — Eq. (1)–(3)

| Symbol | Meaning |
|---|---|
| $q$ | a query |
| $a$ | the generated answer |
| $\mathcal{D}$ | the corpus |
| $d$ | a retrieval unit — here a **page**, not a passage |
| $\mathcal{R}_K(q) \subseteq \mathcal{D}$ | the set of $K$ units the retriever returns |
| $s(q,d)$ | relevance score of $d$ for $q$ |
| $K$ | retrieval depth (top-$K$) |
| $N$ | corpus size, in pages |
| $\mathbf{u}_i$ | the $i$-th query embedding, late interaction |
| $\mathbf{z}_j$ | the $j$-th document embedding — a **patch** for page images |

## The page and its channels — Eq. (4)–(6)

| Symbol | Meaning |
|---|---|
| $\Omega \subset \mathbb{R}^2$ | the page domain |
| $\mathcal{P}$ | a channel-annotated page |
| $\mathcal{C}$ | the channel set, $\lvert\mathcal{C}\rvert = 8$ |
| $m$ | the number of annotated regions on a page |
| $r_k \subseteq \Omega$ | the $k$-th page region |
| $c_k \in \mathcal{C}$ | its channel |
| $x_k$ | its content |
| $\mathcal{P}\vert_S$ | restriction of $\mathcal{P}$ to triples whose channel lies in $S$ |
| $\mathcal{P}\vert_\varnothing$ | the empty page |
| $\Delta_{ij}(q,\mathcal{P})$ | channel interference of $c_i$ and $c_j$ under query $q$ |
| $\omega(c_i,c_j)$ | region overlap between two channels |
| $\delta(c_i,c_j)$ | channel dissimilarity |

**Regions are not assumed disjoint.** A caption may lie inside a figure's
bounding box, a stamp may overprint a form field, a table may be embedded
in a chart. That non-disjointness is what distinguishes Eq. (4) from a
segmentation, and it is what makes Eq. (6) non-trivial.

## Encoding and cost — Eq. (5)

| Symbol | Meaning |
|---|---|
| $E$ | encoder, $E : \mathcal{P} \mapsto \mathbf{e}$ |
| $\mathbf{e}$ | the page embedding |
| $\psi(r_k, x_k)$ | local feature map — takes **position and appearance, not channel** |
| $\bigoplus$ | permutation-invariant pooling operator |
| $\phi$ | readout / projection head |
| $\pi$ | channel-forgetting map, $\pi(\mathcal{P}) = \{(r_k, x_k)\}$ |
| $\tilde{E}$ | the encoder that $E$ factors through: $E = \tilde{E} \circ \pi$ |
| $v$ | retained vectors per page |
| $t$ | tokens per page after parsing |
| $n$ | embedding dimension |

**The domain of $\psi$ is the whole of Proposition 1.** In every encoder
surveyed, it is a function of position and appearance alone; $c_k$ appears
nowhere in it, so $E$ factors through $\pi$ and cannot be injective.

## The channel-aware score — Eq. (7)

| Symbol | Meaning |
|---|---|
| $g(r)$ | graded relevance of a retrieved region |
| $c(r)$ | the channel of that region |
| $c^{*}(q)$ | the channel a query requires |
| $\mathcal{R}^{*}_{c}(q)$ | the ideal ranking restricted to channel $c$ |
| $\mathrm{CARS}_c(q)$ | channel-aware retrieval score, reported **per channel** |

$\mathrm{CARS}$ is reported for all eight channels against the channel each
query requires, forming an $8\times8$ confusion matrix whose off-diagonal
entries record which channel a system substituted for the one asked for.

---

## Terminology

### channel †

A *content type* occupying a page region. At least two recent works use
the same word for *modality* — the distinction between the textual and the
visual encoding of a page.

The two are **orthogonal**: one modality carries all eight channels, and
one channel is reachable through either modality. A reader who conflates
them will misread [the matrix](matrix.md) entirely, since its rows and
columns would then be the same thing.

### page †

**One rendered side of a document.** Several benchmarks count a multi-page
file as one "document", and the two conventions are *not interchangeable
when corpus sizes are compared* — which is why
[`datasets.csv`](datasets.csv) carries a `unit` column recording which one
each row uses.

### interference †

Non-additivity of retrieval score across co-located channels. **Not** the
signal-processing sense. Formally it is the discrete second difference of
the score in two channels, and it vanishes exactly when the retriever's
response to the pair is the sum of its responses to each alone.

### modality

The form in which a page reaches an encoder: parsed text, or pixels.

### granularity

The size of the retrieval unit: page, element or region. Read down the
`Gran.` column of [`methods.md`](methods.md) and it stays at the page
until 2025.

### paradigm

One of four system classes — OCR→LLM, MLLM-native, text RAG,
visual/multimodal RAG. These are the columns of [the matrix](matrix.md).

### parsing

Conversion of a page image to a structured representation. OCR is its
text-only case, and the distinction matters: the parsing literature moved
to structured output at the same moment the retrieval literature moved to
pooling it away.

### coverage

The proportion of a page occupied by a given channel. Qiao et al. use this
as a single scalar and find it predictive of retrieval robustness; the
eight channels are a refinement of a variable the field has already found
to work.
