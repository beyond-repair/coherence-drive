# Discovery: A two-neighbor heat-kernel sum sharpens the neighbor Harnack and the audit floor (Theorem AI)

## Discovery ID

DISC-0090

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0091.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8 (main tip at archive time). Paths: GASKET.md "Theorem AI. A two-neighbor heat-kernel sum sharpens the neighbor Harnack" (Assumption, Theorem AI items 1–5, Proof, Witness, Kept Failure AI.1, Observation, NOT THIS; Conjecture J.1 and OPEN updated); CLAIM_STATUS.md (zero-vs-positive row now NOT ZERO via AI floor 0.051988 sharpening AH's 6.44e−4; new row "Two-neighbor heat-kernel sum; sharpened neighbor Harnack and audit floor" VERIFIED); scripts/gasket_fractional_harnack_sum.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AI, for every α∈(0,1) and level n≥1 (notation of Theorems AE–AH; Theorems AA, AC, AF, AG, AH used as stated):
1. Two-neighbor kernel sum: for every j∈Far, w_pj + w_qj ≥ 2 w_aj (first-step identity ∂_t H_t(a,j)+2 H_t(a,j)=H_t(p,j)+H_t(q,j); subordination; Tonelli; K(s)=∫_s^∞ e^{−2(t−s)} t^{−1−α} dt ≤ s^{−1−α}/2).
2. Sharpened one-step Harnack: I_far ≤ (4^α/2) I_a (AH (2) with κ replaced by 1).
3. Sharpened gap-ratio ceiling: with AG's W_far ≥ W_far^min, γ_n ≤ 4^α/W_far ≤ Γ_AI(α):=4^α/W_far^min = 8/(α(1−α)).
4. Sharpened share floors: with AF's w_n ≤ 2^(α−1), σ_n ≥ σ_AI(α):=1/(2^(α−1)+4^α/2)=2/(2^α(1+2^α)), ρ_n ≥ ρ_AI(α):=α/(α+2).
5. Sharpened audit floor below log3/log5: for α<γ=log3/log5, ‖F(n,α)‖ ≥ σ_AI ‖F_frac‖ ≥ σ_AI·9√21/(28 C_AC(α)) > 0; at α=0.45 with AA's ‖F_frac‖≥0.084015, ‖F(n,0.45)‖ ≥ σ_AI·0.084015 ≈ 0.051988 at every level (~80.7× AH's 6.442·10^(−4)).

Witness at α=0.45: 4^α/2≈0.933033, Γ_AI≈32.323232 (vs Γ_AH≈4494.13), σ_AI≈0.6187915, ρ_AI≈0.1836735, AA-route floor ≈0.0519878.

## Discovery

Theorem AI removes κ from the Harnack step by comparing the *sum* of the two neighbor kernels with 2 w_aj, so Γ_AI ≈ 32.32 at 0.45 (vs AH ~4494) and ‖F‖ ≥ 0.051988. Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Raises the proved floor by ~80.7× over DISC-0088 while keeping the same vanishing-closed status for DISC-0034. Still far below live ‖F(6)‖≈0.880 and below Conjecture J.1's 0.70. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. First-step identity at deg-2 corner → Duhamel formula for H_t(a,j); subordination + Tonelli + K(s)≤s^{−1−α}/2 give the two-neighbor sum.
2. Add L^α-harmonicity at p and q before comparing kernels → I_far ≤ (4^α/2) I_a.
3. γ_n = 2 I_far/(W_far I_a) ≤ 4^α/W_far, then AG's W_far floor.
4. I_a^α = w_n I_a + I_far and AF's w_n ≤ 2^(α−1) give σ_AI and ρ_AI.
5. Schur line ‖F‖ = σ_n ‖F_frac‖ plus AC/AA floors on ‖F_frac‖.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems AA (DISC-0072), AC (DISC-0078), AF (DISC-0084), AG (DISC-0086), AH (DISC-0088) as stated. Items (1)–(4) hold for every α∈(0,1); (5) needs α<log3/log5 for a positive ‖F_frac‖ floor.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AI.log` (repository witness `python3 scripts/gasket_fractional_harnack_sum.py` at cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8, EXIT 0, 161 PASS, 0 FAIL, "all checks passed") and `/workspace/scratch-ifi/indep_theorem_AI.py` / `indep_theorem_AI.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import, numpy only; EXIT 0, 178 PASS, 0 FAIL, ALL PASS):
- closed forms Γ_AI=8/(α(1−α)), σ_AI=2/(2^α(1+2^α)), ρ_AI=α/(α+2), AA/AC floors, gain vs AH ~80.7×;
- levels 1–3 (and α∈{0.10,0.90} at level 2): L row at a, backward equation, Duhamel, K(s)≤s^{−1−α}/2, subordination identity for w_aj, live sum inequality;
- levels 1–6 at α=0.45: sum ratio ≥1, v≥0, harmonic at p,q, (L^α)_pp≤4^α, I_far≤(4^α/2)I_a, γ_n≤Γ_AI, σ_n≥σ_AI, ρ_n≥ρ_AI, ‖F‖≥σ_AI‖F_frac‖≥0.051988, AE γ table reproduced; level-2 lock 1.165909;
- α sweep {0.10,0.30,0.50,0.60,0.68,0.80,0.95} × levels 1–5: sum inequality, γ ceiling, σ floor (and AC-route ‖F‖ floor below γ).

## Prior Art

Elementary: Balakrishnan/subordination integral for L^α, first-step heat-kernel identity at a degree-2 vertex, Tonelli, one-step Harnack from L^α-harmonicity at degree-4 neighbors, Jensen diagonal bound. Sharpens DISC-0088 by removing κ. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Sharpens the DISC-0088 floor; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket independently; checked first-step identity, K-bound, two-neighbor sum, Harnack, ceilings/floors, and AA-contingent audit floor through level 6; swept seven other α values. Pointwise w_pj≥w_aj observed live (not proved). No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Vanishing of ‖F(n,α)‖ for α<log3/log5 remains closed (stronger floor than DISC-0088). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and for L≥0.70 (Conjecture J.1). Observed γ_n≈1.375 and ‖F(6)‖≈0.880 are not limit theorems.

## Patent Relevance

None.

## Related Discoveries

- DISC-0088. Mathematical. Theorem AH (weaker floor via κ); AI sharpens by κ→1 via the two-neighbor sum.
- DISC-0086, DISC-0084. Mathematical. AG/AF supply W_far and w_n for (3)–(4).
- DISC-0078, DISC-0072. Mathematical. AC/AA supply ‖F_frac‖ floors for (5).
- DISC-0091. Failed hypothesis. Kept Failure AI.1 (κ→1 + AA does not reach J.1's 0.70).
- DISC-0034. Conjecture. Vanishing already closed by DISC-0088; convergence and L≥0.70 stay OPEN (DISC-0034 row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges, and whether the limit is ≥0.70 (Conjecture J.1). The κ→1 chain cannot reach 0.70 from AA alone (Kept Failure AI.1).

## Next Experiments

None required. Optional: levels 7–10 ‖F‖ by the sparse route; prove or refute the observed pointwise w_pj≥w_aj.

## Reproduction Instructions

`git checkout cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8 && python3 scripts/gasket_fractional_harnack_sum.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AI.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AI.log`, `/workspace/scratch-ifi/indep_theorem_AI.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AI at cfdc7de313215a4bd0f56d9e56c7d2f9c8f96ba8; repo witness EXIT 0 (161 PASS); independent check ALL PASS (178 PASS). Repository description still matches its claim fence (closed-surface identity / not thrust).

## Change History

- 2026-10-15. Initial archive entry.
