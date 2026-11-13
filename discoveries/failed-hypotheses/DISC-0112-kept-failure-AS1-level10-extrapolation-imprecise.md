# Discovery: Kept Failure AS.1, AR's exact ratio does not make level-10 extrapolation precise

## Discovery ID

DISC-0112

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York).

## Source Repositories

beyond-repair/informational-flux-identity, main, a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7, GASKET.md "KEPT FAILURE AS.1"; witness scripts/gasket_fractional_limit_digits.py.

## Original Evidence

Claim tested by the repository: with ρ=5^0.45/3≈0.687726 (DISC-0109), one-step geometric extrapolation of recorded levels 9, 10 recovers 𝓛(0.45) to 1e−4.

## Discovery

False. ρ-extrapolation gives 0.820862 (miss 2.76e−4); Aitken Δ² on levels 8, 9, 10 gives 0.821526 (miss 3.87e−4); the effective ratio (‖F(10)‖−𝓛)/(‖F(9)‖−𝓛)=0.68298 still differs from ρ by ≈0.7%.

## Why It Matters

AR fixes the ratio only asymptotically; finite-level data plus AR do not certify digits. Only the DISC-0111 certificate does.

## Derivation

Arithmetic on recorded ‖F(8)‖=0.848024495085, ‖F(9)‖=0.839442326601, ‖F(10)‖=0.833639705732 (GASKET.md Kept Failure J.4) and certified 𝓛.

## Assumptions

Recorded level values; DISC-0111 enclosure.

## New Results

Archive reproduces: ρ-extrapolation 0.8208605 (miss 2.781e−4), Aitken 0.8215261 (miss 3.874e−4), effective ratio 0.682981. Digits-only note: the archive's ρ-extrapolation differs from the repo's printed 0.820862 by ≈1.5e−6 (miss 2.78e−4 vs 2.76e−4), likely from the repo using unrounded level values; immaterial to the >1e−4 conclusion.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

The rejection itself was reproduced independently (archive section D).

## Experimental Validation

None.

## Mathematical Status

Rejected heuristic.

## Patent Relevance

None.

## Related Discoveries

- DISC-0111 → DISC-0112. Mathematical.
- DISC-0112 sits beside DISC-0110 and DISC-0107. Failed hypothesis: shortcuts around AQ/AS's certificates.

## Open Questions

None.

## Next Experiments

None required.

## Reproduction Instructions

As DISC-0111.

## Evidence Log

- 2026-10-22. Repo and archive PASS.

## Change History

- 2026-10-22. Initial archive entry.
