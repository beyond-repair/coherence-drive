# Discovery: Theorem EG, an explicit threshold at alpha = 4 gamma/3: every-n lower bounds for EE's coefficients give Y_n < Y_oo for every N >= 1 and every n >= N

## Discovery ID
DISC-0246

## Status
THEOREM (mathematical sense only; EG.1 and EG.2 are proved in the repository from AQ, BK.1-2, BL, DZ.1-2, EB.1, ED.1, ED.2 (a) and EE.1's exact formulas as stated; EG.3-EG.4 are arb-certified (128 bits, monotone cell bounds) at the listed alpha values only; EG.5 is floats, OBSERVED). Method KNOWN (pointwise monotone comparison of the Poincare-function iterates, geometric-series summation, interval arithmetic). Novelty of the specific constants UNRESOLVED. Answers DISC-0245's open item "a rate ... (explicit n_0)" on the lower side only, and sharpens DISC-0244's / DISC-0243's every-n lower bound L_alpha (dated notes on DISC-0245, DISC-0244, DISC-0243). No archive status change otherwise.

## Date Discovered
2026-11-15 (indexed ~9:10 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit b819534ca2ef04f2a1791423f7fe0f07ea2f24df (2026-11-15 8:25 AM EST); parent 9ab32c906761 (Theorem EF, DISC-0245).

## Original Evidence
- GASKET.md §Theorem EG (header line 6141; kept limits line 6211; what stays open line 6213; NOT THIS line 6215), +95/-7 lines overall; EF's kept limit and open item, EE's kept limit and open item, ED's kept limit annotated in place with the original wording kept.
- CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_explicit_threshold.py (new, 417 lines); registered in scripts/cli.py; tests/test_cli.py (+20); tests/test_flux_identity.py (+24, numpy-only CI test).

## Discovery
Setting as in Theorems AZ, DZ, EA-EF: gamma = log3/log5, rho = 5^alpha/3; alpha = 4 gamma/3 is where rho^3 = 3.
- EG.1 (THEOREM, every alpha in (gamma,1), k0 >= 1): Psi_k >= x^-a 5^k b (Rh_k - R_k)(R_k + Rh_k) (from omega^0 >= 1 and 1/((1-u)(1-v)) >= 1+u+v), Rh_k - R_k = R_k Rh_k A_k (phi_k+6)/(phi_k+5) with A_k >= A, phi_k <= Phi, and 1/R_k <= V_k0 for every k >= k0 (phi_j nondecreasing in j). Hence c_k = (3/rho)^k (Mt_(k+1) - Mt_k) >= c_lo(k0) for EVERY k >= k0, with c_lo(k0) -> d*, so (3/rho)^n eps_n >= L(k0) = 3 c_lo/(2(1 - rho/3)), 3^n eta_n >= 1.5 kappa_lo(N,k0), 3^n R_n >= varrho_lo for every n >= max(N,k0). One-sided explicit rate.
- EG.2 (THEOREM, exact on EB.1): at rho^3 = 3, rho^n (Y_n - Y_oo) <= (1-delta_N)(|nu|^3 - L/D'_oo)/(1 + nu rho^-n) - 1.5 kappa_lo/D'_oo; for rho^3 >= 3, L(k0) > |nu|^3 D'_oo gives Y_n < Y_oo for every N and every n >= max(N,k0).
- EG.3 (arb, --full) at 4 gamma/3: |nu|^3 D'_oo in [0.374448, 0.374929]; L(k0) >= 0.287670, 0.483482, 0.629570, 0.698114, 0.729177, 0.732098 (k0 = 1, 2, 3, 4, 6, 8). L(2) > |nu|^3 D'_oo covers n >= 2; L(1) does not, so N = n = 1 uses the eta term: kappa_lo(1,1) >= 0.017260 gives rho (Y_1 - Y_oo) <= -0.00277434. Result: Y_n < Y_oo for every N >= 1 and every n >= N (explicit n_0 = N). Quantitative: for n >= max(N,6), rho^n (Y_n - Y_oo) <= S_N^+ = -0.0228058, -0.168032, -0.412478, -1.62341, -2.26477 (N = 1, 2, 3, 6, 10).
- EG.4 (arb): L(k0) at 0.7, 0.8, 0.9, 0.95; at 0.8, (3/rho)^n eps_n >= 0.732431 for every n >= 8 (about 132x ED.2's L_0.8 = 0.005532, within 1.2% of e*); 3^n R_n >= 0.0284712, 0.234988, 0.681678, 6.60087, 14.5593 (N = 1, 2, 3, 6, 10; ED.4's lower column was 3.716e-5 ... 7.155e-4). At 0.95 (rho^3 > 3): |nu|^3 D'_oo <= 0.119525 < 0.305669 <= L(1), so Y_n < Y_oo for every n >= N.
- EG.5 (floats, OBSERVED): L(k0) at 4 gamma/3 -> 0.73976 (k0 = 10: 0.739763), gap shrinking about 3x per level; c_lo(k) below the direct quadrature of c_k at 0.8.

## Why It Matters
DISC-0245 decided the sign only "for all large n". EG makes it effective: at the critical exponent the inequality Y_n < Y_oo holds from the first admissible level n = N on, and the corner-deficit chain now has explicit every-n lower brackets that are within about 1% of the limits instead of two orders of magnitude below.

## Derivation
Checked here: EG.2 is EB.1's exact identity at rho^3 = 3 with (3/rho)^n eps_n and 3^n eta_n replaced by their every-n lower bounds; since 0 < 1 + nu rho^-n <= 1 (nu < 0) the substitution is monotone in the right direction. The geometric sum (3/rho)^n eps_n >= c_lo 3^n sum_(k>=n) 3^-k/(1 - rho') = (3/2) c_lo/(1 - rho') and the elementary inequality 1/((1-u)(1-v)) - 1 - u - v = [u^2(1-v) + v^2(1-u) + uv]/((1-u)(1-v)) >= 0 are checked symbolically by the witness. The pointwise core (1/V_k0 <= R_k for k >= k0) is checked by the witness at sample points (max ratio 1.0000), not proved here independently.

## Assumptions
AQ, BK.1-2, BL, DZ.1-2, EB.1, ED.1, ED.2 (a), EE.1's exact formulas, all as stated in the repository; EF.1's integral representations for nu and D'_oo; python-flint arb correctness.

## New Results
Explicit n_0 = N for Y_n < Y_oo at alpha = 4 gamma/3 and at 0.95; every-n lower bounds L(k0) for (3/rho)^n eps_n at 0.7, 0.8, 0.9, 0.95, 4 gamma/3; every-n lower bounds for 3^n R_n at 0.8 and 4 gamma/3; negative every-n upper bounds S_N^+ for rho^n (Y_n - Y_oo).

## Prior Art
Same as DISC-0244/0245: Poincare functions and scaled limits for gasket decimation (Kigami; Strichartz; Fukushima-Shima; Teplyaev; Derfel-Grabner-Vogl); interval enclosures (Tucker 2011; arb, Johansson). No external source for these constants was searched in this slice.

## Novelty Analysis
Method KNOWN. Constants new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Repo witness default run EXIT 0 (15.1 s, "all EG checks passed"); --full run repeated here EXIT 0 (193.8 s wall), 28 "ok" checks, every bracket in the commit message reproduced digit for digit (D'_oo, nu, |nu|^3 D'_oo, L(k0) at all five alpha, kappa_lo(1,1), the n = 1 bound, S_N^+, 3^n R_n at 0.8, the 0.95 comparison).
- Independent mpmath interval check from the quoted brackets: |nu|^3 D'_oo in [0.3744478, 0.3749285] (matches); L(2) = 0.483482 > 0.374929 (margin ~29%); L(1) = 0.287670 < 0.374448, so the separate n = 1 argument is needed, as the repo says.
- n = 1 bound recomputed from EF's quoted brackets (1 - delta_1 in [0.076561, 0.076758] derived from -nu^3(1-delta_1) / |nu|^3, rho = 3^(1/3)): rho (Y_1 - Y_oo) <= -0.0027725. The repo's -0.00277434 is slightly tighter, which fits its finer internal enclosure of 1 - delta_1; both are negative, so the conclusion holds with the coarser public brackets too.
- Consistency of every-n bounds with the certified limits: every L(k0) at 4 gamma/3 < EF's e* upper end 0.7399065; L(6) at 0.7 = 0.767548 < e*(0.7) lower end 0.78098; L(6) at 0.9 = 0.726991 < 0.73737; L(6) at 0.95 = 0.742948 < 0.75298; L(8) at 0.8 = 0.732431 < 0.7409667; S_N^+ >= EF's S_N for N = 1, 2, 3, 6, 10 (-0.0228 >= -0.0233, -0.168 >= -0.1747, -0.412 >= -0.4545, -1.62 >= -4.69, -2.26 >= -89.1); 3^n R_n lower bounds at 0.8 below EE.4's varrho_N. No contradiction.
- Ratio checks: 0.732431/0.7410025 = 0.9884 (the "within 1.2%" holds); 0.732431/0.005532 = 132.4 (the "132x" holds).
- EG.5 "~3x per level": certified L(k0) gaps to e* do NOT shrink 3x per level from k0 = 6 to 8 (0.0106 -> 0.0077), but the float L(k0) gaps to 0.73976 do (0.0351, 0.00329, 0.000297 at k0 = 4, 6, 8, ~10.6x per two levels). The repo attributes the certified shortfall to grid loss and labels the rate OBSERVED; no overclaim.
- Scope: one-sided only (no two-sided rate, no every-n upper bound beyond EC.2's B_alpha), no explicit n_0 below 4 gamma/3, explicit n_0 certified only at 4 gamma/3 and 0.95 (not all of [4 gamma/3, 1)), kappa_lo weak for large N (S_10^+ = -2.26 vs S_10 = -89). All stated as kept limits; KEPT FAILURE: none. No overclaim found.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EG.1-EG.2 proved, conditional on the listed inputs); EG.3-EG.4 computer-assisted; EG.5 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0245 (Theorem EF; its "no explicit n_0" limit answered), DISC-0244 (Theorem EE; L_alpha sharpened for finite n, lower side of the rate), DISC-0243 (Theorem ED; "thresholds not explicit" answered at 4 gamma/3 and 0.95), DISC-0241 (Theorem EB; EB.1 identity used), DISC-0238 (Theorem DZ).

## Open Questions
An every-n upper bound for c_k (two-sided rate); explicit n_0 on all of [4 gamma/3, 1) and below 4 gamma/3; a proof of the observed 3^-k0 approach of L(k0); alpha <= gamma.

## Next Experiments
Certify L(k0) > |nu|^3 D'_oo on a cover of [4 gamma/3, 1) (needs nu_alpha and D'_oo as certified functions of alpha); refine the cell grid at k0 >= 6 to see whether the certified gap follows the observed 3x rate.

## Reproduction Instructions
Clone informational-flux-identity at b819534ca2ef04f2a1791423f7fe0f07ea2f24df; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_explicit_threshold.py` (~15 s) and `--full` (~190 s) for the brackets quoted above; tests `python3 -m pytest -q tests -k eg`.

## Evidence Log
- 2026-11-15 ~9:00 AM EST: repo default witness EXIT 0 (15.1 s); --full witness EXIT 0 (193.8 s), all checks ok, commit-message brackets reproduced; pytest EG subset 4 passed (15.7 s).
- 2026-11-15 ~9:05 AM EST: independent mpmath interval arithmetic PASS (n = 1 bound -0.0027725 from public brackets); no display defect found.

## Change History
- 2026-11-15: created.
- 2026-11-15 (dated note): Theorem EH (IFI 4e198bae1a55, DISC-0247) answers this entry's open item 'explicit n_0 on all of [4 gamma/3, 1)': L(2) - f^2 |nu|^3 D'_oo >= 0.09058 on 36 certified cells, so Y_n < Y_oo for every alpha in [4 gamma/3, 1), N >= 1, n >= N (n = 1 by the eta route below alpha = 0.9225, else L(1)). Below 4 gamma/3 the finite-n sign changes (EH.4). No status change.
- 2026-11-15 (dated note): Theorem EI (IFI 74dea9103351, DISC-0248) answers this entry's kept limit 'no explicit n_0 below 4 gamma/3 under EC.4's 60' on the upper side, without a two-sided rate: EC.2's crude B_alpha and DZ.1's etabar suffice below 4 gamma/3, giving Y_n > Y_oo for every n >= n1, n1 = 13 at 0.8 (N = 1, 2, 3; 14 for N = 6, 18 for N = 10). A two-sided rate for c_k is still open. No status change.
