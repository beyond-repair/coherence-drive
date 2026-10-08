# Discovery: Fractional audit-norm bounds on the gasket (Theorems J, K, L)

## Discovery ID

DISC-0032

## Status

THEOREM

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0031.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56. Path: GASKET.md Theorems J, K, L. Evidence commits: cd5a3b5f3449d925225aa0d55b60473ee452fc22 (Theorems J, K), 2c016eb0f16530ccbea5bccf30f1c7c43abee1e8 (Theorem L). CLAIM_STATUS.md rows "Fractional audit norm, α = 0.45 … OPEN; divergence excluded by Theorem J; energy controls the norm (Theorem L)" and "Fractional audit norm for α > log 3/log 5 — VERIFIED tends to 0 (Theorem K)". Script: scripts/gasket_fractional_limit.py.

## Original Evidence

Complete proofs in GASKET.md.

## Discovery

Let u_n be the L^α-Dirichlet solution on level n with corner data (1, −1/2, 0), ‖F‖ the audit norm from combinatorial corner currents, ‖F_frac‖ the one from fractional currents, Q_α = u^T L^α u, w_min(α) = α 4^{α−1}.
- Theorem J: for all n ≥ 1, α ∈ (0,1): ‖F(n,α)‖ ≤ (3/5)√21.
- Theorem K: for α ∈ (log 3/log 5, 1): Q_α(u_n) ≤ (7/2)^α 3^{1−α} (3·5^{−α})^n and ‖F(n,α)‖ ≤ C(α)(3·5^{−α})^{n/2} → 0.
- Theorem L: for α ∈ (0,1): ‖F_frac‖ ≥ w_min ‖F‖ and ‖F‖ ≤ (√21/5)√(2/w_min) √Q_α(u_n).

## Why It Matters

It brackets the only open quantity in the repository (α = 0.45): not infinite, and zero exactly when energy collapses forces zero. It is the mathematical floor under Conjecture J.1 (DISC-0034).

## Derivation

Repository proofs, checked line by line in this archive:
1. Bochner subordination λ^α = (α/Γ(1−α))∫(1−e^{−λs})s^{−1−α}ds; with M = 4I − L ≥ 0 entrywise (degree ≤ 4 lemma), e^{−sL} = e^{−4s}e^{sM} > 0 off-diagonal, so L^α has strictly negative off-diagonal entries; (e^{−sL})_{cp} ≥ s e^{−4s} gives −(L^α)_{cp} ≥ α 4^{α−1} (∫ s^{−α}e^{−4s}ds = Γ(1−α)4^{α−1}, checked).
2. Maximum principle for the positive-weight form gives −1/2 ≤ u ≤ 1, so 0 ≤ I_a ≤ 3; Schur line gives ‖F‖ = I_a√21/5 (J).
3. Dirichlet minimality, Q_1(u_H) = (7/5)I_a^H = (7/2)(3/5)^n (checked), Hölder ∫λ^α dμ ≤ (∫λ dμ)^α(∫dμ)^{1−α}, ∫dμ ≤ N(n) ≤ 3^{n+1} (K).
4. The two corner edges inside the Dirichlet form: Q_α ≥ w_min(g_1² + g_2²) ≥ (w_min/2) I_a²; and I_a^α = Σ_j w_aj(1 − u_j) ≥ w_min I_a since 1 − u_j ≥ 0 (L).

## Assumptions

As DISC-0031; α ∈ (0,1); fixed corner data (1, −1/2, 0).

## New Results

Archive-side observation, not a claim: the threshold 3·5^{−α} = 1, i.e. α = log 3/log 5 = d_s/2 with d_s = 2 log 3/log 5 the gasket spectral dimension, is the classical point-capacity threshold for subordinate (α-stable-like) processes on the gasket (points are hit iff α d_w > d_h). Independent numerics (DISC-0035) suggest ‖F‖ actually decays like (3·5^{−α})^n above the threshold, so the n/2 exponent in Theorem K is a valid bound but likely not sharp.

## Prior Art

Bochner subordination, Hölder, discrete maximum principle; capacity dichotomy at α d_w = d_h on p.c.f. fractals is classical. The specific bounds concern this repository's audit functional. Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proofs in the repository, verified here). Not a novelty claim.

## Falsification Attempts

Archive independent dense computation (numpy eigh, own gasket builder), levels 1–7, α ∈ {0.1, 0.2, 0.3, 0.45, 0.55, 0.9}: every ‖F‖ is below (3/5)√21 ≈ 2.7495; ‖F_frac‖ ≥ w_min‖F‖ and ‖F‖ ≤ κ√Q hold (‖F_frac‖ taken from the pairing Q_α = (7/5)I_a^α, whose Schur line was checked directly); at α = 0.9 ‖F‖ falls from 1.3839 to 0.1250 by level 7. α = 0.45 values match GASKET.md to nine digits. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proved in-repo; proofs verified.

## Patent Relevance

None.

## Related Discoveries

- DISC-0031. Mathematical. Schur line and dipole algebra.
- DISC-0033. Mathematical. Kept failures are the rejected routes left after these bounds.
- DISC-0034. Mathematical. The open α = 0.45 limit these bounds bracket.
- DISC-0035. Computational. Suggests the Theorem K exponent is not sharp.

## Open Questions

Whether Q_{0.45}(u_n) → 0 (Theorem L would then give ‖F‖ → 0). DISC-0035 numerics point to a positive limit instead.

## Next Experiments

Prove a lower bound on Q_α(u_n) for α < log 3/log 5 via discrete point capacity.

## Reproduction Instructions

`git checkout 81ab02b501aef7df2f5478f55d67d50f93595d56 && python3 scripts/gasket_fractional_limit.py` (levels ≤ 7). Archive script in DISC-0035.

## Evidence Log

- 2026-10-08. GASKET.md read at 81ab02b; proofs checked; independent numerics as above.

## Change History

- 2026-10-08. Initial archive entry.
