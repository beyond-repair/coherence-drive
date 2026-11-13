# Discovery: Pseudotensor (hemitropic) first-derivative readings stay Maxwell, a boundary-only curl, or surface-dependent (Theorem Z)

## Discovery ID

DISC-0070

## Status

KNOWN

## Date Discovered

2026-10-15 (America/New_York), ~2:00am EDT corpus slice. Preferential unread: IFI commit 1282986 (Theorem Z) landed after Theorem Y (391de98, indexed as DISC-0068..0069).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 1282986d667c7ff87164deca5a7834819d1f3555 (2026-10-15 01:07:42 -0400). Paths: README.md "Theorem Z. Pseudotensor (hemitropic) first-derivative readings stay Maxwell, a boundary-only curl, or surface-dependent" (Assumption Z, Z.1–Z.4, Proofs, Kept Failure Z.1, Witness, NOT THIS); README.md Theorem Y NOT THIS cross-reference and Stage-2 OPEN bullet update; CLAIM_STATUS.md Theorem Z row (VERIFIED, not thrust); scripts/hemitropic_reading_flux.py; scripts/cli.py.

## Original Evidence

Family: every C¹ reading T^{ij}=f(x,Ψ,s)δ^{ij}+g(x,Ψ,s)∂^iΨ∂^jΨ+h(x,Ψ,s)ε^{ijk}∂_kΨ, s=|∇Ψ|² (SO(3)-covariant; Theorem Y is the h=0 slice). Z.1: ∂_j(hε^{ijk}E_k)=(∇_x h×E)^i+2h_s(HE×E)^i, no ΔΨ term. Z.2: on-shell conserved iff h_s≡0, ∇_x h≡0, and the Y.2 conditions, so T=κδ+cQ+ε·∇K(Ψ), K′=h. Z.3: ∮_S n×∇K(Ψ) dA=0 on every closed Lipschitz surface where Ψ is C², whatever is inside. Z.4: otherwise G moves with the surface; for h=h(x) alone ∮h n×∇Ψ=−∮Ψ n×∇h, and for h=x_m this is e_m×∮Ψn = (4π/3)e_m×p_c on spheres enclosing the device (the P.2 flux rotated). Witness: sympy 30/30 Z.1 identities; four h(Ψ) divergence-free; rank-3 map H↦HE; three-sphere quadrature; split sphere; exterior-integral match; dilation; x ε·E closed form at R up to 200.

## Discovery

Classical: the hemitropic representation of a second-order tensor function of one scalar and one vector (δ, E⊗E, ε·E), the curl-of-gradient identity, and ∮n×∇φ dA=0 on closed surfaces, applied with the harmonic-jet / even-odd argument of Y.2 to the repository's first-derivative family. Allowing pseudotensor contractions enlarges the conserved class only by a boundary-only curl whose closed-surface flux is zero.

## Why It Matters

It closes the pseudotensor first-derivative gap listed in Theorem Y's NOT THIS (see DISC-0071). It does not decide whether a parity-odd reading is physically admissible. Not thrust.

## Derivation

Checked line by line. Z.1: ε^{ijk}∂_j∂_kΨ=0, chain rule ∂_jh=∂_{x_j}h+h_ΨE_j+h_s∂_js, ∇s=2HE, E×E=0. Z.2: H-carrying terms are 2(f_s+g/2)v+2g_s(E·v)E+2h_s v×E with v=HE ranging over ℝ³ (E≠0); v⊥E gives f_s+g/2=0 and h_s=0, v=E gives g_s=0; the H-free remainder splits under E↦−E into the even Y.2 identity (∇_x k=∇_x g=0) and the odd part (k_Ψ+½s g_Ψ)E+∇_x h×E (k_Ψ=g_Ψ=0, ∇_x h=0). Z.3: (n×∇K)_i=n·∇×(K e_i), cutoff and divergence theorem; no interior regularity used. Z.4: bump argument of Q.3; Stokes on hΨ; ℓ=1 sphere moment ∮n/|y−a| dA=(4π/3)(a−c). No gap. Minor: on a disconnected open domain "constant" means locally constant; does not affect the conclusion on the stated surfaces.

