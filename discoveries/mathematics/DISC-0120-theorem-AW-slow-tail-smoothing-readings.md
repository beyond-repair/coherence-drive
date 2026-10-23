# Discovery: Slow-tail smoothing readings (−Δ)^{−τ}Ψ: the literal reading diverges for τ≥(1+ℓ)/2, a surface-independent value is always 0, and the marginal readings give a radius-free but centre-dependent remainder (Theorem AW)

## Discovery ID

DISC-0120

## Status

KNOWN

## Date Discovered

2026-10-22 (America/New_York), ~8:55am EDT corpus slice. Preferential unread: IFI commit 7a12ab7 (Theorem AW) landed at 08:22:03 −0400 (12:22Z), after Theorem AV (9fc8c7a, indexed as DISC-0118..0119).

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7a12ab736327e6d314c2035b7c8cfb95a2025dc6 (2026-10-22 08:22:03 −0400). Paths: README.md "Theorem AW. Slow-tail smoothing readings \((-\Delta)^{-\tau}\Psi\): a surface-independent value is always \(0\), and the marginal readings give a radius-free but centre-dependent remainder" (Assumption AW, (a) Existence, AW.1–AW.3 with (d) dipole, Proofs, Kept Failure AW.1, Witness, NOT THIS with Conjecture AW.4); README.md Stage-2 OPEN bullet extended; CLAIM_STATUS.md Theorem AW row (VERIFIED, not thrust); scripts/slow_tail_reading_flux.py (new, 274 lines); scripts/cli.py; tests/test_cli.py (SlowTailReadingTests).

## Original Evidence

Reading Φ=(−Δ)^{−τ}Ψ, τ>0, in Maxwell form T[Φ,Φ] or cross form T[Ψ,Φ], static massless C6 (Ψ_info=A_0), C5, isolated compactly supported device ρ̃=−ΔΨ (point charges and point dipoles allowed), effective source σ=−ΔΦ, σ̂=|k|^{−2τ}ρ̂̃ on k≠0. (a) The literal multiplier |k|^{−2−2τ}ρ̂̃ is locally integrable iff τ<(1+ℓ)/2 (ℓ = first nonzero multipole order), so the literal reading does not exist for a charged device when τ≥½ and for a dipole when τ≥1; replaced by the finite-part kernel Φ=C_τ r^{2τ−1}, C_τ=Γ(½−τ)/(4^τ√π Γ(1+τ)) (log kernel −(2/π)ln r at τ=½). AW.1: one charge q at a, sphere radius R about c, b=|c−a|<R: G=D_τ q² J_τ(R,b) ê_b, D_τ=2πτ(2τ−1)²C_τ², J_τ=∫_{R−b}^{R+b} r^{4τ−3}(1−u0²)dr; D_{1/4}=1, D_{1/2}=4/π (limit), D_{3/4}=4/3, D_1=π/2, D_{5/4}=16/5; J_{1/4}=4b/(3(R²−b²)), J_{3/4}=4b/3, J_{5/4}=4b(5R²−b²)/15. AW.2: for every τ>0 a surface-independent G is 0; for τ∉ℤ the self reading is surface-dependent for every nonzero device (|k|^{2τ} not analytic); for τ∈ℤ (canonical kernel) surface independence iff σ compactly supported, then G≡0. AW.3: G(S_{c,R})=(4/3)D_τQ²(c−x_Q)R^{4τ−3}(1+O(R^{−2}))+O(R^{4τ−4}) for 0<τ<3/2: G→0 for τ<3/4 even though (H) fails; marginal τ=3/4 gives exactly (16/9)q²(c−a) on every R>|c−a| (cluster → (16/9)Q²(c−x_Q)); neutral dipole p at 0: marginal τ=5/4 gives exactly (16/75)(|p|²c−8(p·c)p) on every R>|c|; at τ=3/4 with c∥p, G=−(4/15)|p|²c/(R²−|c|²).

## Discovery

Classical potential theory applied to the repository's reading family. The finite-part kernel is the standard fundamental solution of (−Δ)^{1+τ} in ℝ³ (power kernel off the exceptional half-integers, log kernel at them). Because |k|^{2τ} is not analytic for non-integer τ, a compactly supported charge never has a compactly supported smeared source, so its Maxwell stress is not divergence-free on the vacuum and G moves with the audit surface (the same mechanism as DISC-0118, now without the decay hypothesis). The off-centre-sphere cap integral of DISC-0118 (AV.4) is reused on a bounded region, so it needs no decay at infinity. At the marginal exponent the remainder is radius-free but linear in the offset of the audit centre and zero on spheres centred at the centre of charge (or the dipole).

## Why It Matters

