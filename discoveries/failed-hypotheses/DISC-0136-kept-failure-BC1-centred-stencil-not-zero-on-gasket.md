# Discovery: Kept Failure BC.1, a centred stencil does not restore Newton's third law on the frozen 0.45 gasket

## Discovery ID

DISC-0136

## Status

REJECTED (repository's own Kept Failure BC.1). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~5:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Paths: README.md "Theorem BC" (BC.1–BC.5, DERIVED torus-mechanism paragraph, Kept Failure BC.1, Conjecture BC.2, NOT THIS), CLAIM_STATUS.md Theorem BC row, GASKET.md Stage 2 OPEN item (appended sentences), README OPEN paragraph (appended sentences), scripts/mesh_centred_stencil.py, scripts/cli.py, tests/test_cli.py.

## Original Evidence

Every figure below is quoted from README Theorem BC at c7a0cf681bf5 or from the archive check log; archive-only numbers are labelled.

## Discovery

Claim tested by the repository: the centred stencil that gives D=0 on the translation-invariant torus (DISC-0130 / BA.5) gives D=0 on the frozen 0.45 gasket after the Maxwell piece is removed. False. The only form of that stencil existing on the gasket (Green–Gauss) coincides with the one-sided rule at every charged vertex, so certified κ^GG_1..4(0.45)=κ_1..4≠0 (κ^GG_4=−18.526339511158477727…); the cross pair force is certified non-central (tanθ_1..4<0) and the self coefficient s>0. The torus cancellation used a half-turn symmetry the gasket does not have.

## Why It Matters

Closes the centred-stencil rescue of an exact discrete conservation law under this reading. The repository explicitly declines to tune a stencil to s=−2√3h_⊥ or s=h_⊥=0 (a fit to the desired answer) and declines the bow-tie mesh doubling (it changes the frozen mesh).

## Derivation

Follows from BC.2–BC.4 (DISC-0135).

## Assumptions

Assumption BC.

## New Results

None beyond DISC-0135.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection).

## Falsification Attempts

Archive tried to break the rejection: κ via BC.1 equals the direct value and is nonzero at n=1..6; s>0, tanθ<0 at n=1..6. The rejection stands.

## Experimental Validation

See Evidence Log.

## Mathematical Status

Counterexample (certified at levels 1–4).

## Patent Relevance

None. Not thrust.

## Related Discoveries

- DISC-0135 → DISC-0136 (failed hypothesis).
- DISC-0130, DISC-0133 (earlier rejections in the same chain).

## Open Questions

None for this claim.

## Next Experiments

None required.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout c7a0cf6 && python3 scripts/mesh_centred_stencil.py` (repo says about 1.5 min; log /workspace/scratch-ifi/repo_BC_run.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BC.py` (about 80 s; 28/28 PASS, log indep_theorem_BC.log; reuses the own gasket build of indep_theorem_BA.py / indep_theorem_BB.py, not repository code).

## Evidence Log

- 2026-10-22 ~5:05pm EDT. Recorded from IFI c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Archive independent float check (own gasket build and dense spectral calculus): the BC.1 formula κ_n=−(4/R_n²)(s+2√3h_⊥) with BC.4's s=2^n(σ_n−E_n), h_⊥=(√3/6)2^n(E_n−3Y_n) equals the direct pair-force κ_n to 1e−8 at α=0.45, n=1..6; s>0 and tanθ_n<0 at n=1..6; tanθ_1..4 and s_1..4 match the certified values to 1e−9 / 1e−8; archive floats tanθ_5=−0.1963417480579, tanθ_6=−0.1937567642745 (moving toward −1/(3√3)=−0.19245009); no vertex has an odd stencil and every vertex's neighbour offsets lie in a closed half-plane at n=1..5 (N=6..366); BC.5 small-s ratio e_n/y_n at s=1e−5 matches 2·3^n/(3^n+1) to 1e−5 at n=1..4; E_n/Y_n increases toward 2 from below at α=0.25, 0.6, 0.8 (n=4..6), with (2−E/Y)3^n=4.443, 3.194, 2.565 at n=6, consistent with the repo's n=16 values 4.4720, 3.2076, 2.5724. 28/28 PASS. Not independently certified in intervals; the level 1–4 certification and the sympy identities rest on the repository witness. Repository witness scripts/mesh_centred_stencil.py EXIT 0 (121.3 s, "all Theorem BC checks passed").

## Change History

- 2026-10-22. Initial archive entry.
