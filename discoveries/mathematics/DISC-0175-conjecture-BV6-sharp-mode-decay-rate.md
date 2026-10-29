# Discovery: Conjecture BV.6, the Fourier modes of the profile F=θ decay exactly like e^(−2π²|k|/ln5), and F does not continue past the strip |Im t|<π/ln5

## Discovery ID

DISC-0175

## Status

CONJECTURE (repository's own). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~6:56pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit cec4aff731cef6bb581c318f736de79d68d90b1f.

## Original Evidence

GASKET.md Conjecture BV.6 (line 3019); float evidence line 3042.

## Discovery

Claim: |θ̂_k|≍e^(−2π²|k|/ln5), i.e. lim|θ̂_k|^(1/|k|)=e^(−2π²/ln5), so BV.3's upper bound (DISC-0173) is sharp and the strip of holomorphy is maximal (singularities of Q_∞ on (−∞,0)).

## Why It Matters

It would make the strip width π/ln5 the exact analytic radius of the oscillation, the lower half of BU's open decay-rate question.

## Derivation

None (conjecture). Evidence: certified |θ̂_k|e^(2π²k/ln5)∈[0.60,0.93] for k=1–11; consecutive float ratios 3.6–6.5e−6 versus e^(−2π²/ln5)=4.7155e−6.

## Assumptions

Theorem BV (DISC-0173).

## New Results

None.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

My 110-digit floats (/workspace/scratch-ifi/indep_theorem_BV.py) give |θ̂_k|e^(2π²k/ln5)=0.777, 0.607, 0.842, 0.863, 0.728, 0.784, 0.834, 0.674, 0.799, 0.927, 0.706 for k=1..11: bounded and not trending to 0 or ∞, consistent with the conjecture but irregular (no clean geometric correction), so eleven modes cannot rule out a slowly varying sub-exponential factor. Not broken.

## Experimental Validation

Not applicable.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0173 (Theorem BV), DISC-0171 (Theorem BU), DISC-0116 (Theorem AU, Mellin poles of r_∞).

## Open Questions

Whether Q_∞ (equivalently r_∞) has singularities on the negative axis at the boundary angle.

## Next Experiments

Search numerically for zeros of 2+s−2η(s) as s approaches (−∞,0) from above; extend the coefficient table beyond k=11.

## Reproduction Instructions

As DISC-0173.

## Evidence Log

- 2026-10-23 ~6:56pm EDT. Indexed.

- 2026-10-29 ~1:00am EDT. Note: Theorem BW (IFI 14686342bd14, DISC-0176) certifies |θ̂_k|e^(2π²k/ln5)∈[0.60,0.93] for every k≤20 (archive floats 0.6066–0.9268, no trend; uncertified float at k=21 ≈0.713). Evidence only; stays CONJECTURE.

- 2026-10-29 ~1:57am EDT. Note: Theorem BX (IFI 06eddfa75600, DISC-0177) proves BV.6 is equivalent to ρ_k=|m̂_k|/m̂_0 converging to a nonzero limit (m the positive spectral measure per scale period), certifies ρ_k∈[0.60,0.92] for k≤20 with no visible limit, and shows m has ≥17 atoms per period if atomic (DISC-0178). The repository itself remarks that for several atoms in general position ρ_k oscillates, so BV.6 as worded may be too strong. Stays CONJECTURE.

- 2026-10-29 ~4:54am EDT. Note: Theorem BY (IFI 4e57bb8631cd, DISC-0179) certifies ρ_21=0.70637… inside [0.60,0.92]; one more data point, no visible limit. Stays CONJECTURE.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-29. Note added for DISC-0176 (history above kept unchanged).
- 2026-10-29. Note added for DISC-0177/0178 (history above kept unchanged).
- 2026-10-29. Note added for DISC-0179 (history above kept unchanged).
