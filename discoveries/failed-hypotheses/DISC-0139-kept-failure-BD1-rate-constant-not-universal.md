# Discovery: Kept Failure BD.1, the 3^−n constant of 2−E_n/Y_n is neither the small-s value 2 nor independent of α

## Discovery ID

DISC-0139

## Status

REJECTED (repository's own Kept Failure BD.1). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~6:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 30bee3aab038a818c28144ef7d9787eaccdedf5a, README.md "KEPT FAILURE BD.1", CLAIM_STATUS.md Theorem BD row, scripts/mesh_noncentrality_limit.py.

## Original Evidence

README: two guesses fail, (i) c=2 from t_n(0+)=2·3^−n, (ii) c independent of α. Witness: certified c(0.45)∈[3.72198897,3.72914181], c(0.8)∈[2.57126273,2.57352573], disjoint and both >2. Floats c(0.25)≈4.4719725, c(0.45)≈3.7255634, c(0.8)≈2.5724294.

## Discovery

The rejected hypotheses: 2−E_n/Y_n∼2·3^−n, and an α-independent rate constant.

## Why It Matters

The limit angle is universal but the approach rate is not; the measure s^−αy_n ds lives at s∼5^−n where t_n has grown past its s→0 value.

## Derivation

Proved c(α)>2 for every α (BD.4); disjointness of the two certified brackets.

## Assumptions

As DISC-0138.

## New Results

None beyond DISC-0138.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection).

## Falsification Attempts

Archive floats at n=7 give 3^n(2−E/Y)=3.71905 (0.45) and 2.56985 (0.8), already far apart and both >2; Aitken 3.725636 and 2.572380 fall inside the certified brackets.

## Experimental Validation

Repository certification; archive floats agree.

## Mathematical Status

Rejected hypothesis (counterexample certified).

## Patent Relevance

None.

## Related Discoveries

- DISC-0138 → DISC-0139 (failed hypothesis).

## Open Questions

See DISC-0140.

## Next Experiments

None needed for the rejection.

## Reproduction Instructions

As DISC-0138.

## Evidence Log

- 2026-10-22 ~6:05pm EDT. Recorded from IFI 30bee3aab038a818c28144ef7d9787eaccdedf5a; archive indep_theorem_BD.py 45/45 PASS.

## Change History

- 2026-10-22. Initial archive entry.
