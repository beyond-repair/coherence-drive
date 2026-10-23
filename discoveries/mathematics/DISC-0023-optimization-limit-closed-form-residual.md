# Discovery: Closed-form infinite-depth residual on k-ary trees (Optimization-Limit Theorems A/B)

## Discovery ID

DISC-0023

## Status

DERIVATIVE

## Date Discovered

2026-10-08. Archive pass over beyond-repair/optimization-limit-conjecture, first time this repository is indexed.

## Source Repositories

beyond-repair/optimization-limit-conjecture, branch main, HEAD 9d3aed5077369e2cc89d58814a2b95c152568199.

Files: CONJECTURE.md (R_D definition, Theorem roadmap A–D), Proofs/TheoremA.tex (finite-D minimizer), experiments/branching_conflict_experiment.py (calculate_residual, optimal_root), README.md (printed numbers), CLAIM_STATUS.md (Sweep 213, claim cap ≤ 1, "Not claimed: proved asymptotic obstruction floor"), PROOF_13A_LIMIT_CORRECTION.md.

Cross-reference: beyond-repair/-ware-constant-derivation PROOF_13A_RECURSIVE_LIMIT.md at main 6dc4bac0e903a3f222129f98cb6eb9de14125505.

## Original Evidence

The repository computes only finite-depth residuals. README records that the depth-10 default residual is 68890/88573 and that the depth-40 float prints 0.7777777777777778, "collides with 7/9, but the rational is not 7/9". The sweep's closest point to 0.08 is R_D = 0.111111 at a = 0.935510. PROOF_13A_RECURSIVE_LIMIT.md says intermediate limits in (0, 1) need a nonvanishing violating share of the last layer and are "typically a rational in k". Neither repository writes the limit.

## Discovery

Using only the in-repo model (Theorem A minimizer x_0^*(D) = x̄ S_1/S_2 with S_1 = Σ_{d=0}^{D}(ka)^d, S_2 = Σ_{d=0}^{D}(ka^2)^d; states x_d = a^d x_0^*; R_D = violating-node fraction with tolerance ε), and writing δ = ε/|x̄|:

- If k ≥ 2 and k a^2 > 1 (hence k a > 1), put c = (k a^2 − 1)/(a (k a − 1)) > 0. Let S = { j ≥ 0 : |c a^{-j} − 1| < δ }. S is a finite block of consecutive integers [j_1, j_2] (possibly empty), and

  R_∞ = lim_{D→∞} R_D = 1 − k^{-j_1} + k^{-(j_2+1)}, or R_∞ = 1 if S is empty.

- If k a^2 ≤ 1, or k = 1, every fixed leaf-offset state tends to 0, so R_∞ = 1 when δ < 1 and R_∞ = 0 when δ > 1.

These hold away from the boundary set where |c a^{-j} − 1| = δ for some j (or δ = 1 in the second case).

Default (k, a, ε, x̄) = (3, 0.8, 0.05, 1): c = 23/28, c/a = 115/112, S = {1}, so R_∞ = 1 − 1/3 + 1/9 = 7/9 exactly. The finite-D rationals are not 7/9, as README says, but their limit is. The sweep point a = 0.935510 has S = {0, 1}, so R_∞ = 1/9, which is the 0.111111 the sweep prints.

## Why It Matters

CONJECTURE.md Theorem A (existence of lim R_D) and Theorem B (conditions for R_∞ > 0) are open in the repository and CLAIM_STATUS refuses a proved floor. For the k-ary tree model the repository actually implements, both reduce to the closed form above. It also explains the repository's own printed numbers (0.777…, 0.111…) as exact limits rather than coincidences. It does not touch W in K, thrust, or 0.08 (see DISC-0024).

## Derivation

Index nodes from the leaves: depth D − j. For k a^2 > 1, S_1 = ((ka)^{D+1} − 1)/(ka − 1) and S_2 = ((ka^2)^{D+1} − 1)/(ka^2 − 1), so a^{D−j} x_0^* = x̄ a^{-j} · a^D S_1/S_2 → x̄ c a^{-j}, with error O((ka)^{-D} + (ka^2)^{-D}). The node share of depth D − j is k^{D−j}(k − 1)/(k^{D+1} − 1) → (k − 1) k^{-(j+1)}, a summable dominating sequence, so dominated convergence gives R_∞ = Σ_j (k − 1) k^{-(j+1)} 1(|c a^{-j} − 1| > δ) whenever no j sits on the boundary. Because 0 < a < 1, c a^{-j} is strictly increasing to ∞, so the pass set is a finite consecutive block [j_1, j_2] and Σ_{j=j_1}^{j_2} (k − 1) k^{-(j+1)} = k^{-j_1} − k^{-(j_2+1)}. For k a^2 ≤ 1 (any k a), a^D S_1/S_2 → 0 (cases ka > 1, ka = 1, ka < 1 checked separately), so every fixed-offset state → 0 and passes iff |x̄| < ε. For k = 1 the weights are uniform and the deep states also → 0.

