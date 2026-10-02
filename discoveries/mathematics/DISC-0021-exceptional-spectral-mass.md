# Discovery: Exceptional spectral mass μ_exc → 5/9

## Discovery ID

DISC-0021

## Status

DERIVATIVE

## Date Discovered

2026-10-02. Archive pass for beyond-repair/finite-gasket-spectral-derivatives exceptional-mass commit.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at commit 6b512290310ae15eb2f854f1fa6b608035613061 (indexed under HEAD 19a1264e4511a2ff2e60e55040590e250372d3f0). README section “Exceptional spectral mass”; COMPLETION_LOG.md; CLAIM_STATUS.md.

Depends on free mult(3), mult(5), mult(6) indexed as DISC-0020, and on |V_n| = (3^{n+1} + 3)/2 from gasket_graph.py / SPECTRUM.md.

## Original Evidence

CLAIM_STATUS.md marks Exceptional mass M_exc = (5·3^{n−1} − 7)/2, μ_exc → 5/9 (n ≥ 3) as **CLAIMED**, corollary of the three free mult theorems plus |V_n|.

README theorem structure: for n ≥ 3,

    M_exc(n) := mult(3)+mult(5)+mult(6) = (5·3^{n−1} − 7)/2,
    μ_exc(n) := M_exc(n)/N(n) = (5·3^{n−1} − 7)/(3^{n+1} + 3) → 5/9,

with 1 − μ_exc → 4/9. Case n = 2 recorded separately (mass 5/15 = 1/3). Explicit refusal: this does **not** prove that remaining eigenvalues are R-preimages, nor that any hit-rate equals 1 − μ_exc. SPECTRUM.md “hit rates … roughly 0.4–0.7” stays numerical.

## Discovery

Given the three free-multiplicity formulas and the vertex count, the exceptional mass fraction and its limit 5/9 are elementary algebra. They do not upgrade free decimation hit rates.

## Why It Matters

Separates a closed mass-fraction corollary from the still-open hit-rate predicate, and from any W / thrust reading.

## Derivation

No derivation is repeated here. Sum the DISC-0020 formulas and divide by N(n).

## Assumptions

DISC-0020 free-multiplicity formulas for n ≥ 3; N(n) = (3^{n+1} + 3)/2 from the constructor.

## New Results

None beyond the repository’s corollary.

## Prior Art

Exceptional values {3, 5, 6} are classical in SG spectral decimation. The free mass fraction μ_exc → 5/9 is an arithmetic corollary of the free multiplicity claims, not a classical Dirichlet statement by itself.

## Novelty Analysis

Status is DERIVATIVE once DISC-0020 is granted. If DISC-0020 falls, this row falls with it.

## Falsification Attempts

Algebra checked: M_exc(n) = (5·3^{n−1} − 7)/2 and μ_exc formula hold for n = 3..6; n = 2 separate case matches README. Local eigvalsh support for M_exc = 19, 64, 199 at n = 3, 4, 5 (via DISC-0020 numerics). Hit-rate upgrade refused in-repo; not claimed here.

## Experimental Validation

None.

## Mathematical Status

Derivative corollary of DISC-0020 plus |V_n|.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0020. Mathematical. Source multiplicity formulas.
- DISC-0005. Mathematical. SPECTRUM.md exceptional values and hit-rate observation.
- DISC-0007. Mathematical. Does not select W.
- DISC-0002. Mathematical. Mass fraction is not thrust.

## Open Questions

Precise free hit predicate and any equality with 1 − μ_exc remain open.

## Next Experiments

Do not cite 4/9 as a proved hit rate. Keep μ_exc separate from hit-rate strings in SPECTRUM.md.

## Reproduction Instructions

Read README “Exceptional spectral mass” and COMPLETION_LOG at 6b512290310ae15eb2f854f1fa6b608035613061 / HEAD 19a1264e4511a2ff2e60e55040590e250372d3f0. Check algebra against DISC-0020 formulas.

## Evidence Log

- 2026-10-02. Read exceptional-mass section at 6b512290310ae15eb2f854f1fa6b608035613061; algebra verified locally.

## Change History

- 2026-10-02. Initial archive entry.
