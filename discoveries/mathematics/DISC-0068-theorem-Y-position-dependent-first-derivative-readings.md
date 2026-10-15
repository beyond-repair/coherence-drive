# Discovery: Position-dependent first-derivative isotropic readings stay Maxwell or surface-dependent (Theorem Y)

## Discovery ID

DISC-0068

## Status

KNOWN

## Date Discovered

2026-10-15 (America/New_York), ~1:00am EDT corpus slice. Preferential unread: IFI commit 391de98 (Theorem Y) landed after Theorem X (3959241, indexed in the same pass as DISC-0065..0067).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 391de98090da5e55b8e19e59ca63aef5db9122f3 (2026-10-15 00:04:25 -0400). Paths: README.md "Theorem Y. Position-dependent first-derivative isotropic readings stay Maxwell or surface-dependent" (Assumption Y, Y.1–Y.4, Proofs, Kept Failure Y.1, Witness, NOT THIS); README.md Stage-2 OPEN bullet update; CLAIM_STATUS.md Theorem Y row (VERIFIED, not thrust) and Theorem V row cross-reference; scripts/position_dependent_reading_flux.py; scripts/cli.py.

## Original Evidence

Family: every C¹ reading T^{ij}=f(x,Ψ,s)δ^{ij}+g(x,Ψ,s)∂^iΨ∂^jΨ with s=|∇Ψ|² and explicit position dependence allowed (Theorem V is the x-independent slice). Y.1 divergence formula = V.1 plus ∂_{x_i}f + (∇_x g·E)E^i. Y.2 on-shell conserved iff the three V identities hold pointwise in x and the explicit-gradient identity ∇_x h − ½(∇_x g)|E|² + (∇_x g·E)E ≡ 0 holds; E=0 forces ∇h=0, then E⊥∇g forces ∇g=0, so T=κδ+cQ with constants (same conserved class as U/V). Y.3 conserved ⇒ G=0 on every vacuum surface. Y.4 otherwise G=−∫_{outside} div T where it decays, and surface-dependent in every case; a(x)Q, a(x)δ with nonconstant a are never conserved; x·δ gives the exact identity G=Vol(V)e_x; soft a=1/(1+|x|²) times δ has a nonzero but offset-dependent dilation limit (R.4 sibling); soft aQ and Gaussian readings decay. Witness: exact 40/40 polynomial identities, 25/25 affine Maxwell+κ; FD non-poly; three-sphere quadrature; x·δ volume identity; Maxwell removal; dilation.

## Discovery

Classical chain-rule divergence of an isotropic tensor of one scalar and one vector, plus the harmonic-jet (Ψ, E, traceless H independent) argument and an even/odd split in E, applied to the repository's position-dependent first-derivative isotropic family. Position dependence does not enlarge the conserved class beyond constant Maxwell+κδ.

## Why It Matters

It closes the position-dependent first-derivative isotropic gap left open by Theorem V (see DISC-0069). It does not reopen Theorem E: a variable C5 weight W(x) is a different object from a position-dependent reading coefficient. Not thrust.

## Derivation

Checked. Y.1 by direct differentiation (∂_j E^iE^j = ½∂_i s + E^iΔΨ). Y.2: on-shell the H-carrying terms (f_s+g/2)·2HE + g_s E(E·2HE) vanish for all traceless H ⇒ g_s≡0, f_s+g/2≡0 pointwise in x; integrate g=g(x,Ψ), f=−(g/2)s+h(x,Ψ); the H-free remainder splits into an even part ∇_x h − ½s∇_x g + (∇_x g·E)E and an odd part (h_Ψ+½s g_Ψ)E, each zero; odd ⇒ g_Ψ=h_Ψ=0; even with E=0 ⇒ ∇h=0, with E⊥∇g (or E=∇g, giving ½|∇g|²∇g) ⇒ ∇g=0. Y.3 from Y.2 + Kept Failure N.1. Y.4: shell identity + bump argument of Q.3; divergence theorem on V when the exterior does not decay (x·δ). No gap.

## Assumptions

Assumption Y; C5; static massless C6 with Ψ_info=A_0; isolated device inside an open ball; A_0→0 at infinity; d=3; vacuum surfaces; no design parameter selected.

## New Results

