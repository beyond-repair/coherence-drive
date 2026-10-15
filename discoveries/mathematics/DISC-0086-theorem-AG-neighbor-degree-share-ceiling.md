# Discovery: The neighbor-degree share has a uniform ceiling λ_n ≤ 1 − α(1−α)/2^(3−α) < 1, so ‖F‖→0 ⇔ γ_n→∞ below log3/log5 (Theorem AG)

## Discovery ID

DISC-0086

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0087.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e20e13fbe9528abb93e0c430bb810a341622356b (main tip at archive time). Paths: GASKET.md "Theorem AG. The neighbor-degree share has a uniform ceiling below 1" (Assumption, Theorem AG items 1–3, Proof, Witness, Kept Failure AG.1, Observation, NOT THIS); CLAIM_STATUS.md (new row "Uniform ceiling on the neighbor-degree share λ_n" VERIFIED; AF row now says "converse in Theorem AG"; α=0.45 OPEN row extended); scripts/gasket_fractional_lambda_ceiling.py (new); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AG, for every α∈(0,1) and level n≥1 (notation of Theorems AE–AF, DISC-0082 and DISC-0084):
1. Far-weight floor: the three vertices at combinatorial distance 2 from the value-1 corner give W_far(n,α) ≥ W_far^min(α) := 2α(1−α)/4^(2−α) > 0.
2. Uniform ceiling: with AF's Jensen bound (L^α)_aa ≤ 2^α, λ_n ≤ λ_ceil(α) := 1 − α(1−α)/2^(3−α) < 1 (≈0.957738 at α=0.45).
3. Two-sided split: for α<log3/log5, with c_* = (1−λ_ceil)/λ_ceil and C_J = 1/λ_J − 1, 1/(1+C_Jγ_n) ≤ ρ_n ≤ 1/(1+c_*γ_n), hence ‖F(n,α)‖→0 ⇔ γ_n→+∞.

Witness at α=0.45: W_far^min ≈ 0.057731, λ_ceil ≈ 0.957738, c_* ≈ 0.044127, C_J ≈ 2.253524; λ ratios (0.855064, 0.963857, 0.993134, 0.998827, 0.999807).

## Discovery

Theorem AG supplies the converse that DISC-0084 explicitly left unclaimed (it needed limsup λ_n < 1). With λ_n now pinned in [λ_J, λ_ceil] ⊂ (0,1) uniformly in n, DISC-0082's criterion ((1−λ_n)/λ_n)γ_n → ∞ is equivalent to γ_n → ∞. For α<log3/log5 the open combinatorial limit (DISC-0034 at α=0.45) is now exactly the question whether the far-to-neighbor gap ratio γ_n blows up. It does not decide that.

## Why It Matters

Closes the λ→1 escape route in the reduction chain AB → AE → AF → AG, leaving a single scalar sequence γ_n as the whole content of DISC-0034. Live γ_n decreases toward ≈1.375 on levels 1–6, which is evidence against vanishing but not a proof of a positive limit. Not thrust.

## Derivation

Repository proof, checked step by step in this archive (no gap found):
1. Gasket graph degrees are 2 (corners) and 4, so M = 4I − L ≥ 0 entrywise. e^(−sL) = e^(−4s) e^(sM), and every term of the exponential series of a nonnegative matrix is nonnegative, so off the diagonal (e^(−sL))_af ≥ e^(−4s)(s²/2)(M²)_af.
2. For off-diagonal entries, −(L^α)_af = (α/Γ(1−α)) ∫_0^∞ (e^(−sL))_af s^(−1−α) ds (Theorem J / Balakrishnan). Inserting step 1, ∫_0^∞ (s²/2) e^(−4s) s^(−1−α) ds = Γ(2−α)/(2·4^(2−α)), and αΓ(2−α)/Γ(1−α) = α(1−α), so −(L^α)_af ≥ (M²)_af α(1−α)/(2·4^(2−α)).
3. At every level n≥1 the corner a has neighbors p, q (adjacent to each other, degree 4) and exactly three distance-2 vertices with (M²)_af = 1, 2, 1. Since all off-diagonal entries of L^α are ≤ 0 and its row sums vanish, W_far = (L^α)_aa − 2w_n is the sum of −(L^α)_ax over x ∉ {a,p,q}, which is ≥ the three-vertex sum ≥ 4·α(1−α)/(2·4^(2−α)) = 2α(1−α)/4^(2−α).
4. 1 − λ_n = W_far/(L^α)_aa ≥ W_far^min/2^α = α(1−α)/2^(3−α) using AF's Jensen bound (DISC-0084).
5. ρ_n = 1/(1+((1−λ_n)/λ_n)γ_n) (DISC-0082) with c_* ≤ (1−λ_n)/λ_n ≤ C_J gives the sandwich; ρ_n→0 ⇔ γ_n→∞, and AB+AC (DISC-0076, DISC-0078) give ‖F‖→0 ⇔ ρ_n→0 for α<log3/log5.

