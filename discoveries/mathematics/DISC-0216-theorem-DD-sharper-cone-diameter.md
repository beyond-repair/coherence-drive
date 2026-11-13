# Discovery: Theorem DD, a sharper diameter for CF.2's Birkhoff cone (θ 0.5441 → 0.4267, per-level rate 0.8855 → 0.8434)

## Discovery ID
DISC-0216

## Status
THEOREM in the mathematical sense only (the repository contains the proof and a certified `arb` witness). Method KNOWN (Birkhoff–Hilbert-metric cone contraction with a finer oscillation estimate). Constants UNRESOLVED as to novelty. No new phenomenon; the true spectral rate 0.1725 is unchanged and still reached only by the spectral route.

## Date Discovered
2026-10-31 (indexed ~10:00 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 1630b8a08515a2366e261cce9dddf6d8097bc171 (2026-10-31 09:09:50 EDT).

## Original Evidence
- GASKET.md §"Theorem DD. A sharper diameter for CF.2's cone" (inserted after Theorem DC, before Conjecture J.1).
- CLAIM_STATUS.md, new row "A sharper diameter for CF.2's cone (GASKET Theorem DD …)".
- scripts/gasket_fractional_profile_level_cone.py (new, 271 lines; imports CF's script unchanged, CE's for r, CC's for level sums).
- tests/test_cli.py `test_theorem_dd_profile_level_cone`; README.md reproduction list; scripts/cli.py registration.

## Discovery
Same setting as CE/CF/DC: L̃f = w̃₁ f∘σ₁ + w̃₂ f∘σ₂ on X_s = [√5/2, 5/2], σ_{1,2}(s) = √(15/4 ∓ s), w̃₁ = (s+½)/(2s(7/2−s)), w̃₂ = (s−½)/(2s(s+7/2)), cone C_a of positive f with log f a-Lipschitz, a = 47/2, block L̃⁵.
- DD.1 (exact): by the mediant inequality over the 32 length-5 words, osc_X log L̃⁵f ≤ max_{p,q,w}[sup_{J_p} log w̃_w − inf_{J_q} log w̃_w + a·dist⁺(σ_wJ_p, σ_wJ_q)] for f ∈ C_a.
- DD.2 (arb, 2048 cells): V_D ≤ 0.73438 (CF.2: V_5 = 1.0426526), Δ_D ≤ 1.82349, θ_D = tanh(Δ_D/4) ≤ 0.42672, θ_D^{1/5} < 0.84339 (CF.2: 0.8855).
- DD.3: CF.3, CF.5, DC hold with θ_D; non-leading C¹ eigenvalues |μ| ≤ θ_D^{1/5} r < 0.3575 (CF.5: 0.3752); DC.3 level-sum bound |log(s_{k+1}/(r s_k))| ≤ θ_D^{⌊(k−4)/5⌋}·0.28154093, equal to DC.3 for k = 4..8 and 1.2752, 1.6261, 2.6441, 11.368 times smaller at k = 9, 14, 24, 54. C_D = Θ_G θ_D^{−8/5} ≤ 1.09984 is larger than DC's 0.74544057 (block factor), though the floor form is never larger.
- DD.4: f_± = e^{±as} certify sup osc ≥ V_low = 0.51383, so V_D is within 1.43× of any oscillation bound for this cone and block.

## Why It Matters
Closes DC's open item "a better cone" partially: a strictly better Birkhoff constant inside the same cone, plus a certified floor showing how much more this cone family can give. It also records (floats, no claim) that re-optimising a and n in this family stalls (oscillation term ≈ 0.594), so log-Lipschitz cones of this form cannot approach the spectral 0.1725.

## Derivation
DD.1 is Σp_w/Σq_w ≤ max_w p_w/q_w applied termwise with f(σ_wx)/f(σ_wy) ≤ e^{a|σ_wx−σ_wy|}. Δ_D = 2 log((a+b₅)/(a−b₅)) + 2V_D is CF.2's cone lemma with V_5 replaced; θ = tanh(Δ/4) is Birkhoff's theorem. DD.3 substitutes θ_D in CF.3/CF.5/DC.1–DC.3 unchanged.

## Assumptions
CF.1, CF.2's b₅ = 2.078593340 and cone step, CF.3/CF.5 arguments (use Δ only through θ), DC.1–DC.3 proofs, DC.2's Θ_G ≤ 0.28154093 (not re-run by DD). Outward rounding of the float pair maximum with a 10⁻¹² pad.

## New Results
θ_D ≤ 0.42672; per-level Birkhoff rate < 0.84339; non-leading C¹ spectrum radius < 0.3575; sharper explicit level-sum bound for k ≥ 9; certified floor 0.51383 for this cone/block.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (cone contraction for transfer operators); Baladi 2000. Pairwise/mediant oscillation bounds are standard in Hilbert-metric estimates. No prior computation of these specific constants found; not searched beyond that, so novelty of constants is UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a certified sharper constant for this repository's specific operator. Not a world first; no claim made.

## Falsification Attempts
- Independent script `mathematics/scripts/indep_theorem_DD.py` (numpy + mpmath, written from GASKET.md text): 12/12 PASS. Pointwise pairwise maximum over 1601 points is 0.73280560 (below the certified cell bound 0.73437493, as it must be; maximiser word 11111, matching the repo). V_low recomputed 0.5138348942 from e^{±as} at 257 points (agrees). Δ_D, θ_D, θ_D^{1/5}, CF's θ = 0.5441333, ratios at k = 9,14,24,54, C_D = 1.0998298, the floor-form inequality for k = 4..199, and θ_D^{1/5}·r = 0.357370 with r = 0.4237313 from an independent Chebyshev power iteration (|λ₂|/r = 0.17255, matches CG) all reproduced.
- Not independently recomputed: DD.2's interval cell enclosures (my check is pointwise, so it confirms the value is close, not the rigorous upper bound); CF.2's b₅.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_cone.py` EXIT 0 in 23.2 s ("all Theorem DD checks passed"). `pytest tests/test_cli.py -k cone`: 1 passed (22.1 s).

## Mathematical Status
Theorem (proof in repository; certified constants).

## Patent Relevance
None. Mathematical constant for a transfer operator; not a mechanism. Not thrust, not a flux.

## Related Discoveries
DISC-0215 (Theorem DC; DD improves its θ), DISC-0190 (Theorem CF; V_5 replaced), DISC-0188 (Theorem CE; setting), DISC-0205 (CS sharp constant via spectral route, still far better).

## Open Questions
A cone whose Birkhoff rate approaches 0.1725, or a proof that log-Lipschitz cones cannot; the true ratio-of-sums oscillation (between 0.51383 and 0.73438).

## Next Experiments
Certify the float observation that the oscillation term stalls near 0.594 for large n; try weighted/projective-metric cones.

## Reproduction Instructions
In informational-flux-identity @ 1630b8a08515: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_cone.py`. Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DD.py` (≈2 s).

## Evidence Log
- 2026-10-31 ~10:00 EDT: read commit 1630b8a08515 diff; repo witness EXIT 0 (23.2 s); pytest 1 passed; independent 12/12 PASS.

## Change History
- 2026-10-31: created.