This is an elementary corollary of in-repo Theorem A. It is archived as DERIVATIVE, not THEOREM: the derivation is written here, not in the repository, and no repository proof or test asserts it.

## Assumptions

The repository's k-ary tree, Theorem A minimizer, and CONJECTURE.md R_D definition exactly as implemented in calculate_residual. 0 < a < 1. Generic parameters off the boundary set. No other graph family G is covered.

## New Results

The closed form for R_∞ and the exact identifications R_∞ = 7/9 (defaults) and R_∞ = 1/9 (sweep point). Archive-derived; not a repository statement.

## Prior Art

The infinite-depth optimizer x_0^∞ = x̄ (1 − ka^2)/(1 − ka) for a < 1/k is already in TheoremA.tex and PROOF_13A (confirmed: it is the ratio of the two geometric limits). The residual limit itself uses only geometric series and dominated convergence; it is textbook-level and no novelty is claimed.

## Novelty Analysis

DERIVATIVE. Overlooked in the corpus, not new mathematics.

## Falsification Attempts

- Exact arithmetic: c = 23/28 and c/a = 115/112 for the defaults; S = {1}.
- Repository code: calculate_residual at D = 40, 200, 600 prints 0.7777777777777778; at a = 0.935510, D = 400 prints 0.1111111111111111.
- 3000 random draws (k ∈ 2..7, a ∈ (0.05, 0.999), ε ∈ (0.005, 0.6), x̄ ∈ {1, −1, 2.5, 0.3}; 1529 with ka^2 > 1, 804 with ka > 1 ≥ ka^2, 667 with ka < 1) against calculate_residual at D ≤ 300: 2996 agree within 1e−4. The 4 disagreements all have k a^2 within 0.01 of 1 (slow (ka^2)^{-D} convergence) and agree with the closed form at D = 3000 and D = 20000 under a log-space evaluation.
- No counterexample found.

## Experimental Validation

None. experimental_validation false.

## Mathematical Status

Elementary corollary of in-repo Theorem A, archive-derived, numerically checked. Not a repository theorem.

## Patent Relevance

None.

## Related Discoveries

- DISC-0024. Mathematical. The attainable set of R_∞ excludes 0.08 exactly.
- DISC-0018. Historical. -ware-constant-derivation PROOF_13A is the cross-repo correction that fixed the inverted D → ∞ root.

## Open Questions

Other graph families G named in CONJECTURE.md are not implemented and are not covered. Boundary-set behaviour (|c a^{-j} − 1| = δ) is not worked out.

## Next Experiments

If the repository wants Theorems A/B on its tree, it can state the closed form and add a test against calculate_residual. This archive does not edit that repository.

## Reproduction Instructions

Check out beyond-repair/optimization-limit-conjecture at 9d3aed5077369e2cc89d58814a2b95c152568199. Import experiments/branching_conflict_experiment.calculate_residual and compare against 1 − k^{-j_1} + k^{-(j_2+1)} with c and S as above, for depths where D · ln(1/a) < 700.

## Evidence Log

- 2026-10-08. Clean clone at 9d3aed5077369e2cc89d58814a2b95c152568199; read CONJECTURE.md, TheoremA.tex, branching_conflict_experiment.py, core.py, README.md, CLAIM_STATUS.md, PROOF_13A_LIMIT_CORRECTION.md, and -ware-constant-derivation PROOF_13A_RECURSIVE_LIMIT.md.
- 2026-10-08. Residual robustness note: calculate_residual(900, k=6, a=0.45) raises OverflowError in optimal_root (math.exp of about D · ln(1/a)), although R_D is well defined. Not a status input; recorded so later runs do not read the overflow as a limit failure.
- 2026-10-08. GitHub description ("A formal research framework for the derivation of structural obstruction floors…") is aspirational and does not contradict CLAIM_STATUS. No description mismatch recorded.

## Change History

- 2026-10-08. Initial archive entry.
