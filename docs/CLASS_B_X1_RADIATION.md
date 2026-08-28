# Class B Channel X₁ — Radiated Ψ Momentum

**Status:** Framework complete; laboratory thrust **not** established  
**Claim flags:** all false

---

## Established chain

Time-harmonic field \(\Psi=\Re\{\psi e^{-i\omega t}\}\).

**Cycle-averaged stress**

$$
\langle T^{ij}\rangle
=
\tfrac12\Re[(\partial^i\psi)(\partial^j\psi)^*]
-
\delta^{ij}\Big(\tfrac14|\nabla\psi|^2+\tfrac14 m^2|\psi|^2\Big).
$$

**Far-field momentum flux**

$$
\langle F_X^i\rangle
=
\oint_{S_\infty}\langle T^{ij}\rangle n_j\,dA
\propto
\int |f(\hat n)|^2\,\hat n^i\,d\Omega.
$$

**Asymmetry factor**

$$
\mathcal{A}
=
\frac{\int \hat n\,|f|^2\,d\Omega}{\int |f|^2\,d\Omega},
\qquad
|\mathcal{A}|\in[0,1].
$$

**Conservation**

$$
F_{\rm device}+F_X=0,
\qquad
\frac{dP_{\rm total}}{dt}=0.
$$

Geometry enters only through BCs that shape \(f(\hat n)\) — antenna pattern, not a divergence-theorem loophole.

---

## Relation to proxy \(\mathcal{G}_A\)

Historical geometric proxy \(\mathcal{G}_A=\oint(\nabla\Psi_{\rm proxy})\cdot n\,dA\) is **replaced** as the force observable by

$$
\langle F_X\rangle=\oint_{S_\infty}\langle T^{ij}\rangle n_j\,dA.
$$

Derived from action + stress, not geometry alone.

---

## Scout numerical note (order-of-magnitude only)

Single-layer Helmholtz face sources on an asymmetric tet (z-scale 0.45):

| Drive | \(|\mathcal{A}|\) (scout) |
|-------|-------------------------|
| Isotropic sample floor | \(\sim 10^{-4}\) |
| Equal face drive | \(\sim 10^{-4}\) |
| Aft-only / fore-only | \(\sim 5\times 10^{-3}\), direction flips with face |

**Not** a laboratory prediction. Full surface Helmholtz BEM required for quantitative \(F/P\).

---

## Project status

| Item | Status |
|------|--------|
| Action-based stress tensor | Complete |
| Cycle-averaged formulation | Complete |
| Far-field momentum observable | Complete |
| Conservation bookkeeping | Complete |
| Class B formalism | Complete |
| Closed-system reactionless thrust | **Not derived** |
| Experimental thrust prediction | **Not computed** |
| Validation against measurement | **Not performed** |

```
thrust_validated = false
experimental_validation = false
target_fitting_performed = false
reactionless_closed_thrust = false
```

---

*Most defensible next engineering step: full outgoing Helmholtz (or EM) BEM on the real 0.45 mesh → extract \(f\) → \(\mathcal{A}\) → \(\langle F\rangle/P_{\rm in}\) as an open prediction, never fitted to \(3\times 10^{-8}\,\mathrm{N/W}\).*
