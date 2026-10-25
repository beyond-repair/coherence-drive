# Refined Class B Verification Protocol

**Status:** Protocol defined; full exterior Helmholtz not yet demonstrated  
**Claim flags:** all false

---

## 1. First-class metrics (momentum closure)

$$
\epsilon_P = \frac{|P_{\rm in}-P_{\rm rad}-P_{\rm loss}|}{|P_{\rm in}|+\delta},
\qquad
\epsilon_F = \frac{\|\mathbf{F}_d+\mathbf{F}_X\|}{|\mathbf{F}_X|+\delta}.
$$

Both must trend to zero under refinement.  
**A stable \(\mathcal{A}\) with unstable \(\epsilon_F\) is invalid.**

---

## 2. Reciprocity control (linear Helmholtz)

Mirror the drive (aft-biased ↔ fore-biased). Expect \(\mathbf{A}\to -\mathbf{A}\) (dominant component flips sign).  
Failure ⇒ numerical asymmetry, not geometry.

---

## 3. Geometry vs drive decomposition

| Case | Geometry | Drive |
|------|----------|-------|
| A | Sphere | Equal |
| B | Sphere | Aft-biased |
| C | 0.45 | Equal |
| D | 0.45 | Aft-biased |

Isolate \(\mathcal{A}_{\rm geometry}\), \(\mathcal{A}_{\rm drive}\), interaction.

---

## 4. Mesh-independence

$$
\left|\frac{\mathcal{A}_{n+1}-\mathcal{A}_n}{\mathcal{A}_n}\right| < \eta
\quad(\text{e.g. }\eta=5\%)
$$

Report ≥3 resolutions.

---

## 5. Far-field radius

\(\mathbf{F}_X(R)\) must plateau as \(R\) increases.

---

## 6. Null geometry test

Identical excitation on sphere, regular tet, 0.45, perturbed sphere.  
If \(|\mathcal{A}|\) comparable → not geometry-specific.  
If \(|\mathcal{A}_{0.45}|\gg|\mathcal{A}_{\rm controls}|\) → evidence of geometric bias.

---

## Scout control matrix (single-layer only, \(k=2.5\))

| Case | \(\|\mathcal{A}\|\) | \(A_z\) |
|------|------------------:|--------:|
| A sphere equal | 0.0016 | +0.0009 |
| B sphere aft | 0.0030 | −0.0027 |
| C 0.45 equal | 0.0018 | +0.0010 |
| D 0.45 aft | 0.0027 | −0.0021 |
| D reciprocal (fore) | 0.0039 | +0.0037 |
| tet equal | 0.0016 | +0.0009 |
| tet aft | 0.0016 | −0.0009 |

**Read:** Reciprocity roughly holds (sign flip). Drive bias dominates; sphere+aft also produces \(\|\mathcal{A}\|\). Unique 0.45 advantage **not** established in this scout.

Mesh depth aft-biased: \(\|\mathcal{A}\|\) 0.0025 → 0.0032 for \(n_{\rm aft}=1\to3\).

\(\epsilon_P,\epsilon_F\) **not reported** (require full dual-surface stress solve).

---

## Maturity

| Component | Status |
|-----------|--------|
| Observable \(\mathcal{A}\) | Defined |
| Conservation identity | Defined |
| Class B accounting | Defined |
| Scout signal | Estimated |
| Exterior Helmholtz | **Not demonstrated** |
| Momentum-closure residuals | **Not reported** |
| Geometry-control suite | Scout only / incomplete |
| Mesh-independence proof | **Not demonstrated** |
| Experimental verification | **Not performed** |

---

## Next major milestone

Demonstrate that \(\mathcal{A}\) survives:

1. Rigorous convergence (\(\epsilon_P,\epsilon_F\to 0\) + mesh independence),  
2. Full control suite (reciprocity, null geometry, bias decomposition),  
3. Far-field plateau of \(\mathbf{F}_X(R)\).

**If achieved:**  
> “The 0.45 geometry biases the radiated wave pattern.”  

Testable; **distinct from reactionless propulsion.**

```
thrust_validated = false
experimental_validation = false
class_B_A_validated = false
reactionless_closed_thrust = false
```
