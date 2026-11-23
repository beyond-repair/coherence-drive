# Discovery: A level-uniform fractional energy floor at every α∈(0,1) (Kept Failure AC.1)

## Discovery ID

DISC-0079

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0078.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 51789b3ef3c56d6e678f9df35dd276a1c8657a87. Paths: GASKET.md Theorem AC → Kept Failure AC.1; CLAIM_STATUS.md ("No floor for α>γ (Kept Failure AC.1, from Theorem K); α=γ OPEN"); scripts/gasket_fractional_capacity_floor.py.

## Original Evidence

For α>γ=log3/log5, Theorem K gives Q_α(u_n) ≤ (7/2)^α 3^{1−α}(3·5^{−α})^n → 0. Live levels 1–6: Q_0.75 ≈ (1.822739, 1.304966, 0.975341, 0.756383, 0.603760, 0.492589), Q_0.90 ≈ (1.984971, 1.282422, 0.846205, 0.568710, 0.387631, 0.266891), strictly decreasing and under the bound.

## Discovery

Rejected hypothesis: "for every α∈(0,1) there is c(α)>0 with Q_α(u_n) ≥ c(α) at every level". False above γ, so neither Theorem AC's floor nor AB's equivalence-by-floor extends past γ.

## Why It Matters

Makes γ the exact threshold for a level-uniform energy floor (endpoint open). Not thrust.

## Derivation

Theorem K (DISC-0032, THEOREM) upper bound with geometric ratio 3·5^{−α}<1 for α>γ. Checked; no gap.

## Assumptions

As DISC-0078; Theorem K.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_AC.py`: Q_α(u_n) strictly decreasing and ≤ Theorem K bound for α∈{0.70,0.75,0.90}, n=1..7 (level 7: Q_0.70=0.504777, Q_0.75=0.408629, Q_0.90=0.185064); repo levels 1–6 values reproduced to 5e−7; R_α(n) grows geometrically above γ (α=0.90: 12.61 at level 7) and ≈linearly at α=γ.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Checked α=0.70 (just above γ, slow ratio 3·5^{−0.7}≈0.97): still under the K bound and decreasing.

## Experimental Validation

None.

## Mathematical Status

Rejection supported by a proved theorem (K). α=γ itself stays OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0078. Theorem AC.
- DISC-0032. Theorem K.
- DISC-0073. Energy collapse at 0.45 rejected (the opposite regime).

## Open Questions

Floor at α=γ.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0078.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AC.1 at 51789b3ef3c56d6e678f9df35dd276a1c8657a87; repo witness EXIT 0; indep PASS.

## Change History

- 2026-10-15. Initial archive entry.
