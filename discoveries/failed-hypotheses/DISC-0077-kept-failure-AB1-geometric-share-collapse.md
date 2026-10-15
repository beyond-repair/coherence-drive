# Discovery: Geometric collapse of the two-neighbor share ρ_n (Kept Failure AB.1)

## Discovery ID

DISC-0077

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0076.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 46915585f71b8d3292fa26d32405d8ff112d3d3a. Paths: GASKET.md Theorem AB → Kept Failure AB.1; CLAIM_STATUS.md (geometric collapse ρ_{n+1}/ρ_n ≤ 0.95 rejected); scripts/gasket_fractional_share.py.

## Original Evidence

The law "ρ_{n+1}/ρ_n ≤ 0.95 for every n, hence ρ_n→0 geometrically and ‖F(n,0.45)‖→0 by Theorem AB plus Theorem AA" is false: ratios (0.842140, 0.962182, 0.993003, 0.998838, 0.999814) for levels 1→6.

## Discovery

Rejected hypothesis: uniform geometric decay of the two-neighbor fractional share at α=0.45.

## Why It Matters

Closes this particular route to zero after energy collapse (DISC-0073). Does not prove a positive limit; DISC-0034 stays OPEN. Not thrust.

## Derivation

Direct computation; one counterexample ratio suffices. Checked; no gap.

## Assumptions

As DISC-0076.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_AB.py` (own builder) reproduces the ratios to 1e−8 and adds level 7: ρ_7/ρ_6≈0.99997055. σ_n>1.35 for n≥3 also reproduced (observation, not a limit theorem).

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Tried to find any level where the ratio drops below 0.95 after level 2; none through level 7.

## Experimental Validation

None.

## Mathematical Status

Rejection of one route only; combinatorial α=0.45 zero-versus-positive stays OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0076. Theorem AB.
- DISC-0073. Energy collapse rejected (previous route).
- DISC-0033. Earlier kept failures for closing the α=0.45 limit.
- DISC-0034. Conjecture. Still OPEN.

## Open Questions

As DISC-0076.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0076.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AB.1 at 46915585f71b8d3292fa26d32405d8ff112d3d3a; repo witness EXIT 0; indep PASS.

## Change History

- 2026-10-15. Initial archive entry.
