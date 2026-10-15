# Discovery: The two-neighbor share factors into a degree share and a gap ratio, with sharp ceiling w_n ≤ 8^α/2 and resistance identity ρ_n = (√21/7) w_n ‖F‖ R_α (Theorem AE)

## Discovery ID

DISC-0082

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0083.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d793add3f4be3ed73d19678b995e38d55b2481a8 (main tip at archive time). Paths: GASKET.md "Theorem AE. Degree–gap factorization of the two-neighbor share" (Assumption, Theorem AE items 1–4, Proof, Witness table, Kept Failure AE.1, NOT THIS); GASKET.md "What this does not say" and OPEN bullets (AE sentences appended); scripts/gasket_fractional_degree_share.py (new); scripts/cli.py; CLAIM_STATUS.md (new row "Degree-gap factorization of ρ_n and sharp weight ceiling" VERIFIED; σ_n row and α=0.45 OPEN row extended); README.md Sequel paragraph.

## Original Evidence

GASKET.md Theorem AE, for every α∈(0,1] and level n≥1 with the L^α-Dirichlet minimizer u and corner data (1,−1/2,0):
1. Sharp weight ceiling: (L^α)_aa = e_a^T L^α e_a ≤ λ_max(L)^α ≤ 8^α and, by AB's equal neighbor weights, (L^α)_aa ≥ 2w_n, so w_n(α) ≤ 8^α/2 (sharpens AB's w_n ≤ 8^α).
2. Degree–gap factorization: λ_n := 2w_n/(L^α)_aa ∈ (0,1], W_far := (L^α)_aa − 2w_n, ḡ_nbr := I_a/2, ḡ_far := I_far/W_far with I_far := I_a^α − I_loc, γ_n := ḡ_far/ḡ_nbr; then ρ_n = λ_n/(λ_n + (1−λ_n)γ_n) and φ_n = 1 − ρ_n = (1−λ_n)γ_n/(λ_n + (1−λ_n)γ_n).
3. Resistance identity: from AD's Q_αR_α = 7/3 and Q_α = (7/5)I_a^α, I_a^α = 5/(3R_α(n)) and ρ_n = (3/5)w_n I_a R_α(n) = (√21/7) w_n ‖F(n,α)‖ R_α(n).
4. Split of the vanishing criterion: for α < log3/log5, AB+AC give ‖F‖→0 ⇔ ρ_n→0, and by the factorization ρ_n→0 ⇔ ((1−λ_n)/λ_n)γ_n → +∞.

Repo witness table at α=0.45, levels 1–6: λ_n ≈ (0.646893, 0.553135, 0.533143, 0.529482, 0.528861, 0.528759); γ_n ≈ (1.443835, 1.390438, 1.378096, 1.375485, 1.374963, 1.374864); λ ratios (0.855064, 0.963857, 0.993134, 0.998827, 0.999807).

## Discovery

Theorem AE rewrites the open quantity of DISC-0076 (ρ_n, whose vanishing is equivalent to ‖F(n,α)‖→0 for α<log3/log5 by DISC-0076 + DISC-0078) as a Möbius function of two finite-level ratios: the neighbor share λ_n of the fractional corner degree and the far-to-neighbor mean-gap ratio γ_n. It also ties ρ_n to the effective resistance R_α of DISC-0080. It does not decide whether ρ_n → 0.

## Why It Matters

Reduces DISC-0034 to one explicit blow-up question, ((1−λ_n)/λ_n)γ_n → ∞, and tightens AB's weight ceiling by a factor 2. At α=0.45 the finite-level values (λ_n ≈ 0.529, γ_n ≈ 1.375) look stable through level 6, but that is not a limit theorem. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Rayleigh quotient: e_a^T L^α e_a ≤ λ_max(L)^α ≤ 8^α (λ_max ≤ 2·max degree = 8 on the 4-regular interior; corners have degree 2). For 0<α<1, L^α has nonpositive off-diagonal entries (Bochner subordination: L^α = c_α∫_0^∞(I − e^{−tL})t^{−1−α}dt and e^{−tL} is entrywise nonnegative), and the row sums vanish, so (L^α)_aa = Σ_{j≠a}|(L^α)_aj| = 2w_n + W_far with W_far ≥ 0. Hence 2w_n ≤ (L^α)_aa ≤ 8^α and λ_n ∈ (0,1]. The repo uses this sign fact implicitly; it is standard and checked numerically here.
2. I_a^α = (L^α u)_a = Σ_j |(L^α)_aj|(u_a − u_j) = 2w_n ḡ_nbr + W_far ḡ_far = diag·(λ_n ḡ_nbr + (1−λ_n)ḡ_far), and I_loc = 2w_n ḡ_nbr = w_n I_a; dividing gives the Möbius form.
3. From DISC-0080: Q = (7/2)κ, R = 2/(3κ) ⇒ Q = 7/(3R); Schur identity Q = (7/5)I_a^α ⇒ I_a^α = 5/(3R); ρ = w_n I_a/I_a^α = (3/5)w_n I_a R; ‖F‖ = I_a√21/5 ⇒ (3/5)I_a = (√21/7)‖F‖.
4. From (2), 1/ρ_n − 1 = ((1−λ_n)/λ_n)γ_n; combine with DISC-0076 item 4 extended by DISC-0078.

