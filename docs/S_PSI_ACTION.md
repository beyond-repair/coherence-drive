# Candidate Action \(S[\Psi]\) for R0

**Status:** Formal field-theoretic construction (not a thrust claim)  
**Prerequisite:** [R0_CHECKPOINT.md](R0_CHECKPOINT.md)  
**Claim flags:** all false

---

## 0. Purpose

R0 defined a map

$$
\Psi \rightarrow C[\Psi] \rightarrow g_{\rm eff}[\Psi] \rightarrow G_{\rm eff} \rightarrow T_{\rm geom}.
$$

\(T_{\rm geom}\) is not automatically a fundamental stress. This document supplies a candidate dynamical action for \(\Psi\), the associated \(T_\Psi^{AB}\), and the total momentum balance structure.

---

## 1. Background and notation

Work on a fixed background manifold with metric \(g_{AB}\) (initially flat Euclidean or Minkowski \(\eta_{AB}\)). Coordinates \(X^A\). The informational field is a real scalar \(\Psi\).

R0 couplings (frozen from checkpoint):

$$
C^2[\Psi]
=
\alpha + \beta\frac{g^{AB}\partial_A\Psi\,\partial_B\Psi}{\Psi_0^2},
\qquad
n_A = \frac{\partial_A\Psi}{\sqrt{g^{CD}\partial_C\Psi\,\partial_D\Psi}}
$$

(when \(\nabla\Psi\neq 0\)). The effective metric \(g_{\rm eff}[\Psi]\) is a **composite** of \((\Psi,\partial\Psi)\), not an independent gravitational degree of freedom unless promoted separately.

---

## 2. Minimal free action (Level 1)

The simplest diffeomorphism-covariant kinetic action on the **background** metric \(g_{AB}\) is

$$
\boxed{
S_0[\Psi;g]
=
\int d^4X\,\sqrt{|g|}\,
\mathcal{L}_0,
\qquad
\mathcal{L}_0
=
-\frac12\,g^{AB}\partial_A\Psi\,\partial_B\Psi
-
V(\Psi).
}
$$

**Euler–Lagrange equation:**

$$
\frac{1}{\sqrt{|g|}}\partial_A\big(\sqrt{|g|}\,g^{AB}\partial_B\Psi\big)
-
V'(\Psi)
= 0,
$$

