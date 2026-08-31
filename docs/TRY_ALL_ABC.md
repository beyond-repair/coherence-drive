# TRY ALL — A / B / C Execution Record

**Date:** 2026-08-30  
**Claim flags:** all false

---

## A — Proca / info stress from action

**Lagrangian (minimal):**
\[
\mathcal{L}
=
-\tfrac14 F_{\mu\nu}F^{\mu\nu}
+
\tfrac12 m^2 A_\mu A^\mu.
\]

**Stress (standard Proca):**
\[
T_{\mu\nu}
=
F_{\mu}{}^{\lambda}F_{\nu\lambda}
-
\eta_{\mu\nu}\mathcal{L}
+
m^2\Big(A_\mu A_\nu-\tfrac12\eta_{\mu\nu}A^2\Big).
\]

**CFT identification:**
\[
I_{\mu\nu}:=T_{\mu\nu}^{\rm info}.
\]

Static longitudinal proxy (Yukawa \(\phi\), \(\mathbf{E}\sim-\nabla\phi\)):
\[
\rho_\zeta \sim T_{00}
\sim
\tfrac12|\mathbf{E}|^2+\tfrac12 m^2\phi^2.
\]

**Numeric (0.45 mesh, offset Yukawa):** surface \(|F|\) nonzero as discrete residual; **not** continuum reactionless thrust. Free-field continuum still requires \(F_{\rm total}=0\) at infinity.

---

## B — Dual-surface Class B sketch

\[
\mathbf{F}_d=-\oint_{\rm device}\langle T\rangle\cdot n\,dA,
\qquad
\mathbf{F}_X=\oint_{S_\infty}\langle T\rangle\cdot n\,dA
\propto\int\hat n|f|^2\,d\Omega.
\]

**Scout result:** magnitude \(\epsilon_F\) **not closed** (device-side and far-field proxies used different normalizations). Direction anti-alignment imperfect in single-layer model.

**Required next:** same stress tensor, same units, both surfaces → \(\epsilon_F\to 0\) under refinement.

---

## C — Scalar \(\Psi\) Lagrangian → mesh flux

\[
\mathcal{L}=\tfrac12(\partial\Psi)^2-\tfrac12 m^2\Psi^2,
\qquad
T^{ij}=\partial^i\Psi\partial^j\Psi-\delta^{ij}\big(\tfrac12|\nabla\Psi|^2+V\big).
\]

| Surface | \(|F|\) (scout) |
|---------|----------------|
| 0.45 mesh, offset Yukawa | \(O(10^{-1})\) residual |
| Sphere \(R=1.5\), centered | \(O(10^{-5})\) |

Sphere control much smaller → residual is geometry/offset/discretization, not a validated continuum drive force.

---

## Verdict after trying all three

| Track | Outcome |
|-------|---------|
| A | \(T^{\rm info}\) **structure** from action — **done**; static net continuum force — **not established** |
| B | Dual-surface **protocol** exercised; magnitude \(\epsilon_F\) — **still open** |
| C | \(T_\Psi\) on mesh **done**; sphere null **consistent**; no reactionless thrust |

```
thrust_validated = false
experimental_validation = false
reactionless_closed_thrust = false
target_fitting_performed = false
epsilon_F_magnitude_closed = false
```

**What worked:** action-level \(T^{\rm info}\) identification with CFT \(I_{\mu\nu}\); sphere vs mesh control logic; Class B direction bookkeeping framework.

**What did not work:** extracting reactionless closed-box thrust; closing \(\epsilon_F\) magnitudes without a single normalized \(T\) on both surfaces.
