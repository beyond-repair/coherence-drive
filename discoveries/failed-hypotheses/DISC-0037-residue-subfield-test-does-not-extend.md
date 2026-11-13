# Discovery: The subfield test S_k ∉ GF(2^p) does not prove the residue conjecture

## Discovery ID

DISC-0037

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0036.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit bd212e6da68d4c71940c977400c66c507b40862a. Paths: README.md "Residue condition: lengths 2^j + 1 and the limits of the subfield test" → Negative result; COMPLETION_LOG.md "fifth run" → Negative result recorded; scripts/check_residue_p_plus_one.py (EXPECTED_SUBFIELD_ZEROS).

## Original Evidence

Exhaustive GF(2^64) counts in the repository of chains whose S_k lies in GF(2^p), p the largest power of two below k: k = 6: 8 of 64; k = 11: 32 of 2048; k = 13: 48 of 8192; k = 14: 32 of 16384; k = 15: 176 of 32768 (separate run, not in the committed script). Zero for k = 7, 10, 12 and for k = 3, 5, 9.

## Discovery

Rejected hypothesis: for every k not a power of two, every chain has S_k ∉ GF(2^p) with p = 2^⌊log₂ k⌋ (the property that proves DISC-0029 and DISC-0036). It fails at k = 6, 11, 13, 14, 15. S_k is still nonzero on those chains, but not for this reason, so the subfield test cannot settle DISC-0030 in general.

## Why It Matters

It closes off the most obvious extension of DISC-0029 / DISC-0036 and tells the next attempt to look for a different invariant.

## Derivation

Not applicable (finite counterexamples).

## Assumptions

As DISC-0028.

## New Results

Archive independent reproduction in GF(2^16) = F_2[x]/(x^16 + x^5 + x^3 + x + 1) by walking down from every nonzero element (no quadratic solver; every chain of length ≤ 15 lies in GF(2^16)): counts 8, 32, 48, 32, 176 for k = 6, 11, 13, 14, 15 and 0 for k = 3, 5, 7, 9, 10, 12, exactly matching the repository, including the k = 15 value that the committed script omits.

## Prior Art

Not applicable.

## Novelty Analysis

REJECTED as a proof route. No novelty claimed.

## Falsification Attempts

The rejection itself was reproduced in a second field model by a different enumeration.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Counterexamples verified; hypothesis false.

## Patent Relevance

None.

## Related Discoveries

- DISC-0029, DISC-0036. Mathematical. The cases where the subfield test does work.
- DISC-0030. Mathematical. Still open; this route does not close it.

## Open Questions

Whether the norm reformulation G_k(1, 0) = 1 (repository, checked k ≤ 7, term counts 3, 3, 13, 27, 103, 365, 1651) has a provable structure.

## Next Experiments

None for this route.

## Reproduction Instructions

Repository: `git checkout bd212e6da68d4c71940c977400c66c507b40862a && python scripts/check_residue_p_plus_one.py` (k ≤ 14). Archive: the GF(2^16) script in DISC-0036 Reproduction Instructions (k ≤ 15).

## Evidence Log

- 2026-10-08. Recorded from README at bd212e6da68d4c71940c977400c66c507b40862a; repository script rerun OK; archive GF(2^16) reproduction exact.

## Change History

- 2026-10-08. Initial archive entry.
