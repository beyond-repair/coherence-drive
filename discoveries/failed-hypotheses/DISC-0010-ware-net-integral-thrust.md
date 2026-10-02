# Discovery: Net non-zero surface integral / thrust from Ware injection

## Discovery ID

DISC-0010

## Status

REJECTED as a thrust claim.

## Date Discovered

2026-10-01. Archive pass for stress-tensor-modification at the named evidence commit.

## Source Repositories

beyond-repair/stress-tensor-modification at commit adab20380b2d2e35776aeed249d39229b8a06fdd. Authoritative files: CLAIM_STATUS.md; README.md; docs/PHOTON_CLASS_B_CEILING.md; docs/BEM_EPSILON_F_EXPLORATION.md; docs/MAXWELL_EPSILON_F_RUN.md; docs/COMPATIBLE_CLOSURE_SIM.md; docs/LOOP_STATUS.md.

## Original Evidence

CLAIM_STATUS.md at that evidence commit: Classification RESEARCH; Experimental validation false; Thrust validated false; Reactionless closed thrust false; Target fitting performed false; epsilon_F (Class B dual-surface residual) not reported. It states that GitHub description text that implies proven thrust is out of date and that this file is authoritative.

README.md: lifecycle RESEARCH, claim ≤1, "NOT CLAIMED thrust · energy extraction · AGI · production autonomy"; badge "not_thrust_demo"; workflow step 5 reports residuals / directionality / estimated pattern A — "NOT product F/P, NOT reactionless thrust."

docs/PHOTON_CLASS_B_CEILING.md: F/P ≤ |A|/c ≤ 1/c ≈ 3.3356e-9 N/W; published engineering target 3e-8 N/W ≈ 9/c; verdict that pure photon / free-space EM Class B cannot reach the target; Branch 2 extinguished for target match.

docs/BEM_EPSILON_F_EXPLORATION.md and docs/MAXWELL_EPSILON_F_RUN.md: dual-surface epsilon_F explored; not closed; scout residuals O(1) to O(10^5); "huge epsilon_F is error, not a reactionless discovery"; Class B construction F_d := -F_X gives epsilon_F=0 by definition (bookkeeping, not dual-surface proof).

docs/COMPATIBLE_CLOSURE_SIM.md: physics-compatible form F_device = -F_X only; scout |A|~0.002–0.003 → photon F/P ~ 1e-11 N/W ≪ target 3e-8; thrust_validated=false; reactionless_closed_thrust=false.

## Discovery

The claim that Ware-injected modified Maxwell stress produces a net non-zero surface integral responsible for Coherence Drive thrust is rejected by the repository's own claim flags and scout numerics. Compatible closure remains F_device = -F_X. Photon Class B cannot hit the 30 μN/kW-scale target.

## Why It Matters

This is the file-level fence inside the repository whose GitHub description still asserts the thrust equation. Indexing it stops description text from being treated as a validated result. It extends DISC-0002's thrust rejection into the stress-tensor stack with new epsilon_F and photon-ceiling evidence.

## Derivation

No thrust derivation is recorded. Scout pattern-A estimates and dual-surface residuals are diagnostics, not certified force.

## Assumptions

Rejection uses in-repo flags and the named docs. It does not assume that every conceivable residual after classical subtraction is impossible (that item remains unresolved on the narrative ledger).

## New Results

None. No claim level is raised.

## Prior Art

Classical EM momentum flux and radiation-pressure bounds (F/P ≤ 1/c for pure photon rockets) are the ceiling used in PHOTON_CLASS_B_CEILING.md. This archive does not add an external citation beyond what that file already uses.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. Relation to DISC-0002 is mathematical (thrust not from the corpus). Relation to DISC-0009 is historical (same evidence commit; Ware-from-K fence). Relation to DISC-0012 is mathematical (classical Maxwell surface integrals do not become reactionless thrust).

## Falsification Attempts

CLAIM_STATUS false flags; photon ceiling vs 3e-8; epsilon_F not closed under scout runs; README claim strip.

## Experimental Validation

None. All thrust-related flags false.

## Mathematical Status

Rejected.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. Broader thrust / Delta F rejection from flux and spectral endpoint.
- DISC-0009. Historical. Same repository; Ware force law not from K.
- DISC-0011. Mathematical. M2 0.08 pin is not a thrust derivation.
- DISC-0012. Mathematical. Classical Maxwell evaluator is not a thrust demo.

## Open Questions

Genuine residual force after classical subtraction remains unresolved on docs/SURVIVED_REJECTED_UNRESOLVED.md. Dual-surface Maxwell epsilon_F with production BEM remains open as engineering work, not as a thrust claim.

## Next Experiments

Do not flip thrust_validated without experiment and closed epsilon_F (LOOP_STATUS.md). Do not read pattern A or scout F/P as product thrust.

## Reproduction Instructions

Read CLAIM_STATUS.md, README.md, docs/PHOTON_CLASS_B_CEILING.md, docs/BEM_EPSILON_F_EXPLORATION.md, docs/MAXWELL_EPSILON_F_RUN.md, and docs/COMPATIBLE_CLOSURE_SIM.md at adab20380b2d2e35776aeed249d39229b8a06fdd. Compare to the GitHub description fetched the same day (provenance only).

## Evidence Log

- 2026-10-01. Read the files named above at adab20380b2d2e35776aeed249d39229b8a06fdd.
- Provenance. GitHub description (2026-10-01 ET): "Modified Maxwell stress tensor with Ware Constant injection — the exact equation that produces the net non-zero surface integral responsible for thrust in the Coherence Drive." CLAIM_STATUS calls that out of date. Description was not edited.

- 2026-10-02. Verification re-check: stress-tensor-modification origin/main had advanced to 09cd4862ea7ec4796b7ff96873e00c5295a92717 (pinch pointer). Cited fences at adab20380b2d2e35776aeed249d39229b8a06fdd still hold; SPECTRAL_ENDPOINT_POINTER.md text unchanged through 953097c. Evidence SHA remains adab203; not re-baselined to newer main.

## Change History

- 2026-10-02. Verification pass: confirmed claims at adab203; noted origin/main advance to 09cd486 without changing cited fences. Wording adjusted from HEAD to evidence commit.
- 2026-10-01. Initial archive entry. Descriptions were not edited. No Stage-1 freeze file was changed.
