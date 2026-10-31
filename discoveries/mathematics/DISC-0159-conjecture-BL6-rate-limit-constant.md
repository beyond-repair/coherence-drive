# Discovery: Conjecture BL.6, the limit C_δ(0.8)=lim ρ^n(δ_N−δ_N^(n)) exists (floats ≈0.6025)

## Discovery ID

DISC-0159

## Status

CONJECTURE (repository's own; floats only). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~4:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit dfc145a9833f96b8960667c572aca38d48adfc17.

## Original Evidence

GASKET.md Conjecture BL.6 at dfc145a9833f96b8960667c572aca38d48adfc17; floats in scripts/gasket_fractional_rate_sharpness.py: ρ^n(δ_10^(100)−δ_10^(n))=0.6300…0.6028 at n=10–40.

## Discovery

The repository conjectures the limit exists, with C_δ(0.8)≈0.6025, about 4.9× the certified floor 0.1240 of DISC-0157 and inside the certified window [c_N, 4.6644].

## Why It Matters

It would upgrade the two-sided bound of DISC-0157 to an asymptotic.

## Derivation

None (numerical).

## Assumptions

Theorems BK and BL as stated.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Floats consistent with DISC-0157's window; not attacked beyond that.

## Experimental Validation

Floats only.

## Mathematical Status

Conjecture.

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0156 → DISC-0159 (historical: the limit half of BK.6, restated for N≥1). DISC-0157 → DISC-0159.

## Open Questions

Existence and value of the limit; dependence on N.

## Next Experiments

Extend floats to n=60–90; test whether the limit is N-independent for N≥9.

## Reproduction Instructions

git checkout dfc145a9833f96b8960667c572aca38d48adfc17; python3 scripts/gasket_fractional_rate_sharpness.py (float section).

## Evidence Log

- 2026-10-23 ~4:54am EDT. Indexed from the repository's float evidence.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-23 ~6:53am EDT. Repository floats in Theorem BM (c9ca93479dbee307e77705a052d995029938a630) give ρ^n(δ_6^(60)−δ_6^(n))≈0.364 at α=0.9 against ≈0.6025 at α=0.8, so C_δ, if it exists, depends on α. Still CONJECTURE (floats only).
- 2026-10-23 ~8:00am EDT. Status split: monotonicity clause (δ_N^(n) increasing in n for every N≥1) proved for α≥1/17 by Theorem BN (DISC-0161, informational-flux-identity 335860e44ebf) → THEOREM; limit clause (existence and N-independence of C_δ) stays CONJECTURE. Earlier text kept above.
