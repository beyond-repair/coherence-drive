# Discovery: Conjecture BA.2, 2^−n κ_n(0.45) has a nonzero limit

## Discovery ID

DISC-0131

## Status

CONJECTURE (repository's own). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~1:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit fe388f3b633ff0cafbfd653758afde0ab7284b93. Path: README.md "CONJECTURE BA.2".

## Original Evidence

Float 2^−nκ_n=−2.0214, −1.6535, −1.3423, −1.1579, −1.0488, −0.9818 (n=1..6); Aitken on float levels 5–7 gives about −0.86 (not certified). Mechanism offered: the corner jump u_{c0}−(u_p+u_r)/2 runs 0.942, 0.763, …, 0.564 (n=1..7), apparently to a positive limit, with q_{c0}>0, so g_c∼2^n. Falsified by a certified sequence tending to 0 or −∞.

## Discovery

A scaling law for the mesh residual of DISC-0129.

## Why It Matters

Quantifies DISC-0130 witness (iii): the residual diverges like 1/h.

## Derivation

None (numerical).

## Assumptions

Assumption BA.

## New Results

Archive floats agree at n=5,6 (−1.0487908, −0.9817914). Successive ratios of increments (−1.0488+1.1579)/(−1.1579+1.3423)=0.592, (−0.9818+1.0488)/(…)=0.614: consistent with geometric convergence but not proof.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Only the float agreement above; level 7 not re-run in the archive.

## Experimental Validation

None.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0129 → DISC-0131 (mathematical); DISC-0130 (uses witness iii).

## Open Questions

Certified κ_5..κ_7; a proof of the corner-jump limit.

## Next Experiments

Interval-certify κ_5, κ_6 with the repository's Krylov pipeline.

## Reproduction Instructions

As DISC-0129.

## Evidence Log

- 2026-10-22. Archive floats n=5,6 match.

## Change History

- 2026-10-22. Initial archive entry.
