# Discovery: Theorem AC's level-uniform energy floor extends to the endpoint α = log3/log5 (Kept Failure AD.1)

## Discovery ID

DISC-0081

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0080.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit b8b48ad72bf62d57da7a69bc5b2b9b63a2e51c5f. Paths: GASKET.md Theorem AD → Kept Failure AD.1; CLAIM_STATUS.md ("Endpoint α=log3/log5 and exact pairing" row; AC row "α=γ settled by Theorem AD"); scripts/gasket_fractional_endpoint.py.

## Original Evidence

By Theorem AD, Q_γ(u_n) ≤ (7/3)/(c_AD n) ≈ 45.19/n → 0. Theorem K cannot decide the endpoint: its majorant at γ is the constant (7/2)^γ 3^{1−γ} ≈ 3.332879 because 3·5^{−γ}=1, and the harmonic comparison energy Q_γ(u_H) ≈ (1.7601, 1.3691, 1.1702, 1.0768, 1.0358, 1.0185, 1.0115) levels off near 1. The AC floor (9/4)/C_AC(α) → 0 as α→γ (0.000109 at 0.68).

## Discovery

Rejected hypothesis: "there is c>0 with Q_γ(u_n) ≥ c at every level" (AC's floor reaching α=γ). False; the endpoint belongs to the collapsing side.

## Why It Matters

Makes the threshold statement complete: floor exactly for α<γ, collapse for α≥γ. Not thrust.

## Derivation

Direct consequence of Theorem AD (DISC-0080, THEOREM); K-majorant computation elementary. Checked; no gap.

## Assumptions

As DISC-0080.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_AD.py`: Theorem K majorant 3.332879 and 3·5^{−γ}=1 reproduced; Q_γ(u_H) levels 1–7 reproduced to 5e−5 (plateau ≈1.0115 at level 7, above the minimizer energy 0.539695); via the exact pairing and the sparse route, Q_γ(u_n) = (7/3)/R_γ(n) = 0.397181 at n=10 (≤ 45.19/n at every n=1..10), less than a quarter of level 1 and still falling.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Looked for a floor numerically through level 10 (N=88,575): none; n·Q_γ grows toward ≈4.51 instead of n·Q_γ→∞, consistent with Θ(1/n) and not with a floor.

## Experimental Validation

None.

## Mathematical Status

Rejection supported by a proved theorem (AD).

## Patent Relevance

None.

## Related Discoveries

- DISC-0080. Theorem AD.
- DISC-0078. Theorem AC (floor for α<γ).
- DISC-0079. Kept Failure AC.1 (no floor above γ).
- DISC-0032. Theorem K (constant majorant at γ).

## Open Questions

None for this rejection. DISC-0034 (α=0.45) unaffected.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0080.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AD.1 at b8b48ad72bf62d57da7a69bc5b2b9b63a2e51c5f; repo witness EXIT 0; indep PASS.

## Change History

- 2026-10-15. Initial archive entry.
