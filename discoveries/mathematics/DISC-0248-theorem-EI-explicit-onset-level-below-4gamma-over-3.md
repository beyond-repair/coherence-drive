# Discovery: Theorem EI, an explicit onset level below 4 gamma/3: a criterion Phi_N(k) increasing in k gives Y_n > Y_oo for every n >= n1, and brackets the last level with Y_n < Y_oo at 0.9, 0.905, 0.91

## Discovery ID
DISC-0248

## Status
THEOREM (mathematical sense only; EI.1 is proved in the repository from EB.1, DZ.1, DZ.2, EC.2, ED.1 as stated, with the identity checked by sympy; EI.2 is arb-certified (128 bits, B_alpha at 256 bits) at eight alpha points; EI.3 combines EI.2 with EH.4; EI.4 is floats, OBSERVED). Method KNOWN (monotone comparison criterion with interval arithmetic). Novelty of the constants UNRESOLVED. n1 is an upper bound on the onset level, not the onset. Answers DISC-0247's open item "onset level below 4 gamma/3", DISC-0246's kept limit "no explicit n_0 below 4 gamma/3 under EC.4's 60", and improves DISC-0242's EC.4 sign statement at 0.8 from k >= 60 to k >= 13 (dated notes). No status change elsewhere.

## Date Discovered
2026-11-15 (indexed ~11:00 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 74dea9103351afce7275aaeae60d22cf1ccdd14d (2026-11-15 10:10 AM EST); parent 4e198bae1a55 (Theorem EH, DISC-0247).

## Original Evidence
- GASKET.md §Theorem EI (+56/-4 lines overall incl. in-place annotations of EH's and EG's kept limits and open items, original wording kept); CLAIM_STATUS.md (+1/-1, new row); README.md (+2/-1).
- scripts/gasket_fractional_corner_onset_level.py (new, 258 lines); registered in scripts/cli.py (+1); tests/test_cli.py (+18); tests/test_flux_identity.py (+27, numpy-only CI test `CornerOnsetLevelFloatTests.test_theorem_ei_onset_level_floats`).

## Discovery
Setting as AZ, DZ, EA-EH: gamma = log3/log5, rho = 5^alpha/3, g = 3/rho^3 > 1 iff alpha < 4 gamma/3.
- EI.1 (THEOREM; every alpha in (gamma, 4 gamma/3), N >= 1, k >= N): Y_k - Y_oo = (rho^2/3)^k {(1-delta_N)(|nu|^3 g^k - (3/rho)^k eps_k/D'_k)/(1+nu rho^-k) - 3^k eta_k/D'_k}. With (3/rho)^k eps_k <= B_alpha (EC.2, k >= 6), D'_k >= D_k := D_lo - rho M_hi rho^-k/(rho-1) (ED.1: eps_k >= 0, C' = -rho Mt_oo/(rho-1)), 0 <= 3^k eta_k <= H_k = 1.5 a_N + b_N (3/(5 rho))^k/(1 - 1/(5 rho)) (DZ.1), 0 < 1 + nu rho^-k <= 1 (nu_hi < rho^6): Phi_N(k) = om_lo (nu_lo^3 g^k - B/D_k) - H_k/D_k > 0 implies Y_k > Y_oo; Phi_N is strictly increasing in k, so one n1 >= max(6, N) with Phi_N(n1) > 0 gives Y_n > Y_oo for EVERY n >= n1.
- EI.2 (arb, --full): n1 for N = 1, 2, 3, 6, 10: 0.7: 7,7,7,8,12; 0.8: 13,13,13,14,18; 0.85: 25,25,25,26,32; 0.88: 52,52,52,53,64; 0.89: 79,79,79,81,96; 0.9: 159,158,159,162,191; 0.905: 316,315,315,322,377; 0.91: 11584,11534,11548,11783,13729. B_0.9 <= 1.0284e3, |nu_0.9| in [0.431992, 0.432892] (--full), 1-delta_1(0.9) >= 0.07380.
- EI.3 (THEOREM, with EH.4): the last level with Y_n < Y_oo exists and lies in [8, 158] at 0.9, [21, 315] at 0.905, [926, 11583] at 0.91 (N = 1; every N <= window end printed).
- EI.4 (OBSERVED, floats): limit-substituted crossing (e*, 1.5 kappa_N) 33, 41, 51, 90, 148 at 0.9, after EH.4's window end and below n1; not used.

## Why It Matters
Below 4 gamma/3 the sign of Y_n - Y_oo changes in n (EH.4); EI gives the first explicit level after which it is positive for good, and so brackets the last negative level, without needing a two-sided rate. At 0.8 EC.4's explicit 60 drops to 13 (sign only).

## Derivation
Checked here independently (sympy, general symbolic k, not only k = 1..8): substituting EB.1's X_k = C_delta/(1+nu rho^-k) - [(1-delta_N) eps_k/(1+nu rho^-k) + rho^k eta_k]/D'_k, C_delta = -nu(1-delta_N), Y_k = rho^k (X_k - C_delta), Y_oo = nu^2 (1-delta_N) gives residual 0 against the EI.1 (rho^2/3)^k {...} form (plus 5 random numeric spot checks, |residual| <= 3e-13). Monotonicity: g > 1; rho > 1 so D_k is increasing and, once positive, stays positive, so B/D_k and 1/D_k decrease; H_k is a positive constant plus a positive multiple of (3/(5 rho))^k with 3/(5 rho) = 9/5^(1+alpha) < 3/5, so H_k/D_k decreases; om_lo, nu_lo, B, D_lo, M_hi are k-independent. Hence Phi_N is strictly increasing on k >= max(6, N) where D_k > 0: the stated ingredients suffice; no gap found. The sufficiency step also needs the bracket in (1+nu rho^-k)^-1 to be positive, which Phi_N > 0 forces (om_lo > 0). Checked that the repo's H_k equals 3^k times DZ's own `ebar` (same formula) and that GASKET ED.1 gives C' = -Mt_oo rho/(rho-1) and D'_k = D'_oo + rho^-k (C' + eps_k), as EI.1 uses. Float scan of Phi_N(k) with the repo's float ingredients (k from max(6,N) to 300..40000): strictly increasing, D_k > 0 throughout, first positive k equal to the certified n1 up to 0.905 and 4-5 below it at 0.91 (certified route only loses).

