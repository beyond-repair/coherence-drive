# Discovery: Theorem DK, certified upper bound for the Hilbert diameter of L̃⁹C₁₀₀ (0.013997 < diam ≤ 0.014000; per-level rate < 0.53349, so the (C₁₀₀, L̃⁹) route is exhausted)

## Discovery ID
DISC-0223

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DK.1, `arb` jets for DK.2 and DK.4, and an outward-rounded float cover for DK.3). Method KNOWN (the Hilbert metric of a cone defined by a family of positive functionals is computed by those functionals, here the cone's own generators m^±_t(u) = a u(t) ± u′(t); ratio-of-integrals ≤ sup of pointwise ratios; branch-and-bound cover). Constants UNRESOLVED as to novelty. Certification standard: DK.3's cover is outward-padded floats checked against `arb` at sample centres, not fully interval arithmetic (the repo states this as a kept limit, same standard as DE.2–DH.3).

## Date Discovered
2026-11-12 (indexed ~1:15 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 261803687762 (2026-11-12 00:39:42 EST).

## Original Evidence
- GASKET.md §Theorem DK (line 5023 onward, 46 added lines); CLAIM_STATUS.md one new row; README.md reproduction list.
- scripts/gasket_fractional_profile_level_diameter_cover.py (new, 408 lines); scripts/cli.py registration; tests/test_cli.py (+25 lines).

## Discovery
Closes DJ's kept limit "no certified upper bound by DJ.1" (open question in DISC-0222).
- DK.1 (proved): ℓ_(x,y)(u) = ∫ e^{a|τ−x|} m^±_τ(u) dτ (sign + for y > x, − for y < x) and u(y) = (m⁺ + m⁻)/(2a), so every DJ.1 quotient is bounded by quotients of m^s_t; with |f′| ≤ a f, explicit word-wise bounds M^∓_(t,s)(f) ≤ m^s_t(L̃⁹f) ≤ M^±_(t,s)(f) with C^{s,±}_w = W_w(a + sλ_w ± a|b_w′|); diam ≤ sup over Q₁, Q₂ ∈ X_s × {±} of ρ̃(Q₁,Q₂) + ρ̃(Q₂,Q₁). Two parameters instead of DJ.1's four.
- DK.2 (`arb`, 128 balls): |b_w′| < 6.46·10⁻⁵, |(log C_w)″| < 1.89, a + sλ_w ± a|b_w′| > 99.
- DK.3 (adaptive dyadic cover, 266116 boxes, outward DP): diam_Θ₁₀₀ L̃⁹C₁₀₀ ≤ 0.014000; with DJ.2, 0.013997 < diam ≤ 0.014000 (width 3·10⁻⁶; DH.4 was 0.025879).
- DK.4 (`arb`): θ_K ≤ 0.0034999857 < 0.0035000; per-level rate ≤ 0.53348041 < 0.53349 (DH.4: 0.57117; DJ.3 floor 0.53342); every other C¹ eigenvalue |μ| < 0.22606 (DH.5: 0.24203); DI.5's level-sum bound improved by factors 1.85…861 at k = 13…103.
- Float observation (not certified): relaxed corner ((5/2,+),(√5/2,+)) = 0.01399809, within 4·10⁻⁸ of DJ.2's floor; dropping the f′ term gives 0.01382 (below the floor, so the term is needed).

## Why It Matters
With DJ.3 it pins the best CF.1-form rate for (C₁₀₀, L̃⁹) into (0.53342, 0.53349). That is a closed negative result for this route: the repo's spectral target 0.1725 needs a different cone family or block. The reduction itself applies verbatim to other (a, n).

## Derivation
Checked by hand this slice: for τ > x, d/dτ[e^{a(τ−x)}u(τ)] = e^{a(τ−x)}(au + u′) = e^{a(τ−x)}m⁺_τ(u); integrating from x to y gives e^{a(y−x)}u(y) − u(x) = ℓ_(x,y)(u). For y < x, d/dτ[e^{a(x−τ)}u(τ)] = −e^{a(x−τ)}m⁻_τ(u), giving the m⁻ form. Both kernels are positive, so ℓ_P(v)/ℓ_P(u) ≤ sup_τ m_τ(v)/m_τ(u) (mediant inequality), and point functionals are the average (m⁺ + m⁻)/(2a). Hence β(u, v) and 1/α(u, v) are each bounded by m-quotients, giving diam ≤ sup_{Q₁,Q₂}[ρ̃ + ρ̃]. This is the standard fact that m^±_t generate the dual of C_a = {|u′| ≤ a u}. DK.4 arithmetic: tanh(0.014/4) = 0.0034999857, ninth root 0.53348041 (recomputed at 30 digits).

## Assumptions
CF's definition of Θ_a and CF.1 (Birkhoff contraction); DJ.1 and DJ.2's floor (DISC-0222); DF.1(i), DH.2 cone inclusions; DG.3's θ_G and DI.4's Θ_I′ (used in DK.4's eigenvalue and level-sum consequences); float word tables and DP outward-padded (kept limit).

## New Results
0.013997 < diam_Θ₁₀₀ L̃⁹C₁₀₀ ≤ 0.014000; CF.1 factor < 0.0035000; per-level rate in (0.53342, 0.53349); |μ| < 0.22606 for every other C¹ eigenvalue.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (log-Lipschitz cones; the Hilbert metric through the cone's defining functionals); Baladi 2000. Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a certified two-sided enclosure of width 3·10⁻⁶ and a precise statement that this cone/block pair is exhausted. No first claimed.

## Falsification Attempts
Independent script `mathematics/scripts/indep_theorem_DK.py` (numpy only, no repo import): own weights and maps, 9-fold image expansion with complex-step derivatives for W_w′ and b_w′, own m-functional ratio programme (f′ at image points chosen locally in [−a f, a f], which turns ℓ₁ − tℓ₂ into effective point coefficients c + a|d|, then DJ-style bang-bang backward recursion and bisection), normalised against the constant function. 7/7 PASS in 41.8 s:
- 512 images inside X_s; every word's m-coefficient positive (a W + sW′ − a|W b′| > 0, min 2.4·10⁻⁹ in unnormalised scale).
- Corner ((5/2,+),(√5/2,+)): 0.01399809, equal to the repo's relaxed corner value to 8 digits.
- Without the f′ term: 0.01382, equal to the repo's and below DJ.2's floor, confirming the term is necessary.
- Search over 1225 Q-pairs (13 grid points + 12 random t, both signs): max 0.01399809 at the same corner, ≤ 0.014000 and > 0.013997. Nothing contradicts DK.3.
- DK.4 arithmetic matches (θ = 0.0034999857, rate 0.53348041).
- Not independently recomputed: the outward cover (my search is a float sample, so it supports DK.3 but does not certify it) and the `arb` jets of DK.2.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_diameter_cover.py` on a fresh clone at 2618036: EXIT 0 in 549.4 s, all checks ok (266116 boxes, every accepted box ≤ 0.01400000, depths 17/12/14; θ_K ≤ [0.0034999857 ± 8.4·10⁻¹²]; rate ≤ [0.53348041 ± 2.1·10⁻⁹]; |μ| ≤ [0.22605234 ± 2.0·10⁻¹⁰]; CC level-sum max ratio [0.1991 ± 10⁻⁵]). The pytest wrapper was not rerun this slice.

## Mathematical Status
Theorem (proof in repository; cover in outward-padded floats with `arb` spot checks, as the repo itself states). diam ≈ 0.013998 is a float observation, not a theorem.

## Patent Relevance
None. A bound in a contraction estimate for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0222 (DJ.1 reduced; its kept limit closed), DISC-0220 (DH.4's 0.025879 replaced), DISC-0221 (DI.5 consequences sharpened), DISC-0219 (DG.3 θ_G used), DISC-0205 (spectral 0.1725 still out of reach).

## Open Questions
A cone family or block whose Birkhoff rate approaches 0.1725; DK's reduction and DJ.3-type floors across other (a, n); making DK.3's cover fully interval-certified.

## Next Experiments
Run indep_theorem_DK.py's programme over a grid of (a, n) to map the exhausted rate as a function of a and n.

## Reproduction Instructions
In informational-flux-identity @ 2618036: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_diameter_cover.py` (~10 min, ~600 MB). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DK.py` (~42 s, numpy only).

## Evidence Log
- 2026-11-12 ~1:15 AM EST: read commit 2618036 message, file list, GASKET.md §DK and CLAIM_STATUS row; checked DK.1's integral identity and DK.4's arithmetic by hand; independent float check 7/7 PASS; repo witness EXIT 0 (549.4 s).

## Change History
- 2026-11-12: created.
- 2026-11-12 (dated note, original text above unchanged): the open question "a cone family or block whose Birkhoff rate approaches 0.1725" is partly answered by IFI Theorem DL (7b88a6d98f10): on (C₂, L̃⁵) the certified rate is < 0.404994 and |μ| < 0.17161, still far from 0.1725. See DISC-0224.
