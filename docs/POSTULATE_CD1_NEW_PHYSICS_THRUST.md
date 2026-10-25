# POSTULATE CD-1 — New-Physics Thrust Hypothesis

**Status:** RESEARCH HYPOTHESIS — not validated  
**Date:** 2026-08-31  
**Known-physics Stage-2 nulls:** remain archived (do not reopen without new law)

```
thrust_validated = false
experimental_validation = false
energy_extraction_validated = false
reactionless_closed_thrust = false   # CD-1 is NOT closed-box; it posits a new channel
target_fitting_performed = false
postulate_CD1_frozen = true
```

---

## 0. Intent

Under known physics, tested maps produced no continuum free thrust.  
CD-1 **abandons** the assumption that the standard stress-energy is the whole story inside a driven asymmetric informational geometry. It introduces an explicit new momentum source tied to measurable fields — so the claim is falsifiable, not verbal.

This is **new physics by postulate**, not a derivation from Maxwell or standard QFT.

---

## 1. Abandoned assumption

**Standard (abandoned inside Ω_drive):**

$$
\partial_\mu T^{\mu\nu}_{\rm EM+matter} = 0
\quad \text{(no external / new sector)}
$$

**CD-1 replacement inside the driven region only:**

$$
\partial_\mu T^{\mu\nu}_{\rm EM+matter}
=
- J^{\nu}_{\rm CD}
$$

where \(J^{\nu}_{\rm CD}\) is a **new** four-current of momentum exchange with an informational / coherence sector.

Outside Ω_drive and when the drive is off: \(J_{\rm CD}=0\) (recovery of standard local conservation).

---

## 2. Constitutive postulate (the new law)

Let \(\Psi\) be a real scalar informational field (or the longitudinal proxy of a Proca field) fixed by geometry and drive.

**CD-1.1 — Coherence momentum density source**

$$
\boxed{
J^{i}_{\rm CD}
=
\kappa_{\rm CD}\,
W(n)\,
S_{\rm drive}\,
\partial^{i}\Psi\,
|\nabla\Psi|^{2}
}
$$

$$J^{0}_{\rm CD} = 0$$

(in the lab frame; no free energy fountain in the postulate — power still comes from the RF/drive supply).

| Symbol | Meaning |
|--------|--------|
| \(W(n)=0.08\,e^{0.23(n-3)}\) | recursive Ware weight (Stage-1 freeze) |
| \(S_{\rm drive}\in\{0,1\}\) | 1 only when the device is actively driven |
| \(\kappa_{\rm CD}\) | **new** coupling (dimension fixed so \(J\) is force density) |
| \(\Psi\) | solved from a stated PDE + BC on the 0.45 mesh |
| \(n\) | recursion depth of the asymmetric Sierpinski boundary |

**CD-1.2 — Geometry**

Domain boundary = generate_asymmetric_sierpinski(\(\alpha=0.45\), n_aft, n_fore).  
Asymmetry enters only through \(\Psi\) and \(\nabla\Psi\), not as a hand-set force.

**CD-1.3 — κ provenance (anti-fitting rule)**

\(\kappa_{\rm CD}\) must be fixed by an **independent** protocol (e.g. null cavity calibration, or a second observable), **never** by forcing \(F/P = 3\times 10^{-8}\).

Until an independent fix exists, predictions are reported as:

$$
F^{i} = \kappa_{\rm CD}\, \mathcal{I}^{i},\qquad
\mathcal{I}^{i}=\int_{\Omega} W(n)\,S_{\rm drive}\,\partial^{i}\Psi\,|\nabla\Psi|^{2}\,dV
$$

with \(\mathcal{I}\) computed; \(\kappa\) left symbolic.

---

## 3. Net force prediction

$$
\boxed{
F^{i}_{\rm device}
=
\int_{\Omega_{\rm drive}} J^{i}_{\rm CD}\,dV
=
\kappa_{\rm CD}\,W(n)\,S_{\rm drive}
\int_{\Omega}
(\partial^{i}\Psi)\,|\nabla\Psi|^{2}\,dV
}
$$

Steady drive: compare to power \(P_{\rm in}\):

$$
\frac{F}{P_{\rm in}}
=
\kappa_{\rm CD}\,\frac{W(n)}{P_{\rm in}}
\left|
\int (\partial\Psi)|\nabla\Psi|^{2}\,dV
\right|
$$

**Channel interpretation (required honesty):**  
Momentum is postulated to enter a **coherence sector** (new physics).  
This is *not* the same as standard photon ADCE. If the sector is later identified with photons, CD-1 must reduce to Class B and obey \(1/c\).

---

## 4. Falsification protocol (how CD-1 dies)

CD-1 is **false** if any of:

1. Drive off (\(S_{\rm drive}=0\)) but net thrust remains (artifact).  
2. Symmetric control geometry (sphere / sym tet) yields the same \(|F|\) as 0.45 at equal drive (geometry independence → law wrong).  
3. Computed \(\mathcal{I}\to 0\) under mesh refinement for the chosen \(\Psi\) PDE (no residual source).  
4. Independent \(\kappa\) determination + measured \(F\) disagree beyond error.  
5. Energy accounting shows \(P_{\rm out}>P_{\rm in}\) without stored-energy draw (over-claim).

**Pass (still not "validated thrust" globally):**  
Measured \(F\) tracks \(\kappa\mathcal{I}\) across \(n=2,3,4\) with pre-registered ratios, controls null, drive-gated.

Only after pass + replication: consider elevating claim flags under ADL governance.

---

## 5. Minimal Ψ problem (so the integral is defined)

Until a deeper action is written, use a driven Helmholtz / Yukawa proxy:

$$
(-\nabla^{2}+\mu^{2})\Psi = \rho_{\rm drive}(x)
\quad\text{on }\Omega,\quad
\text{BC on }\partial\Omega_{0.45}
$$

\(\rho_{\rm drive}\) supported on aft-biased faces (experimental antenna feed).  
This is a **computable stub**, not the final ontology.

---

## 6. What CD-1 does not claim

- Not derived from Maxwell or standard Proca alone.  
- Not ADCE photon ceiling unless sector = photons.  
- Not galactic CFT proof.  
- Not pineal / Master-Class phenomena.  
- Not thrust_validated.

---

## 7. Immediate numerical work order

1. Solve stub Ψ on 0.45 mesh, n_aft = 2,3,4.  
2. Compute vector \(\mathcal{I}\).  
3. Sphere control \(\mathcal{I}_{\rm sph}\).  
4. Report \(\mathcal{I}_{\rm tet}/\mathcal{I}_{\rm sph}\) — if ~1, CD-1 source is not geometry-selective.  
5. Leave \(\kappa\) symbolic.

---

## 8. One-line statement

**CD-1:** Driven asymmetric informational geometry sources a new momentum density \(J_{\rm CD}\propto W\,(\nabla\Psi)|\nabla\Psi|^{2}\); thrust is the integral of \(J_{\rm CD}\); standard local conservation is modified only inside the driven region; κ is not fit to the old target; flags stay false until experiment.
