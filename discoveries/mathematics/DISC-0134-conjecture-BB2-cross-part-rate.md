# Discovery: Conjecture BB.2, κ^cross_n(α) ∼ c(2·5^{α−1}/3)^n

## Discovery ID

DISC-0134

## Status

CONJECTURE (repository's own). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~3:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Paths: README.md "Theorem BB" (BB.1–BB.5, DERIVED rate, Kept Failure BB.1, Conjecture BB.2, NOT THIS), CLAIM_STATUS.md Theorem BB row, GASKET.md Stage 2 OPEN item (appended sentence), README Conjecture BA.2 status line, scripts/mesh_maxwell_limit.py, tests/test_cli.py.

## Original Evidence

See Discovery and Derivation below; every figure is quoted from README Theorem BB at 3b98cd7aa7c1 or from the repository witness log.

## Discovery

The cross (non-self) part of the mesh residual decays like (2·5^{α−1}/3)^n, sharper than the proved BB.3/BB.5 rate O((2(3/20)^{1−α})^n).

## Why It Matters

Would give the exact decay rate of the only non-self residual under Assumption BA.

## Derivation

None (numerical). Repo: on n=10–20 the per-level ratio is 0.2743 vs 2·5^−0.55/3=0.2750; Y_n and E_n each decay like (5^{α−1}/3)^n in floats.

## Assumptions

Assumption BA.

## New Results

Archive per-level ratios at 0.45: κ^cross_2/κ^cross_1=0.178, _3/_2=0.202, _4/_3=0.2265, _5/_4=0.2446, _6/_5=0.2558, rising toward 0.2750; consistent, not proof.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Only the archive ratio trend above; no counterexample at n≤6.

## Experimental Validation

None beyond floats.

## Mathematical Status

Conjecture.

## Patent Relevance

None. A discrete self-force renormalisation constant is not a device mechanism. Not thrust.

## Related Discoveries

- DISC-0132 → DISC-0134 (mathematical).

## Open Questions

A proof via a sharper F_n ceiling in BB.3.

## Next Experiments

Fit ratios from the repo recursion at n=20–40.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout 3b98cd7 && python3 scripts/mesh_maxwell_limit.py` (about 4 min; archive run EXIT 0, log /workspace/scratch-ifi/repo_BB.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BB.py` (about 50 s; 64/64 PASS, log indep_theorem_BB.log; reuses the own gasket build of indep_theorem_BA.py).

## Evidence Log

- 2026-10-22 ~3:55pm EDT. Recorded from IFI 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Repository witness scripts/mesh_maxwell_limit.py EXIT 0 (231.5 s). Archive independent float check (own gasket build, own dense spectral calculus, not the repository code): BB.1 κ_n and κ^self_n formulas equal the direct pair-force sums to 1e−8 relative at α=0.45 levels 1–6 and α=0.25, 0.6 levels 1–4; 0<Y_n≤5^−nR_n/2 and 0<E_n≤ the BB.3 bound at every one of those 14 (α,n); cross constants at 0.45 match the certified κ^cross_1..4 to 1e−9; BB.2 tangential decimation y_n(s)=r_n(s)∏(5+p^j(s))^−1 and BB.3 e_n=s g_n, g_n≤(3/20)^n/s² hold on direct resolvent solves at n=1,2,3, s∈{0.5,3,1.4}. 64/64 PASS. Floats 2^−nκ_n=−2.0214,−1.6535,−1.3423,−1.1579,−1.0488,−0.9818 (n=1..6) increase toward K from below, consistent with the repo's recursion values −0.880867 (n=10), −0.855254 (n=20), −0.854647 (n=40). The archive did NOT independently certify K or reproduce the n=10–40 recursion; those rest on the repository witness (EXIT 0).

## Change History

- 2026-10-22. Initial archive entry.
