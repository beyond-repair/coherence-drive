# Discovery: Kept Failure BB.1, removing the self pair force does not make the gasket mesh residual exactly zero

## Discovery ID

DISC-0133

## Status

REJECTED (repository's own Kept Failure BB.1). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~3:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Paths: README.md "Theorem BB" (BB.1–BB.5, DERIVED rate, Kept Failure BB.1, Conjecture BB.2, NOT THIS), CLAIM_STATUS.md Theorem BB row, GASKET.md Stage 2 OPEN item (appended sentence), README Conjecture BA.2 status line, scripts/mesh_maxwell_limit.py, tests/test_cli.py.

## Original Evidence

See Discovery and Derivation below; every figure is quoted from README Theorem BB at 3b98cd7aa7c1 or from the repository witness log.

## Discovery

Claim tested by the repository: with the self pair force φ_cc removed, the integrated divergence after the Maxwell piece is exactly 0 on the gasket, as the centred stencil gives on the torus (DISC-0130 / BA.5). False: certified κ^cross_{1..4}(0.45)=0.48882868502562873746…, 0.086933485121556483865…, 0.017575791192880243766…, 0.0039810486280556649983…, all >0; recursion values 1.2757e−6 (n=10), 3.0737e−12 (n=20); nonzero at every computed level, tending to 0. Second failure kept: BA's decreasing float modulus was not evidence of a zero limit, and its Aitken '≈−0.86' was 0.005 low (2^−nκ_n increases toward K from below).

## Why It Matters

Closes the obvious rescue of an exact discrete conservation law on the gasket under Assumption BA.

## Derivation

Interval certificates in scripts/mesh_maxwell_limit.py (BA pipeline, mpmath.iv); BB.5 bound for the decay.

## Assumptions

Assumption BA; the 'drop the self term' rule as the only gasket analogue of the centred stencil (repo DERIVED note).

## New Results

κ^cross_n>0 at levels 1–4 (certified) and →0 (BB.5).

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Archive floats reproduce κ^cross_1..4 to 1e−9 and give κ^cross_5=9.7378e−4, κ^cross_6=2.4911e−4 (>0).

## Experimental Validation

Repository certificates plus archive floats.

## Mathematical Status

Failed hypothesis (rejected claim), certified at levels 1–4.

## Patent Relevance

None. A discrete self-force renormalisation constant is not a device mechanism. Not thrust.

## Related Discoveries

- DISC-0132 → DISC-0133 (failed hypothesis).
- Sits beside DISC-0130 (failed hypothesis).

## Open Questions

Whether any other self-consistent discrete rule gives exact conservation on the gasket.

## Next Experiments

None required for the rejection.

## Reproduction Instructions

Repository: `cd informational-flux-identity && git checkout 3b98cd7 && python3 scripts/mesh_maxwell_limit.py` (about 4 min; archive run EXIT 0, log /workspace/scratch-ifi/repo_BB.log). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BB.py` (about 50 s; 64/64 PASS, log indep_theorem_BB.log; reuses the own gasket build of indep_theorem_BA.py).

## Evidence Log

- 2026-10-22 ~3:55pm EDT. Recorded from IFI 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d. Repository witness scripts/mesh_maxwell_limit.py EXIT 0 (231.5 s). Archive independent float check (own gasket build, own dense spectral calculus, not the repository code): BB.1 κ_n and κ^self_n formulas equal the direct pair-force sums to 1e−8 relative at α=0.45 levels 1–6 and α=0.25, 0.6 levels 1–4; 0<Y_n≤5^−nR_n/2 and 0<E_n≤ the BB.3 bound at every one of those 14 (α,n); cross constants at 0.45 match the certified κ^cross_1..4 to 1e−9; BB.2 tangential decimation y_n(s)=r_n(s)∏(5+p^j(s))^−1 and BB.3 e_n=s g_n, g_n≤(3/20)^n/s² hold on direct resolvent solves at n=1,2,3, s∈{0.5,3,1.4}. 64/64 PASS. Floats 2^−nκ_n=−2.0214,−1.6535,−1.3423,−1.1579,−1.0488,−0.9818 (n=1..6) increase toward K from below, consistent with the repo's recursion values −0.880867 (n=10), −0.855254 (n=20), −0.854647 (n=40). The archive did NOT independently certify K or reproduce the n=10–40 recursion; those rest on the repository witness (EXIT 0).

## Change History

- 2026-10-22. Initial archive entry.
