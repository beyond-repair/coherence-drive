# Discovery: Two-moment Jensen on spec(L) ⊂ [0,6] sharpens the diagonal ceilings and the audit floor (Theorem AK)

## Discovery ID

DISC-0094

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0095.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d45c90c7fb92ae96d70edbe73e73b42c3206e55e (main tip at archive time). Paths: GASKET.md "Theorem AK" (placed after Theorem AJ under the AJ heading: items 0–5, Proof, Witness, Kept Failure AK.1, NOT THIS; Conjecture J.1 evidence paragraph, "What this does not say", and OPEN updated); CLAIM_STATUS.md (new row "Two-moment Jensen on spec(L)⊂[0,6]; sharpened diagonal ceilings and audit floor" VERIFIED); scripts/gasket_fractional_moment_jensen.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AK, for every α∈(0,1) and level n≥1 (notation of Theorems AF–AJ; Theorems J, AA, AC, AG, AJ used as stated):
0. Spectral ceiling: with N the 3^n-cell × vertex incidence matrix and c_x∈{1,2} the number of cells containing x, L = 3 diag(c) − NᵀN, so spec(L) ⊂ [0,6] (attained at checked levels 2–4; attainment at every level not claimed).
1. Two-moment ceiling: for a probability measure on [0,6] with mean m<6 and variance s², ∫λ^α dμ ≤ π6^α + (1−π)t^α, t = m − s²/(6−m), π = s²/(s²+(6−m)²). Corner (m,s²)=(2,2) ⇒ D_a = (L^α)_aa ≤ D_a⁺ = 6^α/9 + (8/9)(3/2)^α < 2^α; neighbor (m,s²)=(4,4) ⇒ (L^α)_pp = (L^α)_qq ≤ D_p⁺ = (6^α+2^α)/2 < 4^α.
2. w_n = (D_a − W_far)/2 ≤ w_n⁺ = (D_a⁺ − W_far^min)/2 < 2^(α−1), W_far^min = 2α(1−α)/4^(2−α) (AG).
3. I_far ≤ ((L^α)_pp − w_pq)/2 · I_a ≤ H_AK I_a, H_AK = (D_p⁺ − α4^(α−1))/2 < H_AJ; γ_n ≤ Γ_AK = (D_p⁺ − α4^(α−1))/W_far^min < Γ_AJ.
4. σ_n ≥ σ_AK = 1/(w_n⁺ + H_AK) > σ_AJ; ρ_n ≥ ρ_AK = w_min/(w_min + H_AK).
5. For α<log3/log5, ‖F(n,α)‖ ≥ σ_AK·9√21/(28 C_AC(α)) > 0; at α=0.45 with AA's ‖F_frac‖ ≥ 0.084015, ‖F(n,0.45)‖ ≥ 0.058941 (≈1.060× AJ's 0.055599).

Witness at α=0.45: D_a⁺≈1.315657 (2^α≈1.366040), D_p⁺≈1.802814 (4^α≈1.866066), w_n⁺≈0.628963 (2^(α−1)≈0.683020), H_AK≈0.796441 (H_AJ≈0.828067), Γ_AK≈27.5912 (Γ_AJ≈28.6869), σ_AK≈0.701556 (σ_AJ≈0.661775), ρ_AK≈0.208603; AC-route floor ≈0.015472.

## Discovery

