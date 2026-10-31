# Discovery: The universal resolvent bound r_n≤1/s alone proves a geometric refinement rate (Kept Failure AR.1)

## Discovery ID

DISC-0110

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0109.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3ec0a064caa5c70d6c4bfb23e7c37af89091abb2. Paths: GASKET.md Theorem AR → KEPT FAILURE AR.1; CLAIM_STATUS.md AR row; scripts/gasket_fractional_decimation_rate.py (AR.1 section).

## Original Evidence

GASKET.md Kept Failure AR.1: with only r_n≤1/s (den≥4+s), (3/5)D_j(s)≤(3/5)·M(s), M(s)=(2+s)(5+s)(6+s)/(4+s)², and (3/5)M(0)=(3/5)·60/16=2.25>1, so (3/5)ⁿP_n is uncontrolled and no rate follows. AQ's certified power ceiling forces den→6 at small s, which is what makes ∏(3/5)D_j converge.

## Discovery

Rejected proof route: the rate of DISC-0109 needs DISC-0106's certificate; the a-priori bound is not enough.

## Why It Matters

Marks why Theorem AR is conditional on the computer-assisted part of AQ.

## Derivation

(3/5)·(2·5·6)/16 = 2.25, checked exactly in the archive.

## Assumptions

As DISC-0109.

## New Results

None beyond confirmation.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a proof route).

## Falsification Attempts

Exact arithmetic of the bound; repo witness PASS AR.1; archive indep PASS.

## Experimental Validation

/workspace/scratch-ifi/repo_theorem_AR.log; /workspace/scratch-ifi/indep_theorem_AR.log section F.

## Mathematical Status

Rejected as a proof route (the bound is valid; the inference is not). Note this rejects a route, not the conclusion: DISC-0109 stands.

## Patent Relevance

None.

## Related Discoveries

- DISC-0109. Mathematical. Theorem AR.
- DISC-0106. Mathematical. AQ's power ceiling is the missing input.
- Sits beside DISC-0107 (AQ.1). Failed hypothesis.

## Open Questions

None.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0109.

## Evidence Log

- 2026-10-22. Recorded from GASKET.md Kept Failure AR.1 at 3ec0a064caa5c70d6c4bfb23e7c37af89091abb2; repo and archive confirm.

## Change History

- 2026-10-22. Initial archive entry.
