# Stage-2 Numerical Closure — Summary

**Date:** 2026-08-27  
**Detailed archive:** [stress-tensor-modification/stage2_archive](https://github.com/beyond-repair/stress-tensor-modification/tree/stage2-numerical-closure/stage2_archive)  
**Claim flags:** all **false**

---

## Results (no target fitting)

| Path | Constitutive choice | Continuum |G| |
|------|---------------------|----------------|
| Surface A | Geometric scalar proxy | Stable O(1) — **proxy only, not a PDE solution** |
| Surface B | Electrostatic φ (C6-style) | Machine zero |
| Volume interior Yukawa | (−∇² + μ²)Ψ = 1, Ψ = 0 on ∂Ω | **Decreases under refinement → vanishing continuum limit** |

Primary negative result: the interior Dirichlet Yukawa problem on the solid tetrahedron does **not** produce a robust non-zero G. Refinement study (μ = 1):

| refine | tets | |G| |
|-------:|-----:|----:|
| 2 | 64 | 9.3×10⁻⁵ |
| 3 | 512 | 1.6×10⁻⁵ |
| 4 | 4096 | 4.5×10⁻⁶ |

---

## Claim flags (locked)

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
target_fitting_performed    = false
mu_fitted_to_thrust         = false
```

Stage 1 mathematics remains FROZEN. This document records Stage-2 numerical evidence only.

---

## Next legitimate gate: exterior / transmission BVP

See the full formulation in the stress-tensor-modification archive:
`stage2_archive/EXTERIOR_BVP_FORMULATION.md`

Summary:

- Homogeneous Yukawa in the exterior with decay at infinity.
- Non-force-encoding hull BCs (Neumann homogeneous, constant Dirichlet, or fixed-α Robin).
- Control geometry (sphere) must yield G → 0.
- Hull + truncation-radius refinement required.
- No fitting of μ or boundary coefficients to 3×10⁻⁸ N/W.

Until an exterior study produces a mesh-converged, independently constrained, non-zero G under those rules, the suite does not possess a validated residual-force prediction.
