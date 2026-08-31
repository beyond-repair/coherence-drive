# Defined Field Problem for Class B \(\mathcal{A}\)

**Status:** Geometry and BVP specified; full BEM still approximate in scout  
**Claim flags:** false

---

## Requirement (agreed)

\(\mathcal{A}=\int\hat n|f|^2\,d\Omega\,/\,\int|f|^2\,d\Omega\) cannot be computed from artwork. It requires a field problem.

## Geometry definition (no upload required)

Canonical generator:

[sierpinski-geometry-045/sierpinski_generator.py](https://github.com/beyond-repair/sierpinski-geometry-045)

```text
generate_asymmetric_sierpinski(
    alpha=0.45,
    n_aft=1|2|3,
    n_fore=1,
    aft_vertex=3
) → (vertices, faces)
```

Optional: `python sierpinski_generator.py --stl out.stl --n-aft 3 --n-fore 1`

## Field problem (Class B X₁ scout)

$$
(\nabla^2+k^2)\psi = 0
\quad\text{in exterior (approx. via single-layer potential on faces)},
$$

**Drive:** surface density \(\sigma=1\) on faces with centroid \(z < \mathrm{median}(z)\) (aft-biased), else \(\sigma=0.05\).

**Far field:** \(\psi\sim e^{ikr}f(\hat n)/r\), then

$$
\mathcal{A}
=
\frac{\int\hat n\,|f|^2\,d\Omega}{\int|f|^2\,d\Omega}.
$$

## Scout results (single-layer, \(k=2.5\))

| n_aft | faces | \(|\mathcal{A}|\) aft-biased | \(|\mathcal{A}|\) equal drive |
|------:|------:|----------------------------:|-----------------------------:|
| 1 | 12 | ~0.0048 | ~0.0017 |
| 2 | 18 | ~0.0049 | ~0.0018 |
| 3 | 36 | ~0.0057 | ~0.0019 |

Aft bias increases \(|\mathcal{A}|\) vs equal drive in this approximation. **Not** a laboratory \(F/P\). Full exterior Helmholtz BEM / FEM with true radiation BC is required for quantitative prediction.

## Conservation

$$
F_{\rm device}=-F_X,
\qquad
F_X\propto\int|f|^2\hat n\,d\Omega.
$$

No reactionless closed thrust. No target fitting.

```
thrust_validated = false
experimental_validation = false
```
