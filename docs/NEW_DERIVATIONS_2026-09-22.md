# New derivations from the existing corpus — 2026-09-22

These are implications of objects already written. They are not a new theory
and they do not derive \(W_\star\). Stage 1 freeze is unchanged.

## N1. Closed-surface theorem for the coded informational stress

`physics_evaluator.informational_stress` is

$$
\sigma_{ij}[a] = w\Bigl(a_i a_j - \tfrac12 |a|^2\delta_{ij}\Bigr).
$$

On any closed surface, \(F_i=\oint \sigma_{ij}n_j\,dA\).

**Lemma.** If \(a\) is constant, \(\sigma\) is constant, so \(F=0\).  
**Lemma.** If the surface is a sphere and \(a\parallel n\), traction is radial and odd under \(n\to-n\) after pairing, so \(F=0\) (confirmed on the repo quadrature at \(10^{-16}\)).

**Corollary.** A net force from this template requires an \(a\) that is neither uniform nor a pure radial monopole. A coded example \(a=(1+\varepsilon z)\hat x\) on the unit sphere produces a nonzero \(F_z\) at \(\varepsilon=0.1\).

**Conservation.** For a genuine continuum stress, \(\oint\sigma\cdot n=\int_V\nabla\cdot\sigma\). The dyad above is not obtained from \(\delta S/\delta g_{\mu\nu}\) and is not divergence-free for generic \(a(x)\). Therefore a nonzero \(F\) is the integral of a hand-specified \(\nabla\cdot\sigma_{\rm info}\), not a vacuum thrust theorem.

## N2. Optimization residual cannot land on 0.08 by default

Theorem A (in-tree) on a \(k\)-ary tree:

$$
x_0^*=\bar x\,\frac{\sum_{d=0}^D(ka)^d}{\sum_{d=0}^D(ka^2)^d}.
$$

Residual \(R_D=\frac1{N_D}\sum_i 1_{|x_i-\bar x|>\varepsilon}\).

**Proposition.** If \(|ka|<1\) and \(\varepsilon<|\bar x|\), then as \(D\to\infty\) one has \(a^d x_0^*\to 0\) on almost all nodes (leaves dominate), so \(R_D\to 1\).
Numeric check: \((k,a)=(2,0.4)\), \(\delta=0.5\) gives \(R_3\approx0.87\), \(R_8\approx0.996\), \(R_{15}\approx1\).

**Proposition.** The infinite-\(D\) closed form in Theorem A requires \(|ka|<1\). In that regime the obstruction limit is \(1\), not \(0.08\).

Matching \(\mathcal{W}\to 0.08\) is a parameter fit (CONJECTURE.md target). It is not a derivation of Ware.

## N3. Two uses of 0.45 give two BTFR exponents

Log-ansatz: \(v_\infty^2=W_\star GM/r_0\).

- If \(r_0\propto M^{0.40}\) (the written \(\alpha-0.05\) line), then \(v_\infty\propto M^{0.30}\).
- If \(r_0\propto M^{0.45}\) (the other 0.45), then \(v_\infty\propto M^{0.275}\).

`Ware-Full-Action.tex` quotes \(0.275\). `Math.md` quotes \(r_0\propto M^{0.40}\). Those cannot both follow from one scaling. The geometric design ratio \(\alpha_{\rm geom}=0.45\) is a third object and does not pick the exponent.

## N4. Target vs photon ceiling is a factor of nine

Already in `PHOTON_CLASS_B_CEILING.md`. Restated as a necessary condition:

$$
\frac{(\Delta F/P)_{\rm target}}{1/c}\approx 9.00.
$$

Any channel that hits \(3\times10^{-8}\,\mathrm{N/W}\) is not Class B EM. This does not construct the channel.

## What this pass did not find

- A proof that \(W_\star=1/(4\pi)\) from the Proca action without \(c_\star=1\).
- A proof that gasket spectrum, Kigami factors, or tilt \(F\) equal \(0.08\).
- A conserved \(\Delta T_W\) that yields laboratory thrust.
- Anything that licenses unlocking Stage 1.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