It closes the slow-tail gap that Theorem AV (DISC-0118) left OPEN ((−Δ)^{−τ}, τ≥½, outside (H)). The tempting radius-independent marginal values are not a device property (see DISC-0121). It does not compute Ψ_info on the frozen 0.45 mesh and is not thrust.

## Derivation

Checked line by line. (a): polar integrability at k=0 and real-space tail integrability give the same threshold. Kernel: Δr^p=p(p+1)r^{p−2} gives −Δ(C_τ r^{2τ−1})=−2τ(2τ−1)C_τ r^{2τ−3}; I checked this against an independent Fourier computation (radial sine transform of 4π|k|^{−2τ}), not the README's Riesz constant. AW.1: Φ radial about a, so the centred sphere S_0 gives 0; divergence theorem on the bounded region between S and S_0 gives the AV.4 cap integral with m=−r²Φ′=−qC_τ(2τ−1)r^{2τ}, mm′/r²=2τ(2τ−1)²C_τ²q²r^{4τ−3}; no limit R′→∞ is taken. AW.2: (i) a bump surface gives div T(x0)=0 at every far vacuum point; (ii) real-analyticity on the connected Ω and the integral-domain property give σ≡0 on Ω (or ∇Φ≡0, which also gives σ≡0); (iii) for τ∉ℤ, ρ̂̃(te)/(t^m h(t)) would be meromorphic and equal |t|^{2τ}, impossible for 2τ∉2ℤ (odd 2τ: different one-sided Laurent series), so ρ̃=0; (iv) integer τ: Φ=𝒩*σ with compact σ, |T|=O(R^{−4}), so the constant is lim G(S_R)=0; (v) cross reading reduces to the same steps. The converse (div T=0 on Ω ⇒ constant) uses connectedness of the unbounded component. AW.3: Taylor expansion about x_Q (dipole moment 0 there), error O(R^{4τ−4}); dipole by homogeneity and oddness, exact τ=5/4 constants fixed by O(2)-equivariance from three cases. No gap found. Minor notes: the theorem's cluster error bound O(R^{−1}) at τ=3/4 is not sharp for the README cluster (observed R^{−2}); the README's "|G| centred at x_Q" figures are max-abs components, not Euclidean norms (labelling only).

## Assumptions

Assumption AW; C5; static massless C6 with Ψ_info=A_0; d=3; units 4πε0=1; compactly supported device; finite-part (analytic-continuation) kernel where the literal reading diverges, fixed only up to polynomials (AW.2 holds for every choice when τ∉ℤ, canonical kernel when τ∈ℤ); AW.1 and AW.3 for 0<τ<3/2; vacuum surfaces enclosing supp ρ̃; no design parameter (W, χ_vac, κ, m, 0.08, 0.23, 30 µN/kW) enters.

## New Results

Repository script `scripts/slow_tail_reading_flux.py` at 7a12ab7: 82 "ok" lines, 0 FAIL, "all Theorem AW checks passed; nothing here is thrust", EXIT 0, 10.8 s (archive `/workspace/scratch-ifi/repo_theorem_AW.log`); `pytest tests/test_cli.py -k SlowTail` 1 passed. Archive `/workspace/scratch-ifi/indep_theorem_AW.py` / `indep_theorem_AW.log` (59/59 PASS, EXIT 0, 12.6 min; does not import repo code; mpmath 30 digits plus numpy): C_τ from the Fourier side at τ=0.1,0.25,0.4 (literal Φ) and σ at τ=0.6,0.75,1.25,1.4 to <1e−20; (2τ−1)C_τ→−2/π; divergence threshold at the six (τ,ℓ) pairs; D_τ exact values and limit 4/π; J closed forms at four (R,b); own 160×320 / 240×480 Gauss–Legendre surface quadrature of T·n (not the 1D cap formula) matches D_τJ_τ at τ=0.25,0.5001,0.6,0.75,1,1.25 to ≤1e−13 relative, log kernel 0.435470590524, 6.14125617949, 425.813333333; τ=3/4 one charge q=−2.3 off-axis: (16/9)q²(c−a) on R=0.7,2,3,10,55 (err 2e−12); τ=0.55,0.6,0.7: G∝R^{−(3−4τ)} while ∮|Tn|∝R^{4τ−2} (both exponents to 0.01); Coulomb cluster (repo input data, values recomputed) τ=3/4, τ=1 and cross reading match README to ≤4.3e−7, Maxwell piece ≤6.9e−14, cluster limit (32,12.444444,−14.222222) with errors 3.61e−2→5.60e−4, centred-at-x_Q decay, τ=1 growth 753.29/1507.62/3015.76; dipole: centred spheres 0 at four τ, τ=5/4 closed form for 4 random (p,c) on R from |c|+0.3 to 400 (err 7.8e−12), exact linearity and oddness in c, README dipole value, τ=3/4 c∥p closed form, ratios 0.4996 and 1.5161; radial compact device ρ̃=−Δ(1−r²)⁴: τ=1 gives σ=φ (compact, σ(1.5)=0), τ=0.6 and 1.25 give σ(1.5)=−0.00989, 0.00574 ≠0 (leaks); centre-dependence of the marginal value on three centres at fixed R. First run had 8 FAILs: 7 were my own quadrature error at the k→0 singularity (fixed by k=u⁵ substitution, no README change), 1 was the max-component vs Euclidean labelling noted above.

