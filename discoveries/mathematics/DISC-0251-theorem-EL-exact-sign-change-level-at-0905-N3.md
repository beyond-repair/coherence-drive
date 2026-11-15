# Discovery: Theorem EL, the exact sign-change level of Y_n - Y_oo at alpha = 0.905 for N = 3 (102 -> 103) via a left-node cell bound, and a sharper onset 2587 at alpha = 0.91

## Discovery ID
DISC-0251

## Status
THEOREM (mathematical sense only; EL.1 is a short monotonicity argument stated and proved in the repository from AQ (3); EL.2-EL.3 are arb certificates, 128 bits, per the repository's witness). Method KNOWN (monotone comparison bounds plus interval arithmetic, as DISC-0249/0250; using the monotone endpoint of a cell as the supremum is a standard interval technique). Novelty of the constants UNRESOLVED. Closes DISC-0250's open item "decide level 103 at (0.905, N = 3)". EL.4 OBSERVED. No status change elsewhere.

## Date Discovered
2026-11-15 (indexed ~4:10 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 7ba5c961c4a469f88bd22bc4fa6acdae4fef5cc8 (2026-11-15 3:49 PM EST); parent d2a34ff395c5 (Theorem EK, DISC-0250).

## Original Evidence
- GASKET.md §Theorem EL (+43/-5, incl. in-place marks on EK.1's "level 103 is not decided" sentence, EK's kept limit and open item, EJ's kept-limit bracket list and EJ.4's 0.91 table cell); CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_exact_0905_n3.py (new, 203 lines; imports EJ's module gasket_fractional_corner_two_sided_rate), registered in scripts/cli.py (+1); tests/test_cli.py (+15); tests/test_flux_identity.py (+33).

## Discovery
Setting and notation as DISC-0249 (gamma = log3/log5, rho = 5^alpha/3, Y_n the second correction, N the starting level, R_k(x) = (3/5)^k r_k(5^-k x)).
- EL.1 (THEOREM; every alpha in (gamma,1), k0 >= 1, 1 <= N <= k0; EJ.1 and AQ (3) as stated): R_k and Rh_k(x) = (5/3) R_(k+1)(5x) are nonincreasing in x, so on a cell [a,b] sup R_k <= R^hi(a) = min(1/3, G a^(gamma-1), 1/V^lo(a)), with V^lo evaluated at the single left node; EJ.1's cell sums for c_hi(k0), kappa_hi(N,k0) remain upper bounds with R, Rh taken at the left node. This replaces EJ's two-ended V^lo cell routine, whose excess decays like n^(-1/2) in the number of cells, by one decaying like O(1/n) (EL.4, OBSERVED).
- EL.2 (THEOREM, certified at the point alpha = 0.905; --full grids: EF.1 point cells 4000/32000, upper k0 = 26 on 3200 cells/unit): U(26) <= 0.739060, kappa_hi(1,2,3)(26) <= 0.075711, 0.621040, 1.722784; EJ.2's onset criterion first holds at 68, 84, 103 for N = 1, 2, 3 (Phi_3(103) >= 7.432e-4, Phi_3(102) <= -0.0118). With EK.1 (Y_n < Y_oo for n = 3..102) Y_n - Y_oo changes sign exactly once at N = 3, between 102 and 103. N = 1, 2 reproduce 67 -> 68 and 83 -> 84.
- EL.3 (THEOREM, certified; --full): alpha = 0.91, N = 1: Phi_1(2587) >= 2.13e-6 > 0, so Y_n > Y_oo for every n >= 2587 (EJ.4: >= 2616); last negative level in [2564, 2586] (EJ.4: [2564, 2615]).
- EL.4 (OBSERVED): convergence of kappa_hi(3,26) with grid: EJ's routine 1.73938/1.73453/1.73113 at 1000/2000/4000 cells/unit; EL.1's 1.73645/1.72551/1.722784 at 200/800/3200; EE.1's float limit 1.721863. Float crossings 68, 84, 103 (0.905) and 2586 (0.91).

## Why It Matters
Completes the "exactly one sign change" picture at alpha = 0.905 for N = 1, 2, 3 (68, 84, 103 onsets), and shows the remaining gap in DISC-0250 was a cell-routine artefact on the upper side (two large terms of V^lo taken at opposite cell ends), not a lower-side issue as EK's kept limit framed it.

## Derivation
EL.1: AQ (3) gives r_k(s) decreasing in s; hence R_k(x) = (3/5)^k r_k(5^-k x) is nonincreasing in x and Rh_k likewise, so the cell supremum is attained at the left node, where EJ.1's pointwise bound applies. EJ.1's cell sums are sums of such suprema against nonnegative weights (as stated in EJ.1; inherited, not re-derived here), so replacing the two-ended bound by the left-node bound preserves the upper-bound property. The rest of EL.2-EL.3 is EJ.1-EJ.2 evaluated in arb.

## Assumptions
Everything DISC-0249/0250 list (AQ (1)-(3), r_k(s) <= 1/s, BI.4, BK.1-2, BL, DZ.1-2, ED.1-2, EE.1, EG.1, EB.1/EI.1, EJ.1-EJ.2, EK.1), EF.1 cell routines valid at 0.905 and 0.91, python-flint arb and sympy correctness, and that EJ.1's cell-sum weights are nonnegative so a pointwise supremum bound transfers.

## New Results
Exact sign-change level 102 -> 103 at (0.905, N = 3); onset at (0.91, N = 1) improved 2616 -> 2587, bracket width 52 -> 23; sharper upper constants U(26) <= 0.739060, kappa_hi(3,26) <= 1.722784 (vs EK's 0.740363, 1.734107).

## Prior Art
As DISC-0244..0250 (Poincare-function asymptotics for gasket decimation; arb, Johansson; computer-assisted proofs, e.g. Tucker 2011). Using monotonicity to evaluate a cell supremum at one endpoint is standard interval-analysis practice. No external search in this slice.

## Novelty Analysis
Method KNOWN; the level 102 -> 103 and the onset 2587 are new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Logical consistency: EK.1 already had N = 3 positive for every n >= 104 and negative for 3..102, with 103 undecided; EL.2 decides 103 positive, so the combined statement is consistent (EK.2's +0.005534 was a failure to prove Y_103 < Y_oo, not evidence of the opposite). Float crossing at 103 (braces ~ +0.00125) agrees.
- Two-sided: U(26) > EK's L(14) >= 0.736435, kappa_hi(3,26) > kappa_lo(3,14) >= 1.70926; all EL upper values exceed EE.1's floats (0.738670, 1.721863). No contradiction.
- EL.1 direction check: nonincreasing in x means the LEFT node is the supremum (not a midpoint rule); the repository CI checks exact R_k, k = 26..41, at six points in cells at 5^1, 5^2.5, 5^4, 5^5 never exceeds R^hi(a). Not independently re-derived beyond reading AQ (3)'s statement.
- Repo default witness here (informational-flux-identity @ 7ba5c961c4a4, python3 + python-flint, niced, shared box): EXIT 0, 62.3 s, "all EL checks passed". Printed: D'_oo [5.86416, 5.86461], |nu| [0.4148389, 0.4150687]; upper k0 = 26, n = 1600: c_hi <= 0.257926, U(26) <= 0.739450, kappa_hi(1,2,3) <= 0.075751, 0.621367, 1.723692; N = 1 Phi(68) >= 1.847e-4, Phi(67) <= -5.275e-4; N = 2 Phi(84) >= 3.201e-3, Phi(83) <= -1.893e-3; N = 3 Phi(103) >= 2.351e-4 (matches the commit's default value), Phi(102) <= -0.0123.
- tests/test_flux_identity.py -k "EL or el_ or 0905": 3 passed.
- Scope: one alpha point (0.905) plus 0.91 at N = 1, N <= 3, closure grid-limited (margins 7.4e-4 at --full, 2.35e-4 at default; 2.13e-6 at 0.91 is thin), no proved rate for U - L -> 0, 0.88/0.89 unchanged. KEPT FAILURE: none.
- --full run here (250.5 s inside the script, 251 s wall, niced, EXIT 0, "all EL checks passed"; repo says 222.6 s): point D'_oo [5.86427, 5.8645], |nu| [0.4148964, 0.4150113], 1-delta_3 [0.555176, 0.555218]; upper k0 = 26, n = 3200: c_hi <= 0.257790, U(26) <= 0.739060, kappa_hi(1,2,3) <= 0.075711, 0.621040, 1.722784; N = 1 Phi(68) >= 2.133e-4; N = 2 Phi(84) >= 3.405e-3; N = 3 Phi(103) >= 7.432e-4, Phi(102) <= -0.0118, exactly one sign change 102 -> 103; alpha = 0.91, N = 1: |nu| [0.3970713, 0.3971799], U(26) <= 0.740156, kappa_hi(1) <= 0.074694, Phi(2587) >= 2.13e-6, last negative level in [2564, 2586]. Every EL.2-EL.3 number in the commit is reproduced.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Computer-assisted theorem at a point, conditional on DISC-0249/0250's inputs; EL.1 a short proof; EL.4 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0250 (EK), DISC-0249 (EJ), DISC-0248 (EI), DISC-0247 (EH).

## Open Questions
alpha-cells instead of points; N >= 4; exact level at 0.91 (bracket [2564, 2586]); 0.88, 0.89 exact levels; apply EL.1's left-node bound to the lower side (EG's routine has the same end-mixing); a proved rate for U - L -> 0.

## Next Experiments
Port EL.1 to EG's lower routine and retry 0.91 (float braces -+1e-5 at 2585/2586); cell version of EJ.2 around 0.905.

## Reproduction Instructions
Clone informational-flux-identity at 7ba5c961c4a4; pip install python-flint sympy numpy; python3 scripts/gasket_fractional_corner_exact_0905_n3.py (~1 min) and --full (~4-6 min); pytest -q tests/test_flux_identity.py.

## Evidence Log
- 2026-11-15 ~4:00 PM EST: default EXIT 0 (62.3 s), pytest 3 passed.
- 2026-11-15 ~4:08 PM EST: --full EXIT 0 (250.5 s); 102 -> 103 at (0.905, N = 3) and onset 2587 at (0.91, N = 1) reproduced.

## Change History
- 2026-11-15: created.
