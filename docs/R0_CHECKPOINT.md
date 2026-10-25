# Model R0 — First Coherence Drive Integration Checkpoint

**Status:** Corrected formal result (not a thrust claim)  
**Claim flags:** all false

---

## Key distinction (locked)

$$
\text{Existence of a geometric construction}
\;\neq\;
\text{Existence of a nonzero closed-boundary force}.
$$

The proposed conclusion that effective signature causes non-canceling momentum flux is **too strong**. The derivation supports the curvature/metric construction; the claimed nonzero closed-boundary force **does not** follow from the stated assumptions.

---

## 1. Minimal coupling (defined)

$$
C^2[\Psi]
=
\alpha
+
\beta\frac{|\nabla\Psi|^2}{\Psi_0^2}
$$

$$
g_{\rm eff}^{AB}
=
\delta^{AB}
-
(1+C^2)\,n^A n^B,
\qquad
n_A=\frac{\partial_A\Psi}{|\nabla\Psi|}.
$$

Inverse (\(C\neq 0\)):

$$
g^{\rm eff}_{AB}
=
\delta_{AB}
-
\left(1+\frac{1}{C^2}\right)n_A n_B.
$$

---

## 2. Lorentzian signature — PASS

Where \(\nabla\Psi\neq 0\) and \(C^2>0\), in an adapted frame:

$$
g_{\rm eff}^{AB}=\operatorname{diag}(-C^2,1,1,1)
\quad\Rightarrow\quad
\operatorname{signature}(g_{\rm eff})=(-,+,+,+).
$$

**Interpretation:** The admissibility rule **generates a Lorentzian effective metric**. It is not yet shown that the admissibility rule itself follows from deeper Coherence Drive dynamics.

---

## 3. Curvature — COMPUTABLE

$$
\Psi \rightarrow g_{\rm eff} \rightarrow \Gamma \rightarrow R \rightarrow G_{\rm eff}
$$

is a valid calculational chain (\(\Gamma=\mathcal{O}(\partial^2\Psi)\), \(R=\mathcal{O}(\partial^3\Psi)+\mathcal{O}((\partial^2\Psi)^2)\) schematically).

---

## 4. Geometric stress — DEFINED / OPEN as physical \(T\)

$$
T_{\rm geom}^{AB}
=
\frac{1}{8\pi G} G_{\rm eff}^{AB}
$$

is a **computable effective source**. Locked distinction:

$$
T_{\rm geom}
\neq
\text{automatically a fundamental physical }T_{\rm eff}.
$$

An action and dynamical equation for \(\Psi\) are still required. **R2: PARTIAL / OPEN.**

---

## 5–8. Closed-boundary force — NOT ESTABLISHED

$$
F_A
=
\oint_{\partial\Omega} T_{AB}^{\rm eff} N^B\,d\Sigma
=
\int_\Omega \nabla_B T_A{}^B\,dV
$$

(with the appropriate covariant formulation).

If \(\nabla_B T_A{}^B=0\), then **\(F_A=0\)**.

Asymmetric \(\Psi\) can produce asymmetric **local** stress. That does **not** imply net momentum creation:

$$
\text{asymmetric field}
\Rightarrow
\text{asymmetric local stress}
\quad\text{(yes)},
$$
$$
\text{asymmetric field}
\Rightarrow
\text{net momentum creation}
\quad\text{(not from conservation alone)}.
$$

For a localized field with translationally invariant asymptotics and no external momentum source, complete closed-system balance requires \(F_{\rm total}=0\).

**Corrected R0 conclusion:**

$$
\mathcal{A}\rightarrow\mathcal{C}\rightarrow g_{\rm eff}\rightarrow G_{\rm eff}\rightarrow T_{\rm geom}
$$

is viable as a formal construction.

$$
T_{\rm geom}\rightarrow F_{\rm closed}\neq 0
$$

does **not** follow. Under conservation, \(F_{\rm closed}=0\).

---

## 9. What this strengthens

The remaining question is not “can asymmetry produce asymmetric stress?” (yes). It is:

$$
\textbf{Where does the equal and opposite momentum go?}
$$

Legitimate channels: \(\Psi\)-field momentum; another dynamical field; external/background sector; radiation; boundary/environment; time-dependent geometry. If none exists, a closed-system reactionless force is excluded.

---

## 10. Revised gate status

| Component | Result |
|-----------|--------|
| Euclidean relational substrate | PASS |
| Field-defined preferred direction | PASS |
| Admissibility cone | PASS as postulate |
| Lorentzian metric reconstruction | PASS |
| Lorentzian signature | PASS |
| \(C[\Psi]\) coupling | DEFINED |
| Curvature \(R[g_{\rm eff}]\) | COMPUTABLE |
| Einstein tensor | COMPUTABLE |
| Geometric \(T_{\rm eff}\) | DEFINED |
| Fundamental physical \(T_{\rm eff}\) | OPEN |
| Conservation law | MUST BE DERIVED |
| Asymmetric local stress | POSSIBLE |
| Nonzero closed-boundary force | **NOT ESTABLISHED** |
| Reactionless thrust | **NOT ESTABLISHED** |
| Momentum source/channel | OPEN |
| Experimental prediction | OPEN |

---

## 11. Decisive next calculation

Do **not** assume nonzero force. Derive the conservation identity for the coupled system:

$$
\nabla_B\big(
T_{\rm matter}^{AB}+T_\Psi^{AB}+T_{\rm geom}^{AB}+T_{\rm interaction}^{AB}
\big)=0,
$$

then evaluate

$$
\oint_{\partial\Omega} T_{\rm total}^{AB} N_B\,d\Sigma.
$$

| Outcome | Meaning |
|---------|---------|
| **A** — \(F_{\rm total}=0\) | R0 cannot produce reactionless thrust |
| **B** — \(F_{\rm device}\neq 0\), \(F_{\rm total}=0\) | Viable if momentum-transfer channel is identified |
| **C** — \(F_{\rm total}\neq 0\) | Violates conservation unless a dynamical sector was omitted |

---

## R0 checkpoint (strongest justified result)

$$
\textbf{R0 establishes a candidate relational-to-Lorentzian geometric bridge,}
$$

but does **not** yet establish force generation.

Explicit pathway now available for action-level analysis:

$$
\Psi_{\rm info}\rightarrow C[\Psi]\rightarrow g_{\rm eff}[\Psi]\rightarrow G_{\rm eff}[\Psi].
$$

**Next rigorous target:** explicit \(S[\Psi]\), then exact \(T_\Psi^{AB}\) and total momentum balance — the point at which R0 either becomes a coherent extension or is killed.

```
thrust_validated            = false
experimental_validation     = false
F_closed_nonzero_established = false
target_fitting_performed    = false
```
