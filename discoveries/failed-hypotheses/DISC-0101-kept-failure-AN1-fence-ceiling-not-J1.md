# Discovery: The boundary-fence ceiling combined with AK's share floor reaches Conjecture J.1's 0.70 (Kept Failure AN.1)

## Discovery ID

DISC-0101

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0100.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7edc36aaf6f28959f43698c7c1b8f37230ec8be5. Paths: GASKET.md Theorem AN → Kept Failure AN.1, NOT THIS; Conjecture J.1 evidence paragraph; CLAIM_STATUS.md (boundary-fence row); scripts/gasket_fractional_fence_ceiling.py (Kept Failure AN.1 section).

## Original Evidence

GASKET.md Kept Failure AN.1: the claim "replacing the cycle by the boundary fence/collar and combining with Theorem AK's share floor yields ‖F(n,0.45)‖≥0.70" is false. The chain gives σ_AK·0.305377≈0.214239. Even the absolute one-step envelope 2^(1−α)·0.305377≈0.4471, or the live share σ_n≈1.3525 times the new floor (≈0.4130), stays below 0.70. Using the sharper extrapolated collar limit R^col_∞≈4.91 (δ≈0.406) only lifts the σ_AK floor to ≈0.2177. As Kept Failure AM.1 already recorded, no resistance ceiling can rescue the σ_AK chain. The fence still leaves a gap to the live gasket resistance (5.00 against ≈2.35).

## Discovery

Rejected hypothesis: the boundary-fence ceiling of DISC-0100 combined with σ_AK proves Conjecture J.1's 0.70. False. Confirms and continues DISC-0099's rejection of the whole energy-floor×σ_AK family (AN does not rescue that chain).

## Why It Matters

Confirms that further ceiling sharpenings (cycle → fence) cannot close DISC-0034 along the σ_AK chain; the obstruction remains the share floor. DISC-0034 stays OPEN. Not thrust.

## Derivation

σ_AK·0.305377≈0.214239 < 0.70; 2^(1−α)·0.305377≈0.447097 < 0.70; live-σ·0.305377≈0.413022 < 0.70; sharp-collar (R^fen_∞+0.42) σ_AK floor ≈0.217721 < 0.70. Live σ_AK·‖F_frac‖_live on L2–5 (same values as AM.1) already < 0.70, so AN's better fractional floor cannot lift the chain. Checked; no gap.

## Assumptions

As DISC-0100.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AN.log`, EXIT 0, 109 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AN.py` / `indep_theorem_AN.log`, ALL PASS, 137 PASS) reproduce AN floor 0.214239, envelope 0.447097, live-σ·Ffrac≈0.413022, sharp 0.217721, all <0.70; live σ_AK·‖F_frac‖ on L2–5 = 0.598008, 0.534474, 0.495867, 0.471857 < 0.70 (AN does not rescue AM.1); at L5 a share floor ≥≈1.0408 would be needed (σ_AK≈0.7016); Rceil=5.0021 ≫ live R(L5)=2.2711.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed envelopes and confirmed the live chain independently with own builder; matches GASKET.md. The rejection is analytic for the stated envelopes; the live-chain observation reuses AM.1.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. DISC-0100 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0100. Mathematical. Theorem AN.
- DISC-0099. Failed hypothesis. Energy-floor×σ_AK family; AN.1 continues that rejection.
- DISC-0097, DISC-0095, DISC-0093, DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

Whether a share floor near the live σ_n≈1.35 can be proved; not addressed by the repository.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0100.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AN.1 at 7edc36aaf6f28959f43698c7c1b8f37230ec8be5; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
