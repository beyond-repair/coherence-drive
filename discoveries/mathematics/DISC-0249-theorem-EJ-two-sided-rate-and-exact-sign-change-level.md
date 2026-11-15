# Discovery: Theorem EJ, a two-sided every-level rate for (3/rho)^n eps_n and 3^n eta_n, and the exact sign-change level of Y_n - Y_oo at alpha = 0.9 and 0.905

## Discovery ID
DISC-0249

## Status
THEOREM (mathematical sense only; EJ.1-EJ.2 are proved in the repository from AQ (1)-(3), r_k(s) <= 1/s, BI.4, BK.1-2, BL, DZ.1-2, ED.1, EE.1, EG.1, EB.1/EI.1 as stated, with sympy checks; EJ.3-EJ.4 are arb-certified at points; EJ.5 is floats, OBSERVED). Method KNOWN (monotone upper/lower comparison and interval arithmetic). Novelty of the constants UNRESOLVED. The exact levels in EJ.3 are a --full certificate; this slice reproduced only the default grid (see Falsification Attempts). Answers DISC-0248's open items (two-sided rate; exact sign-change level and count at 0.9 / 0.905), DISC-0247's kept limit (no exact sign-change position) and DISC-0246's open item (an every-n upper bound for c_k). No status change elsewhere.

