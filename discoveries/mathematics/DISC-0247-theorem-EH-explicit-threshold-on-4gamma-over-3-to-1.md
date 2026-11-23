# Discovery: Theorem EH, the explicit threshold on all of [4 gamma/3, 1): Y_n < Y_oo for every alpha there, every N >= 1 and every n >= N; below 4 gamma/3 the sign changes in n

## Discovery ID
DISC-0247

## Status
THEOREM (mathematical sense only; EH.1-EH.2 are proved in the repository from EF.1, EG.1 and their cell routines as stated; EH.3-EH.4 are arb-certified (128 bits); EH.5 is floats, OBSERVED). Method KNOWN (monotone-in-parameter interval enclosures on cells; EG.2 on a cell). Novelty of the constants UNRESOLVED. Answers DISC-0246's open item "explicit n_0 on all of [4 gamma/3, 1)" and DISC-0245's "nu_alpha at five points only" (dated notes). No status change elsewhere.

## Date Discovered
2026-11-15 (indexed ~10:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 4e198bae1a55dafe42996fd67a9ffb85f2244dbb (2026-11-15 9:17 AM EST); parent b819534ca2ef (Theorem EG, DISC-0246).

## Original Evidence
- GASKET.md §Theorem EH (+~68/-4 lines overall incl. annotations of EG/EF kept limits); CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_uniform_threshold.py (new, 445 lines); registered in scripts/cli.py; tests/test_cli.py (+19); tests/test_flux_identity.py (+29, numpy-only CI test).

## Discovery
Setting as AZ, DZ, EA-EG: gamma = log3/log5, rho = 5^alpha/3, alpha = 4 gamma/3 gives rho^3 = 3.
- EH.1 (THEOREM): on each alpha-cell in (gamma,1] every alpha-dependence is a weight x^-alpha or x^(1-alpha), monotone in alpha on each x-cell (exact node x = 1), or F nondecreasing in alpha (d omega^0/dalpha = log(1+q/5) omega^0), so D'_oo >= D_lo, Mt_oo <= M_hi, L(k0) >= L_lo, kappa_lo >= k_lo, h <= h_hi uniformly on the cell.
- EH.2 (THEOREM): EG.2 on a cell with f = min(1, 3/rho(a1)^3); n >= 2 by k0 <= 2, n = 1 by L(1) or the eta term.
- EH.3 (arb, --full): 36 closed cells cover [4 gamma/3, 1] (first endpoint the ball 4log3/(3log5)); all pass, so Y_n < Y_oo for EVERY alpha in [4 gamma/3, 1), N >= 1, n >= N. Smallest margin L(2) - f^2 |nu|^3 D'_oo >= 0.09058; n = 1 via eta up to alpha = 0.9225 (bound <= -0.002291, 5 cells), else L(1) (31 cells, margin >= 0.02004); |nu| in [0.38461, 0.40022] on [4 gamma/3, 0.9125], <= 0.01359 on [0.9975, 1).
- EH.4 (arb, below 4 gamma/3): Y_n < Y_oo for n in [max(N,3), 8] at 0.9, [max(N,2), 21] at 0.905, [max(N,2), 926] at 0.91; none certified at 0.88, 0.89. With EC.3/ED.3 (Y_n > Y_oo for all large n) Y_n - Y_oo changes sign in n there (EF.2's S_N exists only at rho^3 = 3).
- EH.5 (OBSERVED): |nu|^3 D'_oo meets e* near alpha = 0.875.

## Why It Matters
EG's explicit n_0 = N now holds on the whole supercritical interval, and the sharpness of 4 gamma/3 is visible numerically: just below it the inequality holds only on finite n-windows.

## Derivation
Checked here: d/dalpha log omega^0 = log(1+q/5) >= 0 for q >= 0, so omega^0 is nondecreasing in alpha; rho = 5^alpha/3 is increasing and rho^3 = 5^(3a)/27 = 81/27 = 3 at a = 4 log3/(3 log5) (mpmath 30 digits PASS). Cell-wise sufficiency and the arb enclosures are the repository's; the pointwise core is inherited from EG.1 and not re-proved here.

## Assumptions
EF.1, EG.1-EG.2 and cell routines as stated; EC.3/ED.3 for the large-n side of EH.4; python-flint arb correctness.

## New Results
Cell-certified Y_n < Y_oo on [4 gamma/3, 1) with explicit n_0 = N; certified n-windows at 0.9, 0.905, 0.91; |nu| brackets as functions of alpha on 36 cells.

## Prior Art
As DISC-0244..0246 (Poincare functions for gasket decimation; arb, Johansson; Tucker 2011). No external search in this slice.

## Novelty Analysis
Method KNOWN; constants new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Repo default witness EXIT 0 (10 s, "all EH checks passed"). --full EXIT 0 (104 s wall, "all EH checks passed"); reproduced: 36-cell cover, smallest margin 0.09058, eta-route bound -0.002291 up to 0.9225, L(1) margin 0.02004, |nu| brackets 0.38461/0.40022/0.01359, EH.4 windows at 0.88, 0.89 (none), 0.9 (3..8), 0.905 (2..21), 0.91 (2..926). Local pytest subset (uniform/threshold) 2 passed.
- Display note, not a defect: the default (coarser) run certifies narrower windows than the commit message (0.905: 3..13; 0.91: 2..662); the message quotes --full values, which the repo states.
- Fixed-alpha attempts at 0.9125, 0.93, 0.9625, 0.9975 obey the cell bounds; floats on a 9-point grid have positive margins and n = 1 bound < 0.
- No contradiction with DISC-0243..0246: EG's 4 gamma/3 and 0.95 brackets sit inside the cell brackets (checked by the witness); EF's S_N < 0 unchanged.
- Scope: one-sided only, no onset level below 4 gamma/3, EH.4 at five points, nothing below ~0.89. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Not thrust; Stage 2 still blocked.

## Mathematical Status
Theorem as stated (EH.1-EH.2 proved, conditional on listed inputs); EH.3-EH.4 computer-assisted; EH.5 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0246 (EG), DISC-0245 (EF), DISC-0244 (EE), DISC-0243 (ED), DISC-0241 (EB).

## Open Questions
Upper rate; onset level and exact sign-change position below 4 gamma/3; alpha <= gamma; alpha below ~0.89.

## Next Experiments
Finer cells below 4 gamma/3 to locate where the n-window closes; certify EH.5's crossing near 0.875.

## Reproduction Instructions
Clone informational-flux-identity at 4e198bae1a55dafe42996fd67a9ffb85f2244dbb; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_uniform_threshold.py` (~10 s) and `--full` (~100 s).

## Evidence Log
- 2026-11-15 ~10:10 AM EST: default EXIT 0 (10 s); --full EXIT 0 (104 s); pytest subset 2 passed; rho^3 = 3 and monotonicity checks PASS.

## Change History
- 2026-11-15: created.
- 2026-11-15 (dated note): Theorem EI (IFI 74dea9103351, DISC-0248) answers this entry's open item 'onset level below 4 gamma/3' with an explicit upper bound on it: a criterion Phi_N(k) strictly increasing in k (g = 3/rho^3 > 1) gives Y_n > Y_oo for every n >= n1, arb n1 (N = 1) = 159 at 0.9, 316 at 0.905, 11584 at 0.91; with EH.4's windows the last level with Y_n < Y_oo lies in [8, 158], [21, 315], [926, 11583]. Every n1 exceeds the EH.4 window ends 8 / 21 / 926 (no contradiction). The exact sign-change position and the number of sign changes stay open. No status change.
- 2026-11-15 (dated note): Theorem EJ (IFI 344496c145e9, DISC-0249) fixes the exact sign-change position this entry left open, at 0.9 (N = 1: 32 -> 33; N = 2: 40 -> 41; N = 3: 50 -> 51) and 0.905 (N = 1: 67 -> 68), with exactly one sign change there (from the repo's --full certificate). It also certifies new initial windows [2,8] at 0.88 and [2,14] at 0.89. Every EJ window contains this entry's EH.4 windows. No status change.
