# Discovery: Screened polynomial readings leave only surface-dependent mass flux (Theorem T)

## Discovery ID

DISC-0057

## Status

KNOWN

## Date Discovered

2026-10-08 (America/New_York), ~11pm EDT corpus slice. Preempted finite-gasket excess-11 attack when IFI pushed f495b0b during the slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit f495b0bf8d055e0df7581546814a5485af641476 (2026-10-08 23:23:30 -0400). Paths: README.md "Theorem T. Screened polynomial readings leave only surface-dependent mass flux" (Assumption T, T.1–T.4, Proofs, Kept Failure T.1, Witness, NOT THIS); CLAIM_STATUS.md Theorem T row (VERIFIED, not thrust); scripts/screened_reading_flux.py.

## Original Evidence

Same O(3)-covariant constant-coefficient polynomial family as Theorems Q/R under the screened equation (Δ−m²)Ψ=−ρ/ε₀, m>0 fixed. T.1 Yukawa decay: G(S_R)→0 exponentially. T.2 on-shell conserved ⇒ G=0 on every vacuum surface. T.3 otherwise G equals a mass/screening remainder that moves with S and decays. T.4 massless loopholes die: ∮Ψ n and ∮Ψ² n both →0 (kill P.2 growth and R.4 nonzero dilation limit). Witness: seven readings H,Q,Tr,U1,U2,L1,C0; exact Fraction identities 25/25; quadrature at m=0.7 matches recorded G_Q on three spheres; centred decay and off-centre U2 dilation →0.

## Discovery

Classical Yukawa pointwise bounds + divergence theorem + on-shell substitution Δ→m², applied to the repository's polynomial reading family under a screened field equation.

## Why It Matters

It closes the screened gap left open by DISC-0055/0056 inside polynomial readings (see DISC-0058).

## Derivation

Checked. T.1 from Yukawa bounds O(e^{−c|x|}|x|^K). T.2 shell identity + T.1. T.3 exterior integral of on-shell div T; concrete remainders H→m²∂Ψ, Q/U1→m²Ψ∂Ψ, U2→2Ψ∂Ψ, L1→∂Ψ. T.4 immediate from T.1. No gap.

## Assumptions

Assumption T; C5; C6 with Ψ_info=A_0 under screened equation; isolated device; d=3; no m selected as design target.

## New Results

Repository script `scripts/screened_reading_flux.py` at f495b0b: all Theorem T checks passed (exact 25/25; |C0|,|Q−(m²/2)U2|≤8.9e−14; recorded G_Q and dilation figures match README). Archive `/workspace/scratch-ifi/indep_theorem_T.log`: independent sympy identities for div H/Q/C0/U2/L1 and div(Q−(m²/2)U2)=∇Ψ(Δ−m²Ψ) on 25/25 random polys; Yukawa area·amp scales decay with R.

## Prior Art

Classical: Yukawa / Proca decay estimates; divergence theorem; Maxwell-stress and Hessian divergences under (Δ−m²)Ψ=0.

## Novelty Analysis

None. Classical identities applied to the repository's screened polynomial family.

## Falsification Attempts

Attacked off-shell and on-shell divergence formulas, conserved C0/Q−(m²/2)U2 near-zero fluxes, three-sphere surface dependence, centred decay, and off-centre U2 dilation→0. No discrepancy with README figures.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct.

## Patent Relevance

None.

## Related Discoveries

- DISC-0055 / DISC-0056. Mathematical / failed hypothesis. Massless polynomial family (shift / non-shift).
- DISC-0048 / DISC-0049. Linear undifferentiated term (P.2 loophole closed by T.4).
- DISC-0058. Failed hypothesis. Kept Failure T.1.

## Open Questions

Non-polynomial readings; position-dependent coefficients; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN).

## Next Experiments

None from the archive.

## Evidence Log

- 2026-10-08 ~11pm EDT. Repo witness EXIT 0; archive sympy 25/25; pivoted from excess-11 (filter survivors confirmed; directs pending) when f495b0b landed mid-slice.
