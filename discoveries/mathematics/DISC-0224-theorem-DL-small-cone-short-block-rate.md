# Discovery: Theorem DL, a small cone and a short block beat the (C₁₀₀, L̃⁹) cap (0.0435818 < diam_Θ₂ L̃⁵C₂ ≤ 0.043583; per-level rate < 0.404994; |μ| < 0.17161)

## Discovery ID
DISC-0224

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DL.1, `arb` jets for DL.2, an `arb` floor for DL.3 and `arb` arithmetic for DL.5, and an outward-rounded float cover for DL.4). Method KNOWN (DK.1's generator reduction from DISC-0223 applied to a different cone and block; Birkhoff contraction; branch-and-bound cover). Constants UNRESOLVED as to novelty. Certification standard: DL.4's cover and the word tables are outward-padded floats checked against `arb` at sample centres, not full interval arithmetic (stated by the repo as a kept limit, same standard as DE.2–DK.3).

## Date Discovered
2026-11-12 (indexed ~2:10 AM EST)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 7b88a6d98f10 (2026-11-12 01:44:55 EST).

## Original Evidence
- GASKET.md §Theorem DL (line 5069 onward, 39 added lines; "NOT THIS" paragraph line 5099); CLAIM_STATUS.md new row (line 120); README.md reproduction list (+2).
- scripts/gasket_fractional_profile_level_small_cone.py (new, 547 lines); scripts/cli.py registration; tests/test_cli.py (+30 lines).

## Discovery
Answers DISC-0223's open question "a cone family or block whose Birkhoff rate approaches 0.1725" partially: the rate drops from 0.53349 to 0.40499, still far from 0.1725.
- Why a can shrink: DF–DK used a = 100 because their bounds carried a cone-lemma term 2 log((a+b_n)/(a−b_n)); DK.1 has no such term, so a can sit just above CF.2's absorbing value b* = 1.6884.
- DL.1 (proved, `arb`): φ(2) = max(14/15 + 2/√5, M₂ + 2c₂) < 1.8278 < 2, so L̃C_b ⊂ C₂ for b ≤ 2; |(log L̃⁵f)′| ≤ sup|λ_w| + 2 sup|b_w′| < 0.929, so L̃⁵C₂ ⊂ C₀.₉₂₉ and DK.1 holds verbatim for (a, n) = (2, 5).
- DL.2 (`arb`, 128 balls): |b_w′| < 5.224·10⁻³, |(log C_w)″| < 8.83, a + sλ_w ± a|b_w′| > 1.074.
- DL.3 (`arb`, DJ.2's construction at the (−,−) corner): Θ₂(L̃⁵f, L̃⁵g) ≥ 0.043581853.
- DL.4 (adaptive cover, 79662 boxes, depths 6/19/7): 0.0435818 < diam_Θ₂ L̃⁵C₂ ≤ 0.043583 (width 1.2·10⁻⁶).
- DL.5 (`arb`): θ_L ≤ 0.010895319; per-level rate θ_L^{1/5} ≤ 0.40499344 < 0.404994; every CF.1-form rate on (C₂, L̃⁵) is > 0.404991, so this pair is exhausted too; every other C¹ eigenvalue |μ| ≤ θ_L^{1/5}·r < 0.17161 (DK.4: 0.22606).
- Float observations (not claimed by the repo as theorems): corner-value rates on C₂ for L̃ⁿ are 0.405, 0.389, 0.378, 0.370, 0.364 at n = 5…9; a = 1.69 gives 0.4035 at n = 5; a trial (C₂, L̃⁷) cover is reported but not in the repo.

## Why It Matters
DJ.3's floor 0.53342 was a cap only for (C₁₀₀, L̃⁹); DL shows the cap was an artefact of the cone choice and gives a 24% lower certified rate and a 24% lower eigenvalue bound. The float trend over n (≈0.36 at n = 9) suggests the CF.1 route on C₂ plateaus well above the spectral 0.1725, which remains open.

## Derivation
DK.1's reduction (checked by hand in DISC-0223) uses only the identity ℓ_(x,y)(u) = ∫ e^{a|τ−x|} m^±_τ(u) dτ and positivity of the generators on the image cone; DL.1 supplies that positivity for (2, 5) through L̃⁵C₂ ⊂ C₀.₉₂₉ ⊂ C₂. Hand checks this slice: 14/15 + 2/√5 = 1.827761 < 1.8278; tanh(0.043583/4) = 0.0108953188, fifth root 0.40499344; tanh(0.0435818/4)^{1/5} = 0.40499121 (the 0.404991 floor); 0.40499344 × r (r = 0.4237312870 from CE.4) = 0.17160839.

## Assumptions
CF's Θ_a and CF.1; CF.2's b* and CF.3/CF.5 hypotheses; DJ.2's floor construction (DISC-0222); DK.1 (DISC-0223); CE.4's r; float word tables and DP outward-padded (kept limit); M₂, c₂ in φ(2) taken from the repo (not recomputed here).

## New Results
0.0435818 < diam_Θ₂ L̃⁵C₂ ≤ 0.043583; CF.1 per-level rate in (0.404991, 0.404994); |μ| < 0.17161 for every other C¹ eigenvalue.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (choice of log-Lipschitz cone aperture trades invariance against contraction); Baladi 2000. Specific constants for this operator: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN; re-choosing the cone aperture once a cone-lemma term is removed is standard practice. Contribution is a certified enclosure for a new (a, n) pair. No first claimed.

## Falsification Attempts
Independent script `mathematics/scripts/indep_theorem_DL.py` (numpy only, no repo import; DISC-0223's script re-parameterised to a = 2, n = 5 with new checks). 8/8 PASS in 6.6 s:
- 32 images inside X_s; every word coefficient a W + sW′ − a|W b′| > 0 (min 1.8·10⁻⁶ in unnormalised scale) at 9 t-values and both signs.
- Sampled sup|b_w′| = 5.218·10⁻³ (< DL.2's 5.224·10⁻³, and close to it, so the bound is tight); sampled sup|λ_w| = 0.9157, so sup|λ| + 2 sup|b′| ≈ 0.926 < 0.929 as DL.1 states.
- All eight endpoint corners computed: the maximum is (−,−) at 0.04358194, matching the repo's relaxed corner to 8 digits; (+,+) 0.03831, mixed 0.03716/0.04035.
- Search over 2145 Q-pairs (17 grid + 16 random t, both signs): max 0.04358194 at the (−,−) corner, inside (0.0435818, 0.043583]. Nothing contradicts DL.4.
- DL.5 arithmetic matches.
- Not independently recomputed: the outward cover (my search is a float sample, so it supports DL.4 but does not certify it), the `arb` jets of DL.2 and φ(2)'s second branch M₂ + 2c₂.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_small_cone.py` at 7b88a6d: EXIT 0 in 10.9 s, all checks ok (79662 boxes, every accepted box ≤ 0.04358300, depths 6/19/7; θ_L ≤ [0.010895319 ± 1.5·10⁻¹⁰]; rate ≤ [0.40499344 ± 1.9·10⁻¹⁰]; floor rate ≥ [0.40499131 ± 2.9·10⁻⁹]; |μ| ≤ [0.17160839 ± 1.6·10⁻⁹]; CE.4 r re-certified). The pytest wrapper was not rerun this slice.

## Mathematical Status
Theorem (proof in repository; cover in outward-padded floats with `arb` spot checks, as the repo states). The n = 5…9 rate trend and a = 1.69 value are float observations only.

## Patent Relevance
None. A contraction bound for a transfer operator. Not a flux, not thrust.

## Related Discoveries
DISC-0223 (DK.1 reused; its open question partly answered), DISC-0222 (DJ.2 floor construction reused; DJ.3 cap shown cone-specific), DISC-0220/0221 (earlier rate and eigenvalue bounds superseded), DISC-0205 (spectral 0.1725 still out of reach).

## Open Questions
Whether any CF.1-form bound reaches 0.1725 (float trend says not on C₂ up to n = 9); optimising a below 2; carrying DK.4's level-sum bound to C₂; a fully interval-certified cover.

## Next Experiments
Extend indep_theorem_DL.py's corner search over a ∈ [1.69, 3] and n = 5…9 to map the float corner-rate surface and see whether it flattens above 0.1725.

## Reproduction Instructions
In informational-flux-identity @ 7b88a6d: `pip install python-flint numpy`, `python3 scripts/gasket_fractional_profile_level_small_cone.py` (~11 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DL.py` (~7 s, numpy only).

## Evidence Log
- 2026-11-12 ~2:05 AM EST: read commit 7b88a6d message, file list, GASKET.md §DL and CLAIM_STATUS row; hand-checked DL.1's first branch and DL.5 arithmetic; independent float check 8/8 PASS; repo witness EXIT 0 (10.9 s).

## Change History
- 2026-11-12: created.
- 2026-11-12 (dated note, original text above unchanged): the kept limit "longer blocks only floats" is answered by Theorem DM (IFI 80fa08242cd4, DISC-0225), which certifies the float rates 0.378 (n = 7) and 0.364 (n = 9) recorded above.
