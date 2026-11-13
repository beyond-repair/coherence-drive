# Discovery: Keeping the neighbor-edge weight sharpens the Harnack constant below 4^α/2 (Theorem AJ)

## Discovery ID

DISC-0092

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0093.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit bf808891d7ff130e78a8bc2722cad1e41effa794 (main tip at archive time). Paths: GASKET.md "Theorem AJ. Keeping the neighbor-edge weight sharpens the Harnack constant below \(4^{\alpha}/2\)" (Assumption, exact neighbor identity, Theorem AJ items 1–5, Proof, Witness, Kept Failure AJ.1, Observation, NOT THIS; Conjecture J.1 and OPEN updated); CLAIM_STATUS.md (zero-vs-positive row now NOT ZERO via AJ floor 0.055599; new row "Neighbor-edge weight sharpens Harnack below 4^α/2; improved audit floor" VERIFIED); scripts/gasket_fractional_wpq_harnack.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AJ, for every α∈(0,1) and level n≥1 (notation of Theorems AH–AI; Theorems J, AA, AC, AF, AG, AI used as stated):
1. Neighbor-edge weight floor: w_pq ≥ w_min(α) = α·4^(α−1) (Theorem J on p∼q: H_t(p,q) ≥ t e^{−4t} from M=4I−L ≥ 0 entrywise, M_pq=1; subordination).
2. Sharpened one-step Harnack: exact L^α-harmonicity of v=u_a−u at p and q keeps the cross term, Σ_Far (w_pj+w_qj) v_j = (L^α)_pp v_p + (L^α)_qq v_q − w_pq I_a; with AI's w_pj+w_qj ≥ 2w_aj and Jensen (L^α)_pp ≤ 4^α, I_far ≤ ((4^α−w_pq)/2) I_a ≤ H_AJ I_a, H_AJ = (4^α − α4^(α−1))/2 = (4^α/2)(1−α/4).
3. γ_n ≤ Γ_AJ = 2(4−α)/(α(1−α)) = Γ_AI(1−α/4).
4. σ_n ≥ σ_AJ = 2/(2^α + 4^α − α4^(α−1)); ρ_n ≥ ρ_AJ = 2α/(α+4).
5. For α<log3/log5, ‖F(n,α)‖ ≥ σ_AJ ‖F_frac‖ ≥ σ_AJ·9√21/(28 C_AC(α)) > 0; at α=0.45 with AA's 0.084015, ‖F(n,0.45)‖ ≥ 0.055599 (≈1.069× AI's 0.051988).

Witness at α=0.45: w_min≈0.209932, H_AJ≈0.828067 (vs 0.933033), Γ_AJ≈28.6869 (vs 32.3232), σ_AJ≈0.661775, ρ_AJ=9/44.5≈0.202247; AC-route floor ≈0.014594.

## Discovery

Theorem AJ refines DISC-0090 by not discarding the nonnegative cross terms w_pq v_q, w_pq v_p in the neighbor harmonicity equations, and floors w_pq by Theorem J's uniform edge weight. A modest constant improvement (factor 1−α/4 on H and Γ; floor 0.051988 → 0.055599). Convergence of ‖F(n,0.45)‖ and Conjecture J.1 (L≥0.70) stay OPEN.

## Why It Matters