Repository script `scripts/position_dependent_reading_flux.py` at 391de98: all Part 0–2, x·δ volume identity, Maxwell removal, dilation, and locked-figure checks pass, EXIT 0 (archive `/workspace/scratch-ifi/repo_theorem_Y.log`). Archive `/workspace/scratch-ifi/indep_theorem_Y.py` / `indep_theorem_Y.log` (ARCHIVE_INDEP_THEOREM_Y_PASS; does not import the repo script): Y.1 formula equals the direct divergence for 9/9 generic non-polynomial (Ψ, f(x,Ψ,s), g(x,Ψ,s)) triples at 3 rational points to 40 digits; div(aQ)=(E·∇a)E−(s/2)∇a+aEΔΨ and div(aδ)=∇a identically for undefined sympy a(x), Ψ(x); Y.2 collapse (E=0 ⇒ ∇h; E=∇g ⇒ ½|∇g|²∇g); Maxwell+κδ conserved 25/25 on x³−3xy²+2yz, 9/9 on the Theorem Q Ψ_h, and on the Coulomb cluster; soft/Gaussian aQ and aδ not on-shell conserved; div(xQ) at (1,½,−1) = (−2031/32, −253/8, 33/8) matches the repo; own 160×320 quadrature reproduces every README three-sphere flux to ≤4.4e−11 (Maxwell |G|≤6e−14), soft aδ surface flux = ∫_V∇a by 3-D quadrature (≤7e−14); ∮x n dA = (4π/3)R³e_x symbolically on any sphere; soft aδ dilation limit in closed form 2π[1/ρ − (1+ρ²)/(2ρ²)·ln((1+ρ)/(1−ρ))]ĉ = −3.3278ĉ for ρ=|C1| (repo R=64 value 3.3258, R=32 3.3198, converging), offset-direction dependent; soft aQ dilation decays; Maxwell removal from Q+aδ leaves exactly the aδ flux. Two failures on the first independent run were checker bugs (sp.Integer(1/2) truncation; a different harmonic Ψ used for the spot value), fixed before the PASS; no repository discrepancy.

## Prior Art

Classical: representation of isotropic tensor functions of one scalar and one vector; chain-rule divergence; Maxwell-stress divergence; Coulomb multipole decay; R.4 surface-dependent limit (already in Theorem R / DISC-0055); harmonic jets realise arbitrary (Ψ, ∇Ψ, traceless Hessian) at a point. No prior-art comparison in the repository warrants THEOREM elevation; none invented here.

## Novelty Analysis

None. Classical identities applied to the repository's position-dependent first-derivative isotropic family (same pattern as DISC-0059 / DISC-0061).

## Falsification Attempts

Attacked the Y.1 identity with non-polynomial x-, Ψ-, and s-dependence on harmonic and non-harmonic Ψ; the Y.2 collapse (E=0 and E=∇g choices); Maxwell+κ conservation with non-integer c; non-conservation of soft/Gaussian a(x); three-sphere surface dependence with an independent grid and a volume-integral cross-check; the x·δ exact identity symbolically; the soft aδ dilation limit in closed form. No contradiction with the theorem statement.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct. Classified KNOWN (not THEOREM elevation): continuum reduction matching the Q–V pattern.

## Patent Relevance

None.

## Related Discoveries

- DISC-0061 / DISC-0062. Mathematical / failed hypothesis. Ψ-dependent x-independent slice (Theorem V).
- DISC-0059 / DISC-0060. Ψ-independent first-derivative family (Theorem U).
- DISC-0055. R.4 surface-dependent limit (soft aδ dilation is a sibling).
- DISC-0069. Failed hypothesis. Kept Failure Y.1.

## Open Questions

Higher-derivative non-polynomial readings; nonlocal kernels; pseudotensor contractions; time-dependent fields; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN). Claim ceiling unchanged.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 391de98090da5e55b8e19e59ca63aef5db9122f3 && python3 scripts/position_dependent_reading_flux.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_Y.log`, `/workspace/scratch-ifi/indep_theorem_Y.log`.

## Evidence Log

- 2026-10-15 ~1:00am EDT. Repo witness EXIT 0; independent check ARCHIVE_INDEP_THEOREM_Y_PASS. Repository description still matches its claim fence. Excess-11 side note: finite-gasket direct p=256 still running; DISC-0030 unchanged (CONJECTURE).

## Change History

- 2026-10-15. Initial archive entry.
