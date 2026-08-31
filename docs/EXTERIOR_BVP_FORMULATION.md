# Exterior / Transmission BVP for Ψ_info

**Status:** Design specification. No exterior numerical solution claimed.  
**Parent archive:** stress-tensor-modification `stage2_archive/`  
**Claim flags:** all false.

## Exterior Yukawa (first exterior path)

Domain: Ωᶜ = ℝ³ \ Ω̄ (Ω = solid tetrahedron / craft).

```
−∇²Ψ + μ²Ψ = 0     in Ωᶜ
Ψ → 0 at infinity (Yukawa decay for μ > 0)
```

Hull BC options (non-force-encoding):

| ID | Condition | Notes |
|----|-----------|-------|
| E1 | ∂ₙΨ = 0 | Homogeneous Neumann |
| E2 | Ψ = const | Linearly scalable; no angular data |
| E3 | ∂ₙΨ + αΨ = 0 | α > 0 fixed, never fitted to force |
| E4 | Transmission | Continuity of Ψ and normal flux; interior equation optional |

## Null tests required

1. μ → ∞ ⇒ Ψ → 0 ⇒ G → 0  
2. Spherical control hull ⇒ G → 0 by symmetry  
3. Combined hull + truncation-radius refinement reported  

## Prohibited

Fitting μ, α, or any boundary/source amplitude to the design target 3×10⁻⁸ N/W.  
Elevating thrust_validated or experimental_validation from an exterior residual alone.

## Exit criteria

Mesh-converged G under independent constraints + sphere control + claim flags still false unless a separate ADL-Governance claim-validation process is completed.

Full detail: stress-tensor-modification/stage2_archive/EXTERIOR_BVP_FORMULATION.md
