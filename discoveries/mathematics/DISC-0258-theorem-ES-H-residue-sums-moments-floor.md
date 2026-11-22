# Discovery: Theorem ES, the sum, the low moments and a magnitude floor for H_n's residues at every level n

## Discovery ID
DISC-0258

## Status
THEOREM (mathematical sense only). ES.1–ES.3 are pen-and-paper proofs for every n >= 1, given in GASKET.md §Theorem ES and in the script docstring. They use EQ.1 and EQ.2 (DISC-0256), ER.1 (DISC-0257) and, through them, AQ (1) as stated in the repository. ES.4 holds the repository's checks: exact for n <= 10, arb-certified for n <= 8, mpmath quadrature for n <= 4. The method is KNOWN: the Laurent expansion at infinity of a proper rational function (residue power sums vanish below the degree gap), a Mellin-type continuation of a finite exponential sum, and the elementary bound min p = -25/4. Whether these explicit constants are new is UNRESOLVED; no external literature search was done. This closes DISC-0257's kept limit "signs and counts only: no magnitude, no sum". ES.3 is a floor only. It gives no upper bound, limit or rate for S_n^-, and no new sign of Y_n - Y_oo. No other status change.

## Date Discovered
2026-11-22. The commit is from 4:57 PM EST; it was indexed about 5:50 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 361b25c217afdc360bf0ec2ff76129ab0cf72322 (2026-11-22 4:57:50 PM EST; 21:57:50Z). Parent: c02dafc238e5 (Theorem ER, DISC-0257).

