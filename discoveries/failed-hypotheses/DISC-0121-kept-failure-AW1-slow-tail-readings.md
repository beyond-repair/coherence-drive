# Discovery: Device-intrinsic residual from a slow-tail smoothing reading (−Δ)^{−τ}Ψ, including the radius-free marginal readings, under C5 + static massless C6 (Kept Failure AW.1)

## Discovery ID

DISC-0121

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0120.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7a12ab736327e6d314c2035b7c8cfb95a2025dc6. Paths: README.md Theorem AW → Kept Failure AW.1; CLAIM_STATUS.md Theorem AW row; scripts/slow_tail_reading_flux.py.

## Original Evidence

Slow-tail smoothing does not open a surface-independent nonzero G for an isolated static device. The literal (−Δ)^{−τ}A_0 does not exist for τ≥(1+ℓ)/2; its finite-part continuation exists for every τ>0, but any value that is the same on every audit surface is 0 (AW.2), and for non-integer τ the self reading is surface-dependent for every nonzero device. The tempting cases are the marginal readings τ=3/4 (charged) and τ=5/4 (dipole): G is finite, nonzero and the same on every radius for a given centre ((16/9)Q²(c−x_Q), (16/75)(|p|²c−8(p·c)p)), but it is linear in where the audit sphere is centred and vanishes on spheres centred on the device. Above the marginal τ it grows like R^{4τ−3} (or R^{4τ−5}). The integer-τ loophole needs a polynomial added to Φ (e.g. Φ+E0·x, giving G=−E0∫σ), i.e. an external uniform field, outside Assumption AW. Interpretive step (labeled in the README, same as O.1–AV.1): a centre-dependent G cannot be read as a force on the device.

## Discovery

Rejected hypothesis: a slow-tail smoothing reading of Ψ produces a net, device-intrinsic residual after Maxwell removal. It does not; the radius-independent marginal value is an audit-centre artefact.

## Why It Matters

With DISC-0119 it closes the nonlocal Maxwell-form route for static massless A_0, including kernels without the o(R^{−2}) decay. It is a failure of that route, not of Stage 2.

## Derivation

See DISC-0120.

## Assumptions

As DISC-0120, plus the README's labeled interpretive step that a force on the device is independent of the audit surface.

## New Results

Archive surface quadrature (`/workspace/scratch-ifi/indep_theorem_AW.log`): τ=3/4, one unit charge, R=4: centres 0, e_x, −2e_y give 0, (16/9)e_x, −(32/9)e_y (centre-dependent, radius-free); τ=5/4 dipole: G(2c)=2G(c), G(−c)=−G(c) exactly; centred spheres 0; τ=1 cluster grows ∝R; τ<3/4 decays to 0; non-integer τ leaks σ into the vacuum for a compact radial device while τ=1 does not.

## Prior Art

Not applicable (failed hypothesis); mechanism is the classical non-locality of fractional powers of the Laplacian plus the zero static self-force.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Tried to find a surface-independent nonzero value: the marginal value is the same on every radius but changes with the centre and is 0 on centred spheres; the integer-τ compact-σ case gives G≡0. Hypothesis fails.

## Experimental Validation

None.

## Mathematical Status

Kept Failure (rejected route), supported by DISC-0120's proofs plus a labeled interpretive step.

## Patent Relevance

None.

## Related Discoveries

- DISC-0120. Theorem AW.
- DISC-0119. Kept Failure AV.1 (decaying nonlocal kernels).
- DISC-0071, DISC-0069, DISC-0062, DISC-0060, DISC-0058. Earlier kept failures of the same class.

## Open Questions

Higher multipoles (DISC-0122), non-Maxwell slow-tail tensors, time-dependent fields, Ψ_info ≠ A_0, and the 0.45 mesh remain OPEN.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0120.

## Evidence Log

- 2026-10-22 ~8:55am EDT. Repo witness EXIT 0 (82 ok); independent check 59/59 PASS.

## Change History

- 2026-10-22. Initial archive entry.
