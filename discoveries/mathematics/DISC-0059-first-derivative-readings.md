# Discovery: First-derivative readings (non-polynomial allowed) stay zero or surface-dependent (Theorem U)

## Discovery ID

DISC-0059

## Status

KNOWN

## Date Discovered

2026-10-09 (America/New_York), ~12:08am EDT corpus slice. Preferential unread: IFI commit 769f963 landed; finite-gasket excess-11 directs remain pending (lower priority).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 769f963041764d8466d52c81ea744400422c578a (2026-10-09 00:06:32 -0400). Paths: README.md "Theorem U. First-derivative readings (non-polynomial allowed) are still zero or surface-dependent" (Assumption U, U.1–U.4, Proofs, Kept Failure U.1, Witness, NOT THIS); CLAIM_STATUS.md Theorem U row (VERIFIED, not thrust); GASKET.md Stage-2 OPEN bullet update; scripts/first_derivative_reading_flux.py; scripts/cli.py.

## Original Evidence

Family: every O(3)-covariant C¹ reading T^{ij}=f(s)δ^{ij}+g(s)∂^iΨ∂^jΨ with s=|∇Ψ|² (non-polynomial f,g allowed; affine recovers Theorem O). U.1 divergence formula. U.2 on-shell conserved iff g'≡0 and f'+g/2≡0, i.e. T=κδ+cQ. U.3 conserved ⇒ G=0 on every vacuum surface. U.4 otherwise G=−∫_{outside} div T, surface-dependent, O(R^{−2}). Maxwell removal leaves 0 or that remainder. Witness: exact 40/40 poly identities; 25/25 affine Maxwell+κ; FD non-poly (e^{−s}, 1/(1+s), exp-weighted); quadrature three spheres; dilation R²G leading coefficients.

## Discovery

Classical isotropic tensor representation for one vector + chain-rule divergence + multipole decay, applied to the repository's first-derivative reading family (polynomial gap of Q–T closed for this class).

## Why It Matters

It closes the non-polynomial first-derivative gap left open by Theorems Q–T (see DISC-0060).

## Derivation

Checked. U.1 by differentiating T. U.2: on-shell formula vanishes iff both coefficient functions vanish; harmonic jet x²−y² separates them; integrate. U.3 from U.2 + Kept Failure N.1. U.4: f(0)δ flux vanishes; remainder O(R^{−4}) on S_R ⇒ flux O(R^{−2}); exterior shell identity. No gap.

## Assumptions

Assumption U; C5; static massless C6 with Ψ_info=A_0; isolated device; d=3; vacuum surfaces; no design parameter selected.

## New Results

Repository script `scripts/first_derivative_reading_flux.py` at 769f963: all Theorem U checks passed (EXIT 0; archive `/workspace/scratch-ifi/repo_theorem_U.log`). Archive `/workspace/scratch-ifi/indep_theorem_U.log` (+ script indep_theorem_U.py): independent sympy U.1 residuals 0/0/0 on cubic harmonic; Maxwell crit (0,0); exp-Maxwell-ish (f'+g/2=0, g'≠0) not conserved; FD non-poly rel_err ≤4.5e−6; affine Maxwell+κ conserved; 20/20 random affine formula matches.

## Prior Art

Classical: representation of isotropic tensor functions of one vector; Maxwell-stress divergence; Coulomb multipole decay.

## Novelty Analysis

None. Classical identities applied to the repository's first-derivative family.

## Falsification Attempts

Attacked U.1 identity, conservation criterion (including the g'≠0 counterexample with f'+g/2=0), affine Maxwell+κ conservation, and FD match for three non-polynomial pairs. No discrepancy with README figures (repo witness also locked recorded fluxes).

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct. Classified KNOWN (not THEOREM elevation): continuum reduction matching Q–T pattern.

## Patent Relevance

None.

## Related Discoveries

- DISC-0044 / DISC-0045. Mathematical / failed hypothesis. Affine (quadratic/trace) subfamily.
- DISC-0053–DISC-0058. Polynomial family (shift / non-shift / screened).
- DISC-0060. Failed hypothesis. Kept Failure U.1.

## Open Questions

Non-polynomial dependence on undifferentiated Ψ or higher derivatives; nonlocal kernels; position-dependent coefficients; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN).

## Next Experiments

None from the archive.

## Evidence Log

- 2026-10-09 ~12:10am EDT. Repo witness EXIT 0; indep sympy+FD PASS. Excess-11 side note only: repo direct k=75 (p=64,m=11) S=0=0; p=32/p=128 directs still running; DISC-0030 unchanged.
