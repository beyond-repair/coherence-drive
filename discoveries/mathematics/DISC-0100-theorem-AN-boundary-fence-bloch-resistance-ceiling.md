# Discovery: Boundary-fence resistance ceiling via Bloch spectrum (Theorem AN)

## Discovery ID

DISC-0100

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0101.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 7edc36aaf6f28959f43698c7c1b8f37230ec8be5 (main tip at archive time). Paths: GASKET.md "Theorem AN. Boundary-fence resistance ceiling via Bloch spectrum" (after Theorem AM: ASSUMPTION, THEOREM AN, Proof (i)–(iv), Witness, Kept Failure AN.1, NOT THIS; Conjecture J.1 evidence paragraph and OPEN updated); CLAIM_STATUS.md (new row "Boundary-fence resistance ceiling via Bloch spectrum; improved fractional and audit floors" VERIFIED; audit-norm row now ‖F(n,0.45)‖≥0.214239; energy/frac row updated); scripts/gasket_fractional_fence_ceiling.py (new); README.md.

## Original Evidence

GASKET.md Theorem AN, for every α∈(0,1/2) and every m≥1 (m=2^n, N=3m; M the Laplacian of the boundary collar — edges of every unit triangle meeting the outer boundary — padded by zero on non-collar vertices; Theorems AA, AL, AM, AK used as stated):
1. 0≤M≤L, so M^α≤L^α (Löwner–Heinz), hence Q_α(u_n)≥u_n^T M^α u_n; three-corner pairing ⇒ Q≥(7/3)/R^col with R^col=(e_a−e_b)^T(M^α)^+(e_a−e_b).
2. The abstract fence F_N (N-cycle with a distinct degree-2 apex on every edge) has Bloch symbol Ĥ(θ)=[[4−2cosθ, −(1+cosθ)+i sinθ], [−(1+cosθ)−i sinθ, 2]]; G_xx(θ;α)=(Ĥ(θ)^(−α))_xx; R^fen_α(m)=(e_0−e_m)^T(F_N^α)^+(e_0−e_m)=(1/N)Σ_{p=1}^{N−1} 4 sin²(πp/3) G_xx(2πp/N;α).
3. R^fen_α(m) < R^fen_∞(α)=(1/π)∫_0^{2π} G_xx(θ;α) dθ, on all of (0,1/2) (heat-kernel periodization on the infinite fence strip; λ_min(θ)∼(3/4)θ², G_xx∼(1/2)(3/4)^(−α) θ^(−2α), integrable iff α<1/2).
4. Three-corner defect δ(m)=R^col(m)−R^fen(m)<1/2 on checked m (increasing toward ≈0.406 at α=0.45), so R^col < R^fen_∞+1/2.
5. At α=0.45: R^fen_∞≈4.502104 (AM cycle ≈7.284859), R^col ceiling ≈5.002104, Q≥0.466470, ‖F_frac‖≥0.305377 (≈1.456× AM's 0.209685); with σ_AK≈0.701556, ‖F(n,0.45)‖≥0.214239 (≈1.456× AM's 0.147106).

## Discovery

