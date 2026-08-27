# Stage-2 Final Numerical Closure

**Date:** 2026-08-27 (includes Proca B1 null)  
**Detailed archive:** [stress-tensor-modification/stage2_archive](https://github.com/beyond-repair/stress-tensor-modification/tree/stage2-numerical-closure/stage2_archive)  
**Claim flags:** permanently **false**

---

## Executive statement

Under tested constitutive paths — scalar interior/exterior Yukawa **and** vector Proca P-E2 — **no robust non-vanishing continuum G is established**. Residuals track at or below spherical control noise floors under joint refinement.

Stage 1 mathematics remains FROZEN. Design target 3×10⁻⁸ N/W is not a prediction. Stage-3 experiment is not justified by present evidence under these choices.

---

## Paths closed (all null or non-physical proxy)

| Path | Result |
|------|--------|
| Surface geometric proxy | O(1) but not a PDE solution |
| Surface electrostatic | Machine zero |
| Interior Yukawa Dirichlet | Vanishing under refinement |
| Exterior scalar E2 Yukawa | Tet ≤ sphere floor (ratio 0.09–0.38) |
| **Proca P-E2 nodal scout** | **Tet ≤ sphere floor (ratio 0.11–0.50)** |

---

## Nédélec policy

Nédélec edge elements would likely lower the absolute noise floor but will not convert a sub-floor residual into a physical force for this BVP. Further Nédélec work for Proca P-E2 is **halted** unless a new, independently motivated BC or constitutive map is introduced.

---

## Claim flags (locked)

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
target_fitting_performed    = false
```

Further Stage-2 work requires a new map that passes the spherical paired-floor test **above** the noise floor without target fitting.
