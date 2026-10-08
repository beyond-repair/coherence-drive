# Discovery: Positive limit of the α = 0.45 gasket audit norm (Conjectures J.1, J.2)

## Discovery ID

DISC-0034

## Status

CONJECTURE

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0031.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56. Path: GASKET.md "Conjecture J.1" and the α = 0.10 Conjecture J.2; CLAIM_STATUS.md row "Fractional audit norm, α = 0.45, zero vs positive — OPEN". Witness: scripts/gasket_fractional_level10.py (prints conjecture_J1_still_open_above_0.70 True).

## Original Evidence

GASKET.md: "CONJECTURE, not a theorem. For α = 0.45 … ‖F(n)‖ decreases for every n ≥ 1 and lim ‖F(n)‖ = L with L ≥ 0.70." Falsifier: first level with ‖F‖ < 0.70 or a rise above 10^{−8}. Through level 10, ‖F(10)‖ ≈ 0.833640, not fired. J.2: ‖F(n, 0.10)‖ ≥ 1.410 for every n.

## Discovery

Repository conjectures, recorded as stated.

## Why It Matters

It is the repository's single open mathematical question in the gasket note. A positive limit would be a finite neutral dipole, not thrust; the repository says so.

## Derivation

None in-repo. Open.

## Assumptions

As DISC-0032.

## New Results

Archive evidence (DISC-0035, a separate conjecture): the fitted law 1/‖F(n,α)‖ ≈ A(α) + B(α)(5^α/3)^n predicts L(0.45) ≈ 0.8211 and L(0.10) ≈ 1.4106. Both are consistent with J.1 (L ≥ 0.70) and with J.2 (≥ 1.410, margin only about 6·10^{−4}). Archive independent levels 1–7 at α = 0.10 give ‖F(7, 0.10)‖ = 1.410949855, still above 1.410.

## Prior Art

Not searched for this functional. No novelty claimed.

## Novelty Analysis

CONJECTURE (repository's own open item).

## Falsification Attempts

Independent recomputation of levels 1–7 at α = 0.10 and 0.45; repository level-10 replay rerun. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Open. Divergence excluded (DISC-0032, Theorem J); zero would follow from energy collapse (Theorem L), which is not proved and not seen (Q_{0.45}(u_10) ≈ 0.941537).

## Patent Relevance

None.

## Related Discoveries

- DISC-0032. Mathematical. Bounds bracketing the limit.
- DISC-0033. Mathematical. Rejected shortcut laws.
- DISC-0035. Computational. Scaling law predicting L ≈ 0.821.

## Open Questions

Prove a positive lower bound on ‖F(n, 0.45)‖ uniform in n.

## Next Experiments

Level 11 (N = 265,722) with the repository's matrix-free code; DISC-0035 predicts ‖F(11)‖ ≈ 0.82970.

## Reproduction Instructions

`git checkout 81ab02b501aef7df2f5478f55d67d50f93595d56 && python3 scripts/gasket_fractional_level10.py`

## Evidence Log

- 2026-10-08. Recorded from GASKET.md at 81ab02b.

## Change History

- 2026-10-08. Initial archive entry.
