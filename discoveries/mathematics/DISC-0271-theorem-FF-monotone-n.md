# Discovery: Theorem FF, monotonicity in n of G_n = ρ^-n·H_n for 2 ≤ n ≤ 10 on real α ∈ [−1, 1), with a certified kept failure at n = 1

## Discovery ID
DISC-0271

## Status
THEOREM (mathematical sense only) for FF.1 (Arb certificate, 2 ≤ n ≤ 10, real α ∈ [−1, 1)). FF.2 is a certified KEPT FAILURE (n = 1 is not monotone near α = −1). FF.3 is OPEN / OBSERVED (sign of G_2 − G_1 on (−13/20, −3/8); n ≥ 11). Method KNOWN (FC's ball evaluator, monotonicity in α, Arb rigorous integration). Whether the constants μ_n are new is UNRESOLVED (no literature search). **Status change: DISC-0268 FC.4 / DISC-0270's open item "G_(n+1) > G_n OBSERVED only" becomes THEOREM for 2 ≤ n ≤ 10, REJECTED for n = 1 on (−1, −13/20], and stays OPEN for n ≥ 11.**

## Date Discovered
2026-11-23. The commit is from 7:45 AM EST and was indexed at about 8:00 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 192340ee69caf4691d8d3e6e98a6b24410e15667 (2026-11-23T12:45:13Z = 2026-11-23 7:45:13 AM EST). Parent: 0279889e2465 (Theorem FE, DISC-0270).

## Original Evidence
- GASKET.md §Theorem FF (+16 lines, including one Reproduce line).
- scripts/gasket_fractional_corner_h_alpha_monotone_n.py (new, 171 lines; python-flint arb, exit 1 on any failure; repo reports 918.6 s local).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+15 lines, HAlphaMonotoneNTests, float only).

## Discovery
- FF.1: for n ∈ {2,…,10} and every real α ∈ [−1, 1), G_(n+1)(α) − G_n(α) = ∫ t^−α (h_n − h_(n+1)) dt ≥ μ_n·3^−n, with μ_2..μ_10 ≥ 0.054350, 0.061110, 0.062337, 0.061557, 0.060536, 0.059745, 0.059211, 0.058864, 0.058634, each minimum on [3/4, 1]. With FC.2 and FB.4: G_2 < G_3 < … < G_11 < W/2.
- FF.2 (KEPT FAILURE): G_2 < G_1 on (−1, −13/20] (certified; witness G_2(−4/5) − G_1(−4/5) ∈ [−7.524274669, −7.521126147]); G_2 > G_1 on [−3/8, 1) (3(G_2 − G_1) ≥ 0.038527).
- FF.3 (OPEN): sign on (−13/20, −3/8) not certified; float crossing ≈ −0.56. n ≥ 11 open: FB's bounds m·3^−n ≤ D_n ≤ C·3^−n (m ≥ 0.0674, C ≤ 1095.75) would need m > C/3.

## Why It Matters
It closes the last OBSERVED item of the n ≤ 10 gasket chain (FC.4) and shows exactly where monotonicity breaks (n = 1, α near −1), which bounds any future "monotone for all n" claim.

## Derivation
Checked here, not re-derived in full. G_(n+1) − G_n = D_n − D_(n+1) follows from D_n = W/2 − G_n. For fixed t, α ↦ t^−α g(t) is monotone whatever the sign of g, so min over [a_0, a_1] is min(t^−a_0 g, t^−a_1 g): a valid lower integrand. Large-t tail: f_(n+1) ≥ 0 gives h_n − h_(n+1) = f_(n+1) − f_n ≥ −f_n and t^−α f_n ≤ t^−a_0 f_n for t ≥ 1, α ≥ a_0, as the repo states. FF.2's consequence on (−1, α_c] follows from G_2 < W/2 (FC.2) and G_1 ≥ W/2 there (FC.3/FD.3). The n ≥ 11 kept limit is correct: D_n > D_(n+1) from FB needs m·3^−n > C·3^−(n+1), i.e. m > C/3. The limit 3^n(G_(n+1) − G_n) → (2/3)V(α) follows from FB.3: 3^n D_n − (1/3)·3^(n+1) D_(n+1) → V − V/3.

