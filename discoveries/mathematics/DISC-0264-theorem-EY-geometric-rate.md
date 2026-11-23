# Discovery: Theorem EY, an explicit geometric rate (2/5)^n for the alpha-weighted refinement limit on the strip -1 <= Re alpha <= 9/10

## Discovery ID
DISC-0264

## Status
THEOREM (mathematical sense only) for EY.1–EY.3; the true rate 3^-n (EY.4) is OBSERVED, not proved. Rests on EU.1, EU.3, EU.4, BD.4, BJ.6 and EX.1, all as stated in the repository and not re-derived here. Method KNOWN: a log-Lipschitz comparison of Koenigs iterates (psi_m vs psi), a pointwise ratio bound, and a super-exponential tail estimate. The constants are specific to this repository; whether they are new is UNRESOLVED (no literature search).

## Date Discovered
2026-11-23. The commit is from 12:07 AM EST and was indexed at about 1:00 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 9adc08ff3a1d7d09c78cfb6cda490312d151929e (2026-11-23T05:07:22Z = 2026-11-23 12:07:22 AM EST). Parent: 165a8ed0eded (Theorem EX, DISC-0263).

## Original Evidence
- GASKET.md §Theorem EY (line ~6916, +16 lines).
- scripts/gasket_fractional_corner_h_alpha_rate.py (new, 177 lines; floats, log-grid Simpson, exit 1 on failure).
- tests/test_flux_identity.py, class HAlphaRateTests (+31 lines).

## Discovery
With f_n = R_n/(2(5+psi_(n-1)(t/5))), f = R/(2(5+psi(t/5))), G_n = rho^-n H_n:
- EY.1: 0 <= log psi(t) − log psi_m(t) <= (t/10)(2/5)^m.
- EY.2: for 0 < t <= (5/2)^n, |f_n(t)/f(t) − 1| <= (t/3)(2/5)^n.
- EY.3: for every complex alpha with −1 <= Re alpha <= 9/10 and every n >= 11, |rho^-n H_n(alpha) − W(alpha)/2| <= (W(alpha−1)/6 + 1)(2/5)^n.
- EY.4 (OBSERVED): the true gap is about 3^-n; 3^n(W/2 − G_n) ≈ 304.73, 24.894, 0.3976, 0.1152 at alpha = −1, −1/2, 1/2, 9/10 (n = 12).

