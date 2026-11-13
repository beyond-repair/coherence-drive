# Discovery: The neighbor-degree share λ_n wipes out geometrically, λ_{n+1}/λ_n ≤ 0.95 for every n (Kept Failure AE.1)

## Discovery ID

DISC-0083

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0082.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d793add3f4be3ed73d19678b995e38d55b2481a8. Paths: GASKET.md Theorem AE → Kept Failure AE.1 and NOT THIS; CLAIM_STATUS.md ("Degree-gap factorization of ρ_n and sharp weight ceiling" row: "Geometric wipeout λ_{n+1}/λ_n≤0.95 rejected"); scripts/gasket_fractional_degree_share.py.

## Original Evidence

GASKET.md Kept Failure AE.1: the law "λ_{n+1}/λ_n ≤ 0.95 for every n, hence λ_n → 0 geometrically, and therefore (with any uniform positive lower bound on γ_n) ρ_n → 0 and ‖F(n,0.45)‖ → 0 by Theorems AB and AA" is false. The ratio from level 3 to level 4 is already 0.99314, and from level 4 to level 5 it is 0.99883.

## Discovery

Rejected hypothesis: uniform geometric wipeout of the neighbor-degree share λ_n at α=0.45. False; λ_n levels off near 0.529 on levels 1–6.

## Why It Matters

Closes the λ-side geometric route to ‖F(n,0.45)‖ → 0 after DISC-0077 (Kept Failure AB.1) closed geometric collapse of ρ_n itself. It does not prove a positive limit and does not bound γ_n. Not thrust.

## Derivation

Direct finite-level counterexample (one ratio > 0.95 suffices); checked; no gap.

## Assumptions

As DISC-0082.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AE.log`, EXIT 0): lambda_ratios 0.85506394, 0.96385657, 0.99313410, 0.99882714, 0.99980692; "PASS Kept Failure AE.1: lambda ratio level 3→4 = 0.99313410 > 0.99". Independent archive (`/workspace/scratch-ifi/indep_theorem_AE.py` / `indep_theorem_AE.log`, own builder) reproduces the same five ratios to 8 digits, ALL PASS. Already at level 2→3 the ratio 0.96386 exceeds 0.95.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed λ_n independently through level 6; ratios increase monotonically toward 1 (0.9998 at 5→6). No sign of renewed decay.

## Experimental Validation

None.

## Mathematical Status

Rejection by explicit finite-level counterexample, reproduced independently.

## Patent Relevance

None.

## Related Discoveries

- DISC-0082. Theorem AE (degree–gap factorization).
- DISC-0077. Kept Failure AB.1 (no geometric ρ collapse).
- DISC-0073. Kept Failure AA.1 (no energy collapse).
- DISC-0034. Conjecture. α=0.45 combinatorial limit still OPEN.

## Open Questions

None for this rejection. DISC-0034 unaffected (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0082.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AE.1 at d793add3f4be3ed73d19678b995e38d55b2481a8; repo witness EXIT 0; indep ALL PASS.

## Change History

- 2026-10-15. Initial archive entry.