## Original Evidence
- GASKET.md §Theorem ES (+31/-2, including in-place marks on ER's kept limit and open items). Also README.md (+1/-1) and CLAIM_STATUS.md (+3/-2; new ES row, ER row marked).
- scripts/gasket_fractional_corner_h_residue_sums.py (new, 189 lines; imports EQ's and ER's scripts unchanged), registered in scripts/cli.py (+2/-1). Also tests/test_cli.py (+14, runs the full witness) and tests/test_flux_identity.py (+35, pure-Python/numpy CI test).

## Discovery
- Setting (from EQ, ER). p(s) = s(s+5), q_k = p^k + 5, r_n = B_n/A_n. A_n is monic of degree 2^n with simple real roots z_j < 0, w_j = -z_j, and residues c_j > 0 with sum c_j = 1. H_n's reduced integrand is h_n = Q_n/(2 A_n) with Q_n = prod_(k<=n-2) q_k (monic, degree 2^(n-1) - 1, Q_n(0) = 5^(n-1)). Its residues are h_j = c_j/(2 q_(n-1)(z_j)), and H_n = pi/sin(pi alpha) * sum_j h_j w_j^(-alpha) on (0,1). S_n^∓ = sum over h_j < 0 (resp. > 0) of |h_j|; C_n^- = sum of c_j over the negative-residue poles.
- ES.1 (THEOREM, every n >= 1). deg(2A_n) - deg Q_n = 2^(n-1) + 1. Hence sum_j h_j z_j^m = 0 for m = 0..2^(n-1) - 1, the sum equals 1/2 at m = 2^(n-1), and sum_j h_j/w_j = h_n(0) = 5^(n-1)/(2·3^(n+1)). In particular sum_j h_j = 0 and S_n^- = S_n^+.
- ES.2 (THEOREM). F_n(alpha) = sum_j h_j w_j^(-alpha) is entire, with zeros at alpha = 0, -1, ..., -(2^(n-1) - 1), and F_n(1) = h_n(0). H_n extends continuously to alpha = 0 with H_n(0) = int_0^oo h_n = F_n'(0) = -sum_j h_j ln w_j.
- ES.3 (THEOREM). For n >= 2, S_n^- >= (2/5) C_n^-, because q_(n-1) >= -5/4 on {p^(n-1) < -5}. For n = 1, S_1^- = S_1^+ = 1/(2 sqrt 13).
- ES.4 (repository checks). Exact Laurent coefficients n = 1..10. arb n = 1..8 (1024 bits for n <= 7, 2048 bits for n = 8). A first all-1024-bit run failed only the 1e-100 radius threshold at n = 8; it is kept and documented as a precision issue, not a counterexample. mpmath quadrature n = 1..4. KEPT FAILURE: none.

## Why It Matters
ER (DISC-0257) fixed the signs of H_n's residues but said nothing about their size. ES shows that the negative part exactly balances the positive part at every level, pins the first 2^(n-1) moments, and bounds the negative mass below by (2/5) of the r_n-mass on those poles. These are the first magnitude statements in the residue route for om_n = H_n/J_n. On their own they decide no thin level (0.88, n = 9 is unchanged) and no sign of Y_n - Y_oo.

## Derivation
This slice re-checked the proof step by step (reviewer check, not new mathematics):
1. Degrees. deg Q_n = sum_(k<=n-2) 2^k = 2^(n-1) - 1 and deg A_n = 2^n (EQ.1), so the gap is 2^(n-1) + 1 >= 2. Both are monic, so h_n = (1/2) s^-(2^(n-1)+1) (1 + O(1/s)).
2. Power sums. The poles are simple (EQ.2), so h_n = sum_j h_j/(s - z_j) = sum_(k>=1) (sum_j h_j z_j^(k-1)) s^-k for |s| > max|z_j|. Comparing coefficients gives ES.1's power sums. h_n(0) = Q_n(0)/(2A_n(0)) = 5^(n-1)/(2·3^(n+1)) uses A_n(0) = 3^(n+1) (EQ.1) and q_k(0) = 5.
3. ES.2. F_n is a finite sum of exponentials in alpha, so it is entire, and F_n(-m) = (-1)^m sum h_j z_j^m = 0. On s > 0, Q_n > 0 and A_n > 0 (all roots negative; p^k(s) > 0 there), so h_n >= 0 is bounded near 0 and O(s^-2) at infinity. Dominated convergence gives H_n(alpha) -> int h_n as alpha -> 0+, and l'Hôpital with F_n(0) = 0 gives pi F_n(alpha)/sin(pi alpha) -> F_n'(0).
4. ES.3. For n >= 2, p^(n-1) = p(p^(n-2)) >= min p = p(-5/2) = -25/4, so q_(n-1) >= -5/4 everywhere on the real line, in particular on {q_(n-1) < 0}. Then |h_j| = c_j/(2|q_(n-1)(z_j)|) >= (2/5) c_j. Summing over the negative-residue poles (ER.1) gives the floor. For n = 1, h_1 = 1/(2(s^2+7s+9)), whose residues are ±1/(2 sqrt 13).
No gap was found. The bound in step 4 does not even need the interval structure; it holds wherever q_(n-1) < 0.

## Assumptions
- EQ.1, EQ.2 (DISC-0256) and ER.1 (DISC-0257) as proved in the repository. Through them, AQ (1) and AQ's setting r_n = 1/2 v^T (L_n + s)^-1 v with v = e_a - e_b.
- H_n's reduced integrand is Q_n/(2 A_n) as stated in EQ.2 (not re-derived here from earlier theorems).
- Repository ES.4 (b) only: arb root isolation in python-flint is correct.

## New Results
For every n >= 1: sum_j h_j = 0, S_n^- = S_n^+, the first 2^(n-1) residue moments vanish and the next one is 1/2, sum h_j/w_j = 5^(n-1)/(2·3^(n+1)), and H_n(0) = -sum h_j ln w_j. For n >= 2: S_n^- >= (2/5) C_n^-. For n = 1: S_1^- = 1/(2 sqrt 13) ≈ 0.1386750491.

## Prior Art
Residue power sums from the Laurent expansion at infinity (the "sum of residues is zero when the degree gap is >= 2" rule) are textbook complex analysis. Mellin transforms of rational functions with negative real poles, and their continuation via pi/sin(pi alpha), are standard. The bound min s(s+5) = -25/4 is elementary. Gasket spectral decimation (Rammal-Toulouse, Fukushima-Shima, Teplyaev) supplies the setting. No external search was done for these specific constants.

## Novelty Analysis
The method is KNOWN. The constants (5^(n-1)/(2·3^(n+1)), the 2/5 floor, 1/(2 sqrt 13)) are specific to the repository's construction and may not appear in the literature in this form. Their novelty is UNRESOLVED.

## Falsification Attempts
- Independent check (this slice; /workspace/es-audit/check_es_lean.py, pure-Python integer polynomials plus mpmath at 150 digits). It builds A_n, B_n from EQ's recursion as stated in the task (A_0 = s+3, B_0 = 1, A_(n+1) = [(s+6)A_n(p) - 2s(s+5)B_n(p)]/(s+2), B_(n+1) = (s+5)B_n(p)), with an exactness check on the division by s+2, and builds Q_n = prod_(k<=n-2)(p^k + 5) on its own. It does not import any repository code. Checks: degree gap 2^(n-1)+1; exact Laurent coefficients (Fractions) 0 for m < 2^(n-1) and 1/2 at m = 2^(n-1); h_n(0) = 5^(n-1)/(2·3^(n+1)) and A_n(0) = 3^(n+1) exactly; residues computed directly as Q_n(z_j)/(2A_n'(z_j)) and compared with c_j/(2q_(n-1)(z_j)); all c_j > 0, sum c_j = 1; numeric power sums; sum h_j/w_j; S_n^- = S_n^+; negative counts 2^(n-2) on {p^(n-1) < -5}; S_n^- >= (2/5) C_n^- and min q_(n-1) >= -5/4 at the negative poles; S_1^- = 1/(2 sqrt 13). Results: every check passed for n = 1..6 (n = 6 finished at 1022.5 s wall on a load-26 box; the run was stopped during n = 7, which did not finish in the time box). Degree gaps 2, 3, 5, 9, 17, 33. Largest |Q_n/(2A_n') - c_j/(2q_(n-1))| was 8.8e-103 (n = 6); largest relative power-sum error was 4.0e-104. S_n^- = 0.1386750491, 0.1721204086, 0.0956848017, 0.0514241311, 0.0255395123, 0.0120411135; C_n^- = 0.0839748528, 0.4226424684, 0.1785254910, 0.1013288360, 0.0500236842, 0.0233106734; S_n^-/C_n^- = 1.651 (n = 1), 0.4072, 0.5360, 0.5075, 0.5105, 0.5165; min q_(n-1) at negative-residue poles = -0.303, -1.228, -1.146, -1.144, -1.243, -1.131 (all >= -5/4); H_n(0) = 0.1579836359, 0.0685090601, 0.0266745120, 0.0095409589, 0.0032661609, 0.0010987844. All values match GASKET.md ES.4 (b) to the digits shown.
- An earlier sympy-based version of the same check (60 digits, lambdified expanded polynomials) passed n = 1..4 but tripped its own 1e-40 residue-agreement threshold at n = 5. That was float cancellation in evaluating expanded degree-32 polynomials at 60 digits, not a counterexample. At 200 digits it gave errors ≤ 1e-192 for n = 1..4, and the 150-digit Horner check above covers n = 5 and 6. Kept here, not hidden.
- mpmath quadrature (this slice, n = 1..4): int_0^oo h_n agrees with -sum h_j ln w_j to < 1e-20 (0.1579836359, 0.06850906012, 0.02667451197, 0.009540958935), matching GASKET.md ES.4 (c).
- Repository CI test tests/test_flux_identity.py::test_theorem_es_h_residue_sums: 1 passed in 7.8 s (fresh clone at 361b25c). The local-only tests/test_cli.py ES test runs the full witness (repository time 2118.6 s) and was NOT run here. A first attempt with a too-broad pytest -k filter selected many other slow CLI tests and was stopped by its 600 s timeout with no failures reported; it says nothing about ES. The full witness script was not rerun.
- Proof attack: the n = 1 boundary (q_0 = s + 5 is linear, so the p ∘ p^(n-2) argument needs n >= 2; n = 1 is handled in closed form); positivity of h_n on s > 0 for dominated convergence; the 1/w_j identity read as F_n(1) = h_n(0); the 2/5 floor near-tight at n = 2 (S_2^-/C_2^- = 0.40725). All held.
- Document consistency: README.md, CLAIM_STATUS.md and GASKET.md state the same ES.1–ES.3, the same kept limits (floor only; no Y_n - Y_oo sign), and the same status labels. The reported per-level decay ratios 0.556, 0.537, 0.497, 0.472, 0.465, 0.448 agree with the listed S_n^- values. No contradiction found.

## Experimental Validation
None applicable (pure mathematics on a finite graph). Computer checks as above.

## Mathematical Status
Theorem (proof every n >= 1, conditional on EQ and ER and therefore on AQ (1) as stated). ES.4: exact checks n <= 10, certified n <= 8 (repository); independent checks as listed above.

## Patent Relevance
None. Identities and a floor for the residues of a rational function on the combinatorial gasket. Not a flux, not thrust.

## Related Discoveries
- DISC-0257 (Theorem ER): the sign count that ES.3 sums over. Its kept limit "no magnitude, no sum" is closed here.
- DISC-0256 (Theorem EQ): degrees, A_n(0) = 3^(n+1), Q_n, simple poles.
- DISC-0255 (Theorem EP), DISC-0254 (Theorem EO): the residue route for om_n and the n = 1 closed form h_1 = 1/(2(s^2+7s+9)).

## Open Questions
- An upper bound, limit or rate for S_n^- and C_n^- (observed decay factor about 0.45–0.56 per level for n <= 8, not proved).
- Whether the moment identities plus the floor decide any thin level (0.88, n = 9) or any sign of Y_n - Y_oo.
- N = 2, 3; alpha-cells; poles of r_n versus r_(n+1). Stage 2 is still BLOCKED (no Psi_info).
- A prior-art search for the explicit constants.

## Next Experiments
- Combine ES.1's vanishing moments with ER's interval locations to get a two-sided bound on F_n(alpha) for alpha in (gamma, 1), and test it at (0.88, n = 9).

## Reproduction Instructions
1. Clone informational-flux-identity and check out 361b25c217af.
2. Run pip install python-flint mpmath.
3. Run python3 scripts/gasket_fractional_corner_h_residue_sums.py (about 35 min on a loaded box; n = 8 at 2048 bits dominates). Exit 0 means every check passed. For the fast CI subset: python3 -m pytest -q tests/test_flux_identity.py -k theorem_es.

## Evidence Log
- 2026-11-22: commit 361b25c217af read (GASKET.md §Theorem ES, new script docstring, README and CLAIM_STATUS rows, both new tests). Independent exact/mpmath checks and the CI test were run here; the full witness was not.

## Change History
- 2026-11-22: created.