## Prior Art

Classical: fundamental solution of (−Δ)^s in ℝⁿ, κ_{n,s}|x|^{2s−n} with κ_{n,s}=Γ(n/2−s)/(4^s π^{n/2}Γ(s)) and log kernels at s−n/2∈ℕ₀ (Riesz 1949; Stein; Gel'fand–Shilov on |x|^λ continuation; survey Abatangelo–Valdinoci "Laplaciani frazionari d'ordine superiore"; Stinga, arXiv:1808.05159, on the s≥n/2 restriction of (−Δ)^{−s}); with n=3, s=1+τ and source 4πδ this is exactly C_τ. Non-locality of (−Δ)^{s} for non-integer s (compact support not preserved) is standard. Maxwell stress tensor divergence identity, surface independence ⇔ div T=0, real-analytic unique continuation, Paley–Wiener (compact support ⇒ entire transform). The off-centre-sphere constants D_τ, 16/9, 16/75 are elementary integrals for this reading; not separately searched, no novelty claimed.

## Novelty Analysis

None for the method (same pattern as DISC-0118 and DISC-0059/0061/0068/0070). The specific marginal constants (16/9)q²(c−a) and (16/75)(|p|²c−8(p·c)p) are elementary consequences of classical kernels applied to the repository's own reading; whether they appear in prior literature is UNRESOLVED (not searched) and they are not claimed as new.

## Falsification Attempts

Checked C_τ by an independent Fourier route rather than the Riesz formula; checked the 1D cap formula against direct 3D surface quadrature that never uses it; moved the τ=3/4 charge off-axis with a negative non-unit q and radii from just above b to 55; random (p,c) dipoles and R up to 400; recomputed every quoted cluster figure from the repo's input data; tested the integer/non-integer dichotomy on a compact radial device (σ compact at τ=1, leaks at τ=0.6, 1.25); confirmed (H) fails while G→0 for τ<3/4. No contradiction with the theorem statement.

## Experimental Validation

None.

## Mathematical Status

Classical results applied to the repository's reading; proof checked and independently reproduced numerically. Classified KNOWN (not THEOREM elevation), matching DISC-0118.

## Patent Relevance

None.

## Related Discoveries

- DISC-0118. Theorem AV (nonlocal Maxwell-form readings); AW reuses the AV.4 cap formula without (H) and closes AV's slow-tail gap.
- DISC-0119. Kept Failure AV.1; same rejected route class.
- DISC-0121. Failed hypothesis. Kept Failure AW.1.
- DISC-0122. Conjecture AW.4 (2^ℓ-pole marginal τ).
- DISC-0070 / DISC-0068 / DISC-0061 / DISC-0059. Theorems Z, Y, V, U (local first-derivative readings).
- DISC-0049. P.2 undifferentiated flux; the integer-τ polynomial loophole is an external field, same class.

## Open Questions

Conjecture AW.4 for ℓ≥2 (DISC-0122); r^{2j}ln r kernels (τ=3/2,5/2,…) beyond AW.2; non-Maxwell slow-tail tensors; physical meaning of the finite-part continuation where the literal reading diverges; time-dependent fields; Ψ_info ≠ A_0; Stage 2 0.45 mesh (still OPEN). Claim ceiling unchanged.

## Next Experiments

Symbolic derivation of the ℓ=2 marginal matrix M_{7/4,2} to test DISC-0122 beyond numerics.

## Reproduction Instructions

`git checkout 7a12ab736327e6d314c2035b7c8cfb95a2025dc6 && python3 scripts/slow_tail_reading_flux.py` (and `python3 -m pytest tests/test_cli.py -k SlowTail`). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AW.py` (~13 min; section 8 nested quadrature dominates). Logs: `/workspace/scratch-ifi/repo_theorem_AW.log`, `/workspace/scratch-ifi/indep_theorem_AW.log`.

## Evidence Log

- 2026-10-22 ~8:55am EDT. Repo witness EXIT 0 (82 ok, 0 FAIL); repo test 1 passed; independent check 59/59 PASS. Only other pushes since the previous slice: mend fix/mend-playtest-rc 0097bb9 / 23e2efc / bc18167 (world-map edge pins, Citadel pan, turn-order name wrap, QA docs; no research claim).

## Change History

- 2026-10-22. Initial archive entry.
