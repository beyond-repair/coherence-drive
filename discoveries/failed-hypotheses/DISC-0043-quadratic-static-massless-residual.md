# Discovery: Nonzero residual from the quadratic reading with static massless A_0 (Kept Failure N.1)

## Discovery ID

DISC-0043

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0042.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 20e45cdb6b1bc16bff4739cc45ccba92fd446e33. Paths: README.md Theorem N → Corollary 1 "KEPT FAILURE N.1" and Corollary 2 (screened case); CLAIM_STATUS.md quadratic-reading row; scripts/quadratic_flux_reduction.py.

## Original Evidence

Under C6 (Ψ_info = A_0) with static massless fields, ε₀Q is exactly the Maxwell electrostatic stress, so nothing is left after the Maxwell piece is removed; without removing it, G_i = ε₀⁻¹∫ρE_i, the Coulomb self-force, which is 0 for an isolated device (odd integrand). Screened case: G_i = (m²/2)∮Ψ²n_i, surface-dependent and O(e^{−2mR}). Witnesses: isolated cluster |G| ≈ 10⁻¹⁴ against ∮|Q^{xj}n_j| = 15.131871; outside charge gives 4π F_Coulomb; Yukawa m = 0.7, |G| = 1.524401, 0.3233750, 0.01713515 at R = 2, 3, 5.

## Discovery

Rejected hypothesis: the route "quadratic reading + C5 + static massless C6" yields a nonzero residual after the Maxwell piece is removed. It yields identically zero; the screened leftover is a mass-term surface flux that depends on the drawn surface and decays as the surface recedes, not an interior source.

## Why It Matters

Together with DISC-0040 it closes both named readings of the frozen chain under static massless electrostatics.

## Derivation

DISC-0042 plus Gauss's law and Newton's third law for the Coulomb kernel (absolutely integrable odd integrand for Hölder, compactly supported ρ). Screened case: (Δ − m²)Ψ = −ρ/ε₀ gives ∂_iΨ ΔΨ = ρE_i/ε₀ + ½m²∂_i(Ψ²); radial Yukawa kernel kills the self-force term. Checked; no gap.

## Assumptions

Assumption N, C5, C6 static; massless for N.1, Yukawa-screened for Corollary 2; no charge outside S for the zero self-force.

## New Results

Repository witness rerun at 20e45cd: all checks passed (isolated |G| = 1.98×10⁻¹⁴; external-charge G = 4π F_Coulomb; Yukawa figures as quoted, shrinking with R).

## Prior Art

Not applicable (rejection of a route). Zero electrostatic self-force and the Proca stress are classical.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Looked for an escape inside the assumptions: interior asymmetry does not help (odd integrand); an outside charge gives the ordinary Coulomb force with its reaction outside S; screening gives only the surface-dependent mass-term flux. None survives as a residual.

## Experimental Validation

None.

## Mathematical Status

Route rejected under its stated assumptions.

## Patent Relevance

None.

## Related Discoveries

- DISC-0042. Mathematical. The reduction that forces the zero.
- DISC-0040. Failed hypothesis. The Hessian-reading counterpart (Kept Failure M.1).
- DISC-0002. Failed hypothesis. Earlier thrust reading of the same flux identity.
- DISC-0045. Failed hypothesis. Kept Failure O.1 (a1de4d9) closes the same route for every two-derivative reading.

## Open Questions

Readings other than Hessian and quadratic; Ψ_info ≠ A_0; the 0.45 mesh solve.

## Next Experiments

See DISC-0042.

## Reproduction Instructions

`git checkout 20e45cdb6b1bc16bff4739cc45ccba92fd446e33 && python3 scripts/quadratic_flux_reduction.py`.

## Evidence Log

- 2026-10-08. Recorded from README Kept Failure N.1 at 20e45cdb6b1bc16bff4739cc45ccba92fd446e33; witness rerun OK.

## Change History

- 2026-10-08. Initial archive entry.
