# Discovery: The gap ratio γ_n blows up geometrically, γ_{n+1}/γ_n ≥ 1.05 for every n (Kept Failure AF.1)

## Discovery ID

DISC-0085

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0084.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit f5f89d9c359498d6be6c952b51a96af7914ad831. Paths: GASKET.md Theorem AF → Kept Failure AF.1, Observation, NOT THIS; CLAIM_STATUS.md ("Uniform floor on the neighbor-degree share λ_n" row: "Geometric blowup γ_{n+1}/γ_n≥1.05 rejected"); scripts/gasket_fractional_lambda_floor.py.

## Original Evidence

GASKET.md Kept Failure AF.1: the law "γ_{n+1}/γ_n ≥ 1.05 for every n, hence γ_n→∞ geometrically, and therefore ‖F(n,0.45)‖→0 by Theorems AF and AE" is false. Every live ratio through level 6 is below 1, starting at 0.96302 from level 1 to level 2.

## Discovery

Rejected hypothesis: geometric blowup of the far-to-neighbor gap ratio γ_n at α=0.45. False; γ_n decreases on levels 1–6.

## Why It Matters

After DISC-0084 made γ_n→∞ necessary for ‖F(n,0.45)‖→0, this rejects the geometric version of that last route. It does not prove a positive limit: γ_n could still turn and drift to ∞ slowly beyond the computed range. Not thrust.

## Derivation

Direct finite-level counterexample (the first ratio is already < 1.05); checked; no gap.

## Assumptions

As DISC-0084.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AF.log`, EXIT 0) and independent archive (`/workspace/scratch-ifi/indep_theorem_AF.py` / `indep_theorem_AF.log`, own builder, ALL PASS) both give γ ratios 0.963017, 0.991123, 0.998105, 0.999620, 0.999928 (levels 1→6), all below 1 and rising toward 1.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed γ_n independently through level 6; no ratio ≥ 1.

## Experimental Validation

None.

## Mathematical Status

Rejection by explicit finite-level counterexample, reproduced independently.

## Patent Relevance

None.

## Related Discoveries

- DISC-0084. Theorem AF (λ floor; γ_n→∞ necessary).
- DISC-0083. Kept Failure AE.1 (no geometric λ wipeout).
- DISC-0077. Kept Failure AB.1 (no geometric ρ collapse).
- DISC-0034. Conjecture. α=0.45 combinatorial limit still OPEN.

## Open Questions

None for this rejection. DISC-0034 unaffected (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0084.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AF.1 at f5f89d9c359498d6be6c952b51a96af7914ad831; repo witness EXIT 0; indep ALL PASS.

## Change History

- 2026-10-15. Initial archive entry.
