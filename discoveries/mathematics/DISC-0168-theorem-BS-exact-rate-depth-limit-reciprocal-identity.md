# Discovery: Theorem BS, below log3/log5 ρ^N C_N reaches c_∞ at the exact rate ρ^N (c_∞−ρ^N C_N=ρ^N χ_N, χ_N→χ_∞∈(0,∞)), via an exact scaled reciprocal identity 1/𝓡=1/Q_∞+Φ; certified C_N for N=1–6

## Discovery ID

DISC-0168

## Status

THEOREM in the mathematical sense only (repository proof; constants computer-assisted with python-flint arb). Method KNOWN (scaled limit of an exact one-level identity, dominated/monotone convergence, interval Riemann sums of monotone integrands). Closed forms for χ_∞, C_N, P_N, c_∞ (all expressed through one unknown log-periodic function u^(1−γ)Q_∞(u)) and novelty UNRESOLVED. No Kept Failure in this commit. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~3:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 316ee92917b18b6c95346b02c2e1fd7f7bb05dac (committed 2026-10-23 3:02pm EDT).

## Original Evidence

GASKET.md Theorem BS (heading at GASKET.md line 2786, statement line 2792, Conjecture BS.4 line 2831, AT.1-derived identification line 2833, proofs of BS.1 line 2835 and BS.3 line 2844, "What stays open" line 2852, NOT-THIS fence line 2857, witness list line 2859), CLAIM_STATUS.md new row (line 75), README.md OPEN paragraph and reproduction list, scripts/gasket_fractional_deficit_correction.py (new, 414 lines), scripts/cli.py, tests/test_cli.py (FractionalDeficitCorrectionTests), all at 316ee92917b18b6c95346b02c2e1fd7f7bb05dac. Builds on Theorem BR (DISC-0167, bed41594e18c), Theorem BQ (DISC-0165, 01c39d01aa86), BJ.1/BJ.3 (DISC-0153), BH.2 (DISC-0149), BG.3 (DISC-0146), AQ (3), BD.4, BJ.6, BL.1. The repository's own git grep shows no "Kept Failure BS".

## Discovery

Setting as in BG/BH/BJ/BQ/BR: p(z)=z(z+5), β=(z+6)/((z+2)(z+5)), η=lim η_N (η_0=−1/2), ψ(v)=lim p^k(5^−k v), ρ=5^α/3, γ=log3/log5, 𝓡(u)=lim (3/5)^M r_M(5^−M u), P_N=∫u^−α 𝓡(u) η_N(ψ(5^−N u))du, C_N=P_N/D_∞ (BQ.2), c_∞=lim ρ^N C_N (BR.4).

