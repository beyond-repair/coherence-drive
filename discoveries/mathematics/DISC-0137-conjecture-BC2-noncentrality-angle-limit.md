# Discovery: Conjecture BC.2, E_n/Y_n → 2 for every α, so the gasket non-centrality angle tends to −1/(3√3) independently of α

## Discovery ID

DISC-0137

## Status

THEOREM for every α∈(0,1) (proved by IFI Theorem BD at 30bee3a, DISC-0138: 2/(3^n+1)<2−E_n/Y_n≤2/(3^n+1)+B_α3^−n). Originally CONJECTURE (repository's own Conjecture BC.2; floats only); history below. The float (2−E/Y)3^n→3.7255634 at 0.45 lies inside the certified c(0.45)∈[3.72198897,3.72914181]. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~5:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Paths: README.md "Theorem BC" (BC.1–BC.5, DERIVED torus-mechanism paragraph, Kept Failure BC.1, Conjecture BC.2, NOT THIS), CLAIM_STATUS.md Theorem BC row, GASKET.md Stage 2 OPEN item (appended sentences), README OPEN paragraph (appended sentences), scripts/mesh_centred_stencil.py, scripts/cli.py, tests/test_cli.py.

## Original Evidence

Every figure below is quoted from README Theorem BC at c7a0cf681bf5 or from the archive check log; archive-only numbers are labelled.

## Discovery

For every α∈(0,1), E_n/Y_n→2 from below with 2−E_n/Y_n∼c(α)3^−n; hence tanθ_n→−1/(3√3)=−0.19245008973… (angle 10.893395°), independent of α. Repository floats: at 0.45, E_n/Y_n=1.99993691129 (n=10), 1.99999999893 (n=20), 1.99999999999998 (n=30), (2−E/Y)3^n→3.7255634; at α=0.25, 0.6, 0.8 and n=16, (2−E/Y)3^n≈4.4720, 3.2076, 2.5724. Numerically e_n/y_n≤2·3^n/(3^n+1) for every s (n≤11); the factorwise bound that would prove it fails.

## Why It Matters

The limit 2 would make the non-central direction a universal constant of the gasket geometry, and E_n<3Y_n for all n would extend DISC-0133's κ^cross_n>0 to every level. Note the s→0 value 2·3^n/(3^n+1) (BC.5) also tends to 2, which is suggestive but not a proof, since E_n integrates e_n(s) against the Balakrishnan weight.

## Derivation

None (conjecture). Heuristic: the Balakrishnan integral is dominated at large n by s∼5^−n where the ratio is near its s→0 value.

## Assumptions

Assumption BC; BB recursions.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive attempted to break α-independence at levels 4–6 with an independent dense build: E/Y is increasing and below 2 at α=0.25, 0.45, 0.6, 0.8; at n=6 (2−E/Y)3^n=4.443 (0.25), 3.194 (0.6), 2.565 (0.8), still rising toward the repo's n=16 values. At 0.45, archive E_5/Y_5=1.984910048542, E_6/Y_6=1.994916368981. No counterexample found; levels ≤6 cannot test the limit.

## Experimental Validation

Floats only (repository and archive).

## Mathematical Status

Conjecture.

## Patent Relevance

None. Not thrust.

## Related Discoveries

- DISC-0135 → DISC-0137 (mathematical).
- DISC-0133 → DISC-0137 (mathematical). Would extend κ^cross>0 to all levels.
- DISC-0134 (Conjecture BB.2, cross-part rate) is a sibling asymptotic conjecture on the same E_n, Y_n.

## Open Questions

Prove the bound e_n/y_n≤2·3^n/(3^n+1) for all s; identify c(α).

## Next Experiments

Independent recursion to n=30 at several α; interval enclosure of E_n/Y_n at n=10.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout c7a0cf6 && python3 scripts/mesh_centred_stencil.py` (repo says about 1.5 min; log /workspace/scratch-ifi/repo_BC_run.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BC.py` (about 80 s; 28/28 PASS, log indep_theorem_BC.log; reuses the own gasket build of indep_theorem_BA.py / indep_theorem_BB.py, not repository code).

## Evidence Log

- 2026-10-22 ~5:05pm EDT. Recorded from IFI c7a0cf681bf54979d31ff5c28c8ef9b0dad530b9. Archive independent float check (own gasket build and dense spectral calculus): the BC.1 formula κ_n=−(4/R_n²)(s+2√3h_⊥) with BC.4's s=2^n(σ_n−E_n), h_⊥=(√3/6)2^n(E_n−3Y_n) equals the direct pair-force κ_n to 1e−8 at α=0.45, n=1..6; s>0 and tanθ_n<0 at n=1..6; tanθ_1..4 and s_1..4 match the certified values to 1e−9 / 1e−8; archive floats tanθ_5=−0.1963417480579, tanθ_6=−0.1937567642745 (moving toward −1/(3√3)=−0.19245009); no vertex has an odd stencil and every vertex's neighbour offsets lie in a closed half-plane at n=1..5 (N=6..366); BC.5 small-s ratio e_n/y_n at s=1e−5 matches 2·3^n/(3^n+1) to 1e−5 at n=1..4; E_n/Y_n increases toward 2 from below at α=0.25, 0.6, 0.8 (n=4..6), with (2−E/Y)3^n=4.443, 3.194, 2.565 at n=6, consistent with the repo's n=16 values 4.4720, 3.2076, 2.5724. 28/28 PASS. Not independently certified in intervals; the level 1–4 certification and the sympy identities rest on the repository witness. Repository witness scripts/mesh_centred_stencil.py EXIT 0 (121.3 s, "all Theorem BC checks passed").

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22 ~6:05pm EDT. Status CONJECTURE → THEOREM after IFI 30bee3aab038 (Theorem BD, DISC-0138); the open bound e_n/y_n≤2·3^n/(3^n+1) for all s is also proved there (BD.2). Archive /workspace/scratch-ifi/indep_theorem_BD.py 45/45 PASS. Earlier text preserved (Mathematical Status section below reflects the original entry).
