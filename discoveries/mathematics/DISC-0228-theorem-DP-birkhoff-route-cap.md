# Discovery: Theorem DP, a cap for the whole cone-diameter (Birkhoff) route: every CF.1-form per-level rate on a C¹-open cone is ≥ ρ(L₁)/r > 0.3170757; kept failure DP.3 (spectral 0.1725 unreachable by this route)

## Discovery ID
DISC-0228

## Status
THEOREM in the mathematical sense only (DP.1, DP.2, DP.4 proved in the repository with sympy and `arb`; DP.3 is a certified kept failure, i.e. a proved obstruction). Method KNOWN: DP.2 is the classical fact that Birkhoff's contraction coefficient is at least |μ|/ρ for any real eigenvalue μ of a positive operator with Perron eigenvalue ρ (Birkhoff 1957; Bushell 1973). Constants UNRESOLVED as to novelty. This is a negative result for the route: no further cone-diameter refinement of the DK/DL/DM/DN/DO kind can push the per-level rate below 0.3170757.

## Date Discovered
2026-11-12 (indexed ~8:10 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 7c94df4d7979 (2026-11-12 07:10:47 EST).

## Original Evidence
- GASKET.md §Theorem DP (line 5238 onward, +38 lines; "NOT THIS" disclaimer line 5268); CLAIM_STATUS.md new row (line 124); README.md (+2/−1).
- scripts/gasket_fractional_profile_level_birkhoff_cap.py (new, 210 lines); scripts/cli.py registration; tests/test_cli.py (+27, local only, needs python-flint, sympy).

## Discovery
Answers DISC-0227's kept limit "per-level rate still far from spectral 0.1725".
- DP.1 (sympy): for a cone K of positive functions, h ∈ K, φ h-bounded, Θ_K(h + tφ, h) = log((1 + t s₁)/(1 − t s₀)) exactly, with s₀ = min{s : s h + φ ∈ K̄}, s₁ = min{s : s h − φ ∈ K̄}, s₀ + s₁ ≥ osc(φ/h) > 0.
- DP.2: T h = ρ h, T φ = μ φ (μ real) give τ(T; K) ≥ |μ|/ρ, so tanh(diam T K / 4) ≥ |μ|/ρ.
- DP.3 (kept failure, witness CI.4/CM.3's real C¹ eigenfunctions, CI.1 re-run in `arb`): on every C_a with a > b* = 1.688416, every block L̃ⁿ or mixed blocks, and every invariant cone with C¹ in V_h̃, τ(L̃ⁿ) ≥ (ρ(L₁)/r)ⁿ, so every CF.1-form per-level rate is ≥ ρ(L₁)/r ∈ [0.3170757, 0.3170762]. DM.5's 0.363655 is < 1.1469 × cap; DK.4's 0.53349 < 1.6825 × cap; spectral |λ₂|/r = 0.1725476 lies below the cap by a factor > 1.8376.
- DP.4 (CM.4): with the λ₂-eigenfunction in V_h̃ the floor is |λ₂|/r; for V_h̃ ⊂ C² DP's mechanism gives nothing more (ρ(L₂)/r < 0.101646), so the cap is a C¹ phenomenon.
- Observation only: (D₉/D₇)^{1/2} ∈ [0.317569, 0.317601] on C₂, i.e. the measured diameter ratios already sit near the cap.

## Why It Matters
It closes the line of work DISC-0219..0227: the certified per-level rate on C¹-open cones cannot go below ≈0.3171, and the current 0.363655 is within 15% of that. Reaching the spectral 0.1725 needs a different cone class (C²-type order unit) or a different method, not more blocks or cover work.

## Derivation
Hand-checked this slice: for the positive cone, u/v = 1 + tφ/h, so Θ = log((1 + t max φ/h)/(1 + t min φ/h)), which is DP.1 with s₁ = max φ/h, s₀ = −min φ/h. DP.2 follows because T(h + tφ) = ρ(h + t(μ/ρ)φ), and by DP.1 the ratio Θ(h + tqφ, h)/Θ(h + tφ, h) → |q| as t → 0. Ratios 0.363655/0.3170757 = 1.14690, 0.53349/0.3170757 = 1.68253, 0.3170757/0.1725476 = 1.83761 (all match).

## Assumptions
CF.1–CF.3, CI.4, CM.3/CM.4, CG.3 as stated; CI.1 and CL.3 re-run by the script. That CM.3's statement "every real |μ| < ρ(L₁) is a C¹ eigenvalue" holds is taken from the repository (DISC-0205 era), not re-derived here.

## New Results
None beyond the repository's. Minor rounding note: the script prints 4 artanh(q⁵) < 0.0128197 using the lower end of q; with q's upper enclosure 0.317076185 the value is 0.01281975, about 5·10⁻⁸ above the printed number. The consistency conclusion (well below DL.3's floor 0.0435818) is unaffected.

## Prior Art
Birkhoff 1957 (contraction coefficient τ = tanh(Δ/4)); Bushell 1973 (Hilbert metric, eigenvalue lower bound for τ); Seneta, Non-negative Matrices and Markov Chains (coefficient of ergodicity ≥ |λ₂|/λ₁); Liverani 1995; Baladi 2000. Specific constants for this gasket operator: none found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. The contribution is an explicit certified cap for this operator's cone route and the identification that it is a C¹ phenomenon. No first claimed.

## Falsification Attempts
Independent script `mathematics/scripts/indep_theorem_DP.py` (numpy only, none of DP's code):
- DP.1 on the positive-function cone: 2000 random (h, φ, t) triples, identity holds to 1e−12 and s₀ + s₁ ≥ osc(φ/h). PASS.
- DP.2: 300 random positive 6×6 matrices, Birkhoff τ = tanh(diam/4) computed from column ratios is ≥ |μ|/ρ for every real non-Perron eigenvalue. PASS.
- 4 artanh(qⁿ) at q's upper end: n = 5, 7, 9 give 0.01282, 0.001289, 0.0001296, all below the repo floors 0.0435818, 0.0044106, 0.00044485. PASS.
- Not independently recomputed: CI.1/CL.3 `arb` intervals for ρ(L₁), ρ(L₂), CM.3/CM.4's spectral statements, the D₇/D₉ enclosures.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_birkhoff_cap.py` at 7c94df4: EXIT 0 in 1.3 s, "all Theorem DP checks passed". pytest not rerun.

## Mathematical Status
Theorem (proof in repository) plus a proved obstruction (DP.3).

## Patent Relevance
None. Contraction bounds for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0227 (kept limit answered), DISC-0225/0226 (rate 0.363655 shown within 1.147 of cap), DISC-0223 (DK.4 rate within 1.6825), DISC-0205 (spectral 0.1725, now shown out of reach for this route).

## Open Questions
A C²-type invariant cone with a certified diameter; whether τ(L̃ⁿ; C₂)^{1/n} → ρ(L₁)/r; Stage 2 (no Ψ_info).

## Next Experiments
Construct a cone whose order-unit space excludes the C¹ eigenfunctions (DP.4's C² hint) and certify one block diameter; check numerically whether the C₂ diameter ratios converge to 0.3170757.

## Reproduction Instructions
In informational-flux-identity @ 7c94df4: `pip install python-flint sympy numpy`, `python3 scripts/gasket_fractional_profile_level_birkhoff_cap.py` (~1 s). Archive check: `python3 discoveries/mathematics/scripts/indep_theorem_DP.py` (~1 s, standalone).

## Evidence Log
- 2026-11-12 ~8:05 AM EST: read commit 7c94df4 message, file list, GASKET.md section header, CLAIM_STATUS row; repo witness EXIT 0 (1.3 s); independent checks PASS.

## Change History
- 2026-11-12: created.
