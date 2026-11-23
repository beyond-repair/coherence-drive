# Discovery: Replacing κ by 1 in AH plus AA's floor yields Conjecture J.1's 0.70 (Kept Failure AI.1)

## Discovery ID

DISC-0091

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0090.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8. Paths: GASKET.md Theorem AI → Kept Failure AI.1, Observation, NOT THIS; CLAIM_STATUS.md ("Two-neighbor heat-kernel sum…" row: κ→1 chain does not give Conjecture J.1's 0.70); scripts/gasket_fractional_harnack_sum.py.

## Original Evidence

GASKET.md Kept Failure AI.1: "replacing κ by 1 in AH and combining with AA's floor yields ‖F(n,0.45)‖ ≥ 0.70 (Conjecture J.1's value)" is false. The chain gives σ_AI · 0.084015 ≈ 0.051988; even with live ‖F_frac(n)‖ in place of AA's floor, σ_AI ‖F_frac(n)‖ ≤ 0.620534 through level 6; and even Harnack constant 0 gives only 2^(1−α)·0.084015 ≈ 0.123005 < 0.70.

## Discovery

Rejected hypothesis: the κ→1 sharpening of Theorem AH, combined with Theorem AA's fractional-current floor, reaches Conjecture J.1's numerical value 0.70. False; the best AA-route bound under any Harnack constant is ~0.123.

## Why It Matters

Shows that raising the Harnack constant alone cannot prove Conjecture J.1 from AA. DISC-0090 still supplies a sharper positive floor (~0.052). DISC-0034 (convergence / L≥0.70) stays OPEN. Not thrust.

## Derivation

Direct numerical comparison of the closed-form chain against 0.70; checked; no gap.

## Assumptions

As DISC-0090.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AI.log`, EXIT 0) and independent archive (`/workspace/scratch-ifi/indep_theorem_AI.py` / `indep_theorem_AI.log`, own builder, ALL PASS) both give σ_AI·0.084015≈0.051988, live chain ≤0.620534, and perfect-Harnack bound ≈0.123005, all strictly below 0.70.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed σ_AI, AA floor product, live σ_AI‖F_frac‖ through level 6, and 2^(1−α)·AA independently; matches GASKET/commit message.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient condition for L≥0.70. DISC-0090 still supplies a positive floor by a different (weaker) constant. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0090. Mathematical. Theorem AI (the working sharpened floor).
- DISC-0089, DISC-0033. Failed hypotheses. Other rejected shortcuts toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN; vanishing closed by DISC-0088/0090.

## Open Questions

None specific to this rejection.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0090 (`scripts/gasket_fractional_harnack_sum.py`; archive indep_theorem_AI.py).

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AI.1 at cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