## Assumptions

Spectral calculus as GASKET item 4; corner data (1,−1/2,0); Theorems J, AB (DISC-0076), AC (DISC-0078), AE (DISC-0082), AF (DISC-0084) as stated; nonpositive off-diagonal entries of L^α for α∈(0,1) (standard, implied by the integral representation). α=1 is excluded (the constant α(1−α) vanishes).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AG.log` (repository witness `python3 scripts/gasket_fractional_lambda_ceiling.py` at e20e13fbe9528abb93e0c430bb810a341622356b, EXIT 0, 121 PASS, 0 FAIL, "all checks passed") and `/workspace/scratch-ifi/indep_theorem_AG.py` / `indep_theorem_AG.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import, numpy only; EXIT 0, 100 PASS, 0 FAIL, ALL PASS):
- constants W_far^min=0.057731, λ_ceil=0.957738, c_*=0.044127, C_J=2.253524 match GASKET; λ_ceil = 1 − W_far^min/2^α exactly;
- the integral identity (α/Γ(1−α))∫ s^(1−α) e^(−4s)/2 ds = α(1−α)/(2·4^(2−α)) by independent quadrature at α ∈ {0.1, 0.45, 0.8};
- at α=0.45, levels 1–6: M ≥ 0; exactly three distance-2 vertices with path counts 1,1,2 (sorted); each −(L^α)_af ≥ (M²)_af α(1−α)/(2·4^(2−α)); W_far ≥ far-3 sum ≥ W_far^min (far-3 sum 0.425292, 0.254112, 0.222746, 0.217222, 0.216294, 0.216142); λ_J ≤ λ_n ≤ λ_ceil; c_* ≤ (1−λ_n)/λ_n ≤ C_J; ρ sandwich; AE factorization; λ_n, γ_n, ρ_n reproduce the AE/AF values to 6 digits;
- the two-step heat-kernel bound holds live at level 3 for s ∈ {0.1, 0.5, 1, 2, 5} (heat kernel from an independent eigendecomposition);
- α sweep {0.05, 0.1, 0.3, 0.6, 0.68, 0.8, 0.95, 0.99} × levels 1–5: far-weight floor, λ ceiling, and per-far-vertex bound all hold.

## Prior Art

Elementary: Balakrishnan/subordination integral for fractional powers of a graph Laplacian, entrywise lower bounds on heat kernels by truncating the exponential series of the nonnegative matrix dI − L (a standard short-time path-count bound), and the Γ-function identity. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). An exact reduction of DISC-0034 to γ_n→∞; not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Rebuilt the gasket independently; checked that the local six-vertex patch and path counts really are level-independent through level 6 (repo checks through level 4); checked the per-far-vertex bound, not only the sum; checked the heat-kernel inequality itself at several s; swept eight α values up to 0.99 where the constant nearly vanishes. The bound is loose (live 1 − λ_n ≈ 0.471 versus guaranteed 0.042) but correct. No break found.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. DISC-0034 unchanged (OPEN): for α<log3/log5 it is now exactly whether γ_n→∞; nothing bounds γ_n above. Observed γ_n≈1.375 and λ_n≈0.529 are not limit theorems.

## Patent Relevance

None.

## Related Discoveries

- DISC-0084. Mathematical. Theorem AF (λ floor, one-sided split); AG supplies the converse (DISC-0084 row not edited).
- DISC-0082. Mathematical. Theorem AE factorization used in step 5.
- DISC-0076, DISC-0078. Mathematical. AB+AC equivalence ‖F‖→0 ⇔ ρ_n→0 for α<log3/log5.
- DISC-0087. Failed hypothesis. Kept Failure AG.1 (no geometric λ climb).
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN, now ⇔ γ_n→∞.

## Open Questions

Whether γ_n→∞ at α=0.45 (equivalently, whether ‖F(n,0.45)‖→0); an upper bound on γ_n would settle DISC-0034 as a positive limit.

## Next Experiments

None required. Optional: γ_n at levels 7–10 by the sparse route used for DISC-0080.

## Reproduction Instructions

`git checkout e20e13fbe9528abb93e0c430bb810a341622356b && python3 scripts/gasket_fractional_lambda_ceiling.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AG.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AG.log`, `/workspace/scratch-ifi/indep_theorem_AG.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AG at e20e13fbe9528abb93e0c430bb810a341622356b; repo witness EXIT 0 (121 PASS); independent check ALL PASS (100 PASS). Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
