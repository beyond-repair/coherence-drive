# Zero-Point Energy & Reactionless Thrust — Literature Watch

**Date:** 2026-08-31  
**Purpose:** Track published claims; **not** a discovery announcement.

```
thrust_validated = false
experimental_validation = false
energy_extraction_validated = false
reactionless_closed_thrust = false
target_fitting_performed = false
```

---

## Hard constraints (unchanged)

1. Closed system: \(\nabla_\mu T^{\mu\nu}=0\) \(\Rightarrow\) \(F_{\rm total}=0\) without external channel.
2. Photon rocket: \(F/P \le 1/c \approx 3.3\times 10^{-9}\,\mathrm{N/W}\).
3. Target \(3\times 10^{-8}\,\mathrm{N/W}\) exceeds pure photon ceiling.
4. Casimir / ZPE forces are real but typically **internal** (plate–plate); net free-body thrust requires open radiation or thermal asymmetry with a channel.

---

## What recent literature actually contains

### A. Serious, small, conservation-respecting effects

| Work | Claim | Scale / status |
|------|--------|----------------|
| Milton et al., Phys. Rev. A 110, 042814 (2024) | Quantum self-propulsion of **inhomogeneous** body **out of thermal equilibrium** | Second-order in susceptibility; authors note forces **too small for a thruster**; needs sustained temperature imbalance |
| Cao et al., arXiv:2501.07908 (2025) | Asymmetric vacuum radiation from time-varying mirrors ("vacuum propellion") | Class B–like: photons carry momentum; recoil on cavity |
| Onishi & Fu, arXiv:2602.07116 (2026) | Zero-point energy in solids \(\rightarrow\) "quantum geometric force" on circuit elements | ~pN–fN lab scale; condensed-matter probe, **not** spacecraft thrust |
| Kezerashvili, Acta Astronautica / arXiv:2510.21743 | Review: solar sails, mag sails, gravity assist; Casimir path **speculative** | Standard propellantless (open systems) |

These are **not** closed reactionless vacuum drives. They either radiate, couple thermally, or produce tiny internal forces.

### B. Speculative / unverified self-published claims

Zenodo and similar hosts contain designs claiming kN-scale reactionless thrust at watts (e.g. TET–CVTL, QRWCED, various metamaterial papers). **No independent replication, no peer-closed momentum audit.** Treat as claims, not results.

### C. Mainstream consensus

- EmDrive-class and similar: null or artifact-level after careful tests.
- True reactionless closed drive: incompatible with momentum conservation under known physics.
- Propellantless \(\neq\) reactionless (sails, beamed power, gravity assist are open systems).

---

## Implication for Coherence Drive / Ware stack

| Item | Status |
|------|--------|
| Stage-2 continuum G (tested maps) | Archived **null** |
| Vacuum screen S | Turns **off** in lab (\(S\to 0\)) |
| ZPE harvest for \(30\,\mu\mathrm{N/kW}\) closed box | **Not established** in literature or our numerics |
| Legitimate research path | Class B named channel + \(\epsilon_F\); or new law **before** numerics |

**No race was won.** Publishing a fitted number is not discovery. Discovery requires a frozen mechanism, spherical controls, residual above floor, and experiment.

---

## Watch list (forward)

1. Independent replication of any Casimir/dynamic-mirror recoil with full power and force metrology.
2. Peer-reviewed thermal-nonequilibrium vacuum forces at measurable scale.
3. Any claim that reports \(F_d+F_X\) residual under refinement.

Until then: **do not flip claim flags.**
