# Discovery: Theorem J's 3/2 gap cap alone floors the audit norm (Kept Failure AH.1)

## Discovery ID

DISC-0089

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0088.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 167ef7c0c8f0ba365751cab033da77a3b48def96. Paths: GASKET.md Theorem AH → Kept Failure AH.1, Observation, NOT THIS; CLAIM_STATUS.md ("Uniform ceiling on the far-to-neighbor gap ratio γ_n; positive audit floor" row: max-principle shortcut rejected); scripts/gasket_fractional_gamma_ceiling.py.

## Original Evidence

GASKET.md Kept Failure AH.1: the shortcut "every far gap satisfies u_a−u_j≤3/2 (maximum principle, Theorem J), so I_far≤(3/2)W_far and I_a=(I_a^α−I_far)/w_n≥(I_a^α−(3/2)W_far)/w_n>0 at every level" is false. Live at α=0.45, I_a^α<(3/2)W_far at levels 3 through 6, and the shortcut bound is (1.171102, 0.277444, −0.141539, −0.347367, −0.464237, −0.536750), negative from level 3.

## Discovery

Rejected hypothesis: a pure max-principle gap cap floors the combinatorial audit without the kernel comparison of Theorem AH. False from level 3 at α=0.45.

## Why It Matters

Shows why AH's heat-kernel Harnack at the neighbors is essential: a sup-norm bound on far gaps cannot see that L^α-harmonicity ties far gaps to neighbor gaps. Does not weaken DISC-0088. Not thrust.

## Derivation

Direct finite-level counterexample; checked; no gap.

## Assumptions

As DISC-0088.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AH.log`, EXIT 0) and independent archive (`/workspace/scratch-ifi/indep_theorem_AH.py` / `indep_theorem_AH.log`, own builder, ALL PASS) both give the shortcut sequence above and confirm negativity at levels 3–6.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed (I_a^α−(3/2)W_far)/w_n independently through level 6; matches GASKET to 6 digits; negative from level 3.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient condition for a positive floor. DISC-0088 still supplies the floor by a different argument.

## Patent Relevance

None.

## Related Discoveries

- DISC-0088. Mathematical. Theorem AH (the working floor).
- DISC-0033. Failed hypothesis. Other rejected shortcuts toward the α=0.45 limit.
- DISC-0034. Conjecture. Convergence still OPEN; vanishing closed by DISC-0088.

## Open Questions

None specific to this rejection.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0088.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AH.1 at 167ef7c0c8f0ba365751cab033da77a3b48def96; repo and independent witnesses agree.

## Change History

- 2026-10-15. Initial archive entry.
