# Discovery: Replacing C by R_∞ and combining with AK's share floor reaches Conjecture J.1's 0.70 (Kept Failure AL.1)

## Discovery ID

DISC-0097

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0096.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 483de961575bca353a2cd3ff6719b8a357610a87. Paths: GASKET.md Theorem AL → Kept Failure AL.1, NOT THIS; Conjecture J.1 evidence paragraph; CLAIM_STATUS.md ("Sharp path-resistance ceiling R_∞…" row: σ_AK·0.111208≈0.078; even 2^(1−α)·0.111208≈0.163); scripts/gasket_fractional_path_ceiling.py.

## Original Evidence

GASKET.md Kept Failure AL.1: the claim "replacing Theorem AA's C(α) by R_∞(α) and combining with Theorem AK's share floor yields ‖F(n,0.45)‖≥0.70" is false. The chain gives σ_AK·0.111208≈0.078019. Even the absolute one-step envelope 2^(1−α)·0.111208≈0.1628, or the live share σ_n≈1.3525 times the new fractional floor (≈0.1504), stays below 0.70. The obstruction is the path comparison itself: live gasket resistance at 0.45 is near 2.35, while R_∞≈13.25.

## Discovery

Rejected hypothesis: sharpening AA's path ceiling to R_∞ and combining with AK's share floor proves Conjecture J.1's 0.70. False; this route is different from the one-step neighbor-Harnack family closed in Kept Failure AK.1, and both fall short of 0.70.

## Why It Matters

Closes a second, independent route family toward J.1 (path-resistance ceiling sharpening). DISC-0034 stays OPEN; a route to 0.70 needs a comparison closer to the live gasket resistance. Not thrust.

## Derivation

Direct computation of the floors and envelopes against 0.70; checked; no gap.

## Assumptions

As DISC-0096.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AL.log`, EXIT 0, 376 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AL.py` / `indep_theorem_AL.log`, ALL PASS, 442 PASS) reproduce σ_AK·0.111208≈0.078019 < 0.70, 2^(1−α)·0.111208≈0.162818 < 0.70, live-σ·0.111208≈0.150409 < 0.70; R_∞≫live gasket R; attack: reaching 0.70 via σ_AK would need R_∞≤≈1.48 (below live ~2.35).

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed envelopes independently; matches GASKET.md and the commit message. The rejection is analytic for the stated chain (not a computed-range caveat like AK.1's live-constant chain).

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. DISC-0096 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0096. Mathematical. Theorem AL.
- DISC-0095, DISC-0093, DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

Which comparison beyond path resistance / one-step Harnack could reach 0.70; not addressed by the repository.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0096.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AL.1 at 483de961575bca353a2cd3ff6719b8a357610a87; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
