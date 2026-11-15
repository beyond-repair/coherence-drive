# Discovery: Kept Failure BL.0, Conjecture BK.6 as worded fails at N=0

## Discovery ID

DISC-0158

## Status

REJECTED (repository's own Kept Failure; the original wording of BK.6, not the restated N≥1 form).

## Date Discovered

2026-10-23 (America/New_York), ~4:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit dfc145a9833f96b8960667c572aca38d48adfc17.

## Original Evidence

GASKET.md Kept Failure BL.0 and the annotated Conjecture BK.6 heading at dfc145a9833f96b8960667c572aca38d48adfc17.

## Discovery

BK.6 asserted ρ^n(δ_N−δ_N^(n))→C_δ(α)>0 for every N. At N=0 the 'neighbours' are the corners b and c themselves, so δ_0^(n)=3/2 for every n and ρ^n(δ_0−δ_0^(n))=0. The conjecture is restated for N≥1.

## Why It Matters

Records exactly where the original statement breaks; the restated form is what DISC-0157 partly proves.

## Derivation

Immediate from the definition: η_0=−1/2 gives G≡3/2.

## Assumptions

Corner data with x_a≠d̄.

## New Results

Witness: δ_0^(n)≡3/2.

## Prior Art

Not applicable.

## Novelty Analysis

KNOWN-type degenerate case (definitional).

## Falsification Attempts

Reproduced independently on my own gasket graph, levels 0–7, α=0.8, data (1,−1/2,−1/2) and (1,0.3,−0.8): δ_0^(n)=3/2 to 1e−10 at every n. PASS.

## Experimental Validation

Exact.

## Mathematical Status

Counterexample (kept failure).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0156 → DISC-0158 (historical: BK.6 as first worded). DISC-0157 → DISC-0158.

## Open Questions

None.

## Next Experiments

None.

## Reproduction Instructions

git checkout dfc145a9833f96b8960667c572aca38d48adfc17; GASKET.md Kept Failure BL.0.

## Evidence Log

- 2026-10-23 ~4:54am EDT. Indexed and independently reproduced.

## Change History

- 2026-10-23. Initial archive entry.