## Why It Matters
It is the first rate of any kind for the limit of DISC-0263 at alpha != 0 (DISC-0263's kept limit "no rate for alpha != 0"). The ratio 2/5 is not sharp; the observed ratio is 1/3.

## Derivation
Hand-checked here:
- EY.1: psi(t) = p^m(psi(w)), psi_m(t) = p^m(w), w = 5^-m t. psi(w) >= w (nonnegative Taylor coefficients, EV.1), so the left inequality holds. d log p/d log y = 1 + y/(y+5) <= 2, so log p^m is 2^m-Lipschitz in log y; with BJ.6 log(psi(w)/w) <= w/10 this gives <= 2^m · 5^-m t/10. Correct.
- EY.3 tail: psi_(n-1)(t/5) >= (t/5^(J+1))^(2^J) (p(y) >= y^2 J times, then psi_k(x) >= x since p(y) >= 5y); f_n + f <= 1/(3(5+psi_(n-1)(t/5))). Substituting u = t/5^(J+1) gives exactly (1/3)·5^((J+1)(1−a))·s0^(1−a−2^J)/(2^J+a−1). Since 5^(J+1)s0 = T_n > 1, the expression is T_n^(1−a)·s0^(−2^J)/(3(2^J+a−1)), decreasing in a, so a = −1 is the worst case. Correct.
- Head: integrating EY.2 against |t^-alpha| f gives (2/5)^n/3 · ∫ t^(1−Re alpha) f = (2/5)^n · W(Re alpha − 1)/6.
- EY.2's numeric constants (0.0127, 0.037, 0.127, 0.106) were not re-derived by hand; they were checked numerically (below).

## Assumptions
EU.1, EU.3 (R_n <= 1/3), EU.4 (product for 1/R), BD.4, BJ.6 (psi(v) <= v e^(v/10)), EX.1 — as stated in the repository.

## New Results
An explicit, uniform geometric bound with constant W(Re alpha − 1)/6 + 1 on the strip, for n >= 11.

## Prior Art
Koenigs linearization and comparison of iterates, dominated tails: textbook. Spectral decimation on the Sierpinski gasket: KNOWN (Fukushima–Shima, Strichartz, Teplyaev). No external search for these constants.

## Novelty Analysis
Methods KNOWN. The bound is specific to this repository's functional; novelty UNRESOLVED.

## Falsification Attempts
Independent checks (ey_check.py: mpmath 30 digits, own psi via 60-step Koenigs with second-order start; ey_check2.py: mpmath tail formula; ey_check3.py: numpy float, 400001-point log-grid Simpson on [1e-14, 1e9]):
- EY.1, m = 0..9, 51 log-spaced t in [0.01, 1000]: no negative value; worst ratio to the bound 0.49996.
- EY.2, n = 1..12, 61 log-spaced t in [1e-4, (5/2)^n]: worst ratio to the bound 0.6167 (n = 1), falling to 0.0562 (n = 12). Matches the repository's 0.617.
- EY.3 tail formula, a = −1, n = 11..60: s0 > 1 and tail <= (2/5)^n every time; ratio 0.1679 at n = 11. At n = 10 the ratio is 16.4, so the n >= 11 threshold is needed and correctly stated.
- EY.3 itself, alpha = −1, −1/2, 1/2, 9/10, n = 11, 12, 13: actual gap / bound between 7.9e-3 and 2.5e-2. Held with wide slack.
- EY.4 constants reproduced: 3^n·gap = 304.81, 24.892, 0.39736, 0.11517 at n = 13 (304.73, 24.894, 0.39758, 0.11524 at n = 12).
- Cross-check: W(−1) = 71.7956686755 (float), W(0) − ln5 = 3.2e-12.
Nothing broke.
- Notational caveat (not a failure): for complex alpha the constant written W(alpha−1) should read W(Re alpha − 1); the proof integrates t^(1−Re alpha) f, and W is real and positive only on the real axis. For real alpha the two agree.
- Repository script and CI not rerun.

## Experimental Validation
Numerical only. No physical experiment; the repository says "functions on a graph, not a flux, not thrust".

## Mathematical Status
THEOREM (EY.1–EY.3, conditional on the listed repository results); OBSERVED (EY.4, rate 3^-n).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
- DISC-0263 → DISC-0264. Label: mathematical. EY puts a rate on EX.1's limit and partly closes EX's kept limit "no rate for alpha != 0".
- DISC-0260 → DISC-0264. Label: mathematical. EU.1 closed form, EU.3 R_n <= 1/3, EU.4 product for 1/R.
- DISC-0262 → DISC-0264. Label: mathematical. W(alpha − 1) finite because Re(alpha − 1) < 1 (EW.1).

## Open Questions
Prove the 3^-n rate (EY.4) and identify its constants as a function of alpha; extend below Re alpha = −1 and above 9/10; cover n < 11; certify the constants in Arb.

## Next Experiments
Fit c(alpha) = lim 3^n(W/2 − G_n) on a real grid and compare with EU.4's c(0) = 2.67182...; test whether c(alpha) has a Mellin-type integral like EU.4's.

## Reproduction Instructions
In informational-flux-identity @ 9adc08ff3a1d: `python scripts/gasket_fractional_corner_h_alpha_rate.py`. Independent checks: ey_check.py, ey_check2.py, ey_check3.py (local to the research box, not committed).

## Evidence Log
- 2026-11-23 ~1:00 AM EST: ey_check.py / ey_check3.py results above.

## Change History
- 2026-11-23 ~1:00 AM EST: created (THEOREM EY.1–EY.3, OBSERVED EY.4; method KNOWN, constants UNRESOLVED).
- 2026-11-23 ~2:00 AM EST: correction and status note. In 9adc08ff3a1d, EY.3's tail inequality was only grid-checked for n < 40 (the repository says so in 3a6c5e27648d); this record did not say that. Theorem EZ (informational-flux-identity 3a6c5e27648d; DISC-0265) now proves the tail for every n >= 11. EY.2's float constants and W(Re alpha − 1) remain uncertified. The text above is kept as first written.
- 2026-11-23 ~3:00 AM EST: correction and status note. Theorem FA (informational-flux-identity 3aa8369c57c8; DISC-0266) finds that EY.2's constant 0.127 is false by a hair (sharp value 4 − √15 = 0.12701665…; witness y = 39/10), which this record accepted; EY.2 and EY.3 still hold after the correction. FA certifies all of EY's constants and W(−2), so EY.3 holds with C = W(Re α − 1)/6 + 1 ≤ 1882.97224758106857. The text above is kept as first written.
