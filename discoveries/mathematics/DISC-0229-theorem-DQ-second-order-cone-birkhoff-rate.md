# Discovery: Theorem DQ, the Birkhoff rate of a cone is the spectral radius of its order-unit space: C_a attains the C¹ cap ρ(L₁)/r, and the invariant second-order cone K_(2,6) tends to the spectral rate |λ₂|/r = 0.1725476; kept failure DQ.5 (blocks n ≤ 3 on K_(2,6) stay above the cap, threshold n₀ not effective)

## Discovery ID
DISC-0229

## Status
THEOREM in the mathematical sense only (DQ.1 by sympy and `arb`; DQ.2–DQ.4 by textbook Fredholm/Riesz/Gelfand arguments written out in the repository, resting on earlier repo results CJ/CK, CM.4, CF.1–CF.3); DQ.5 is a certified kept failure. Method KNOWN: that the asymptotic Birkhoff contraction rate of a positive operator equals the spectral ratio on the cone's order-unit space, and that C^k-type cones see the C^k essential spectral radius, is classical (Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012; Baladi 2000 for C^k essential radii). Constants UNRESOLVED as to novelty. Limits only: no certified diameter D_n on K_(2,6), so no certified rate improvement over DISC-0225's 0.363655 yet.

## Date Discovered
2026-11-12 (indexed ~9:05 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 011624344923 (full 0116243449233838aeeb8214c516741e83fd75d3, 2026-11-12 08:38:37 EST).

## Original Evidence
- GASKET.md §Theorem DQ (line 5276 onward, +44 lines; "NOT THIS" disclaimer line 5311); CLAIM_STATUS.md new row (line 125); README.md (+2/−1).
- scripts/gasket_fractional_profile_level_second_order_cone.py (new, 439 lines; imports CI.1 and CL.3 modules and re-runs them); scripts/cli.py registration; tests/test_cli.py (+26, local only, needs python-flint, sympy).

## Discovery
Answers DISC-0228's two open items ("a C²-type invariant cone" and "whether τ(L̃ⁿ; C₂)^{1/n} → ρ(L₁)/r").
- DQ.1: (L̃f)'' = M₂f'' + Σ[w̃ᵢ'' f∘σᵢ + (2w̃ᵢ'σᵢ' + w̃ᵢσᵢ'') f'∘σᵢ]; the cone K_(2,6) = {f > 0 : |f'| ≤ 2f, |f''| ≤ 6f} maps into K_(a',b') with a' < 1.8280, b' < 5.149 (every K_(2,b), b ≥ 4.936, invariant); h̃ interior, V_h̃ = W^{2,∞}.
- DQ.2: on W^{k,∞}, L̃ = (0 ⊕ M_k) + compact with ρ(M_k) ≤ ρ(L_k); eigenfunctions with |μ| > ρ(L_k) are C^k; r simple. So the non-Perron spectral radius is ρ(L₁) on W^{1,∞} and |λ₂| on W^{2,∞} (ρ(L₂) ≤ 0.0430704 < |λ₂|).
- DQ.3: on every C_a, a > b*, lim τ^{1/n} = lim D_n^{1/n} = ρ(L₁)/r ∈ [0.317075713, 0.317076185]: DISC-0228's cap is attained.
- DQ.4: on K_(2,6) the limit is |λ₂|/r ∈ [0.1725475, 0.1725477], below the cap by > 1.83761, so some n₀ has tanh(D_n/4)^{1/n} < 0.3170757 for all n ≥ n₀.
- DQ.5 (kept failure, `arb`): τ(L̃ⁿ; K_(2,6))^{1/n} ≥ 0.5523034, 0.3922673, 0.3221097 for n = 1, 2, 3, so n₀ ≥ 4; n₀ not effective.
- Observation only (floats, not certified): near-h̃ per-level ratios 0.28560, 0.25942, 0.24259 at n = 4, 5, 6.

## Why It Matters
It turns DISC-0228's negative result into a route: the C¹ cap is exactly the C¹ essential radius, and moving to a second-order cone removes it in the limit. The open engineering step is now a certified D_n on K_(2,6) for some n ≥ 4.

## Derivation
Checked this slice: DQ.1's second-derivative formula is the chain rule for w(x) f(σ(x)) (sympy with generic w, σ, f, PASS), and σ'² = 1/(4σ²) holds for σ = √(c ∓ s). The DQ.3/DQ.4 argument is: τ ≥ spectral ratio by DP.2, and τ ≤ tanh(D_n/4) with D_n ≲ C‖L̃ⁿ(1 − Π)‖/rⁿ in the order-unit norm of V_h̃, whose n-th root tends to the non-Perron spectral radius on that space by Gelfand. Consistency: implied r from ρ(L₁)'s interval is [0.4237307, 0.4237319] and from |λ₂|/r it is 0.4237313, inside. Cap/limit 0.3170757/0.172547602 = 1.837613. DQ.5 roots: 0.1538736^{1/2} = 0.3922673, 0.03342037^{1/3} = 0.3221097.

## Assumptions
CF.1–CF.3, CG.3, CJ/CK, CM.4 and DP.1–DP.3 as stated in the repository; CI.1 and CL.3 re-run by the script. The bootstrap and compact-perturbation steps of DQ.2 are written in prose in GASKET.md and the docstring, with only the J = 4 algebraic identity checked by sympy; I did not re-derive the compactness of K_k.

## New Results
None beyond the repository's. One check that could have broken DQ.4 and did not: the repo's own float observation reports M₁'s top eigenvalue −0.08337 on smooth functions (|·|/r = 0.1968 > 0.1725). If that were an eigenvalue of L̃ on W^{2,∞}, DQ.4's limit would be 0.1968, not 0.1725. An independent Chebyshev collocation of L̃ itself (N = 30, 50, 80) gives the spectrum 0.4237313, −0.0731138, −0.0170676, … with no eigenvalue near −0.0834, so M₁'s eigenvalue is not one of L̃'s and DQ.4's |λ₂| stands (float evidence only).

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (cone contraction and decay of correlations); Lemmens & Nussbaum, Nonlinear Perron–Frobenius Theory (2012); Baladi 2000 and Ruelle 1990 (essential spectral radius of transfer operators on C^k is governed by the k-th derivative weights). Specific constants for this gasket operator: none found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. The contribution is the explicit invariant second-order cone for this operator, the identification of both limits, and certified lower bounds for n ≤ 3. No first claimed.

## Falsification Attempts
Archive script `mathematics/scripts/indep_theorem_DQ.py` (sympy and numpy, none of DQ's code):
- DQ.1 chain-rule identity with generic functions: PASS; σ'² = 1/(4σ²): PASS.
- Finite analog of DQ.3/DQ.4: 50 random positive 5×5 matrices, tanh(D_n/4)^{1/n} against |λ₂|/λ₁; median relative gap 0.337, 0.216, 0.130, 0.089, 0.060 at n = 4, 6, 9, 12, 15 (decreasing toward 0, as Gelfand predicts; slow, which matches DQ.5's non-effective n₀).
- Spectrum of L̃ and M₁ by Chebyshev collocation from the CE/CF formulas: r = 0.4237313, λ₂ = −0.0731138 stable in N; M₁'s −0.083371 is not in L̃'s spectrum. PASS.
- Arithmetic of DQ.4/DQ.5 and ρ(L₂) < |λ₂| < ρ(L₁): PASS.
- Not independently recomputed: the 20000-ball `arb` invariance cover (a' < 1.8280, b' < 5.149), the 8000-cell DQ.5 oscillation bounds, the min ℓ(p) ≥ 0.843413 base check, CI.1/CL.3 intervals.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_second_order_cone.py` at 0116243: EXIT 0 in about 8.7 s wall (script reports 7.9 s), "all Theorem DQ checks passed". pytest and the DQ_LP=1 float LP not rerun.

## Mathematical Status
Theorem (proof in repository, limits only) plus a certified kept failure (DQ.5).

## Patent Relevance
None. Contraction rates for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0228 (both open items answered; cap shown attained), DISC-0225 (DM ratios ~0.3176 identified as converging to the cap), DISC-0205 (spectral 0.1725 now reachable in the limit on K_(2,6)).

## Open Questions
A certified D_n on K_(2,6) (or another second-order cone) for some n ≥ 4 below the cap; an effective n₀; optimising b; Stage 2 (no Ψ_info).

## Next Experiments
Certify the float ratios 0.28560/0.25942/0.24259 (n = 4..6) with an `arb` cover of L̃ⁿK_(2,6); then carry a CF.3-form level-sum bound to K_(2,6).

## Reproduction Instructions
In informational-flux-identity @ 0116243: `pip install python-flint sympy numpy`, `python3 scripts/gasket_fractional_profile_level_second_order_cone.py` (~8 s). Archive check: `python3 discoveries/mathematics/scripts/indep_theorem_DQ.py` (~1 s, standalone, sympy + numpy).

## Evidence Log
- 2026-11-12 ~9:00 AM EST: read commit 0116243 message, file list, script docstring, GASKET.md section header, CLAIM_STATUS row; repo witness EXIT 0; independent checks PASS.

## Change History
- 2026-11-12: created.
