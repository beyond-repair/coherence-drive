# Discovery: Exact refinement rates of the corner-resolvent integrals (Theorem AR)

## Discovery ID

DISC-0109

## Status

THEOREM (mathematical sense only; proof in the repository, conditional on the interval-certified power ceiling of Theorem AQ, DISC-0106). Novelty: UNRESOLVED (the method is classical renormalization/Koenigs linearization applied to the repository's own recursion; the specific constants are not found in a quick search, which is not a prior-art search). Not thrust.

## Date Discovered

2026-10-22 (America/New_York). Commit authored 2026-10-22 03:17 EDT; archived ~04:05–04:30 EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3ec0a064caa5c70d6c4bfb23e7c37af89091abb2. Paths: GASKET.md "Theorem AR. Exact refinement rates" (Setting, THEOREM AR items 1–4, Proof, Witness table, KEPT FAILURE AR.1, NOT THIS); CLAIM_STATUS.md row "Exact refinement rates of the corner resolvent integrals"; README.md Sequel; scripts/gasket_fractional_decimation_rate.py (new, 193 lines); scripts/cli.py registry line.

## Original Evidence

With r_n(s)=½vᵀ(L_n+s)⁻¹v, r_(n+1)(s)=Φ_s(r_n(p(s))), p(s)=s(s+5), q=p⁻¹, δ_n=r_n−r_(n−1), ρ=5^α/3, μ=ρ/5, γ=log3/log5:

1. Product formula δ_(n+1)(qⁿ(u))=P_n(u)δ_1(u), P_n=∏_(j=1..n) D_j(q^j u), D_j the Möbius secant slope of Φ_s between r_(j−1)(ps) and r_j(ps); D_j(s)≥(2+s)(5+s)/(6+s)≥5/3, so (3/5)ⁿP_n ↑ P_∞<∞ (finiteness uses AQ's ceiling r_n(s)≤Bs^(−0.35) on (0,0.01]).
2. R_α(n+1)−R_α(n)=c_R(α)ρⁿ(1+o(1)) and σ_n−σ_(n+1)=c_S(α)μⁿ(1+o(1)), 0<c_R,c_S<∞, with c_R, c_S integrals of the Koenigs function Ψ=lim 5ⁿqⁿ against P_∞δ_1 (dominated convergence).
3. σ_n>σ_∞≥2·4^(−α).
4. α<γ: ‖F(n,α)‖−𝓛(α)∼Cρⁿ (gap ratio exactly 5^α/3); α=γ: R_γ(n)=c_R(γ)n+o(n), ‖F(n,γ)‖∼√21σ_∞/(3c_R(γ)n); α>γ: ‖F(n,α)‖=Θ((3·5^(−α))ⁿ).

Repo witness table: c_R(0.25)=0.37699178, c_R(0.45)=0.49780265, c_R(0.60)=0.52084941, c_R(γ)=0.51716583, c_R(0.75)=0.50798513 (float quadrature, not certified).

## Discovery

The approach of the fractional corner resistance and of the audit norm to their limits is exactly geometric with ratio 5^α/3 for every α∈(0,1), and the critical case α=log3/log5 has an exact linear slope. This turns the archive observation of DISC-0035 (difference ratios → 5^α/3) and AQ.1's measured increment ≈0.5172/level (DISC-0107, DISC-0080) into theorem statements, with the constants left as computed values.

## Why It Matters

It closes the rate question for the corner-resolvent family that DISC-0106 opened, sharpens Theorem AD's Θ(n) (DISC-0080) to an exact asymptotic slope, and makes Theorem K's decay (DISC-0032) quantitative with the exact ratio 3·5^(−α).

## Derivation

Checked in the archive: (i) Φ_s is Möbius, so its secant slope is (2+s)(5+s)(6+s)/(den(x)den(y)), den(x)=(6+s)−2s(5+s)x; with r>0, den≤6+s gives the 5/3 floor; (ii) substitution s=qⁿ(u) gives prefactor 5^(nα)·5^(−n)·(5/3)ⁿ=ρⁿ for R and 5^(−nβ)·5^(−n)·(5/3)ⁿ=μⁿ for σ (β=1−α); (iii) ∫₀^∞ s^(β−1)·2/(4+s) ds·sin(πβ)/π = 2·4^(β−1)=2·4^(−α); (iv) consequences by summing increments and ‖F‖=(√21/3)σ_n/R_α(n). The domination step (orbit points above 1 counted by log₂log u, √-factor cancellation by 5q′(u)≤5/(2√u)) is a sketch-level estimate in the repository; it was read, not re-proved line by line here.

## Assumptions

- Theorem AQ (DISC-0106) including its mpmath.iv-certified power ceiling r_n(s)≤Bs^(−0.35) on (0,0.01] (α-independent).
- Stieltjes representations of R_α(n) and σ_n (AQ (2)).
- The constants c_R, c_S are asserted to exist and be positive; their digits are floating-point quadrature, not certified.

## New Results

- Archive-independent values (own quadrature of s^(expo)δ_(n+1) directly, no cancellation): c_R(0.30)=0.41942808, c_S(0.30)=1.090541; c_R(0.80)=0.49837199, c_S(0.80)=0.2719273 (α values not in the repository table); c_R(0.45)=0.49780265, c_R(γ)=0.51716583, c_S(0.45)=0.927093 matching the repository.
- c_R(α) is not monotone in α on the computed points (0.377, 0.419, 0.498, 0.521, 0.517, 0.508, 0.498 at α=0.25, 0.30, 0.45, 0.60, γ, 0.75, 0.80): it peaks between 0.60 and γ. Observation only.

## Prior Art

Classical: spectral decimation on the Sierpinski gasket (Rammal–Toulouse 1983/84; Fukushima–Shima 1992; Strichartz, Teplyaev), resistance renormalization 5/3 (Kigami), Koenigs linearization at an attracting fixed point (Koenigs 1884), Stieltjes/Balakrishnan representation of fractional powers. Theorems AD, K, AQ in the same repository (DISC-0080, DISC-0032, DISC-0106). No search of the fractional-Laplacian-on-gasket-graph literature for these exact constants has been done.

## Novelty Analysis

The rates themselves are what renormalization theory predicts (spectral dimension d_s=2log3/log5, so α=d_s/2 is critical). What may be specific is the exact corner-resolvent bookkeeping (product formula with Möbius secant slopes) and the constants c_R, c_S for this audit construction. UNRESOLVED; no novelty claimed.

## Falsification Attempts

- Exact Fraction algebra at 60 random rationals: secant identity, 5/3-floor identity, δ_1 closed form, q(u)=u/(5+q(u)). PASS.
- Product formula at 12 (u,n) pairs outside the repository's set, 60 digits: max relative error 2.6e−59. PASS.
- (3/5)D_j ≥ 1 on s∈[1e−15,1e15], j<40 (min 1.0 to 25 digits); (3/5)D_j−1 < 1e−4 for j≥30 at s<1e−6. PASS.
- c_R, c_S converge (n=12,16,20) at α∈{0.30,0.45,γ,0.80}. PASS.
- σ_18 > 2·4^(−α) at α∈{0.10,0.45,0.80}. PASS. ‖F(10,0.45)‖=0.83363971 matches recorded 0.833640. Gap ratio at 0.45 (n=16–18) 0.68715 vs 5^0.45/3=0.68773. PASS.
- One archive check FAILED as first written: at α=0.80 the ‖F‖ ratio at n=15→16 was 0.82152 vs the claimed limit 3·5^(−0.8)=0.82784. Follow-up at n=25, 35, 45 gives errors 9.3e−4, 1.4e−4, 2.1e−5, shrinking geometrically (≈ρ^(−10) per 10 levels, the expected constant-term correction). The failure was an over-tight tolerance on a slowly converging ratio, not a contradiction; the limit claim survives. Logged here rather than hidden.
- R_γ(40)/40=0.5347 vs c_R(γ)=0.5172: consistent with c_R n + const (o(n)).

## Experimental Validation

Computational only. Repo witness: /workspace/scratch-ifi/repo_theorem_AR.log, EXIT 0, 25 PASS lines, ~7 s. Archive independent: /workspace/scratch-ifi/indep_theorem_AR.py + indep_theorem_AR.log (22 PASS, 1 FAIL explained above, EXIT 1 as written) and indep_theorem_AR_alpha08.py + indep_theorem_AR_alpha08.log (4 PASS, EXIT 0). numpy-free, mpmath + fractions only. Both on the box, not committed to the source repository.

## Mathematical Status

Theorem (conditional on AQ's interval certificate, which DISC-0106 already verified). Constants: computed, not certified. Closed forms of c_R, c_S, 𝓛: OPEN.

## Patent Relevance

None. Pure mathematics on a graph audit norm.

## Related Discoveries

- DISC-0106. Mathematical. Theorem AQ supplies the recursion, Stieltjes formulas and the power ceiling AR needs.
- DISC-0035. Computational → mathematical. The archive law's difference-ratio limit 5^α/3 is now proved asymptotically (for α≠γ, and ratio 1 at γ); the exact affine form A+Bρⁿ stays a heuristic (row not edited, status unchanged CONJECTURE).
- DISC-0080. Mathematical. Theorem AD's Θ(n) at γ sharpened to the exact slope c_R(γ)≈0.517166 (AD floor slope c_AD=0.051634).
- DISC-0107. Mathematical. AQ.1's measured growth laws (≈0.5172/level at γ; ratio→5^α/3 above) are now theorem statements.
- DISC-0032. Mathematical. Theorem K's ‖F‖→0 above γ gets the exact rate Θ((3·5^(−α))ⁿ).
- DISC-0108. Mathematical. AR's floor σ_∞≥2·4^(−0.1)≈1.741 does not decide J.2 (needs 𝓛(0.10)≥1.410 via R ceiling); J.2 stays CONJECTURE.
- DISC-0110. Failed hypothesis. Kept Failure AR.1.

## Open Questions

- Closed forms or certified digits for c_R(α), c_S(α); location of the maximum of c_R on (0,1).
- Second-order correction at α=γ (the constant in R_γ(n)=c_R n + C + o(1)).

## Next Experiments

- Interval-certify c_R(0.45) and c_R(γ) with mpmath.iv along the same lines as AQ's certificate.
- Use 𝓛(0.10) from the recursion plus AR's rate to decide Conjecture J.2 (DISC-0108) numerically, then seek a certificate.

## Reproduction Instructions

git clone https://github.com/beyond-repair/informational-flux-identity && cd informational-flux-identity && git checkout 3ec0a064caa5c70d6c4bfb23e7c37af89091abb2 && python3 scripts/gasket_fractional_decimation_rate.py (exit 0 expected, ~7 s).

## Evidence Log

- 2026-10-22. Read GASKET.md Theorem AR at 3ec0a064caa5c70d6c4bfb23e7c37af89091abb2; repo witness EXIT 0; archive independent check as above.

## Change History

- 2026-10-22. Initial archive entry.
