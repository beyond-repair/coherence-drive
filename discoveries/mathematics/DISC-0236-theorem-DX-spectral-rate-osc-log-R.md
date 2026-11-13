# Discovery: Theorem DX, the exact per-level rate |lambda_2|/r = 0.1725476 of osc log R_m by a spectral (non-cone) route

## Discovery ID
DISC-0236

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Promotes DISC-0235's observation "consecutive row ratios ~0.1725, not a proved rate" to a proved two-sided rate for the orbit F_m = Lt^m F_0 (every m >= 5). This is a rate for the orbit, not a cone contraction rate: DISC-0233's theta_8^(1/8) <= 0.2380 and DP.3's cap 0.3171 are unchanged statements about cones.

## Date Discovered
2026-11-13 (indexed ~5:10 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3b72f8e0bc10af67848983e5a460e55c4c089d6a (2026-11-13 4:19 AM EST).

## Original Evidence
- GASKET.md §Theorem DX (line 5581; NOT THIS disclaimer at line 5624), +54 lines.
- CLAIM_STATUS.md (new row, Theorem DX); README.md (+3/-1).
- scripts/gasket_fractional_profile_level_spectral_osc.py (new, 410 lines; imports CN's, CO's, CG's, DC's and DV's scripts unchanged); registered in scripts/cli.py; tests/test_cli.py `test_theorem_dx_profile_level_spectral_osc` (+49 lines).

## Discovery
- DX.1 (certified): Riesz projections A_j = Pi_j F_0 (j = r, lambda_2, lambda_3) via CO.3's exact projection formula on M_80 with Krawczyk eigenvectors and CO.4's second-resolvent errors 2.532e-14, 2.387e-11, 2.025e-8 in H^2(D); CN.2's four circles re-run (K_in <= 1.0141e9). On 1024 cells of X: A_1 >= 0.0028742 > 0; phi = A_2/A_1 strictly decreasing; osc_X phi in [0.09528337, 0.09528341]; sup|phi| <= 0.06847674; sup|A_3/A_1| <= 0.40617.
- DX.2 (proved from DX.1 and CN.2): F_m = r^m A_1 (1 + q^m phi + eps_m), q = lambda_2/r < 0; mean value theorem gives L_m |q|^m <= osc log R_m <= U_m |q|^m with U_m nonincreasing, L_m nondecreasing, L_5 = 0.104411 > 0, U_5 = 0.119038, both tending to Omega = (1+|q|) osc phi in [0.1117242878, 0.1117243292]. Hence the exact rate of osc log R_m is |q| = 0.1725476021 (two-sided, every m >= 5). Proved consecutive-ratio intervals [0.1725333, 0.1725619] (m = 8), [0.1725475, 0.1725477] (m = 15).
- DX.3: DX.2's intervals meet DV.1's (m = 5..7) and DW.1's (m = 6..12) enclosures; two independent methods.
- DX.4 (exact rationals, DV/DW constants as stated): B_X(k) = min(B_W(k), U_(k-4)|q|^(k-4)) < B_W(k) for every k >= 10 (ratio 1.0036 at k = 10, 1.0003..1.0012 at k = 12..16, 21.37 at k = 17, 3.53e13 at k = 103); not at k = 9 (0.9449, DV.1's row stays).
- DX.5 (derived, kept limit): by DO.4 every CF.3-form bound exceeds CS.2's D_4|q|^k by a factor >= 8.0706 for k >= 9 (>= 8.6358 asymptotically): the rate is now spectral, the constant cannot reach CS's.

## Why It Matters
Closes DISC-0235's main open question (a proved rate near 0.1725) without any cone, by decomposing F_0 spectrally. It also explains why the cone route stalled at 0.2380: the cone rate bounds every positive function, while this orbit's rate is set by the second eigenvalue. DX.5 records honestly that CS.2's constant stays out of reach for this whole family of bounds.

## Derivation
F_0 = A_1 + A_2 + A_3 + Pi_in F_0 (CG.3 eigenvalue count; CN.2 inner circle |z| = 1e-3). Lt^m acts as lambda_j^m on Pi_j, and ||Lt^m Pi_in F_0|| <= 1e-3(m+1) K_in S. So F_m = r^m A_1 (1 + x_m + eps_m), x_m = q^m phi, |eps_m| <= e_m. Then log R_m - log r = g(x_m) + p_(m+1) - p_m with g(x) = log(1+qx) - log(1+x); g' = (q-1)/((1+qx)(1+x)) has constant sign for |x| <= a_m, so osc g(x_m) is pinned between inf|g'| and sup|g'| times |q|^m osc phi; the remainders |p_j| <= eta_j shift the oscillation by at most 2(eta_m + eta_(m+1)).

## Assumptions
CG.3's enclosures of r, lambda_2, lambda_3 and its count (exactly three eigenvalues in |z| >= 1e-3, all simple); CE.4's r; CO.3's projection formula and CO.4's resolvent bound (re-run); CN.1's S and CN.2's circles (re-run); CO.1/CO.2 Taylor data. For DX.4/DX.5 only: CF.3's inclusion r in [inf R_m, sup R_m], DO.4, DV/DU/DT/DO constants as stated, DW.1's stated uppers m = 8..12, CS.2's D_4 = 14.59509785, DV.3's 8-periodicity of G_U. Textbook: Riesz projections, H^2 point-evaluation bound, mean value theorem. python-flint arb correctness.

## New Results
Two-sided osc log R_m for every m >= 5 with limit constant Omega; proved rate 0.1725476 for the orbit; best level-sum bound of CF.3 form for every k >= 10; a proved floor (8.07x) on how close any CF.3-form bound can get to CS.2.

## Prior Art
Ruelle–Perron–Frobenius spectral decomposition of transfer operators; Riesz projections and spectral gap give exponential convergence at rate |lambda_2|/r (Ruelle 1978; Baladi 2000, Positive Transfer Operators and Decay of Correlations); Hilbert-space-of-analytic-functions transfer operators (Mayer; Jenkinson–Pollicott); rigorous eigenvalue enclosure (Krawczyk; Tucker 2011). The rate-equals-second-eigenvalue-ratio statement is textbook; only the certified constants are corpus-specific. No external first claimed or supported.

## Novelty Analysis
Method KNOWN (spectral decomposition plus perturbation of a simple leading eigenvalue). Constants (L_5, U_5, Omega, B_X) new to the corpus; external novelty UNRESOLVED and unlikely to matter.

## Falsification Attempts
- Repo default witness: see Evidence Log.
- Independent arithmetic (mpmath, from the stated constants): (1+|q|)·[0.09528337, 0.09528341] = [0.11172429, 0.11172433], matching Omega to the displayed digits; Omega|q|^12 = 7.78135e-11 (in DX's [7.781344, 7.781351]e-11 and DW.1's [7.78134, 7.79092]e-11); Omega|q|^16 = 6.89748e-14 (row m = 16); U_5|q|^5 = 1.82065e-5 > DV.1's 1.7204e-5 (so k = 9 is correctly not improved); DW upper / (U_8|q|^8) = 1.00029 and DW m = 9 upper / (U_9|q|^9) = 1.00034 (match DX.4's k = 12, 13); L_5|q|^-4/D_4 = 8.07056 and Omega^-|q|^-4/D_4 = 8.63585 (match DX.5); |lambda_3/lambda_2| = 0.2334 and 1e-3/|lambda_2| = 0.0137 (match attempts iii, iv). PASS.
- Attack on "rate": the bound is two-sided with L_5 > 0, so no faster rate is possible; finite U_5 excludes a slower one. Holds.
- Attack on scope: the statement concerns one orbit F_m from F_0 = Lt^4 G; it does not bound cone diameters. The repo says this itself; preserved here.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated, conditional on CG.3/CO.3/CO.4/CN.2 inputs; DX.4/DX.5 additionally conditional on the stated DV/DW/DO/CS constants.

## Patent Relevance
None.

## Related Discoveries
DISC-0235 (DW; observation promoted to a proved rate), DISC-0234 (DV; rows m = 5..7 cross-checked), DISC-0233 (DU; cone rate 0.2380 unchanged), DISC-0229 (DQ; spectral 0.1725), DISC-0227 (DO; DO.4 floor), DISC-0205 (CS; D_4 and DX.5's 8.07x gap), DISC-0201 (CO; projections re-run), DISC-0200 (CN; circles re-run), DISC-0191 (CG; eigenvalue count).

## Open Questions
Push m_0 below 5 with CQ/CR's lambda_4, lambda_5 and a 1e-8 inner circle; a cone with certified rate near 0.1725; bounds not of CF.3 form that could close the 8.07x gap to CS.2.

## Next Experiments
Independent re-run with a different DX_CELLS and a different N for the projection; reproduce Omega from an independent eigenvector computation.

## Reproduction Instructions
Clone informational-flux-identity at 3b72f8e0bc10; `pip install python-flint mpmath sympy numpy`; `python3 scripts/gasket_fractional_profile_level_spectral_osc.py` (~3 min); test `python3 -m pytest -q tests/test_cli.py -k theorem_dx`.

## Evidence Log
- 2026-11-13 ~5:10 AM EST: repo default witness `python3 scripts/gasket_fractional_profile_level_spectral_osc.py` EXIT 0, all Theorem DX checks passed, 208 s on a shared box (repo states 188 s). Printed values match GASKET to the stated digits: osc_X phi in [0.09528337068, 0.09528340598], L_5 = 0.104411451, U_5 = 0.119037166, DX.4 ratios 0.944936 (k = 9), 1.00361 (k = 10), 21.3662 (k = 17), DX.5 factor 8.07059. Nit: the run prints |phi - phi^N| <= 8.83e-9, GASKET rounds up to 8.9e-9; consistent.
- 2026-11-13 ~5:10 AM EST: independent mpmath arithmetic PASS (see Falsification Attempts).

## Change History
- 2026-11-13: created.

## Dated note (2026-11-13, ~7:05 AM EST)
DX's open item "push m_0 below 5" is answered by Theorem DY (informational-flux-identity 91838c872b39; DISC-0237): with lambda_4 split off and inner circle |z| = 1/20000, the two-sided bound holds from m >= 4, and for m >= 5 the constants tighten to [0.111129, 0.112319] (nested inside DX's [0.104411, 0.119038], still containing Omega). DX.4's "not at k = 9" is superseded: B_Y beats DV.1's k = 9 row; k = 8 stays. The original text above is preserved unchanged.
