# Discovery: Spectral decimation of the corner resolvent; ‖F(n,0.45)‖ strictly decreases to 𝓛∈[0.819255, 0.822959] (Theorem AQ; proves Conjecture J.1)

## Discovery ID

DISC-0106

## Status

THEOREM

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0104, DISC-0105, DISC-0107, and DISC-0108.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 4b4509f6f086f3f52b034f55508862f130381f2b (main HEAD at archive time, 2026-10-22 02:19 EDT). Paths: GASKET.md "Theorem AQ. Spectral decimation of the corner resolvent: the audit norm decreases to a limit in [0.819,0.823]" (ASSUMPTION, THEOREM AQ items 1–5, Proof (1)–(5), Witness, table, Kept Failure AQ.1, OBSERVATION, NOT THIS); GASKET.md "Conjecture J.1" header changed to "Status: PROVED by Theorem AQ (formerly a conjecture; the text below records it as first stated)", statement body unchanged; "What this does not say" bullets re-headed "LIMIT AT α=0.45: SETTLED BY THEOREM AQ" / "SETTLED (Theorem AQ)"; CLAIM_STATUS.md audit-norm row "LIMIT SETTLED" and new AQ row ("supersedes the 'Conjecture J.1 OPEN' notes in the rows above"); README.md Sequel; scripts/gasket_fractional_decimation.py (new); scripts/cli.py.

## Original Evidence

GASKET.md Theorem AQ (G_n = build_gasket level n, v=e_a−e_b, r_n(s)=½vᵀ(L_n+s)⁻¹v, R_α(n)=vᵀ(L_n^α)⁺v; Theorem AB, the pairing ‖F_frac‖=√21/(3R_α) (AA/AD/AE), and Theorem AP (1) used as stated; item 5 rests on an outward-rounded mpmath.iv certificate at 30 digits):
1. Exact decimation: Schur(L_{n+1}+s → V_n)=c(s)L_n+(2e(s)+s)I−e(s)P_C, c=(6+s)/((5+s)(2+s)), e=2s/(2+s), (2e+s)/c=s(s+5); hence r_0=1/(3+s), r_{n+1}(s)=Φ_s(r_n(s(s+5))), Φ_s(x)=(2+s)(5+s)x/((6+s)−2s(5+s)x).
2. Stieltjes: R_α(n)=(2 sin πα/π)∫s^(−α)r_n ds; σ_n=½vᵀL^βv=(sin πβ/π)∫s^(β−1)(1−s r_n) ds.
3. r_n(s)<r_{n+1}(s) for all s>0, n≥0 ⇒ R_α(n) strictly increases, σ_n strictly decreases, ‖F(n,α)‖=σ_n√21/(3R_α(n)) strictly decreases and converges, for every α∈(0,1).
4. Pointwise ceilings r_n≤T^k(1/s) for all n,k; r_n≥T^k r_0 for n≥k; power supersolution Bs^(−β′) on (0,σ₀] under (C1)–(C3), β′∈(1−log3/log5, 1−α).
5. At α=0.45 (β′=0.35, σ₀=0.01, B≈0.892577, X≈2.555816, 18459 grid points on [1e−20,1e12]): R_0.45(n)<2.518955, σ_n>1.350986, ‖F_frac‖>0.606412 for every n≥1; ‖F(n,0.45)‖ strictly decreases to 𝓛∈[0.819255, 0.822959]; "This is Conjecture J.1 … now proved"; also S_AP·√21/(3R̄)≈0.794563≥0.70 closes AP.1's open step.

## Discovery

The antisymmetric corner resolvent of the combinatorial gasket obeys an exact one-dimensional renormalization map under midpoint decimation. Through two Stieltjes integrals this gives monotonicity in the level of both factors of ‖F‖=σ_n‖F_frac‖ for every α∈(0,1), so the audit norm strictly decreases and converges; an interval certificate at α=0.45 bounds the limit to [0.819255, 0.822959]. This proves the repository's Conjecture J.1 as stated (decrease for every n≥1, existence of the limit, L≥0.70). It does not give 𝓛 in closed form, and gives no positive limit for α≥log3/log5 (Kept Failure AQ.1, DISC-0107). Not thrust.

## Why It Matters

It settles the single open mathematical question of the gasket note recorded in this archive as DISC-0034 (J.1). It supersedes every floor in the chain DISC-0088…DISC-0104 (0.274743 / 0.415238 → 0.819255) and closes the step DISC-0105 (AP.1) called open (R̄=2.518955<2.859237). The limit of a graph audit norm of corner currents is not a force and not thrust.

## Derivation

