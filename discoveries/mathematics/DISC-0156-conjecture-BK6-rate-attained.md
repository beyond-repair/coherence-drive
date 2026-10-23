# Discovery: Conjecture BK.6, the ρ^−n rate of Theorem BK is attained (C_δ(0.8)≈0.6025)

## Discovery ID

DISC-0156

## Status

CONJECTURE (repository's own; floats only). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~2:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 00d0d28b71db264b070be23c73f8e3f67de704db, GASKET.md Theorem BK / Conjecture BK.6; scripts/gasket_fractional_uniform_rate.py float section.

## Original Evidence

At α=0.8 and N=10, the deficit n-error δ^(100)−δ^(n) times ρ^n is 0.6289, 0.6127, 0.6041, 0.6028, 0.6025 at n=15, 20, 30, 40, 50. It is positive and below the certified BK.3/BK.4 bound. Reproduced in the repository witness run at that commit.

## Discovery

The repository conjectures that ρ^−n is attained, with C_δ(0.8)≈0.6025. It says this would follow from a sign of Cov(ω_k,F_k), for example if ω_k were monotone.

## Why It Matters

Together with DISC-0155 it would make ρ^−n the exact order of the n-error, as DISC-0153 did for the cell modulus in N.

## Derivation

None (numerical).

## Assumptions

Theorems BJ and BK as stated.

## New Results

None proved. Observation only, not a claim: 0.6025 is close to the certified g-bracket [0.600945014,0.600963487] of DISC-0153 but lies outside it, and the sequence is still drifting. No relation is asserted.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Not attacked independently this slice beyond confirming the repository's floats in its own witness run.

## Experimental Validation

Floats only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0155 → DISC-0156 (mathematical); DISC-0154 → DISC-0156 (historical: the attainment half of BJ.7's "order ρ^−n").

## Open Questions

Whether Cov(ω_k,F_k) has a fixed sign; the limit value of C_δ.

## Next Experiments

Test the monotonicity of ω_k(y) in y numerically on graph levels; extend floats to n=60–90.

## Reproduction Instructions

git -C informational-flux-identity checkout 00d0d28b71db264b070be23c73f8e3f67de704db; python3 scripts/gasket_fractional_uniform_rate.py (float section).

## Evidence Log

- 2026-10-23 ~2:54am EDT. Indexed from the repository's float evidence.

## Change History

- 2026-10-23. Initial archive entry.
