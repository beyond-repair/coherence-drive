# Stage-2 Final Numerical Closure

**Date:** 2026-08-27  
**Acceptance criterion:** [STAGE2_ACCEPTANCE_CRITERION.md](STAGE2_ACCEPTANCE_CRITERION.md)  
**Claim flags:** permanently **false** for tested paths

---

## Executive statement

Under the constitutive maps and boundary-value problems **actually solved**, there is **no demonstrated continuum source term** for a residual force.

Stage-1 symbolic framework remains frozen and logically open.  
Stage-2 tested realizations (scalar Yukawa paths + Proca P-E2) produced residuals at or below spherical-control floors under joint refinement → **negative numerical closure** for those paths.

This is not a proof that every possible constitutive realization must be zero. It is a statement about the solved problems only.

---

## Paths closed

| Path | Classification |
|------|----------------|
| Surface geometric proxy | Non-physical proxy (not a PDE solution) |
| Surface electrostatic | Null |
| Interior Yukawa Dirichlet | Null |
| Exterior scalar E2 Yukawa | Null (tet ≤ sphere floor) |
| Proca P-E2 nodal scout | Null (tet ≤ sphere floor, ratio 0.11–0.50) |

Nédélec for Proca P-E2: **halted** (low information gain once residual is sub-floor).

---

## Claim flags (locked)

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
target_fitting_performed    = false
```

---

## Legitimate continuations

1. **New constitutive physics** — independently motivated map, frozen before solve, then full acceptance criterion.  
2. **Program close-out** — merge, tag, archive; propulsion conclusions unresolved but unsupported under tested maps.

Stage-3 experiment is not justified by present evidence under the maps tested.
