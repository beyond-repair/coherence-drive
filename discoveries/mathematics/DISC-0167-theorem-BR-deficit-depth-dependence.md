# Discovery: Theorem BR, the corner deficit decreases in the depth N at every level, and below log3/log5 ρ^N C_N strictly increases to a finite limit c_∞(α)

## Discovery ID

DISC-0167

## Status

THEOREM in the mathematical sense only (repository proof; constants computer-assisted with python-flint arb). Method KNOWN (induction on the neighbour recursion, rescaling τ=5^N t, monotone convergence under a power-law majorant). Constants c_∞(α) closed form and novelty UNRESOLVED. No Kept Failure in this commit. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~1:59pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit bed41594e18cbcb7af443349e9e3c6ea11426c26 (committed 2026-10-23 1:11pm EDT).

## Original Evidence

GASKET.md Theorem BR (heading at GASKET.md line 2715, statement line 2721, proof of BR.5 line 2763, "What stays open" line 2771, NOT-THIS fence line 2776, witness list line 2778), CLAIM_STATUS.md new row (line 74), README.md OPEN paragraph and reproduction list, scripts/gasket_fractional_deficit_depth.py (new, 265 lines), scripts/cli.py, tests/test_cli.py (FractionalDeficitDepthTests), all at bed41594e18cbcb7af443349e9e3c6ea11426c26. Builds on Theorem BQ (DISC-0165, 01c39d01aa86), BH.2 (DISC-0149), BJ.2–BJ.3 (DISC-0153), BG.1/BG.3 (DISC-0146), AQ (3), BD.4, BI.4, BJ.4, AT.1 (derived part only). The repository's own git grep shows no "Kept Failure BR".

## Discovery

Setting as in BG/BH/BJ/BQ: p(z)=z(z+5), α_1=(z+4)/((z+2)(z+5)), β=(z+6)/((z+2)(z+5)), η_0=−1/2, η_N=α_1+β·η_(N−1)∘p, η=lim η_N, ρ=5^α/3, γ=log3/log5.

BR.1 (proved here, previously quoted from BH.2/BJ.4): η_N(z)≤2/(2+z) for every N≥0, by induction, since α_1+β=2/(2+z) and 2/(2+z)−(α_1+2β/(2+p))=z(z+6)/((z+2)(z²+5z+2))≥0.

BR.2: η_(N+1)(w)−η_N(p(w))=α_1−(1−β)η_N(pw)≥w/(w²+5w+2).

BR.3: for every α∈(0,1) and 0≤N<n, δ_N^(n)−δ_(N+1)^(n)≥D_n^−1∫s^−α r_n w/(w²+5w+2)ds>0, w=p^(n−N−1)s; so 3/2=δ_0^(n)>δ_1^(n)>…>δ_n^(n) at every level. Derived (BJ.4 as stated): δ_(N+1)<δ_N for the limit deficit above γ.

BR.4 (α<γ, N≥1): ρ^N P_N=∫t^−α Q_N(t)η_N(ψ(t))dt with Q_N=(5/3)^N R(5^N t) nondecreasing in N (AQ (3)) and η_N strictly increasing in N at fixed z (remainder identity (1/2+η)−β(1/2+η∘p)=1/2+1/(2(x+5))). So ρ^N C_N strictly increases and, bounded by BJ.2's Q_N≤g_hi t^(γ−1), converges to c_∞(α)∈[g_lo M_α/D_∞, g_hi M_α/D_∞], M_α=∫t^(γ−1−α)η(ψ(t))dt≤2^(γ−α)π/sin(π(γ−α)). Hence C_N has exact order ρ^−N, C_N∼c_∞ρ^−N. BQ-free floor ρ^N C_N≥L_1/D_∞. Derived from AT.1 as stated: c_∞=D_∞^−1∫t^(γ−1−α)Θ_AT(ψ t)η(ψ t)dt.

