# Coherence Drive — Master Integration Repository

**Status (2026-08-14):** Architectural pointer. Not hardware-ready.

## Locked Baseline

- \(W_\star = 1/(4\pi)\approx 0.0796\) (tree-level matching)
- Option A: M2 is geometric/LDOS enhancement only
- Macro \(r_0(M_b)\) verified; local SPARC median χ²_red ~12
- Engineering thrust target remains a design goal, not a demonstrated result

## Component Map

| Repo | Role | Maturity |
|------|------|----------|
| ware-constant-phenomenology | Math, SPARC, lensing, W_star | Highest |
| sierpinski-geometry-045 | 0.45 geometry generator | Working |
| stress-tensor-modification | Evaluator + BEM/EFIE | Working (research grade) |
| momentum-closure | Conservation structure | Conceptual |
| topological-pinch | Aft-face localization | Hypothesis |
| thrust-target-30 | F/P = 3e-8 N/W target | Design goal |
| m2-renormalization-law | Geometric scaling | Provisional |
| -ware-constant-derivation | Derivation sketches | Provisional |
| CFTv3.3-IQG-Unified-Framework | Ledger + synthesis | Active |

## Next Engineering Steps

1. Close local SPARC and Bullet lag physics issues upstream.
2. Higher-order RWG full-wave BEM if precision is required.
3. Only then: mesh-converged residual force with physical fields.
