# Discovery: Theorem ET, the refinement limit of H_n(0) = int_0^oo h_n

## Discovery ID
DISC-0259

## Status
ET.1–ET.3: THEOREM (mathematical sense only), conditional on BG.3, BI.4 and BJ.6 as stated in the repository (pointwise limits R_n -> R and psi_k -> psi; the ceiling/floor 1/(3+t) <= R_n <= min(1/3, G t^(gamma-1)), G = 0.6031; t <= psi(t) <= t e^(t/10)). ET.5 (K = ln(5)/2): CONJECTURE, OBSERVED only. It survived an independent numerical attack in this slice (see Falsification Attempts). The method is KNOWN: exact change of variables, dominated convergence with a supplied dominator, and certified quadrature bounds. Whether the constant K, or its conjectured closed form ln5/2, appears in the literature is UNRESOLVED; no external search was done. This closes DISC-0258's kept limit "H_n(0) for n <= 8 only, no statement as n -> oo". No other status change.

## Date Discovered
2026-11-22. The commit is from 6:44 PM EST; it was indexed about 7:05 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 87936a0d4338f27ac7cd67b99b5d549f1349a4a9 (2026-11-22 6:44:42 PM EST; 23:44:42Z). Parent: 361b25c217af (Theorem ES, DISC-0258).

