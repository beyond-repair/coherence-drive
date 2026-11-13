# Discovery: Theorem DG, a signed local-slope bound replaces DF's cone-lemma term (C_100 under L̃⁸; per-level rate 0.6440 → 0.5875)

## Discovery ID
DISC-0219

## Status
THEOREM in the mathematical sense only (the repository contains the proof of DG.1 and a certified witness: `arb` cell enclosures on 4096 cells plus an outward-rounded float dynamic programme). Method KNOWN (Birkhoff–Hilbert-metric cone contraction; local slope / log-derivative bounds for transfer operators; linear-fractional maximisation by dynamic programme). Constants UNRESOLVED as to novelty. Spectral rate 0.1725 unchanged.

## Date Discovered
2026-10-31 (indexed ~1:05 PM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 347ea08d1560ef1bdace2a1df1d6312e0e79736d (2026-10-31 12:12:05 EDT).

## Original Evidence
- GASKET.md §Theorem DG (49 added lines); CLAIM_STATUS.md one new row; README.md reproduction list.
- scripts/gasket_fractional_profile_level_hilbert.py (new, 263 lines; imports DF's script `gasket_fractional_profile_level_block.py`, hence DE/DD/CF, unchanged).
- tests/test_cli.py `test_theorem_dg_profile_level_hilbert`; scripts/cli.py registration.

## Discovery
DF's open item ("the true Hilbert diameter (the cone-lemma term)"). Only CE.3's cone-lemma term 2 log((a+b₈)/(a−b₈)) = 0.0738370 is replaced; DF.2's joint term W_F < 0.04451 is used as stated.
- DG.1 (proved): factor lemma. If log u(x)−log u(y) ≤ α(x−y) and log v(x)−log v(y) ≥ −β(x−y) for x > y, then Φ_v/Φ_u ≤ (v(y)/u(y))·(a+β)/(a−α), Φ_u(x,y) = e^{ad}u(y) − u(x). Hence Θ₁₀₀(u,v) ≤ log(sup(v/u)/inf(v/u)) + 2 log K, K = max((a+D₋)/(a−D₊), (a+D₊)/(a−D₋)). The signed slope (log L̃⁸f)′ is bounded by a 256-point ratio-of-sums programme.
- DG.2 (certified): D₊ < 0.76155, D₋ < −0.15311, so every log L̃⁸f (f ∈ C₁₀₀) is strictly increasing with slope in [0.15311, 0.76155], and L̃⁸C₁₀₀ ⊂ C_{0.76155} (DF.1: C_{1.8457}).
- DG.3: 2 log K < 0.012225 (DF: 0.0738370); Δ_G < 0.056735; θ_G < 0.014183; per-level rate θ_G^{1/8} < 0.58745 (DF: 0.64398).
- DG.4: non-leading C¹ eigenvalues |μ| < 0.24893 (DF: 0.27288); |log(s_{k+1}/(r s_k))| ≤ θ_G^{⌊(k−4)/8⌋}·0.11477 for k ≥ 4 (equal to DF.4 for k ≤ 11; smaller by 2.086, 4.350, 82.31 at k = 12, 20, 52).

## Why It Matters
Third consecutive certified improvement of the Birkhoff route for this operator. With DG the cone-lemma term (0.0122) is now well under the joint term (0.0445), so the remaining slack is in W_F and in the cone family itself, not in the slope.

## Derivation
Factor lemma: from the slope hypotheses, v(x) ≥ v(y)e^{−βd} and u(x) ≤ u(y)e^{αd}, so Φ_v/Φ_u ≤ (v(y)/u(y))·g(d), g(d) = (e^{ad} − e^{−βd})/(e^{ad} − e^{αd}); the repo proves g(d) ≤ g(0⁺) = (a+β)/(a−α) (F(0)=0, F′ ≥ 0). Signed slope: (log L̃⁸f)′ = Σ_w wt_w((log wt_w)′ f_w + f′(σ_w s)σ_w′)/Σ_w wt_w f_w with |f′/f| ≤ a, giving the 256-point programme with consecutive a-Lipschitz constraints; solved per cell by outward bisection on the backward recursion V_k = c_k + max(E⁺V, E⁻V).

## Assumptions
DF.1/DF.2 (W_F < 0.04451 used as stated); CE.3 Hilbert-metric definition; CF.1; DF.4's proofs with θ_G; Θ_G′ < 0.11477 (DF.4, not redone with DG.1). Float DP with nextafter outward rounding (same rigour as DE.2/DF.2).

## New Results
θ_G < 0.014183; per-level Birkhoff rate < 0.58745; |μ| < 0.24893; L̃⁸C₁₀₀ ⊂ C_{0.76155}.
Independent result (this archive, floats, not certified): the slope bounds are nearly tight. Evaluating the same pointwise programme at 1025 points of X_s (endpoints included) gives max D₊ = 0.759386 (at s = 5/2) and max D₋ = −0.153817 (at s = √5/2). Because the pointwise programme only has consecutive constraints, its optimiser is realised by an actual f ∈ C₁₀₀ (piecewise exponential), so these are lower bounds for the true suprema up to float error: D₊ ∈ [0.75939, 0.76155), D₋ ∈ [−0.15382, −0.15311). The repo lists "no floor for D±" as a kept limit; this gives a float floor, within 0.29 % (D₊) and 0.46 % (D₋).

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995 (cones of log-Lipschitz functions, slope bounds for expanding maps); Baladi 2000; Dinkelbach / Charnes–Cooper. The factor-lemma style bound of the Hilbert diameter by slope ratios is standard in Liverani's cone method. Specific constants: no prior computation found; not searched further, so UNRESOLVED.

## Novelty Analysis
Technique KNOWN. Contribution is a sharper certified constant for this repository's operator. No first claimed.

## Falsification Attempts
- Independent script `mathematics/scripts/indep_theorem_DG.py` (numpy + mpmath; own orbit/weight/derivative recursion and Dinkelbach + exact DP; written after reading the repo script, so not text-only independent): 19/19 PASS in 3.9 s. Pointwise D± inside the certified bounds (above). Central finite differences of log L̃⁸f for f = 1, e^{±100s}, e^{100|s−1.8|} at s = 1.3, 1.9, 2.4 all lie in [−D₋, D₊] (slopes 0.205 to 0.648). Factor lemma g(d)/g(0⁺) ≤ 1 checked at 50 digits for d = 10⁻¹⁵..10^{1.75}, both orientations. 2 log K = 0.012224745, Δ_G = 0.056734745, θ_G = 0.014182735, rate 0.58744877 recomputed from the stated D± (all just under the stated bounds; the repo's arb values from its sharper D± are 0.012224488, 0.056734488, 0.014182671, 0.58744844). |μ| = 0.24892546 via rate_G/rate_F × DF's bound; DF/DG gains 2.0856, 4.3499, 82.306 at k = 12, 20, 52 reproduced.
- Attack on margins: the stated bounds are tight to the 5th–6th digit (e.g. Δ_G arb 0.056734488 vs stated 0.056735), but every check passes with arb enclosures, so no failure.
- Not independently recomputed: the certified per-cell enclosures (my check is pointwise); W_F (DF.2, used as stated in both).

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_hilbert.py` EXIT 0 in 54 s (fresh clone at 347ea08; D₊ ≤ 0.76154217 at cell 4095, D₋ ≤ −0.15311497 at cell 0). `pytest tests/test_cli.py -k theorem_dg`: 1 passed (53.2 s).

## Mathematical Status
Theorem (proof and certificate in repository). The float floor for D± is an observation, not a theorem.

## Patent Relevance
None. A contraction constant for a transfer operator. Not thrust, not a flux.

## Related Discoveries
DISC-0218 (Theorem DF; DG is its open item), DISC-0217 (Theorem DE), DISC-0215 (Theorem DC), DISC-0190 (Theorem CF), DISC-0188 (Theorem CE; cone lemma replaced), DISC-0205 (spectral route 0.1725).

## Open Questions
The true Hilbert diameter (DG is still a decoupled bound); re-optimising (a, n) with DG.1; redoing Θ_G′ with DG.1; whether log-Lipschitz cones can approach 0.1725 (gap now 0.587 vs 0.1725).

## Next Experiments
Re-scan (a, n) with the DG.1 term in place of the cone lemma; certify a floor for D± (the pointwise programme at s = 5/2 and s = √5/2 in arb would do it); a coupled bound of the diagonal ratio and the two factors.

## Reproduction Instructions
In informational-flux-identity @ 347ea08: `pip install python-flint numpy sympy mpmath`, `python3 scripts/gasket_fractional_profile_level_hilbert.py` (~55 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DG.py` (numpy + mpmath, ~4 s).

## Evidence Log
- 2026-10-31 ~1:05 PM EDT: read commit 347ea08 diff and script; repo witness EXIT 0 (54 s); pytest 1 passed (53.2 s); independent check 19/19 PASS; float floor for D± found (within 0.3–0.5 % of the certified bounds).

## Change History
- 2026-10-31: created.

### Dated note 2026-10-31 (~2:10 PM EDT): correction to this archive's float floor
The float floor stated above (D₊ ≥ 0.75939, D₋ ≥ −0.15382) came from my Dinkelbach iteration in `indep_theorem_DG.py`, which stalls below the supremum near s = 5/2 (found while checking Theorem DH; see DISC-0220). Re-running the same pointwise programme for L̃⁸ with bisection on the exact chain DP (129 points) gives max D₊ = 0.760712 and max D₋ = −0.153556. Corrected float floor: D₊ ∈ [0.76071, 0.76155) (gap 0.11 %), D₋ ∈ [−0.15356, −0.15311). The certified bounds and the 19/19 PASS verdict are unaffected: the old values were still lower bounds, only weaker. Theorem DH now certifies a floor for the L̃⁹ case. The text above is kept as written.
