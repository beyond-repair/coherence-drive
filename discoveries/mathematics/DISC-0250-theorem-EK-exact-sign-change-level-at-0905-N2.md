# Discovery: Theorem EK, the exact sign-change level of Y_n - Y_oo at alpha = 0.905 for N = 2 (83 -> 84) and a narrowed bracket [102,103] for N = 3

## Discovery ID
DISC-0250

## Status
THEOREM (mathematical sense only; EK.1 is EJ.1-EJ.2 (DISC-0249) applied unchanged on finer arb grids, 128 bits, per the repository's --full certificate; EK.2 is floats, OBSERVED). Method KNOWN (monotone comparison bounds plus interval arithmetic, as DISC-0249). Novelty of the constants UNRESOLVED. Answers DISC-0249's open item "exact levels for N >= 2 at 0.905" for N = 2; N = 3 only narrowed. No status change elsewhere.

## Date Discovered
2026-11-15 (indexed ~3:10 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit d2a34ff395c5 (2026-11-15 2:23 PM EST); parent 344496c145e9 (Theorem EJ, DISC-0249).

## Original Evidence
- GASKET.md §Theorem EK (+38 lines incl. in-place marks on EJ.3's 0.905 bracket sentence and EJ's kept limit); CLAIM_STATUS.md (EJ open item marked, +1/-1); README.md (EJ paragraph, +2/-1).
- scripts/gasket_fractional_corner_exact_0905.py (new, 134 lines; imports EJ's module unchanged: certify_point, certify_upper, certify_lower, onset_upper, below_upper), registered in scripts/cli.py (+1); tests/test_cli.py (+14); tests/test_flux_identity.py (+20).

## Discovery
Setting and notation as DISC-0249 (gamma = log3/log5, rho = 5^alpha/3, Y_n the second correction, N the starting level).
- EK.1 (THEOREM, certified at the point alpha = 0.905): grids EF.1 cells 2000/8000, EJ.1 upper k0 = 14 on 8000/unit, EG lower k0 <= 12 on 2000/unit and k0 in {12,14} on 4000/unit. D'_oo in [5.86416, 5.86461], |nu| in [0.41474, 0.415168]; U(14) <= 0.740363, L(12) >= 0.73421 (2000/unit grid) and >= 0.736432 (4000/unit grid) >= 0.736432 on the 4000/unit grid, see Falsification Attempts), L(14) >= 0.736435; kappa_lo(2,14) >= 0.618019, kappa_lo(3,14) >= 1.70926, kappa_hi(2,14) <= 0.623710, kappa_hi(3,14) <= 1.734107.
  - N = 1: Y_n < Y_oo for n = 1..67, Y_n > Y_oo for every n >= 68 (reproduces EJ.3).
  - N = 2: Y_n < Y_oo for n = 2..83 and Y_n > Y_oo for every n >= 84: exactly one sign change, between 83 and 84 (EJ.3 had [82,83]).
  - N = 3: Y_n < Y_oo for n = 3..102, Y_n > Y_oo for every n >= 104; last negative level in [102,103] (EJ.3: [101,103]).
- EK.2 (OBSERVED): at N = 3, n = 103 the smallest EJ.2 lower-side bound is +0.005534 (k0 = 14), so 103 is undecided by this method; float crossings 68, 84, 104 equal the certified onsets.

## Why It Matters
Extends the "exactly one sign change" picture of DISC-0249 from (0.9, N = 1..3) and (0.905, N = 1) to (0.905, N = 2). The closure at level 83 is tight: certified margin 3.25e-4, versus 5.3e-3 at level 82.

## Derivation
No new analytic step: EK.1 is EJ.1-EJ.2 (DISC-0249) evaluated on finer grids. The derivation status is inherited from DISC-0249 (telescoping identity independently checked there in exact rational arithmetic).

## Assumptions
Everything DISC-0249 lists (AQ (1)-(3), r_k(s) <= 1/s, BI.4, BK.1-2, BL, DZ.1-2, ED.1-2, EE.1, EG.1, EB.1/EI.1, EJ.1-EJ.2), EF.1 cell routines valid at 0.905, python-flint arb and sympy correctness.

## New Results
Exact sign-change level 83 -> 84 at (0.905, N = 2); N = 3 bracket narrowed from width 3 to width 2; all EK enclosures nested inside EJ.3's.

## Prior Art
As DISC-0244..0249 (Poincare-function asymptotics for gasket decimation; arb, Johansson; computer-assisted proofs, e.g. Tucker 2011). Grid refinement of interval certificates is standard. No external search in this slice.

## Novelty Analysis
Method KNOWN; the level 83 -> 84 is new to the corpus; external novelty UNRESOLVED, modest (a single point refinement of DISC-0249).

## Falsification Attempts
- Repo default witness (lower-side certificates only) EXIT 0 here: 113.5 s inside the script (1m53.7s wall, niced, repo says 184.5 s), "all EK checks passed". Printed: D'_oo [5.86416, 5.86461], |nu| [0.41474, 0.415168], nested inside EJ.3's (5.86394, 5.86483), (0.414526, 0.415382); lower grid n = 4000, hi = 14: L(12) >= 0.736432, L(14) >= 0.736435, kappa_lo(1,14) >= 0.075460, kappa_lo(2,14) >= 0.618019, kappa_lo(3,14) >= 1.709263; N = 2, n = 82 braces <= -0.005306; N = 2, n = 83 braces <= -0.0003251 (k0 = 12); N = 3, n = 102 braces <= -0.007008; N = 3, n = 103 smallest bound +0.005534 > 0 (kept limit confirmed).
- Apparent mismatch checked: the commit message's "L(12) >= 0.73421" is the 2000/unit-grid value; GASKET.md line 6413 states both (0.73421 on 2000/unit, 0.736432 on 4000/unit) and the --full run prints both. No defect.
- tests/test_flux_identity.py -k 0905: 1 passed.
- Consistency with DISC-0249: 83 lies in EJ.3's [82,83]; [102,103] lies in [101,103]; onset 68 at N = 1 reproduced; [L(12), U(14)] inside EJ.3's [0.729805, 0.741544] at 0.905. No contradiction found.
- Scope: one alpha point, N <= 3, closure grid-limited (level 83 is not certified on EJ's --full grid or on the 2000/unit lower grid); no proved rate for U - L -> 0. KEPT FAILURE: none.
- --full run here (394.4 s inside the script, 6m34.6s wall, niced, EXIT 0, "all EK checks passed"; repo says 469.6 s): upper k0 = 14, n = 8000: c_hi <= 0.258245, U(14) <= 0.740363, kappa_hi(1,2,3) <= 0.075935, 0.623710, 1.734107; lower 2000/unit L(12) >= 0.734210; N = 1 'negative for n = 1..67, positive for every n >= 68'; N = 2 'negative for n = 2..83, positive for every n >= 84' (k0 <= 12 grid reaches 82, k0 in {12,14} adds 83); N = 3 'negative for n = 3..102, positive for every n >= 104', last negative level in [102,103]. Every EK.1 number in the commit is reproduced.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Computer-assisted theorem at a point, conditional on DISC-0249's inputs; EK.2 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0249 (EJ), DISC-0248 (EI), DISC-0247 (EH), DISC-0246 (EG).

## Open Questions
Decide level 103 at (0.905, N = 3) (needs a finer lower grid or a sharper method); exact levels at 0.88, 0.89, 0.91; alpha-cells instead of points; N >= 4; a proved rate for U - L -> 0.

## Next Experiments
Rerun EK's lower side for N = 3, n = 103 on an 8000/unit grid; cell version of EJ.2 around 0.905.

## Reproduction Instructions
Clone informational-flux-identity at d2a34ff395c5; pip install python-flint sympy numpy; python3 scripts/gasket_fractional_corner_exact_0905.py (~2-3 min) and --full (~8 min); pytest -q tests/test_flux_identity.py.

## Evidence Log
- 2026-11-15 ~3:05 PM EST: default EXIT 0 (113.5 s), pytest 0905 test passed.
- 2026-11-15 ~3:15 PM EST: --full EXIT 0 (394.4 s, informational-flux-identity @ d2a34ff395c5, python3 + python-flint); 83 -> 84 at (0.905, N = 2) and [102,103] at N = 3 reproduced.

## Change History
- 2026-11-15: created.
