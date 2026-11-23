# Discovery: Kept Failure BV.5, the maximum and minimum of the log-periodic profile F=θ are not half a period apart

## Discovery ID

DISC-0174

## Status

REJECTED (repository's own Kept Failure, certified witness). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~6:56pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit cec4aff731cef6bb581c318f736de79d68d90b1f.

## Original Evidence

GASKET.md Kept Failure BV.5 (line 3017), using Theorem BV.5 (line 3005) certified extremes.

## Discovery

Hypothesis: t_min=t_max+1/2 (mod 1), suggested by BU.3's extremal grid nodes 197068 and 65996 out of 2^18 (difference exactly 2^17) and BT.4's 2^16. It is weaker than BU.4's antisymmetry (DISC-0172), so BU.4's refutation did not decide it. Refuted: t_max−t_min−1/2=−1.6240189637007127e−7≠0 (certified radii ~1e−55), about 0.043 of a BU cell, which is why the grids could not see it.

## Why It Matters

Closes the next experiment I recorded in DISC-0171 (float offset 0.4999998376). The profile has no hidden half-period structure of either kind (value antisymmetry or extremal placement).

## Derivation

Direct subtraction of BV.5's certified locations.

## Assumptions

Theorem BV.3–BV.5 as stated (DISC-0173).

## New Results

The extremal offset is 1/2−1.6240189637e−7 periods.

## Prior Art

n/a.

## Novelty Analysis

n/a (failed hypothesis).

## Falsification Attempts

Independent 110-digit floats (/workspace/scratch-ifi/indep_theorem_BV.py): Newton on the 13-mode trig polynomial gives t_max−t_min−1/2=−1.6240189637007127e−7, matching to <1e−20; consistent with DISC-0171's 5^−44 float 0.4999998376.

## Experimental Validation

Not applicable.

## Mathematical Status

Hypothesis refuted by certified witness.

## Patent Relevance

None.

## Related Discoveries

DISC-0173 (Theorem BV), DISC-0172 (Kept Failure BU.4), DISC-0171 (Theorem BU).

## Open Questions

Closed form of t_max, t_min.

## Next Experiments

None needed for the rejection.

## Reproduction Instructions

As DISC-0173.

## Evidence Log

- 2026-10-23 ~6:56pm EDT. Indexed; reproduced in floats.

## Change History

- 2026-10-23. Initial archive entry.
