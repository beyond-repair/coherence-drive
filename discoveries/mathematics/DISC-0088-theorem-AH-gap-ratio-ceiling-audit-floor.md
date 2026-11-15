# Discovery: The far-to-neighbor gap ratio has a uniform ceiling; the audit norm does not vanish below log3/log5 (Theorem AH)

## Discovery ID

DISC-0088

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0089.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 167ef7c0c8f0ba365751cab033da77a3b48def96 (main tip at archive time). Paths: GASKET.md "Theorem AH. The far-to-neighbor gap ratio has a uniform ceiling; the audit norm does not vanish below log 3/log 5" (Assumption, Theorem AH items 1–5, Proof, Witness, Kept Failure AH.1, Observation, NOT THIS; Conjecture J.1 and OPEN updated); CLAIM_STATUS.md (zero-vs-positive row now NOT ZERO via AH; new row "Uniform ceiling on the far-to-neighbor gap ratio γ_n; positive audit floor" VERIFIED); scripts/gasket_fractional_gamma_ceiling.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AH, for every α∈(0,1) and level n≥1 (notation of Theorems AE–AG; Theorems AA, AB, AC, AE, AF, AG used as stated; s=1/10):
1. Kernel comparison: for every j∈Far and x∈{p,q}, w_xj ≥ κ(α) w_aj with K(α)=e^(8s)α/((2−α)(1−2^(−α))), κ(α)=s e^(−4s) 2^(−1−α)/(1+K).
2. One-step Harnack at the neighbors: I_far ≤ (4^α/(2κ)) I_a.
3. Uniform gap-ratio ceiling: with AG's W_far ≥ W_far^min(α)=2α(1−α)/4^(2−α), γ_n ≤ 4^α/(κ W_far) ≤ Γ_AH(α):=4^α/(κ W_far^min) < ∞.
4. Share floors: with AF's w_n ≤ 2^(α−1), σ_n ≥ σ_min(α):=(2^(α−1)+4^α/(2κ))^(−1) and ρ_n ≥ ρ_min(α):=w_min/(w_min+4^α/(2κ)).
5. Positive audit floor below log3/log5: for α<γ=log3/log5, ‖F(n,α)‖ ≥ σ_min ‖F_frac‖ ≥ σ_min·9√21/(28 C_AC(α)) > 0; at α=0.45 with AA's ‖F_frac‖≥0.084015, ‖F(n,0.45)‖ ≥ σ_min·0.084015 ≈ 6.442·10^(−4) at every level. Hence ‖F(n,0.45)‖↛0; with Theorem J, 6.442·10^(−4) ≤ ‖F(n,0.45)‖ ≤ (3/5)√21.

Witness at α=0.45: K≈2.411299, κ≈7.1923·10^(−3), 4^α/(2κ)≈129.726, Γ_AH≈4494.13, σ_min≈7.6682·10^(−3), ρ_min≈1.6157·10^(−3), AA-route floor ≈6.4424·10^(−4).

## Discovery

