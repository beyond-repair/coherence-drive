# Discovery: Kept Failure BG.1, the flat refinement limit below γ is not uniform

## Discovery ID

DISC-0147

## Status

REJECTED (the hypothesis "u_n → d̄ uniformly on V_n \ V_0 for α ≤ γ" fails at α = 0.45; repository's own Kept Failure, certified). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 073ace5091ac17b2adcd2eb956ef8f0bf0a14bce, GASKET.md "Kept Failure BG.1"; scripts/gasket_fractional_extension_limit.py.

## Original Evidence

For data (1, −1/2, 0) at α = 0.45 the mean of the two neighbours of corner a is 1 − 5‖F(n)‖/(2√21) (Theorem J's Schur form). With ‖F(n)‖ ↓ 𝓛(0.45), the gap above d̄ increases to 5/6 − 5𝓛(0.45)/(2√21) = 0.3853654863… (certified via AS re-run). So sup |u_n − d̄| stays above 0.3853 although u_n → d̄ at every fixed vertex (DISC-0146).

## Discovery

A corner boundary layer of shrinking width carries the data; BG.2's bound grows like 5^(m(1−α)) and cannot be made uniform.

## Why It Matters

Rules out a uniform (continuous-function) limit below γ; any continuum object must be a measure-like or polar-corner description.

## Derivation

Repository's (Theorem J Schur form plus AQ/AS monotone limit of ‖F‖).

## Assumptions

As DISC-0146; certified 𝓛(0.45) from AS (DISC-0111).

## New Results

Certified non-uniformity gap 0.3853654863….

## Prior Art

Boundary layers at polar points are the expected discrete shadow of point polarity (KNOWN qualitatively).

## Novelty Analysis

Qualitative phenomenon KNOWN-type; constant internal to the corpus, novelty UNRESOLVED.

## Falsification Attempts

Archive dense solves at α = 0.45, n = 1..6 reproduce the repository's neighbour means 0.214634, 0.363945, 0.436850, 0.478347, 0.503722, 0.519861 to 6 digits (increasing), gaps 0.047967 … 0.353195, consistent with the certified limit 0.38537 from below. The repository text calls them gap values next to a formula for the gap; they are the means (reading note).

## Experimental Validation

Computational only.

## Mathematical Status

Proved failure (counterexample with certified constant).

## Patent Relevance

None.

## Related Discoveries

DISC-0146 → DISC-0147 (failed hypothesis); DISC-0111 → DISC-0147 (computational).

## Open Questions

Width scaling of the corner layer.

## Next Experiments

Measure the layer profile u_n at distance 2^−k from a corner as n grows.

## Reproduction Instructions

As DISC-0146.

## Evidence Log

- 2026-10-22. Archive check inside indep_theorem_BG.py (6 PASS rows "corner-neighbour gap").

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22 ~10:00pm EDT. Status unchanged (REJECTED). informational-flux-identity 156d8ce80c73147e3dc8aa34cbcea2ce6e42d989 (Theorem BH, DISC-0149) resolves the layer: u_n(2^−n ξ)→d̄+x_a Θ(ξ) for α<γ, and the gap x_a θ_0 now holds at each neighbour separately (exact asymmetry (x_b−x_c)I_n/D_n ≤ 5^−n). Open question "width scaling" answered: decay ρ per doubling (BH.6). Earlier text kept.
