# Discovery: Device-intrinsic residual from any pseudotensor first-derivative reading + C5 + static massless C6 (Kept Failure Z.1)

## Discovery ID

DISC-0071

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0070.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 1282986d667c7ff87164deca5a7834819d1f3555. Paths: README.md Theorem Z → Kept Failure Z.1; CLAIM_STATUS.md; scripts/hemitropic_reading_flux.py.

## Original Evidence

Allowing Levi-Civita contractions hε^{ijk}∂_kΨ in the first-derivative family does not open a surface-independent nonzero G for an isolated device under C5 and static massless C6. The conserved class grows only by ε·∇K(Ψ), a curl with zero flux on every closed surface (Z.3). Every other reading moves with the audit surface (Z.4): s ε·E gives three different decaying values on the three vacuum spheres; x ε·E equals e_x×∮Ψn, the P.2 flux rotated, and is set by the sphere centre. After Maxwell removal the residual is 0, a boundary-only curl that is 0, or surface-dependent.

## Discovery

Rejected hypothesis: relaxing O(3) to SO(3) covariance (parity-odd pseudotensor term) opens a net source. It does not.

## Why It Matters

With DISC-0060, DISC-0062, and DISC-0069 it closes every first-derivative reading f δ+g E⊗E+h ε·E in (x, Ψ, s) under static massless A_0. The only new conserved piece is invisible to every closed audit surface.

## Derivation

DISC-0070 Theorem Z.2–Z.4. Checked; no gap. Interpretive step (same as O.1/P.2/Q.1/R.1/T.1/U.1/V.1/Y.1): a force on the device does not depend on where the audit surface is drawn.

## Assumptions

Assumption Z, C5, static massless C6, isolated device.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_Z.py`: h(Ψ) ε·E zero on all spheres including the split sphere; s ε·E and x ε·E reproduce the README values on an independent grid; extra attack h=|x|² gives 2c×(4π/3)p_c, centre-dependent (zero at c=0), so nonlinear position dependence also fails to give a surface-independent flux.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Tried to break the rejection with a nonlinear x-dependent h (|x|²) and with surfaces cutting through the charge region (split sphere). Both behave as the theorem says.

## Experimental Validation

None.

## Mathematical Status

Rejection of one route only; higher-derivative non-polynomial, nonlocal, time-dependent, Ψ_info ≠ A_0, and Stage 2 0.45 mesh stay OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0070. Theorem Z.
- DISC-0069, DISC-0062, DISC-0060. Sibling first-derivative kept failures.
- DISC-0049. Kept Failure P.2 (x_m ε·∇Ψ reduces to it).

## Open Questions

As DISC-0070.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 1282986d667c7ff87164deca5a7834819d1f3555 && python3 scripts/hemitropic_reading_flux.py`; archive `/workspace/scratch-ifi/indep_theorem_Z.py`.

## Evidence Log

- 2026-10-15 ~2:00am EDT. Repo witness EXIT 0; archive ALL PASS.

## Change History

- 2026-10-15. Initial archive entry.
