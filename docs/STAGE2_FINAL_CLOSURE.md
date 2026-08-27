# Stage-2 Final Numerical Closure

**Date:** 2026-08-27  
**Detailed archive:** [stress-tensor-modification/stage2_archive](https://github.com/beyond-repair/stress-tensor-modification/tree/stage2-numerical-closure/stage2_archive)  
**Claim flags:** permanently **false**

---

## Executive statement

Under the constitutive proxies and boundary-value problems tested in Stage 2, **neither the interior Dirichlet Yukawa problem nor the exterior E2 Yukawa problem supports a robust, non-vanishing physical G in the continuum limit**.

The informational surface integral in ΔF = W(n) χ_vac G is consistent with **zero** once discretisation noise is controlled. Stage 1 mathematics remains FROZEN; no claim level is elevated.

---

## Evidence

| Study | Result |
|-------|--------|
| Surface geometric proxy (A) | O(1) — proxy only, not a PDE solution |
| Surface electrostatic (B) | Machine zero |
| Interior volume Yukawa | |G| falls under refinement → vanishing |
| Exterior E2 Yukawa (v2 paired) | Tet residual tracks **below** spherical noise floor (ratio 0.09–0.38) → consistent with zero |

Exterior v2 paired floor (μ=1, E2): at R=8, n_ang=50 → sphere floor 9.2×10⁻³, tet residual 7.8×10⁻⁴.

---

## Claim flags (locked)

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
target_fitting_performed    = false
mu_fitted_to_thrust         = false
```

---

## Programme implications

1. Stage-2 numerical closure for the tested BVPs is **complete with a negative result**.
2. Stage-3 experiment is **not** justified by present numerical evidence under these constitutive choices.
3. Further work requires a new, independently motivated constitutive map or BVP that again passes the spherical-control floor test without target fitting.
4. Design target 3×10⁻⁸ N/W remains a design target, not a prediction.

Full tables and artifact index: stress-tensor-modification `stage2_archive/STAGE2_FINAL_CLOSURE.md`.
