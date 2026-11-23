# Discovery: Theorem FE, D_n = W/2 − ρ^-n·H_n is holomorphic on −2^(n−1) < Re α < 1 and may be differentiated under the integral (discharges Theorem FD's assumption)

## Discovery ID
DISC-0270

## Status
THEOREM (mathematical sense only) for FE.1–FE.4. Method KNOWN (textbook: elementary max bound, dominated convergence, mean value theorem, Morera/Fubini). No new constant; nothing here is novel as mathematics. **Status change: DISC-0269 (Theorem FD) loses its stated ASSUMPTION "differentiation under the integral"; FD.2/FD.3 now hold with no assumption beyond FD's already-proved inputs.**

## Date Discovered
2026-11-23. The commit is from 6:11 AM EST and was indexed at about 7:00 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 0279889e24656a115e57ea22d0a2b23f66b6db07 (2026-11-23T11:11:15Z = 2026-11-23 6:11:15 AM EST). Parent: 2f21233357a9 (Theorem FD, DISC-0269).

## Original Evidence
- GASKET.md §Theorem FE (+16 lines) and a one-phrase edit to §Theorem FD's assumptions ("ASSUMPTION, *discharged by Theorem FE*"); the original assumption text is kept, not deleted.
- scripts/gasket_fractional_corner_h_alpha_analytic.py (new, 60 lines; pure Python; checks FE.1 only, exit 1 on failure).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+11 lines, HAlphaAnalyticTests).

## Discovery
- FE.1: for k ≥ 1, δ > 0, real u: |u|^k e^(−δ|u|) ≤ (k/(eδ))^k. Hence for a' + δ ≤ Re α ≤ b' − δ: |ln t|^k |t^−α| ≤ (k/(eδ))^k (t^−a' + t^−b').
- FE.2: |h_n| ≤ f + f_n, so ∫ t^−a |h_n| ≤ W(a)/2 + G_n(a) < ∞ for real a ∈ (−2^(n−1), 1) (EX.1, nonnegative integrands).
- FE.3: D_n is holomorphic on −2^(n−1) < Re α < 1, D_n^(k)(α) = ∫ (−ln t)^k t^−α h_n dt, with |D_n^(k)| ≤ (k/(eδ))^k [W(a')/2 + G_n(a') + W(b')/2 + G_n(b')].
- FE.4: D_1 is real-analytic on (−1, 1); its only zero α_c ∈ (−0.7408, −0.7406) is simple (D_1'(α_c) ≥ 26.39).

## Why It Matters
It removes the only unproved step from DISC-0269, so the n = 1 crossing result is unconditional (relative to the earlier gasket chain).

## Derivation
Re-derived here. FE.1: u^k e^(−δu) is maximised at u = k/δ with value (k/δ)^k e^−k. Dominator: for t ≥ 1, t^−Re α = t^−a' · t^−(Re α − a') ≤ t^−a' e^(−δ ln t); for t < 1, t^−Re α = t^−b' · t^(b' − Re α) ≤ t^−b' e^(−δ|ln t|); multiply by |ln t|^k and apply FE.1. FE.3 then follows by the standard dominated-convergence argument for parameter integrals; FD.2's interval [−3/4, −73/100] fits with a' = −0.8, b' = −0.68, δ = 0.05 (a' + δ = −0.75, b' − δ = −0.73, a' > −1). The argument is complete.

## Assumptions
As stated by the repository: EX.1 (finiteness of W/2 and G_n on the strip), f, f_n ≥ 0 continuous (EU.1/EU.3, BD.4). Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4).

## New Results
None beyond the discharge; the derivative bound is not evaluated numerically (repo kept limit: G_1(a') blows up as a' → −1).

## Prior Art
Standard theorem on holomorphic parameter integrals (any real/complex analysis text). No external search needed for the method.

## Novelty Analysis
KNOWN method. The record exists only for provenance of DISC-0269's status change.

## Falsification Attempts
- Repository script rerun on the box at 0279889e2465: "FE.1 lemma (k=1..3) and dominator on FD.2 interval: ok", EXIT 0. **Held.**
- Independent of repository code: /workspace/corpus-discovery/fe_check.py (mpmath 30 digits). FE.1 on a grid u ∈ [0, 4000], k ∈ {1,2,3,5}, δ ∈ {0.01, 0.05, 0.5}: max ratio to the bound 0.99999999 (sharp, never above 1). Dominator on FD.2's interval (11 values of α, t = 5^(m/8), m = −400..400): 0 violations. **Held.**
- Logic: checked the t ≥ 1 / t < 1 split and the strip endpoint (f_1 ~ 15/t² forces a' > −1 for n = 1; −0.8 is inside). No contradiction between commit message, GASKET.md and CLAIM_STATUS.md.
- Not done: CI not rerun.

## Experimental Validation
Not applicable (pure mathematics).

## Mathematical Status
THEOREM (FE.1–FE.4).

## Patent Relevance
None.

## Related Discoveries
- DISC-0269 (Theorem FD): assumption discharged. Label: mathematical.
- DISC-0263 (Theorem EX): EX.1 supplies the integrability. Label: mathematical.

## Open Questions
Closed form for α_c; G_(n+1) > G_n (FC.4, still OBSERVED); α < −1 and non-real α.

## Next Experiments
Certified monotonicity in n.

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_analytic.py` at informational-flux-identity 0279889e2465. Independent: `python3 fe_check.py` (mpmath).

## Evidence Log
- 2026-11-23 ~7:00 AM EST: commit read; proof re-derived; repo script EXIT 0; independent mpmath check held.

## Change History
- 2026-11-23 ~7:00 AM EST: created.
