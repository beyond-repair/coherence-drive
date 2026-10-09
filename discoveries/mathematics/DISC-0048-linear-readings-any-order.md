# Discovery: Every linear reading of any order reduces to ∮ r(Δ)Ψ n (Theorem P)

## Discovery ID

DISC-0048

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0045.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 9e0fee59ee966cceefa8bc7a88870d25d71e43f8. Paths: README.md "Theorem P. Every linear reading, of any order, reduces to one surface scalar" (Assumption P, Derived classification, Theorem P, Proof, Corollaries 1–4, Witness, NOT THIS) and the updated OPEN bullet; GASKET.md Stage 2 OPEN bullet; CLAIM_STATUS.md new Theorem P row (VERIFIED, not thrust); scripts/linear_reading_flux.py; scripts/cli.py.

## Original Evidence

Inside Assumption P (local, constant-coefficient, linear in Ψ, O(d)-covariant, any finite order), T^{ij} = p(Δ)∂^i∂^jΨ + δ^{ij} q(Δ)Ψ, and with r(s) = s p(s) + q(s), ∂_jT^{ij} = ∂_i r(Δ)Ψ and G_i = ∮_S r(Δ)Ψ n_i dA. Classification witness: O(3)-invariant tensors A^{ij}_{k_1…k_m} symmetric in the k's have dimensions 1, 0, 2, 0, 2 for m = 0..4. Exact box witness on [0,2]×[−1,1]×[0,3]: 40/40 random (p, q, Ψ) satisfy the identity; on a harmonic quintic, 20 shift-invariant readings give G = 0 and δ^{ij}Ψ gives G = (80, 36, 0).

## Discovery

Commutation of constant-coefficient operators plus Theorem M (DISC-0039) applied to Φ = p(Δ)Ψ, plus isotropic-tensor classification. Classical; the repository applies it to the entire linear family of readings of the frozen rank-2 symbol.

## Why It Matters

It closes the linear side of the Stage 2 reading question at every order: adding derivatives to a linear reading cannot create a residual beyond the single surface scalar r(Δ)Ψ (see DISC-0049 for what that leaves under static massless C6).

## Derivation

Checked. p(Δ)∂_i∂_jΨ = ∂_i∂_jΦ; Theorem M gives ∮∂_i∂_jΦ n_j = ∮ΔΦ n_i; the δ-term contributes ∮q(Δ)Ψ n_i. Classification: −I ∈ O(d) kills odd m; for even m, delta products contracted with symmetric derivatives leave only δ^{ij}Δ^{m/2}Ψ and ∂^i∂^jΔ^{m/2−1}Ψ (the antisymmetric-in-k pairing drops out). ε-tensor terms are excluded by reflection covariance. No gap.

## Assumptions

Assumption P (a family of readings, not a change to the freeze); Ψ ∈ C^{2D+3} near S; d = 3 for the witness and corollaries.

## New Results

Archive `/workspace/scratch-ifi/indep_linear_P.py`: sympy divergence residual for degree ≤ 2 symbolic p, q and generic Ψ is (0, 0, 0); invariant-tensor null spaces over random orthogonal matrices (with reflections) plus k-symmetrisation give 1, 0, 2, 0, 2 for m = 0..4; exact box integral of ∇Ψ for the harmonic quintic gives (80, 36, 0); own quadrature (200–400 Gauss–Legendre in cos θ by 400–800 azimuthal nodes, own ellipsoid parametrisation) reproduces all three charged-sphere values, the four dilation magnitudes 30.584623, 54.991733, 104.759332, 204.860214, the neutral sphere value (equal to (4π/3)·dipole on two different spheres), and both ellipsoid values to the printed decimals. Repository script rerun at 9e0fee5: "all Theorem P checks passed".

## Prior Art

Classical: isotropic tensors / first fundamental theorem for O(d) (Weyl, The Classical Groups); divergence theorem; commuting constant-coefficient operators; electrostatic ∫_V E over a region containing charges (Jackson §4.1 and the sphere-average theorem).

## Novelty Analysis

None. Classical identities applied to the repository's linear family of readings.

## Falsification Attempts

Attacked the classification count (missing pseudotensor terms, antisymmetric pairings), the divergence formula at six derivatives, and every recorded quadrature figure with an independent integrator and an independent ellipsoid parametrisation. No discrepancy.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0039. Mathematical. Theorem M, the p = 1, q = 0 member and the lemma used in the proof.
- DISC-0044. Mathematical. Theorem O's linear part is p = a, q = bs.
- DISC-0049. Failed hypothesis. The route this closes for all linear readings.

## Open Questions

Nonlinear readings with more than two derivatives (the repository's later Theorems Q and R, not indexed in this pass); position-dependent coefficients; Ψ_info ≠ A_0; the 0.45 mesh solve (Stage 2 stays OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 9e0fee59ee966cceefa8bc7a88870d25d71e43f8 && python3 scripts/linear_reading_flux.py`. Archive: `python3 /workspace/scratch-ifi/indep_linear_P.py`.

## Evidence Log

- 2026-10-08. Recorded from README Theorem P at 9e0fee59ee966cceefa8bc7a88870d25d71e43f8; script rerun OK; archive checks as above. Repository description still matches its claim fence.

## Change History

- 2026-10-08. Initial archive entry.
