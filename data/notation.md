# Notation

Table 2 of the survey.

| Symbol | Meaning |
|---|---|
| 𝒟, q, a | corpus of pages, query, generated answer |
| ℛ_K(q) | the K units retrieved for q |
| E_Q, E_D | query and document encoders |
| u_t, z_j | query-token and page-patch vectors |
| N, t, v, n | pages in corpus, tokens per parsed page, vectors retained per page, embedding dimension |
| Ω | page domain, Ω ⊂ ℝ² |
| 𝒞 | set of content channels, |𝒞| = 8 |
| 𝒫 = {(r_k, c_k, x_k)} | channel-annotated page: region, channel, content |
| ψ, ⊕, φ | local feature map, permutation-invariant pooling, readout |
| π | channel-forgetting map of Proposition 1 |
| 𝒫|_S | restriction of 𝒫 to channels in S ⊆ 𝒞 |
| Δ_ij | second-order interference of channels i and j |
| ω, σ | region overlap and appearance similarity of a channel pair |
| g(r), c*(q) | graded relevance of a region; channel a query requires |
| CARS_c | channel-aware retrieval score |

**Channel interference.** Δ_ij(q, 𝒫) = s(q, 𝒫|{i,j}) − s(q, 𝒫|{i}) − s(q, 𝒫|{j}) + s(q, 𝒫|∅).

Under additive scoring (sum pooling, affine readout, bilinear score) Δ_ij vanishes for disjoint channels. Under late interaction (MaxSim) it does not: Δ_ij = −Σ_t min(a_t, b_t).