Theorem AN refines DISC-0098 by comparing the gasket with its boundary collar (cycle plus inward unit-triangle spokes) instead of the bare cycle, ceilings the abstract fence by the Bloch integral R^fen_∞, and bounds the three-corner defect by 1/2. The proved audit floor at α=0.45 rises from 0.147106 to 0.214239. Incremental constant improvement. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Further sharpening of the proved positive floor for DISC-0034's sequence; still far below live ‖F(6)‖≈0.880 and below 0.70. Kept Failure AN.1 (DISC-0101) confirms that even this sharper ceiling cannot reach 0.70 along the σ_AK chain (AM.1 already closed that route family). Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Collar edges ⊂ G_n ⇒ 0≤M≤L ⇒ M^α≤L^α; three-corner pairing of AM (ii) on M^α.
2. Infinite fence strip is block-circulant; Fourier reduces to the displayed 2×2 Hermitian Ĥ(θ); spectral calculus gives G_xx; Goldstone mode λ_min∼(3/4)θ² with equal mass on boundary and apex ⇒ |U_x|²=1/2.
3. Periodization: p^{F_N}_t(0)−p^{F_N}_t(m)<p^{F_∞}_t(0,0); integrating t^(α−1)/Γ(α) yields R^fen(m)<R^fen_∞; integral = 2∫_0^1 G_xx(2πt) dt with singularity removal against κ(2πt)^(−2α), κ=(1/2)(3/4)^(−α).
4. Defect δ(m) positive, increasing on dyadics, converges to Δ_α≈0.406 < 1/2 at α=0.45 (same leading m^(2α−1) correction for fence and collar).
5. Floors: ‖F_frac‖=Q√21/7 (AA); AK (4)–(5) with fractional floor 0.305377.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems AA (DISC-0072), AK (DISC-0094), AL/AM notation (DISC-0096/0098) as stated. α∈(0,1/2) only; defect bound δ(m)<1/2 is witnessed on dyadics (lim≈0.406), used as 1/2 in the uniform ceiling.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AN.log` (repository witness `python3 scripts/gasket_fractional_fence_ceiling.py` at 7edc36aaf6f28959f43698c7c1b8f37230ec8be5, EXIT 0, 109 PASS, 0 FAIL, "All checks passed. Not thrust.") and `/workspace/scratch-ifi/indep_theorem_AN.py` / `indep_theorem_AN.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py` with integer lattice coordinates, own collar extraction from unit triangles meeting the outer boundary, no repo import, numpy only; EXIT 0, 137 PASS, 0 FAIL, ALL PASS):
- Bloch G_xx closed form matches direct Ĥ(θ)^(−α)_{xx} (rel err <1e-6); λ_min/θ²→3/4; G_xx·θ^(2α)→κ=(1/2)(3/4)^(−α);
- R^fen_∞(0.45)=4.502103886 stable under 0.5M/2M/4M-node singularity-removed quadrature; R^fen_∞ < R^cyc_∞≈7.284859;
- fence Fourier = dense (F_N^α)^+ corner resistance (rel err <1e-14) for m≤16; R^fen(m)<R^fen_∞ for dyadic m≤1024 at α∈{0.05,0.2,0.45,0.49}; control α=0.5 grows;
- abstract collar δ(m)<1/2 and increasing on dyadics m=2..256 (max δ≈0.405); R^col < R^fen_∞+1/2≈5.002104;
- floors at 0.45: Q≥0.466470, ‖F_frac‖≥0.305377, σ_AK recomputed 0.701556, ‖F‖≥0.214239 (~1.456× AM);
- live levels 1–5 at α=0.45: collar ⊂ gasket, L−M≥0 and L^α−M^α≥0; R_live≤R_col≤R_cyc, R_fen<R_col<Rceil; Q≥(7/3)/R_col≥0.466470; live ‖F‖ table 1.439599…0.909692 reproduced; live σ_AK·‖F_frac‖ on L2–5 = 0.598008…0.471857 < 0.70.

## Prior Art

Elementary: Löwner–Heinz, Bloch/Floquet reduction of a 1D strip with apexes, spectral calculus on 2×2 Hermitians, heat-kernel periodization; the R^fen_∞=(1/π)∫G_xx interpretation is the fractional Green function of the infinite fence strip evaluated at adjacent boundary sites distance m apart in the continuum limit. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Incremental sharpening of DISC-0098 / DISC-0094; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket and collar independently; recomputed G_xx by direct matrix power of Ĥ(θ); matched Fourier against dense fence pseudo-inverses; checked the ceiling across α∈(0,1/2) and dyadic m; verified δ(m)<1/2 and Loewner–Heinz on live levels 1–5. No break found. The δ(m)<1/2 step remains a finite-range witness (as the repository states), not a closed-form defect bound.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0098's numerical floor (DISC-0098 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0098. Mathematical. Theorem AM; AN replaces the bare cycle by the boundary fence/collar, R^fen_∞+1/2.
- DISC-0094. Mathematical. Theorem AK; AN uses σ_AK with the new ‖F_frac‖ floor.
- DISC-0072. Mathematical. Theorem AA; same Löwner–Heinz embedding mechanism.
- DISC-0101. Failed hypothesis. Kept Failure AN.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges and whether L≥0.70. DISC-0101 / DISC-0099 show no resistance ceiling in the σ_AK chain can reach 0.70; a share floor near the live σ_n≈1.35 would be needed. A closed-form proof that δ(m)<1/2 for all m (not just dyadics) would remove the finite-range step.

## Next Experiments

None required.

## Reproduction Instructions

`git checkout 7edc36aaf6f28959f43698c7c1b8f37230ec8be5 && python3 scripts/gasket_fractional_fence_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AN.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AN.log`, `/workspace/scratch-ifi/indep_theorem_AN.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AN at 7edc36aaf6f28959f43698c7c1b8f37230ec8be5; repo witness EXIT 0 (109 PASS); independent check ALL PASS (137 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-15. Initial archive entry.
