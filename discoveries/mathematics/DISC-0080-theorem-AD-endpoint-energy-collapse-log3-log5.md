# Discovery: At α = log3/log5 the fractional energy collapses like 1/n, with the exact pairing Q_α R_α = 7/3 (Theorem AD)

## Discovery ID

DISC-0080

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0081.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit b8b48ad72bf62d57da7a69bc5b2b9b63a2e51c5f. Paths: GASKET.md "Theorem AD. At α=log 3/log 5 the energy collapses like 1/n" (Assumption incl. CITED Stieltjes and variational formulas, Theorem AD (i)–(ii), Proof: (i) / lower bound on R_γ / upper bound on R_γ / Conclusion, Witness, Kept Failure AD.1, NOT THIS); GASKET.md item 4 now cites AA–AD; GASKET.md Theorem AC paragraph ("endpoint decided on the collapsing side by Theorem AD"); "What this does not say" bullets; scripts/gasket_fractional_endpoint.py (new); scripts/cli.py; scripts/gasket_fractional_capacity_floor.py (closing print only); CLAIM_STATUS.md (new row "Endpoint α=log3/log5 and exact pairing" VERIFIED; AC row and α=0.45 OPEN row extended); README.md Sequel paragraph.

## Original Evidence

(i) For every α∈(0,1] and n≥1 the corner Schur complement of L^α is κ_n(3I−J), so with corner data (1,−1/2,0) and v=e_a−e_b: Q_α(u_n)=(7/2)κ_n, R_α(n)=v^T(L^α)^+v=2/(3κ_n), hence Q_α(u_n)·R_α(n)=7/3 exactly. (ii) At α=γ=log3/log5, c_AD n ≤ R_γ(n) ≤ 80((n+1)ln3+1), c_AD=(sin πγ/π)(3/25)ln5≈0.051634; so (7/3)/(80((n+1)ln3+1)) ≤ Q_γ(u_n) ≤ (7/3)/(c_AD n), ‖F_frac(n,γ)‖=Q_γ√21/7→0 and, by Theorem L, ‖F(n,γ)‖ ≤ κ(γ)√((7/3)/(c_AD n))→0. Repo witness levels 1–7: R_γ ≈ (1.330561, 1.780895, 2.270069, 2.776998, 3.290658, 3.806650, 4.323426); Q_γ ≈ (1.753647, 1.310202, 1.027869, 0.840236, 0.709078, 0.612962, 0.539695); ‖F(n,γ)‖ ≈ (1.407584, …, 0.406991).

## Discovery

Decides the endpoint left open by DISC-0078/DISC-0079: at α=γ there is no level-uniform energy floor; the energy decays exactly at order 1/n (i.e. 1/log N), and the combinatorial audit norm tends to 0 (rate n^{−1/2} only as an upper bound). With Theorems AC and K: a level-uniform energy floor holds exactly for α<γ, and ‖F(n,α)‖→0 for every α≥γ. Part (i) sharpens the duality constant 9/4 used in AA/AC to the exact 7/3.

## Why It Matters

