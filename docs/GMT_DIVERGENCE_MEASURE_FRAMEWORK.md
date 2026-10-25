# Formal GMT / Divergence-Measure Framework for the 0.45-Scale Asymmetric Recursive Boundary

**Status:** Mathematical governance document (not a thrust claim)  
**Claim flags:** all false  
**Related:** STAGE2_ACCEPTANCE_CRITERION.md, ARCHIVED_NULL_REOPEN_POLICY.md, MOMENTUM_PINCH (satellite)

---

## 1. Measure-Theoretic Setting

### 1.1 Recursive Geometry

Let \(\Omega_0\subset\mathbb{R}^3\) be a compact polyhedral seed (e.g. tetrahedral hull).

Define an asymmetric recursive operator \(\mathcal{R}_{0.45}\) consisting of a finite family of similarity maps

\[
S_i(x)=0.45\,R_i x+t_i,
\]

with asymmetric placement rules. **Note:** \(0.45\) is a **linear scale ratio**, not an angle of \(45^\circ\).

The depth-\(n\) approximant is

\[
\Omega_n=\mathcal{R}_{0.45}^n(\Omega_0).
\]

Assume \(\Omega_n\subset\Omega_{n-1}\) (or the appropriate monotonic construction for the chosen solid/gasket variant) and every \(\Omega_n\) is polyhedral. Then each \(\Omega_n\) is a set of **finite perimeter**:

\[
P(\Omega_n)=\mathcal{H}^2(\partial^*\Omega_n)<\infty.
\]

The reduced boundary \(\partial^*\Omega_n\) is countably \(\mathcal{H}^2\)-rectifiable and admits a measure-theoretic outer normal \(\nu_n\).

### 1.2 Convergence to the Recursive Limit

Assume \(\Omega_n\to\Omega_\infty\) in \(L^1_{\mathrm{loc}}\) and/or Hausdorff sense (as appropriate to the construction). Three cases:

| Case | Condition | Consequence |
|------|-----------|-------------|
| **A — Finite perimeter limit** | \(\sup_n P(\Omega_n)<\infty\) | \(\Omega_\infty\) remains finite perimeter; \(D\mathbf{1}_{\Omega_n}\rightharpoonup D\mathbf{1}_{\Omega_\infty}\); classical GMT applies |
| **B — Infinite perimeter limit** | \(P(\Omega_n)\to\infty\) | May leave \(BV\); reduced-boundary flux representation may fail to capture the limit |
| **C — Fractal boundary limit** | \(\dim_H(\partial\Omega_\infty)=D_h\) (often \(\neq 2\)) | Natural measure \(\mu_h=\mathcal{H}^{D_h}\llcorner\partial\Omega_\infty\) need **not** equal \(|D\mathbf{1}_{\Omega_\infty}|\) |

**Central distinction:** The classical Gauss–Green theorem couples volume divergence to **perimeter / reduced-boundary measure**, not automatically to an arbitrary \(\mathcal{H}^{D_h}\).

---

## 2. Divergence-Measure Stress Fields

Let \(T_{\mathrm{eff}}\in L^1_{\mathrm{loc}}\) with distributional divergence a finite vector-valued Radon measure:

\[
T_{\mathrm{eff}}\in DM.
\]

Schematic decomposition:

\[
\operatorname{Div}T_{\mathrm{eff}}
=
(\operatorname{Div}T_{\mathrm{eff}})_{\mathrm{bulk}}
+
\mu_\partial,
\]

with \(\mu_\partial\) supported on the boundary (when such a splitting is meaningful).

| Model | \(\mu_\partial\) |
|-------|----------------|
| Pure bulk balance | \(=0\) |
| Classical surface source | \(g\,\mathcal{H}^2\llcorner\partial^*\Omega\) |
| Fractal surface source | \(g\,\mathcal{H}^{D_h}\llcorner\partial\Omega_\infty\) |

The fractal surface-source case is **not** implied by geometry alone. It is an **additional constitutive postulate**.

---

## 3. Conditions for Non-Zero Net Flux

Define

