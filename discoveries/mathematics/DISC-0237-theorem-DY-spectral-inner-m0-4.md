# Discovery: Theorem DY, the two-sided spectral rate of osc log R_m from m >= 4 with lambda_4 split off and a 1/20000 inner circle

## Discovery ID
DISC-0237

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Sharpens DISC-0236 (Theorem DX): the start index m_0 drops from 5 to 4, the m >= 5 constants tighten from [0.104411, 0.119038] to [0.111129, 0.112319] (U_5/L_5 from 1.140 to 1.0107), and DX's kept limit "for k <= 9 DV.1's direct rows stay" now holds only for k <= 8. Still a rate of the orbit F_m, not a cone contraction rate (DISC-0233's theta_8^(1/8) <= 0.2380 and DP.3's cap unchanged).

## Date Discovered
2026-11-13 (indexed ~7:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 91838c872b39773470318596dc1b0c90b6d1c3e3 (2026-11-13 6:08 AM EST).

## Original Evidence
- GASKET.md §Theorem DY (line 5635; NOT THIS disclaimer at line 5675), +51 lines.
- CLAIM_STATUS.md (Theorem DY sentence appended to the DX row); README.md (+3/-1).
- scripts/gasket_fractional_profile_level_spectral_inner.py (new, 368 lines); registered in scripts/cli.py; tests/test_cli.py (+44 lines).

## Discovery
- DY.1 (certified): DX.1 re-run, plus CQ.2's circles G_4 = |z + 2.164466e-4| = 1/20000 and |z| = 1/20000 re-run at N = 80 (rigorous float resolvent bounds, K' <= 6.8945e13), CQ.3's Krawczyk eigenvector of M_140 at lambda_4 = -0.00021644655283736 +/- 1.53e-18. F_0 = A_1 + A_2 + A_3 + A_4 + Pi'_in F_0 with ||d_4||_H2 <= 3.139e-11, sup|A_4| <= 1.0873, beta_4 <= 378.30, rho' K' S <= 5.8287e7, beta' <= 2.383e10.
- DY.2 (proved, DX.2's mean-value argument with e^Y_m = |l_3/r|^m sup|psi| + |l_4/r|^m beta_4 + (rho'/r)^m beta', |l_4|/r = 0.000510811, rho'/r = 0.000117999): L_m > 0 first at m_0 = 4; 0.098782|q|^m <= osc log R_m <= 0.124667|q|^m for every m >= 4; 0.111129|q|^m <= osc log R_m <= 0.112319|q|^m for every m >= 5; m = 4 enclosure [8.75615, 11.05060]e-5; proved ratio intervals osc_5/osc_4 in [0.1538119, 0.1961927], osc_6/osc_5 in [0.1714241, 0.1736831].
- DY.3: inside DX's [L_m, U_m] for m = 5..40 (strictly for m = 5..21); meets DV.1's (m = 4..7) and DW.1's (m = 6..12) enclosures.
- DY.4 (exact rationals, DV/DW constants as stated): B_Y = min(B_X, U^Y_(k-4)|q|^(k-4)); at k = 9, U^Y_5|q|^5 = 1.71790e-5 < DV.1's 1.7204e-5 (B_X/B_Y = 1.0014584); strictly below B_X for k = 9..25 (checked k = 8..399); at k = 8 DV.1's row stays (1.09934).
- DY.5 (derived, kept limit): every CF.3-form bound >= 8.58991x CS.2's D_4|q|^k for k >= 9 (DX.5: 8.07059), >= 7.63546x for k >= 8.
- DY.6 (kept limit, certified): m_0 = 3 is not reachable with rho' = 1/20000 (inner term >= 15.24 > 0.111724 at m = 3).

## Why It Matters
Answers DX's open item ("a sharper inner remainder would push m_0 below 5") and nearly closes the gap between the upper and lower constants at m = 5 (1.07% apart). It also certifies where this route stops (DY.6) and tightens the floor on how close any CF.3-form bound can get to CS.2 (8.59x).

