# Discovery: Theorem DM, a corner box bound makes longer blocks on C₂ cheap to cover (0.0044106 < diam_Θ₂ L̃⁷C₂ ≤ 0.004411; 0.00044485 < diam_Θ₂ L̃⁹C₂ ≤ 0.0004449; per-level rate < 0.363655; |μ| < 0.15410)

## Discovery ID
DISC-0225

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DM.1, `arb` jets for DM.2, `arb` floors for DM.3 and `arb` arithmetic for DM.5, and an outward-rounded float cover for DM.4). Method KNOWN (convexity chord/tangent bounds plus monotonicity of linear-fractional functions, applied inside DK.1's generator reduction from DISC-0223 and DL's cone from DISC-0224). Constants UNRESOLVED as to novelty. Certification standard: cover and word tables are outward-padded floats checked against `arb` at sample centres (repo's kept limit, same as DE.2–DL.4). The n = 9 case is certified only by a local ~33 min run (`DM_N=9`), not in CI and not rerun here.

## Date Discovered
2026-11-12 (indexed ~4:05 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 80fa08242cd4 (2026-11-12 03:07:46 EST).

## Original Evidence
- GASKET.md §Theorem DM (line 5108 onward, +51 lines); CLAIM_STATUS.md new row (line 121); README.md (+2).
- scripts/gasket_fractional_profile_level_chord_cover.py (new, 309 lines; imports DL's script as a module); scripts/cli.py registration; tests/test_cli.py (+42 lines, n = 7 local only, `DM_SLOW=1` for n = 9).

## Discovery
Answers DISC-0224's kept limit "longer blocks only floats: the box pad scales with h, not D".
- DM.1 (proved): on a box of half-width h, log C^(s,±)_w = l + gδ + R with |R| ≤ G₂h²/2; with x = g − μ, convexity gives e^{xδ} ≤ cosh(xh) + (δ/h)sinh(xh) (chord) and e^{xδ} ≥ 1 + xδ (tangent). Each quotient N_i/D_i is then affine/affine in δ_i, hence monotone, so the box supremum is attained at one of 4 corners: bound 4K + max_(ε₁,ε₂)[ρ^(ε)(1,2) + ρ^(ε)(2,1)], K = a s_b h + G₂h²/2. The only first-order pad left is 4 a s_b h; DK.3's 2h max|g − μ| becomes a second-order x²h²/2 gap.
- DM.2 (`arb`, 128 balls): n = 7: |b_w′| < 5.80·10⁻⁴; n = 9: |b_w′| < 6.45·10⁻⁵; |(log C_w)″| < 8.80; a + sλ_w ± a|b_w′| > 1.081; L̃ⁿC₂ ⊂ C₀.₉₁₉₆.
- DM.3 (`arb`): floors Θ₂ ≥ 0.004410643 (n = 7), ≥ 0.000444861 (n = 9).
- DM.4 (cover, outward DP): n = 7, 31351 boxes (DL's trial at 0.0045 needed 2245300): 0.0044106 < diam ≤ 0.004411; n = 9, 268292 boxes: 0.00044485 < diam ≤ 0.0004449.
- DM.5 (`arb`): n = 7 rate < 0.378005, |μ| < 0.16018; n = 9 rate < 0.363655 (floor > 0.363650, pair exhausted), |μ| < 0.15410 (DL.5: 0.404994, 0.17161).

## Why It Matters
The cost reduction (31351 vs ~2.2 million boxes at n = 7) turns DISC-0224's float trend for n = 7, 9 into certified bounds, matching that trend (0.378, 0.364). It also confirms the CF.1 route on C₂ is plateauing (diameter ratio ≈ 0.3175 per level, floats), still far above the spectral 0.1725.

## Derivation
Hand-checked this slice: the chord bound is the secant of the convex e^{xδ} on [−h, h]; the tangent bound is e^y ≥ 1 + y; a product/quotient of positive affine functions of δ_i, separately in each δ_i, is linear-fractional and so monotone, giving corner attainment (needs positive denominators, i.e. |x|h < 1, which the repo's tangent clause states). Arithmetic: tanh(0.004411/4) = 0.0011027496, 7th root 0.37800426; tanh(0.0044106/4)^{1/7} = 0.37799937; × r (0.4237312870) = 0.16017223. tanh(0.0004449/4) = 0.000111225, 9th root 0.36365466; floor 9th root 0.36365012; × r = 0.15409186.

## Assumptions
CF's Θ_a, CF.1, CF.3/CF.5; DJ.2's floor construction (DISC-0222); DK.1 (DISC-0223); DL.1's cone step (DISC-0224); CE.4's r; float word tables and DP outward-padded (kept limit); G₂ and s_b bounds from the repo's `arb` jets (not recomputed with intervals here).

## New Results
0.0044106 < diam_Θ₂ L̃⁷C₂ ≤ 0.004411; 0.00044485 < diam_Θ₂ L̃⁹C₂ ≤ 0.0004449; per-level rate in (0.363650, 0.363655) on (C₂, L̃⁹); |μ| < 0.15410 for every other C¹ eigenvalue.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Baladi 2000. Chord/tangent bounding of convex exponentials and vertex attainment for linear-fractional objectives on boxes are textbook (convexity; linear-fractional programming, Charnes–Cooper 1962). Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a cheaper certified cover and new (a, n) enclosures. No first claimed.

## Falsification Attempts
Independent script `mathematics/scripts/indep_theorem_DM.py` (numpy only, no repo import; DISC-0224's script parameterised by n, plus a randomised DM.1 lemma test). v1 8/9: the lemma test FAILED because my random instances allowed non-positive denominators (my test bug, outside DM.1's hypotheses); v2 with positive denominators 9/9 PASS for both n:
- n = 7 (35 s): sampled sup|b_w′| = 5.794·10⁻⁴ (< 5.80·10⁻⁴, tight); eight endpoint corners, max (−,−) = 0.0044106519 inside (0.0044106, 0.004411]; 2145-pair search max equals that corner; DM.5 arithmetic matches.
- n = 9 (32 s, 561 pairs): sup|b_w′| = 6.437·10⁻⁵ (< 6.45·10⁻⁵); max (−,−) corner 0.0004448617 inside (0.00044485, 0.0004449]; search max equals it; DM.5 arithmetic matches.
- Chord/tangent inequalities and 4-corner maxima: 0 failures in 20000 random instances.
- Not independently recomputed: the outward cover, the `arb` jets, the n = 9 repo cover (33 min).
- Note: the script's first check label still says "32 images" (cosmetic); it tests 2ⁿ images.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_chord_cover.py` at 80fa082 (n = 7 default): EXIT 0 in 53.0 s, all checks ok (31351 boxes, every accepted box ≤ 0.004410946, depths 6/11/6; θ_M ≤ [0.0011027496 ± 4.7·10⁻¹¹]; rate ≤ [0.37800426 ± 3.8·10⁻⁹]; floor rate ≥ [0.37799989 ± 2.5·10⁻⁹]; |μ| ≤ [0.16017223 ± 3.2·10⁻⁹]; CE.4 r re-certified). `DM_N=9` and pytest not rerun this slice.

## Mathematical Status
Theorem (proof in repository; cover in outward-padded floats with `arb` spot checks). n = 9 rests on the repo's local run, which this archive has not reproduced.

## Patent Relevance
None. A contraction bound for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0224 (kept limit answered; float trend now certified at n = 7, 9), DISC-0223 (DK.3's cover pad replaced), DISC-0222 (DJ.2 floor construction reused), DISC-0205 (spectral 0.1725 still out of reach).

## Open Questions
A cone family or block reaching 0.1725; full interval cover; carrying DK.4's level-sum bound to C₂; optimising a below 2.

## Next Experiments
Run `DM_N=9` once (~33 min) to reproduce the n = 9 cover; extend indep_theorem_DM.py's corner search over a ∈ [1.69, 3] to map the plateau.

## Reproduction Instructions
In informational-flux-identity @ 80fa082: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_chord_cover.py` (~1 min); `DM_N=9 python3 scripts/gasket_fractional_profile_level_chord_cover.py` (~33 min). Independent: `N=7 python3 discoveries/mathematics/scripts/indep_theorem_DM.py`; `N=9 K=9 python3 ...` (~35 s each, numpy only).

## Evidence Log
- 2026-11-12 ~4:00 AM EST: read commit 80fa082 message, file list, script docstring and CLAIM_STATUS row; hand-checked DM.1's convexity/monotonicity argument and DM.5 arithmetic; independent check v1 8/9 (my test bug), v2 9/9 at n = 7 and n = 9; repo witness EXIT 0 (53.0 s).

## Change History
- 2026-11-12: created.
- 2026-11-12 ~5:05 AM EST (dated note): informational-flux-identity 928bc79323cc (Theorem DN, DISC-0226) carries DK.4's level-sum bound to C₂, answering the open question "carrying DK.4's level-sum bound to C₂"; its commit message reports a clean DM_N=9 re-run by the repo author (268292 boxes, diam ≤ 0.000444899, unchanged numbers). This archive still has not reproduced the n = 9 cover. Original text above preserved.