## Assumptions

Spectral calculus L^α = V diag(λ^α)V^T, 0^α := 0 (GASKET item 4); corner data (1,−1/2,0); Theorems AB (DISC-0076: equal neighbor weights, σ_n = ρ_n/w_n), AC (DISC-0078: floor for α<γ) and AD (DISC-0080: Q_αR_α = 7/3) used as stated in the repository; nonpositivity of off-diagonal entries of L^α (standard, implicit in the repo proof). γ_n is defined only when W_far > 0 (true for α<1; at α=1, W_far = 0 and λ_n = 1).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AE.log` (repository witness `python3 scripts/gasket_fractional_degree_share.py` at d793add, EXIT 0, 90 PASS, 0 FAIL, "all checks passed", ≈13 s) and `/workspace/scratch-ifi/indep_theorem_AE.py` / `indep_theorem_AE.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; dense levels 1–6 at α=0.45; 40 PASS, 0 FAIL, ALL PASS; re-run 2026-10-15 ~6:57am EDT with identical tail):
- equal neighbor weights to 1e−12; w_min ≤ w_n ≤ 8^α/2 (w_6 = 0.33226015 vs 8^0.45/2 ≈ 1.2747);
- ρ_n = λ_n/(λ_n + (1−λ_n)γ_n) (ρ_6 = 0.4493761598), QR = 7/3, I_a^α = 5/(3R), ρ = (3/5)w_n I_a R = (√21/7)w_n‖F‖R at every level 1–6;
- λ_n, γ_n match the GASKET AE table at every level; λ ratios 0.85506394, 0.96385657, 0.99313410, 0.99882714, 0.99980692.

Archive supplement `/workspace/scratch-ifi/indep_theorem_AE_alpha_sweep.py` / `indep_theorem_AE_alpha_sweep.log` (own builder; 8 values α ∈ {0.1, 0.3, 0.45, 0.6, log3/log5, 0.75, 0.9, 1.0} × levels 1–5; 40/40 PASS, ALPHA_SWEEP_PASS): off-diagonal entries of L^α ≤ 1e−12 (sign fact of Derivation step 1), w_n ≤ 8^α/2, (L^α)_aa ≤ 8^α, λ_n ∈ (0,1], factorization and resistance identity to 1e−9 at every α (factorization vacuous at α=1, where W_far = 0 and λ_n = ρ_n = 1).

## Prior Art

Elementary: Rayleigh quotient bound, sign structure of fractional graph Laplacians (Bochner subordination), weighted-mean decomposition of a corner current. The resistance identity is a rewriting of DISC-0080's exact pairing. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Reformulation of the open DISC-0034 criterion; not a novelty claim and not a Stage-1 / claim-level raise. Wording note: "sharp" means sharper than AB's 8^α, not attained; on the sweep w_n/(8^α/2) ≤ 0.271 (0.2607 at α=0.45, level 5; exactly 0.25 at α=1). Notation note: GASKET item 4 uses γ both for log3/log5 and for the gap ratio γ_n; the meaning is clear from subscripts.

## Falsification Attempts

Rebuilt the gasket independently and recomputed every identity at α=0.45 through level 6; swept seven other α in (0,1] through level 5, including the endpoint log3/log5 and α=1; checked the off-diagonal sign condition the proof relies on implicitly. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. DISC-0034 unchanged (OPEN): AE reduces it to ((1−λ_n)/λ_n)γ_n → ∞ but gives no limit for λ_n or γ_n. Finite-level λ_n ≈ 0.529, γ_n ≈ 1.375 are not limit theorems.

## Patent Relevance

None.

## Related Discoveries

- DISC-0076. Mathematical. Theorem AB (equal neighbor weights, ‖F‖→0 ⇔ ρ_n→0); ceiling sharpened here from 8^α to 8^α/2 (DISC-0076 row not edited).
- DISC-0078. Mathematical. Theorem AC extends AB's equivalence to every α<log3/log5, used in item 4.
- DISC-0080. Mathematical. Theorem AD exact pairing Q_αR_α = 7/3, used in item 3.
- DISC-0083. Failed hypothesis. Kept Failure AE.1 (no geometric λ wipeout).
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Whether ((1−λ_n)/λ_n)γ_n → ∞ at α=0.45 (equivalently DISC-0034). Limits of λ_n and γ_n separately.

## Next Experiments

None required. Optional: λ_n, γ_n at levels 7–10 by the sparse route used for DISC-0080.

## Reproduction Instructions

`git checkout d793add3f4be3ed73d19678b995e38d55b2481a8 && python3 scripts/gasket_fractional_degree_share.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AE.py 6` and `python3 /workspace/scratch-ifi/indep_theorem_AE_alpha_sweep.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AE.log`, `/workspace/scratch-ifi/indep_theorem_AE.log`, `/workspace/scratch-ifi/indep_theorem_AE_alpha_sweep.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AE at d793add3f4be3ed73d19678b995e38d55b2481a8; repo witness EXIT 0 (90 PASS); independent check ALL PASS; α sweep ALPHA_SWEEP_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
