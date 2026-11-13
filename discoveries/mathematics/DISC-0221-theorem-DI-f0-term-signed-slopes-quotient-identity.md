# Discovery: Theorem DI, DH.5's f₀ term recomputed with signed slopes and an exact Hilbert-quotient identity (Θ₁₀₀(f₀, L̃f₀): 0.10465 → 0.064982, floor 0.064975)

## Discovery ID
DISC-0221

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DI.1, an `arb` certificate on 16384 cells for DI.2–DI.3, an outward-padded float cell-pair pass for DI.4, and an `arb` floor). Method KNOWN (the identity DI.1 is the standard explicit form of the Hilbert metric on a log-Lipschitz cone, cf. Liverani 1995; mean-value bounds on cells are routine). Constants UNRESOLVED as to novelty. The contraction rate (0.57117 per level) is unchanged; spectral 0.1725 unchanged.

## Date Discovered
2026-10-31 (indexed ~3:15 PM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit b33223d2efb535bfabd02b3dfc3e7de2329bbaf8 (2026-10-31 14:26:32 EDT).

## Original Evidence
- GASKET.md §Theorem DI (line 4934 onward, 45 added lines); CLAIM_STATUS.md one new row; README.md reproduction list.
- scripts/gasket_fractional_profile_level_f0_coupled.py (new, 337 lines; imports `gasket_fractional_profile_level_birkhoff.py` and its CO/CN dependencies, unchanged).
- tests/test_cli.py `test_theorem_di_profile_level_f0_coupled`; scripts/cli.py registration.

## Discovery
Closes DH's kept limit "Θ_H′ uses DC.2's symmetric slope bounds for f₀, L̃f₀" (also listed as an open question in DISC-0220). Only the constant Θ₁₀₀(f₀, L̃f₀) changes; θ_G, θ_H and the rate are used as stated.
- DI.1 (proved, exact): for R = v/u, Φ_v/Φ_u(x, y) = R(y) + (R(y) − R(x))/(e^{a|x−y|}u(y)/u(x) − 1), so Θ_a(u, v) = log(β/α) with β, α the sup/inf of {R} ∪ {Φ_v/Φ_u}.
- DI.2 (certified): (log F₀)′ ∈ [0.035291, 0.77334], (log L̃F₀)′ ∈ [0.17682, 0.79038]; both functions strictly increasing; L̃f₀ ∈ C_{0.79038} directly (DC.2: C_{1.2791803}); log(sup R₀/inf R₀) < 0.063387 (DC.2: 0.063592701; DC.4 floor 0.0633864).
- DI.3 (certified): DH.1 with signed slopes gives Θ₁₀₀(f₀, L̃f₀) < 0.078489 (cone part 0.0151021 vs DH's 0.0410521).
- DI.4 (certified, float pair pass with outward pads): Θ₁₀₀(f₀, L̃f₀) ≤ Θ_I′ < 0.064982; `arb` floor 0.064975528 from DI.1's one-sided limits at 2049 points. Gap 5.7·10⁻⁶.
- DI.5: level-sum bound |log(s_{k+1}/(r s_k))| ≤ Θ_I′·min(θ_G^{⌊(k−4)/8⌋}, θ_H^{⌊(k−4)/9⌋}), DH.5's bound divided by ≥ 1.6104 at every k ≥ 4.

## Why It Matters
The f₀ constant is now effectively exact (to 5.7·10⁻⁶) within C₁₀₀, so the repository itself concludes that any further improvement of the level-sum bound must come from the contraction θ, not this constant. The extremes sit at the endpoints and in the x → y limit, which is why a coarse grid cannot see them (see my v1 below).

## Derivation
DI.1: Φ_v(x, y) = e^{ad}u(y)R(y) − u(x)R(x) = R(y)Φ_u(x, y) + u(x)(R(y) − R(x)); divide by Φ_u. The Hilbert-metric characterisation (tu − v ∈ closure of C_a iff t ≥ v/u and t ≥ Φ_v/Φ_u) is DH.1's. Floor: as x → y±, Φ_v/Φ_u → R(y)(a ∓ q₁)/(a ∓ q₀) since F₀ is analytic on X_s. Upper bound: denominator ≥ e^{kd} − 1 with k from span slopes of log F₀; numerator by the mean value theorem on R′ = R(q₁ − q₀) or cell sup/inf; x/(e^x − 1) decreasing handles d ≥ gap.

## Assumptions
CF.1 and CF's definition of Θ_a; DG.1(i) (proved in DG); DF.4/DH.5's proofs of CF.3 for a = 100; θ_G < 0.014183 (DG.3) and θ_H < 0.0064696 (DH.4) used as stated, not re-run; CO.1/CO.2 Taylor data and CN.1 box checks re-run unchanged. The DI.4 pair pass is float arithmetic with relative pads 10⁻¹², the same rigour level as DE.2–DH.

## New Results
Θ₁₀₀(f₀, L̃f₀) ∈ (0.064975, 0.064982); L̃f₀ ∈ C_{0.79038}; log(sup R₀/inf R₀) < 0.063387; level-sum constant improved by 1.6104×.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (log-Lipschitz cones; the explicit sup/inf form of the cone's Hilbert metric); Baladi 2000. The quotient identity is an algebraic rearrangement of that explicit form. Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a sharper certified constant for this repository's operator. No first claimed.

## Falsification Attempts
Independent scripts in `mathematics/scripts/indep_theorem_DI_v1.py`, `_v2.py`, `_v3_endpoints.py`. My own code for weights, log-slopes (finite differences), the direct Hilbert quotient (from the definition, not DI.1), one-sided limits and all arithmetic. The one input not rebuilt is the repo's Taylor evaluator for F₀ (`gasket_fractional_profile_level_birkhoff.Taylor`), used as a black box. Not text-only independent.
- v1, 8/11 PASS. Passed: own weights equal the repo's; slope grid ranges (q₀ ∈ [0.035299, 0.773282], q₁ ∈ [0.177152, 0.790313]) inside the certified ranges; q₀, q₁ increasing on a 401-point grid; log(sup R/inf R) = 0.06338649 ∈ [0.0633864, 0.063387); DI.1 identity matches the direct quotient on all 1601² pairs (relative error < 10⁻⁹); DI.3 reconstructed 0.07848860745 (cone 0.015102098); ratio 0.10465/0.064982 = 1.610446. Three FAILs, all from my own test design, not defects in DI:
  - "slope bounds tight to 2·10⁻⁴": the certified lower bound for q₁ (0.17682394) sits 3.3·10⁻⁴ below my finite-difference minimum 0.177152 at s = √5/2. The bound is valid in the safe direction; the threshold was my arbitrary choice.
  - pair grid Θ = 0.06490645 below the floor and β, α off by ~3·10⁻⁵: grid spacing 7.8·10⁻⁴ (a·d = 0.078) cannot reach the x → y limits where the extremes sit. A grid gives a lower bound, so this is not a contradiction.
- v2, 3/4 PASS: my own one-sided limits (second-order finite-difference slopes) at 2049 points give floor 0.064975528, equal to the repo's to 9 digits (β = 0.4347484992, α = 0.4073986432); no near-diagonal pair (|x − y| from 10⁻⁷ to 10⁻¹ at 257 base points) exceeds the certified bound. FAIL: those direct pairs alone reached only 0.064541, because my sampler never put y exactly at an endpoint.
- v3 (endpoint addendum): direct pairs (5/2 − d, 5/2) and (√5/2 + d, √5/2), d from 10⁻⁸ to 10⁻¹, give Θ = 0.064975527 ∈ (0.06497, 0.064982). PASS. So the direct definition reaches the floor, and nothing exceeds the bound.
- Not independently recomputed: the `arb` cell enclosures, the outward pair pass, F₀ itself (CO.1/CO.2), and θ_G, θ_H (taken from DG/DH, which this archive checked in DISC-0219/0220).

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_f0_coupled.py` on a fresh clone at b33223d: EXIT 0 in 116.9 s, no FAIL (β ≤ 0.434749363098 at cell 16383, α ≥ 0.407397144130 at cell 0; Θ_I′ = 0.064981194 ± 4.7·10⁻¹⁰; floor 0.064975528; Θ_I′ − floor ≤ 5.667·10⁻⁶; ratio ≥ 1.61047; s₄..s₁₃ max ratio 0.1991). The pytest wrapper calls the same `main()` and was not rerun this slice.

## Mathematical Status
Theorem (proof and certificate in repository; DI.4 at outward-float rigour).

## Patent Relevance
None. A constant in a contraction estimate for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0220 (Theorem DH; DI closes its kept limit on f₀ slopes), DISC-0219 (DG.1(i) used per orientation), DISC-0215 (DC.2's F₀, R₀; DC.4 floor), DISC-0205 (spectral route 0.1725).

## Open Questions
The joint Hilbert diameter of L̃⁹C₁₀₀ (DI.1 gives an exact starting point; a DE.1-type joint programme is not attempted); a floor for DH's cone term; a cone family whose Birkhoff rate approaches 0.1725.

## Next Experiments
Apply DI.1 to the diameter of L̃⁹C₁₀₀ with a joint sup over (u, v) of R and R′; test second-derivative or projective cones against the 0.570 plateau.

## Reproduction Instructions
In informational-flux-identity @ b33223d: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_f0_coupled.py` (~2 min). Independent: `IFI_SCRIPTS=<ifi>/scripts python3 discoveries/mathematics/scripts/indep_theorem_DI_v2.py` (~90 s) and `..._v3_endpoints.py` (~85 s); v1 kept for the record (~4 min).

## Evidence Log
- 2026-10-31 ~3:15 PM EDT: read commit b33223d message, diff, script header and GASKET.md §DI; checked DI.1's algebra and one-sided limits by hand; repo witness EXIT 0 (116.9 s); independent v1 8/11 (my test design), v2 3/4 (my sampler), v3 PASS; floor reproduced to 9 digits.

## Change History
- 2026-10-31: created.

## Dated note (2026-10-31, ~4:00 PM EDT)
The open question "the joint Hilbert diameter of L̃⁹C₁₀₀" is answered as a floor by Theorem DJ (informational-flux-identity 3c24c1135b02, DISC-0222): 0.013997 < diam ≤ 0.025879, so CF.1-form rates on (C₁₀₀, L̃⁹) stay above 0.53342. No new upper bound. DI's own statements are unchanged. Original text above preserved.
