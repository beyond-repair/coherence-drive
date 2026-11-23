# Discovery: Theorem EX, the alpha-weighted refinement limit on the whole half-plane Re alpha < 1 and the real-axis shape of W

## Discovery ID
DISC-0263

## Status
THEOREM (mathematical sense only) for EX.1–EX.3; EX.4 is OBSERVED, not proved. Rests on BG.3/BD.4, the BI.4 floor, EU.1/EU.3, ES.1/ES.2, EV.1–EV.3, EW.1, Koenigs linearization and Arb correctness, all as stated in the repository and not re-derived here. Method KNOWN: dominated convergence plus Vitali for the limit; positivity, Hölder log-convexity and the small-tau slope of a Mellin transform for the shape; certified Arb quadrature for the values. Whether the constants or the statement are new is UNRESOLVED, because no literature search was done.

## Date Discovered
2026-11-22. The commit is from 11:35 PM EST and was indexed at about 11:55 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 165a8ed0eded03a3e8c49a43a23e8e81a4906fe1 (2026-11-23T04:35:50Z = 2026-11-22 11:35:50 PM EST). Parent: 084cb3bba7ca (Theorem EW, DISC-0262).

## Original Evidence
- GASKET.md §Theorem EX (36 lines changed), README.md, CLAIM_STATUS.md (CI now 26 tests).
- scripts/gasket_fractional_corner_h_alpha_limit.py (new, 209 lines), registered in scripts/cli.py; tests/test_cli.py (+13), tests/test_flux_identity.py (+18).

## Discovery
- EX.1: for -2^(n-1) < Re alpha < 1, rho^-n H_n(alpha) = int t^-alpha R_n(t)/(2(5+psi_(n-1)(t/5))) dt exactly (ES.1 degree gap). With p(y) >= y^2, 5y one gets psi_k(t) >= (t/5^J)^(2^J), and R_n <= 1/3 (EU.1/EU.3) gives an integrable dominator for every Re alpha < 1; dominated convergence and Vitali give rho^-n H_n(alpha) -> W(alpha)/2 locally uniformly, with all alpha-derivatives, and H_(n+1)(alpha)/H_n(alpha) -> 5^alpha/3 on real alpha < 1.
- EX.2: on real alpha < 1, W > 0, W'' > 0, log W convex, (1-alpha) W(alpha) -> 1/15 as alpha -> 1-, W -> oo as alpha -> -oo; hence a unique minimiser alpha*.
- EX.3 (certified Arb, widths <= 9e-20): W(-1) = 71.795668675310493193..., W(-1/2) = 8.8315491682555681078..., W(0) contains ln5, W(1/2) = 0.53800241803375371570..., W(9/10) = 0.84871798062514988..., W'(3/5) = -0.274972185892416957... < 0 < W'(7/10) = 0.214875716738099452...; so alpha* in (3/5, 7/10), W > ln5 for alpha < 0, W < ln5 on (0, 9/10], and W = ln5 again at exactly one alpha_1 in (9/10, 1).
- EX.4 (OBSERVED): 2 rho^-n H_n(alpha), n = 1..8, increase to W(alpha) at alpha = ±1/2 with gap ratios near 0.33; alpha* ~ 0.662 (float).

## Why It Matters
It closes DISC-0262's kept limit "no value, sign or closed form for real alpha": before EX the limit was known only on (0,1) (BG.3), at alpha = 0 (ET/EU) and at alpha = 2 pi i k/ln5 (EW). It now holds on the whole half-plane, and the real-axis graph of W is pinned down qualitatively and at certified points.

## Derivation
As in the repository (GASKET.md §Theorem EX). Hand-checked here: (1-alpha) W -> 1/15 follows from F(tau) = tau R/(5+psi(tau/5)) ~ tau/15 at tau -> 0 (int_0^1 tau^-alpha/15 dtau = 1/(15(1-alpha))); log-convexity of a Mellin transform of a positive function is Hölder's inequality (KNOWN); uniqueness of alpha* and alpha_1 follows from strict convexity once the sign of W' and the values at 0 and 9/10 are certified. The dominated-convergence step and the psi growth bound were read, not re-derived line by line.

## Assumptions
BG.3/BD.4, BI.4 floor, EU.1/EU.3, ES.1/ES.2, EV.1–EV.3, EW.1, Koenigs linearization, Arb correctness — as stated in the repository.

## New Results
Certified values of W at five real points and the bracket alpha* in (3/5, 7/10); existence and uniqueness of a second crossing W = ln5 in (9/10, 1).

## Prior Art
Mellin transforms of positive functions (log-convexity, Hölder), dominated convergence/Vitali, Arb validated integration: textbook. Spectral decimation on the Sierpinski gasket: KNOWN (Fukushima–Shima, Strichartz, Teplyaev). No external search for these constants.

## Novelty Analysis
Methods KNOWN. The constants W(-1), W(1/2), alpha*, alpha_1 are specific to this repository's functional; novelty UNRESOLVED.

## Falsification Attempts
Independent mpmath (30 digits) quadrature of W(alpha) = int F(tau) tau^(-alpha-1) dtau over blocks 5^-50..5^9 with an analytic small-tau tail tau/15 (script ex_check.py, reusing ew_check.py's 70-step Koenigs evaluator):
- F(5^-50)/5^-50 = 0.0666666666666666667 (slope 1/15 confirmed).
- W(-1) − EX value: 7.8e-19; W(-1/2): −8.0e-22; W(0) − ln5: −3.8e-30; W(1/2): 7.9e-21; W(9/10): 6.9e-18 — all within the truncation of the quoted digits.
- W'(3/5): −0.27497218589241695704 (diff −4.1e-20); W'(7/10): 0.21487571673809945213 (diff 1.3e-19). Signs agree.
- Root finding for alpha* and alpha_1 timed out and was not completed. Repository script and CI not rerun.
Nothing broke.

## Experimental Validation
Numerical only (certified Arb in the repository; independent mpmath here). No physical experiment; the repository says "functions on a graph, not a flux, not thrust".

## Mathematical Status
THEOREM (EX.1–EX.3, conditional on the listed repository results); OBSERVED (EX.4).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
- DISC-0262 → DISC-0263. Label: mathematical. EW.1's holomorphy and dominator extended to the convergence statement on Re alpha < 1; EW's real-alpha open item closed.
- DISC-0261 → DISC-0263. Label: computational. EX.3 uses EV.2's evaluator and EV.3's tail bound.
- DISC-0260 → DISC-0263. Label: mathematical. EU.1/EU.3 give R_n <= 1/3; W(0) = ln5 is the reference level for alpha_1.
- DISC-0258 → DISC-0263. Label: mathematical. ES.1 degree gap gives the exact integral for -2^(n-1) < Re alpha.

## Open Questions
Closed forms for W(alpha), W'(0), alpha*, alpha_1; rate for alpha != 0; zeros off the real and imaginary axes; small n with 2^(n-1) <= -Re alpha.

## Next Experiments
Certify alpha* and alpha_1 to many digits; fit and prove the ~1/3 gap ratio of EX.4; search for complex zeros of W.

## Reproduction Instructions
In informational-flux-identity @ 165a8ed0eded: `python scripts/gasket_fractional_corner_h_alpha_limit.py` (reported 354.1 s; python-flint). Independent check: ex_check.py (mpmath; local to the research box, not committed).

## Evidence Log
- 2026-11-22 ~11:55 PM EST: ex_check.py results above.

## Change History
- 2026-11-22 ~11:55 PM EST: created (THEOREM EX.1–EX.3, OBSERVED EX.4; method KNOWN, statement UNRESOLVED).
