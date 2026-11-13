# Discovery: Kept Failure AU.1, the corner-resolvent oscillation is not a single harmonic

## Discovery ID

DISC-0117

## Status

REJECTED (the hypothesis). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~7:02am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, main, b036dcfb89e66ffa51ebf8407c08996d7fa3d17e, GASKET.md "KEPT FAILURE AU.1"; witness scripts/gasket_fractional_log_mean.py.

## Original Evidence

Claim tested: θ(x)=⟨Θ⟩+2 Re(θ̂_1 x^(iω)), a pure cosine in log_5 x. AT.1's eight 9-digit Θ values fit it, which makes it tempting.

## Discovery

False: |θ̂_2| ≥ 1.34873e−11 is certified, so the second harmonic is present and M has a genuine pole at 1−γ±2iω (also k=3,4).

## Why It Matters

Shows the profile carries a full tower of complex poles, not one pair; a 9-digit fit is not evidence of a single mode.

## Derivation

By DISC-0116 (2), a nonzero θ̂_k is exactly a genuine pole.

## Assumptions

DISC-0116 assumptions.

## New Results

None beyond the rejection.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Archive DFT (60 digits, own recursion): |θ̂_2| = 1.3487e−11, far above float error (~1e−35). Rejection confirmed.

## Experimental Validation

None.

## Mathematical Status

Counterexample (certified in repo, reproduced in float here).

## Patent Relevance

None.

## Related Discoveries

DISC-0116 → DISC-0117 (mathematical); sits beside DISC-0114 (failed hypothesis: simplest closed forms fail where certificates succeed).

## Open Questions

Whether θ̂_k≠0 for every k.

## Next Experiments

None specific.

## Reproduction Instructions

As DISC-0116.

## Evidence Log

- 2026-10-22. Repo + archive PASS.

## Change History

- 2026-10-22. Initial archive entry.
