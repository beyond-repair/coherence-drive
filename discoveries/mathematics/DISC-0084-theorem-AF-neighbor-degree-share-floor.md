# Discovery: The neighbor-degree share has a uniform floor λ_n ≥ α2^(α−1) (Jensen), so ‖F‖→0 forces γ_n→∞ below log3/log5 (Theorem AF)

## Discovery ID

DISC-0084

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0085.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit f5f89d9c359498d6be6c952b51a96af7914ad831 (main tip at archive time). Paths: GASKET.md "Theorem AF. The neighbor-degree share has a uniform floor" (Assumption, Theorem AF items 1–3, Proof, NOT CLAIMED (converse), Witness, Kept Failure AF.1, Observation, NOT THIS); CLAIM_STATUS.md (new row "Uniform floor on the neighbor-degree share λ_n" VERIFIED; α=0.45 OPEN row extended); scripts/gasket_fractional_lambda_floor.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AF, for every α∈(0,1] and level n≥1 (notation of Theorem AE, DISC-0082):
1. Uniform floor: λ_n ≥ λ_min(α) := 2w_min/8^α = α2^(−1−α) (≈0.164710 at α=0.45), using (L^α)_aa ≤ λ_max(L)^α ≤ 8^α and w_n ≥ w_min = α4^(α−1) (Theorem J).
2. Jensen sharpening: (L^α)_aa ≤ (L_aa)^α = 2^α, so λ_n ≥ λ_J(α) := α2^(α−1) (≈0.307359) and w_n ≤ 2^(α−1) (sharpens AE's 8^α/2).
3. One-sided split: for α<log3/log5, C_J = 1/λ_J − 1 (≈2.253524 at 0.45) gives ρ_n ≥ 1/(1 + C_J γ_n), hence ‖F(n,α)‖→0 ⇒ γ_n→+∞. The converse is explicitly NOT CLAIMED (would need limsup λ_n < 1).

Witness at α=0.45, levels 1–6: (L^α)_aa ≈ (1.204427, 1.244994, 1.254590, 1.256396, 1.256704, 1.256755) ≤ 2^0.45 ≈ 1.366040; γ ratios (0.963017, 0.991123, 0.998105, 0.999620, 0.999928).

## Discovery

Theorem AF turns DISC-0082's criterion ((1−λ_n)/λ_n)γ_n → ∞ into a necessary condition on γ_n alone: since λ_n is bounded away from 0 uniformly in n, vanishing of the combinatorial audit norm below log3/log5 requires the far-to-neighbor gap ratio γ_n to blow up. It does not decide whether that happens.

## Why It Matters

Narrows the only remaining route to ‖F(n,0.45)‖→0 (DISC-0034) to γ_n→∞. The computed γ_n is decreasing toward ≈1.375 on levels 1–6, which is evidence against that route but not a proof of a positive limit. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Rayleigh quotient (as DISC-0082 step 1) and w_n ≥ w_min (Theorem J) give λ_n ≥ 2w_min/8^α; closed form 2α·2^(2α−2)·2^(−3α) = α2^(−1−α).
2. μ_a = Σ_k v_k(a)² δ_{λ_k} is a probability measure with mean L_aa = deg a = 2 (corner degree 2). t ↦ t^α is concave for α∈(0,1], so (L^α)_aa = ∫t^α dμ_a ≤ 2^α (Jensen). Then λ_n ≥ 2w_min/2^α = α2^(α−1). w_n ≤ 2^(α−1) uses 2w_n ≤ (L^α)_aa, which rests on nonpositive off-diagonals of L^α and zero row sums (standard, implicit in the repo; checked numerically here as for DISC-0082).
3. ρ_n = 1/(1 + ((1−λ_n)/λ_n)γ_n) (DISC-0082) and (1−λ_n)/λ_n ≤ 1/λ_J − 1 = C_J give the bound; ρ_n→0 (DISC-0076 + DISC-0078) then forces C_Jγ_n→∞ with C_J a fixed finite positive number for α<log3/log5.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems J, AB (DISC-0076), AC (DISC-0078), AE (DISC-0082) as stated; nonpositivity of off-diagonal entries of L^α (standard).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AF.log` (repository witness `python3 scripts/gasket_fractional_lambda_floor.py` at f5f89d9, EXIT 0, 99 PASS, 0 FAIL, "all checks passed", ≈28 s) and `/workspace/scratch-ifi/indep_theorem_AF.py` / `indep_theorem_AF.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; EXIT 0, 69 PASS, 0 FAIL, ALL PASS):
- constants λ_min=0.164710, λ_J=0.307359, C_J=2.253524, C=5.071290 match GASKET;
- at α=0.45, levels 1–6: off-diagonals of L^α ≤ 0 (max 0), (L^α)_ii ≤ (L_ii)^α at every vertex (not only the corner), corner diag ≤ 2^α, w_min ≤ w_n ≤ 2^(α−1), λ_J ≤ λ_n ≤ 1, ρ_n ≥ 1/(1+C_Jγ_n); diag, w_n, λ_n, γ_n, ρ_n reproduce the GASKET/AE values to 6 digits;
- α sweep {0.05, 0.2, 0.45, 0.6, 0.75, 0.9, 1.0} × levels 1–4: Jensen at every vertex, λ_n ≥ α2^(α−1), off-diagonals ≤ 0.

## Prior Art

Elementary: Jensen's inequality for the spectral measure of a unit vector (the diagonal bound f(A)_ii ≤ f(A_ii) for concave f is standard), Rayleigh quotient, and the Möbius rewriting of DISC-0082. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). A one-sided reduction of DISC-0034; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket independently; checked the Jensen bound at every vertex (stronger than the corner statement), the off-diagonal sign fact used implicitly for w_n ≤ 2^(α−1), and the floors across seven α values including α=1 (λ_n=1 exactly). Checked that the converse is not claimed: the repo states it would need limsup λ_n < 1. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. DISC-0034 unchanged (OPEN): AF makes γ_n→∞ necessary for ‖F(n,0.45)‖→0 but bounds neither γ_n above nor limsup λ_n below 1. Observed γ_n≈1.375 and λ_n≈0.529 are not limit theorems.

## Patent Relevance

None.

## Related Discoveries

- DISC-0082. Mathematical. Theorem AE (factorization and 8^α/2 ceiling); AF floors λ_n and sharpens the ceiling to 2^(α−1) (DISC-0082 row not edited).
- DISC-0076, DISC-0078. Mathematical. AB+AC equivalence ‖F‖→0 ⇔ ρ_n→0 for α<log3/log5, used in item 3.
- DISC-0085. Failed hypothesis. Kept Failure AF.1 (no geometric γ blowup).
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Whether γ_n→∞ at α=0.45; whether limsup λ_n < 1 (would make γ_n→∞ also sufficient).

## Next Experiments

None required. Optional: γ_n at levels 7–10 by the sparse route used for DISC-0080.

## Reproduction Instructions

`git checkout f5f89d9c359498d6be6c952b51a96af7914ad831 && python3 scripts/gasket_fractional_lambda_floor.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AF.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AF.log`, `/workspace/scratch-ifi/indep_theorem_AF.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AF at f5f89d9c359498d6be6c952b51a96af7914ad831; repo witness EXIT 0 (99 PASS); independent check ALL PASS (69 PASS). Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
