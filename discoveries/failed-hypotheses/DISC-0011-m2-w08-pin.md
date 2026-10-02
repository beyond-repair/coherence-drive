# Discovery: M2 W(n)=0.08 pin as theorem from K

## Discovery ID

DISC-0011

## Status

REJECTED as a theorem or as a consequence of locked K.

## Date Discovered

2026-10-01. Archive pass for stress-tensor-modification at the named evidence commit.

## Source Repositories

- beyond-repair/stress-tensor-modification at commit adab20380b2d2e35776aeed249d39229b8a06fdd, file physics_evaluator.py (W_M2_PIN, model M2).
- beyond-repair/coherence-drive docs/SPECTRAL_ENDPOINT.md at 095d29d1a107d719f8aed9f89834d917b119ca4c: W = 0.08 and xi = 0.23 are not consequences of K.
- beyond-repair/coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md Rejected rows: "Historical W(n)=0.08 e^{0.23(n-1)} indexing for residual-force work"; "Action-derived numerical values 0.08 and 0.23 from the constant-W Gaussian".

## Original Evidence

physics_evaluator.py at adab20380b2d2e35776aeed249d39229b8a06fdd defines:

    W_STAR = 1.0 / (4.0 * np.pi)  # Option A galactic / Maxwell anchor
    W_M2_PIN = 0.08  # engineering recursion pin at n=3

For model == "M2", W(n) = W_base * exp(0.23 * (n - 3)) with default W_base = W_M2_PIN. The constructor emits RuntimeWarning: "M2 model selected: uses frozen W(n)=W_base*exp(0.23*(n-3)). W<0.125 is a model-internal bound, not a no-ghost theorem."

Default model for self-tests is "star" (W_STAR). M2 is optional and warned.

docs/SPECTRAL_ENDPOINT.md denies that W = 0.08 and xi = 0.23 follow from locked K. The narrative Rejected list already rejects the historical W(n)=0.08 e^{0.23(n-1)} indexing and action-derived 0.08 / 0.23.

physics_evaluator_snippet.py at the same evidence commit is deprecated and raises ImportError; its comment mentions W_star = 1/(4π) ≈ 0.08 as phenomenology ledger, Option A — numerical proximity, not a derivation of the engineering pin from K.

## Discovery

Treating the M2 pin W(n)=0.08 * exp(0.23*(n-3)) as a theorem, a no-ghost theorem, or a consequence of locked K is rejected. The implementing file itself warns that the bound is model-internal. The spectral endpoint and the narrative Rejected list already deny derivation of 0.08 and 0.23 from K / the constant-W Gaussian.

## Why It Matters

Code that still ships the historical pin can be misread as selecting 0.08 from spectral mathematics. The warning and the endpoint fence block that reading without deleting the engineering hook.

## Derivation

No derivation from K is recorded. W_STAR = 1/(4π) is an Option A anchor in code; W_M2_PIN = 0.08 is labeled an engineering recursion pin.

## Assumptions

Rejection uses the RuntimeWarning text, SPECTRAL_ENDPOINT.md, and the narrative Rejected rows. It does not forbid keeping 0.08 as a design-goal index for residual-force experiments already marked historical/rejected as physics.

## New Results

None. No claim level is raised.

## Prior Art

The narrative Rejected list and SPECTRAL_ENDPOINT.md already record the same refusal. This entry indexes the concrete code constants at the stress-tensor evidence commit.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. Relation to DISC-0002 and DISC-0009 is mathematical (0.08 / Delta F / thrust not from K). Relation to DISC-0003 and DISC-0007 is mathematical (W < 1/6 does not select 0.08).

## Falsification Attempts

In-code RuntimeWarning; SPECTRAL_ENDPOINT not-consequences list; SURVIVED_REJECTED_UNRESOLVED Rejected rows for historical W(n) indexing and action-derived 0.08/0.23.

## Experimental Validation

None.

## Mathematical Status

Rejected as theorem / spectral consequence. Engineering pin may remain as non-physics indexing.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. W = 0.08 not from K.
- DISC-0003 / DISC-0007. Mathematical. Finite-gasket window does not select 0.08.
- DISC-0009. Mathematical. Ware stress force law not from K.
- DISC-0010. Mathematical. Thrust claim using Ware injection rejected.

## Open Questions

None opened by this row beyond what the narrative Rejected list already closed for 0.08/0.23 as physics.

## Next Experiments

Do not cite W_M2_PIN or the M2 exponential as a spectral theorem. Prefer model "star" / W_STAR when exercising the classical Maxwell path (DISC-0012).

## Reproduction Instructions

Read W_M2_PIN, W(), and the M2 RuntimeWarning in physics_evaluator.py at adab20380b2d2e35776aeed249d39229b8a06fdd. Read docs/SPECTRAL_ENDPOINT.md and the Rejected 0.08/0.23 rows in docs/SURVIVED_REJECTED_UNRESOLVED.md at coherence-drive 095d29d1a107d719f8aed9f89834d917b119ca4c.

## Evidence Log

- 2026-10-01. Read physics_evaluator.py and physics_evaluator_snippet.py at adab20380b2d2e35776aeed249d39229b8a06fdd.
- 2026-10-01. Cross-checked SPECTRAL_ENDPOINT.md and SURVIVED_REJECTED_UNRESOLVED.md Rejected section.

- 2026-10-02. Verification re-check: stress-tensor-modification origin/main had advanced to 09cd4862ea7ec4796b7ff96873e00c5295a92717 (pinch pointer). Cited fences at adab20380b2d2e35776aeed249d39229b8a06fdd still hold; SPECTRAL_ENDPOINT_POINTER.md text unchanged through 953097c. Evidence SHA remains adab203; not re-baselined to newer main.

## Change History

- 2026-10-02. Verification pass: confirmed claims at adab203; noted origin/main advance to 09cd486 without changing cited fences. Wording adjusted from HEAD to evidence commit.
- 2026-10-01. Initial archive entry. No Stage-1 freeze file was changed. Code was not edited.
