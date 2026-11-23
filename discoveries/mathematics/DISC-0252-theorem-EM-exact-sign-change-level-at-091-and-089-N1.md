# Discovery: Theorem EM, the exact sign-change level of Y_n - Y_oo at alpha = 0.91 (2585 -> 2586) and alpha = 0.89 (14 -> 15) for N = 1, via a right-node lower cell bound

## Discovery ID
DISC-0252

## Status
THEOREM (mathematical sense only; EM.1 is a short monotonicity argument stated and proved in the repository from AQ (3), the mirror of DISC-0251's EL.1; EM.2-EM.3 are arb certificates, 128 bits, per the repository's witness; EM.2 needs the --full grids). Method KNOWN (monotone-endpoint cell bounds plus interval arithmetic, as DISC-0249..0251). Novelty of the constants UNRESOLVED. Closes DISC-0251's kept limit / open item "exact level at 0.91 (bracket [2564,2586])" and the 0.89 bracket. EM.4 OBSERVED (kept limit, later closed by DISC-0253). No status change elsewhere.

## Date Discovered
2026-11-16 (indexed ~7:40 AM EST; the commit is 2026-11-15 7:14 PM EST, missed by the failed hourly runs since ~7 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 4e72d34b6ed327f753b24f09d46a2156e5e34d34 (2026-11-15 7:14 PM EST; 2026-11-16 00:14Z); parent 7ba5c961c4a469f88bd22bc4fa6acdae4fef5cc8 (Theorem EL, DISC-0251). Reproduced at the child ceb654d12046 (Theorem EN), which changes only the EM script's docstring (EN.4).

## Original Evidence
- GASKET.md §Theorem EM (+47/-10, incl. in-place marks on EL.3's 0.91 bracket sentence, EL's kept limits and open item, EJ.4's 0.89/0.91 table cells and "within two levels" sentence, EJ's kept-limit bracket list, EK's kept limit and open item); CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_exact_091.py (new, 324 lines; parallel EF.1 cell routine certify_mt_par, EM.1 lower routine certify_lower_em), registered in scripts/cli.py (+1); tests/test_cli.py (+15); tests/test_flux_identity.py (+32, CornerExact091FloatTests).

## Discovery
Setting and notation as DISC-0249/0251.
- EM.1 (THEOREM; every alpha in (gamma,1), k0 >= 1, N >= 1; EG.1 and AQ (3) as stated): R_k and Rh_k are nonincreasing in x (as in EL.1), so on a cell [a,b] inf R_k >= 1/V_k0(b) and inf Rh_k >= (5/3)/V_(k0+1)(5b) with V at the single right node; EG.1's cell sums for c_lo(k0), kappa_lo(N,k0) stay lower bounds. This is the mirror of DISC-0251's EL.1 for the lower side (EG's vcell had taken its two large terms from opposite cell ends). OBSERVED: at 0.905, k0 = 12, 200 cells/unit, L(12) >= 0.735421 (EM.1) vs 0.696283 (EG's cell).
- EM.2 (THEOREM, certified at alpha = 0.91, N = 1; --full only: EF.1 point cells 16000/256000, EM.1 lower k0 in {14,20,26} and EL.1 upper k0 = 26 on 12800 cells/unit): D'_oo [6.00139547, 6.0014498], |nu| [0.39711787, 0.397133255], 1-delta_1 [0.0766194814, 0.0766208692]; L(14,20,26) >= 0.73971443, 0.73971486, 0.73971486, kappa_lo(1,26) >= 0.07464970, U(26) <= 0.73986384, kappa_hi(1,26) <= 0.07466495; EJ.2 (b) lower-side bounds -4.325e-05, -2.406e-05, -4.863e-06, +1.435e-05 at n = 2583..2586 so Y_n < Y_oo for n = 2565..2585 (with EJ.4 for n = 1..2585); Phi(2586) >= 4.779e-06 > 0, Phi(2585) <= -1.443e-05, so Y_n > Y_oo for every n >= 2586. Exactly one sign change, 2585 -> 2586 (DISC-0251/EL.3: [2564,2586]). The default grid (point 4000/32000, lower 3200/unit) reaches only n = 2584 (bound +1.169e-05 at 2585), i.e. last negative level in [2584,2586] by default.
- EM.3 (THEOREM, certified at alpha = 0.89, N = 1; default and --full; point 4000/32000, EL.1 upper k0 = 15, EM.1 lower on 1600/unit): |nu| [0.4663815, 0.4665156], U(15) <= 0.737190, kappa_hi(1) <= 0.079005, Phi(15) >= 0.0002257 > 0, so Y_n > Y_oo for every n >= 15 (EJ.4: >= 16), Y_n < Y_oo for n = 2..14: exactly one sign change 14 -> 15 (EJ.4: [14,15]).
- EM.4 (OBSERVED / KEPT LIMIT): alpha = 0.88, level 9 undecided by both sides (upper Phi(9) <= -0.001656, lower-side bound +0.0007145); bracket [8,9] unchanged (later closed by DISC-0253, Theorem EN).

## Why It Matters
Closes the widest remaining bracket in the series (0.91, width 23 after DISC-0251) to an exact level, and decides 0.89. Together with DISC-0251 it shows both sides' losses were cell-routine artefacts (end-mixing), fixable by monotonicity at one node.

## Derivation
EM.1: AQ (3) gives r_k(s) decreasing in s, so R_k(x) = (3/5)^k r_k(5^-k x) is nonincreasing in x and its cell infimum sits at the right node, where EG.1's pointwise lower bound applies; EG.1's cell sums use nonnegative weights (inherited, as in DISC-0251). EM.2-EM.3 are EJ.1-EJ.2 with EM.1/EL.1 evaluated in arb.

## Assumptions
Everything DISC-0249..0251 list (AQ (1)-(3), BI.4, BK.1-2, BL, DZ.1-2, ED.1-2, EE.1, EG.1, EB.1/EI.1, EJ.1-EJ.2, EJ.4, EL.1), EF.1 cell routines valid at 0.89 and 0.91 (checked), certify_mt_par equal to EF's certify_mt (checked at n_m = 200 to 1e-12), python-flint arb and sympy correctness; (3/rho) beta(p^k0(1)) <= 1 at k0 = 15 (0.89) and 26 (0.91).

## New Results
Exact sign-change levels 2585 -> 2586 at (0.91, N = 1) and 14 -> 15 at (0.89, N = 1); a right-node lower cell bound that dominates EG's.

## Prior Art
As DISC-0251 (monotone-endpoint interval bounds are standard; arb, Johansson; computer-assisted proofs, e.g. Tucker 2011). No external search in this slice.

## Novelty Analysis
Method KNOWN; the two levels are new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Consistency with DISC-0251: EM.2's onset 2586 and last negative level 2585 both lie in EL.3's [2564,2586]; EM.2's onset improves EL.3's 2587 by one; EM.2's |nu| bracket [0.39711787, 0.397133255] is nested in EL.3's [0.3970713, 0.3971799]; DISC-0251 recorded float braces -8.7e-6 at 2585 and +1.0e-5 at 2586 (float crossing 2586), matching. Float crossings from EE's float limits recomputed here: 2586 (0.91), 15 (0.89), 10 (0.88), all equal to the certified onsets.
- Two-sided and nesting checks on the runs here: default (3200/unit) L(26) >= 0.73956281 <= --full L(26) >= 0.73971486 <= U(26) <= 0.73986384, with EE's float e* = 0.7397656 inside; default point brackets D'_oo [6.00131397, 6.0015313], |nu| [0.397071274, 0.397179855] contain the --full ones. The 0.91 margins (4.9e-6 lower at 2585, 4.8e-6 onset at 2586) are thin but certified; EM.2 is grid-limited (the default grid does not decide 2585).
- EN.4 (DISC-0253) found that EM's script docstring had quoted unlogged L values (and the wrong index L(14) for L(12)) at 800/3200 cells/unit, 3e-6 high; the docstring was corrected at ceb654d12046. Those numbers are not used by EM.1-EM.3. The 200/unit value 0.735421 is reproduced here.
- Repo default witness here (informational-flux-identity @ ceb654d12046, python3 + python-flint 0.9.0, numpy 2.5.4, niced, heavily loaded shared box, concurrent with EN's witness and EM --full): `python3 scripts/gasket_fractional_corner_exact_091.py` EXIT 0, 844.9 s (repo says 389.3 s; slower because of load), "all EM checks passed". Printed EM.1 spot check ok; L(12) >= 0.735421 vs 0.696283; EM.3 |nu| [0.4663815, 0.4665156], U(15) <= 0.737190, kappa_hi(1) <= 0.079005, Phi(15) >= 0.0002257, Y_n < Y_oo for n = 2..14; EM.4 Phi(9) <= -0.001656, lower +0.0007145; 0.91 point D'_oo [6.00131397, 6.0015313], |nu| [0.397071274, 0.397179855], 1-delta_1 [0.0766174005, 0.0766229503]; L(14,20,26) >= 0.73956238, 0.73956281, 0.73956281, kappa_lo >= 0.07463436; lower-side bounds -2.671e-05, -7.515e-06, +1.169e-05, +3.092e-05 at 2583..2586. Matches the commit's default statement (Y_n < Y_oo up to 2584; bound +1.169e-05 at 2585). The default run does NOT certify EM.2's onset or level 2585; EM.3 (0.89) is fully certified by default.
- pytest (numpy CI): `pytest -q tests/test_flux_identity.py -k "em_exact or en_exact or el_exact"`: 3 passed (1.0 s).
- --full on this box (an earlier, interrupted slice's audit clone /workspace/ifi-em-audit at 4e72d34b6ed3; log /workspace/em_audit_full.log, finished 2026-11-15 9:02 PM EST; niced, shared box): `--full` EXIT 0, 2498.1 s (repo says 927.3 s), "all EM checks passed". Printed: 0.91 point (16000/256000) D'_oo [6.00139547, 6.0014498], |nu| [0.39711787, 0.397133255], 1-delta_1 [0.0766194814, 0.0766208692]; lower (12800/unit) L(14,20,26) >= 0.73971443, 0.73971486, 0.73971486, kappa_lo >= 0.07464970; lower-side bounds -4.325e-05, -2.406e-05, -4.863e-06, +1.435e-05 at 2583..2586; upper U(26) <= 0.73986384, kappa_hi <= 0.07466495, Phi(2586) >= 4.779e-06, Phi(2585) <= -1.443e-05; EE floats inside; exactly one sign change 2585 -> 2586. Every EM.2 number in the commit message is reproduced. The EM script is unchanged in substance between 4e72d34 and ceb654d (docstring only, EN.4).
- A fresh --full at ceb654d12046 in this slice was started at nice 15 at 6:57 AM EST, was CPU-starved on the loaded box (26 s CPU in 33 min after finishing EM.3), killed at 7:31 AM EST and restarted at nice 5; its result, if it completes, is recorded as a dated append below.
- Scope: points only (0.89, 0.91), N = 1 only, not alpha-cells; no proved rate for U - L -> 0. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Computer-assisted theorems at points, conditional on DISC-0249..0251's inputs; EM.1 a short proof; EM.4 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0251 (EL), DISC-0250 (EK), DISC-0249 (EJ), DISC-0246 (EG), DISC-0253 (EN, closes EM.4).

## Open Questions
alpha-cells instead of points; N >= 2 at 0.89/0.91; 0.88 level 9 (closed by DISC-0253); a proved rate for U - L -> 0.

## Next Experiments
Cell version of EJ.2 near 0.91 with EL.1/EM.1; N = 2, 3 at 0.91.

## Reproduction Instructions
Clone informational-flux-identity at 4e72d34b6ed3 (or ceb654d12046); pip install python-flint sympy numpy; python3 scripts/gasket_fractional_corner_exact_091.py (~6.5-14 min, 4 workers) and --full (~15-45 min; needed for EM.2); pytest -q tests/test_flux_identity.py -k em_exact.

## Evidence Log
- 2026-11-16 ~6:56-7:10 AM EST: default witness EXIT 0 (844.9 s); pytest 3 passed.
- 2026-11-15 ~9:02 PM EST (earlier interrupted slice, box log em_audit_full.log): --full EXIT 0 (2498.1 s) at 4e72d34b6ed3; EM.2 reproduced.

## Change History
- 2026-11-16: created.

- 2026-11-16 ~7:40 AM EST note (append; history above unchanged): EM.4's kept limit (0.88, level 9 undecided, bracket [8, 9]) is closed by DISC-0253 (Theorem EN, informational-flux-identity ceb654d12046): EN.1's two-sided D'_n gives Y_9 < Y_oo (lower side -2.344e-4), so exactly one sign change 9 -> 10 at (0.88, N = 1, n >= 2). EN.4 corrects EM's script docstring: the quoted "L(14) = 0.735421, 0.737856, 0.738466" (200/800/3200 cells/unit) should read L(12) >= 0.735421, 0.737853, 0.738463 (the 800/3200 values were unlogged and 3e-6 high); EM.1-EM.3 do not use them, so no EM claim changes. Status of DISC-0252 unchanged.
