# Discovery: Theorem DZ, the renormalised corner deficit has a limit C_delta(alpha, N) = -nu_alpha (1 - delta_N), and C_alpha < 0 on all of (gamma, 1)

## Discovery ID
DISC-0238

## Status
THEOREM (mathematical sense only; DZ.1–DZ.3 have written proofs in the repository, conditional on AQ, BH.2, BI.4, BK.2, BL.1, AZ (1)/(3), BN.4 and BJ (6) as stated; DZ.4's numbers are arb-certified at alpha = 0.8 only). Method KNOWN (substitution / change of variables, monotone convergence, outward-rounded interval arithmetic). Novelty of the specific results and constants UNRESOLVED. Proves the limit part of Conjecture BL.6 (DISC-0159) with the limit identified, and AZ's open item "whether C_alpha < 0 on all of (gamma, 1)" (DISC-0127). BL.6's clause "independent of N" is false: recorded separately as DISC-0239 (REJECTED, Kept Failure DZ.4). Not thrust.

## Date Discovered
2026-11-13 (indexed ~8:15 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 6630f9bcfbfaa421c133ec52339a3a0c41fbe7e3 (2026-11-13 7:12 AM EST); parent 91838c872b39 (Theorem DY, DISC-0237).

## Original Evidence
- GASKET.md §Theorem DZ (line 5686; statement 5696–5727, proof 5729, attempts to break it 5731, kept limits 5733, NOT THIS 5737), +64/-2 lines overall.
- GASKET.md line 1805: AZ's OPEN list now marks "whether C_alpha < 0 on all of (gamma,1)" as PROVED by DZ.3.
- GASKET.md line 2398: Conjecture BL.6 header annotated in place (limit part PROVED by DZ, "independent of N" FALSE by DZ.4; original wording kept).
- CLAIM_STATUS.md line 134 (new row); README.md (+2/-1).
- scripts/gasket_fractional_corner_limit.py (new, 420 lines; imports BI's gasket_fractional_uniform_limit unchanged for G); registered in scripts/cli.py; tests/test_cli.py test_theorem_dz_corner_limit (+34 lines).

## Discovery
Setting: alpha in (gamma, 1), gamma = log3/log5, rho = 5^alpha/3, p(s) = s(s+5), r_k the corner resolvent, J_k = int_0^oo s^-alpha r_k ds, D'_k = rho^-k J_k, eta_N = alpha_1 + beta eta_(N-1) o p, eta_0 = -1/2, delta_N^(k) = J_k^-1 int s^-alpha r_k (1 - eta_N(p^(k-N) s)) ds.
- DZ.1 (proved, every alpha in (gamma,1), N >= 1, k >= N): with H_k = J_k (1 - delta_N^(k)), BK.1's substitution t = p(s) gives exactly H_(k+1) = rho int t^-alpha r_k(t) eta_N(p^(k-N) t) omega_k(q(t)) dt, omega_k >= 1 (BK.2). So rho^-k H_k increases to h_oo = (1 - delta_N) D'_oo with 0 <= h_oo - rho^-k H_k <= (3/2) a_N 3^-k + b_N (5 rho)^-k / (1 - 1/(5 rho)); ingredients omega_k - 1 <= K_1 s^gamma on s <= q(1) < 1/5, m_0 = 2/3 - 1/(21 + 6 sqrt 10), eta_N <= min(1, 2/z), BI.4's G = 0.6031, and rho 5^(2 gamma - alpha) = 3.
- DZ.2 (proved from DZ.1 and AZ (1)): exact identity X_k := rho^k (delta_N - delta_N^(k)) = [-h_oo (C' + eps_k) - rho^k eta_k D'_oo] / (D'_k D'_oo), hence X_k -> C_delta(alpha, N) = -nu_alpha (1 - delta_N), nu_alpha = C_alpha / A_alpha. At alpha = 0.8: |X_k - C_delta| <= 2.77e-7 (N = 1) .. 5.23e-6 (N = 10) for every k >= 60.
- DZ.3 (corollary with BN.4, BJ (6)): c_N <= -nu_alpha (1 - delta_N), so nu_alpha < 0 and C_alpha < 0 for every alpha in (gamma, 1); rho^n ||F(n, alpha)|| approaches K_alpha from above on the whole range (AZ.1's sign, DISC-0128, now everywhere); C_delta(alpha, N) -> -nu_alpha as N -> oo.
- DZ.4: see DISC-0239 (Kept Failure: the limit depends on N; certified at 0.8: C_delta(0.8, N) in [0.030733, 0.031869], [0.158436, 0.159369], [0.257779, 0.258555], [0.461214, 0.461662], [0.602405, 0.602621] for N = 1, 2, 3, 6, 10).
- DZ.5 (floats): nu_0.8 ~ -0.7274459 from J_70, J_80; nu_0.9 ~ -0.4328054; -nu (1 - delta_6) at 0.9 ~ 0.364298 reproduces BM's 0.3643; BL's 0.6025 is the N = 10 value at 0.8.

## Why It Matters
Closes the oldest open item in the BK–BN corner-deficit chain (BL.6's limit, open since 2026-10-23) and identifies the limit as a product of one N-free scalar (AZ's intercept ratio nu_alpha) and the limit deficit share 1 - delta_N. As a by-product it settles the sign of AZ's intercept C_alpha on all of (gamma, 1), previously known only near gamma and at 0.75, 0.8.

## Derivation
DZ.1: substitute s = q(t) in H_(k+1); AQ (1) turns r_(k+1)(s) into r_k(t)/(beta - e r_k(t)); collecting factors gives rho times BK.1's weight. Summing rho^-(j+1)(H_(j+1) - rho H_j) over j >= k with the bounds on omega_k - 1 (t <= 1) and omega_k (t >= 1) gives the 3^-k + (5 rho)^-k gap. DZ.2: delta_N - delta_N^(k) = rho^-k H_k / D'_k - h_oo / D'_oo with AZ (1) for D'_k; algebra. DZ.3: BN.4's X_k >= c_N > 0 passes to the limit.

## Assumptions
AQ (1)–(3), BH.2, BI.4 (G re-run live), BK.2 (omega_k >= 1), BL.1 (eta_N positive, decreasing, eta_N(0) < 1), AZ (1) and AZ (3)'s certified A_0.8, C_0.8, nu_0.8, E_60^+-; for DZ.3 only BN.4 and BJ (6); BN.5's c_1, c_2 and BK/BN's 4.6644 ceiling for consistency only. Textbook: substitution, monotone convergence. python-flint arb correctness.

## New Results
Existence and identification of lim rho^n (delta_N - delta_N^(n)) for every alpha in (gamma, 1), N >= 1, with an explicit error bound; C_alpha < 0 on all of (gamma, 1); certified C_delta(0.8, N) for N = 1, 2, 3, 6, 10.

## Prior Art
Change of variables / renormalisation transfers and monotone convergence are textbook; interval enclosures follow Tucker 2011 / Moore-style outward rounding (arb, Johansson). Second-order asymptotics of resolvent integrals on the Sierpinski gasket via decimation are standard in analysis on fractals (Kigami; Strichartz; Fukushima–Shima on spectral decimation). No external first is claimed or supported.

## Novelty Analysis
Method KNOWN. The specific limit formula, the sign result and the certified constants are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Independent float quadrature written from scratch (archive script /workspace/ifi-dz-indep/indep.py, numpy; does not import the IFI script): recursion r_(k+1)(s) = r_k(p s)/(beta(s) - e(s) r_k(p s)) along orbits, trapezoid in log s on [5^-130, 1e14] with analytic tails, steps 4e-3 and 2e-3 agree. J_60 = 536714.608914 (repo's AZ (1) value 536714.608916 inside the repo's arb bracket [536383.90, 536821.86]); from J_79, J_80: A = kappa D'_oo = 2.3964097040 (AZ 2.3964097040), C = kappa C' = -1.74325718 (AZ -1.7432571784), nu_0.8 = -0.727445386 (AZ -0.7274453844). PASS.
- Same script, delta_N^(80)(0.8) = 0.9569594, 0.7815111, 0.6450391, 0.3656139, 0.1717109 (N = 1, 2, 3, 6, 10), giving -nu (1 - delta_N) = 0.031310, 0.158939, 0.258215, 0.461481, 0.602535: each inside the repo's certified bracket; X_30, X_40 (reference level 80) = 0.03139/0.03131, ..., 0.60401/0.60245, converging to those values. PASS.
- mpmath (40 digits): m_0 = 2/3 - 1/(21 + 6 sqrt 10) = 0.64165019705, equal to the numeric minimum of 2/3 - s/(3s^2 + 21s + 30) at s = sqrt 10 = 3.16227766 (>= 0.641650 PASS); rho 5^(2 gamma - alpha) = 3 exactly (5^gamma = 3), checked at alpha = 0.69, 0.8, 0.9, 0.99 (PASS); q(1) = 0.19258 < 1/5 (PASS); identity B - C/p = (s+4)(2s+5)/(3(s+2)(s+5)) = 2/3 - s/(3s^2+21s+30) checked by hand (PASS); C_0.8/A_0.8 = nu_0.8 to 20 digits (PASS).
- DEFECT (cosmetic, no effect on any certified number): K_1 = ((1/5 + 0.14) 5^(gamma-1) + 1.8 G 5^(gamma-1))/m_0 = 1.33304408529 with G = 0.6031, so the stated "K_1 <= 1.333044" (GASKET line 5705, commit message, script message) is false by 8.5e-8; the script only asserts K_1 < 1.34 and prints float(K1.upper()) with %.6f, which rounds down. All downstream bounds (a_N, ebar_k) use the arb K_1, so nothing certified changes; the honest display is K_1 <= 1.333045.
- Logical check of DZ.2: re-derived the identity from delta_N^(k) = 1 - rho^-k H_k / D'_k, delta_N = 1 - h_oo / D'_oo and D'_k = D'_oo + rho^-k (C' + eps_k); limit -h_oo C' / D'_oo^2 = -(1 - delta_N) C'/D'_oo = -nu_alpha (1 - delta_N) since nu = C/A = kappa C'/(kappa D'_oo). Holds.
- Logical check of DZ.1's gap: the sum uses rho^-j 5^(-j(2 gamma - alpha)) = 3^-j and rho^-j 5^-j; the t <= 1 integrand bound uses s <= t/5 and r_k <= r_oo <= G t^(gamma-1); the t >= 1 bound uses omega_k (not omega_k - 1), which is an overestimate. Holds.
- Logical check of DZ.3: BN.4 gives X_k >= c_N > 0 for all k >= N; with DZ.2 the limit is >= c_N > 0; 1 - delta_N = h_oo/D'_oo > 0 and A_alpha > 0 give nu_alpha < 0 and C_alpha < 0. Valid for every alpha in (gamma, 1) provided AZ (1), BN.4 and BJ (6) hold on all of (gamma, 1) as the repository states (their headers/settings say so); not re-verified here.
- Scope: certified numbers only at alpha = 0.8 (the repo says so); DZ.3's side bound -nu_alpha <= (3/2) J_alpha/((1 - rho^-1) D'_0) was not checked here. In GASKET line 5716 the ceiling is written "<= 7.2e-6 rho^60" for X_60 (equivalently delta_N - delta_N^(60) <= 7.2e-6, as the script prints); consistent, but the units differ from the commit message's "<= 7.2e-6".
- Repo default witness and unit test: see Evidence Log.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (DZ.1–DZ.3), conditional on the listed AQ/BH/BI/BK/BL/AZ/BN/BJ inputs; DZ.4's values computer-assisted at alpha = 0.8.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0159 (Conjecture BL.6; limit part proved, N-independence rejected), DISC-0239 (Kept Failure DZ.4), DISC-0127 (Theorem AZ; open sign item proved), DISC-0128 (Kept Failure AZ.1; sign now on the whole range), DISC-0155 (BK; transfer reused), DISC-0157 (BL), DISC-0160 (BM; 0.3643 reproduced), DISC-0161 (BN; BN.4 floor used), DISC-0153 (BJ; delta_N = O(rho^-N)), DISC-0151 (BI; G re-run).

## Open Questions
Closed forms for delta_N, nu_alpha, C_delta; certified nu_alpha at alpha other than 0.75, 0.8; sign and rate of the second-order term of X_k - C_delta; a flux functional on the infinite gasket.

## Next Experiments
Certify nu_alpha and C_delta(alpha, N) at alpha = 0.9 (BM's exponent) to turn DZ.5's floats into enclosures; certify the second-order term (1 - delta_N) C'^2 rho^-k / D'_oo^2.

## Reproduction Instructions
Clone informational-flux-identity at 6630f9bcfbfaa421c133ec52339a3a0c41fbe7e3; `pip install python-flint mpmath sympy numpy`; `python3 scripts/gasket_fractional_corner_limit.py` (~7 s); test `python3 -m pytest -q tests/test_cli.py -k test_theorem_dz`.

## Evidence Log
- 2026-11-13 ~8:05 AM EST: repo default witness `python3 scripts/gasket_fractional_corner_limit.py` (niced, BLAS threads = 1) EXIT 0, "all DZ checks passed", 6.8 s wall (repo states 6.6 s); unit test `pytest -k test_theorem_dz` 1 passed, 7.1 s wall (repo states 6.3 s). Printed values match GASKET: m_0 >= 0.641650, 69052 cells, J_60 in [536383.898973, 536821.858922], the five C_delta(0.8, N) brackets, ceiling 7.191e-6 <= 5.566e-5, rate bounds 2.766e-7 .. 5.231e-6.
- 2026-11-13 ~8:10 AM EST: independent numpy quadrature and mpmath arithmetic PASS; K_1 display defect found (see Falsification Attempts).

## Change History
- 2026-11-13: created.
