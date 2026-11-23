# Discovery: Theorem EU, the value of ET's limit: 3^n H_n(0) -> ln5/2, so W(0) = ln5

## Discovery ID
DISC-0260

## Status
EU.1–EU.3: THEOREM (mathematical sense only). They rest only on AQ's recursion, EQ.1 and ES.2 as stated in the repository, and no longer on BG.3, BI.4 or BJ.6. EU.4 (the rate c 3^-n): THEOREM for the limit formula, conditional on BD.4 and BJ.6. The numerical value of c is OBSERVED and not certified. This **changes the status of DISC-0259's ET.5 from CONJECTURE to THEOREM**: K = W(0)/2 = ln5/2. The method is KNOWN (an exact telescoping closed form plus a Frullani integral). Whether the constants are new is UNRESOLVED, because no literature search was done.

## Date Discovered
2026-11-22. The commit is from 8:45 PM EST and was indexed at about 9:05 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 1e03cae997ed (2026-11-23T01:45:56Z = 2026-11-22 8:45:56 PM EST). Parent: 87936a0d4338 (Theorem ET, DISC-0259).

## Original Evidence
- GASKET.md §Theorem EU (+40/-2, which includes the in-place mark "ET.5 ... Status: PROVED by Theorem EU" and the mark on ET's open item). README.md (+1/-1). CLAIM_STATUS.md (+2/-1; CI now has 23 tests).
- scripts/gasket_fractional_corner_h_zero_value.py (new, 229 lines), registered in scripts/cli.py. tests/test_cli.py (+14) and tests/test_flux_identity.py (+36).

## Discovery
- Setting: p(s) = s(s+5), q_k = p^k + 5. AQ's step is 1/r_(k+1)(s) = c(s)/r_k(p(s)) - e(s), with c = (s+6)/((s+2)(s+5)), e = 2s/(s+2) and r_0 = 1/(3+s). h_n = r_n/(2 q_(n-1)) and H_n(0) = int_0^oo h_n.
- EU.1 (exact, every n >= 0). 1/r_n(s) = s/2 + ((s+6)/2) prod_(k<n) (p^k(s)+3)/(p^k(s)+5). Equivalently, 2A_n = s B_n + (s+6) prod_(k<n)(p^k+3).
- EU.2 (exact, every n >= 1). Let r~_n = 2/((s+6)Theta_n), where Theta_n is the product above, and g_n = 3^(n+1) s r~_n/p^n. Then 2·3^n H_n(0) = ln5 - E_n - D_n, where E_n = int (s+4) g_n/(3(s+2)(s+5)) ds >= 0 and D_n = (3^-n/2) int t R_n R~_n/(5+psi_(n-1)(t/5)) dt >= 0.
- EU.3. E_n <= 5^(5/3-n) for n >= 2, and 3^n D_n <= (pi/72) 5^(11/2) < 305 for n >= 3. Hence 3^n H_n(0) <= ln5/2 for every n, and 3^n H_n(0) -> ln5/2, so W(0) = ln5.
- EU.4. 1/R = 3 prod_(j>=1) (5/3)(psi(5^-j t)+3)/(psi(5^-j t)+5). There is a partition of unity sum_j F(5^j t) = 1 with F = tR/(5+psi(t/5)). 3^n(ln5/2 - 3^n H_n(0)) -> c = (1/4) int t R^2/(5+psi(t/5)) dt = 2.67182281196926907... (quadrature digits, OBSERVED).

## Why It Matters
It turns DISC-0259's only conjecture into a theorem, with an explicit rate. It also removes the dependence of the limit on BG.3, BI.4 and BJ.6. The limit is now proved with explicit, crude, non-asymptotic error bounds, and the closed form EU.1 for r_n is new structure for the whole H_n route. alpha = 0 is still outside the (gamma, 1) window where Y_n lives, so EU decides no sign of Y_n - Y_oo.

## Derivation
Reviewer check (this slice):
1. EU.1 by induction, checked by hand. First, c·p/2 - e = s(s+6)/(2(s+2)) - 2s/(s+2) = s/2. Second, c·(p+6) = (s+6)(s+2)(s+3)/((s+2)(s+5)) = (s+6)(s+3)/(s+5). So, if 1/r_k(y) = y/2 + ((y+6)/2) Theta_k(y), then 1/r_(k+1)(s) = c[p/2 + ((p+6)/2) Theta_k(p)] - e = s/2 + ((s+6)/2)·((s+3)/(s+5))·Theta_k(p(s)) = s/2 + ((s+6)/2) Theta_(k+1)(s). The base case is n = 0: 1/r_0 = s + 3. **Held.**
2. EU.2 and EU.3 (Frullani along p and the two correction bounds): read, not re-derived line by line. The identity and the bounds were attacked numerically (see Falsification Attempts).

## Assumptions
- AQ's recursion, EQ.1 (r_n = B_n/A_n, B_n = prod (p^k+5)) and ES.2 (H_n(0) = int h_n), as in DISC-0256 and DISC-0258.
- For EU.4 only: BD.4 (psi_k increasing to psi, psi(5v) = p(psi(v))) and BJ.6 (psi(v) <= v e^(v/10)), not re-derived here.

## New Results
K = ln5/2 exactly. 3^n H_n(0) <= ln5/2 for every n >= 1. Finite-n error: 2(ln5/2 - 3^n H_n(0)) = E_n + D_n <= 5^(5/3-n) + 305·3^-n for n >= 3. Rate constant c = (1/4) int t R^2/(5+psi(t/5)), numerically 2.6718228119...

## Prior Art
Frullani integrals and telescoping products under a self-similar map are textbook. The setting is spectral decimation on the Sierpinski gasket (Rammal–Toulouse, Fukushima–Shima, Teplyaev), and a log 5 from the time-scaling factor 5 is the expected shape. No external search was done.

## Novelty Analysis
The method is KNOWN. The specific constants (K = ln5/2, c) are tied to the repository's construction. Novelty is UNRESOLVED.

## Falsification Attempts
These checks are independent: mpmath only, and no repository code was imported. The scripts are /workspace/corpus-discovery/eu_check.py and eu_check2.py on the box.
- EU.1: 1/r_n from the Moebius recursion against the product formula, n = 0..8, five points (s = 0.013, 0.37, 2.5, 11, -0.7). The maximum relative error was 2.8e-40 at 40 digits. **Held.**
- EU.2 identity: computed 2·3^n H_n(0) + E_n + D_n - ln5 directly from the definitions of g_n, r~_n and R_n, n = 1..6, at 30 digits. The result was -2.0e-31 at every n, which is zero to working precision. E_n <= 5^(5/3-n) held at every n checked, and g_n(0+) = 1. **Held.**
- EU.3: ln5/2 - 3^n H_n(0) > 0 for n = 1..20, and 2(ln5/2 - 3^n H_n(0)) <= 5^(5/3-n) + 305·3^-n for n = 3..20. **Held.**
- EU.4: c_n = 3^n(ln5/2 - 3^n H_n(0)) for n = 1..20 equals 0.992, 1.693, ..., 2.671944 at n = 18. Richardson (5c_n - 3c_(n-1))/2, which assumes a next correction of order (3/5)^n, gives 2.6718228223 at n = 20. Its distance to the repository's 2.67182281197 shrinks by about 3x per level. Consistent with the value, but not a certification.
- Not done: the repository witness (967.5 s) and the CI tests were not rerun. EU.3's constants (5^(5/3-n), (pi/72)5^(11/2)) were checked numerically, not re-derived.
- Document consistency: the commit message, GASKET.md and the in-place mark on ET.5 agree. No contradiction was found.

## Experimental Validation
Not applicable (pure mathematics). Computer checks are listed above.

## Mathematical Status
EU.1, EU.2 and EU.3: THEOREM (exact identity plus elementary bounds). EU.4: THEOREM for the limit formula. c's digits: OBSERVED. DISC-0259's ET.5 is now THEOREM.

## Patent Relevance
None. This is an identity for rational functions on the combinatorial gasket. It is not a flux and not thrust.

## Related Discoveries
- DISC-0259 (Theorem ET): its ET.5 conjecture K = ln5/2 is proved here, and ET's rate gap is closed (c identified).
- DISC-0258 (Theorem ES): ES.2's H_n(0).
- DISC-0256 (Theorem EQ): EQ.1's A_n, B_n. EU.1 gives A_n in closed form.

## Open Questions
- A closed form or certified enclosure for c. Is the next correction of order 5^-n?
- Monotonicity of 3^n H_n(0) in n (observed, not proved).
- Does EU.1's closed form give limits of H_n(alpha) inside (gamma, 1), or of S_n^- and C_n^-? Any Y_n - Y_oo sign at 0.88, n = 9? N = 2, 3. Stage 2 is still BLOCKED (no Psi_info).

## Next Experiments
- Arb-certify c, and use PSLQ against ln5, pi and gasket constants.
- Use EU.1 to write h_n explicitly and retry the Y_n window.

## Reproduction Instructions
1. Check out informational-flux-identity at 1e03cae997ed and run pip install mpmath.
2. Run python3 scripts/gasket_fractional_corner_h_zero_value.py (repository: 967.5 s). Exit 0 means every check passed.
3. Independent check: reimplement the Moebius step r_(k+1)(s) = (s+2)(s+5)x/((s+6) - 2s(s+5)x) from r_0 = 1/(3+s). Compare against EU.1, then integrate H_n(0), E_n and D_n with breakpoints 5^(k/2-n). This takes a few minutes.

## Evidence Log
- 2026-11-22 ~9:05 PM EST: read commit 1e03cae997ed (commit message, GASKET.md §Theorem EU). Checked EU.1's induction by hand. Ran the independent mpmath checks above.

## Change History
- 2026-11-22: created.