BS.1 (every u>0, no α): Q_∞(u)=lim (3/5)^M r_∞(5^−M u) exists without AT.1; 1/𝓡(u)−1/Q_∞(u)=Φ(u):=(1+2η(ψ(u)))∏_(k≥1)(5/3)β(ψ(5^−k u))∈(0,3]; Q_∞ nonincreasing, Q_∞(5u)=(3/5)Q_∞(u) (u^(1−γ)Q_∞ multiplicatively 5-periodic), g_lo u^(γ−1)≤Q_∞≤g_hi u^(γ−1) for every u; 1/Q_N(t)=1/Q_∞(t)+(3/5)^N Φ(5^N t), so c_∞D_∞=∫t^−α Q_∞(t)η(ψ(t))dt (replaces BR.4's AT.1-derived formula).

BS.2 (α∈(0,γ), N≥1): c_∞−ρ^N C_N=ρ^N χ_N, χ_N=(A_N+B_N)/D_∞, A_N=∫u^−α h(u)η(ψ(5^−N u))du with h=Q_∞−𝓡=Q_∞²Φ/(1+Q_∞Φ)>0 strictly increasing to J=∫u^−α h∈(0,∞); B_N=∫u^−α 𝓡∏_(k=1..N)β(ψ(5^−k u))(1/2+η(ψ(u)))du with 0<B_(N+1)≤(3/5)B_N. Hence χ_N→χ_∞=J/D_∞, C_N=c_∞ρ^−N−χ_∞+o(1); rate ρ^N exact (χ_N≥A_1/D_∞>0 and bounded); χ_N−χ_∞≤(3/5)^(N−1)B_1/D_∞.

BS.3 (certified, printed 6 digits; see erratum): χ_∞(0.01)∈[0.016049,0.016055], χ_∞(0.1)∈[0.156240,0.156355], χ_∞(0.3)∈[0.438643,0.438973], χ_∞(0.45)∈[0.633344,0.633869]; J(0.45)∈[2.534835,2.535667]; at 0.45: C_1..C_6∈[0.071899,0.071951], [0.458110,0.458442], [0.964854,0.965556], [1.692718,1.693950], [2.749351,2.751355], [4.285424,4.288550]; every N≥6 χ_N(0.45)∈[0.618141,0.649097]; C_1 inside BQ.3's independent bracket at all four α; A_N+B_N certified strictly decreasing N=1–5 at 0.45 (Conjecture BS.4, DISC-0169).

Derived (AT.1 as used in BH.6, as stated): if u^(1−γ)Q_∞(u)=Θ_AT(ψ(u)), then c_∞(α)=θ_∞^BH(α), so BH's float θ_∞(0.45)≈0.52061 (DISC-0150) lies in BR.5's bracket — derived level only.

## Why It Matters

Answers DISC-0167's (Theorem BR) open questions "rate of ρ^N C_N→c_∞" (exactly ρ^N, with an explicit positive limit χ_∞ of the renormalised gap) and "certified C_N for individual N≥2" (N=1–6 at four exponents), and DISC-0165's open "N≥2 certificates". It also removes AT.1 from the c_∞ formula (Q_∞ exists unconditionally) and gives a second, tighter C_1 bracket by a different route from BQ.3.

## Derivation

Repository proof (GASKET.md Theorem BS). Re-derived this slice: BS.1 by setting s=5^−M u in BJ.1, multiplying by (5/3)^M and reindexing k=M−i; each factor (5/3)β∈(0,1] since 1−(5/3)β=x(3x+16)/(3x²+21x+30), and Σ−log factors converges because ψ(5^−k u)≤5^−k u e^(u/10); the BJ.3 bracket transports through (3/5)^M(5^−M u)^(γ−1)=u^(γ−1). BS.2 by the change of variables t=5^−N u (ρ^−N t^−α(5/3)^N dt=u^−α du) and the split Q_∞η−𝓡η_N=(Q_∞−𝓡)η+𝓡(η−η_N), with BH.2's remainder η−η_N=∏β(p^i z)(1/2+η(p^N z)) at z=ψ(5^−N u); B_(N+1)≤β(0)B_N=(3/5)B_N because β is decreasing; J<∞ because h≤Q_∞≤g_hi u^(γ−1) near 0 (integrable iff α<γ) and h≤Q_∞²Φ=O(u^(2γ−4)) at ∞.

## Assumptions

Used as stated by the repository, not re-run there or here: AQ (3), BD.4, BJ.6's ψ(v)≤ve^(v/10), BG.3, BH.2, BJ.1, BJ.3 (g_lo=0.600945014, g_hi=0.600963487), BL.1, BQ.2–BQ.3 (C_N=P_N/D_∞, D_∞ routine), BR.4; AT.1 for the derived identification only. α<γ for BS.2–BS.3. Certificates pointwise in α.

## New Results

Exact scaled reciprocal identity 1/𝓡=1/Q_∞+Φ with explicit Φ; unconditional existence and 5-scaling of Q_∞; exact two-integral representation of c_∞−ρ^N C_N; exact rate ρ^N with χ_∞∈(0,∞); certified χ_∞ at four exponents and C_N, ρ^N C_N, χ_N for N=1–6.

## Prior Art

Scaled limits of exact renormalisation identities, monotone/dominated convergence and interval quadrature of monotone integrands are standard (renormalisation-map analysis on p.c.f. fractals is a known framework). No literature search on these specific gasket constants; not searched further.

## Novelty Analysis

Method KNOWN. Novelty of χ_∞(α), C_N(α) and of the identity on this specific operator UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Repository witness /workspace/ifi-br/scripts/gasket_fractional_deficit_correction.py at 316ee92917b1: EXIT 0, 183.4 s script time (184 s wall), every check "ok", "all Theorem BS checks passed" (/workspace/scratch-ifi/repo_theorem_BS.log). The same arb computation re-printed with 10 digits via a wrapper that only changes the print format (/workspace/scratch-ifi/run_BS_fullprec.py → repo_theorem_BS_fullprec.log, EXIT 0, 185 s).
(2) Archive /workspace/scratch-ifi/indep_theorem_BS.py, 63/63 PASS (/workspace/scratch-ifi/indep_theorem_BS.log): sympy 1−(5/3)β, β decreasing with β(0)=3/5, β≤1/x, h=Q²Φ/(1+QΦ) and the four monotonicity derivatives, 5^(γ−1)=3/5, the t=5^−N u Jacobian, 1/Q_N=1/Q_∞+(3/5)^NΦ(5^N t); exact J-tail constant (25/9)·125, geometric sums, η_N(0)=1−(9/10)(3/5)^(N−1) (=DISC-0167's 1−(3/2)(3/5)^N), finite BH.2 remainder identity (source of B_N); from the full-precision log: χ_∞=J/D_∞ rebuilt from printed J, D_∞ at all four α; ρ^N C_N = ρ^N×C_N; c_∞=ρ^N(C_N+χ_N) intervals for N=1–6 have a common point meeting BR.5's outward bracket at all four α; C_1 inside BQ.3; ρ^N C_N strictly increasing N=1–6; χ_N−χ_∞ ≤ (3/5)^(N−1)B_1/D_∞ not contradicted; every-N bracket [A_1/D_hi,(J+B_1)/D_lo] contains each χ_N. Independent float model (own code, different route: r_∞=1/(s+2(1−η(s))) with 1−η computed by the cancellation-free recursion 1−η=z/(z+2)+β(1−η∘p); Q_∞ as (3/5)^M r_∞(5^−M u) at 5^−M u≈5^−170; Φ by its product; log-grid trapezoid; no use of the repository's ⟨Θ⟩ approximation): g(s)=s^(1−γ)r_∞ at s=1e−12…1e−80 inside BJ.3's bracket; Q_∞(5u)/Q_∞(u)=3/5; Φ(0+)=3, decreasing; D_∞(0.45)=4.0013017735 (matches BQ/AS float 4.0013017734819 to 1e−12) and D_∞ inside the certified bracket at all four α; c_∞(0.45)=0.5206072, χ_∞(0.45)=0.6336065, C_1(0.45)=0.0719251, C_6(0.45)=4.2869868, and c_∞, χ_∞, all C_N, χ_N (N=1–6) inside the certified brackets at α=0.01, 0.1, 0.3, 0.45; the identity χ_N=(A_N+B_N)/D=(c_∞−ρ^N C_N)/ρ^N holds to 1e−9 numerically.
(3) Logic attack: (a) lower/upper Riemann sums need each true integrand nonincreasing in u — Q_∞, 𝓡, Φ, η∘ψ, η_N∘ψ (BL.1), β∘ψ are, and h is increasing in (Q,Φ), both nonincreasing; (b) the Φ lower bound uses ∏(1−c_k)≥1−Σc_k with c_k≤x_k(3x_k+16)/30, x_k≤5^−j w — reproduced; (c) tails use ψ(v)/v nondecreasing, η,η_N≤2/z, β≤1/z; heads use 𝓡≤1/3, h≥Q−1/3, ∏β≤(3/5)^N — all consistent with stated assumptions. (d) Weak point noted, not a fault: the repository's "c_∞ meets BR.5" check is not independent of BR.5 (both are [g_lo,g_hi]·M_α/D_∞ with the same D_∞ routine); the C_1 vs BQ.3 check is a genuinely different route (shares only the D_∞ routine). No mathematical failure found. Arb cells were not independently re-certified.

Erratum (printed constants, no effect on any claim): as in BR (DISC-0167), the script prints 6-digit endpoints with round-to-nearest (Python :.6f), not outward. Against the full-precision arb endpoints, 113 of 224 printed endpoints in the witness output are on the inward side, by at most 4.74e−7. Affected headline values (outward 6-digit): χ_∞(0.01)∈[0.016048,0.016056], χ_∞(0.1)∈[0.156239,0.156355], χ_∞(0.3)∈[0.438643,0.438974] (χ_∞(0.45) printed bracket is already outward); C_1(0.45)∈[0.071899,0.071952], C_2(0.45)∈[0.458109,0.458443], C_4(0.45)∈[1.692718,1.693951], C_5(0.45)∈[2.749351,2.751356], C_6(0.45)∈[4.285423,4.288551] (C_3 already outward); D_∞(0.45)∈[4.000301,4.002303]. The script's own pass/fail checks compare arb balls, not printed strings, so they are unaffected.

Archive-derived (from the repository's own full-precision enclosures; not stated or certified by the repository): intersecting the six enclosures c_∞=ρ^N(C_N+χ_N), N=1–6, gives c_∞(0.45)∈[0.52041409,0.52080033], slightly tighter than BR.5's outward [0.520386,0.520825]. Recorded as a consistency note only.

## Experimental Validation

Computational only. Repository witness logs and archive log as above.

## Mathematical Status

Theorem (mathematical sense; BS.3 constants computer-assisted; c_∞=θ_∞^BH derived from AT.1 only).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0167 → DISC-0168 (mathematical: answers BR's open rate of ρ^N C_N→c_∞ and individual-N certificates; replaces BR.4's AT.1-derived c_∞ formula). DISC-0165 → DISC-0168 (mathematical: C_N=P_N/D_∞, D_∞ routine; BQ.3's C_1 independently reproduced and tightened; BQ's N≥2 certificates supplied). DISC-0153 → DISC-0168 (mathematical: BJ.1 identity scaled; BJ.3 bracket transported to every u). DISC-0149 → DISC-0168 (mathematical: BH.2 remainder gives B_N). DISC-0168 → DISC-0169 (mathematical: Conjecture BS.4). DISC-0168 → DISC-0150 (mathematical, derived only: c_∞=θ_∞^BH under AT.1; BH.7 not decided). DISC-0166 unchanged (eventual monotonicity of V^(n) still open). DISC-0159's limit clause (above γ) unchanged.

## Open Questions

Closed form for the log-periodic u^(1−γ)Q_∞ (hence c_∞, C_N, P_N, χ_∞); a rate for J−A_N; Conjecture BS.4 (DISC-0169); brackets uniform in α; tighter D_∞ (now the width-limiting factor, relative ~5e−4); eventual monotonicity of V^(n) (DISC-0166); a* closed form; Conjecture BL.6's limit part (DISC-0159); Conjecture BH.7 (DISC-0150).

## Next Experiments

Tighten D_∞ to separate A_5+B_5 from A_6+B_6; prove the archive float observation that χ_N−χ_∞ shrinks by ≈5.00 per step at all four α (DISC-0169), i.e. that the (3/5)^N parts of J−A_N and B_N cancel; certify χ_∞(α) monotone in α (0.0160, 0.1562, 0.4388, 0.6336 at 0.01, 0.1, 0.3, 0.45).

## Reproduction Instructions

git -C informational-flux-identity checkout 316ee92917b18b6c95346b02c2e1fd7f7bb05dac; python3 scripts/gasket_fractional_deficit_correction.py (≈183 s; sympy, mpmath, python-flint). Full-precision print: python3 /workspace/scratch-ifi/run_BS_fullprec.py (from the repo root). Archive: python3 /workspace/scratch-ifi/indep_theorem_BS.py (≈5 s; needs both logs and /workspace/scratch-ifi/bs_floats.py).

## Evidence Log

- 2026-10-23 ~3:57pm EDT. Indexed; repo witness EXIT 0 (183.4 s); independent checks 63/63 PASS; rounding erratum recorded.

## Change History

- 2026-10-23. Initial archive entry.