Small sharpening of the proved positive floor for DISC-0034's sequence. Still far below live ‖F(6)‖≈0.880 and below 0.70. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. (L^α v)_p = 0 and (L^α v)_q = 0 with v_a = 0 give the two exact identities; adding them gives the cross-term identity (verified live to <1e−10 at levels 1–6).
2. AI's two-neighbor sum with v_j ≥ 0 bounds the left side below by 2 I_far; Jensen bounds the diagonals by 4^α.
3. Theorem J: e^{tM} ≥ I + tM entrywise, so H_t(p,q) ≥ t e^{−4t}; (α/Γ(1−α))∫ t e^{−4t} t^{−1−α} dt = α4^(α−1) (checked by quadrature at α∈{0.1,0.45,0.9}).
4. (3)–(5) are AI's (3)–(5) with 4^α/2 → H_AJ; closed forms recomputed (Γ_AJ, σ_AJ, ρ_AJ) on a 99-point α grid.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems J, AA (DISC-0072), AC (DISC-0078), AF (DISC-0084), AG (DISC-0086), AI (DISC-0090) as stated. Items (1)–(4) hold for every α∈(0,1); (5) needs α<log3/log5.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AJ.log` (repository witness `python3 scripts/gasket_fractional_wpq_harnack.py` at bf808891d7ff130e78a8bc2722cad1e41effa794, EXIT 0, 217 PASS, 0 FAIL, "all checks passed") and `/workspace/scratch-ifi/indep_theorem_AJ.py` / `indep_theorem_AJ.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import, numpy only; EXIT 0, 145 PASS, 0 FAIL, ALL PASS):
- closed forms and strict improvement over AI on (0,1) grid; AA/AC floors; gain ≈1.069 over AI;
- subordination integral of t e^{−4t} equals α4^(α−1) (α∈{0.1,0.45,0.9});
- levels 1–3 at α=0.45 and level 2 at α∈{0.10,0.90}: p∼q, M=4I−L ≥ 0 with M_pq=1, H_t(p,q) ≥ t e^{−4t} on a 60-point t grid, w_pq ≥ w_min;
- levels 1–6 at α=0.45: exact cross-term identity, harmonic at p,q, v≥0, two-neighbor sum, diagonals ≤4^α, w_pq,w_n ≥ w_min, w_n ≤ 2^(α−1), I_far ≤ ((4^α−w_pq)/2)I_a ≤ H_AJ I_a, γ_n ≤ Γ_AJ, σ_n ≥ σ_AJ, ρ_n ≥ ρ_AJ, ‖F‖ ≥ σ_AJ‖F_frac‖ ≥ 0.055599; recorded live w_pq (0.371367 … 0.308206), (4^α−w_pq)/2 (0.747349 … 0.778930), AE γ table, level-2 lock 1.165909 all reproduced;
- α sweep {0.10,0.30,0.50,0.60,0.68,0.80,0.95} × levels 1–5: same items (AC-route ‖F‖ floor below log3/log5).

## Prior Art

Elementary: Balakrishnan/subordination, entrywise positivity of e^{tM}, Jensen diagonal bound, one-step Harnack from L^α-harmonicity. A direct refinement of DISC-0090 (keeping a dropped term). Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Incremental sharpening of DISC-0090; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket independently; checked the cross-term identity, edge-weight floor, heat-kernel lower bound, Harnack chain, ceilings/floors, and AA-contingent audit floor through level 6; swept seven other α values. Attack on sharpness: live residual Harnack slack (4^α−w_pq)/2 − I_far/I_a stays ≈0.37–0.44 at every level (live I_far/I_a(6)≈0.407121), so the bound is far from tight, consistent with the repo's "no sharp constant is claimed". No break found. (First archive run had one FAIL in my own quadrature at α=0.9 from small-t truncation; fixed with an analytic tail; not a repository issue.)

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0090's numerical floor (DISC-0090 row not edited). DISC-0034 remains CONJECTURE for existence of lim ‖F(n,0.45)‖ and L≥0.70.

## Patent Relevance

None.

## Related Discoveries

- DISC-0090. Mathematical. Theorem AI (4^α/2 Harnack); AJ keeps w_pq to reach H_AJ = (4^α/2)(1−α/4).
- DISC-0088. Mathematical. Theorem AH (κ-based floor).
- DISC-0086, DISC-0084. Mathematical. AG/AF supply W_far and w_n.
- DISC-0078, DISC-0072. Mathematical. AC/AA supply ‖F_frac‖ floors.
- DISC-0093. Failed hypothesis. Kept Failure AJ.1.
- DISC-0034. Conjecture. Convergence and L≥0.70 stay OPEN (row not edited).

## Open Questions

Whether ‖F(n,0.45)‖ converges and whether L≥0.70. Any Harnack-only route from AA caps at ≈0.123 (DISC-0093).

## Next Experiments

None required.

## Reproduction Instructions

`git checkout bf808891d7ff130e78a8bc2722cad1e41effa794 && python3 scripts/gasket_fractional_wpq_harnack.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AJ.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AJ.log`, `/workspace/scratch-ifi/indep_theorem_AJ.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AJ at bf808891d7ff130e78a8bc2722cad1e41effa794; repo witness EXIT 0 (217 PASS); independent check ALL PASS (145 PASS). Repository description still matches its claim fence (closed-surface identity / not thrust).

## Change History

- 2026-10-15. Initial archive entry.
