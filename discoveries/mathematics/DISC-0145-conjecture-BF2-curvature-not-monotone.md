# Discovery: Conjecture BF.2, c''(α) is not monotone

## Discovery ID

DISC-0145

## Status

CONJECTURE (repository's own Conjecture BF.2; floats only). Do not cite as a theorem. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:00pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit b090826f15adc93d8ed6cbf352346dabb31ea136, README "Conjecture BF.2", scripts/mesh_noncentrality_convex.py float_cpp().

## Original Evidence

Repository floats: c''(1^−) ≈ 1.5310, c''(0.75) ≈ 1.5757, c''(0.46) ≈ 1.5932, c''(0.25) ≈ 1.5851, c''(0^+) ≈ 1.5567. Certified enclosures (e.g. [0.52046, 2.62473] near α = 0) are too wide to decide.

## Discovery

c'' rises from α = 1 to an interior maximum near α ≈ 0.46 and falls toward α = 0.

## Why It Matters

Fixes the next-order shape of c; would rule out a simple log-convex or monotone-cumulant mechanism.

## Derivation

None (conjecture).

## Assumptions

As DISC-0144.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive independent floats (own Schur recursion, n=24, 60 digits, centred second differences on α = k/40): 1.5604 at α = 0.025, maximum 1.5934 at α ≈ 0.45–0.475, 1.5416 at α = 0.95, consistent with the repository's profile (interior maximum, both ends lower). No counterexample; floats only.

## Experimental Validation

Floats only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

- DISC-0144 → DISC-0145 (mathematical).

## Open Questions

Certified enclosure of c'' tight enough (width < ~0.03) to separate the interior maximum from both ends.

## Next Experiments

Rerun the BF certificate with finer ε-intervals and cells near the ends; certify c''(0.46) − c''(1^−) > 0 and c''(0.46) − c''(0^+) > 0.

## Reproduction Instructions

As DISC-0144.

## Evidence Log

- 2026-10-22 ~8:15pm EDT. Recorded from IFI b090826f15adc93d8ed6cbf352346dabb31ea136; archive floats as above.

## Change History

- 2026-10-22. Initial archive entry.
