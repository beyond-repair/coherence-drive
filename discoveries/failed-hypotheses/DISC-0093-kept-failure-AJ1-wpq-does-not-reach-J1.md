# Discovery: Keeping w_pq in the Harnack identity plus AA's floor yields Conjecture J.1's 0.70 (Kept Failure AJ.1)

## Discovery ID

DISC-0093

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0092.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit bf808891d7ff130e78a8bc2722cad1e41effa794. Paths: GASKET.md Theorem AJ → Kept Failure AJ.1, Observation, NOT THIS; CLAIM_STATUS.md ("Neighbor-edge weight sharpens Harnack…" row: w_pq chain does not give 0.70); scripts/gasket_fractional_wpq_harnack.py.

## Original Evidence

GASKET.md Kept Failure AJ.1: "keeping the neighbor-edge cross term in the Harnack identity and combining with Theorem AA's floor yields ‖F(n,0.45)‖ ≥ 0.70" is false. The chain gives σ_AJ·0.084015 ≈ 0.055599; with live ‖F_frac(n)‖, σ_AJ‖F_frac(n)‖ ≈ (0.663639, 0.564099, 0.504167, 0.467750, 0.445101, 0.430641) on levels 1–6, all < 0.70; Harnack constant 0 gives only 2^(1−α)·0.084015 ≈ 0.1230.

## Discovery

Rejected hypothesis: the w_pq sharpening reaches Conjecture J.1's 0.70. False.

## Why It Matters

Second consecutive Harnack-constant refinement (after DISC-0091) that cannot reach 0.70; any such route from AA is capped at ≈0.123. DISC-0034 stays OPEN. Not thrust.

## Derivation

Direct comparison of the closed-form and live chains against 0.70; checked; no gap.

## Assumptions

As DISC-0092.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AJ.log`, EXIT 0, 217 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AJ.py` / `indep_theorem_AJ.log`, ALL PASS, 145 PASS) reproduce 0.055599, the six live chain values to 6 digits, and 0.123005, all < 0.70.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed σ_AJ, the AA product, live σ_AJ‖F_frac‖ through level 6, and 2^(1−α)·AA independently; matches GASKET.md and the commit message.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient condition for L≥0.70. DISC-0092 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0092. Mathematical. Theorem AJ.
- DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

None specific to this rejection.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0092.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AJ.1 at bf808891d7ff130e78a8bc2722cad1e41effa794; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