Theorem AH ceilings γ_n uniformly and, with AC (or AA at 0.45), floors the combinatorial audit norm away from zero for every α<log3/log5. Combined with AG (DISC-0086), this is the same as γ_n↛∞, now proved directly. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Closes the vanishing half of DISC-0034 at α=0.45 (and for all α<log3/log5): liminf ‖F‖ ≥ positive constant. The remaining open content of DISC-0034 is whether the limit exists and whether L≥0.70. The proved floor is crude (live ‖F(6,0.45)‖≈0.880). Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Small-time heat-kernel bound from (M^k)_aj=0 for k≤1 and semigroup comparison H_{τ+s}(p,j)≥H_s(p,a)H_τ(a,j) with H_s(p,a)≥s e^(−4s) give w_pj≥κ w_aj on Far (same for q).
2. v=u_a−u≥0 is L^α-harmonic at p,q; drop nonnegative terms and use (1) plus Jensen (L^α)_pp≤4^α to get I_far≤(4^α/(2κ))I_a.
3. γ_n=2 I_far/(W_far I_a)≤4^α/(κ W_far), then AG's W_far floor.
4. I_a^α=w_n I_a+I_far and AF's w_n≤2^(α−1) give σ_min and ρ_min.
5. Schur line ‖F‖=σ_n ‖F_frac‖ plus AC/AA floors on ‖F_frac‖.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems J, AA (DISC-0072), AB (DISC-0076), AC (DISC-0078), AE (DISC-0082), AF (DISC-0084), AG (DISC-0086) as stated. Items (1)–(4) hold for every α∈(0,1); (5) needs α<log3/log5 for a positive ‖F_frac‖ floor.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AH.log` (repository witness `python3 scripts/gasket_fractional_gamma_ceiling.py` at 167ef7c0c8f0ba365751cab033da77a3b48def96, EXIT 0, 157 PASS, 0 FAIL, "all checks passed") and `/workspace/scratch-ifi/indep_theorem_AH.py` / `indep_theorem_AH.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import, numpy only; EXIT 0, 163 PASS, 0 FAIL, ALL PASS):
- closed forms K, κ, Γ_AH, σ_min, ρ_min, AA/AC floors match GASKET;
- levels 1–3 heat-kernel ingredients: M≥0, (M^1)_aj=0 on Far, H_s(p,a)≥s e^(−4s), live min_j w_pj/w_aj≥κ;
- levels 1–6 at α=0.45: v≥0, harmonic at p,q, (L^α)_pp≤4^α, I_far≤(4^α/(2κ))I_a, γ_n≤Γ_AH, σ_n≥σ_min, ρ_n≥ρ_min, ‖F‖≥σ_min‖F_frac‖≥6.442e−4, AE γ table and GASKET I_far/I_a and min kernel ratios reproduced; level-2 lock 1.165909;
- α sweep {0.10,0.30,0.50,0.60,0.68,0.80,0.95} × levels 1–5: kernel ratio, γ ceiling, σ floor (and AC-route ‖F‖ floor below γ).

## Prior Art

Elementary: Balakrishnan/subordination integral for L^α, short-time heat-kernel comparison via the nonnegative matrix M=4I−L, one-step Harnack from L^α-harmonicity at degree-4 neighbors, Jensen diagonal bound. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Closes vanishing for DISC-0034 below log3/log5; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket independently; checked kernel comparison, Harnack, ceilings/floors, and AA-contingent audit floor through level 6; swept seven other α values. The proved κ≈7.2e−3 is crude versus live min ratios ≥1; the floor is far below live ‖F‖. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Vanishing of ‖F(n,α)‖ for α<log3/log5 is closed (positive level-uniform floor). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and for L≥0.70 (Conjecture J.1). Observed γ_n≈1.375 and ‖F(6)‖≈0.880 are not limit theorems.

## Patent Relevance

None.

## Related Discoveries

- DISC-0086. Mathematical. Theorem AG (λ ceiling, two-sided vanishing split); AH ceilings γ and so rules out γ_n→∞.
- DISC-0084, DISC-0082. Mathematical. AF/AE share floors and factorization used in (4).
- DISC-0076, DISC-0078, DISC-0072. Mathematical. AB+AC/AA supply ‖F_frac‖ floors for (5).
- DISC-0089. Failed hypothesis. Kept Failure AH.1 (max-principle shortcut gives no floor).
- DISC-0034. Conjecture. Vanishing closed by this row; convergence and L≥0.70 stay OPEN (DISC-0034 row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges, and whether the limit is ≥0.70 (Conjecture J.1). Sharper κ (live ratios suggest κ→1) would raise the floor but still not reach 0.70 from AA alone.

## Next Experiments

None required. Optional: levels 7–10 γ_n / ‖F‖ by the sparse route; watch for a later Theorem that sharpens κ.

## Reproduction Instructions

`git checkout 167ef7c0c8f0ba365751cab033da77a3b48def96 && python3 scripts/gasket_fractional_gamma_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AH.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AH.log`, `/workspace/scratch-ifi/indep_theorem_AH.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AH at 167ef7c0c8f0ba365751cab033da77a3b48def96; repo witness EXIT 0 (157 PASS); independent check ALL PASS (163 PASS). Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