## Original Evidence
- GASKET.md §Theorem ET (+34/-2, including in-place marks on ES's kept limit and open item). README.md (+1/-1), CLAIM_STATUS.md (+3/-2; CI now 22 tests).
- scripts/gasket_fractional_corner_h_zero_limit.py (new, 190 lines; imports gasket_fractional_corner_pole_structure for EQ.1's A_n, B_n), registered in scripts/cli.py (+1). tests/test_cli.py (+14) and tests/test_flux_identity.py (+21).

## Discovery
- Setting (from EQ, ER, ES and BG.3). p(s) = s(s+5), q_k = p^k + 5, r_n = B_n/A_n, h_n = Q_n/(2A_n) = r_n/(2 q_(n-1)), H_n(alpha) = int_0^oo s^-alpha h_n ds, H_n(0) = int_0^oo h_n (ES.2). R_n(t) = (3/5)^n r_n(5^-n t), psi_k(t) = p^k(5^-k t).
- ET.1 (THEOREM, exact, every n >= 1). s = 5^-n t gives 3^n H_n(0) = int_0^oo R_n(t) / (2(5 + psi_(n-1)(t/5))) dt.
- ET.2 (THEOREM). 3^n H_n(0) -> K := W(0)/2 = int_0^oo R(t)/(2(5 + psi(t/5))) dt > 0. BG.3's own dominator t^-alpha (1/3)/(4 + t/5) is not integrable at alpha = 0 (log divergence); BI.4's ceiling gives the integrable dominator min(1/3, G t^(gamma-1)) · 5/(2(25+t)) = O(t^(gamma-2)). Hence H_(n+1)(0)/H_n(0) -> 1/3.
- ET.3 (THEOREM, arb-certified). 0.190286685866 <= 3^n H_n(0) <= 1.934636803264 for every n >= 1, and the same bracket holds for K. The floor uses BI.4's R_n >= 1/(3+t) and BJ.6's psi <= t e^(t/10) (with psi_(n-1) <= psi because p(y) >= 5y on y >= 0); the ceiling is a closed-form integral of BI.4's ceiling.
- ET.4 (repository checks). Exact rationals n <= 6 for the recursion, h_n = Q_n/(2A_n) and the scaling identity; mpmath quadrature reproduces ES.4's H_n(0), n = 1..8, to 1e-9; bracket checked n = 1..24; BI.4/BJ.6 bounds on a grid n <= 20, no violation. KEPT FAILURE: none.
- ET.5 (CONJECTURE, OBSERVED). K = ln(5)/2 = 0.80471895621705...; 3^n H_n(0) = K - c 3^-n + ..., c ≈ 2.67182; Richardson (3 v_31 - v_30)/2 = ln5/2 to 2.6e-22 (repository's separate probe).

## Why It Matters
ES (DISC-0258) gave H_n(0) for n <= 8 only. ET makes the alpha = 0 extension asymptotically exact: H_n(0) = (K + o(1)) 3^-n, with a uniform certified bracket for K. It is the first limit statement in the H_n residue route. alpha = 0 is outside the (gamma, 1) window where Y_n lives, so it decides no sign of Y_n - Y_oo and no thin level (0.88, n = 9 unchanged).

## Derivation
Reviewer check of the proof (not new mathematics):
1. ET.1. With s = 5^-n t, ds = 5^-n dt and p^(n-1)(5^-n t) = psi_(n-1)(t/5) by the definition psi_k(t) = p^k(5^-k t) at k = n-1, argument t/5. Then 3^n h_n(5^-n t) 5^-n = (3/5)^n r_n(5^-n t) / (2(5 + psi_(n-1)(t/5))) = R_n(t)/(2(5 + psi_(n-1)(t/5))). Exact.
2. ET.2. Pointwise convergence of the integrand follows from BG.3. Domination: R_n <= min(1/3, G t^(gamma-1)) (BI.4) and psi_(n-1)(t/5) >= t/5 (because p(y) >= 5y for y >= 0), so the integrand is <= min(1/3, G t^(gamma-1)) · 5/(2(25 + t)), which is bounded near 0 and O(t^(gamma-2)) at infinity with gamma - 2 < -1. Dominated convergence gives the limit. K > 0 follows from the floor in ET.3.
3. ET.3. Same two bounds, integrated: the upper one in closed form (split at t0 = (3G)^(1/(1-gamma)), where the two pieces of the min meet), the lower one over [0, 4000] with arb.
No gap was found, given BG.3, BI.4 and BJ.6 as stated. This slice did not re-derive those three imported results.

## Assumptions
- BG.3 (pointwise R_n -> R, psi_k -> psi), BI.4 (ceiling with G = 0.6031 and floor 1/(3+t), n >= 1), BJ.6 (psi bracket), as proved in the repository; not re-derived here.
- EQ.1 / ES.2 (h_n = r_n/(2 q_(n-1)), H_n(0) = int_0^oo h_n), DISC-0256 and DISC-0258.
- python-flint arb integration is correct (repository ET.3 only).

## New Results
For every n >= 1: 0.19029 <= 3^n H_n(0) <= 1.93464; 3^n H_n(0) converges to K in that bracket; H_(n+1)(0)/H_n(0) -> 1/3. Conjectured: K = ln5/2, with first correction -c 3^-n, c ≈ 2.6718, and (from this slice's numerics) a next correction of order 5^-n.

## Prior Art
Change of variables plus dominated convergence is textbook analysis. Spectral decimation on the Sierpinski gasket (Rammal–Toulouse, Fukushima–Shima, Teplyaev) and renormalized resolvent limits of the R_n type (Kigami-style resolvent/heat-kernel scaling) supply the setting. A log 5 factor is natural under a time-scaling ratio of 5 (the gasket's Laplacian renormalization factor); a Frullani-type identity int_0^oo (f(t) - f(5t)) dt/t = (f(0) - f(oo)) ln 5 would produce exactly ln5 times a boundary value. That is a HUNCH about where ln5/2 could come from, not a derivation. No external search was done for K.

## Novelty Analysis
The method is KNOWN. The constant K and its conjectured value ln5/2 are specific to the repository's construction; novelty UNRESOLVED.

## Falsification Attempts
- Independent quadrature (this slice; /workspace/corpus-discovery/et_check.py, mpmath at 40 digits, no repository code imported). It re-implements the Moebius decimation step r_(k+1)(s) = (s+2)(s+5)x/((s+6) - 2s(s+5)x) from r_0 = 1/(3+s), sets h_n = r_n/(2(p^(n-1)+5)), and integrates ET.1's rescaled integrand with breakpoints 5^(k/2), k = -8..25. Results:
  - n = 1: quadrature 0.4739509077956933791634... equals the closed form (3/(2 sqrt13)) ln((7+sqrt13)/(7-sqrt13)) from h_1 = 1/(2(s^2+7s+9)) to all 40 digits. H_1(0) = 0.15798363593, matching ES.4.
  - 3^n H_n(0) for n = 2..22: 0.61658154104, 0.72021182327, 0.77281767375, 0.79367710443, 0.80101382766, 0.80348591513, 0.80430909705, 0.80458264834, 0.80467359136, 0.80470384977, 0.80471392387, 0.80471727941, 0.80471839741, 0.80471876997, 0.80471889414, 0.80471893553, 0.80471894932, 0.80471895392, 0.80471895545, 0.80471895596, 0.80471895613190843. All lie inside the ET.3 bracket [0.19029, 1.93464]; n = 2..8 divided by 3^n match ES.4's H_n(0) to the 10 digits printed.
  - Richardson (3 v_n - v_(n-1))/2 - ln5/2 = -0.117, -0.0327, -0.0056, -6.1e-4, -3.7e-5, then +3.0e-6, 1.7e-6, 4.7e-7, 1.07e-7, 2.3e-8, 4.7e-9, 9.6e-10, 1.9e-10, 3.9e-11, 7.8e-12, 1.6e-12, 3.1e-13, 6.3e-14, 1.25e-14, 2.5e-15, 5.0e-16 (n = 2..22). From n ≈ 9 on the residual shrinks by a steady factor 5 per level, which is what a next correction of order 5^-n predicts, with no plateau away from ln5/2. A second Richardson step for that 5^-n term, (5 R_22 - R_21)/4, agrees with ln5/2 to well under 1e-16. The estimate (K - v_n) 3^n with K = ln5/2 tends to 2.67184 (n = 22), consistent with the repository's c ≈ 2.67182.
  - Verdict: ET.5 survives this attempt to break it. It is still a CONJECTURE: no proof, and numerics cannot certify a transcendental closed form.
- Proof attack on ET.2: the claim that BG.3's dominator fails at alpha = 0 is right (t^0 · (1/3)/(4 + t/5) ~ 5/(3t), log-divergent); the replacement O(t^(gamma-2)) with gamma ≈ 0.6826 is integrable. psi_(n-1)(t/5) >= t/5 uses p(y) >= 5y on y >= 0. Held.
- Not done here: the full witness (repository 1374.6 s) and the CI tests were not rerun; BG.3, BI.4, BJ.6 were not re-derived.
- Document consistency: the commit message, the script docstring and the kept limits agree (limit and bracket only; no rate; K = ln5/2 conjectured; nothing on S_n^- or C_n^-; alpha = 0 outside the Y_n window; N = 1 only). No contradiction found.

## Experimental Validation
None applicable (pure mathematics on a finite-graph sequence). Computer checks as above.

## Mathematical Status
ET.1 exact identity; ET.2, ET.3 theorems conditional on BG.3, BI.4, BJ.6; ET.5 conjecture (strong numerical support, independently reproduced).

## Patent Relevance
None. A limit of integrals of rational functions on the combinatorial gasket. Not a flux, not thrust.

## Related Discoveries
- DISC-0258 (Theorem ES): H_n(0) = -sum h_j ln w_j for n <= 8; its kept limit "no statement as n -> oo" is closed here.
- DISC-0256 (Theorem EQ): h_n = Q_n/(2A_n), A_n(0) = 3^(n+1).
- DISC-0254 (Theorem EO): h_1 = 1/(2(s^2+7s+9)), the n = 1 closed form.

## Open Questions
- Prove K = ln5/2 (suggested route, unverified: a Frullani-type telescoping from the 5-scaling self-similarity of R and psi).
- A rate: is 3^n H_n(0) - K = -c 3^-n + O(5^-n) provable, and is c a closed form?
- Whether the same scaling route gives a limit for H_n(alpha) inside (gamma, 1), or for S_n^-, C_n^- (ES's open items).
- N = 2, 3; Stage 2 is still BLOCKED (no Psi_info).

## Next Experiments
- Fit c to high precision (n up to 40 at 60 digits) and test candidate closed forms; check whether the 5^-n correction coefficient is also simple.
- Try to evaluate W(0) = int_0^oo R(t)/(5 + psi(t/5)) dt directly from the functional equations of R and psi.

## Reproduction Instructions
1. Clone informational-flux-identity and check out 87936a0d4338.
2. Run pip install python-flint mpmath.
3. Run python3 scripts/gasket_fractional_corner_h_zero_limit.py (repository: 1374.6 s on a loaded box). Exit 0 means every check passed.
4. Independent check: the 30-line mpmath script described above (Moebius recursion, rescaled quadrature, Richardson), about 1–2 minutes.

## Evidence Log
- 2026-11-22: commit 87936a0d4338 read (commit message, new script with docstring). Independent quadrature n = 1..22 and Richardson extrapolation run here; full witness and CI tests not rerun.

## Change History
- 2026-11-22: created.