Closes the last threshold question in the fractional-energy picture on this graph. It does not touch α=0.45: at 0.45 the energy has a floor (DISC-0072, DISC-0078) and the combinatorial limit is still exactly lim ρ_n (DISC-0076); DISC-0034 stays OPEN. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. D3 symmetry of G_n permutes the corners in every way and commutes with L, hence with L^α and with the corner Schur complement S; S=xI+yJ and S𝟙=0 ⇒ S=κ(3I−J), κ>0 (kernel of L^α = constants). Q=b^TSb=κ Σ_{i<j}(b_i−b_j)² = κ(9/4+1/4+1)=(7/2)κ.
2. For v supported on the corners and ⊥𝟙, v^T(L^α)^+v = v^T S^+ v (Kron reduction preserves effective resistance) = |v|²/(3κ)=2/(3κ). Hence QR=7/3.
3. Stieltjes: λ^{−γ}=(sin πγ/π)∫_0^∞ s^{−γ}(λ+s)^{−1}ds; Tonelli ⇒ R_γ=(sin πγ/π)∫ s^{−γ}R^s ds, R^s=v^T(L+s)^{−1}v (v⊥𝟙, no zero mode).
4. Test function: harmonic f on the level-k corner cell at a (a copy of G_k, 0≤k≤n−1), f(a)=1, f=0 at its two far corners and outside. The cell attaches to the rest of G_n only at those two corners, so E(f)=cell energy=2(3/5)^k (Δ of resistors (5/3)^k); 0≤f≤1 ⇒ ‖f‖² ≤ N(k) ≤ 3^{k+1}; ⟨f,v⟩=1. Variational formula: for s∈[5^{−(k+1)},5^{−k}), R^s ≥ 1/(2(3/5)^k+3(3/5)^k) = (5/3)^k/5 = 5^{k(1−γ)}/5 ≥ (5s)^{γ−1}/5 (γ−1<0, 5s≥5^{−k}).
5. ∫_{5^{−n}}^1 s^{−γ}(5s)^{γ−1}/5 ds = 5^{γ−2} n ln5 = (3/25) n ln5 (5^γ=3) ⇒ R_γ ≥ c_AD n.
6. Upper bound: AC's μ((0,s]) ≤ min(2, 80s^γ) and μ=0 below 5^{−(n+1)} (λ_1≥5^{−n}/4, DISC-0078); layer cake R_γ=γ∫s^{−γ−1}μ((0,s])ds ≤ 80γ ln(s_*5^{n+1}) + 2s_*^{−γ} = 80((n+1)ln3 − ln40 + 1), s_*=40^{−1/γ}; if s_*<5^{−(n+1)} then 3^{n+1}<40 and R_γ ≤ 2·3^{n+1} < 80.
7. Insert into (i); Theorem K pairing ‖F_frac‖=Q√21/7; Theorem L ‖F‖ ≤ κ(γ)√Q.

## Assumptions

Spectral calculus L^α=V diag(λ^α)V^T, 0^α:=0 (GASKET item 4); corner data (1,−1/2,0); standard Stieltjes and variational (Dirichlet-principle) formulas; standard network facts (Kigami 5/3 renormalization, Kron reduction); Theorems K, L (DISC-0032) and AC's spectral-mass and gap lemmas (DISC-0078).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AD.log` (repository witness at b8b48ad, EXIT 0, 36 PASS, 0 FAIL, 1m08s; AC witness re-run at the same tip EXIT 0) and `/workspace/scratch-ifi/indep_theorem_AD.py` / `indep_theorem_AD.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; 111 PASS, 0 FAIL, ARCHIVE_INDEP_THEOREM_AD_PASS; dense through level 7, sparse through level 10; scipy in `/workspace/scratch-ifi/.venv-sci`):
- (i) Schur complement = κ(3I−J) to rel ≤7.3e−12 and |QR−7/3|, |Q−(7/2)κ| ≤ 1.5e−12, levels 1–7, 11 α values (0.1, 0.3, 0.45, 0.6, γ, 0.75, 0.9, 1.0 and three random in (0.05,1)); R agrees three ways (spectral sum, pinv(L^α), Kron-reduced S^+) to rel ≤5.4e−14. Control: one edge weight changed to 1.7 on G_3 (D3 broken) gives QR=2.334853≠7/3, so the identity rests on the symmetry, not on a generic duality.
- (ii) the corner-cell bump built inside G_n (lattice cell i+j≤2^k) attaches only through its two far corners, has E=2(3/5)^k exactly and ‖f‖² ≤ N(k) for every k<n≤7 (e.g. G_7, k=6: |cell|=1095, E=0.093312, ‖f‖²=170.61); on every band [5^{−(k+1)},5^{−k}) (both edges sampled) R^s ≥ 1/(E+s‖f‖²) ≥ (5s)^{γ−1}/5; worst R^s/bound over [5^{−n},1) = 4.98, 5.26, 5.34, 5.37, 5.376, 5.378, 5.379 (levels 1–7; GASKET "about 5.38", so c_AD is crude by ≈5.4×). c_AD n reproduced by mpmath quadrature (n=1,3,7,20) to 1e−12; Stieltjes formula checked.
- (iii) eigen-free route: R_α(n) by whole-line trapezoid in log s with sparse LU solves of (L+s)x=v and exact tail expansions; agrees with dense to ≤7.1e−13 for n≤7; levels 8–10 new: R_γ = 4.840462, 5.357585, 5.874736; increments 0.450335, 0.489173, 0.506929, 0.513660, 0.515992, 0.516775, 0.517036, 0.517123, 0.517151 → ≈0.51715 per level; n·Q_γ = 1.754, 2.620, …, 3.972 (n=10) rising toward (7/3)/0.51715≈4.51, consistent with Θ(1/n); sandwich c_AD n ≤ R_γ ≤ 80((n+1)ln3+1) holds n=1..10. R^0=(2/3)(5/3)^n reproduced at every level.
- Endpoint attack: α=γ−0.02 increments contract with ratio → 0.9684 (pred. 5^{α−γ}=0.9683, bounded R); α=γ+0.02 ratio → 1.0328 (pred. 1.0327, geometric growth); so log3/log5 is exactly where R_α switches from bounded to divergent, linear growth only at γ.
- (iv) own Euclidean audit vector: ‖F(n,γ)‖ and Q_γ match GASKET to 5e−7 at levels 1–7; ‖F‖ ≤ κ(γ)√Q; ‖F_frac‖=Q√21/7 to 1e−9.
- α=0.45: R_0.45(n) bounded (R_0.45(10)=2.478218 ≤ C_AC); AD supplies nothing there.

