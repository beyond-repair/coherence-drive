# Discovery: Boundary-cycle resistance ceiling via Fourier and the heat kernel (Theorem AM)

## Discovery ID

DISC-0098

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0099.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 0a11b759297d446a05f203ae18aea505e6fa4e86 (main tip at archive time). Paths: GASKET.md "Theorem AM. Boundary-cycle resistance ceiling via Fourier and the heat kernel" (after Theorem AL: ASSUMPTION, THEOREM AM, Proof (i)–(v), Witness, Kept Failure AM.1, NOT THIS; Conjecture J.1 evidence paragraph and OPEN updated); CLAIM_STATUS.md (new row "Boundary-cycle resistance ceiling via Fourier and heat-kernel periodization; improved fractional and audit floors" VERIFIED; audit-norm row now ‖F(n,0.45)‖≥0.147106); scripts/gasket_fractional_cycle_ceiling.py (new); README.md.

## Original Evidence

GASKET.md Theorem AM, for every α∈(0,1/2) and every m≥1 (m=2^n, N=3m; M the Laplacian of the 3m outer boundary edges, padded by zero on interior vertices; Theorems AA, AD (i), AK, AL used as stated):
1. 0≤M≤L, so M^α≤L^α (Löwner–Heinz), hence Q_α(u_n)≥u_n^T M^α u_n.
2. The boundary is one cycle C_N with corners a,b,c at positions 0,m,2m; R^cyc_α(m)=(e_a−e_b)^T(M^α)^+(e_a−e_b)=(2/N)Σ_{k=1}^{N−1}λ_k^(−α)(1−cos(2πk/3))=(3/N)Σ_{3∤k}λ_k^(−α), λ_k=4sin²(πk/N).
3. R^cyc_α(m) < R^cyc_∞(α)=2∫_0^1(2sinπx)^(−2α)dx=(2/π)4^(−α)B(1/2−α,1/2)=(1−α)R_∞(α), on all of (0,1/2) (no α_* threshold as in AL).
4. Dihedral symmetry makes the corner block of (M^α)^+ circulant; best corner-supported test vector gives Q_α(u_n)≥(7/3)/R^cyc_α(2^n)>(7/3)/((1−α)R_∞(α)), ‖F_frac(n,α)‖≥√21/(3(1−α)R_∞(α)).
5. At α=0.45: R^cyc_∞≈7.284859 (AL: 13.245199), Q≥0.320299, ‖F_frac‖≥0.209685 (=(28/27)/(1−α)≈1.886× AL's 0.111208); two-corner vector alone gives 0.308860; with σ_AK≈0.701556, ‖F(n,0.45)‖≥0.147106 (≈1.886× AL's 0.078019).

## Discovery

