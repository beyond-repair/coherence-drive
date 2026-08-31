# Class B \(\mathcal{A}\) — Defined / Estimated / Validated

**Claim flags:** all false  
**Related:** CLASS_B_X1_RADIATION.md, CLASS_B_DEFINED_BVP.md

---

## Layers

| Layer | Content | Status |
|-------|---------|--------|
| **Defined** | `generate_asymmetric_sierpinski(α=0.45,…)`; observable \(\mathcal{A}\); \(F_{\rm device}=-F_X\) | **Yes** |
| **Estimated** | Single-layer scout \(\|\mathcal{A}\|\sim 10^{-3}\)–\(10^{-2}\) | **Plausible, approximate** |
| **Validated** | Full exterior Helmholtz/BEM + convergence + lab | **No** |

---

## Defined (sufficient without STL upload)

Geometry: [sierpinski-geometry-045](https://github.com/beyond-repair/sierpinski-geometry-045) generator.  
Observable:

$$
\mathcal{A}
=
\frac{\int\hat n\,|f|^2\,d\Omega}{\int|f|^2\,d\Omega}.
$$

Conservation: ordinary Class B wave recoil. **Not** reactionless propulsion.

---

## Estimated — convergence scout (single-layer only)

**Mesh depth** (\(k=2.5\), aft-biased vs equal drive):

| n_aft | faces | \(\|\mathcal{A}\|_{\rm aft}\) | \(\|\mathcal{A}\|_{\rm eq}\) |
|------:|------:|---------------------------:|--------------------------:|
| 1 | 12 | 0.0025 | 0.0016 |
| 2 | 18 | 0.0027 | 0.0018 |
| 3 | 36 | 0.0032 | 0.0020 |

**\(k\) sweep** (\(n_{\rm aft}=2\)):

| \(k\) | \(\|\mathcal{A}\|_{\rm aft}\) | \(\|\mathcal{A}\|_{\rm eq}\) |
|------:|---------------------------:|--------------------------:|
| 1.0 | 0.0026 | 0.0018 |
| 2.5 | 0.0027 | 0.0018 |
| 5.0 | 0.0035 | 0.0017 |
| 7.5 | 0.0033 | 0.0011 |

Aft bias stays above equal-drive in this model; values remain \(O(10^{-3})\). **Not** a converged BEM result.

---

## Consequence (order of magnitude, not a claim)

$$
F \sim \frac{P}{v_{\rm phase}}\,\|\mathcal{A}\|.
$$

If \(\|\mathcal{A}\|\approx 5\times 10^{-3}\) and air sound \(v\approx 343\,\mathrm{m/s}\):

$$
F/P \sim 1.5\times 10^{-5}\,\mathrm{N/W}
\quad\text{(ordinary acoustic recoil example only)}.
$$

Mildly directional pattern ≈ 0.5% of the radiated momentum budget in the net direction. Neither spectacular nor impossible.

---

## What would move Estimated → stronger

| Study | Requirement |
|-------|-------------|
| Mesh / depth refinement table | Full surface Helmholtz or FEM-BEM |
| \(k\) sweep on same solver | Stable \(\|\mathcal{A}\|\) trend |
| Sphere control | \(\|\mathcal{A}\|\to 0\) |
| Lab | Measured force + input power + field accounting |

---

## Assessment (locked)

| Item | Status |
|------|--------|
| Geometry definition | Sufficient |
| Observable \(\mathcal{A}\) | Properly defined |
| Conservation | Correct (Class B) |
| Scout \(\|\mathcal{A}\|\sim 5\times 10^{-3}\) | Plausible estimate |
| Engineering prediction | **Not yet** |
| Reactionless propulsion | **None** |
| 0.45 geometry can bias a radiated pattern | **Potentially yes** — needs reproducible exterior solve |

```
thrust_validated = false
experimental_validation = false
target_fitting_performed = false
reactionless_closed_thrust = false
class_B_A_validated = false
```
