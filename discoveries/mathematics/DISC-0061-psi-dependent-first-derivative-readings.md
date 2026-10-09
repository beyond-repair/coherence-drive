# Discovery: Ψ-dependent first-derivative isotropic readings stay Maxwell or surface-dependent (Theorem V)

## Discovery ID

DISC-0061

## Status

KNOWN

## Date Discovered

2026-10-09 (America/New_York), ~1:35am EDT corpus slice. Preferential unread: IFI commits 7f561c9…87aa103 (Theorem V) landed after Theorem U; finite-gasket excess-11 directs remain pending (lower priority this slice).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 87aa1030b701bf1258f7d44af373e21b6e559c85 (docs tip; witness introduced at 7f561c9f9b69f5d9b598ebf29363dc9fdb028563, 2026-10-09 01:14–01:22 -0400). Paths: README.md "Theorem V. Ψ-dependent first-derivative isotropic readings stay Maxwell or surface-dependent" (Assumption V, V.1–V.4, Proofs, Kept Failure V.1, Witness, NOT THIS); CLAIM_STATUS.md Theorem V row (VERIFIED, not thrust); GASKET.md Stage-2 OPEN bullet update; scripts/psi_gradient_reading_flux.py; scripts/cli.py; scripts/apply_theorem_v_docs.py.

## Original Evidence

Family: every O(3)-covariant C¹ reading T^{ij}=f(Ψ,s)δ^{ij}+g(Ψ,s)∂^iΨ∂^jΨ with s=|∇Ψ|² (undifferentiated Ψ allowed; Theorem U is the Ψ-independent slice). V.1 divergence formula. V.2 on-shell conserved iff g_s≡0, f_s+g/2≡0, and f_Ψ+s g_Ψ≡0, which integrates to T=κδ+cQ (same conserved class as U). V.3 conserved ⇒ G=0 on every vacuum surface. V.4 otherwise G=−∫_{outside} div T, surface-dependent; exp(−Ψ²)δ recovers the R.4 limit; pseudo-Maxwell and soft remainders decay. Maxwell removal leaves 0 or that remainder. Witness: exact 40/40 poly identities; 25/25 affine Maxwell+κ; FD non-poly; quadrature three spheres; dilation.

## Discovery

Classical isotropic tensor representation for one scalar and one vector + chain-rule divergence + multipole / R.4 asymptotics, applied to the repository's Ψ+∇Ψ first-derivative isotropic family (closes the undifferentiated-Ψ gap left by Theorem U).

## Why It Matters

It closes the Ψ-dependent first-derivative isotropic gap left open by Theorem U (see DISC-0062). Ψ-dependence does not enlarge the conserved class beyond Maxwell+κδ.

## Derivation

Checked. V.1 by differentiating T (identity ∂_j E^i E^j = ½∂_i s). V.2: on-shell formula vanishes iff three coefficient functions vanish; integrate g=g(Ψ), f=−(g/2)s+h(Ψ), then h'+(g'/2)s≡0 for all s forces g'≡h'≡0. V.3 from V.2 + Kept Failure N.1. V.4: shell identity + bump argument of Q.3; R.4 caveat for even undifferentiated powers. No gap.

## Assumptions

Assumption V; C5; static massless C6 with Ψ_info=A_0; isolated device; d=3; vacuum surfaces; no design parameter selected.

## New Results

Repository script `scripts/psi_gradient_reading_flux.py` at 87aa103: Part 0–2 and lock figures pass; one dilation rate check FAIL on soft E⊗E/(1+Ψ²) at R=4→8 (ratio 0.658 vs threshold 0.6) while |G_soft| still →0 with later ratios ~0.25–0.27 (archive `/workspace/scratch-ifi/repo_theorem_V.log`, EXIT 1). Archive `/workspace/scratch-ifi/indep_theorem_V.log`: independent sympy V.1 residual 0 on generic degree-≤2 poly f,g of (Ψ,s); Maxwell+κ div=0 on x, x²−y², xyz; pseudo-Maxwell on-shell div=(s/2)E exactly; integration coeffs force g',h'=0.

## Prior Art

Classical: representation of isotropic tensor functions of one scalar and one vector; Maxwell-stress divergence; Coulomb multipole decay; R.4 surface-dependent Ψ²δ limit (already in Theorem R).

## Novelty Analysis

None. Classical identities applied to the repository's Ψ-dependent first-derivative isotropic family.

## Falsification Attempts

Attacked V.1 identity, conservation criterion (including pseudo-Maxwell and pseudo-exp-Maxwell with f_s+g/2=g_s=0 but f_Ψ+s g_Ψ≠0), Maxwell+κ conservation, three-sphere surface dependence, and exterior-integral match. Soft dilation early-step rate flake noted; asymptotic decay and |G|→0 still hold. No contradiction with the theorem statement.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct. Classified KNOWN (not THEOREM elevation): continuum reduction matching Q–U pattern.

## Patent Relevance

None.

## Related Discoveries

- DISC-0059 / DISC-0060. Mathematical / failed hypothesis. Ψ-independent first-derivative family (Theorem U).
- DISC-0053–DISC-0058. Polynomial family (shift / non-shift / screened).
- DISC-0062. Failed hypothesis. Kept Failure V.1.

## Open Questions

Higher-derivative non-polynomial readings; nonlocal kernels; position-dependent coefficients; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN).

## Next Experiments

None from the archive.

## Evidence Log

- 2026-10-09 ~1:35am EDT. Repo witness mostly PASS (1 soft-rate flake); indep sympy PASS. Excess-11 side note: repo directs p=16 S=0=0 done; p=32/128/256 still running; DISC-0030 unchanged.
