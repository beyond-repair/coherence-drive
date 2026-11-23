# Discovery: Theorem EV, a certified Arb enclosure of EU's rate constant c

## Discovery ID
DISC-0261

## Status
THEOREM (mathematical sense only): EV.1–EV.3 are proofs in the repository, and EV.4 is a certified interval computation (Arb / python-flint acb_calc_integrate) that rests on EU.4, BD.4, Koenigs linearization and the correctness of Arb. Method KNOWN (Koenigs coefficient recursion, explicit truncation bounds, rigorous ball-arithmetic integration). Whether the constant is new is UNRESOLVED, because no literature search was done. This **changes the status of DISC-0260's EU.4 value of c from OBSERVED to certified enclosure**.

## Date Discovered
2026-11-22. The commit is from 9:11 PM EST. It was indexed at about 11:00 PM EST; the ~9:55 PM run missed it (the events feed showed no push).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3b810e829dd05edbaa789ab35406048a302a824f (2026-11-23T02:11:36Z = 2026-11-22 9:11:36 PM EST). Parent: 1e03cae997ed (Theorem EU, DISC-0260).

## Original Evidence
- GASKET.md §Theorem EV (+32), README.md (+1), CLAIM_STATUS.md (+1; CI now 24 tests).
- scripts/gasket_fractional_corner_h_zero_rate_constant.py (new, 208 lines), registered in scripts/cli.py; tests/test_cli.py (+13), tests/test_flux_identity.py (+30).

## Discovery
- c = (1/4) int_0^oo t R(t)^2/(5+psi(t/5)) dt = lim 3^n(ln5/2 - 3^n H_n(0)) (EU.4).
- EV.1 (exact): psi(5w) = psi(w)(psi(w)+5) gives Taylor coefficients a_m(5^m - 5) = sum_(i=1)^(m-1) a_i a_(m-i), a_1 = 1, a_2 = 1/20, 0 <= a_m <= 20^(1-m); so |psi(w) - w - w^2/20| <= |w|^3/(400(1-|w|/20)); psi increasing on [0,oo), psi(5v) >= psi(v)^2.
- EV.2: truncation bound for EU.4's infinite product (|prod_(j>J) f_j - 1| <= e^delta - 1 once |5^-J z| <= 2^-130) gives a rigorous complex-ball evaluator of R and psi.
- EV.3: R decreasing; the tail beyond 5^8 is <= 2·5^17 R(5^8)^2/(5+psi(5^7)) <= 1.77e-52.
- EV.4 (certified): c in [2.6718228119692690732957669002, 2.6718228119692690732957669003]; ball 2.671822811969269073295766900258501 +/- 3.5e-34. The same evaluator's K ball contains ln5/2.

## Why It Matters
It closes EU's kept limit "c by quadrature, not an arb enclosure": the second-order term of the gasket corner functional now has a certified value rather than observed digits.

## Derivation
EV.1 follows by equating coefficients of w^m in psi(5w) = 5psi(w) + psi(w)^2; the bound a_m <= 20^(1-m) follows by induction since (m-1)·20^(2-m) <= (5^m - 5)·20^(1-m) iff 20(m-1) <= 5^m - 5, true for m >= 2 (equality at m = 2). Checked by hand this run. EV.2–EV.3 were read, not re-derived line by line. EV.4 is the repository's Arb computation.

## Assumptions
EU.4 (product formula for 1/R and the partition of unity), BD.4, Koenigs linearization, correctness of Arb / python-flint.

## New Results
A certified 28-digit enclosure of c; c has no closed form in the repository.

## Prior Art
Koenigs/Poincaré functions of quadratic maps and their Taylor recursions are textbook; Arb rigorous integration (Johansson) is standard. No external search for the constant.

## Novelty Analysis
Method KNOWN. The constant c is specific to this gasket construction; whether it appears elsewhere is UNRESOLVED.

## Falsification Attempts
Independent mpmath script /workspace/corpus-discovery/ew_check.py (34 digits, product truncated at N = 70, quadrature split at powers of 5 on [0, 5^9]): c = 2.67182281196926907329576690026, which differs from EV's ball midpoint by 4.8e-35 — inside the ball. Exact rational check of EV.1: a_2 = 1/20 and 0 <= a_m <= 20^(1-m) for m <= 40. Nothing broke. The repository's script and CI were not rerun this run.

## Experimental Validation
Numerical only; no physical experiment applies.

## Mathematical Status
Theorem (with certified numerics).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
DISC-0260 (EU.4 defines c; EV certifies it), DISC-0259 (ET), DISC-0262 (EW reuses EV's evaluator and tail bound).

## Open Questions
Closed form for c; next term of 3^n H_n(0); monotonicity; S_n^-, C_n^-; N > 1.

## Next Experiments
Run scripts/gasket_fractional_corner_h_zero_rate_constant.py and the 24-test CI locally; look for c in terms of known constants (PSLQ against ln5, pi, Koenigs-type constants) as a heuristic only.

## Reproduction Instructions
In informational-flux-identity @ 3b810e829dd0: `python scripts/gasket_fractional_corner_h_zero_rate_constant.py` (needs python-flint; reported 205.5 s locally). Independent check: ew_check.py (mpmath), recorded in the Evidence Log.

## Evidence Log
- 2026-11-22 ~11:00 PM EST: ew_check.py: c = 2.67182281196926907329576690026, minus EV midpoint = 4.8e-35; EV.1 coefficient recursion and bound held m <= 40.

## Change History
- 2026-11-22 ~11:00 PM EST: created (THEOREM; method KNOWN, constant UNRESOLVED).