\[
F_n
=
\int_{\partial^*\Omega_n}
T_{\mathrm{eff}}\,\nu_n\,d\mathcal{H}^2.
\]

Gauss–Green (finite perimeter) yields

\[
F_n
=
\langle\operatorname{Div}T_{\mathrm{eff}},\mathbf{1}_{\Omega_n}\rangle
\]

in the appropriate duality sense (classical integral form when \(\operatorname{Div}T\) is integrable).

### Theorem 1 (Finite-\(n\) closure)

If \(\operatorname{Div}T_{\mathrm{eff}}=0\) distributionally on a neighborhood of \(\overline{\Omega}_n\) (or in the bulk with zero boundary measure), then

\[
F_n=0.
\]

**Asymmetry of the 0.45 recursion does not by itself generate net momentum imbalance.**

### Theorem 2 (Limit of conservative approximants)

Assume uniform integrability of the relevant traces, \(\operatorname{Div}T_{\mathrm{eff}}=0\) (no singular boundary measure), and a conservative discretization. Then

\[
F_n\to 0,
\]

even if \(P(\Omega_n)\to\infty\) or \(\dim_H(\partial\Omega_\infty)\neq 2\).

**Infinite perimeter does not imply non-zero net force.**

### Necessary escape routes for \(F_\infty\neq 0\)

| Route | Content |
|-------|---------|
| **A** | Explicit boundary measure \(\mu_\partial\neq 0\) |
| **B** | Non-zero bulk source \((\operatorname{Div}T)_{\mathrm{bulk}}\neq 0\) |
| **C** | Non-Euclidean energy calculus (e.g. Kigami resistance forms) with a redefined flux object — not classical \(Tn\) |

### What geometry alone cannot do

There is **no** standard GMT theorem implying

\[
\operatorname{Div}T_{\mathrm{eff}}=0
\quad\Longrightarrow\quad
\int_{\partial\Omega_\infty} T_{\mathrm{eff}}n\,d\mathcal{H}^{D_h}\neq 0
\]

merely because \(D_h\neq 2\).

---

## 4. Numerical Diagnostic Protocol

| Phase | Action |
|-------|--------|
| **I — Geometry ladder** | Build \(\Omega_n\) with frozen 0.45 recursion; track \(P(\Omega_n)\), \(\mathcal{H}^2(\partial\Omega_n)\), empirical dimension estimates |
| **II — Frozen field solve** | Freeze PDE, constitutive map, BCs, stress definition; no target-derived parameters |
| **III — Flux diagnostics** | \(F_{n,h}=\int_{\partial\Omega_n} T n\,dA\), \(R_{n,h}\approx\int \operatorname{Div}T\); require \(|F-R|\to 0\) (discrete Gauss–Green) |
| **IV — Localization** | Partition aft/fore; \(L_n=\|F_A\|/(\|F_A\|+\|F_F\|+\varepsilon)\). High \(L\) with \(F\to 0\) = redistribution |
| **V — Controls** | Sphere and symmetric tet: \(F\to 0\). Candidate requires \(|F_n|\gg |F^{\mathrm{sph}}|,|F^{\mathrm{sym}}|\) under joint refinement |
| **VI — Artifacts** | AMR at 0.45-scale vertices (Gibbs); require \(h/(0.45)^n\to 0\) (staircasing); monitor \(|F-R|\) (conservation) |

### Formal research criterion

A continuum boundary-measure **candidate** exists only if

\[
F_n\to F_\infty\neq 0,
\]

while \(R_n\to 0\) (or the mismatch is exactly accounted for by a written \(\mu_\partial\)), controls \(\to 0\), and an explicit \(\mu_\partial\) or non-Euclidean flux law is identified.

Absent that, the GMT expectation is

\[
F_\infty=0,
\]

with recursive asymmetry producing at most **localization / stress redistribution**, not net momentum imbalance.

---

## 5. Claim flags

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
target_fitting_performed    = false
GMT_net_flux_established    = false
```

---

*This document freezes the measure-theoretic reading of the 0.45 recursive boundary program. It does not assert non-zero continuum force.*