## Assumptions
EB.1, DZ.1, DZ.2, EC.2 (B_alpha, k >= 6), ED.1 (eps_k >= 0), EF's cell routines for D'_oo, Mt_oo, h_N, EH.4's certified windows, all as stated in the repository; python-flint arb and sympy correctness.

## New Results
Explicit every-n onset levels n1(alpha, N) at eight alpha points, five N; certified brackets for the last level with Y_n < Y_oo at 0.9, 0.905, 0.91; at 0.8 Y_n > Y_oo for every n >= 13 (N = 1, 2, 3), 14 (N = 6), 18 (N = 10).

## Prior Art
As DISC-0244..0247 (Poincare functions for gasket decimation; arb, Johansson; Tucker 2011). The monotone-criterion trick is a standard comparison argument. No external search in this slice.

## Novelty Analysis
Method KNOWN; constants new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Repo default witness EXIT 0 (21 s wall here, "all EI checks passed"; repo says ~36 s). --full EXIT 0 (106 s wall, "all EI checks passed"; repo says ~129 s); --full reproduces every EI.2 n1 and the EI.3 brackets [8,158], [21,315], [926,11583] exactly, and EI.4's 33, 41, 51, 90, 148.
- Display note, not a defect: the default (coarser) run gives n1 +1 at 0.9/0.905 (N=1: 160, 317) and +31 at 0.91 (N=1: 11615, ~0.27%), equal up to 0.89; the commit message quotes --full values and says so ("+1 at 0.9/0.905, +0.3% at 0.91").
- Minor wording note: "EI.4 ... inside every bracket" applies to N <= window end; at 0.9 N = 10 has no EH.4 bracket (10 > 8), and the witness only checks N <= w. Also n1 is not monotone in N (0.9: N=2 gives 158 < 159 for N=1), consistent with 1-delta_N and a_N, b_N both varying in N; not a defect.
- Minimality "Phi_N(n1-1) not > 0" is an arb-decision statement (n1 is the first level the route certifies), not a statement about the true Phi_N; correctness of "every n >= n1" does not depend on it.
- Consistency: n1 <= 60 at 0.8 (EC.4) holds (13..18); every n1 exceeds EH.4's window end 8 / 21 / 926 (0.9 / 0.905 / 0.91), so no contradiction with DISC-0247; B_0.8 <= 1.9375e3 and B_0.9 <= 1.0284e3 match EC.2; |nu_0.8| bracket contains AZ (3)'s 0.7274454 and |nu_0.9| contains EF.4's [0.432350, 0.432534].
- CI subset: tests/test_flux_identity.py 11 passed (EI/onset subset 4 passed, 0.21 s).
- Scope: upper side only through EC.2's crude B_alpha (~1.4e3 e*) and DZ.1's etabar; eight points, no alpha-cells; EC.4's monotonicity (Y_k decreasing) not redone. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Theorem as stated (EI.1 proved, conditional on listed inputs; identity re-verified here symbolically); EI.2-EI.3 computer-assisted; EI.4 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0247 (EH), DISC-0246 (EG), DISC-0245 (EF), DISC-0244 (EE), DISC-0243 (ED), DISC-0242 (EC), DISC-0241 (EB).

## Open Questions
The exact onset level and number of sign changes below 4 gamma/3; sharper upper bound on (3/rho)^k eps_k than B_alpha (would shrink n1 toward EI.4's crossing); alpha-cells instead of points; initial windows below ~0.89.

## Next Experiments
Replace B_alpha by an every-n upper bound near e* (two-sided rate) and redo EI.2; cell version on (gamma, 4 gamma/3); redo EC.4's monotonicity statements with the new level.

## Reproduction Instructions
Clone informational-flux-identity at 74dea9103351afce7275aaeae60d22cf1ccdd14d; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_onset_level.py` (~20-36 s) and `--full` (~125 s); `pytest -q tests/test_flux_identity.py`.

## Evidence Log
- 2026-11-15 ~11:00 AM EST: default EXIT 0 (21 s); --full EXIT 0 (106 s); pytest test_flux_identity.py 11 passed; independent sympy identity (general k) residual 0; float monotonicity scan PASS.

## Change History
- 2026-11-15: created.
