# Discovery: Theorem EA, the corner deficit has an exact positive second-order correction of order (rho/5)^N, so rho^N delta_N is eventually strictly decreasing

## Discovery ID
DISC-0240

## Status
THEOREM (mathematical sense only; EA.1–EA.3 have written proofs in the repository, conditional on BD.4, BH.2, BJ.3/BJ.4/BJ.6, BR.4, BS.1, CB.2–CB.3, DZ.2–DZ.3 and AZ (3) as stated; EA.4's numbers are arb-certified at alpha = 0.8 only). Method KNOWN (exact algebraic identity, change of variables, monotone/dominated convergence, outward-rounded interval arithmetic). Novelty of the specific results and constants UNRESOLVED. Answers BJ's open item "whether rho^N delta_N is eventually monotone" (see dated note on DISC-0153).

## Date Discovered
2026-11-13 (indexed ~9:15 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 0a46e2094140f32db5bc36921e521454b06274ef (2026-11-13 8:21 AM EST); parent 6630f9bcfbfa (Theorem DZ, DISC-0238/DISC-0239).

## Original Evidence
- GASKET.md §Theorem EA (header line 5748; statement EA.1–EA.5 follow; proof line 5798; attempts to break it, kept limits line 5802, NOT THIS), +73/-3 lines overall.
- GASKET.md line 2131 (BJ.6's derived limit annotated "proved directly ... by Theorem EA.1") and line 2182 (BJ's open item "Whether rho^N delta_N is eventually monotone" marked PROVED by EA.2, original wording kept).
- CLAIM_STATUS.md line 135 (new row); README.md (+3/-1).
- scripts/gasket_fractional_corner_second_order.py (new, 496 lines); registered in scripts/cli.py; tests/test_cli.py test_theorem_ea_corner_second_order (+36 lines).

## Discovery
Setting as in Theorems BH, BJ, BR, BS, CB, DZ: alpha in (gamma, 1), gamma = log3/log5, rho = 5^alpha/3, delta_N the limit corner deficit (BJ.4), Q_oo the rescaled limit resolvent (BS.1), Pi(u) = prod_(j>=1) (5/3) beta(x_j), Xi(t) = prod_(j>=1) (x_j+6)/(3(x_j+2)), pi_N BH.2's remainder (1 - eta_N = 1 - eta + pi_N), h = Q_oo - R > 0.
- EA.1 (proved, every alpha, N >= 0): rho^N delta_N = c_corner + E_N, c_corner = kappa int t^-alpha Q_oo (1 - eta o psi) dt, E_N = kappa int t^(1-alpha) Q_oo^2 pi_N(psi) Xi / (2(1 + 2 Q_oo pi_N(psi) Pi)) dt > 0. So the limit exists without AT.1 and is approached strictly from above.
- EA.2 (proved, every alpha): E_N = kappa (rho/5)^N I_N, kappa I_N -> K_corner = (kappa/4) int u^(1-alpha) h du in (0, oo), with every-N >= N0 brackets K^-_N0 <= kappa I_N <= K^+_N0 converging to K_corner. Hence delta_N = c_corner rho^-N + K_corner 5^-N + o(5^-N) and rho^N delta_N is eventually strictly decreasing.
- EA.3 (corollary with DZ.2–DZ.3): -nu_alpha - C_delta(alpha, N) = -nu_alpha rho^-N (c_corner + E_N); C_delta increases to -nu_alpha with gap of exact order rho^-N and second-order term of exact order 5^-N.
- EA.4 (arb, alpha = 0.8; 56367 cells on [1e-15, 5^8], closed heads/tails): K_corner in [0.0747956, 0.0748243]; K^-_1 in [0.0666158, 0.0666414], K^+_1 in [0.1001359, 0.1001756]; (rho/5) K^+_1 < K^-_1, so rho^N delta_N(0.8) strictly decreases for every N >= 0 (with delta_0 = 3/2 > rho delta_1). C_delta(0.8, N) in [0.031293, 0.031327], [0.158926, 0.158951], [0.258205, 0.258225], [0.461475, 0.461487], [0.602532, 0.602538] for N = 1, 2, 3, 6, 10: inside DZ.4's level-60 brackets (DISC-0239), 33–41x narrower. -nu c_corner in [0.826298, 0.826333], -nu K_corner in [0.054410, 0.054431].
- EA.5 (floats only): c_corner(0.8) ~ 1.1359144728, K_corner ~ 0.0748099777; E_N (5/rho)^N decreasing toward K_corner (observed only, not claimed).

## Why It Matters
Gives the full two-term asymptotics of the corner deficit and closes BJ's monotonicity question (open since 2026-10-23). Combined with DZ (DISC-0238) it pins down how fast the N-dependent limit C_delta(alpha, N) of DISC-0239 approaches -nu_alpha, and it re-derives BJ.6's limit without the AT.1 profile assumption.

## Derivation
EA.1: from BR.4's scaling and BH.2, rho^N delta_N = kappa int t^-alpha Q_N (1 - eta(psi) + pi_N(psi)). BS.1's 1/Q_N = 1/Q_oo + (3/5)^N Phi(5^N .) splits, via psi(5^(N-k) t) = p^(N-k)(psi(t)), into 1/Q_N = 1/Q_oo + 2 pi_N(psi) Pi. CB.3 gives 1/Q_oo = Pi (2(1 - eta(psi)) + psi/2). With A = 1 - eta: Q_N (A + pi) - Q_oo A = Q_oo pi (1 - 2 Q_oo A Pi)/(1 + 2 Q_oo pi Pi) = Q_oo^2 pi Pi psi / (2(1 + 2 Q_oo pi Pi)) (re-derived by hand here), and Pi psi = t Xi since psi(t)/t = prod (x_j+5)/5 and (5/3) beta(x)(x+5)/5 = (x+6)/(3(x+2)). EA.2: t = 5^-N u, Q_oo(5^-N u) = (5/3)^N Q_oo(u), pi_N = (3/5)^N b_N; the powers combine to 5^(-N(2-alpha)) (5/3)^(2N) (3/5)^N = (rho/5)^N (re-checked here). Limit integrand Q^2 (Phi/2)/(2(1 + Q Phi)) = h/4; brackets from monotonicity of the integrand in b, Xi, Pi; dominator integrable because 2 gamma - 1 < alpha < 2 gamma. Monotonicity: E_(N+1)/E_N <= (rho/5) K^+_N0 / K^-_N0 -> rho/5 < 1.

## Assumptions
BD.4 and BJ.6's v <= psi(v) <= v e^(v/10), psi(5v) = p(psi(v)); BH.2; BJ.3 (g_lo, g_hi); BJ.4; BJ.6 (finiteness of M_alpha, certified band of c_corner at 0.8); BR.4's scaling; BS.1; CB.2–CB.3; DZ.2–DZ.3; AZ (3)'s nu_0.8; BL.0 (delta_0 = 3/2); BR.3 (delta_N decreasing). Textbook: monotone and dominated convergence. python-flint arb correctness.

## New Results
Exact positive correction E_N for every alpha and N; exact rate (rho/5)^N with certified constant K_corner(0.8); eventual strict monotonicity of rho^N delta_N for every alpha, and monotonicity for every N at 0.8; certified C_delta(0.8, N) about 35x narrower than DZ.4's.

## Prior Art
Two-term asymptotics of renormalised resolvent/Green-function integrals on the Sierpinski gasket via decimation (Kigami; Strichartz; Fukushima–Shima spectral decimation; Teplyaev) are standard in form; interval enclosures follow Tucker 2011 / arb (Johansson). No external source for these specific constants was searched in this slice.

## Novelty Analysis
Method KNOWN. The specific identity for E_N, the constant K_corner and the certified values are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Re-derived EA.1's algebraic identity by hand from 1/Q_N = 1/Q_oo + 2 pi Pi and 1/Q_oo = Pi(2A + psi/2): holds. Re-checked the beta identity (5/3)(x+6)/((x+2)(x+5)) (x+5)/5 = (x+6)/(3(x+2)) and EA.2's scaling exponent: hold.
- Positivity of E_N (every factor positive) and EA.3 (-nu - C_delta = -nu delta_N from C_delta = -nu (1 - delta_N)): hold.
- Independent mpmath (30 digits) from the published brackets: (rho/5) at 0.8 = 0.2415932; E_1 = [0.0200561, 0.0200641], E_10 = [5.06668, 5.06862]e-8 match the table; C_delta(0.8, N) recomputed as nu_0.8 (1 - rho^-N [row]) gives [0.0312926, 0.0313266], [0.1589262, 0.1589512], [0.2582045, 0.2582247], [0.4614755, 0.4614868], [0.6025323, 0.6025376] (N = 1, 2, 3, 6, 10), matching EA.4 to rounding and inside DZ.4's brackets; -nu c_corner = [0.826298, 0.826333] and -nu K_corner = [0.054410, 0.054431] reproduced.
- DEFECT (cosmetic, no effect on the conclusion): (rho/5) K^+_1 with K^+_1's upper end 0.1001756 is 0.02420175, so GASKET's and CLAIM_STATUS's "(rho/5) K^+_1 <= 0.02420" rounds an upper bound down (false by 1.7e-6; the script prints the value with 5 decimals). The certificate's inequality against K^-_1 >= 0.0666158 holds with a wide margin.
- Not done here: an independent quadrature of c_corner or K_corner (earlier archive work reproduced BJ.6's band); c_corner remains certified only to BJ.6's 4.8e-5 width, as the repo states.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EA.1–EA.3), conditional on the listed inputs; EA.4 computer-assisted at alpha = 0.8; EA.5's monotonicity of E_N (5/rho)^N observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0153 (Theorem BJ; open monotonicity item answered, BJ.6's limit re-derived without AT.1), DISC-0238 (Theorem DZ; C_delta formula used, rate in N now known), DISC-0239 (Kept Failure DZ.4; brackets sharpened 33–41x), DISC-0127 (Theorem AZ; nu_0.8 used).

## Open Questions
Closed forms for c_corner, K_corner, nu_alpha; the third-order term of delta_N; whether E_N (5/rho)^N is monotone; N_0(alpha) off 0.8; DZ's second-order term in n (not N); a flux functional on the infinite gasket.

## Next Experiments
Re-certify c_corner(0.8) at width comparable to K_corner's; certify K_corner at alpha = 0.9; identify the 25^-N or (rho/25)^N-type third term from EA.1's integral.

## Reproduction Instructions
Clone informational-flux-identity at 0a46e2094140f32db5bc36921e521454b06274ef; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_second_order.py` (~10 s); test `python3 -m pytest -q tests/test_cli.py -k test_theorem_ea`.

## Evidence Log
- 2026-11-13 ~9:05 AM EST: repo default witness `python3 scripts/gasket_fractional_corner_second_order.py` (niced, OPENBLAS_NUM_THREADS = 1) EXIT 0, "Theorem EA: all checks passed (8.9s)", 9.6 s wall (repo states 10.3 s). Printed N = 10 float: rho^N delta_N = 1.135914523471, direct difference 5.067658e-08 vs EA.1 integral 5.067654e-08.
- 2026-11-13 ~9:10 AM EST: mpmath arithmetic and hand derivations PASS; (rho/5) K^+_1 display defect noted.

## Change History
- 2026-11-13: created.
