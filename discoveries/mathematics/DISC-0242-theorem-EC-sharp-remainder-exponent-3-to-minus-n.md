# Discovery: Theorem EC, the corner-deficit remainder is O(3^-n), not O(5^-0.65n), on all of (gamma, 1), extending EB's third-order sign to alpha < 4 gamma/3 and removing EB.3's finite windows at alpha = 0.8

## Discovery ID
DISC-0242

## Status
THEOREM (mathematical sense only; EC.1–EC.3 have written proofs in the repository, conditional on BI.4, AQ (3), AR (1), AT (1)–(3), AZ (1)/(3), EA.4 and DZ.1 as stated; EC.4 is arb-certified at alpha = 0.8 only; EC.5 is floats, OBSERVED). Method KNOWN (substituting a sharper certified ceiling into an existing weight estimate, geometric-tail bounds, exponent comparison, outward-rounded interval arithmetic). Novelty of the specific results and constants UNRESOLVED. Upper bound only: Theta(3^-n) is observed, not proved. Answers DISC-0241's kept limit "remainder exponent 0.65 (not the observed 3^-n)" and the upper half of AT's open "sharp correction exponent" for alpha in (gamma, 1) (dated notes on DISC-0241 and DISC-0113).

## Date Discovered
2026-11-13 (indexed ~11:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit ebaa8c8629b48bec0cccdbeb851ea897785f4e0d (2026-11-13 10:06 AM EST); parent f0c35377564e (Theorem EB, DISC-0241).

## Original Evidence
- GASKET.md §Theorem EC (header line 5873; NOT THIS line 5922), +64/-2 lines; GASKET.md line 1606 (AT's OPEN list) and line 5860 (EB's "What stays open") annotated "now Theorem EC", original wording kept.
- CLAIM_STATUS.md (+3/-1, new row); README.md (+3/-1).
- scripts/gasket_fractional_corner_remainder_sharp.py (new, 242 lines); registered in scripts/cli.py; tests/test_cli.py test_theorem_ec_corner_remainder_sharp (+33); tests/test_flux_identity.py CornerRemainderFloatTests (+20, numpy-only CI test).

## Discovery
Setting as in Theorems AT, AZ, DZ, EA, EB: gamma = log3/log5, rho = 5^alpha/3, X_k = rho^k (delta_N - delta_N^(k)), C_delta = -nu_alpha (1 - delta_N), eps_k AZ's error, R_n EB.1's remainder.
- Diagnosis (the repo's): EB's 0.65 came only from AQ's power ceiling r <= B s^-0.35 inside AT's small-y lemma; BI.4's certified sharp ceiling s^(1-gamma) r_oo <= G = 0.6031 had never been fed back into AT's weight.
- EC.1 (proved, every t in (0,1], alpha in (0,1]): with the ceiling min(zr, G z^gamma), |A_k^alpha B_k C_k - 1| <= K_alpha t^gamma, K_alpha = e^(alpha/20 + K_1/2) - 9/10, K_1 = 0.2^(1-gamma) 16.6/30 + 2c_e/(1 - 0.2^gamma c_e), c_e = 2G 5.2^gamma/6; K_1 <= 1.893324, K_0.8 <= 1.782266 (AT had t^0.65).
- EC.2 (proved, every alpha in (gamma,1), explicit): |eps_k| <= B_alpha (rho/3)^k for k >= 6, B_0.7 <= 3.88e3, B_0.8 <= 1.94e3, B_0.9 <= 1.03e3, B_0.95 <= 7.74e2. Derived: rho^-n eps_n, AT (4a)'s rate, AZ (4)'s, and EB.1's R_n are O(3^-n); X_n - C_delta/(1 + nu rho^-n) = O((rho/3)^n).
- EC.3 (proved): X_n = C_delta sum_(j<J) (-nu rho^-n)^j + o(rho^-(J-1)n) whenever rho^J < 3, i.e. alpha < (J+1) gamma/J. So EB's third term -nu^3 (1 - delta_N) rho^-2n > 0 holds for alpha < 4 gamma/3 = 0.910142 (EB had 0.89927). The repo states this is the end of the route: above 4 gamma/3 a Theta(3^-n) remainder would dominate, so the third term there is neither claimed nor refuted.
- EC.4 (arb, alpha = 0.8, N = 1, 2, 3, 6, 10): |X_k - C_delta/(1 + nu rho^-k)| <= Lam1_N (rho/3)^k + Lam2_N 5^-k (N=1: 13.97, 2.07; N=10: 3.63e3, 4.05e6); X_k > C_delta, X_k decreasing, Y_k > Y_oo, Y_k decreasing for EVERY k >= 60 (EB.3's windows [60, 232..270] and [60, 115..129] removed); -nu Y_oo in [0.016560, 0.016578] (N=1) .. [0.318846, 0.318849] (N=10).
- EC.5 (floats, OBSERVED): w_k = (u_(k+1) - u_(k+2)) - (u_k - u_(k+1))/rho removes the Möbius part; w_(k+1)/w_k -> 1/3 (0.33426 at 0.8, 0.33360 at 0.9, 0.33335 at 0.95), 3^k w_k ~ -5.04, -1.341, -0.558. A nonzero 3^-n remainder is observed, not proved.

## Why It Matters
It closes the gap between the proved (5^-0.65n) and observed (3^-n) remainder in the corner-deficit chain AT → AZ → DZ → EA → EB, as an upper bound, by reusing a certified result (BI.4) the chain had not yet used. It turns EB.3's finite windows into all-k statements at 0.8 and marks honestly where this route stops (4 gamma/3).

## Derivation
Checked here: the repo's rho' = 5^(alpha - gamma)/3 equals rho/3, since 5^gamma = 3 gives 5^(alpha - gamma) = 5^alpha/3 = rho. EC.3's threshold: an error O((rho/3)^n) in X_n is below the j-th term rho^-(J-1)n iff rho^J < 3 iff J (alpha log 5 - log 3) < log 3 iff alpha < (J+1) gamma/J; J = 3 gives 4 gamma/3 = 0.9101416 (mpmath), J = 4 gives 5 gamma/4 = 0.85326. At alpha = 0.95, rho = 1.5378 and rho^3 = 3.64 > 3, so the third term is correctly not claimed there. K_1 and K_0.8 recomputed from the stated formula (G = 0.6031): K_1 = 1.8933237687, K_0.8 = 1.7822657980, so the printed upper bounds 1.893324 and 1.782266 are correct outward roundings.

## Assumptions
BI.4's ceiling G = 0.6031, AQ (3), AR (1), AT (1)–(3)'s proofs, AZ (1)/(3), EA.4's C_delta(0.8, N) widths, DZ.1, all as stated in the repository. python-flint arb and sympy correctness.

## New Results
O(3^-n) remainder for every alpha in (gamma, 1) with explicit B_alpha at five alpha values; third-order sign of X_n extended from alpha < 0.89927 to alpha < 0.910142; every-k monotonicity of X_k and Y_k at alpha = 0.8 for five N; certified -nu Y_oo(0.8, N).

## Prior Art
Error-exponent improvements by inserting a sharper a-priori ceiling into an existing estimate are standard technique; renormalisation and decimation on the Sierpinski gasket (Kigami; Strichartz; Fukushima–Shima; Teplyaev); interval enclosures (Tucker 2011; arb, Johansson). No external source for these constants was searched in this slice.

## Novelty Analysis
Method KNOWN. The constants and the 4 gamma/3 threshold are new to the corpus; external novelty UNRESOLVED and of modest consequence.

## Falsification Attempts
- Independent mpmath (30 digits): gamma, 4 gamma/3, old alpha* = 0.8992728612, K_1, K_0.8 reproduced; rho^2 < 3 at 0.7, 0.8, 0.9, 0.95 and rho^3 < 3 exactly at 0.7, 0.8, 0.9 (fails at 0.95), consistent with EC.3.
- Scope attack: the result is an upper bound only; the commit and GASKET.md say so (no lower bound on the 3^-n coefficient). Every-k claims are certified only at 0.8; B_alpha only at listed alpha values and loose by ~2.6e3 (repo's own kept limit). alpha <= gamma not redone. No overclaim found.
- Display check: commit-message numbers (Lam1/Lam2, -nu Y_oo brackets, defect < 2e-10, ratios 0.33426) match the witness output (Lam1_1 = 1.3968e+01, Lam2_1 = 2.0689e+00, Lam1_10 = 3.6240e+03, Lam2_10 = 4.0409e+06, defect at 60 <= 1.578e-10). No defect found.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem as stated (EC.1–EC.3), conditional on the listed inputs; EC.4 computer-assisted at alpha = 0.8 only; EC.5 observed only.

## Patent Relevance
None. Pure mathematics on a graph; not a mechanism.

## Related Discoveries
DISC-0241 (Theorem EB; kept limit answered), DISC-0113 (Theorem AT; open sharp correction exponent, upper half answered above gamma), DISC-0151 (Theorem BI; ceiling G used), DISC-0127 (Theorem AZ; eps structure), DISC-0240 (Theorem EA; C_delta widths), DISC-0238 (Theorem DZ).

## Open Questions
A lower bound giving Theta(3^-n) and the sign of its coefficient; the third-order sign for alpha in [4 gamma/3, 1) (needs the next non-Möbius term, from eta_k); alpha <= gamma; tighter B_alpha; certified values off 0.8; closed forms.

## Next Experiments
Prove a lower bound on 3^n w_k (observed ~ -5.04 at 0.8); identify the 3^-n coefficient analytically from eta_k; certify EC.4 at alpha = 0.9.

## Reproduction Instructions
Clone informational-flux-identity at ebaa8c8629b48bec0cccdbeb851ea897785f4e0d; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_corner_remainder_sharp.py` (~1 s); tests `python3 -m pytest -q tests/test_cli.py -k test_theorem_ec` and `python3 -m pytest -q tests/test_flux_identity.py`.

## Evidence Log
- 2026-11-13 ~11:00 AM EST: repo default witness EXIT 0 (~1 s), every printed check "ok", no failures; tests/test_cli.py -k test_theorem_ec 1 passed (1.0 s); tests/test_flux_identity.py subset 4 passed (0.4 s).
- 2026-11-13 ~11:00 AM EST: mpmath arithmetic PASS; no display defect found.

## Change History
- 2026-11-13: created.
- 2026-11-13 (dated note): Theorem ED (IFI 417b34c61298, DISC-0243) answers EC's kept limit and open item: eps_n >= L_alpha (rho/3)^n and R_n = Theta(3^-n), so EC.3's 4 gamma/3 boundary is sharp and the third term fails above it. ED also corrects EC's B_0.7 <= 3.88e3 to <= 3.89e3 (true 3.8818e3; the original was a downward rounding). This archive's entry above said "No display defect found" and missed that rounding; the original text is kept. No status change.