## Derivation
As in DISC-0236, with one more simple eigenvalue split off: F_m = r^m A_1 (1 + q^m phi + eps_m), now |eps_m| <= e^Y_m, whose inner part decays like (rho'/r)^m = 0.000118^m instead of (1e-3/r)^m (m+1). The mean-value bound on g(x) = log(1+qx) - log(1+x) then gives L_m > 0 one level earlier.

## Assumptions
CG.3's eigenvalue enclosures and count; CQ.2/CQ.3's lambda_4 (simple, alone in G_4) and circle |z| = 1/20000 (re-run); CO.2 Taylor data to f_140; CO.3/CO.4 projections; CN.1's S. For DY.4/DY.5 only: CF.3's inclusion, DO.4, DV/DW/DX constants and CS.2's D_4 = 14.59509785 as stated. Textbook: Riesz projections, H^2 point evaluation, mean value theorem. python-flint arb correctness.

## New Results
Two-sided rate for every m >= 4; m >= 5 constants within 1.07%; best CF.3-form level-sum bound now for every k >= 9; certified obstruction to m_0 = 3 with this circle; 8.59x floor to CS.2 from k = 9.

## Prior Art
Same as DISC-0236: Ruelle–Perron–Frobenius spectral decomposition and Riesz projections (Ruelle 1978; Baladi 2000), analytic-function-space transfer operators (Mayer; Jenkinson–Pollicott), Krawczyk/interval eigenvalue enclosures (Tucker 2011). Splitting off more eigenvalues to shrink a remainder is standard. No external first claimed or supported.

## Novelty Analysis
Method KNOWN. Constants new to the corpus; external novelty UNRESOLVED and of little consequence.

## Falsification Attempts
- Independent mpmath arithmetic from stated constants (|q| = 0.1725476021, D_4 = 14.59509785): 0.112319|q|^5 = 1.71790e-5 (< 1.7204e-5; ratio 1.001455 from the 6-digit rounded U, consistent with the stated 1.0014584); 0.098782|q|^4 = 8.75616e-5 and 0.124667|q|^4 = 1.105063e-4 (match the m = 4 enclosure); 0.111129|q|^-4/D_4 = 8.58983 and 0.098782|q|^-4/D_4 = 7.63546 (match DY.5 to displayed digits); 2(rho'/r)^3 beta'/|q|^3 = 15.2427, with eta_4 added 15.2445 (matches DY.6's 15.24); U_5/L_5 = 1.01071; DX's Omega interval [0.1117242878, 0.1117243292] lies inside [0.111129, 0.112319]. PASS.
- Attack on consistency with DX: the m >= 5 interval is nested in DX's and still contains DX's proved limit Omega. Holds.
- Attack on scope: orbit rate only; cone rate unchanged; repo says so. Preserved.
- Repo default witness: see Evidence Log.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated, conditional on the listed CG/CQ/CO/CN inputs; DY.4/DY.5 additionally conditional on the stated DV/DW/DX/DO/CS constants.

## Patent Relevance
None.

## Related Discoveries
DISC-0236 (DX; sharpened), DISC-0235 (DW; rows m = 6..12 cross-checked), DISC-0234 (DV; k = 9 row superseded, k = 8 kept), DISC-0233 (DU; cone rate unchanged), DISC-0205 (CS; 8.59x floor), DISC-0203 (CQ; lambda_4 and circle G_4 re-run as inputs), DISC-0204 (CR; lambda_5, the next split for m_0 = 3).

## Open Questions
m_0 = 3 needs a smaller inner circle or lambda_5 split off (DY.6); a non-CF.3-form bound to close the 8.59x gap to CS.2; a cone with certified rate near 0.1725.

## Next Experiments
Re-run with lambda_5 split off and |z| <= 1e-6; independent N for the projection.

## Reproduction Instructions
Clone informational-flux-identity at 91838c872b39; `pip install python-flint mpmath sympy numpy`; `python3 scripts/gasket_fractional_profile_level_spectral_inner.py` (~5 min); test `python3 -m pytest -q tests/test_cli.py -k theorem_dy`.

## Evidence Log
- 2026-11-13 ~7:00 AM EST: independent mpmath arithmetic PASS (see Falsification Attempts).
- 2026-11-13 ~7:04 AM EST: repo default witness `python3 scripts/gasket_fractional_profile_level_spectral_inner.py` EXIT 0, all Theorem DY checks passed, 299.7 s on a shared box (repo states 295 s). Printed values match GASKET: L_4 = 0.098782030, U_4 = 0.12466659, L_5 = 0.11112997, U_5 = 0.11231865; m = 4 enclosure [8.7561595e-5, 1.1050598e-4]; DY.4 ratios 1.0014584 (k = 9), 1.09934 (k = 8); DY.5 8.58991; DY.6 15.24 (lambda_4 term only 1.96e-5).

## Change History
- 2026-11-13: created.
