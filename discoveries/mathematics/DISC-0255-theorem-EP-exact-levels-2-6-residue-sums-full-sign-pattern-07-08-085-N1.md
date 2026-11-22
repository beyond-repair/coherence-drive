# Discovery: Theorem EP, levels 2..6 of Y_n - Y_oo as exact residue sums, and the full sign pattern at alpha = 0.85, 0.8, 0.7 (N = 1)

## Discovery ID
DISC-0255

## Status
THEOREM (mathematical sense only). EP.1 is an exact computation in Z[s] (python-flint fmpz_poly) with certified root isolation, for n <= 6 only. EP.2 and EP.3 are arb certificates (128 bits; residue sums at 512 bits), per the repository's witness. Method KNOWN: partial fractions/residues, the Mellin integral int_0^oo s^-a/(s+w) ds = pi w^-a / sin(pi a), interval arithmetic, and the EF.1/EL.1/EJ.2 routines of DISC-0249..0254. Novelty of the constants UNRESOLVED. This closes DISC-0254's open item "levels 2..5 and the number of sign changes at 0.85" and DISC-0249's (EJ.4) "levels n < 6 not decided" at 0.7/0.8/0.85. EP.4 OBSERVED. No other status change.

## Date Discovered
2026-11-22 (indexed ~8:20 AM EST; the commit is 2026-11-22 7:31 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 1a5d6a76e74d61b31f5d3f4d9639debada1bf4d5 (2026-11-22 7:31:21 AM EST; 12:31:21Z). Parent: a5a95218e714 (Theorem EO, DISC-0254).

## Original Evidence
- GASKET.md §Theorem EP (+57/-9), including in-place marks on EJ.4's 0.7/0.8/0.85 table cells and its "levels n < 6 are not decided" sentence, EJ's kept limit, EO.3/EO.4's 0.85 sentences, and EO's kept limit and open item. Also CLAIM_STATUS.md (+1/-1) and README.md (+1/-1).
- scripts/gasket_fractional_corner_exact_levels.py (new, 324 lines; imports the EJ, EL, EM, EN and EO scripts), registered in scripts/cli.py (+1). Also tests/test_cli.py (+15; test_theorem_ep_corner_exact_levels wraps main()) and tests/test_flux_identity.py (+35; numpy-only test_theorem_ep_exact_levels_floats).

## Discovery
Setting and notation are as in DISC-0249/0254: gamma = log3/log5, rho = 5^alpha/3, om = 1 - delta_1, nu < 0, and D'_n as in ED.1.
- EP.1 (THEOREM, exact; n = 1..6): running AQ (1) exactly in Z[s] gives r_n = B_n/A_n (gcd-reduced) with deg A_n = 2^n and deg B_n = 2^n - 1. A_n has 2^n simple roots, all real and < 0 (certified isolation; gcd(A_n, A_n') = 1), and the residues c_j = B_n(z_j)/A_n'(z_j) are > 0. The reduced denominator of r_n eta_1(p^(n-1)(s)) = B_n/(2 A_n (p^(n-1)(s)+5)) also has simple real negative roots. This gives J_n = pi/sin(pi a) sum_j c_j (-z_j)^-a and H_n likewise, with om_n = H_n/J_n, D'_n = J_n/rho^n and Y_n - Y_oo = rho^(2n) (om_n - om) - om |nu| (rho^n + |nu|), which is decreasing in om and |nu|. n = 1 is EO.1.
- EP.2 (THEOREM, certified; EF.1 point cells 4000/32000 per unit; EL.1 upper at k0 = 5, 1600 cells/unit): at alpha = 0.85, |nu| is in [0.59110183, 0.59128836] and 1-delta_1 is in [0.059038919, 0.059046046]. Exact om_n = 0.0907457636, 0.0844691702, 0.0783754360, 0.0733690985, 0.0695975186, 0.0668440463 (n = 1..6). Y_n - Y_oo is in [-1.201914e-02,-1.197148e-02], [-5.798026e-03,-5.735473e-03], [-1.658777e-03,-1.573205e-03], [+4.025341e-04,+5.242939e-04], [+1.157117e-03,+1.336626e-03] and [+1.267014e-03,+1.539905e-03]. EJ.2 (a) at k0 = 5 gives Phi_1(5) >= +6.853e-03, so Y_n > Y_oo for every n >= 5. Result: Y_n - Y_oo changes sign exactly once for all n >= 1, between levels 3 and 4.
- EP.3 (THEOREM, certified; 1000/8000; EL.1 k0 in {5,6}): at 0.7 and 0.8, Y_n - Y_oo > 0 for n = 1..5 and the onset is 5. So Y_n > Y_oo for every n >= 1, with no sign change. Lower bounds for n = 1..5: +6.3958e-02, +5.5127e-02, +4.6083e-02, +3.8372e-02, +3.2325e-02 (0.7) and +3.9129e-03, +8.2107e-03, +9.4927e-03, +8.8841e-03, +7.5618e-03 (0.8).
- EP.4 (OBSERVED / break attempts): the lattice-coordinate Laplacian of G_n (n = 1..3) reproduces B_n/A_n. Exact D'_n lies inside EN.1's certified brackets for n = 1..5. The trapezoid om_n matches to 1e-8. The tail route leaves n = 2, 3, 4 undecided at 0.85, which is a limitation of a one-sided criterion, not a failure.

## Why It Matters
At 0.7-0.85, levels 1..5 had been the gap between EO's exact level 1 and EJ.4's tail onset 6. Each G_n is a finite graph, so r_n is rational, and the partial-fraction route of EO extends to every finite level. With this, the N = 1 sign pattern is now fully decided at all eight exponents studied: 0.7 and 0.8 have no change; 0.85 changes at 3 -> 4, 0.88 at 9 -> 10, 0.89 at 14 -> 15, 0.9/0.905 at the levels in DISC-0247..0251, and 0.91 at 2585 -> 2586.

## Derivation
This is EO.1's derivation applied level by level. r_n has simple real negative poles with positive residues, so partial fractions plus the Mellin integral give J_n and H_n as finite sums. The Y_n identity comes from EB (sympy-checked in the script). Because Y_n - Y_oo is monotone in om and |nu|, evaluating it at the corners of EF.1's certified box bounds it.

## Assumptions
Everything listed in DISC-0249..0254: AQ (1)-(3), BL (including eta_1(z) = 1/(2(z+5)) and the H_n integrand r_n eta_1(p^(n-1)(s))), DZ.3, EB, EF.1, EJ.2 (a), EL.1 and EN.1. The pole structure is certified for n <= 6 only; it is not proved for all n. python-flint arb/fmpz_poly and sympy are assumed correct. This slice did not re-derive the H_n integrand; it used the repository's definition.

## New Results
Exact om_n and D'_n for n = 1..6 at every alpha in (0,1). Exactly one sign change for all n >= 1 at (0.85, N = 1), 3 -> 4. No sign change at (0.7, N = 1) or (0.8, N = 1).

## Prior Art
The resolvent of a finite graph Laplacian is a Stieltjes function, i.e. a sum of w_k/(lambda_k + s) with w_k >= 0. That explains the real negative poles and positive residues; it is standard spectral theory. The spectral decimation map p(s) = s(s+5) for the Sierpinski gasket is classical (Rammal-Toulouse, Fukushima-Shima). Partial fractions plus the Mellin integral are textbook (e.g. Gradshteyn-Ryzhik 3.222), and arb is used as in DISC-0249..0254. No external search was done in this slice.

## Novelty Analysis
Method KNOWN. The level-n constants and the completed sign patterns are new to the corpus. External novelty UNRESOLVED and modest.

## Falsification Attempts
- Repo witness here (informational-flux-identity @ 1a5d6a76e74d, fresh clone /workspace/ifi-ep-audit; python3, python-flint 0.9.0, numpy 2.5.5, sympy 1.14.0; niced, shared box). `python3 scripts/gasket_fractional_corner_exact_levels.py` returned EXIT 0 in 283.9 s in-script (284 s wall; the repo says 213.6 s) and printed "all EP checks passed". Every EP.1 degree/root/residue check passed for n = 1..6. Every EP.2 om_n, D'_n and Y_n - Y_oo interval, Phi(5) >= 0.006853, U(5) <= 0.791572 and kappa_hi <= 0.107859 was reproduced to the printed digits, as were the EP.3 lower bounds and onset 5 at 0.7 and 0.8, and the EN.1 brackets for n = 1..5. The script has no --full mode.
- pytest: `pytest -q tests/test_flux_identity.py` gave 18 passed in 1.95 s, matching the repo's "18 tests" (the -k theorem_e subset gave 15 passed, 3 deselected). test_cli.py::test_theorem_ep_corner_exact_levels only wraps main(), which the default run above covers. The whole test_cli.py suite was not completed: it re-runs every repo script and was stopped after 10 min.
- Independent check (this slice; /workspace/ep_indep.py, own code, not the repo's scripts). G_n was built by recursive three-copy gluing of half-scaled copies with exact rational coordinates, a different construction from the repo's lattice subdivision. |V| = 6, 15, 42, 123, 366, 1095 = (3^(n+1)+3)/2 for n = 1..6. I used the eigen-expansion r_n(s) = 1/2 sum_k (v.phi_k)^2/(lambda_k + s), with v = e_corner0 - e_corner1 (numpy eigh). This agrees with the AQ (1) recursion to <= 4.7e-15 at s = 0.1, 1, 7.3, 50. There are exactly 2^n distinct poles for n = 1..6, with smallest |pole| 1.697, 0.570, 0.135, 0.0283, 0.00574, 0.00115 and smallest weight 9.9e-6 > 0. The Stieltjes form makes positive residues and negative real poles automatic. J_n = pi/sin(pi a) sum w_k lambda_k^-a matches mpmath quadrature (s = e^u) to <= 4.5e-12. H_n was computed by mpmath quadrature of the repo's integrand r_n/(2(p^(n-1)(s)+5)). At 0.85 the resulting om_n = 0.090745763626, 0.084469170169, 0.078375436008, 0.073369098473, 0.069597518611, 0.066844046317 agree with the repo's om_n to <= 3.1e-11 for all n = 1..6. D'_n = 3.19587007, 3.6470823, 4.03995171, 4.36088243, 4.61370218, 4.80944508 match as well.
- Sign check (this slice): with the repo's certified EF.1 box at 0.85 and the independent om_n, the four-corner evaluation of rho^(2n) (om_n - om) - om |nu| (rho^n + |nu|) gives [-0.01201914, -0.01197148], [-0.005798023, -0.005735475], [-0.001658773, -0.001573206], [+0.0004025401, +0.000524293], [+0.001157127, +0.001336626] and [+0.001267029, +0.001539906] for n = 1..6. These are EP.2's balls to within about 1e-8, and the signs are (-,-,-,+,+,+).
- Partial: the H_n denominator's root/residue structure was not checked independently (H_n was computed by quadrature only). The EF.1 box, EL.1 U(5), EJ.2 (a) onset and the EP.3 0.7/0.8 values were reproduced only through the repo's witness, not by independent code.
- Margins: the thinnest is n = 4 at 0.85, where the ball [+4.03e-4, +5.24e-4] has width 1.22e-4 and lies 4.0e-4 from 0. At 0.8 the smallest margin is 3.91e-3 (n = 1). KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). These are functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
EP.1 is exact for n <= 6. EP.2 and EP.3 are computer-assisted theorems at points, conditional on the inputs of DISC-0249..0254. EP.4 is observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0254 (EO; open item 'levels 2..5 at 0.7-0.85' closed), DISC-0249 (EJ; EJ.4 cells at 0.7/0.8/0.85), DISC-0253 (EN.1 brackets used as a break test), DISC-0251 (EL.1 upper bound at k0 = 5).

## Open Questions
The pole structure (simple, real, negative, positive residues) for all n; the Stieltjes argument suggests it holds, but distinct poles and the degree 2^n are not proved in general. The H_n denominator structure for n >= 7. Residue sums cannot decide thin levels (0.88, n = 9: rho^18 times the om-width ~2e-3 against a gap of 7.1e-6). Alpha-cells instead of points. N >= 2. (gamma, 1) only.

## Next Experiments
Prove the degree and simplicity of the poles for all n from spectral decimation (eigenvalue multiplicities of G_n). Certify on alpha-cells over [0.7, 0.91].

## Reproduction Instructions
Clone informational-flux-identity at 1a5d6a76e74d and run pip install python-flint sympy numpy mpmath. Then run python3 scripts/gasket_fractional_corner_exact_levels.py (~4-5 min on a loaded box). Tests: pytest -q tests/test_flux_identity.py.

## Evidence Log
- 2026-11-22 ~7:55-8:20 AM EST: default witness EXIT 0 (283.9 s); pytest tests/test_flux_identity.py 18 passed; independent gasket-gluing eigen-expansion with mpmath om_n/sign checks above (146.8 s).

## Change History
- 2026-11-22: created.
