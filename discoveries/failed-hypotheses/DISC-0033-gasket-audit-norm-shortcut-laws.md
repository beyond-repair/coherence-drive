# Discovery: Shortcut laws for the gasket audit-norm limit (Kept Failures H.1, I.1, J.1–J.4)

## Discovery ID

DISC-0033

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0031.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56. Path: GASKET.md "Kept failures at α = 0.45", Kept Failure H.1, I.1, J.3, J.4. Evidence commits: 3f5c655092b39f5a4a970cb98a5321f05ec00839 (H.1), a5094e16f32a857e00334eaebb02da35b200b642 (I.1), cd5a3b5f3449d925225aa0d55b60473ee452fc22 and f64e1bd36c0e38d1188879757f15d9f0a7af656f (J.1, J.2), 2c016eb0f16530ccbea5bccf30f1c7c43abee1e8 (J.3), 5ab3ec92a3f13954ca471225d1802811ef663a34 (J.4). Scripts: scripts/gasket_fractional_limit.py, scripts/gasket_fractional_level9.py, scripts/gasket_fractional_level10.py, scripts/gasket_fractional_matrix_free.py.

## Original Evidence

Computed audit norms at α = 0.45, levels 1–10 (levels 8–10 matrix-free), and minimizer energies Q_{0.45}.

## Discovery

Six proposed laws are false on the repository's own data:
- H.1: the 3/5 refinement factor does not carry over to L^{0.45} (ratios 0.810, 0.885, 0.926).
- I.1: 1/d² weights do not give a finite nonzero limit (exact growth 12/5).
- J.1: no uniform ratio bound ‖F(n+1)‖/‖F(n)‖ ≤ 0.95 (0.95136 at 4→5).
- J.2: no gap contraction δ_{n+1} ≤ 5^{−0.45} δ_n (δ_6/δ_5 ≈ 0.6685 > 0.4847).
- J.3: no uniform 0.95 decay of Q_{0.45} (0.95158 at 4→5).
- J.4: no gap contraction δ_{n+1}/δ_n < log 3/log 5 ≈ 0.682606 (δ_10/δ_9 ≈ 0.683038).

## Why It Matters

Each was a sufficient condition for settling zero versus positive at α = 0.45. Their failure is why Conjecture J.1 (DISC-0034) is still open.

## Derivation

Direct comparison with computed values.

## Assumptions

As DISC-0032.

## New Results

Archive recomputation: from the recorded norms, δ_10/δ_9 = 0.683038 > 0.682606 (margin 4.3·10^{−4}). Levels 1–7 independently reproduced to nine digits (DISC-0035 script), so H.1, J.1, J.2, J.3 do not depend on repository code. DISC-0035 explains J.4: the gap ratio appears to converge to 5^{0.45}/3 ≈ 0.687726, which sits just above log 3/log 5, so J.4 was bound to fail; that limit is still below 1, so its failure does not point toward a zero limit.

## Prior Art

Not applicable (rejected numerical laws).

## Novelty Analysis

REJECTED readings.

## Falsification Attempts

Levels 1–7 recomputed independently; levels 8–10 not recomputed here (matrix-free run is about half an hour). scripts/gasket_fractional_level10.py rerun at 81ab02b: exit 0.

## Experimental Validation

None.

## Mathematical Status

Rejected as stated. None of these rejections proves either limit.

## Patent Relevance

None.

## Related Discoveries

- DISC-0032. Mathematical. The proved bounds these laws tried to sharpen.
- DISC-0034. Mathematical. The open conjecture left standing.
- DISC-0035. Computational. Predicts the gap-ratio limit 5^α/3 that explains J.2 and J.4.

## Open Questions

None here.

## Next Experiments

None.

## Reproduction Instructions

`git checkout 81ab02b501aef7df2f5478f55d67d50f93595d56 && python3 scripts/gasket_fractional_limit.py && python3 scripts/gasket_fractional_level10.py`

## Evidence Log

- 2026-10-08. Recorded from GASKET.md / CLAIM_STATUS.md at 81ab02b; level-10 replay rerun (exit 0); levels 1–7 recomputed independently.

## Change History

- 2026-10-08. Initial archive entry.
