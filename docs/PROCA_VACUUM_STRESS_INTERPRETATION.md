# Proca Vacuum, Exterior Domain, and Stress Interpretation

**Status:** Permanent scientific-governance record  
**Claim flags:** all false  
**Related:** STAGE2_ACCEPTANCE_CRITERION.md, STAGE2_FINAL_CLOSURE.md

---

## 1. Vacuum solutions ≠ net force

Linear Proca theory

```text
(□ + m²) A^μ = 0,
∂_μ A^μ = 0
```

admits plane waves, wave packets, static Yukawa multipoles in exterior domains, and superpositions thereof.

**None of those facts alone imply a nonzero closed-surface momentum flux.**

Existence of a nontrivial Proca vacuum solution is not existence of a nonzero net force. Speculative propulsion arguments that collapse this distinction are rejected by this archive.

---

## 2. Exterior-domain classification

Coherence Drive exterior problems are:

> **vacuum PDEs with boundary data**

- The exterior region satisfies homogeneous Proca (or Yukawa) equations.
- Nontrivial fields exist because boundary conditions are imposed on the hull.

This is **different from**:

- source-free global Minkowski vacuum,
- spontaneous vacuum anisotropy,
- vacuum energy extraction.

Those distinctions remain explicit in repository documentation.

---

## 3. Stress tensor and momentum accounting

Conservation identity:

```text
d/dt ∫_V T^{0i} dV  =  − ∮_{∂V} T^{ji} n_j dA
```

Any claimed force must sit inside a **complete momentum accounting** framework. A surface integral alone is not sufficient evidence of propulsion.

One must also establish:

1. where momentum is stored,
2. where momentum leaves,
3. whether radiation terms exist,
4. whether boundary reactions are fully represented.

Proca working stress used in Stage-2:

```text
T_eff = T_M + T_P
```

(Maxwell-like + mass term). Definition frozen for the archived P-E2 branch.

---

## 4. Stage-2 numerical interpretation

Strongest numerical conclusion for tested branches:

```text
|G|_tet  ≤  |G|_sphere
```

with both decreasing under refinement.

This does **not** prove G = 0 as a mathematical identity for every conceivable map.  
It **does** establish that the solved numerical problem failed to demonstrate a continuum residual above the control floor — the standard required by STAGE2_ACCEPTANCE_CRITERION.md.

---

## 5. Programme fork

### Archived branch (closed)

| Branch | Status |
|--------|--------|
| Scalar paths | tested → negative closure → archived |
| Proca P-E2 | tested → negative closure → archived |

### Future branch (only if all specified beforehand)

1. New constitutive law  
2. New boundary-condition class  
3. New stress definition (if altered)  
4. Independent physical motivation  
5. No target-derived parameter choices  

Then apply the five-step acceptance criterion again from the start.

---

## 6. What the archive actually says

The archive does **not** say: “Propulsion from field theories is impossible.”

The archive **does** say:

> Under the constitutive maps, stress definitions, and boundary-value problems actually tested, no continuum force residual was demonstrated above numerical controls.

That statement is precise, falsifiable, and tied to solved equations.

---

## 7. Final status table

| Item | Status |
|------|--------|
| Proca vacuum theory | Well-defined |
| Exterior Yukawa / Proca solutions | Established |
| Proca stress tensor | Established |
| Momentum-flux interpretation | Established |
| Continuum residual for tested P-E2 branch | **Not established** |
| Experimental thrust evidence | None |
| Energy-extraction mechanism | Undefined |
| Claim flags | **False** |
| Stage-2 governance criterion | Locked |
| Scalar branch | Archived null |
| Proca P-E2 branch | Archived null |

---

*The numerical programme has transitioned from searching for a signal on closed maps to requiring new physics assumptions before any further Stage-2 investigation is justified.*