Theorem AK refines DISC-0092 by replacing the first-moment Jensen diagonal ceilings (2^α at the corner, 4^α at a neighbor) with sharp two-moment (Hermite/two-point) ceilings on [0,6], using the line-graph spectral bound λ_max(L) ≤ 6. Incremental constant improvement (floor 0.055599 → 0.058941 at α=0.45). Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Small further sharpening of the proved positive floor for DISC-0034's sequence; still far below live ‖F(6)‖≈0.880 and below 0.70. Kept Failure AK.1 (DISC-0095) closes the whole one-step neighbor-Harnack family as a route to 0.70. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Each edge lies in exactly one upward cell and two vertices are adjacent iff they share a cell, so NᵀN = diag(c) + A and deg = 2c; L = 2diag(c) − A = 3diag(c) − NᵀN ≤ 3diag(c) ≤ 6 (NᵀN ⪰ 0). Verified exactly at levels 1–5 with an independently built cell list.
2. f(λ)=λ^α has f''' = α(α−1)(α−2)λ^(α−3) > 0 on (0,6]. The quadratic g interpolating f at 6 and (value+slope) at t satisfies f − g = (f'''(ξ)/6)(x−t)²(x−6) ≤ 0 on [0,6]; ∫g dμ depends only on (m, s²) and equals the two-point value on {t,6}. Two-point laws recomputed: corner t=3/2, π=1/9; neighbor t=2, π=1/2 (both t ≥ 0).
3. Local moments: L_xx = d_x, (L²)_xx = d_x² + d_x, so (2,6) at the degree-2 corner and (4,20) at its degree-4 neighbors (verified at levels 1–5).
4. Row sums of L^α vanish and w_ap = w_aq, so D_a = 2w_n + W_far; with AG's W_far ≥ W_far^min this gives w_n ≤ w_n⁺.
5. (3)–(5) are AJ's chain with 4^α → D_p⁺ and 2^(α−1) → w_n⁺; closed forms recomputed on a 99-point α grid.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems J, AA (DISC-0072), AC (DISC-0078), AG (DISC-0086), AJ (DISC-0092) as stated. Items (0)–(4) hold for every α∈(0,1); (5) needs α<log3/log5.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AK.log` (repository witness `python3 scripts/gasket_fractional_moment_jensen.py` at d45c90c7fb92ae96d70edbe73e73b42c3206e55e, EXIT 0, 186 PASS, 0 FAIL, "All Theorem AK / Kept Failure AK.1 checks passed") and `/workspace/scratch-ifi/indep_theorem_AK.py` / `indep_theorem_AK.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py` plus own cell list, no repo import, numpy only; EXIT 0, 171 PASS, 0 FAIL, ALL PASS):
- two-point laws (t,π) and their moments; D_a⁺, D_p⁺ equal the two-point values on a 99-point α grid; all closed forms at 0.45; strict improvement over AJ on (0,1); AA floor 0.058941, AC floor 0.015472, gain ≈1.0601 over AJ;
- Hermite quadratic ≥ λ^α on a 60001-point [0,6] grid (α∈{0.10,0.45,0.68,0.90}, both t); attack: 40000 random 3-atom laws on [0,6] with each moment pair (α∈{0.10,0.45,0.90}) never exceed the two-point bound;
- levels 1–5: 3^n cells, c=1 at corners / 2 elsewhere, deg = 2c, L = 3diag(c) − NᵀN exactly, λ_max ≤ 6 (= 6 at levels 2–5), local moments (2,6)/(4,20), spectral-measure moments, g ≥ f on spec(L), E g = two-point value, D_a ≤ D_a⁺ and D_p ≤ D_p⁺ at four α;
- levels 1–6 at α=0.45: D_a ≤ D_a⁺, D_p = D_q ≤ D_p⁺, zero row sums, D_a = 2w_n + W_far, w_min ≤ w_n ≤ w_n⁺, W_far ≥ W_far^min, exact neighbor identity, v ≥ 0 harmonic at p,q, two-neighbor sum, I_far ≤ ((D_p−w_pq)/2)I_a ≤ H_AK I_a, γ_n ≤ Γ_AK, σ_n ≥ σ_AK, ρ_n ≥ ρ_AK, ‖F‖ ≥ σ_AK‖F_frac‖ ≥ 0.058941; live L6 D_a≈1.256755, D_p≈1.742623, w_n≈0.332260, live ‖F‖ table and level-2 lock 1.165909 reproduced;
- α sweep {0.10,0.30,0.50,0.60,0.68,0.80,0.95} × levels 1–5: same items (AC-route ‖F‖ floor below log3/log5).

## Prior Art

Elementary: line-graph bound λ_min(A) ≥ −2 (equivalently λ_max(L) ≤ 2·max c here), Hermite interpolation remainder, the classical two-moment (Chebyshev–Markov–Krein type) extremal bound for functions with f''' of fixed sign, one-step Harnack chain of DISC-0090/0092. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Incremental sharpening of DISC-0092; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt gasket and cell incidence independently; checked the cell identity, spectral ceiling, moments, Hermite majorant (on spectra and densely on [0,6]), random 3-atom competitors, and the full chain through level 6; swept seven other α values. Attack on sharpness: live residual slack (D_p−w_pq)/2 − I_far/I_a ≈ 0.345, 0.318, 0.311, 0.310, 0.310, 0.310 on levels 1–6, so the Harnack step remains far from tight (consistent with AK.1). No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0092's numerical floor (DISC-0092 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0092. Mathematical. Theorem AJ; AK replaces its Jensen diagonal ceilings 2^α, 4^α by two-moment ceilings D_a⁺, D_p⁺.
- DISC-0090, DISC-0088. Mathematical. Theorems AI/AH (earlier Harnack floors).
- DISC-0086, DISC-0084. Mathematical. AG/AF supply W_far^min and the earlier w_n ceiling.
- DISC-0078, DISC-0072. Mathematical. AC/AA supply ‖F_frac‖ floors.
- DISC-0095. Failed hypothesis. Kept Failure AK.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges and whether L≥0.70. DISC-0095 shows the one-step neighbor-Harnack family cannot reach 0.70 even with live constants; a different comparison is needed.

## Next Experiments

None required.

## Reproduction Instructions

`git checkout d45c90c7fb92ae96d70edbe73e73b42c3206e55e && python3 scripts/gasket_fractional_moment_jensen.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AK.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AK.log`, `/workspace/scratch-ifi/indep_theorem_AK.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AK at d45c90c7fb92ae96d70edbe73e73b42c3206e55e; repo witness EXIT 0 (186 PASS); independent check ALL PASS (171 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-15. Initial archive entry.
