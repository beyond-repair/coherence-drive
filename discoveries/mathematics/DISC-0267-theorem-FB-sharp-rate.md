# Discovery: Theorem FB, the sharp 3^-n rate for ρ^-n·H_n(α) → W(α)/2, its exact leading coefficient V(α), and approach from below

## Discovery ID
DISC-0267

## Status
THEOREM (mathematical sense only) for FB.1–FB.3; FB.4 is an Arb certificate; FB.5 is OBSERVED (non-rigorous 200-bit quadrature). Method KNOWN (exact split of EY's closed form, mean value theorem on Koenigs iterates, dominated convergence, Arb quadrature). Whether the constants are new is UNRESOLVED (no literature search). **Status change: DISC-0264's EY.4 (true 3^-n rate and its limiting constants) moves from OBSERVED to THEOREM; DISC-0266's open item "prove the 3^-n rate" is closed.** No kept failure in the repository.

## Date Discovered
2026-11-23. The commit is from 3:29 AM EST and was indexed at about 4:15 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 7d8d12e5ed3638632ef7cd2efd36510adc5eafda (2026-11-23T08:29:51Z = 2026-11-23 3:29:51 AM EST). Parent: 3aa8369c57c8 (Theorem FA, DISC-0266).

## Original Evidence
- GASKET.md §Theorem FB (+30 lines, from line 6973).
- scripts/gasket_fractional_corner_h_alpha_sharp_rate.py (new, 288 lines; python-flint arb, exit 1 on failure).
- CLAIM_STATUS.md (+1 row; CI count now 30 tests); tests/test_flux_identity.py (+30 lines).

## Discovery
Notation: G_n(α) = ρ^-n H_n(α) = ∫ t^-α f_n, W(α)/2 = ∫ t^-α f, a = Re α, w = 5^-n t, P = ∏_{j≥1} g(ψ(5^-j t)) (1/R = 3P), P_n = ∏_{k<n} g(p^k(5^-n t)).
- FB.1 (exact split): f_n/f = e^Δ/(1+E), E = (t/6)3^-n(1/P_n + (3/5)^n), Δ = log(P/P_n) + log((5+ψ(t/5))/(5+ψ_{n-1}(t/5))), with (t/2)3^-n R ≤ E ≤ (t/6)3^-n(1+(3/5)^n) and 0 ≤ Δ ≤ w[(c*n+1)κ max(1,t)^{log5 2}/10 + e^{w/50}/30], c* = 4 − √15, κ = exp(e^{0.1}/4). The 3^-n part E is the only negative one; the ψ-part is O(n5^-n t M), which is where EY's (2/5)^n came from.
- FB.2: for n ≥ 9 and −1 ≤ Re α < 1, |G_n − W/2| ≤ C_n(a)·3^-n, C_n(a) = (1+(3/5)^n)W(a−1)/12 + δ_n(W(a−1)+W(a−3/2))/2 + τ_n; uniformly C ≤ 1330.6917 (n ≥ 9), ≤ 1095.7499 (n ≥ 11). Arb: W(−5/2) ∈ [199623.963637, 199623.963638]. This replaces FA's 1882.97·(2/5)^n and widens the strip from Re α ≤ 9/10 to Re α < 1.
- FB.3: 3^n(W/2 − G_n) → V(α) = (1/4)∫ t^{1−α} R²/(5+ψ(t/5)) dt on −1 ≤ Re α < 1; V(0) = EU.4/EV's c.
- FB.4 (Arb): for real α ∈ [−1, 1) and n ≥ 11, W/2 − G_n ≥ m_i·3^-n > 0 on 12 subintervals (m ≥ 29.17 on [−1, −9/10] … ≥ 0.06741 on [3/4, 1)). So the approach is from below, two-sided Θ(3^-n).
- FB.5 (OBSERVED): n = 2..60 at 10 α values, all from below, converging to V; n ≤ 10 from below is observed only.

## Why It Matters
It closes the last OBSERVED item of the EY→EZ→FA line: the rate is now the sharp 3^-n with an exact leading coefficient, not the (2/5)^n upper bound. It extends EU.4's α = 0 rate constant to a function V(α) on the whole strip, and proves the one-sidedness (monotone side) that EX.4 only observed. Values: V(−1) = 304.937971786, V(−1/2) = 24.887593103, V(1/2) = 0.397026453, V(9/10) = 0.115055944 (floats). The archive's DISC-0264 had recorded EY.4's float estimates (304.7, 24.89, 0.3976, 0.1152); the first is now seen to be about 0.08% low, consistent with the slow (3/5)^n correction.

## Derivation
Reviewer reading (this slice): FB.1's split is EY's closed form 1/R_n = 3P_n + (t/2)3^-n(1 + (3/5)^n P_n) divided by 1/R = 3P; I re-derived that P_n = (5/3)^n Θ_n from EU.1 (Θ_n = ∏(p^k+3)/(p^k+5)), so (3/5)^n P_n = Θ_n and the split is consistent with DISC-0260's EU.1. The bounds on E follow from 1 ≤ P_n ≤ P. The Δ upper bound (mean value theorem in log y on p^m, Π(u) ≤ κ max(1,u)^{log5 2}) and the tail τ_n were read, not re-derived line by line. FB.3's dominated-convergence argument was read and is the standard one.

## Assumptions
As stated in the repository: EU.1, EU.3, EU.4, BD.4, EV.1, EV.2's ball evaluator, EX.1, EX.2 (W decreasing on (−∞, α*], α* > 3/5), FA.1, FA.2, EY.3/EZ's tail reduction. Textbook: mean value theorem, dominated convergence, Arb's rigorous integrator.

## New Results
|ρ^-n H_n(α) − W(α)/2| ≤ 1095.75·3^-n for n ≥ 11, −1 ≤ Re α < 1. Exact asymptotic W/2 − G_n = V(α)3^-n + o(3^-n). Strict approach from below on the real segment [−1, 1) for n ≥ 11.

## Prior Art
Rates of convergence of renormalised iterates to a Koenigs/Poincaré function and Mellin-type functionals under spectral decimation on the Sierpinski gasket (Fukushima–Shima, Teplyaev, Derfel–Grabner–Vogl) are a known setting; the method is textbook. No external search was done.

## Novelty Analysis
Method KNOWN. The specific V(α) and constants are tied to the repository's construction. Novelty UNRESOLVED.

## Falsification Attempts
Independent of repository code (plain Python doubles, Simpson h ≈ 0.01 in log t on [5^-45, 5^{max(n,9)+3}]; ψ by Koenigs iteration from w + w²/20; f − f_n computed through FB.1's split with expm1 to avoid cancellation). Script: /workspace/corpus-discovery/fb_check2.py, output fb_check2.out (box).
- V(α): V(−1) = 304.93797178590, V(−1/2) = 24.88759310334, V(0) = 2.67182281196927 (EV's c to 4e-15), V(1/2) = 0.39702645280, V(9/10) = 0.11505594387. All match the repository's floats to the digits given. **Held.**
- 3^n(W/2 − G_n), n = 6, 9, 11, 14, 18, 24: positive at every α tried (from below) and converging to V. α = −1: 294.74, 303.78, 304.5735 (n = 11, matches repo 304.5735), 304.86, 304.928, 304.9386. α = 0: 2.7010 at n = 6 (the repo's overshoot), then 2.6829, 2.6761, 2.6728, 2.67194, 2.67184 ↓ c. All values lie between FB.4's floors m_i and FB.2's C ≤ 1095.75. **Held.**
- W(−5/2) = 199623.96363754 (inside the Arb bracket), W(−2) = 11291.8334854864 (matches FA.4), W(−1), W(−1/2), W(1/2), W(0) = ln5 match EX.3/EU to 1e-13. (W(9/10) came out 5e-4 low only because of my lower cutoff 5^-45, where t^{0.1} is not small; not a repository issue.)
- An mpmath pointwise check of FB.1's E and Δ bounds was started but abandoned as too slow (fb_check.py); the bounds are indirectly supported by the integrated split reproducing V. Not done: the repository script (Arb, 537 s) and the CI tests were not rerun.
- Document consistency: the commit message, GASKET.md and CLAIM_STATUS.md agree. No contradiction found.

## Experimental Validation
Not applicable (pure mathematics). Computer checks above.

## Mathematical Status
FB.1–FB.3: THEOREM. FB.4: THEOREM (Arb-certified). FB.5: OBSERVED.

## Patent Relevance
None. Pure analysis of functions on a graph; the repository itself says "not a flux, not thrust; Stage 2 still blocked".

## Related Discoveries
- DISC-0264 (Theorem EY) → DISC-0267: mathematical; EY.4 OBSERVED → THEOREM.
- DISC-0266 (Theorem FA) → DISC-0267: mathematical; FA's c*, ψ bound and W(−2) are inputs; FA's "q = 2/5 not sharp" closed.
- DISC-0265 (Theorem EZ) → DISC-0267: mathematical; tail reduction reused.
- DISC-0260/0261 (EU, EV) → DISC-0267: mathematical; V(0) = c.
- DISC-0263 (Theorem EX) → DISC-0267: mathematical; EX.4's observed side proved.

## Open Questions
- Is the approach from below true for n ≤ 10 (observed only)? Next-order term (repo: "(3/5)^n-ish")? Closed form for V(α)? Behaviour of V as α → 1⁻ and for Re α < −1.

## Next Experiments
Rerun the repository script; certify the second-order correction; extend FB.4 to complex α.

## Reproduction Instructions
In informational-flux-identity @ 7d8d12e: python scripts/gasket_fractional_corner_h_alpha_sharp_rate.py (needs python-flint). Independent: python3 fb_check2.py (plain Python, ~5 min).

## Evidence Log
- 2026-11-23 ~4:15 AM EST: read commit 7d8d12e (message, GASKET.md §FB, CLAIM_STATUS.md diff); ran fb_check2.py; all checks held.

## Change History
- 2026-11-23 ~4:15 AM EST: created.
