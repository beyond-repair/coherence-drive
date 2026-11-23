# Discovery: Theorem FD, the n = 1 crossing of D_1 = W/2 − ρ^-1·H_1 is unique on (−1, 1) and lies in (−0.7408, −0.7406)

## Discovery ID
DISC-0269

## Status
THEOREM (mathematical sense only) for FD.1, FD.2 (Arb certificates) and FD.3 (consequence with FC.3); FD.4 is an OBSERVED correction about the repository's own float evaluator. Method KNOWN (sign bracket plus a certified positive derivative, Arb rigorous integration). Differentiation under the integral is an ASSUMPTION stated by the repository (with a domination sketch). Whether the constant α_c is new is UNRESOLVED (no literature search). **Status change: DISC-0268's open item "α_c ≈ −0.7407 and its uniqueness uncertified" (OBSERVED) becomes THEOREM: exactly one zero, bracketed to width 2·10^-4.**

## Date Discovered
2026-11-23. The commit is from 5:06 AM EST and was indexed at about 6:05 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 2f21233357a9e3ae642046a8735ce64239bc37c8 (2026-11-23T10:06:16Z = 2026-11-23 5:06:16 AM EST). Parent: 0f0ca3bd3e5d (Theorem FC, DISC-0268).

## Original Evidence
- GASKET.md §Theorem FD (+13 lines; FC's kept-limits paragraph not rewritten).
- scripts/gasket_fractional_corner_h_alpha_n1_crossing.py (new, 118 lines; python-flint arb, 128 bits, exit 1 on failure; reuses FC's evaluator and tails).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+13 lines).

## Discovery
Notation of FB/FC: h_1 = f − f_1, D_1(α) = ∫_0^∞ t^-α h_1 dt.
- FD.1 (Arb): D_1(−3703/5000) ≥ 0.0033645979 > 0 (α = −0.7406) and D_1(−463/625) ≤ −0.0034022267 < 0 (α = −0.7408).
- FD.2 (Arb): D_1'(α) = ∫ t^-α(−ln t) h_1 dt ≥ 26.3930645 > 0 for every α ∈ [−3/4, −73/100] (pointwise monotone integrand, real_min of endpoint values on blocks 5^m, m = −24..6, analytic tails).
- FD.3: with FC.3 (D_1 < 0 on (−1, −3/4], D_1 > 0 on [−73/100, 1)), D_1 has exactly one zero α_c on (−1, 1), α_c ∈ (−0.7408, −0.7406); ρ^-1 H_1 < W/2 exactly for α > α_c (real α).
- FD.4 (OBSERVED correction): the repository's float Simpson D truncates f_1 at 5^13 and is unreliable near −0.74 (gives +0.118 at −0.741 where Arb gives ≈ −0.0034 at −0.7408). FC's float ≈ −0.7407 agreed with the bracket by luck.

## Why It Matters
It closes the last open sign question of DISC-0268 at n = 1: the failure region of "approach from below" is exactly (−1, α_c), with α_c certified to four decimals.

## Derivation
Repository proof (GASKET.md §Theorem FD): intermediate value on [−0.7408, −0.7406] from FD.1; strict monotonicity on [−3/4, −73/100] from FD.2; FC.3 excludes zeros outside that interval. Logic re-checked here; it is complete given the stated assumptions.

## Assumptions
As stated by the repository: all of FC's (FB.1, EX.1, EU.1, EU.3/EU.4, BD.4, EV.1, EV.2, Arb integrator and acb.real_min) and FC.3; differentiation under the integral for α > −1 (ASSUMPTION; h_1 = O(t) at 0, O(t^-2) at ∞). Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4).

## New Results
Unique crossing α_c ∈ (−0.7408, −0.7406). Independent interpolation (below) puts α_c ≈ −0.74070 (OBSERVED).

## Prior Art
Textbook analysis plus certified interval integration; no external search done.

## Novelty Analysis
Methods KNOWN. Constant specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts
- Repository script rerun on the box at 2f21233357a9 (python-flint 0.9.0, load ≈ 35): all FD checks PASS, min certified D_1' lower bound 26.3931, elapsed 87.4 s, EXIT 0. **Held.**
- Independent of repository code: /workspace/corpus-discovery/fc_check.py (mpmath 30 digits, mpmath.quad in u = log t over breakpoints m·ln5, m = −30..60, so no 5^13 truncation). D_1(−0.7406) = +0.0033646654 (≥ repo bound 0.0033645979), D_1(−0.7408) = −0.0034022935 (≤ repo bound −0.0034022267), D_1(−0.75) = −0.340212 (repo scan −0.340), D_1(−0.73) = +0.331500. Secant slopes 33.8 on the FD.1 bracket and 33.6 on [−3/4, −73/100], above the certified 26.39. Linear interpolation α_c ≈ −0.740699. **Held.**
- Logic: FD.2 covers [−3/4, −73/100], which contains the FD.1 bracket, and FC.3 covers the complement in (−1, 1); no gap. No contradiction between commit message, GASKET.md and CLAIM_STATUS.md.
- Not done: CI not rerun; differentiation-under-integral assumption not separately proved here.

## Experimental Validation
Not applicable (pure mathematics). Computer checks above.

## Mathematical Status
THEOREM (FD.1–FD.3, conditional on stated assumptions), OBSERVED (FD.4, interpolated α_c digits).

## Patent Relevance
None. Pure mathematics.

## Related Discoveries
- DISC-0268 (Theorem FC): FD closes its open item "certify α_c and uniqueness". Label: mathematical.
- DISC-0267 (Theorem FB): n = 1 boundary of the kept limit now sharp. Label: mathematical.
- DISC-0261 (Theorem EV): evaluator reused through FC. Label: computational.

## Open Questions
Closed form or higher-precision α_c; G_{n+1} > G_n (FC.4, still OBSERVED); α < −1 and non-real α.

## Next Experiments
Certified monotonicity in n; extend sign analysis below α = −1.

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_n1_crossing.py` at informational-flux-identity 2f21233357a9 (python-flint). Independent: `python3 fc_check.py <alpha> 1` (mpmath).

## Evidence Log
- 2026-11-23 ~6:05 AM EST: commit read; repo script rerun EXIT 0 (87.4 s); independent mpmath D_1 at 4 α values; all held.

## Change History
- 2026-11-23 ~6:05 AM EST: created.
