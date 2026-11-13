# Discovery: The depth-2 collar ceiling combined with AK's share floor reaches Conjecture J.1's 0.70 (Kept Failure AO.1)

## Discovery ID

DISC-0103

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0102.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7f0099c3161ce2fa714c414cbae44bb316fc68f2. Paths: GASKET.md Theorem AO → Kept Failure AO.1, NOT THIS; Conjecture J.1 evidence paragraph; CLAIM_STATUS.md; scripts/gasket_fractional_depth2_ceiling.py (Kept Failure AO.1 section).

## Original Evidence

GASKET.md Kept Failure AO.1: the claim "replacing the depth-1 fence by the depth-2 collar and combining with Theorem AK's share floor yields ‖F(n,0.45)‖≥0.70" is false. The chain gives σ_AK·0.316911≈0.222331. Even the absolute one-step envelope 2^(1−α)·0.316911≈0.4640, or the live share σ_n≈1.3525 times the new fractional floor (≈0.4286), stays below 0.70. The sharper extrapolated defect δ₂≈0.53 only lifts the σ_AK floor to ≈0.2233. As Kept Failures AM.1–AN.1 recorded, no resistance ceiling can rescue the σ_AK chain; the ceiling 4.82 is still more than twice the live resistance ≈2.35.

## Discovery

Rejected hypothesis: the depth-2 collar ceiling of DISC-0102 combined with σ_AK proves Conjecture J.1's 0.70. False. Continues DISC-0099 / DISC-0101's rejection of the energy-floor×σ_AK family.

## Why It Matters

Confirms that thickening the boundary collar cannot close DISC-0034 along the σ_AK chain; the obstruction remains the share floor. DISC-0034 stays OPEN. Not thrust.

## Derivation

σ_AK·0.316911≈0.222331 < 0.70; 2^(1−α)·0.316911≈0.463985 < 0.70; 1.3525·0.316911≈0.428622 < 0.70; sharp (R^d2_∞+0.53) ≈0.223257 < 0.70; with the archive's accurate R^d2_∞≈4.269089 and δ₂(L10)≈0.445084 the floor is ≈0.227324 < 0.70. Live σ_AK·‖F_frac‖_live on L2–7 = 0.598008, 0.534474, 0.495867, 0.471857, 0.456527, 0.446523 < 0.70, so no ceiling (however sharp) lifts the chain: reaching 0.70 via σ_AK would need R ≤ ≈1.5309, below even the live R(L7)≈2.4000. Checked; no gap.

## Assumptions

As DISC-0102.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AO.log`, EXIT 0, 84 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AO.py` / `indep_theorem_AO.log`, ALL PASS, 81 PASS) reproduce 0.222331, 0.463985, 0.428622, 0.223257 to 6 digits, all < 0.70; live chain through L7 as above.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed envelopes, used the sharper accurate ceiling and the level-10 defect, and extended the live chain to L7 with the own builder. All stay below 0.70.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. DISC-0102 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0102. Mathematical. Theorem AO.
- DISC-0101, DISC-0099. Failed hypotheses. Fence / energy-floor×σ_AK family; AO.1 continues that rejection.
- DISC-0097, DISC-0095, DISC-0093, DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

Whether a share floor near the live σ_n≈1.35 can be proved; not addressed by the repository.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0102.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AO.1 at 7f0099c3161ce2fa714c414cbae44bb316fc68f2; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
