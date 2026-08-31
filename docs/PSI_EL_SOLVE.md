# Euler–Lagrange Solve for \(\Psi\)

**Action:** \(S=\int\big(-\tfrac12(\partial\Psi)^2-\tfrac12 m^2\Psi^2\big)\)  
**EL (static):** \((-\nabla^2+m^2)\Psi=0\) away from sources  
**Claim flags:** all false

---

## Analytic solutions

Fundamental solution (Yukawa / screened Poisson):

$$
G_m(\mathbf{x})=\frac{e^{-m r}}{4\pi r},\qquad r=|\mathbf{x}|.
$$

Linear combinations (monopole, offset monopole, dipole) satisfy the homogeneous EL equation everywhere **except** at point-source centers, where a \(\delta\)-function source appears.

Massless limit \(m\to 0\): Laplace equation, Coulomb kernel \(1/(4\pi r)\).

---

## Numerical diagnostic (\(m=1\), grid)

| Configuration | EL residual (away from centers) | Sphere \(|F|=|\oint T_\Psi\cdot n\,dA|\) |
|---------------|----------------------------------|----------------------------------------|
| Monopole at origin | Small (discretization) | \(\sim 10^{-18}\)–\(10^{-19}\) (noise) |
| Dipole along \(z\) | Small away from poles | \(\sim 10^{-18}\) (noise) |
| Offset monopole | Elevated near offset singularity | Falls rapidly with \(R\) (\(10^{-4}\to 10^{-7}\)) — grid/singularity artifact, not stable continuum thrust |

\(T_\Psi^{ij}=\partial^i\Psi\,\partial^j\Psi-\delta^{ij}\big(\tfrac12|\nabla\Psi|^2+V\big)\).

---

## Interpretation

1. Free EL solutions exist and are under control (Yukawa family).  
2. On-shell conservation implies vanishing **total** flux for localized free configurations at infinity — matched by centered monopole/dipole numerics.  
3. Asymmetry (offset source) does not establish reactionless closed-boundary force; residual finite-\(R\) flux shrinks with radius and is contaminated by the singular source.  
4. A physical “device” would require either a smooth source-free field supported by boundary data, or an explicit second sector (Class B channel).

---

## Link to R0

Pathway \(\Psi\to T_\Psi\) is now explicit. Geometric \(T_{\rm geom}[g_{\rm eff}(\Psi)]\) remains a composite diagnostic and must not be double-counted.

**Next (optional):** smooth compact-support initial data evolved or solved with boundary-value formulation (no point sources); then device-hull vs \(S_\infty\) flux comparison under the same conservation test.

```
thrust_validated             = false
F_closed_nonzero_established = false
target_fitting_performed     = false
```
