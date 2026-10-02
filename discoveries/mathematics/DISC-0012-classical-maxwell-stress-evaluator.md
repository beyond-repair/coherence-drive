# Discovery: Classical Maxwell stress surface evaluator

## Discovery ID

DISC-0012

## Status

KNOWN

## Date Discovered

2026-10-01. Archive pass that indexed the classical evaluator already marked Survived in coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md.

## Source Repositories

beyond-repair/stress-tensor-modification at commit adab20380b2d2e35776aeed249d39229b8a06fdd. Files: physics_evaluator.py (maxwell_stress_tensor, surface_force, null and uniform-E closed-surface self-tests); closure.py (uniform_E_two_surface; "No Ware term is introduced here"); README.md Maxwell stress section.

## Original Evidence

README.md states the SI Maxwell stress

    T_ij = ε_0 (E_i E_j - (1/2) δ_ij E^2) + μ_0^{-1} (B_i B_j - (1/2) δ_ij B^2)

and that physics_evaluator.py integrates F_i = ∫ T_ij n_j dA and passes null / closed-surface checks.

physics_evaluator.py implements that tensor, surface traction sum, and _self_test: zero fields → F_total = 0; uniform E on the unit sphere → F_em ≈ 0; W_star = 1/(4π) lock for model "star".

closure.py builds a dual-sphere uniform-E diagnostic with MaxwellStressTensorEvaluator(model="star") and states no Ware term is introduced there.

docs/SURVIVED_REJECTED_UNRESOLVED.md Survived list already includes "Maxwell stress infrastructure (classical evaluator + sphere nulls)".

## Discovery

The classical Maxwell stress surface integral and the sphere null / uniform-E checks are ordinary EM, already implemented and already marked Survived. This row indexes that fact so it is not confused with the rejected Ware force-law and thrust readings in the same repository.

## Why It Matters

Separating KNOWN classical infrastructure from REJECTED Ware-from-K and thrust claims keeps Stage-1 claim levels from drifting when the same Python module also exposes optional informational_stress hooks.

## Derivation

No new derivation. The tensor is the standard Maxwell stress tensor in SI units as written in the README.

## Assumptions

Linear isotropic vacuum Maxwell stress; closed surface for the uniform-E null. No continuum Ware Delta T_W is assumed.

## New Results

None beyond what that evidence commit and the Survived list already state.

## Prior Art

Classical continuum electromagnetism (Maxwell stress tensor). This archive does not add an external citation.

## Novelty Analysis

There is no novelty claim. Status is KNOWN. Relation to DISC-0009 / DISC-0010 is historical: same repository; classical path versus rejected Ware thrust reading.

## Falsification Attempts

Self-tests in physics_evaluator.py; dual-sphere uniform-E path in closure.py. Optional M2 / informational hooks are out of scope for this KNOWN row (see DISC-0009, DISC-0011).

## Experimental Validation

None required for the classical identity. Laboratory thrust remains false (CLAIM_STATUS.md).

## Mathematical Status

Known classical EM.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0009. Historical. Ware-modified force law is not a consequence of K.
- DISC-0010. Mathematical. Classical surface integrals do not certify reactionless thrust.
- DISC-0011. Historical. Same evaluator module; M2 pin is not a theorem.

## Open Questions

Dual-surface epsilon_F with production BEM remains open as engineering work (docs in this repo). Far-field accounting remains unresolved on the narrative ledger.

## Next Experiments

Use model "star" classical path for null checks. Do not promote informational_stress results as spectral theorems.

## Reproduction Instructions

Run `python physics_evaluator.py` at adab20380b2d2e35776aeed249d39229b8a06fdd (null and uniform-E tests). Read the Maxwell section of README.md and the Survived Maxwell row in coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md.

## Evidence Log

- 2026-10-01. Read physics_evaluator.py, closure.py, README.md at adab20380b2d2e35776aeed249d39229b8a06fdd.
- 2026-10-01. Confirmed Survived Maxwell stress infrastructure row in docs/SURVIVED_REJECTED_UNRESOLVED.md.

- 2026-10-02. Verification re-check: stress-tensor-modification origin/main had advanced to 09cd4862ea7ec4796b7ff96873e00c5295a92717 (pinch pointer). Cited fences at adab20380b2d2e35776aeed249d39229b8a06fdd still hold; SPECTRAL_ENDPOINT_POINTER.md text unchanged through 953097c. Evidence SHA remains adab203; not re-baselined to newer main.

## Change History

- 2026-10-02. Verification pass: confirmed claims at adab203; noted origin/main advance to 09cd486 without changing cited fences. Wording adjusted from HEAD to evidence commit.
- 2026-10-01. Initial archive entry. No Stage-1 freeze file was changed.
