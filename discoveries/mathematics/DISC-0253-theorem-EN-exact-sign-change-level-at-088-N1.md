# Discovery: Theorem EN, the exact sign-change level of Y_n - Y_oo at alpha = 0.88 (N = 1), 9 -> 10, via a two-sided denominator D'_n = D'_oo + rho^-n (C' + eps_n)

## Discovery ID
DISC-0253

## Status
THEOREM (mathematical sense only; EN.1 is a short exact identity plus inequalities stated and proved in the repository from ED.1 / AZ (1), EJ.1 and EM.1; EN.2 is an arb certificate, 128 bits, per the repository's witness). Method KNOWN (the same comparison bounds plus interval arithmetic as DISC-0249..0252; replacing a monotone-limit bound D'_n <= D'_oo by the exact first-order correction is a standard refinement). Novelty of the constants UNRESOLVED. Closes DISC-0252's kept limit and open item "the exact level at 0.88 (level 9)". EN.3, EN.4 OBSERVED. Level n = 1 at 0.88 remains undecided (kept limit). No status change elsewhere.

## Date Discovered
2026-11-16 (indexed ~7:40 AM EST; the commit is 2026-11-15 8:16 PM EST, missed by the failed hourly runs since ~7 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit ceb654d1204632c2ab5c61dd6ba7681a0affd5f0 (2026-11-15 8:16 PM EST; 2026-11-16 01:16Z); parent 4e72d34b6ed327f753b24f09d46a2156e5e34d34 (Theorem EM, DISC-0252).

## Original Evidence
- GASKET.md §Theorem EN (+52/-10; 8 files, +318/-15 overall), incl. in-place marks on EM's title, EM.4, EM's kept limits and open item, EJ.4's 0.88 table cells and "within two levels" sentence, EJ/EK/EL 0.88 bracket notes; CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_exact_088.py (new, 204 lines; imports EJ's gasket_fractional_corner_two_sided_rate, EL's gasket_fractional_corner_exact_0905_n3, EM's gasket_fractional_corner_exact_091), registered in scripts/cli.py (+2/-1); scripts/gasket_fractional_corner_exact_091.py (+3/-2, EN.4 docstring correction); tests/test_cli.py (+14); tests/test_flux_identity.py (+40, CornerExact088FloatTests).

## Discovery
Setting and notation as DISC-0249 (gamma = log3/log5, rho = 5^alpha/3, Y_n the second correction, N the starting level, D'_n, Mt_k, eps_n as in ED.1).
- EN.1 (THEOREM; every alpha in (gamma,1), k0 >= 1, n >= k0): ED.1 gives D'_(k+1) - D'_k = rho^-k Mt_k, hence the exact identity D'_n = D'_oo + rho^-n (C' + eps_n), C' = -rho Mt_oo/(rho - 1) (AZ (1)); with EJ.1 / EM.1's L(k0) <= (3/rho)^n eps_n <= U(k0): D'_oo + rho^-n C' + 3^-n L(k0) <= D'_n <= D'_oo + rho^-n C' + 3^-n U(k0). EJ.2 (b)'s lower-side criterion stays valid with D'_oo^hi replaced by D_n^hi = D'_oo^hi + rho^-n C'^hi + 3^-n U(k0), checked per level (no monotone-in-n claim). EJ.2 (a) unchanged.
- EN.2 (THEOREM, certified at the point alpha = 0.88, N = 1; EF.1 point cells 4000/32000, EL.1 upper and EM.1 lower at k0 = 9 on 1600 cells/unit): D'_oo in [5.4676986, 5.4679626], Mt_oo in [0.74287912, 0.74306202], |nu| in [0.49916739, 0.4993144], 1-delta_1 in [0.068040179, 0.06804675]; L(9) >= 0.73446007, U(9) <= 0.74222855, kappa_lo(1,9) >= 0.08095188, kappa_hi(1,9) <= 0.08322902; D'_9 in [5.31126720, 5.31157011]; EJ.2 (b) at n = 9 is +6.965e-4 with D'_9 <= D'_oo (undecided) but -2.344e-4 < 0 with EN.1, so Y_9 < Y_oo; with Y_n < Y_oo for n = 2..8 (EJ.4) and Phi(10) >= 3.518e-3 > 0 (Y_n > Y_oo for every n >= 10), Y_n - Y_oo changes sign exactly once for n >= 2, between 9 and 10 (EM.4: [8,9]).
- EN.3 (OBSERVED, floats): trapezoid D'_9 = 5.31141855 inside EN.1's bracket, 2.9 % below float D'_oo = 5.46783058; EE's float e* = 0.7349862, kappa_1 = 0.0810231 inside [L(9),U(9)], [kappa_lo, kappa_hi]; float crossing 10.
- EN.4 (OBSERVED; correction to EM's script docstring): EM's docstring quoted "L(14) = 0.735421, 0.737856, 0.738466" on 200/800/3200 cells/unit; the logged certified values are L(12) >= 0.735421, 0.737853, 0.738463 (the 800/3200 values were never logged and were 3e-6 high). EM's theorems did not use them (see DISC-0252 note).

## Why It Matters
Finishes the N = 1 exact-sign-change table at the four bracketed points: 0.88 (9 -> 10), 0.89 (14 -> 15), 0.905 (67 -> 68), 0.91 (2585 -> 2586), plus 0.9. It also locates where the lower side lost at small n: in its denominator (D'_n <= D'_oo is ~2.9 % loose at n = 9), not in its integrals.

## Derivation
EN.1: telescoping ED.1 and splitting Mt_k = Mt_oo - (Mt_oo - Mt_k) gives D'_oo - D'_n = -rho^-n C' - rho^-n eps_n exactly; EJ.1/EM.1's two-sided rate then brackets rho^-n eps_n in [3^-n L, 3^-n U] for n >= k0. In EJ.2 (b), E_n >= L > 0 and 0 < D'_n <= D_n^hi give -E_n/D'_n <= -L/D_n^hi and -3^n eta_n/D'_n <= -1.5 kappa_lo/D_n^hi; the sign split on X is EJ.2's. EN.2 is EN.1 at n = k0 = 9 evaluated in arb.

## Assumptions
Everything DISC-0249..0252 list (AQ (1)-(3), BI.4, BK.1-2, BL, DZ.1-2, ED.1-2, EE.1, EG.1, EB.1/EI.1, EJ.1-EJ.2, EJ.4, EL.1, EM.1), EF.1 cell routines valid at 0.88 (checked by the script), python-flint arb and sympy correctness; (3/rho) beta(p^9(1)) <= 1 (checked).

## New Results
Exact sign-change level 9 -> 10 at (0.88, N = 1, n >= 2); certified two-sided D'_9 in [5.31126720, 5.31157011]; EN.1 as a reusable every-level denominator correction.

## Prior Art
As DISC-0244..0252 (Poincare-function asymptotics for gasket decimation; arb, Johansson; computer-assisted proofs, e.g. Tucker 2011). First-order correction of a monotone limit by an exact remainder identity is standard. No external search in this slice.

## Novelty Analysis
Method KNOWN; the level 9 -> 10 and the D'_9 bracket are new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Repo witness here (informational-flux-identity @ ceb654d12046, python3 + python-flint 0.9.0, numpy 2.5.4, niced, heavily loaded shared box, run concurrently with EM's two witnesses): `python3 scripts/gasket_fractional_corner_exact_088.py` EXIT 0, 400.2 s in-script (401 s wall; repo says 452.0 s), "all EN checks passed". Every EN.2 number in the commit message is reproduced to the printed digits: D'_oo [5.4676986, 5.4679626], Mt_oo [0.74287912, 0.74306202], |nu| [0.49916739, 0.4993144], 1-delta_1 [0.068040179, 0.06804675], U(9) <= 0.74222855, kappa_hi <= 0.08322902, Phi(10) >= 0.003518, Phi(9) <= -0.001656, L(9) >= 0.73446007, kappa_lo >= 0.08095188, EJ.2 (b) n = 1 +0.005057 (undecided), n = 2..8 negative, n = 9 +0.0006965 (undecided), D'_9 [5.31126720, 5.31157011], EN.1 lower side at n = 9 -0.0002344; EN.4 L(12) >= 0.735421, 0.737853, 0.738463. There is no --full mode for EN.
- pytest (numpy CI): `pytest -q tests/test_flux_identity.py -k "em_exact or en_exact or el_exact"`: 3 passed (1.0 s).
- Independent quadrature (this slice, not in the repo): D'_9 = int x^-a R_9 recomputed by (i) the repo's trapezoid at 50/100/400/1000 points per unit and ranges [5^-120,5^120] .. [5^-200,5^200] (all 5.3114185537 +- 3e-10), and (ii) Simpson's rule using EJ's original R_k routine (ej.rk_float) on [5^-150, 5^6] spliced to the bounded recursion beyond 5^6: 5.311418553877, inside [5.31126720, 5.31157011]. Note: EJ's routine alone is numerically unusable above ~5^9 at k = 9 (returns negative values, e.g. -0.0058 at 5^10), which is why EN uses the bounded recursion w_j = u_j/s_j; the two agree to 1e-15 relative up to 5^8.
- EN.1 identity check in floats: D'_oo + rho^-9 C' + 3^-9 e* with EE's float limits (D'_oo 5.46783058, C' -2.72976462, e* 0.73498621) = 5.31141847, within 8.7e-8 of the direct quadrature and inside the certified bracket. D'_n increases monotonically to D'_oo in floats (D'_6, 8, 9, 10, 12, 20, 30 = 5.0631, 5.2530, 5.3114, 5.3540, 5.4075, 5.4631, 5.4676), consistent with ED.1.
- Float crossing at 0.88 from EE's float limits: 10 (recomputed here); agrees with the certified onset.
- Margins: 2.3e-4 at n = 9 (certified, not thin relative to the grid). Level 1 undecided (+5.057e-3); EN.1 at n = 1 would need U(1). One point alpha = 0.88, N = 1 only, not alpha-cells. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Computer-assisted theorem at a point, conditional on DISC-0249..0252's inputs; EN.1 a short exact derivation; EN.3-EN.4 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0252 (EM), DISC-0251 (EL), DISC-0249 (EJ), DISC-0247 (EH, ED.1-based denominators).

## Open Questions
Level 1 at 0.88; alpha-cells instead of points; N >= 2 at 0.88/0.89/0.91; a proved rate for U - L -> 0.

## Next Experiments
EN.1 with U(1) to decide level 1 at 0.88; apply EN.1 at other small-n levels (0.85 and below, where k0 = 6 is a floor of the method).

## Reproduction Instructions
Clone informational-flux-identity at ceb654d12046; pip install python-flint sympy numpy; python3 scripts/gasket_fractional_corner_exact_088.py (~7 min, 4 workers); pytest -q tests/test_flux_identity.py -k en_exact.

## Evidence Log
- 2026-11-16 ~6:56-7:03 AM EST: default witness EXIT 0 (400.2 s); pytest 3 passed; independent quadrature and EN.1 float identity checks above.

## Change History
- 2026-11-16: created.
