# Discovery: Quadratic reading turns the closed-surface flux into ∫ ∂_iΨ ΔΨ (Theorem N)

## Discovery ID

DISC-0042

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0039.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 20e45cdb6b1bc16bff4739cc45ccba92fd446e33. Paths: README.md "Theorem N" (Assumption N, Theorem, Proof, Corollaries 1–2, Witness, NOT THIS) and the updated OPEN bullet in "What was tried and does not follow"; CLAIM_STATUS.md quadratic-reading row; GASKET.md Stage 2 OPEN bullet; scripts/quadratic_flux_reduction.py.

## Original Evidence

Under (∇Ψ)^{ij} = Q^{ij} = ∂^iΨ ∂^jΨ − ½δ^{ij}|∇Ψ|², ∂_jQ^{ij} = ∂_iΨ ΔΨ, so G_i = ∮_S Q^{ij} n_j dA = ∫_V ∂_iΨ ΔΨ dV. Witness: Ψ = x³ on [0,2]×[−1,1]×[0,3] gives G_x = 432; harmonic Ψ = x³ − 3xy² + 2yz gives G = 0 with x-row faces 907/5, 173/5, −90, −126.

## Discovery

The classical divergence identity of the electrostatic (Maxwell) stress tensor, div(EE − ½|E|²I) = E div E, applied to the repository's second reading of the frozen rank-2 symbol.

## Why It Matters

With DISC-0039 (Hessian reading) it covers both readings the repository has named; under both, static massless C6 on a vacuum surface gives no residual (DISC-0040, DISC-0043).

## Derivation

Product rule plus divergence theorem, as in the README. Checked.

## Assumptions

Assumption N (a reading, not a change to the freeze); Ψ ∈ C²(V̄), V bounded Lipschitz.

## New Results

Archive `/workspace/scratch-ifi/indep_quadratic_N.py` (sympy, exact): symbolic residual of ∂_jQ^{ij} − ∂_iΨ ΔΨ is 0 for a general Ψ; Ψ = x³ gives volume and surface G_x = 432; the harmonic Ψ_H gives every row of G equal to 0, with x-row faces (x = 2: 907/5, x = 0: 173/5, y = 1: −90, y = −1: −126, z: 0, 0), all as stated. Repository script rerun at 20e45cd: all Theorem N checks passed. Minor: README quotes the isolated-cluster |G| as 3.0×10⁻¹⁴, the rerun prints 1.98×10⁻¹⁴; both are floating-point zero, not a discrepancy of substance.

## Prior Art

Classical: the Maxwell stress tensor and its divergence (any electromagnetism text, e.g. Jackson §6.7); the screened variant is the static Proca/Yukawa stress.

## Novelty Analysis

None. Classical identity applied to the repository's symbol.

## Falsification Attempts

Checked sign conventions and the face bookkeeping exactly on an independent sympy build; no discrepancy.

## Experimental Validation

None.

## Mathematical Status

Classical identity; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0039. Mathematical. The Hessian-reading counterpart (Theorem M).
- DISC-0012. Mathematical. Classical Maxwell stress evaluator; Theorem N says the quadratic reading of the informational tensor is that same stress over ε₀ when Ψ = A_0.
- DISC-0043. Failed hypothesis. The route this closes.

## Open Questions

Readings other than Hessian and quadratic; Ψ_info ≠ A_0; the 0.45 mesh solve (Stage 2 stays OPEN).

## Next Experiments

None from the archive; the open item is the repository's Stage 2 mesh computation.

## Reproduction Instructions

`git checkout 20e45cdb6b1bc16bff4739cc45ccba92fd446e33 && python3 scripts/quadratic_flux_reduction.py`. Archive: `python3 /workspace/scratch-ifi/indep_quadratic_N.py`.

## Evidence Log

- 2026-10-08. Recorded from README Theorem N at 20e45cdb6b1bc16bff4739cc45ccba92fd446e33; script rerun OK; archive sympy check as above.

## Change History

- 2026-10-08. Initial archive entry.
