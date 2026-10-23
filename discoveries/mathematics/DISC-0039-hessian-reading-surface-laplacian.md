# Discovery: Under the Hessian reading, the closed-surface flux sees only ΔΨ on the surface

## Discovery ID

DISC-0039

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Archive pass, same run as DISC-0038.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 5d931cf0eaca893135c92198de3dd81989629a4c. Paths: README.md "Theorem M. Under the Hessian reading, G sees only ΔΨ on the surface" (Assumption M, Theorem M continuum, Corollaries 1 and 3, Theorem M discrete, Witness, NOT THIS); CLAIM_STATUS.md row "Hessian reading … VERIFIED (Theorem M, Kept Failure M.1)"; GASKET.md Stage 2 OPEN bullet; scripts/hessian_flux_reduction.py; scripts/cli.py (reproduce list, now 8 scripts).

## Original Evidence

Continuum proof (cutoff χ near S, divergence theorem twice) and an exact integer discrete version on the Theorem A rectangle, with a witness script on an 8×8 grid: 200 seeded random potentials; a lopsided interior lump with ΔP = 0 on the boundary layers gives summed |cell div| 398 / 422 and G = (0, 0); P = x³ gives G = (384, 0) = (6 N_x N_y, 0); a discrete screened column gives G_x = 8.

## Discovery

If (∇Ψ)^{ij} is read as the Hessian ∂^i∂^jΨ, then for any bounded Lipschitz V with Ψ ∈ C³ near S = ∂V, G_i = ∮_S ∂_i∂_jΨ n_j dA = ∮_S ΔΨ n_i dA, whatever Ψ does inside V. Discretely, with forward differences and the five-point Laplacian, G_x = Σ_y (ΔP_{N_x,y} − ΔP_{0,y}) and G_y likewise, exactly on integers. If ΔΨ = 0 on S then G = 0; if (Δ − m²)Ψ = 0 on S then G_i = m² ∮ Ψ n_i dA.

## Why It Matters

It narrows the repository's open Stage 2 question, under one reading of the frozen rank-2 symbol, to a single boundary quantity (ΔΨ_info on the enclosing surface). It is the basis of the rejected route DISC-0040. It is not thrust, and the repository says so.

## Derivation

Continuum: ∂_j(∂_i∂_jΨ) = ∂_iΔΨ (mixed partials commute for C³), then the divergence theorem on V for the cutoff Φ = χΨ, which equals Ψ to third order on S. Discrete: cell divergence of row i is Δ(D_iP) = D_i(ΔP) (constant-coefficient differences commute), Theorem A (DISC-0001) turns flux into the cell sum, and Σ D_iΔP telescopes in direction i. Both checked line by line; no gap.

## Assumptions

Assumption M (Hessian reading). The quadratic reading ∂^iΨ∂^jΨ − ½δ^{ij}|∇Ψ|² is not covered. No W, χ_vac, or κ enters. Stage 1 untouched.

## New Results

Archive-side independent checks (2026-10-08), not using repository code:
- sympy: div(Hess f) = grad(Δf) symbolically for a generic f(x, y, z).
- Unit sphere, Ψ = x³ + xy² + zx²: quadrature of ∮ ∂_i∂_jΨ n_j and of ∮ ΔΨ n_i agree, G = (32π/3, 0, 8π/3) ≈ (33.510322, 0, 8.377580) (Laplacian-side quadrature error about 3·10^{−5} at the poles).
- numpy: the discrete identity holds on 300 random integer potentials on non-square grids 5×9, 11×3, 7×7.
- Repository witness rerun at 5d931cf: scripts/hessian_flux_reduction.py exit 0, integers 398, 422, 384, 8 as recorded.
- Archive remark (immediate from the theorem, not a repository statement): only the non-constant part of ΔΨ on S matters, since ∮ n_i dA = 0; a constant nonzero ΔΨ on S also gives G = 0.

## Prior Art

Classical: the divergence of the Hessian is the gradient of the Laplacian, and the boundary form follows from the divergence theorem (any vector-calculus text); the discrete form is summation by parts. The repository states no novelty and calls it a reduction.

## Novelty Analysis

KNOWN mathematics applied to the repository's frozen symbol. Not a novelty candidate.

## Falsification Attempts

Proof read; independent symbolic, continuum-quadrature, and discrete-grid checks. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proved (classical identity).

## Patent Relevance

None.

## Related Discoveries

- DISC-0001. Mathematical. Theorem A, used for the discrete version.
- DISC-0040. Failed hypothesis. The static massless route it rules out.
- DISC-0031. Mathematical. GASKET.md Stage 2 OPEN bullet now cites Theorem M.
- DISC-0044. Mathematical. Theorem O (a1de4d9) puts this reading inside the four-parameter two-derivative family.

## Open Questions

The quadratic (Maxwell-like) reading, and ΔΨ_info on the frozen 0.45 mesh (repository: OPEN).

## Next Experiments

Repeat the reduction for the quadratic reading: ∂_j(∂_iΨ∂_jΨ − ½δ_{ij}|∇Ψ|²) = ∂_iΨ ΔΨ, so its flux equals ∫_V ∂_iΨ ΔΨ, which is a volume (not surface-only) quantity.

## Reproduction Instructions

Repository: `git checkout 5d931cf0eaca893135c92198de3dd81989629a4c && python3 scripts/hessian_flux_reduction.py`. Archive: indep_hessian.py in the archive box scratch /workspace/scratch-ifi (sympy + numpy).

## Evidence Log

- 2026-10-08. Recorded from README / CLAIM_STATUS / GASKET.md at 5d931cf0eaca893135c92198de3dd81989629a4c; proofs verified; repository witness rerun OK; archive checks as above.

## Change History

- 2026-10-08. Initial archive entry.
