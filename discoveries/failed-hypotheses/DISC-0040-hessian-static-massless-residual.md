# Discovery: Nonzero residual from the Hessian reading with static massless A_0 on a vacuum surface

## Discovery ID

DISC-0040

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0039.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 5d931cf0eaca893135c92198de3dd81989629a4c. Paths: README.md Theorem M → Corollary 2 "KEPT FAILURE M.1"; README "What was tried and does not follow" OPEN bullet; CLAIM_STATUS.md Hessian-reading row; scripts/hessian_flux_reduction.py.

## Original Evidence

Kept Failure M.1: under C6 (Ψ_info = A_0) with static massless fields, ΔA_0 = −ρ/ε_0 = 0 on any closed surface drawn in vacuum around the device, so G = 0 and ΔF = W χ_vac G = 0 for every W and every κ in C5. Witness: lopsided interior lump with ΔP = 0 on the boundary layers gives G = (0, 0) exactly while summed |cell div| is 398 / 422.

## Discovery

Rejected hypothesis: the route "Hessian reading + C5 + static massless C6" yields a nonzero closed-surface residual on a vacuum surface. By DISC-0039 G depends only on ΔA_0 on S, which is zero in vacuum electrostatics, so the residual is zero for every W and κ. This rejects one route, not Stage 2 as a whole; the quadratic reading and the 0.45 mesh solve remain OPEN.

## Why It Matters

It closes the simplest electrostatic reading of the frozen chain as a source of net force, independent of the interior asymmetry of the device.

## Derivation

DISC-0039 plus Gauss's law in the static case: in vacuum near S, A_0 is harmonic, hence smooth (C³ holds), and ΔA_0 = 0 on S. Checked; no gap. A surface charge on S, or a massive (screened) field, would leave the hypothesis of the failure; the repository records the screened case separately as G = m² ∮ Ψ n.

## Assumptions

Assumption M (Hessian reading), C5, C6 with static massless fields, S in vacuum.

## New Results

Archive check: the repository lump witness rerun at 5d931cf gives G = (0, 0); archive discrete checks in DISC-0039 confirm G = boundary sum of ΔP on independent grids, so any P with ΔP = 0 on the boundary layers has G = 0.

## Prior Art

Not applicable (rejection of a route). The physics fact used, ΔA_0 = 0 in source-free electrostatics, is classical.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Looked for an escape inside the stated assumptions (interior singularities, asymmetric devices): Theorem M allows both and still gives G = 0. None found.

## Experimental Validation

None.

## Mathematical Status

Route rejected under its stated assumptions.

## Patent Relevance

None.

## Related Discoveries

- DISC-0039. Mathematical. The reduction that forces the zero.
- DISC-0002. Failed hypothesis. Earlier thrust reading of the same flux identity.

## Open Questions

The quadratic reading of (∇Ψ)^{ij}; ΔΨ_info on the frozen 0.45 mesh.

## Next Experiments

See DISC-0039.

## Reproduction Instructions

`git checkout 5d931cf0eaca893135c92198de3dd81989629a4c && python3 scripts/hessian_flux_reduction.py`.

## Evidence Log

- 2026-10-08. Recorded from README Kept Failure M.1 at 5d931cf0eaca893135c92198de3dd81989629a4c; witness rerun OK.

## Change History

- 2026-10-08. Initial archive entry.
