# Physics-Compatible Closure of Coherence Drive (Propulsion Track)

**Date:** 2026-08-31  
**Status:** CLOSED for reactionless vacuum claim; OPEN only as Class B / math calculus

```
thrust_validated = false
experimental_validation = false
real_world_validated = false
reactionless_closed_thrust = false
target_fitting_performed = false
physics_compatible_class_B = true
```

---

## 1. Compatible equations (the only propulsion form that works with known physics)

$$
\boxed{F_{\rm device}+F_X=0}
$$

$$
\mathcal{A}=\frac{\int\hat n|f|^2\,d\Omega}{\int|f|^2\,d\Omega}
$$

EM channel:

$$
\frac{F}{P}\le\frac{|\mathcal{A}|}{c}\le\frac{1}{c}\approx 3.34\times 10^{-9}\,\mathrm{N/W}
$$

Stage-1 symbols remain as *mathematics*. Free static continuum \(\mathcal{G}\) under tested maps is archived **null**. Driven radiation uses the same geometry to shape \(f(\hat n)\).

---

## 2. Simulation (Class B scout, 0.45 mesh)

Single-layer driven radiation; aft-biased vs equal drive; sphere control.

| n_aft | faces | \|A\|_aft | \|A\|_eq | F/P photon (aft) | vs target 3e-8 |
|------:|------:|----------:|---------:|-----------------:|---------------:|
| 1 | 12 | 0.00224 | 0.00011 | 7.5e-12 | 0.025% of target |
| 2 | 18 | 0.00223 | 0.00027 | 7.4e-12 | 0.025% |
| 3 | 36 | 0.00265 | 0.00043 | 8.9e-12 | 0.030% |

Sphere equal \|A\| ~ 1.7e-4; sphere aft-bias ~ 2.7e-3 (drive dominates).

**Verdict**

| Question | Answer |
|----------|--------|
| Closed reactionless vacuum? | **No** |
| Photon Class B at 30 µN/kW? | **No** (~3000× below target in this scout) |
| Photon Class B micro-recoil possible in principle? | **Yes** (ordinary physics) |
| Real-world validated? | **No** — needs lab + full BEM ε_F |

---

## 3. What is closed vs open

| Item | State |
|------|--------|
| Reactionless closed-box engine claim | **CLOSED / extinguished** |
| Free static Stage-2 maps | **NULL archived** |
| Physics-compatible propulsion form | **Class B only** |
| Mathematical calculus (W, T_eff, G form, geometry) | **Retained** as formal system |
| CFT / Ware galactic phenomenology | **Separate track** |
| World-changing thruster at target via this sim | **Not supported** |

---

## 4. No more circular BS

- Do not reopen free static G without new constitutive map.
- Do not fit κ to 3e-8.
- Do not claim thrust_validated without experiment.
- Do update this file if a driven BEM ε_F study completes.

**Changing the world** here means: honest equations, measured forces, or a real new law — not a louder README.
