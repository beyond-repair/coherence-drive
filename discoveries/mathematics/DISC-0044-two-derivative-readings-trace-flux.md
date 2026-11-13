# Discovery: Every two-derivative reading reduces to a surface-dependent trace flux (Theorem O)

## Discovery ID

DISC-0044

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0042.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit a1de4d9cf64fd360075d63f8a0a054871513fb2a. Paths: README.md "Theorem O. Every two-derivative reading reduces to a trace flux" (Assumption O, Theorem O, Proof, Corollaries O.1–O.2, Asymptotics, Witness, NOT THIS) and the updated OPEN bullet in "What was tried and does not follow"; GASKET.md Stage 2 OPEN bullet; scripts/general_reading_flux.py; scripts/cli.py. CLAIM_STATUS.md has no Theorem O row at this commit (provenance note only, not a contradiction).

## Original Evidence

Inside Assumption O (local, constant-coefficient, shift-invariant, O(d)-covariant, exactly two derivatives per term), T^{ij} = a ∂_i∂_jΨ + b δ_{ij}ΔΨ + c ∂_iΨ∂_jΨ + d δ_{ij}|∇Ψ|², and ∂_jT^{ij} = (a+b)∂_iΔΨ + c ∂_iΨ ΔΨ + (c/2 + d)∂_i|∇Ψ|². With static massless C6 (Ψ = A_0, E = −∇A_0) on a closed vacuum surface S around an isolated device, G_i(S) = (c/2 + d)∮_S |E|² n_i dA (O.1); ∫_{ℝ³} ∂_jT^{ij} = 0 and G(S) = −(exterior integral) (O.2); for dilations S_R = R·S_1, G(S_R) = (c/2 + d) R^{−2} Q_tot²/(4πε₀)² ∮_{S_1} n|y|^{−4} dA + O(R^{−3}). Witness trace fluxes P on three vacuum spheres around the asymmetric cluster of Theorem N: (−18.295274824, −6.781652669, 6.231252988), (−35.04687982, −11.166762011, 14.456027559), (4.23976535, −2.825807999, −3.116738754); dilation limit (−105.632225, 70.421484, −35.210742).

## Discovery

Classification of isotropic rank-2 tensors quadratic or linear in the first and second derivatives (first fundamental theorem of invariant theory for O(d)), followed by the product rule, the Maxwell-stress split c(∂Ψ∂Ψ − ½δ|∇Ψ|²) + (c/2 + d)δ|∇Ψ|², and the far-field Coulomb expansion. All classical; the repository applies them to the whole two-derivative family of readings of the frozen rank-2 symbol at once.

## Why It Matters

It generalises DISC-0039 (Hessian, (1,0,0,0)) and DISC-0042 (quadratic, (0,0,1,−½)) to every reading in the family: under static massless C6 the only survivor is the trace flux (c/2 + d)∮|E|²n, which vanishes when c + 2d = 0 and otherwise depends on where the audit surface is drawn (DISC-0045).

## Derivation

Checked line by line. Shift invariance removes undifferentiated Ψ; two derivatives allow only ∂∂Ψ or ∂Ψ∂Ψ; O(d)-invariant rank-4 tensors are spanned by the three δδ pairings, and symmetry of ∂_k∂_l and of ∂_kΨ∂_lΨ collapses them to the four terms. Divergence formula, O.1 split, O.2 decay (|E|² = O(r^{−4}), sphere flux O(R^{−2})) and the R^{−2} leading coefficient (x = Ry, dA_x = R²dA_y) all verified; the coefficient vanishes on spheres centred at the expansion point by symmetry.

## Assumptions

Assumption O (a family of readings, not a change to the freeze); d = 3 for the corollaries; C5; C6 with Ψ_info = A_0, static, massless; ρ ∈ C^∞_c; S closed Lipschitz in vacuum enclosing supp ρ.

## New Results

Archive `/workspace/scratch-ifi/indep_general_O.py`: sympy residual of the divergence formula for general (a, b, c, d) and general Ψ is (0, 0, 0); null space of (R⊗R⊗R⊗R − I) stacked over six random orthogonal R (random reflections) has dimension 3, as stated; independent quadrature (160 Gauss–Legendre in cos θ by 320 azimuthal nodes, against the repository's 128 by 256) reproduces all three trace fluxes P to the 9 printed decimals and gives Maxwell flux ≤ 6.5×10⁻¹⁴; dilation limit coefficient reproduced to 6 decimals; R²P at R = 16, 32, 64 approaches it with errors halving, Richardson 2s(64) − s(32) off by 1.22×10⁻³ relative, as stated. Repository script rerun at a1de4d9: "all Theorem O checks passed".

## Prior Art

Classical: isotropic tensors / first fundamental theorem for O(d) (Weyl, The Classical Groups); Maxwell stress divergence (Jackson §6.7); Coulomb multipole expansion.

## Novelty Analysis

None. Classical identities applied to the repository's family of readings.

## Falsification Attempts

Attacked the classification (missing ε-tensor terms are excluded by reflection covariance; no third independent quadratic term exists once both factors are symmetrised), the sign of the trace term, and the surface dependence on three off-centre spheres with a different quadrature. No discrepancy.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0039. Mathematical. Hessian reading, the (1,0,0,0) member.
- DISC-0042. Mathematical. Quadratic reading, the (0,0,1,−½) member.
- DISC-0012. Mathematical. Classical Maxwell stress evaluator.
- DISC-0045. Failed hypothesis. The route this closes for the whole family.

## Open Questions

Readings with more than two derivatives, position-dependent coefficients, or undifferentiated Ψ (screened mass term); Ψ_info ≠ A_0; the 0.45 mesh solve (Stage 2 stays OPEN).

## Next Experiments

None from the archive; the open item is the repository's Stage 2 mesh computation.

## Reproduction Instructions

`git checkout a1de4d9cf64fd360075d63f8a0a054871513fb2a && python3 scripts/general_reading_flux.py`. Archive: `python3 /workspace/scratch-ifi/indep_general_O.py`.

## Evidence Log

- 2026-10-08. Recorded from README Theorem O at a1de4d9cf64fd360075d63f8a0a054871513fb2a; script rerun OK; archive checks as above.

## Change History

- 2026-10-08. Initial archive entry.