Theorem AM refines DISC-0096 by comparing the gasket with its whole outer boundary cycle instead of one side, which both lowers the resistance ceiling by the factor (1−α) and lets the three-corner pairing (7/3 instead of 9/4) be used; it removes AL's α_* threshold. The proved audit floor at α=0.45 rises from 0.078019 to 0.147106. Incremental constant improvement. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Further sharpening of the proved positive floor for DISC-0034's sequence; still far below live ‖F(6)‖≈0.880 and below 0.70. Kept Failure AM.1 (DISC-0099) shows the energy-floor×σ_AK chain cannot reach 0.70 with any resistance ceiling, so the obstruction is now located in the share floor σ_AK, not in the resistance comparison. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. L−M is a sum of PSD edge matrices of non-boundary edges ⇒ 0≤M≤L ⇒ M^α≤L^α for α∈(0,1). Corner-supported zero-sum v lie in range(M^α) (kernel = interior indicators + boundary constant), so Cauchy–Schwarz gives u^TM^αu≥(v^Tu)²/(v^T(M^α)^+v).
2. Rotation by m and reflections of C_{3m} fixing {0,m,2m} permute the corners and commute with M^α ⇒ corner block g_0I+g_1(J−I), R^cyc=2(g_0−g_1); maximizing over zero-sum v gives 2|u_C−ū_C|²/R^cyc; for (1,−1/2,0), ū_C=1/6, |u_C−ū_C|²=7/6 ⇒ (7/3)/R^cyc.
3. Fourier on C_N: 2πkm/N=2πk/3, so 1−cos is 0 for 3|k and 3/2 otherwise.
4. λ^(−α)=Γ(α)^(−1)∫t^(α−1)e^(−tλ)dt ⇒ R^cyc=(2/Γ(α))∫t^(α−1)(p^C_t(0)−p^C_t(m))dt. Periodizing, residues 0 and m mod 3m sorted by |x| give p^C_t(0)−p^C_t(m)=p^Z_t(0)−Σ_{r≥0}[p((3r+1)m)+p((3r+2)m)−2p((3r+3)m)]; p^Z_t(x)=e^(−2t)I_|x|(2t) strictly decreasing in |x| ⇒ every bracket >0 ⇒ strict inequality; integrating gives 2∫_0^1(4sin²πx)^(−α)dx (finite iff α<1/2). (Rearrangement re-derived here: |x| values in class 0 are 0, 3rm (twice), in class m are (3r+1)m, (3r+2)m once each.)
5. Beta: ∫_0^π sin^(−2α)θ dθ=B(1/2−α,1/2); B(x,3/2)=B(x,1/2)/(2(x+1/2)) with x=1/2−α ⇒ R^cyc_∞=(1−α)R_∞.
6. Floors: ‖F_frac‖=Q√21/7 (AA); AK (4)–(5) with fractional floor 0.209685.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems AA (DISC-0072), AD (i), AK (DISC-0094), and AL's R_∞ notation (DISC-0096) as stated. α∈(0,1/2) only; the cycle resistance diverges at α≥1/2 (Theorem AC still covers [1/2,log3/log5) with its own floor).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AM.log` (repository witness `python3 scripts/gasket_fractional_cycle_ceiling.py` at 0a11b759297d446a05f203ae18aea505e6fa4e86, EXIT 0, 164 PASS, 0 FAIL, "All checks passed. Theorem AM / Kept Failure AM.1. Not thrust.") and `/workspace/scratch-ifi/indep_theorem_AM.py` / `indep_theorem_AM.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py` with integer lattice coordinates, own boundary-cycle extraction, no repo import, numpy only; EXIT 0, 156 PASS, 0 FAIL, ALL PASS):
- independent split R^cyc(m)=3S(3m)−S(m) (no 3∤k mask) equals a dense pseudo-inverse of C_{3m}^α (max rel err <1e-10) at α∈{0.01,0.05,0.2,0.45,0.499,0.7};
- R^cyc_∞=(1−α)R_∞ = an analytically singularity-free quadrature at 8 values of α incl. 0.001, α_*, 0.499;
- ceiling R^cyc(m)<R^cyc_∞ for m≤199, dyadic m to 2^22 and 15 random m≤3·10^6 at 9 values of α including below α_* (0.001, 0.02, 0.05, 0.079), plus 60 random (α,m) attacks — no break; R^cyc(2^n)<path R(2^n) n≤13; controls α=1/2 (log growth) and α=0.6 (power growth) diverge;
- independent asymptotic (Euler–Maclaurin ζ): (R^cyc(m)−R^cyc_∞)/m^(2α−1) → 2ζ(2α)(2π)^(−2α)(3^(2α)−1) (negative since ζ(2α)<0), matched to 6 digits at α=0.2 (−0.600474) and α=0.45 (−6.088712); this independently explains the "slow m^(2α−1) correction" and R^cyc_0.45(2^20)≈5.7627;
- heat kernel: 0≤p^C_t(0)−p^C_t(m)≤p^Z_t(0) on 64 (t,m) pairs (t∈[1e-3,2000], m≤256; at small t/large m the gap is below float64 resolution); on 43 resolvable pairs the gap equals the bracket sum and is >0 (p^Z via continued-fraction Bessel ratios I_{n+1}/I_n<1, checked n<200, z≤1000); Gamma-integral representation reproduces the Fourier value (m=4, α=0.45; m=8, α=0.25);
- constants at 0.45: R^cyc_∞=7.284859258, (9/4)/R=0.308860, (7/3)/R=0.320299, ‖F_frac‖ floor=√21/(3R)=0.209685, σ_AK recomputed 0.701556, ‖F‖ floor 0.147106, gain vs AL=(28/27)/(1−α);
- live levels 1–6 at α=0.45: outer boundary is one cycle C_{3m} with corners at 0,m,2m; L−M≥0 and L^α−M^α≥0; padded M^α on the boundary equals C_{3m}^α; corner block circulant with 2(g_0−g_1)=R^cyc (1.609952 … 3.267812); Schur boundary energy = (7/3)/R^cyc; Q≥u^TM^αu≥(7/3)/R^cyc≥0.320299 (L6: Q=0.994015, u^TM^αu=0.811534, cycle floor 0.714035 vs path floor 0.448821); live ‖F‖ table 1.439599 … 0.880109 reproduced; live gasket R<R^cyc.

## Prior Art

Elementary: Löwner–Heinz operator monotonicity, discrete Fourier analysis on cycles, the Gamma-integral (subordination) representation of λ^(−α), monotonicity of modified Bessel functions in the order, Beta integrals; the R^cyc_∞=2G^Z_α(0,0) interpretation is the standard fractional Green function on Z. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Incremental sharpening of DISC-0096 / DISC-0094; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket and boundary cycle independently; recomputed R^cyc by a different decomposition and against dense pseudo-inverses; tried to break the ceiling below AL's α_*, near α→0 and α→1/2, at very large and random m; derived the asymptotic sign of the correction from ζ(2α)<0 independently of the heat-kernel argument; re-derived the periodization rearrangement; checked the Bessel monotonicity input by continued fractions. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0096's numerical floor (DISC-0096 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0096. Mathematical. Theorem AL; AM replaces the single-side path by the full boundary cycle, R^cyc_∞=(1−α)R_∞.
- DISC-0094. Mathematical. Theorem AK; AM uses σ_AK with the new ‖F_frac‖ floor.
- DISC-0072. Mathematical. Theorem AA; same Löwner–Heinz embedding mechanism.
- DISC-0099. Failed hypothesis. Kept Failure AM.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges and whether L≥0.70. DISC-0099 shows no resistance ceiling in the σ_AK chain can reach 0.70; a share floor near the live σ_n≈1.35 would be needed.

## Next Experiments

None required.

## Reproduction Instructions

`git checkout 0a11b759297d446a05f203ae18aea505e6fa4e86 && python3 scripts/gasket_fractional_cycle_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AM.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AM.log`, `/workspace/scratch-ifi/indep_theorem_AM.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AM at 0a11b759297d446a05f203ae18aea505e6fa4e86; repo witness EXIT 0 (164 PASS); independent check ALL PASS (156 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-15. Initial archive entry.