BR.5 (certified, printed to 6 digits): c_∞(0.01)∈[0.010439,0.010444], c_∞(0.1)∈[0.105440,0.105526], c_∞(0.3)∈[0.327320,0.327592], c_∞(0.45)∈[0.520387,0.520824]; every N≥1, ρ^N C_N(0.45)∈[0.049440,0.520824] (lower end = BQ.3's ρC_1). M_α brackets [1.7335799,1.7341000], [1.7583870,1.7589146], [2.1990754,2.1997359], [3.4657841,3.4668569]. See erratum below.

## Why It Matters

Answers DISC-0165's (Theorem BQ) open "N-dependence of C_N" question: C_N grows exactly like ρ^−N, with an increasing normaliser and a certified limit; the growth from N=1 to N=∞ is about ×10.5 at α=0.45 and genuine (ρC_1≤0.049490<0.520386≤c_∞). It also closes the BR.1 ceiling that BQ had only quoted. BR.3 is the depth-direction counterpart of DISC-0164 (Theorem BP, monotone in the level n).

## Derivation

Repository proof (GASKET.md Theorem BR). Re-derived this slice: BR.1 follows from β>0 and the sympy gap; BR.2 from writing η_(N+1)(w)=α_1+β η_N(pw) and using 1−β>0 with BR.1; BR.3 by subtracting the two deficit integrands at the same level; BR.4 from monotone convergence (both factors increase, dominated by g_hi t^(γ−1−α)·2/(2+t), integrable exactly when 0<γ−α<1).

## Assumptions

Used as stated by the repository, not re-run there or here: AQ (3), BD.4, BG.1, BG.3, BJ.4, BH.2, BJ.2, BJ.3 (g_lo=0.600945014, g_hi=0.600963487), BJ.6's ψ(y)≤ye^(y/10), BI.4 (G=0.6031), BQ.2–BQ.3 (C_N=P_N/D_∞, D_∞ routine, certified C_1), AT.1 (derived identification only). α<γ for BR.4–BR.5. Certificates pointwise in α.

## New Results

δ_N^(n) strictly decreasing in N at every level for every α∈(0,1); ρ^N C_N strictly increasing to a finite positive c_∞(α) below γ; certified c_∞ at four exponents; closed ceiling for M_α.

## Prior Art

Induction on a rational recursion, change of variables and monotone/dominated convergence are routine. No literature search on these specific gasket constants; not searched further.

## Novelty Analysis

Method KNOWN. Novelty of c_∞(α) and of the depth monotonicity on this specific operator UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Repository witness /workspace/ifi-br/scripts/gasket_fractional_deficit_depth.py: EXIT 0, 105.4 s script time (1m46 wall), all checks "ok" (/workspace/scratch-ifi/repo_theorem_BR.log). Full-precision endpoints of the same arb computation re-printed with 10 digits (/workspace/scratch-ifi/repo_theorem_BR_fullprec.log).
(2) Archive /workspace/scratch-ifi/indep_theorem_BR.py, 35/35 PASS (/workspace/scratch-ifi/indep_theorem_BR.log): sympy α_1+β=2/(2+z), the BR.1 gap and nonnegative coefficients, BR.2 identity, 1−β form, remainder identity, the Beta-integral ceiling at c=1/3; exact rationals η_N≤2/(2+z) (N=0–7), BR.2 (N=0–6), η_(N+1)>η_N (N=0–6) on z∈{0,1/1000,1/10,1,7/2,30,10^6}, η_N(0)=1−(3/2)(3/5)^N; c_∞ brackets rebuilt as [g_lo M_lo/D_hi, g_hi M_hi/D_lo] from printed cells agree to 1e−6 at all four α; the closed ceilings 5.846206, 4.867696, 4.390927, 5.530505 reproduced and exceed M_hi; ρC_1 (BQ brackets) lies below c_∞,lo at all four α (consistency with DISC-0165); an independent mpmath quadrature of M_α (η by recursion, ψ by p^40(5^−40 t)) gives M(0.01)=1.7338399, M(0.45)=3.4663311, inside the certified brackets; floats δ_N^(6)(0.45) decreasing in N=1–5; the commit's scratch values ρ^N V_N^(N+14)(0.45)=0.049579…0.453730 increase and stay below c_∞,lo. A first draft of the archive check used a too-tight threshold for η_8(0) (0.9748, not >0.98); that was an error in the archive check, corrected, not a repository fault.
(3) Logic attack: BR.4's strict increase needs η_N>0 (η_N≥1/(2(z+5)) for N≥1) and Q_N nondecreasing; the bound needs η(ψ(t))≤2/(2+t), which uses BR.1 in the limit, η decreasing and ψ(t)≥t. All supplied. No mathematical failure found. Arb cells were not independently re-certified.

Erratum (printed constants, no effect on any claim): the 6-digit endpoints are printed with round-to-nearest (Python :.6f), not outward. Against the full-precision arb endpoints: c_∞(0.01) upper printed 0.010444 < 0.0104444429; c_∞(0.1) lower printed 0.105440 > 0.1054396381; c_∞(0.3) upper printed 0.327592 < 0.3275921486; c_∞(0.45) lower printed 0.520387 > 0.5203869327 and upper printed 0.520824 < 0.5208243029; every-N lower ends ρC_1 at 0.01 and 0.3 printed 0.002653, 0.050414 vs 0.0026527527, 0.0504137648; M(0.3), M(0.45) lower ends printed 2.1990754, 3.4657841 vs 2.1990753593, 3.4657840920. All discrepancies ≤4.5e−7. Outward 6-digit brackets: c_∞(0.01)∈[0.010439,0.010445], c_∞(0.1)∈[0.105439,0.105526], c_∞(0.3)∈[0.327320,0.327593], c_∞(0.45)∈[0.520386,0.520825]. Same pattern as the earlier BM/BN round-to-nearest errata.

## Experimental Validation

Computational only. Repository witness log and archive log as above.

## Mathematical Status

Theorem (mathematical sense; BR.5 constants computer-assisted; BR.4's Θ_AT identification derived from AT.1 only).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0165 → DISC-0167 (mathematical: answers BQ's open N-dependence of C_N; BQ.3's ρC_1 is the every-N lower end). DISC-0164 → DISC-0167 (mathematical, related: BP monotone in level n; BR monotone in depth N). DISC-0149 → DISC-0167 (mathematical: BH.2's η recursion and remainder identity). DISC-0153 → DISC-0167 (mathematical: BJ.2–BJ.3 power bracket bounds ρ^N C_N). DISC-0166 unchanged (BR does not address eventual monotonicity of V^(n)). DISC-0159's limit clause (above γ) stays CONJECTURE.

## Open Questions

Closed forms for c_∞, C_N, P_N; the rate of ρ^N C_N→c_∞ (floats suggest slow: 0.454 at N=6 against 0.520); certified C_N for individual N≥2; brackets uniform in α; matching c_∞ with BH's layer (derived only); eventual monotonicity of V^(n) (DISC-0166); a* closed form; Conjecture BL.6's limit part (DISC-0159).

## Next Experiments

Certify ρ^2 C_2(0.45); float ρ^N V_N^(N+14) for N up to 12 to estimate the convergence rate to c_∞; test whether c_∞(α) is monotone in α (0.0104, 0.1054, 0.3273, 0.5204 at α=0.01, 0.1, 0.3, 0.45 suggest increasing).

## Reproduction Instructions

git -C informational-flux-identity checkout bed41594e18cbcb7af443349e9e3c6ea11426c26; python3 scripts/gasket_fractional_deficit_depth.py (≈105 s; sympy, mpmath, python-flint). Archive: python3 /workspace/scratch-ifi/indep_theorem_BR.py (≈2 s).

## Evidence Log

- 2026-10-23 ~1:59pm EDT. Indexed; repo witness EXIT 0 (105.4 s); independent checks 35/35 PASS; rounding erratum recorded.

## Change History

- 2026-10-23. Initial archive entry.