i.e. \(\square_g\Psi = V'(\Psi)\).

**Optional mass / Proca-adjacent potential (still scalar):**

$$
V(\Psi)=\frac12 m^2\Psi^2 + \frac{\lambda}{4}\Psi^4.
$$

This level does **not** yet know about \(g_{\rm eff}\); it only gives dynamics and stress for \(\Psi\) on \(g\).

---

## 3. Stress-energy of \(\Psi\) (Belinfante / metric variation)

Varying with respect to the background metric defines the Hilbert stress-energy tensor:

$$
\boxed{
T_\Psi^{AB}
:=
\frac{2}{\sqrt{|g|}}
\frac{\delta S_0}{\delta g_{AB}}.
}
$$

For \(\mathcal{L}_0\) as above:

$$
\boxed{
T_\Psi^{AB}
=
\partial^A\Psi\,\partial^B\Psi
-
 g^{AB}\Big(
\tfrac12\partial_C\Psi\,\partial^C\Psi + V(\Psi)
\Big).
}
$$

**On-shell conservation** (diffeomorphism invariance of \(S_0\) on a fixed background with Killing symmetries, or covariant conservation when coupled consistently):

$$
\nabla_B T_\Psi^{AB}=0
$$

when the EL equation holds and there are no other non-variational forces. (On curved dynamical \(g\), the full Bianchi story pairs with Einstein; here \(g\) is background.)

---

## 4. Action that knows about \(C[\Psi]\) (Level 2)

To encode the R0 admissibility structure in the **dynamics** (not only in a post-hoc metric), replace the kinetic coefficient by a function of \(C\) or of \(X:=g^{AB}\partial_A\Psi\partial_B\Psi\):

$$
\boxed{
S_C[\Psi;g]
=
\int d^4X\,\sqrt{|g|}\,
\Big(
-\tfrac12\,K(X)\,X
-
V(\Psi)
\Big),
\qquad
X=g^{AB}\partial_A\Psi\,\partial_B\Psi.
}
$$

**Minimal R0-inspired choice** (example, not fitted to thrust):

$$
K(X)
=
1 + \gamma\,\frac{X}{\Psi_0^2}
\quad\text{or}\quad
K(X)=f(C^2(X)),
$$

with \(\gamma\) a dimensionless coupling **reported, never fitted to** \(3\times 10^{-8}\,\mathrm{N/W}\).

**EL equation** (schematic):

$$
\nabla_A\big(
(K+X K')\,\partial^A\Psi
\big)
-
V'(\Psi)=0.
$$

**Stress-energy** (k-essence / P(X) form):

$$
T_\Psi^{AB}
=
(K+X K')\,\partial^A\Psi\,\partial^B\Psi
-
 g^{AB}\Big(
\tfrac12 K\,X + V
\Big).
$$

Still: on-shell \(\nabla_B T_\Psi^{AB}=0\) in the absence of external non-variational sources.

---

## 5. Geometric composite \(T_{\rm geom}\) vs dynamical \(T_\Psi\)

R0 also defined

$$
T_{\rm geom}^{AB}
=
\frac{1}{8\pi G} G_{\rm eff}^{AB}[g_{\rm eff}(\Psi)].
$$

**Critical bookkeeping rule:**

| Object | Origin | Independent DOF? |
|--------|--------|------------------|
| \(T_\Psi\) | Metric variation of \(S[\Psi;g]\) | No — built from \(\Psi\) |
| \(T_{\rm geom}\) | Einstein tensor of **composite** \(g_{\rm eff}(\Psi)\) | No — also built from \(\Psi\) |
| Einstein \(G[g]\) of dynamical metric | True gravity | Only if \(g\) is dynamical |

**Do not double-count.** If \(g_{\rm eff}\) is purely composite, \(T_{\rm geom}\) is a **repackaging** of derivatives of \(\Psi\), not an extra free sector. The physical stress entering Noether/Hilbert balance is \(T_\Psi\) (and matter), unless an independent gravitational action for a dynamical metric is introduced.

Two consistent programs:

**Program P1 — Composite only**  
Action: \(S[\Psi;g_{\rm bg}]\) only.  
Momentum: carried by \(T_\Psi\).  
\(T_{\rm geom}\) is diagnostic, not an extra source in the conservation law.

**Program P2 — Disformal / matter coupling**  
Matter action uses \(g_{\rm eff}(\Psi)\) (optical/disformal metric); gravity uses \(g\) or remains non-dynamical.  
Then interaction stress appears from variation of \(S_{\rm m}[g_{\rm eff}(\Psi)]\) w.r.t. background / coordinate shifts.

---

## 6. Total conservation identity (decisive structure)

### P1 (minimal)

$$
\boxed{
\nabla_B T_\Psi^{AB}=0
\quad\text{(on-shell)}.
}
$$

Closed-surface flux of \(T_\Psi\) vanishes for localized configurations with suitable falloff (Noether charge of spatial translations is conserved and, for a static localized blob, the net force on a large closed surface is zero).

### P2 (matter on \(g_{\rm eff}\))

$$
\boxed{
\nabla_B\big(T_\Psi^{AB}+T_{\rm m}^{AB}+T_{\rm int}^{AB}\big)=0,
}
$$

where \(T_{\rm m}\) is the stress of matter computed from \(S_{\rm m}[g_{\rm eff}]\), and \(T_{\rm int}\) accounts for the dependence of \(g_{\rm eff}\) on \(\Psi\) if not already included in \(T_\Psi\).

**Device vs total:**

$$
F_A^{\rm device}
=
\oint_{\partial\Omega_{\rm device}} (T_\Psi+T_{\rm m}+\cdots)^{AB} N_B\,d\Sigma,
\qquad
F_A^{\rm total}
=
\oint_{S_\infty} (\cdots)^{AB} N_B\,d\Sigma.
$$

Under full conservation and isolated asymptotics:

$$
F_A^{\rm total}=0.
$$

Outcome classes (from R0 checkpoint):

| Class | Content |
|-------|---------|
| A | \(F_{\rm total}=0\), no reactionless thrust |
| B | \(F_{\rm device}\neq 0\) but \(F_{\rm total}=0\) — channel identified (field, radiation, environment) |
| C | \(F_{\rm total}\neq 0\) — incomplete sector or inconsistency |

---

## 7. Recommended working action for the next calculation

**Freeze (proposal):**

$$
\boxed{
S[\Psi]
=
\int d^4X\,
\Big(
-\tfrac12\partial_A\Psi\,\partial^A\Psi
-
\tfrac12 m^2\Psi^2
\Big)
}
$$

on flat background (Level 1), with R0 \(g_{\rm eff}\) retained **only** as a geometric diagnostic until P2 is explicitly motivated.

**First conservation test:**

1. Solve EL for a localized asymmetric \(\Psi\) (numerical or analytic ansatz).  
2. Build \(T_\Psi^{AB}\).  
3. Evaluate \(\oint T_\Psi^{AB} N_B\,d\Sigma\) on large spheres and on a device hull.  
4. Expect Class A for the total; Class B only if a second sector is present and tracked.

**Do not** set \(m,\alpha,\beta,\gamma\) from the thrust target.

---

## 8. Optional upgrade path (not required to start)

1. Level 2: nontrivial \(K(X)\) tied to \(C^2\).  
2. P2: couple a probe matter field to \(g_{\rm eff}\); compute momentum exchange between \(\Psi\) and matter.  
3. Dynamical gravity: add Einstein–Hilbert for independent \(g\); then Bianchi identities constrain the sum of all stresses.

Each upgrade must restate the conservation identity before claiming force.

---

## 9. Claim flags

```
thrust_validated                 = false
experimental_validation          = false
F_closed_nonzero_established     = false
target_fitting_performed         = false
S_Psi_defined                    = true   # candidate only
T_Psi_derived                    = true   # from S_0 / S_C
conservation_identity_stated     = true
```

---

## 10. Bottom line

$$
\boxed{
S[\Psi]=\int\big(-\tfrac12(\partial\Psi)^2-V(\Psi)\big)
}
$$

yields a definite \(T_\Psi^{AB}\) and on-shell conservation. Together with R0’s geometric bridge, the theory now has an action-level handle on momentum. **Nonzero closed-boundary force is still not implied**; the next numerical/analytic task is to evaluate total vs device fluxes under this \(S[\Psi]\) and classify A/B/C.
