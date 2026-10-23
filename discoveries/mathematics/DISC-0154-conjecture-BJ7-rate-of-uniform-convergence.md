# Discovery: Conjecture BJ.7, the n-error of u_n→ū at the corner neighbours is of order ρ^−n

## Discovery ID

DISC-0154

## Status

CONJECTURE (repository's own; floats only). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~1:02am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 815003f22507fa34258d8b917a0e3a776340b16a, GASKET.md Theorem BJ / Conjecture BJ.7; scripts/gasket_fractional_corner_sharpness.py float section.

## Original Evidence

At α=0.8, at n=N+40 the gap between u_n and ū at the corner neighbours times ρ^(n−N) is 0.60 and 0.71, so the error looks like Cρ^−n. The repository says this explains Theorem BI's drifting n=40 floats.

## Discovery

Open problem: a rate for the uniform convergence of DISC-0151, conjecturally ρ^−n at the corners. This is the third item of Conjecture BI.7, which Theorem BJ left open.

## Why It Matters

Would quantify how fast the graph extensions approach the continuum limit ū.

## Derivation

None (numerical).

## Assumptions

Theorems BI and BJ as stated.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Not attacked independently this slice. Two float ratios (0.60, 0.71) are not yet constant, so the constant C is not pinned.

## Experimental Validation

Floats only (repository).

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0153 → DISC-0154 (mathematical); DISC-0152 → DISC-0154 (historical: BI.7 item 3).

## Open Questions

Whether the ratio converges, and to what.

## Next Experiments

Float ratios at n=N+k for k up to 100 at several N; an upper bound from BJ.1's (3/5)^n defect.

## Reproduction Instructions

git -C informational-flux-identity checkout 815003f22507fa34258d8b917a0e3a776340b16a; python3 scripts/gasket_fractional_corner_sharpness.py (float section).

## Evidence Log

- 2026-10-23 ~1:02am EDT. Indexed from the repository's float evidence.

## Change History

- 2026-10-23. Initial archive entry.
