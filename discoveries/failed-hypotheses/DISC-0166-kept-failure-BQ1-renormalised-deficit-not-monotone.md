# Discovery: Kept Failure BQ.1, the renormalised corner deficit V^(n)=ρ^−n(1−δ_1^(n)) is neither monotone nor one-sided

## Discovery ID

DISC-0166

## Status

REJECTED (the hypothesis that V^(n) approaches C_1 monotonically, or from one side). Certified counterexamples in the repository.

## Date Discovered

2026-10-23 (America/New_York), ~12:58pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 01c39d01aa86aa64eb165f85f28503f2e3209974.

## Original Evidence

GASKET.md Theorem BQ / Kept Failure BQ.1 (section starting line 2643) and scripts/gasket_fractional_deficit_rate_small_alpha.py at 01c39d01aa86aa64eb165f85f28503f2e3209974.

## Discovery

At α=0.45: V^(1)∈[0.083656,0.083739] < V^(2)∈[0.086386,0.086473] > V^(3)∈[0.084972,0.085057], and V^(2)>C_1 (≤0.0719611): not monotone, approached from above. At α=0.3: V^(3)≤0.092755 < C_1∈[0.0933210,0.0934143] < 0.094315≤V^(4): crosses its limit. At α=0.01: V^(1)<C_1: from below.

## Why It Matters

Rules out a monotone-limit proof route for C_N; DISC-0165's limit has to be (and is) obtained by bracketing.

## Derivation

Comparisons of certified arb enclosures (repository).

## Assumptions

The arb cells as printed by the repository.

## New Results

None beyond the counterexamples.

## Prior Art

n/a.

## Novelty Analysis

n/a (failure record).

## Falsification Attempts

The inequalities were re-checked from the printed intervals with exact rationals (/workspace/scratch-ifi/indep_theorem_BQ.py, PASS); repository witness EXIT 0.

## Experimental Validation

Computational only.

## Mathematical Status

Counterexample (certified).

## Patent Relevance

None.

## Related Discoveries

DISC-0165 → DISC-0166 (mathematical).

## Open Questions

Whether V^(n) is eventually monotone (repository lists it open).

## Next Experiments

Float V^(n) for large n at α=0.3, 0.45.

## Reproduction Instructions

As DISC-0165.

## Evidence Log

- 2026-10-23 ~12:58pm EDT. Indexed.

## Change History

- 2026-10-23. Initial archive entry.
