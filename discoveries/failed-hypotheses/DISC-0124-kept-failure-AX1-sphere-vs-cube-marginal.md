# Discovery: Kept Failure AX.1, a centre-independent marginal value on spheres is not a force

## Discovery ID

DISC-0124

## Status

REJECTED (route). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~11:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e81b8148608b360254f88c0534e71ace97c54783. Paths: README.md Kept Failure AX.1; CLAIM_STATUS.md Theorem AX row; scripts/multipole_marginal_flux.py Part 4.

## Original Evidence

P*+ξ_x⁵ at τ=11/4 gives G=g0=(64√11/8085−5888/266805)e_x≈0.0041855e_x on every centred sphere and →g0 on spheres of every centre, but −0.0238957e_x on every centred cube and unbounded (∝λ) on dilated off-centre cubes.

## Discovery

The hypothesis tested: once M=0, the residual g0 is a device-intrinsic, surface-independent value. It fails: spheres and cubes disagree.

## Why It Matters

It is the closest the slow-tail family has come to a radius- and centre-free nonzero reading, and it still depends on the surface shape.

## Derivation

Repository computation (Part 4). Archive recomputation below.

## Assumptions

As DISC-0123.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_AX.py`: centred spheres R=1,3,9 give 0.0041854971e_x (matches g0=0.004185497113 to 1e−10); own cube-face quadrature at half-sides 2 and 4 gives −0.02389574e_x, matching the repo. Off-centre cubes not rerun.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

The failure itself was reproduced independently (sphere vs cube).

## Experimental Validation

None.

## Mathematical Status

Counterexample to surface independence (computed; exact g0 closed form from repo).

## Patent Relevance

None.

## Related Discoveries

- DISC-0123. Theorem AX.
- DISC-0121. Kept Failure AW.1 (same rejected route, centre-dependent version).

## Open Questions

Whether any slow-tail reading is shape-independent beyond spheres; interpretive step is the same as AW.1.

## Next Experiments

Rerun off-centre dilated cubes in the archive.

## Reproduction Instructions

As DISC-0123.

## Evidence Log

- 2026-10-22 ~11:01am EDT. Repo witness EXIT 0; archive sphere and cube values reproduced.

## Change History

- 2026-10-22. Initial archive entry.
