# Discovery: Resistance weights freeze the α=0.45 fractional audit (Kept Failure S.1)

## Discovery ID

DISC-0052

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0051.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d22771de4351d86c5b04d52e36bcfe1a0a22744f. Paths: GASKET.md Theorem S → "KEPT FAILURE S.1 (no fractional freeze from resistance weights)"; scripts/gasket_uniform_weights.py.

## Original Evidence

Spectral calculus: L_res = (5/3)^n L_comb ⇒ L_res^α = (5/3)^{nα} L_comb^α, so the L_res^α-Dirichlet solution coincides with the combinatorial fractional solution. Weighted corner currents are then (5/3)^n times combinatorial, and

‖F_res(n, 0.45)‖ = (5/3)^n ‖F(n, 0.45)‖.

Kept Failure H.1 already says combinatorial ratios are not 3/5, so the product is not level-independent. Recorded resistance-scaled norms through level 7 are strictly increasing ≈ (2.399, 3.239, 4.779, 7.378, 11.699, 18.864, 30.751), while the harmonic resistance value is the constant √21/2 ≈ 2.291.

## Discovery

Rejected hypothesis: resistance weights λ = 5/3 freeze the α = 0.45 fractional audit at a finite nonzero constant by the same cancellation that makes the harmonic audit constantly √21/2. False as an inheritance.

## Why It Matters

Closes one hoped-for route to a finite nonzero α = 0.45 limit. The combinatorial ‖F(n, 0.45)‖ question remains OPEN (DISC-0034).

## Derivation

DISC-0051 / Theorem S plus spectral calculus and Kept Failure H.1. Checked; no gap.

## Assumptions

Uniform resistance weights; spectral calculus for L^α; recorded combinatorial fractional norms.

## New Results

Archive witness rerun: live through level 4, ‖F_res‖ = (5/3)^n ‖F_comb‖ and strictly increasing; recorded scaled sequence through level 7 matches GASKET.md. Log: `/workspace/scratch-ifi/indep_uniform_S.log`.

## Prior Art

Not applicable (rejection of a route).

## Novelty Analysis

None.

## Falsification Attempts

Tried the inheritance reading; the scaled sequence is strictly increasing and already past 30 at level 7.

## Experimental Validation

None.

## Mathematical Status

Correct as a negative result.

## Patent Relevance

None.

## Related Discoveries

- DISC-0051. Mathematical. Theorem S.
- DISC-0031 / DISC-0033. Kept Failure H.1 and other shortcut laws.
- DISC-0034. Conjecture. Combinatorial limit still OPEN.

## Open Questions

Whether combinatorial ‖F(n, 0.45)‖ → 0 or a positive finite L (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0051.

## Evidence Log

- 2026-10-08. Recorded from GASKET.md Kept Failure S.1 at d22771de4351d86c5b04d52e36bcfe1a0a22744f.

## Change History

- 2026-10-08. Initial archive entry.
