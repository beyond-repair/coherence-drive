# Discovery: Theorem EW, W(alpha) is holomorphic for Re alpha < 1 and vanishes at alpha = 2 pi i k/ln5 (k != 0)

## Discovery ID
DISC-0262

## Status
THEOREM (mathematical sense only) for EW.1–EW.4; EW.5 is OBSERVED, not proved. Rests on EU.4, BD.4/BJ.6, EV.1, BG.3, BI.4, Koenigs linearization and Arb correctness as stated in the repository. Method KNOWN: the Mellin transform of a function whose 5-adic periodization is constant vanishes at the nonzero log-periodic frequencies (a standard Mellin / Poisson-summation fact). Whether anything here is new is UNRESOLVED, because no literature search was done.

## Date Discovered
2026-11-22. The commit is from 10:16 PM EST and was indexed at about 11:00 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 084cb3bba7ca28a9654aa106c0d4417726d3dcfa (2026-11-23T03:16:16Z = 2026-11-22 10:16:16 PM EST). Parent: 3b810e829dd0 (Theorem EV, DISC-0261).

## Original Evidence
- GASKET.md §Theorem EW (+26), README.md (+1), CLAIM_STATUS.md (+2; CI now 25 tests).
- scripts/gasket_fractional_corner_h_zero_mellin.py (new, 124 lines), registered in scripts/cli.py; tests/test_cli.py (+13), tests/test_flux_identity.py (+20).

## Discovery
- W(alpha) = int_0^oo tau^-alpha R(tau)/(5+psi(tau/5)) dtau = int_0^oo F(tau) tau^(-alpha-1) dtau, F = tau R/(5+psi(tau/5)) >= 0; W(0) = ln5 (EU).
- EW.1: F <= tau/15 and F <= G tau^gamma/psi(tau/5) (BI.4); psi(5v) >= psi(v)^2 with psi(1) = 1.0508 > 1 gives psi(tau) >= exp(b tau^(log_5 2)); hence W is absolutely convergent and holomorphic on Re alpha < 1.
- EW.2: with omega_k = 2 pi k/ln5, W(i omega_k) = 0 for every integer k != 0.
- EW.3: 3^n H_n(i omega_k) -> W(i omega_k)/2 = 0.
- EW.4 (certified Arb): |W(i omega_1)|, |W(i omega_2)| <= 1.21e-29; the k = 0 ball contains ln5.
- EW.5 (OBSERVED): |3^n H_n(i omega_1)| = 1.96e-5, 5.36e-5, 4.39e-5, 1.54e-5, 4.2e-6, 1.2e-6 for n = 1..6; no rate claimed.

## Why It Matters
It answers EV's open item "W(alpha) for alpha != 0" at the log-periodic imaginary points, and shows that the continuum corner functional carries no log-periodic oscillation at first order — the partition of unity forces it.

## Derivation
Re-derived this run. Put tau = 5^j sigma, sigma in [1,5). For Re alpha = 0, F >= 0 and Tonelli allow exchanging sum and integral:
W(alpha) = int_1^5 sum_j F(5^j sigma) 5^(-j alpha) sigma^(-alpha-1) dsigma.
At alpha = i omega_k, 5^(-j alpha) = 1, and EU.4's sum_j F(5^j sigma) = 1 gives W(i omega_k) = int_1^5 sigma^(-i omega_k - 1) dsigma = (1 - 5^(-i omega_k))/(i omega_k) = 0 for k != 0, and ln5 for k = 0. EW.1 and EW.3 were read, not re-derived line by line.

## Assumptions
EU.4 (partition of unity), BD.4/BJ.6, EV.1, BG.3, BI.4, Koenigs linearization, Arb correctness.

## New Results
An infinite discrete family of zeros of W on the imaginary axis; 3^n H_n at those points tends to 0.

## Prior Art
Mellin transforms of functions with a constant geometric periodization, and the vanishing at the "fluctuation" frequencies 2 pi i k/ln q, are standard (e.g. Mellin-transform harmonic-sum analysis, Flajolet–Gourdon–Dumas 1995, and log-periodic oscillations in fractal spectral asymptotics). No external search for this specific functional.

## Novelty Analysis
Method KNOWN; the result is a direct consequence of EU.4's partition of unity. Specific statement for this gasket functional: UNRESOLVED.

## Falsification Attempts
Independent mpmath script /workspace/corpus-discovery/ew_check.py (34 digits, N = 70): partition of unity sum_j F(5^j tau) - 1 = 4e-34, 4e-34, 3e-34 at tau = 1.7, 3.3, 4.9; quadrature on [5^-30, 5^9] gives W(0) - ln5 = -7.2e-23 (= the omitted head int_0^(5^-30) F/tau ~ 5^-30/15), |W(i omega_1)| ~ 1.8e-23 and |W(i omega_2)| ~ 9.1e-24, both at the same truncation scale. Consistent with EW.2/EW.4. Nothing broke. The repository's script and CI were not rerun this run. Not checked: EW.5's finite-n values.

## Experimental Validation
Numerical only.

## Mathematical Status
Theorem (EW.1–EW.4); observation (EW.5).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
DISC-0260 (EU.4 partition of unity, W(0) = ln5), DISC-0261 (EV evaluator and tail), DISC-0259 (ET.1/ET.2 scaling and dominator reused in EW.3).

## Open Questions
W(alpha) for real alpha != 0 (value, sign, closed form); whether these are all the zeros; rate of 3^n H_n(i omega_k) -> 0; S_n^-, C_n^-; N > 1.

## Next Experiments
Compute W on (0,1) and the real-axis behaviour; test for other zeros off the imaginary axis; fit a rate to EW.5.

## Reproduction Instructions
In informational-flux-identity @ 084cb3bba7ca: `python scripts/gasket_fractional_corner_h_zero_mellin.py` (reported 267.6 s; python-flint). Independent check: ew_check.py (mpmath).

## Evidence Log
- 2026-11-22 ~11:00 PM EST: ew_check.py results above.

## Change History
- 2026-11-22 ~11:00 PM EST: created (THEOREM EW.1–EW.4, OBSERVED EW.5; method KNOWN, statement UNRESOLVED).