## Assumptions

Assumption Z; C5; static massless C6 with Ψ_info=A_0; isolated device inside an open ball; A_0→0 at infinity; d=3; vacuum surfaces; no design parameter selected.

## New Results

Repository script `scripts/hemitropic_reading_flux.py` at 1282986: all checks pass, "all Theorem Z checks passed; nothing here is thrust", EXIT 0 (archive `/workspace/scratch-ifi/repo_theorem_Z.log`). Archive `/workspace/scratch-ifi/indep_theorem_Z.py` / `indep_theorem_Z.log` (ALL PASS; does not import the repo script): Z.1 total-derivative form equals the direct divergence for undefined sympy h(x,y,z,Ψ,s) and undefined Ψ(x,y,z) (no ΔΨ term, off shell); ε·∇K(Ψ) divergence-free for undefined K, Ψ; own randomly rotated 160 Gauss–Legendre × 320 offset-azimuth grid on the README cluster q=(3,−1,2): Ψ, e^{−Ψ}, sin Ψ times ε·E give |G|≤9.4e−14 on the three vacuum spheres and 3.5e−14 on the split sphere around q=3; s ε·E reproduces all three README vectors to <1e−9 and equals minus the exterior integral of 2HE×E (own radial quadrature) to <1e−9; x ε·E equals the own closed form (4π/3)e_x×p_c on all three spheres. Extra attack: |x|²ε·E gives exactly 2c×(4π/3)p_c (zero on the origin-centred sphere, nonzero and different on the two offset spheres), another centre-dependent flux. No repository discrepancy.

## Prior Art

Classical: hemitropic/isotropic tensor-function representation theorems (Wang, Smith); ∇×∇=0 and the closed-surface curl theorem ∮n×F dA=∫∇×F dV; Coulomb multipole moments; P.2 surface flux (already DISC-0049). No prior-art comparison in the repository warrants THEOREM elevation; none invented here.

## Novelty Analysis

None. Classical identities applied to the repository's pseudotensor first-derivative family (same pattern as DISC-0059 / DISC-0061 / DISC-0068).

## Falsification Attempts

Attacked the Z.1 identity with fully generic (undefined) h and Ψ off shell; the Z.2 linear-map step (v and v×E orthogonal and nonzero for v⊥E); boundary-only curl vanishing on a split sphere through the device region; surface dependence of s ε·E with an independent rotated grid and an exterior-integral cross-check; the x ε·E closed form; a nonlinear position-dependent h=|x|². No contradiction with the theorem statement.

## Experimental Validation

None.

## Mathematical Status

Classical results; proof correct. Classified KNOWN (not THEOREM elevation): continuum reduction matching the Q–Y pattern.

## Patent Relevance

None.

## Related Discoveries

- DISC-0068 / DISC-0069. Theorem Y (h=0 slice).
- DISC-0061 / DISC-0062, DISC-0059 / DISC-0060. Earlier first-derivative slices (Theorems V, U).
- DISC-0049. P.2 undifferentiated-reading flux; x_m ε·∇Ψ reduces to it.
- DISC-0071. Failed hypothesis. Kept Failure Z.1.

## Open Questions

Higher-derivative non-polynomial readings; nonlocal kernels; time-dependent fields; Ψ_info ≠ A_0; physical admissibility of parity-odd readings; Stage 2 0.45 mesh (still OPEN). Claim ceiling unchanged.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 1282986d667c7ff87164deca5a7834819d1f3555 && python3 scripts/hemitropic_reading_flux.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_Z.log`, `/workspace/scratch-ifi/indep_theorem_Z.log`.

## Evidence Log

- 2026-10-15 ~2:00am EDT. Repo witness EXIT 0; independent check ALL PASS. Repository description still matches its claim fence. Finite-gasket side note: HEAD 92ad7bd records excess-11 directs through p=128 (S=0=0) with 256/512/1024 pending; DISC-0030 unchanged (CONJECTURE).

## Change History

- 2026-10-15. Initial archive entry.
