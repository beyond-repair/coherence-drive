# Discovery: Conjecture BH.7, the far-field layer constant θ_∞(0.45) ≈ 0.52061 with O(3^−k) correction

## Discovery ID

DISC-0150

## Status

CONJECTURE (repository's own; floats only). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~10:00pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 156d8ce80c73147e3dc8aa34cbcea2ce6e42d989, GASKET.md Theorem BH (BH.6 text and Conjecture BH.7 in the commit message/CLAIM_STATUS row); scripts/gasket_fractional_corner_layer.py (float check "rho^-k theta_k ... settling near 0.52061").

## Original Evidence

Repository float evidence: ρ^−k θ_k increases with increments shrinking, settling near 0.52061 at α=0.45.

## Discovery

The value θ_∞(0.45)≈0.52061 and an O(3^−k) correction rate for ρ^−k θ_k → θ_∞ (existence of θ_∞ is DISC-0149 BH.6, derived).

## Why It Matters

Quantifies how the corner layer joins the outer flat regime.

## Derivation

None; numerical.

## Assumptions

As DISC-0149.

## New Results

None proved.

## Prior Art

Not searched beyond DISC-0149.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive (indep_theorem_BH.py) k=3..8 values 0.5172074, 0.5194682, 0.5202295, 0.5204820, 0.5205656, 0.5205934; successive differences 2.26e−3, 7.6e−4, 2.5e−4, 8.4e−5, 2.8e−5 shrink by ≈3 per level, consistent with O(3^−k); geometric extrapolation ≈0.520607. Survives this first attempt; not a proof.

## Experimental Validation

Computational only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0149 → DISC-0150 (mathematical).

## Open Questions

Interval certificate for θ_∞; closed form; why the correction ratio is 3.

## Next Experiments

Arb enclosure of θ_∞ via AT's Θ_AT on one log-period.

## Reproduction Instructions

As DISC-0149.

## Evidence Log

- 2026-10-22. Archive float trend recorded above.
- 2026-10-23 ~3:57pm EDT. DISC-0168 (Theorem BS at 316ee92917b1) derives, from AT.1 as stated (derived level only), c_∞(α)=θ_∞^BH(α); so θ_∞(0.45) would lie in BR.5's certified c_∞ bracket [0.520386,0.520825] (outward), consistent with ≈0.52061. Archive independent float c_∞(0.45)=0.5206072.

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-23 ~3:57pm EDT. Derived-only bracket for the value part noted from DISC-0168; the identification rests on AT.1 and the O(3^−k) rate is not addressed. Status stays CONJECTURE (the repository still lists BH.7 as open).
