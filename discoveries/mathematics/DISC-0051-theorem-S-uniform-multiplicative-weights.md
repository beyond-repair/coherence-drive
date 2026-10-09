# Discovery: Uniform multiplicative gasket weights trichotomy (Theorem S)

## Discovery ID

DISC-0051

## Status

DERIVATIVE

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0048 / DISC-0049.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d22771de4351d86c5b04d52e36bcfe1a0a22744f. Paths: GASKET.md "Theorem S. Uniform multiplicative weights: trichotomy of the harmonic audit limit" (Assumption item 6, Theorem S, Proof, Kept Failure S.1, NOT THIS); scripts/gasket_uniform_weights.py; CLAIM_STATUS.md (if updated at that commit).

## Original Evidence

On the level-n finest-edge combinatorial gasket, set w_ij = λ^n. Interior harmonicity for L_λ = λ^n L_comb coincides with the combinatorial extension of Theorem G. Corner currents pick up λ^n, so for data (1, −1/2, 0)

‖F_λ(n)‖ = (λ · 3/5)^n √21/2.

Trichotomy: λ < 5/3 → 0; λ = 5/3 (Kigami resistance on this build) → constant √21/2; λ > 5/3 → +∞. Recovers Theorems G (λ = 1) and I (λ = 4).

## Discovery

A one-parameter scalar lift of Theorem G that unifies G and I and isolates resistance weights as the unique uniform multiplicative choice with a finite nonzero harmonic audit limit on this build.

## Why It Matters

It frames the harmonic audit limit as a trichotomy in λ. It does not freeze the α = 0.45 fractional audit (see DISC-0052). Not thrust.

## Derivation

Checked. L_λ = λ^n L_comb cancels in interior equations; currents scale by λ^n; substitute ‖F_comb(n)‖ = (3/5)^n √21/2 from Theorem G / Explicit dipole. One-step ratio λ·3/5 equals 1 iff λ = 5/3. Elementary; not analogous in substance to Theorems J/K/L.

## Assumptions

Uniform multiplicative weights on the finest-edge build (Assumption item 6); corner data (1, −1/2, 0); Theorem G.

## New Results

Archive `/workspace/scratch-ifi/gasket_uniform_weights.py` (repository witness rerun) and `/workspace/scratch-ifi/indep_uniform_S.log`: closed form through level 5 for λ ∈ {1, 5/3, 4, 3/2, 2}; resistance constant √21/2 ≈ 2.291287847478; below/above trichotomy on ratios; recovers G and I. Algebra-only re-derivation written to `/workspace/scratch-ifi/indep_uniform_S_algebra.py`.

## Prior Art

Theorem G / Kigami resistance renormalization λ = 5/3 on this build; Theorem I is the λ = 4 case. Classical gasket harmonic extension.

## Novelty Analysis

DERIVATIVE: scalar lift of DISC-0031 Theorems G and I. No novelty claimed. Not elevated to THEOREM (trivial relative to J/K/L).

## Falsification Attempts

Reran the witness script; re-derived the closed form from G without building the gasket. No discrepancy.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Correct elementary corollary of Theorem G.

## Patent Relevance

None.

## Related Discoveries

- DISC-0031. Mathematical. Theorems G and I are the λ = 1 and λ = 4 cases.
- DISC-0052. Failed hypothesis. Resistance weights do not freeze the α = 0.45 fractional audit.
- DISC-0034. Conjecture. Combinatorial ‖F(n, 0.45)‖ limit still OPEN.

## Open Questions

Multi-scale edge sets (different graph); combinatorial α = 0.45 limit (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout d22771de4351d86c5b04d52e36bcfe1a0a22744f && python3 scripts/gasket_uniform_weights.py`. Archive log: `/workspace/scratch-ifi/indep_uniform_S.log`.

## Evidence Log

- 2026-10-08. Recorded from GASKET.md Theorem S at d22771de4351d86c5b04d52e36bcfe1a0a22744f; script rerun OK. Repository description still matches its claim fence. Note: Theorems Q and R (commits 014b8d08, b6bf27d7) sit between P and S and were not indexed in this pass.

## Change History

- 2026-10-08. Initial archive entry.