## Assumptions
As stated by the repository: FC's list (FB.1's exact split and bounds, EX.1, EU.1/EU.3/EU.4, BD.4, EV.1, EV.2), FC.1's ball evaluator and FC.2's tail bounds unchanged; FC.2, FC.3, FD.3 for FF.2. Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4). Rigour of python-flint's integrator and real_min/real_max assumed (textbook tool).

## New Results
Certified lower bounds μ_n; certified n = 1 sign pattern (negative on (−1, −13/20], positive on [−3/8, 1)).

## Prior Art
Arb interval integration and monotone-in-parameter bounding are standard. No literature search on these specific constants.

## Novelty Analysis
Method KNOWN. The constants are specific to this construction; novelty of the constants UNRESOLVED.

## Falsification Attempts
- Repository script rerun on the box at 192340ee69ca: see Evidence Log for exit status.
- Repository CI test HAlphaMonotoneNTests: 1 passed (7.5 s).
- Independent of repository code: /workspace/corpus-discovery/ff_check.py (mpmath 30 digits, the DISC-0268 fc_check evaluator, D_n by mp.quad on blocks [5^m, 5^(m+1)]), G_(n+1) − G_n = D_n − D_(n+1):
  - α = −0.8, n = 1: −7.52112646 (inside the certified witness interval [−7.524274669, −7.521126147], near its upper end). **Held.**
  - α = −0.65, n = 1: 3·dG = −2.2915 (repo float −2.25); α = −0.56: +0.1170; α = −0.5: +0.6912; α = −3/8: +0.9405 (≥ 0.038527 ✓). Crossing between −0.65 and −0.56, consistent with the observed ≈ −0.56 (slightly below it). **Held** (FF.3 stays OBSERVED).
  - α = −0.99, n = 2: 9·dG = 18.896 (repo bisected lower bound ≥ 7.708 on [−1, −15/16]) ✓; α = −0.5, n = 5: 3^5·dG = 15.85 > 0 ✓.
  - α = 0.95: 3^n·dG = 0.061580 (n = 2), 0.067495 (n = 10), matching the repo's 0.0616 and 0.0675; α = 0.99, n = 2: 0.056588 ≥ μ_2 = 0.054350 ✓ (minimum toward α → 1, as claimed).
- Logic: checked the endpoint-min rule, tail sign, the FF.2 consequence chain and the m > C/3 kept limit. No contradiction between commit message, GASKET.md, CLAIM_STATUS.md and the test.

## Experimental Validation
Not applicable (pure mathematics). Functions on a graph, not a flux, not thrust; the repo's Stage 2 remains blocked.

## Mathematical Status
THEOREM (FF.1); certified counterexample (FF.2); OPEN (FF.3, n ≥ 11).

## Patent Relevance
None.

## Related Discoveries
- DISC-0268 (Theorem FC): FC.4 monotonicity OBSERVED → THEOREM for 2 ≤ n ≤ 10; FC.1 evaluator and FC.2 tails reused. Label: mathematical.
- DISC-0269 (Theorem FD) / DISC-0270 (Theorem FE): α_c used in FF.2; FE's open item closed for 2 ≤ n ≤ 10. Label: mathematical.
- DISC-0267 (Theorem FB): FB.3/FB.4 give the chain end G_11 < W/2 and the (2/3)V limit. Label: mathematical.

## Open Questions
Certified sign change of G_2 − G_1 on (−13/20, −3/8) and its uniqueness; monotonicity for n ≥ 11 (needs a rate for 3^n D_n → V); α < −1 and non-real α.

## Next Experiments
Finer Arb bisection on (−13/20, −3/8) with D_1-style derivative bound (FE.3); a rate for 3^n D_n → V(α).

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_monotone_n.py` at informational-flux-identity 192340ee69ca (~15 min, python-flint 0.9.0). Independent: `python3 ff_check.py <alpha> <n>` (mpmath).

## Evidence Log
- 2026-11-23 ~8:00 AM EST: commit read; logic checked; CI test passed; independent mpmath checks held; repo script rerun: repo script EXIT 0 (17m45s wall on box, load ~43; 'all FF checks passed').

## Change History
- 2026-11-23 ~8:00 AM EST: created.
- 2026-11-23 ~9:20 AM EST: status note. FF.3 (sign of G_2 - G_1 on (-13/20,-3/8), OPEN) is settled by Theorem FG (informational-flux-identity 0a6f9431aee9; DISC-0272): exactly one simple zero beta_c in (-0.5679,-0.5677); G_2 > G_1 iff alpha > beta_c. The text above is kept as first written.
