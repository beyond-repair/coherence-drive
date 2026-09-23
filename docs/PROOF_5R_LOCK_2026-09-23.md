# Proof 5R lock — 2026-09-23

Does not unfreeze Stage 1. Does not derive W★ or W(n).

Operator kept:

    K_sym[W] = ω^{2} I - (1/2)(W H0 + H0 W),   H0 = -∇^{2}

Rejected: K = ω^{2} I - (1-W) H0.

Derived:

- K_sym[W0] = ω^{2} I - W0 H0
- finite-graph Hermitianity
- Q_W[f] = ∫ ω^{2} f^{2} - ∫ W |∇f|^{2} + (1/4) ∫ (∇^{2}W) f^{2}
- δ^{2}Γ_loop = -(1/2) Tr(G δV G δV)
- I2(k)>0 (d≥2) ⇒ unrenormalized Z_loop<0 for this kernel

Removed: Kato-Rellich for the whole insertion; local positivity W≥1 or ∇^{2}W>2ω^{2}.

Open: Z_ren, Lorentzian pole, S_W, W(x)→W(n).

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
