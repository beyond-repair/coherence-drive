# Discovery: Theorem DJ, exact separation of the Hilbert diameter of L̃⁹C₁₀₀ and a certified floor (0.013997 < diam ≤ Δ_H < 0.025879; per-level rate of CF.1 form cannot go below 0.53342)

## Discovery ID
DISC-0222

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DJ.1 and DJ.3 and an `arb` 200-bit certificate for DJ.2). Method KNOWN (the dual description of the Hilbert metric by positive functionals and lower bounds on a projective diameter from explicit test pairs are standard; cf. Birkhoff 1957, Bushell 1973, Liverani 1995). Constants UNRESOLVED as to novelty. No new upper bound: θ_H < 0.0064696 and the rate 0.57117 per level are unchanged; spectral 0.1725 unchanged.

## Date Discovered
2026-10-31 (indexed ~4:00 PM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3c24c1135b02 (2026-10-31 15:10:17 EDT).

## Original Evidence
- GASKET.md §Theorem DJ (line 4979 onward, 44 added lines); CLAIM_STATUS.md one new row; README.md reproduction list.
- scripts/gasket_fractional_profile_level_joint_diameter.py (new, 273 lines); scripts/cli.py registration; tests/test_cli.py new test (+23 lines).

## Discovery
Closes DI's kept limit "DI.1 not applied to the diameter of L̃⁹C₁₀₀" and DH's kept limit "no floor for the cone term" (both open questions in DISC-0220/0221), as a floor only.
- DJ.1 (proved, exact): with functionals ℓ_y(u) = u(y) and ℓ_(x,y)(u) = e^{a|x−y|}u(y) − u(x), diam_Θa L̃ⁿC_a = sup over pairs (P₁, P₂) of ρ(P₁, P₂) + ρ(P₂, P₁), where ρ(P, P′) = sup over f ∈ C_a of log(ℓ_P(L̃ⁿf)/ℓ_P′(L̃ⁿf)). Each ρ is a signed ratio programme on at most 4·2ⁿ image points with a bang-bang maximiser. DE/DF's W is the restriction to point functionals.
- DJ.2 (certified, `arb`): explicit bang-bang f, g at P₁ = (5/2 − 10⁻⁶, 5/2), P₂ = (√5/2, √5/2 + 10⁻⁶) give Θ₁₀₀(L̃⁹f, L̃⁹g) ≥ 0.013998061 > 0.013997, so 0.013997 < diam L̃⁹C₁₀₀ ≤ Δ_H < 0.025879 (DH.3's diagonal floor was 0.013764).
- DJ.3: every CF.1 factor tanh(Δ/4) with Δ ≥ diam is > 0.0034992, so every per-level rate of this form for (a, n) = (100, 9) is > 0.53342.
- Remark in the repo, explicitly an assumption: under Birkhoff–Hopf the true contraction coefficient lies in [0.0034992, 0.0064696].
- Float observation in the repo, explicitly not certified: diam ≈ 0.013998, which would put the rate near 0.5335.

## Why It Matters
It turns the open-ended "sharpen the diameter" programme into a bounded one: on this cone and block, any diameter improvement can move the rate from 0.57117 to at best 0.53342, so the repository's own target (spectral 0.1725) cannot be reached by this route. That is a negative result about the method, stated precisely.

## Derivation
By DI.1's characterisation, tu − v ∈ closure(C_a) iff t ≥ ℓ_P(v)/ℓ_P(u) for every P, so β = sup_P ℓ_P(v)/ℓ_P(u), α = inf_P, and Θ_a(u, v) = sup_{P₁,P₂}[log ℓ_P₁(v)/ℓ_P₂(v) + log ℓ_P₂(u)/ℓ_P₁(u)]. With u = L̃ⁿf, v = L̃ⁿg and f, g independent in C_a, the sup over (f, g) splits into ρ(P₁, P₂) + ρ(P₂, P₁). I checked this algebra by hand; the exchange of suprema is valid because f and g enter separate terms. Positivity of ℓ_(x,y)(L̃ⁿf) needs L̃ⁿC₁₀₀ ⊂ C_b with b < a, supplied by DF.1(i)/DH.2. DJ.3 is monotonicity of tanh plus (0.0034992)^{1/9} = 0.53347.

## Assumptions
CF's definition of Θ_a and CF.1 (Birkhoff contraction); DI.1 (proved in DI, DISC-0221); DF.1(i) and DH.2 cone inclusions; DH.4's Δ_H < 0.025879 and θ_H < 0.0064696 and DH.3's floor 0.013764 used as stated (DH's script not re-run by DJ). The Birkhoff–Hopf remark is an assumption and not part of the theorem.

## New Results
0.013997 < diam_Θ₁₀₀ L̃⁹C₁₀₀ < 0.025879; CF.1-form factor for (100, 9) ≥ 0.0034992; per-level rate of that form > 0.53342.

## Prior Art
Birkhoff 1957; Bushell 1973 (Birkhoff–Hopf); Eveson–Nussbaum 1995; Liverani 1995 (log-Lipschitz cones and the explicit functional form of their Hilbert metric); Baladi 2000. The separation into a two-functional programme is a direct consequence of the dual description. Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a certified floor and a precise cap on what this route can achieve for the repository's operator. No first claimed.

## Falsification Attempts
Independent scripts `mathematics/scripts/indep_theorem_DJ.py` and `indep_theorem_DJ_v2_norm.py`: own weights w₁ = (s+½)/(2s(7/2−s)), w₂ = (s−½)/(2s(s+7/2)), own maps σ₁ = √(15/4 − s), σ₂ = √(15/4 + s), own 9-fold image expansion, own backward-recursion ratio programme with bisection, all in floats. No repository import (fully independent of the repo's code, not of its definitions).
- v1, 5/6 PASS. All 512 images of L̃⁹ lie in X_s. My programme at DJ.2's pairs gives sum 0.013998076 > 0.013997 (repo's explicit f, g: 0.013998061; the gap is consistent with the repo's slopes a(1 − 10⁻⁶) sitting just inside the sup). Sum below Δ_H. DJ.3 arithmetic: tanh(0.013997/4) = 0.00349924, ninth root 0.533468. Point pair (5/2, √5/2) gives 0.0137650, matching DH.3's diagonal floor 0.013764, and is below the near-diagonal end pairs. A search over 75 other pairs (60 random, 15 structured end pairs with d from 10⁻⁸ to 10⁻³) found max 0.013998094, nothing above Δ_H and nothing materially above the repo's float estimate 0.013998. One FAIL from my own test design: the individual ρ values depend on how each functional is scaled (only the sum is invariant), and my unnormalised values (0.53166, −0.51766) could not match the repo's.
- v2 addendum, PASS: normalised against the constant function, my ρ(P₁, P₂) = 0.0070018 and ρ(P₂, P₁) = 0.0069963 equal the repo's to 7 digits.
- Not independently recomputed: the `arb` enclosures of DJ.2 and the upper bound Δ_H (taken from DH, checked in DISC-0220). My search is a float sample, so it supports but does not certify the float observation diam ≈ 0.013998.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_joint_diameter.py` on a fresh clone at 3c24c11: EXIT 0 in 0.45 s, all checks ok (Θ ≥ [0.013998061 ± 4.67·10⁻¹⁰]; margin over DH.3 floor [0.00023406 ± 1.5·10⁻⁹]; factor ≥ 0.0034995010; rate ≥ 0.53347220). The pytest wrapper was not rerun this slice.

## Mathematical Status
Theorem (proof and `arb` certificate in repository). The diameter ≈ 0.013998 and the Birkhoff–Hopf interval are not theorems.

## Patent Relevance
None. A bound in a contraction estimate for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0221 (DI.1 used; DI's kept limit closed as a floor), DISC-0220 (DH.3/DH.4 floor and upper bound; its cone-term floor question answered), DISC-0217/0218 (DE.1/DF's W is DJ.1 restricted to points), DISC-0205 (spectral 0.1725, now shown out of reach on this cone and block).

## Open Questions
A certified upper bound by DJ.1 (outward cover of (x₁, y₁, x₂, y₂) normalised as d → 0), worth at most 0.57117 → 0.53342; whether Birkhoff–Hopf holds for this cone; another cone family or block for any approach to 0.1725.

## Next Experiments
Run DJ.1's programme for other (a, n) to map the floor of CF.1-form rates as a function of a and n; check whether that floor tends to 0.1725 as n grows.

## Reproduction Instructions
In informational-flux-identity @ 3c24c11: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_joint_diameter.py` (< 1 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DJ.py` (~13 s, numpy only) then `python3 indep_theorem_DJ_v2_norm.py` from the same folder.

## Evidence Log
- 2026-10-31 ~4:00 PM EDT: read commit 3c24c11 message, file list and GASKET.md §DJ; checked DJ.1's separation and DJ.3's arithmetic by hand; repo witness EXIT 0 (0.45 s); independent v1 5/6 (one FAIL from my normalisation), v2 PASS.

## Change History
- 2026-10-31: created.
