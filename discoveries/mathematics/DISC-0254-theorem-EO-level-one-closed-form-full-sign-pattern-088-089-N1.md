# Discovery: Theorem EO, level 1 of Y_n - Y_oo in closed form, and the full sign pattern for all n >= 1 at alpha = 0.88 and 0.89 (N = 1)

## Discovery ID
DISC-0254

## Status
THEOREM (mathematical sense only; EO.1 is an exact closed-form derivation in the repository (sympy-checked); EO.2 and EO.3 are arb certificates, 128 bits, per the repository's witness). Method KNOWN (partial fractions plus the standard Mellin integral int_0^oo s^-a/(s+c) ds = pi c^-a / sin(pi a), then the same EF.1 interval routines as DISC-0249..0253). Novelty of the constants UNRESOLVED. Closes DISC-0253's kept limit and open item "level 1 at 0.88" (and the same at 0.89, DISC-0252). EO.4 OBSERVED. No status change elsewhere.

## Date Discovered
2026-11-22 (indexed ~7:30 AM EST; the commit is 2026-11-22 6:18 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit a5a95218e714b0487c6237f0789fa174447100fe (2026-11-22 6:18 AM EST; 11:18:25Z); parent 11f044a28cfa786947eb8183b3e8a7a81b98ca16 (MIT LICENSE only, no claim change), whose parent is ceb654d12046 (Theorem EN, DISC-0253).

## Original Evidence
- GASKET.md §Theorem EO (+42/-5), incl. in-place marks on EJ.4's 0.88 and 0.89 window cells and its "levels n < 6 are not decided" sentence, EN.2's n = 1 table cell, EN's kept limit and open item; CLAIM_STATUS.md (+1/-1); README.md (+2/-1).
- scripts/gasket_fractional_corner_level_one.py (new, 259 lines; imports EJ's gasket_fractional_corner_two_sided_rate, EL's gasket_fractional_corner_exact_0905_n3, EM's gasket_fractional_corner_exact_091, EN's gasket_fractional_corner_exact_088), registered in scripts/cli.py (+2/-1); tests/test_cli.py (+14); tests/test_flux_identity.py (+42).

## Discovery
Setting and notation as DISC-0249 (gamma = log3/log5, rho = 5^alpha/3, Y_n the second correction, N the starting level, om = 1 - delta_1, nu < 0 as in DZ.3, D'_n as in ED.1).
- EO.1 (THEOREM, exact; every alpha in (0,1) for the integrals, (gamma,1) for Y): AQ (1) at k = 0 gives r_1 = (s+5)/(s^2+7s+9) (also from the 6x6 Laplacian of G_1 and from EJ's affine recursion, per the repo); BL's recursion with eta_0 = -1/2 gives eta_1(z) = 1/(2(z+5)). With a_(1,2) = (7 -+ sqrt13)/2 (0 < a_1 < 5 < a_2):
  J_1 = pi/(sqrt13 sin(pi a)) [(5-a_1) a_1^-a + (a_2-5) a_2^-a], H_1 = pi/(sqrt13 sin(pi a)) (a_1^-a - a_2^-a)/2, D'_1 = J_1/rho, om_1 = 1 - delta_1^(1) = H_1/J_1, and
  Y_1 - Y_oo = rho^2 (om_1 - om) - om |nu| (rho + |nu|), decreasing in om and |nu|. Only EF.1's certified om and |nu| enter (no eps_n, eta_n, L, U).
- EO.2 (THEOREM, certified; EF.1 point cells 4000/32000 per unit): alpha = 0.88: om in [0.068040179, 0.06804675], |nu| in [0.49916739, 0.4993144], om_1 = 0.0927170037, D'_1 = 3.69222949, Y_1 - Y_oo in [-1.707624e-02, -1.703396e-02] < 0. alpha = 0.89: om in [0.070945361, 0.070951642], |nu| in [0.46638151, 0.46651559], om_1 = 0.0933602177, D'_1 = 3.92620007, Y_1 - Y_oo in [-1.797190e-02, -1.793204e-02] < 0. With EJ.4 / EN.2 (0.88) and EJ.4 / EM.3 (0.89): Y_n - Y_oo changes sign exactly once for all n >= 1, 9 -> 10 at 0.88 and 14 -> 15 at 0.89.
- EO.3 (THEOREM, certified; --full; 1000/8000 per unit): Y_1 - Y_oo in [+6.395764e-02, +6.401045e-02] (0.7), [+3.912902e-03, +4.109311e-03] (0.8), [-1.209066e-02, -1.189998e-02] (0.85), [-1.851724e-02, -1.836861e-02] (0.9), [-1.860545e-02, -1.846262e-02] (0.905), [-1.858951e-02, -1.845272e-02] (0.91). At 0.85 with EJ.4's onset 6: at least one sign change between levels 1 and 6 (number undecided). At 0.9/0.905/0.91 this reproduces EJ.3/EJ.4's level-1 sign by a route independent of EJ.1/EG.1.
- EO.4 (OBSERVED, floats): om_1 closed form = mpmath = trapezoid of EJ's r_1 recursion; direct float Y_n - Y_oo for n = 1..12 at eight exponents; 0.88 negative exactly for n <= 9 (n = 9: -7.12e-06, n = 10: +4.59e-05); 0.85 float sign change 3 -> 4 (not certified).

## Why It Matters
Level 1 was the last undecided level at 0.88 and 0.89 because the tail route (EJ.2 (b), EN.1) is too loose at k0 = 1. G_1 is a six-vertex graph, so level 1 can be computed exactly. With this, the N = 1 sign pattern is fully decided for every n >= 1 at 0.88 and 0.89. At 0.85 there is now a certified sign change, though how many changes there are is still open.

## Derivation
r_1 = (s+5)/((s+a_1)(s+a_2)) = [(5-a_1)/(s+a_1) + (a_2-5)/(s+a_2)]/sqrt13 and r_1 eta_1 = [1/(s+a_1) - 1/(s+a_2)]/(2 sqrt13). Integrating term by term against s^-a with int_0^oo s^-a/(s+c) ds = pi c^-a / sin(pi a) (0 < a < 1, c > 0) gives J_1 and H_1. The Y_1 identity follows from X_1 = rho (om_1 - om), C_delta = -nu om, Y_1 = rho (X_1 - C_delta), Y_oo = nu^2 om (EB) with nu < 0. Monotonicity in om and |nu| means the corner evaluation of the certified boxes bounds Y_1 - Y_oo.

## Assumptions
Everything DISC-0249..0253 list (AQ (1)-(3), BL, DZ.1-3, EB, ED.1, EF.1, EJ.1-EJ.4, EL.1, EM.1/EM.3, EN.1/EN.2). EF.1 cell routines are valid at each exponent (checked by the script). python-flint arb and sympy are correct. The definitions X_1, C_delta and Y_1 are the repository's. This slice did not re-derive them independently; it checked them numerically against direct quadrature (EO.4).

## New Results
Closed-form om_1(alpha) and D'_1(alpha) for every alpha in (0,1). Y_1 < Y_oo at 0.85..0.91 and Y_1 > Y_oo at 0.7, 0.8. Exactly one sign change for all n >= 1 at (0.88, N = 1), 9 -> 10, and at (0.89, N = 1), 14 -> 15.

## Prior Art
The Mellin/Stieltjes integral of a rational function by partial fractions is textbook (e.g. Gradshteyn-Ryzhik 3.222). Prior art for the Poincare-function and gasket-decimation setting and for arb is as in DISC-0244..0253. No external search was done in this slice.

## Novelty Analysis
Method KNOWN. The level-1 constants and the completed sign patterns are new to the corpus. External novelty UNRESOLVED and modest.

## Falsification Attempts
- Repo witness here (informational-flux-identity @ a5a95218e714 in a fresh clone; python3, python-flint 0.9.0, numpy 2.5.5; niced, shared box): `python3 scripts/gasket_fractional_corner_level_one.py` EXIT 0, 101.3 s in-script (repo says 131.3 s), "all EO checks passed". `--full` EXIT 0, 170 s wall (repo says 206.0 s). Every EO.2 and EO.3 interval in the commit message was reproduced to the printed digits, including the 0.88 brackets matching EN.2 and the break attempts: EN.1 at k0 = n = 1 gives D'_1 in [3.573152, 6.742495], which contains the exact 3.69222949; EJ.2 (b) at n = 1 goes from +0.005057 to +8.635e-05 with the exact D'_1, still undecided.
- pytest: `pytest -q tests/test_flux_identity.py` 15 passed, 2 deselected (by the -k filter); tests/test_cli.py passed.
- Independent quadrature (this slice, not in the repo): mpmath at 30-40 digits with s = e^u on [-400, 400] (81 panels). J_1 and H_1 by direct integration of s^-a r_1 and s^-a r_1 eta_1 agree with the closed forms to 6.6e-21 (0.88), 3.9e-19 (0.89) and 1.4e-15 (0.91). om_1 = 0.0927170037125, 0.0933602176778, 0.0946262541098. D'_1 = J_1/(5^a/3) = 3.692229491, 3.926200071, 4.564116043, matching the repo. (A naive mpmath quad on [0, inf) without the substitution loses up to 6e-4 at 0.91. That is a quadrature artifact, not a defect in the repo; at 0.7 it agrees to 1e-13.)
- Corner check (this slice): evaluating rho^2 (om_1 - om) - om |nu| (rho + |nu|) at the four corners of EN.2's (om, |nu|) box at 0.88, with rho = 5^0.88/3, gives -0.0170340 .. -0.0170762. That is EO.2's interval [-1.707624e-02, -1.703396e-02]. The inferred rho = J_1/D'_1 = 1.3739545 equals 5^0.88/3.
- Margins: |Y_1 - Y_oo| >= 1.70e-2 at 0.88/0.89 against ball widths <= 4.3e-5. The smallest EO.3 margin is 3.91e-3 at 0.8. KEPT FAILURE: none.

## Experimental Validation
None applicable (pure mathematics). Functions on a graph, not a flux; not thrust; Stage 2 still blocked.

## Mathematical Status
EO.1 is an exact derivation. EO.2 and EO.3 are computer-assisted theorems at points, conditional on DISC-0249..0253's inputs. EO.4 is observed.

## Patent Relevance
None.

## Related Discoveries
DISC-0253 (EN; level 1 at 0.88 closed), DISC-0252 (EM; 0.89 pattern completed), DISC-0249 (EJ; EJ.4 level-1 cells), DISC-0247/0248 (ED.1 denominators).

## Open Questions
Levels 2..5 and the number of sign changes at 0.85 (float suggests a single change 3 -> 4). alpha-cells instead of points. N >= 2 at 0.88/0.89. A closed form for n >= 2 (G_2 is still finite, so this may be feasible).

## Next Experiments
Exact level 2 by the same route (G_2 resolvent, a degree-higher rational r_2) to start deciding 0.85. Certify levels 2..5 at 0.85.

## Reproduction Instructions
Clone informational-flux-identity at a5a95218e714. Run pip install python-flint sympy numpy. Then run python3 scripts/gasket_fractional_corner_level_one.py (~2 min) and --full (~3-4 min). Tests: pytest -q tests/test_flux_identity.py.

## Evidence Log
- 2026-11-22 ~7:05-7:25 AM EST: default witness EXIT 0 (101.3 s); --full EXIT 0 (170 s); pytest passed; independent mpmath closed-form and corner checks above.

## Change History
- 2026-11-22: created.

- 2026-11-22 ~8:20 AM EST note (appended; the history above is unchanged): DISC-0255 (Theorem EP, informational-flux-identity 1a5d6a76e74d) closes the open item 'levels 2..5 and the number of sign changes at 0.85' (and the 0.7/0.8 levels 2..5). Exact residue sums for n = 1..6 give exactly one sign change at (0.85, N = 1), 3 -> 4, and no sign change at 0.7 or 0.8. The 'closed form for n >= 2' item is also addressed for n <= 6. EP.1's level-1 residue sum equals EO.1's closed form (om_1 = 0.0907457636 at 0.85, confirmed independently here to 2.6e-11).
