# Discovery: Theorem DH, DG's factor lemma on the longer block L̃⁹ plus an asymmetric factor lemma for the f₀ term (per-level rate 0.5875 → 0.5712)

## Discovery ID
DISC-0220

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DH.1 and a certified witness: `arb` cell tables on 4096 cells, outward-rounded float DPs, adaptive square cover to the 8192-grid). Method KNOWN (Birkhoff–Hilbert-metric cone contraction; Liverani-style slope/factor bounds; linear-fractional maximisation by dynamic programme). Constants UNRESOLVED as to novelty. Spectral rate 0.1725 unchanged.

## Date Discovered
2026-10-31 (indexed ~2:10 PM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit a273479fb36163cc5f3a22cfcd3ec439eb2b29a1 (2026-10-31 13:22:58 EDT).

## Original Evidence
- GASKET.md §Theorem DH (line 4875 onward, 59 added lines); CLAIM_STATUS.md one new row; README.md reproduction list.
- scripts/gasket_fractional_profile_level_reopt.py (new, 282 lines; imports DG's `gasket_fractional_profile_level_hilbert.py`, hence DF/DE/DD/CF, unchanged).
- tests/test_cli.py `test_theorem_dh_profile_level_reopt`; scripts/cli.py registration.

## Discovery
Addresses three of DG's kept limits: (a, n) not re-optimised with DG.1, Θ_G′ not redone with DG.1, no floor for D±. Same cone C₁₀₀; block L̃⁸ → L̃⁹ (512 words, 1024-point line DP).
- DH.1 (proved): asymmetric factor lemma. If u, v carry different two-sided slope bounds (α_u, β_u), (α_v, β_v) in [0, a), then Θ_a(u,v) ≤ log(sup(v/u)/inf(v/u)) + log K_up + log K_dn, K_up = max((a+β_v)/(a−α_u), (a+α_v)/(a−β_u)), K_dn symmetric. DG.1(ii) is the equal-bound case.
- DH.2 (certified): D₊ < 0.74455, D₋ < −0.16327, so every log L̃⁹f (f ∈ C₁₀₀) is increasing with slope in [0.16327, 0.74455]; certified floors D₊ ≥ 0.74356, D₋ ≥ −0.16376 from explicit bang-bang f.
- DH.3 (certified): W_H < 0.0142 (DF.2 on L̃⁸: 0.04451), floor 0.013764.
- DH.4: 2 log K < 0.011679, Δ_H < 0.025879, θ_H < 0.0064696, per-level rate θ_H^{1/9} < 0.57117 (DG: 0.58745).
- DH.5: |μ| < 0.24203 for every other C¹ eigenvalue (DG.4: 0.24893); Θ₁₀₀(f₀, L̃f₀) ≤ Θ_H′ < 0.10465 (DG.4: 0.11477; cone part 0.04105 vs 0.05117); level-sum bound Θ_H′·min(θ_G^{⌊(k−4)/8⌋}, θ_H^{⌊(k−4)/9⌋}), at least 1.0967× smaller than DG.4 at every k ≥ 4.
- Observation (floats): an (a, n) scan with DG.1's cone term plateaus near 0.570; (100, 9) is within 0.002 of the best found. Not certified optimal.

## Why It Matters
Fourth consecutive certified tightening of the Birkhoff route for this operator, and the first one where the floor and the bound are both certified for the slope and the joint term (D₊ within 0.13 %, W within 3.2 %). The float scan says the log-Lipschitz cone family with this decoupled bound saturates near 0.570, so the remaining gap to the spectral 0.1725 is structural, not a tuning issue.

## Derivation
DH.1 is DG.1(i)'s per-orientation argument with α_u and β_v (resp. β_u and α_v) taken from different functions: v(x) ≥ v(y)e^{−β_v d}, u(x) ≤ u(y)e^{α_u d} give Φ_v/Φ_u ≤ (v(y)/u(y))·(e^{ad} − e^{−β_v d})/(e^{ad} − e^{α_u d}) ≤ (v(y)/u(y))(a+β_v)/(a−α_u). With u = f₀ (b₀ ≤ 0.77333706) and v = L̃f₀ (B₀ ≤ 1.2791803), the cone part becomes log((a+B₀)/(a−b₀)) + log((a+b₀)/(a−B₀)) = 0.0410521 instead of 2 log((a+B₀)/(a−B₀)) = 0.0511700. The rest is DG.2/DF.2 rerun at n = 9 and DF.4's proofs with (θ_H, 9).

## Assumptions
CF.1; DG.1(i)/(iii) (proved in DG, block-length free); DE.1/DF.1(ii) line programme; DF.4's proofs of CF.3/CF.5 for a = 100; DC.2's b₀, B₀, log(sup R₀/inf R₀) ≤ 0.063592701 used as stated (signed slopes of f₀ and L̃f₀ not computed); DG.3's θ_G for the 8-block comparison. DP certificates are outward-rounded floats (same rigour as DE.2–DG.2).

## New Results
θ_H < 0.0064696; per-level Birkhoff rate < 0.57117; |μ| < 0.24203; Θ_H′ < 0.10465; L̃⁹C₁₀₀ ⊂ C_{0.74455}.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (log-Lipschitz cones, slope bounds); Baladi 2000; Dinkelbach / Charnes–Cooper. Using different cone parameters for the two arguments of the Hilbert metric is a routine refinement within Liverani's method. Specific constants: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is sharper certified constants for this repository's operator. No first claimed.

## Falsification Attempts
- Independent script `mathematics/scripts/indep_theorem_DH.py` (numpy + mpmath; own orbit, weight and derivative recursion; own chain DP with bisection; written from the GASKET.md text after reading the DG script, so not text-only independent): v2 19/19 PASS (~6 s).
  - Pointwise slope programme at 129 points: max D₊ = 0.743733 (s = 5/2), max D₋ = −0.163727 (s = √5/2), both inside [certified floor, certified bound).
  - Joint term at the endpoint pair: 0.0137650 (repo floor 0.013764, bound 0.0142); 7-point grid sup 0.0137650.
  - Finite differences of log L̃⁹f for f = 1, e^{100s}, e^{100|s−1.8|} at s = 1.3, 2.4 lie inside the slope range.
  - DH.1's factor g(d)/g(0⁺) ≤ 1 at 50 digits for (α_u, β_v) = (b₀, B₀), (B₀, b₀), (0.74455, 0.16327), (0, 99).
  - Arithmetic: 2 log K = 0.011678644, Δ = 0.025878644, θ = 0.0064695706, rate 0.57116809, |μ| ≤ rate·r = 0.24202179, Θ_H′ = 0.104644752 (cone part 0.04105205), Θ_G′ = 0.1147627; min DG.4/DH.5 over k < 400 = 1.09669; ratios 2.4042, 5.2707, 87.432 at k = 13, 22, 104; 9-block form smaller for 160 of k in 4..199 and for all k in 200..599. All match the commit.
- My own failure, kept: v1 (`indep_dh_v1`) reported 17/19, with "FAIL" on both slope floors (grid max D₊ = 0.740854 below the repo's floor 0.74356). Diagnosis: the secant sup over f at (2.5, 2.5 − h) gave 0.74373 as h → 0, which exceeds my derivative value. That is impossible by the mean value theorem, so the bug was mine. My Dinkelbach iteration stalled below the supremum near s = 5/2. Replacing it with bisection on the same exact chain DP gives 0.743733, consistent with the secant limit and with the repo. No defect in Theorem DH.
- Not independently recomputed: the per-cell enclosures and the adaptive square cover (my checks are pointwise and on a coarse grid).

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_reopt.py` on a fresh clone at a273479: EXIT 0 in 320.6 s, 26 ok lines, no FAIL (D₊ ≤ 0.74454753 at cell 4095, D₋ ≤ −0.16327474 at cell 0; 2 log K ≤ 0.011678499; θ_H ≤ 0.0064695307; rate ≤ 0.57116770). The pytest wrapper calls the same `main()` and was not rerun this slice.

## Mathematical Status
Theorem (proof and certificate in repository). The (a, n) plateau near 0.570 is a float observation, not a theorem.

## Patent Relevance
None. A contraction constant for a transfer operator. Not thrust, not a flux.

## Related Discoveries
DISC-0219 (Theorem DG; DH closes three of its kept limits), DISC-0218 (DF; joint term on L̃⁸), DISC-0215 (DC; b₀, B₀, R₀ used as stated), DISC-0205 (spectral route 0.1725).

## Open Questions
The true (coupled) Hilbert diameter; a floor for the cone term; signed slopes for f₀ and L̃f₀; whether any cone family can approach 0.1725, given the float plateau near 0.570.

## Next Experiments
Certify signed slopes of f₀, L̃f₀ (would shrink Θ_H′ further); a coupled bound of the diagonal ratio and the factors; a different cone family (e.g. second-derivative or projective cones) to test whether the 0.570 plateau is a property of log-Lipschitz cones.

## Reproduction Instructions
In informational-flux-identity @ a273479: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_reopt.py` (~6 min). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DH.py` (numpy + mpmath, ~6 s).

## Evidence Log
- 2026-10-31 ~2:10 PM EDT: read commit a273479 message, diff, script header and GASKET.md §DH; independent check v1 17/19 (my solver bug, above), v2 19/19 PASS; repo witness EXIT 0 (320.6 s). Corrected this archive's DISC-0219 float floor (dated note there).

## Change History
- 2026-10-31: created.
