# Discovery: Theorem DF, DE's joint programme on a larger cone and a longer block (C_100 under L̃⁸; per-level rate 0.6931 → 0.6440)

## Discovery ID
DISC-0218

## Status
THEOREM in the mathematical sense only (the repository contains the proof and a certified witness: `arb` point tables plus DE.2's float dynamic programme with outward rounding). Method KNOWN (Birkhoff–Hilbert-metric cone contraction; exact maximisation of a linear-fractional functional under Lipschitz constraints; Lipschitz reduction over a square cover). Constants UNRESOLVED as to novelty. The spectral rate 0.1725 is unchanged and still reached only by the spectral route.

## Date Discovered
2026-10-31 (indexed ~12:20 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3f0579e83c8075e354aaecc7479ff4b477be0591 (2026-10-31 11:12:03 EDT).

## Original Evidence
- GASKET.md §"Theorem DF. A larger cone and a longer block" (inserted after Theorem DE, before Conjecture J.1).
- CLAIM_STATUS.md, one new row.
- scripts/gasket_fractional_profile_level_block.py (new, 429 lines; imports DE's script, hence DD's and CF's, unchanged; CE's for r; CC's for level sums).
- tests/test_cli.py `test_theorem_df_profile_level_block`; README.md reproduction list; scripts/cli.py registration.

## Discovery
DE's own open item ("certify a larger (a, n) with the joint term and carry CF.3/DC to that cone"), done for the pair DE had observed in floats: a = 100, block L̃⁸ (256 words, 512 points).
- DF.1 (exact): b₁ = φ(100) = 45.654693… < 100, so L̃C₁₀₀ ⊂ C₁₀₀; b₈ = φ⁸(100) = 1.8457143960… (b* = 1.6884). DE.1's line programme holds for any block length; the 256 images σ_w(X_s) are disjoint and ordered (smallest gap 7.95·10⁻⁶). Lipschitz reduction: ρ(x,y)+ρ(y,x) ≤ S(x_c,y_c) + 2b₈H on a square of side H.
- DF.2 (certified, adaptive 128-grid → 4096-grid square cover, ~60 s): W ≤ W_F = 0.04449994… < 0.04451 (DE: 0.29040); cone-lemma term 0.07383696; Δ_F < 0.11835; θ_F = tanh(Δ_F/4) < 0.02958; per-level rate θ_F^{1/8} < 0.64398 (DE: 0.69306).
- DF.3 (arb floor): W ≥ 0.04297832 (W_F/W_low ≤ 1.0355). The cone-lemma term is now the larger part of Δ_F.
- DF.4: CF.3/CF.5/DC.3 carried to (a, n) = (100, 8): non-leading C¹ eigenvalues |μ| < 0.27288 (DE: 0.29367); Θ₁₀₀(f₀, L̃f₀) ≤ Θ_G' = 0.11476270 (DC.2 in C_{47/2}: 0.28154093); |log(s_{k+1}/(r s_k))| ≤ θ_F^{⌊(k−4)/8⌋}·0.11477 ≤ 14.531·θ_F^{k/8} for k ≥ 4, smaller than DE.4's bound for every k ≥ 4 except k = 9, 10, 11, 19.

## Why It Matters
Second consecutive improvement of the Birkhoff route for this transfer operator, now certified at the larger cone. The repo's own float scan says this cone family plateaus near 0.63 per level, far from the spectral 0.1725, which sharpens the open question of whether log-Lipschitz cones can ever reach the spectral rate.

## Derivation
As DE (DISC-0217) with n = 8: for fixed (x, y) the sups over f and g separate; ρ is a 512-point linear-fractional programme solved by a backward recursion V_k = c_k + max(e^{a d_k}V_{k+1}, e^{−a d_k}V_{k+1}). New ingredient: L̃⁸C_a ⊂ C_{b₈} makes ρ b₈-Lipschitz in each argument, so a finite square cover with a 2b₈H pad bounds the supremum. Δ_F = 2 log((a+b₈)/(a−b₈)) + W_F; θ = tanh(Δ/4). C_F = Θ_G'·θ_F^{−11/8} from ⌊(k−4)/8⌋ ≥ (k−11)/8.

## Assumptions
CE.3 cone lemma; CF.1; CF.2 cone step (re-run); CF.3/CF.5 proofs (use a only through b* < a and φ(b) < a for b < a); DE.1/DE.2 imported unchanged; DC.2's B₀ ≤ 1.2791803 and log(sup R₀/inf R₀) ≤ 0.063592701 used as stated (DC's Taylor scan not re-run). Float DP correctness with nextafter outward rounding and 10⁻¹² exponential pads (same rigour as DE.2).

## New Results
θ_F < 0.02958; per-level Birkhoff rate < 0.64398; non-leading C¹ spectral radius < 0.27288; joint term known to 3.6%; explicit level-sum constant C_F < 14.531.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Baladi 2000 (cone contraction for transfer operators); Charnes–Cooper / Dinkelbach for linear-fractional programmes. No prior computation of these specific constants found; not searched beyond that, so novelty of the constants is UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a certified sharper constant for this repository's operator. Not a world first; no claim made.

## Falsification Attempts
- Independent script `mathematics/scripts/indep_theorem_DF.py` (numpy + mpmath, written from GASKET.md text only, never reading the repo script): 13/13 PASS on a 17×17 grid (6.1 s) and on a 41×41 grid (34 s). ρ is computed by my own bisection on the chain recursion, then the bang-bang maximiser is rebuilt and the ratio evaluated directly as a primal check (0 primal/dual mismatches). Grid maximum of the joint term 0.04297836 at (√5/2, 5/2), inside [W_low, W_F]; endpoint value matches DF.3's floor 0.04297832. b₁, b₈ recomputed exactly (b₈ = b* + 5⁻⁴(100 − b*)); M₂ = 0.50706443 recomputed; image separation min gap 7.95·10⁻⁶ reproduced; cone term 0.07383696, Δ_F, θ_F = 0.0295756, rate 0.6439716, |μ| bound 0.2728709 (r = 0.42373129 from DD's independent power iteration), Θ_G' = 0.1147627, C_F = 14.53005, Θ₀(100) = 0.643470, the exception set {9, 10, 11, 19} (checked k < 400), and all seven DE.4/DF.4 ratios reproduced.
- My first attempt (v1, kept as `indep_df_v1_lp` in the run log only) used scipy HiGHS as in DE's check and failed every off-diagonal LP with "Model error": gaps up to 0.584 give coefficients e^{58} ≈ 2·10²⁵, above HiGHS's 10²⁰ infinity. That was a limitation of my tool, not of the theorem; v2 replaced it.
- Text discrepancy found (minor, no effect on the theorem): GASKET.md DF.1(i) states b₈ = φ⁸(100) ≤ 1.845714396, but the exact value is 1.845714396038…, which exceeds the stated 9-decimal figure by 3.8·10⁻¹¹ (truncated rather than rounded up). The script's docstring says ≤ 1.8457144 (correct) and the script uses the `arb` value itself, and the cone term 0.07383696 I recompute from the exact b₈ matches. Reported here as a wording slip only.
- Not independently recomputed: the certified outward-rounded square cover (my check is pointwise, so it confirms the value, not the rigorous upper bound); DC.2's B₀ and log(sup R₀/inf R₀).

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_block.py` EXIT 0 in 87.0 s (fresh clone at 3f0579e). `pytest tests/test_cli.py -k theorem_df`: 1 passed (84.9 s).

## Mathematical Status
Theorem (proof in repository; certified constants). The (a, n) plateau near 0.63 is floats only, no claim.

## Patent Relevance
None. A contraction constant for a transfer operator, not a mechanism. Not thrust, not a flux.

## Related Discoveries
DISC-0217 (Theorem DE; DF is its open item, same programme on C₁₀₀/L̃⁸), DISC-0215 (Theorem DC; B₀ and DC.3's argument), DISC-0216 (Theorem DD), DISC-0190 (Theorem CF; cone step), DISC-0188 (Theorem CE; setting, cone lemma), DISC-0205 (spectral route, 0.1725, still sharper).

## Open Questions
Whether log-Lipschitz cones can approach 0.1725 (repo float scan suggests a plateau near 0.63); the true Hilbert diameter versus the cone-lemma term (now the larger part of Δ_F); DC.1's K(β) in C₁₀₀.

## Next Experiments
A different cone family (for example weighted or second-derivative cones); an exact Hilbert-diameter computation; an independent outward-rounded or interval re-run of the square cover.

## Reproduction Instructions
In informational-flux-identity @ 3f0579e83c80: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_block.py` (~90 s, ~160 MB). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DF.py [grid]` (numpy + mpmath; 17 → ~6 s, 41 → ~34 s).

## Evidence Log
- 2026-10-31 ~12:20 EDT: read commit 3f0579e diff; repo witness EXIT 0 (87.0 s); pytest 1 passed; independent v1 (HiGHS LP) unusable (coefficient overflow, my tool limit), v2 13/13 PASS at 17×17 and 41×41; b₈ wording slip noted.

## Change History
- 2026-10-31: created.

### Dated note 2026-10-31 (~1:05 PM EDT)
DF's open item on the cone-lemma term is addressed by Theorem DG (informational-flux-identity 347ea08d1560): signed slope bound, cone term 0.0738370 → 0.012225, θ_G < 0.014183, rate < 0.58745. See DISC-0219. This record is otherwise unchanged.

### Dated note 2026-10-31 (~2:10 PM EDT)
Theorem DH (informational-flux-identity a273479fb361) reruns DF.2's joint-term cover on the longer block L̃⁹: W_H < 0.0142 (floor 0.013764) versus this record's W_F < 0.04451 on L̃⁸. See DISC-0220. This record is otherwise unchanged.