## Date Discovered
2026-11-15 (indexed ~1:15 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 344496c145e9077c42cd1da2f4279b6c358e2882 (2026-11-15 12:03 PM EST); parent 74dea9103351 (Theorem EI, DISC-0248).

## Original Evidence
- GASKET.md §Theorem EJ (+80/-8 lines overall, incl. in-place annotations of EI's, EH's and EG's kept limits and open items, original wording kept); CLAIM_STATUS.md (+2/-1); README.md (+3/-1).
- scripts/gasket_fractional_corner_two_sided_rate.py (new, 523 lines), registered in scripts/cli.py (+1); tests/test_cli.py (+18); tests/test_flux_identity.py (+20).

## Discovery
Setting as EE-EI: gamma = log3/log5, alpha in (gamma,1), rho = 5^alpha/3, g = 3/rho^3, p(s) = s(s+5), beta(s) = (s+6)/((s+2)(s+5)), e(s) = 2s/(2+s), u_(k+1)(s) = beta(s) u_k(ps) - e(s), u_0 = 3+s.
- EJ.1 (THEOREM; every alpha in (gamma,1), k0 >= 1, 1 <= N <= k0, (3/rho) beta(p^k0(1)) <= 1): EG.1's monotonicities read the other way give R_k <= R^hi = min(1/3, G x^(gamma-1), 1/V^lo_k0) for every k >= k0; the t >= 1 region is bounded via u_k - u_(k+1) = prod_(j<k) beta(p^j t) (p^k t+6)/(p^k t+5); the 3^k(omega^0-1) term via log omega^0 <= 0.9 q. Hence c_k <= c_hi(k0), 3^n eta_n <= 1.5 kappa_hi_N(k0), and with EG.1 L(k0) <= (3/rho)^n eps_n <= U(k0) = 3 c_hi/(2(1-rho/3)) for every n >= k0: a two-sided every-level rate.
- EJ.2 (THEOREM): EI.1's monotone criterion with U, 1.5 kappa_hi (one n1 gives Y_n > Y_oo for every n >= n1), plus a per-level criterion with L, kappa_lo certifying Y_n < Y_oo at each n separately.
- EJ.3 (arb, 128 bits, --full, per the repository): at 0.9, (3/rho)^n eps_n in [0.728801, 0.740579] for every n >= 14 (EI used B_0.9 <= 1.0284e3); N = 1: Y_n < Y_oo for n = 1..32, Y_n > Y_oo for every n >= 33, so exactly one sign change; N = 2: 40 -> 41; N = 3: 50 -> 51; 0.905, N = 1: 67 -> 68; 0.905, N = 2, 3: last negative level in [82,83], [101,103].
- EJ.4 (arb, N = 1): onset 6, 6, 6, 10, 16, 33, 68, 2616 at 0.7, 0.8, 0.85, 0.88, 0.89, 0.9, 0.905, 0.91 (6 is the method's floor); negative windows [2,8] at 0.88 and [2,14] at 0.89 (first certified windows below EH.4's range), [1,2564] at 0.91.
- EJ.5 (OBSERVED, floats): U ~ 0.73819, kappa_hi(1) ~ 0.07686 against EE's e* ~ 0.73770, kappa_1 ~ 0.07670; float crossing 33.

## Why It Matters
EI's onset levels were upper bounds driven by a bound ~1.4e3 times too large. EJ closes the gap from above, so the sign of the second correction Y_n - Y_oo is decided level by level: at 0.9 and 0.905 it changes sign exactly once, at a stated level. This settles the "once or several times" question at those points.

## Derivation
Checked here independently: the telescoping identity u_k - u_(k+1) = prod_(j<k) beta(p^j t) (p^k t+6)/(p^k t+5) follows from u_k(s) - u_(k+1)(s) = beta(s)(u_(k-1)(ps) - u_k(ps)) and u_0 - u_1 = (s+6)/(s+5); verified in exact rational arithmetic (Python Fraction) for t in {1/7, 1/2, 1, 3, 10/3}, k = 0..4: 0 mismatches. The rest of EJ.1 rests on EG.1's monotonicities and the listed inputs, as stated in the repository; not re-derived here.

## Assumptions
AQ (1)-(3); r_k(s) <= 1/s; BI.4 (G = 0.6031); BK.1-2; BL; DZ.1-2; ED.1-2; EE.1; EG.1 and its certify_lower; EB.1 / EI.1's identity; EF's cell routines; python-flint arb and sympy correctness.

## New Results
Every-level two-sided enclosure of (3/rho)^n eps_n and 3^n eta_n; exact single sign change of Y_n - Y_oo at 0.9 (N = 1, 2, 3) and 0.905 (N = 1); onset levels 4-5x lower than EI's at every tested alpha; first certified initial negative windows at 0.88 and 0.89.

## Prior Art
As DISC-0244..0248 (Poincare-function asymptotics for gasket decimation; arb, Johansson; computer-assisted proofs, Tucker 2011). Two-sided comparison bounds are standard. No external search in this slice.

## Novelty Analysis
Method KNOWN; constants and sign-change levels new to the corpus; external novelty UNRESOLVED, modest.

## Falsification Attempts
- Repo default witness EXIT 0 here (207.4 s wall under load; repo says 172.7 s), "all EJ checks passed". Default (coarser) grid values: at 0.9, k0 = 14, U <= 0.746441, L(12) >= 0.708819; onset 34 (N = 1), 42 (N = 2), 52 (N = 3); last negative level in [31,33] (the witness prints "--full: exactly 32"); at 0.905, onsets 70 / 85 / 105; EJ.4 onsets 6, 6, 6, 10, 16, 34, 70, 2693 with windows [2,8], [2,14], [1,31], [1,65], [1,2494]. Every default value is weaker than or equal to the --full value in the commit, as it should be.
- --full (633 s per repo) was NOT run in this slice: the box had under 1 GB free memory because of another long-running job, so the exact levels 32 -> 33, 40 -> 41, 50 -> 51, 67 -> 68 are taken from the repository's --full certificate and are unverified here. This is the main open check.
- tests/test_flux_identity.py: 12 passed.
- Consistency: every EJ onset is <= EI's n1 (DISC-0248); 0.9's last negative level 32 lies in EI.3's [8,158], 0.905's 67 in [21,315], 0.91's [2564,2615] in [926,11583]; every EJ negative window contains EH.4's (DISC-0247); [L(12),U(14)] contains EG.4's e*(0.9) [0.73737,0.73802]; EI.4's float crossings 33, 41, 51 (0.9, N = 1, 2, 3) coincide with EJ.3's exact onsets. No contradiction found.
- Scope: exact level only at 0.9 (N <= 3) and 0.905 (N = 1); points, not alpha-cells; signs at n < 6 and windows at 0.7-0.85 undecided; no proved rate for U - L -> 0. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
Theorem as stated (EJ.1-EJ.2 proved conditional on the listed inputs); EJ.3-EJ.4 computer-assisted; EJ.5 observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0248 (EI), DISC-0247 (EH), DISC-0246 (EG), DISC-0244 (EE), DISC-0243 (ED), DISC-0241 (EB).

## Open Questions
A proved rate for U(k0) - L(k0) -> 0; alpha-cells instead of points; exact levels for N >= 2 at 0.905 and at 0.88, 0.89, 0.91; initial windows below 0.88; signs at n < 6.

## Next Experiments
Run --full on an unloaded box and confirm 32 -> 33, 40 -> 41, 50 -> 51, 67 -> 68; cell version of EJ.2 on (gamma, 4 gamma/3).

## Reproduction Instructions
Clone informational-flux-identity at 344496c145e9077c42cd1da2f4279b6c358e2882; pip install python-flint sympy numpy; python3 scripts/gasket_fractional_corner_two_sided_rate.py (~3 min) and --full (~10.5 min); pytest -q tests/test_flux_identity.py.

## Evidence Log
- 2026-11-15 ~1:10 PM EST: default EXIT 0 (207.4 s); pytest test_flux_identity.py 12 passed; exact-rational telescoping check 0 mismatches; --full not run (memory).

## Change History
- 2026-11-15: created.
