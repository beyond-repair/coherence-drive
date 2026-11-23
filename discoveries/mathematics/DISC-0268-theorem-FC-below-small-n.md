# Discovery: Theorem FC, approach from below for 2 ≤ n ≤ 10 (so ρ^-n·H_n(α) < W(α)/2 for every n ≥ 2 on real α ∈ [−1, 1)) and a kept failure at n = 1

## Discovery ID
DISC-0268

## Status
THEOREM (mathematical sense only) for FC.1 (exact identity) and FC.2 (Arb certificate); FC.3 is a certified KEPT FAILURE; FC.4 is OBSERVED (float Simpson). Method KNOWN (FB.1's exact split, monotonicity in α, Arb rigorous integration with real_min/real_max). Whether the constants are new is UNRESOLVED (no literature search). **Status change: DISC-0267's kept limit "n ≤ 10 from below is OBSERVED only" is closed for 2 ≤ n ≤ 10 (THEOREM) and REJECTED at n = 1 near α = −1 (kept failure).**

## Date Discovered
2026-11-23. The commit is from 4:41 AM EST and was indexed at about 5:05 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 0f0ca3bd3e5dcf4a7a65461f780083d7dd0303e8 (2026-11-23T09:41:41Z = 2026-11-23 4:41:41 AM EST). Parent: 7d8d12e5ed36 (Theorem FB, DISC-0267).

## Original Evidence
- GASKET.md §Theorem FC (+19/−2 lines; FB's kept-limits paragraph marked in place, not rewritten).
- scripts/gasket_fractional_corner_h_alpha_below_small_n.py (new, 313 lines; python-flint 0.9.0 arb, 128 bits, exit 1 on failure).
- CLAIM_STATUS.md (+1 row, CI count now 31 tests); tests/test_flux_identity.py (+16 lines).

## Discovery
Notation of FB: h_n = f − f_n, D_n(α) = W(α)/2 − ρ^-n H_n(α) = ∫_0^∞ t^-α h_n dt.
- FC.1 (exact): a cancellation-free ball evaluator h_n = f·(E − expm1 Δ)/(1+E), with d_{k+1} = d_k(Y_k + Z_k + 5), d_0 = ψ(s) − s from EV.1.
- FC.2 (Arb): for n = 2..10 and every real α ∈ [−1, 1), D_n ≥ m_n·3^-n with m_2..m_10 ≥ 0.085097, 0.092085, 0.092890, 0.091657, 0.090298, 0.089284, 0.088611, 0.088181, 0.087902 (minimum on [3/4, 1]). With FB.4: 3^n·D_n ≥ 0.0674 for every n ≥ 2 and real α ∈ [−1, 1).
- FC.3 (KEPT FAILURE, Arb): at n = 1, D_1 < 0 on (−1, −3/4]; witness D_1(−4/5) ∈ [−3.394831488, −3.394830962]. D_1 > 0 on [−73/100, 1). Float crossing α_c ≈ −0.7407 (not certified, uniqueness not certified). Mechanism: ψ_0(t/5) = t/5 is linear, so f_1 ~ 15/t² and G_1(α) → +∞ as α → −1⁺ while W(−1) is finite.
- FC.4 (OBSERVED): float minima within 2% of m_n; G_{n+1} > G_n for n = 2..10 on a grid, not certified.

## Why It Matters
It completes the sign statement of the α-weighted refinement limit on the real strip: from n = 2 on, the refinement approaches W/2 strictly from below, uniformly at rate ≥ 0.0674·3^-n. It also shows the statement is sharp in n: n = 1 genuinely fails.

## Derivation
Repository proof (GASKET.md §Theorem FC): monotonicity of α ↦ t^-α h_n(t) for fixed t bounds the integrand on α-intervals by a pointwise min/max, integrated by Arb on blocks [5^m, 5^{m+1}], m = −24..6; small-t tail ≤ 5^-24/30 from FB.1; large-t tail from f_n ≤ 3^n/(t ψ_{n−1}(t/5)) and ψ_{n−1}(t/5) ≥ (t/5^{J+1})^{2^J}. Not re-derived here beyond the checks below.

## Assumptions
As stated by the repository: FB.1, EX.1, EU.1/EU.3/EU.4, BD.4, EV.1, EV.2; correctness of Arb / python-flint 0.9.0. Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4).

## New Results
Strict approach from below for all n ≥ 2 on real α ∈ [−1, 1); the n = 1 counterexample. My independent check also implies, as a by-product, f_1(t) = 1/(6·P_1·(5+t/5)·(1+E)), a closed form usable without ψ.

## Prior Art
Textbook analysis plus certified interval integration; no external search done.

## Novelty Analysis
Methods KNOWN. Constants specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts
Independent of repository code (mpmath 30 digits, mpmath.quad in u = log t over breakpoints m·ln5, m = −30..12, or to 60 for n = 1; ψ by Koenigs iteration from v + v²/20; f = 1/(6P(5+ψ(t/5))), f_n = 1/(6P_n(5+p^{n−1}(5^-n t))(1+E)) as derived from FB.1's split). Script /workspace/corpus-discovery/fc_check.py (box), outputs fc_*.out.
- FC.3 witness: D_1(−4/5) = −3.39483107166, inside the repository's Arb ball [−3.394831488, −3.394830962]. **Held (kept failure confirmed).**
- n = 1 sign change: D_1(−0.74) = +0.02353, D_1(−0.73) = +0.3315, so the crossing lies in (−0.8, −0.74), consistent with α_c ≈ −0.7407. **Held.**
- FC.2 lower bounds: 3^n D_n at α = 0.75, 0.9, 0.99 for n = 2, 3, 6, 10 are all positive: at α = 0.99, 0.08845 (n = 2), 0.09559, 0.09373, 0.09128 (n = 10), all above m_n; the smallest values sit near α → 1 as stated. At α = −1: 77.70, 176.73, 294.74 (n = 6, matches DISC-0267's check 294.740345), 304.30 (n = 10). At α = −0.7407: 29.46, 52.91, 79.00, 80.51. **Held.**
- Document consistency: commit message and GASKET.md agree; FB's kept limit is marked in place, not rewritten. No contradiction found.
- Not done: the repository Arb script (≈296 s local) and CI were not rerun.

## Experimental Validation
Not applicable (pure mathematics). Computer checks above.

## Mathematical Status
THEOREM (FC.1, FC.2 via Arb certificate), KEPT FAILURE (FC.3), OBSERVED (FC.4, α_c value).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
- DISC-0267 (Theorem FB): FC closes its kept limit for 2 ≤ n ≤ 10 and refutes it at n = 1. Label: mathematical.
- DISC-0263 (Theorem EX): EX.1 integral representation; EX.4's observed "increase to W" now proved from below for n ≥ 2 (monotonicity in n still OBSERVED). Label: mathematical.
- DISC-0261 (Theorem EV): EV.1/EV.2 evaluator. Label: computational.

## Open Questions
Certify α_c and its uniqueness; prove G_{n+1} > G_n (FC.4); sign statements for α < −1 and non-real α.

## Next Experiments
Arb bisection of D_1 on (−3/4, −73/100); certified monotonicity in n.

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_below_small_n.py` at informational-flux-identity 0f0ca3bd3e5d (requires python-flint 0.9.0). Independent: `python3 fc_check.py <alpha> <n,n,...>` (mpmath).

## Evidence Log
- 2026-11-23 ~5:05 AM EST: commit read; independent mpmath checks at 6 α values, n = 1, 2, 3, 6, 10; all held.

## Change History
- 2026-11-23 ~5:05 AM EST: created.
- 2026-11-23 ~6:05 AM EST: status note. The open item "α_c ≈ −0.7407 and uniqueness uncertified" is closed by Theorem FD (informational-flux-identity 2f21233357a9; DISC-0269): exactly one zero α_c ∈ (−0.7408, −0.7406). The text above is kept as first written.
- 2026-11-23 ~8:00 AM EST: status note. FC.4 (monotonicity in n, OBSERVED) is certified for 2 <= n <= 10 and real alpha in [-1,1) by Theorem FF (informational-flux-identity 192340ee69ca; DISC-0271); at n = 1 it fails on (-1,-13/20] (certified kept failure); n >= 11 stays OPEN. The text above is kept as first written.