## Prior Art

Classical ingredients: Stieltjes/Balakrishnan representation of λ^{−α}; Dirichlet/Thomson variational principle; Kron reduction; Kigami resistance 5/3 and spectral dimension d_s=2log3/log5 on the Sierpinski gasket (so γ=d_s/2, the critical exponent where Green-type quantities of L^α diverge logarithmically). The phenomenon (log divergence at α=d_s/2) is the standard critical case; the argument applies it to this repository's audit functional. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete proof in the repository, verified here). Technique derivative of classical SG/resistance analysis; not a novelty claim and not a Stage-1 / claim-level raise. No sharp constants (c_AD crude ≈5.4×; upper constant 80 crude).

## Falsification Attempts

Rebuilt independently with a different coordinate model; checked the pairing for random α and with a symmetry-breaking perturbation (pairing fails, as it must); built the test function inside G_n rather than on a standalone G_k and checked the attachment claim explicitly; sampled band edges where (5s)^{γ−1}/5 is largest; recomputed R_γ without any eigendecomposition up to level 10 (N=88,575); probed α=γ±0.02 to confirm the endpoint. No break found. Minor: the "0.0" printed by the repo witness for the AC floor at α=0.6826 is rounding (floor → 0 as α→γ), not an error.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Resolves the open question "α=γ" recorded in DISC-0078 and DISC-0079 (recorded as graph edges; those rows are not edited). DISC-0034 unchanged (OPEN): AD is about α=γ and gives no lower bound on ‖F(n,0.45)‖ or ρ_n.

## Patent Relevance

None.

## Related Discoveries

- DISC-0078. Mathematical. Theorem AC; its spectral-mass and gap lemmas give the upper bound; its "α=γ open" is settled here.
- DISC-0079. Failed hypothesis. No floor above γ; endpoint now on the same side.
- DISC-0081. Failed hypothesis. Kept Failure AD.1 (AC floor does not reach γ).
- DISC-0032. Mathematical. Theorems K (pairing ‖F_frac‖=Q√21/7) and L (‖F‖ ≤ κ√Q).
- DISC-0072. Mathematical. AA floor constant 9/4 sharpened to the exact pairing 7/3.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Sharp asymptotic constant lim R_γ(n)/n (archive numerics ≈0.51715 per level through n=10; not proved). Combinatorial ‖F(n,0.45)‖ / lim ρ_n zero vs positive (OPEN, DISC-0034).

## Next Experiments

None required. Optional: sparse route to n=11–12 to tighten the empirical slope.

## Reproduction Instructions

`git checkout b8b48ad72bf62d57da7a69bc5b2b9b63a2e51c5f && python3 scripts/gasket_fractional_endpoint.py`. Archive: `/workspace/scratch-ifi/.venv-sci/bin/python /workspace/scratch-ifi/indep_theorem_AD.py 7 10`. Logs: `/workspace/scratch-ifi/repo_theorem_AD.log`, `/workspace/scratch-ifi/indep_theorem_AD.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AD at b8b48ad72bf62d57da7a69bc5b2b9b63a2e51c5f; repo witness EXIT 0; independent check ARCHIVE_INDEP_THEOREM_AD_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
