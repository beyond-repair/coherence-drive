# Discovery: The neighbor-degree share climbs geometrically toward 1, λ_{n+1}/λ_n ≥ 1.01 for every n (Kept Failure AG.1)

## Discovery ID

DISC-0087

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0086.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e20e13fbe9528abb93e0c430bb810a341622356b. Paths: GASKET.md Theorem AG → Kept Failure AG.1, Observation, NOT THIS; CLAIM_STATUS.md ("Uniform ceiling on the neighbor-degree share λ_n" row: "Geometric climb λ_{n+1}/λ_n≥1.01 rejected"); scripts/gasket_fractional_lambda_ceiling.py.

## Original Evidence

GASKET.md Kept Failure AG.1: the law "λ_{n+1}/λ_n ≥ 1.01 for every n, hence λ_n → 1 and AF's converse obstruction materializes" is false. Every live ratio through level 6 is below 1, starting at 0.85506 from level 1 to level 2; λ_n decreases.

## Discovery

Rejected hypothesis: geometric climb of the neighbor-degree share λ_n toward 1 at α=0.45. False; λ_n decreases on levels 1–6.

## Why It Matters

λ_n → 1 was the one way the converse of DISC-0084 could fail. DISC-0086 already closes it by a uniform ceiling; this rejects the geometric version of the same escape. It does not prove a positive limit: γ_n could still drift to ∞ slowly. Not thrust.

## Derivation

Direct finite-level counterexample (the first ratio is already < 1); checked; no gap.

## Assumptions

As DISC-0086.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AG.log`, EXIT 0) and independent archive (`/workspace/scratch-ifi/indep_theorem_AG.py` / `indep_theorem_AG.log`, own builder, ALL PASS) both give λ ratios 0.855064, 0.963857, 0.993134, 0.998827, 0.999807 (levels 1→6), all below 1. Same series as DISC-0083 (AE.1 tested the opposite direction).

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed λ_n independently through level 6; no ratio ≥ 1.

## Experimental Validation

None.

## Mathematical Status

Rejection by explicit finite-level counterexample, reproduced independently; also subsumed by the DISC-0086 ceiling.

## Patent Relevance

None.

## Related Discoveries

- DISC-0086. Theorem AG (λ ceiling; two-sided split).
- DISC-0085. Kept Failure AF.1 (no geometric γ blowup).
- DISC-0083. Kept Failure AE.1 (no geometric λ wipeout).
- DISC-0034. Conjecture. α=0.45 combinatorial limit still OPEN.

## Open Questions

None for this rejection. DISC-0034 unaffected (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0086.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AG.1 at e20e13fbe9528abb93e0c430bb810a341622356b; repo witness EXIT 0; indep ALL PASS.

## Change History

- 2026-10-15. Initial archive entry.
