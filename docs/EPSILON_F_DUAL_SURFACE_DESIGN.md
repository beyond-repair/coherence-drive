# Dual-surface ε_F design (Class B completion path)

**Status:** Design locked; magnitude not yet closed in code  
**Flags:** class_B_A_validated=false; epsilon_F_magnitude_closed=false

## Definition

$$
\mathbf{F}_d = -\oint_{\partial\Omega_{\rm device}} \langle T^{ij}\rangle n_j\,dA
$$

$$
\mathbf{F}_X = \oint_{S_R} \langle T^{ij}\rangle n_j\,dA \quad (R\to\infty \text{ or radiation sphere})
$$

$$
\epsilon_F = \frac{\|\mathbf{F}_d + \mathbf{F}_X\|}{|\mathbf{F}_X|+\delta}
$$

**Same** stress tensor T, **same** units, both surfaces.

## Pass criterion

ε_F → 0 under mesh + R refinement; sphere control |A|→0; no target fitting.

## Implementation path

1. Driven Helmholtz or EFIE on 0.45 mesh (existing fullwave_bem entry)
2. Recover E,B or scalar grad on hull and on S_R
3. Build ⟨T⟩ from Maxwell or scalar formula
4. Integrate both surfaces
5. Report table: (R, n_ang, n_aft) → ε_F, |A|

Until step 5 runs with ε_F trending down: **not complete**.