Repository proof, checked step by step in this archive (hardest-attack pass):
1. Decimation. Every edge of G_n lies in exactly one unit cell; the midpoints of G_{n+1} have degree 4 with all edges in one cell, so the midpoint block is block-diagonal by cell; one cell gives c(3I−J)+eI; corners lie in one cell, other old vertices in two, so the sum is cL_n+e(2I−P_C)+sI. Corner block of an inverse = inverse of the Schur complement; S₃ symmetry decouples the zero-sum corner mode; Woodbury on −eP_C gives μ↦μ/(1−eμ); with the factor 1/c this is Φ_s. Archive: exact Fraction identities at 40 random rational s; recursion = EXACT rational ½vᵀ(L_n+s)⁻¹v on levels 0–4; Schur identity on own graphs n=0→1…5→6 (err ≤9e−16); recursion = dense solve on levels 0–8 (N up to 9843).
2. Stieltjes formulas: standard (λ^(−α) and λ^β integrals; v⊥ker L; |v|²=2). σ_n=½vᵀL^βv follows from AP (1) plus the a↔b reflection; archive re-derives it from the S₃ form pI+qJ of the corner block of L^β, which gives the full vector identity I=(p−q)I^α (so AB's ‖F‖=σ_n‖F_frac‖ is also re-derived). ‖F_frac‖=√21/(3R): Schur complement κ(3I−J) with κ=2/(3R), I^α=κ(5/2,−2,−1/2), and |(5/2)P_a−2P_b−(1/2)P_c|=√21/2 on the unit equilateral triangle — exact.
3. Monotonicity is proved for ALL n by algebra, not by finite-n numerics plus extrapolation: r_n≤1/s; den(Φ_s) at x=1/s′ equals 4+s>0, Φ_s′>0 there; base r_1−r_0=(s+6)/((s+3)(s²+7s+9))>0; induction in n uniformly in s. Integrands are strictly monotone in r_n.
4. Order preservation of T on 0≤f≤1/s, T(1/s)=(2+s)/(s(4+s))<1/s, r_{m+k}=T^k r_m; power-branch induction: (C1) is equivalent to Φ_s(Bs′^(−β′))≤Bs^(−β′) and forces a positive denominator (so Φ_s stays on its increasing branch); the left side of (C1) increases in s, so checking at s* suffices; (C2) is checked on subintervals with a valid lower bound of the denominator and upper bound of the numerator; (C3) is the base case.
5. Quadrature bounds use only r_n decreasing in s and s·r_n increasing in s (both true termwise in the spectral sum); tails (0,s₀] by the power branch, [G,∞) by r_n≤1/s and 1−s r_n≤3/(3+s). The LOWER end of 𝓛 (the one that discharges J.1) uses only all-n bounds (R̄, σ_lo), so ‖F(n,0.45)‖≥0.819255 holds at every level directly, independent of monotonicity; the upper end needs n≥36 and is only used for the limit.

## Assumptions

Spectral calculus (GASKET item 4); corner data (1,−1/2,0); Theorems AB (DISC-0076), AA/AD/AE pairing (DISC-0072/0080/0082), AP (1) (DISC-0104) as stated — all three re-derived independently in this archive (see Derivation 2). No dependence on the finite-range defect constants of AN/AO (DISC-0100/0102), on AM, on any Harnack step, or on any open conjecture; no circularity (the recursion comes from graph structure only). Item 5 is computer-assisted: an outward-rounded interval-arithmetic certificate. Minor rigor note: the repository certificate encloses the binary double 0.45000000000000001110…, not 9/20 exactly (difference 1.1e−17, immaterial); the archive certificate below encloses α=9/20 exactly.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AQ.log` (repository witness `python3 scripts/gasket_fractional_decimation.py` at 4b4509f6f086f3f52b034f55508862f130381f2b, EXIT 0, 69 PASS, 0 FAIL, 2 min 43 s; prints R̄=2.518955, σ_lo=1.350986407, ‖F_frac‖≥0.606412, L∈[0.819255, 0.822959], k≤36) and `/workspace/scratch-ifi/indep_theorem_AQ.py` / `indep_theorem_AQ.log` (own builder, no repo import; numpy + mpmath + mpmath.iv + fractions; EXIT 0, 62 PASS, 0 FAIL, ALL PASS, 2 min 46 s):
- A–C: exact algebra, exact rational resolvent levels 0–4, Schur decimation n≤5→6, recursion vs dense through level 8 (above);
- D: FIRST-PRINCIPLES ‖F(n,0.45)‖ (eigh, L^α Dirichlet minimizer, combinatorial corner currents, geometric audit norm) on levels 1–7 equals the recursion-Stieltjes value to <1e−8: 1.439599390, 1.165908607, 1.032271686, 0.956205578, 0.909692382, 0.880108995, 0.860818…; also at α∈{0.1,0.3,0.6} levels 1–5;
- E: r_n≤r_{n+1} on a 61-point log grid for n<80 (40 digits); R strictly up and ‖F‖ strictly down along n=1…12,15,…,60; repository table (n=1,2,6,10,20,40) reproduced to 6 digits; recorded matrix-free ‖F_frac(9)‖, ‖F_frac(10)‖, ‖F(10)‖=0.833640 reproduced; R gap ratios → 0.6877 = 5^α/3; ‖F(60,0.45)‖=0.821138627;
- F: OWN interval certificate with exact α=9/20 enclosure and different parameters (β′=0.33, σ₀=0.005, s₀=1e−24, G=1e14, grid ratio 1.003, 29211 points, depth ≤42, plus certified tails 1−s r_n≥2/(4+s) and r_n≥1/(3+s)): C1 lhs 5.938199<6, C2 on 1000 cells, C3; B=0.956868, X=3.202090; **R_0.45(n)≤2.518030 and σ_n≥1.351362 for all n; ‖F(n,0.45)‖≥0.819784 for every n; 𝓛∈[0.819784, 0.822494]** — inside and slightly tighter than the repository bracket; contains ‖F(60)‖;
- G: J.1 statement body identical at 7f0099c and 4b4509f (α=0.45, these corner data, decrease for every n≥1, lim=L≥0.70);
- H: Kept Failure AQ.1 reproduced (DISC-0107).

## Prior Art

Spectral decimation on the Sierpinski gasket is classical (Rammal–Toulouse; Fukushima–Shima; Strichartz/Teplyaev) and Stieltjes representations of fractional powers are standard; the application to this repository's audit functional is in-repo. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete proof in the repository, computer-assisted by a rigorous interval certificate, verified and independently re-certified here). Not a novelty claim; no world-first claim.

## Falsification Attempts

Attacked every item named for this pass: (a) decimation map compared exactly (rational arithmetic) and numerically against direct finite-level resolvents and first-principles ‖F(n,0.45)‖ on levels 1–7 — agree; (b) decrease is proven for all n by algebraic induction, not by finite numerics plus extrapolation; (c) the bracket is an outward-rounded interval certificate, reproduced independently with different parameters and exact α — not a float estimate; (d) J.1's precise statement (α=0.45, corner data (1,−1/2,0), the same geometric audit norm, decrease for every n≥1, L≥0.70) is exactly what items 3 and 5 deliver; (e) dependencies AB/pairing/AP (1) re-derived, no unproved conjecture used; (f) the discharge uses the floor (lower end, all-n bounds), not the upper end. Numerical caveat only: strict increase of r_n and strict decrease of σ_n are below floating resolution for large n (σ_10−σ_20≈2.6e−9), so strictness there rests on the algebra, as the repository says. No gap found.

## Experimental Validation

None (pure mathematics; computer-assisted certificate).

## Mathematical Status

Proved in-repo; proof, witness, and certificate verified; certificate independently reproduced. Changes DISC-0034's status for J.1 from CONJECTURE to THEOREM (status-change note appended to DISC-0034; history preserved). J.2 (α=0.10) is not decided and is carried forward as DISC-0108 (CONJECTURE). Closed form of 𝓛 OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0034. Conjecture J.1 → THEOREM via this row (status-change note on DISC-0034).
- DISC-0104. Mathematical. Theorem AP (1) used for σ_n=½vᵀL^βv; AP's floors superseded.
- DISC-0105. Failed hypothesis. AP.1's open resistance ceiling supplied here (R̄=2.518955<2.859237).
- DISC-0076, DISC-0072, DISC-0080, DISC-0082. Mathematical. AB factorization and AD/AE pairing used.
- DISC-0107. Failed hypothesis. Kept Failure AQ.1.
- DISC-0108. Conjecture. J.2 carried forward (not decided by AQ).
- DISC-0035. Conjecture (archive-derived). Predicted L(0.45)≈0.8211 lies inside the certified bracket; the fitted law itself is not proved here.
- DISC-0080, DISC-0032. Mathematical. Theorems AD / K consistent with AQ.1 (limit 0 for α≥log3/log5).

## Open Questions

Closed form of 𝓛 (≈0.821139); a certified bracket narrow enough to decide J.2 (DISC-0108).

## Next Experiments

Optional: run the repository certificate at α=0.10 with a much finer grid / higher G to try to decide J.2 (margin ≈6.4e−4).

## Reproduction Instructions

`git checkout 4b4509f6f086f3f52b034f55508862f130381f2b && python3 scripts/gasket_fractional_decimation.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AQ.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AQ.log`, `/workspace/scratch-ifi/indep_theorem_AQ.log`.

## Evidence Log

- 2026-10-22. Recorded from GASKET.md Theorem AQ at 4b4509f6f086f3f52b034f55508862f130381f2b; repo witness EXIT 0 (69 PASS); independent check ALL PASS (62 PASS) including the independent interval certificate. Repository description still matches its claim fence (closed-surface identity / not a net force; no J.1 or thrust wording).

## Change History

- 2026-10-22. Initial archive entry.
