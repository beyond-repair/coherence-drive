# 0.45 audit — three unrelated uses

Do not conflate these.

## 1. Spectral / operator exponent

If the operator is \((-\Delta)^\alpha\), then \(\alpha=0.45\) is an exponent.
It is not \(45^\circ\), not a slope, not a tilt, not a critical propulsion angle.

On the combinatorial gasket Laplacian this \(\alpha\) is **not** a peak of the
asymmetric-source flux diagnostic (Sweep-138).

## 2. Geometry / design parameter

`sierpinski-geometry-045` uses \(\alpha_{\rm geom}=0.45\) as a **scale ratio**
in the tetrahedron generator (`_midpoint(..., alpha=0.45)`).

This does **not** imply the spectral exponent equals 0.45, or conversely.

## 3. Physical / printed tilt

A printed structure can have \(\theta=0.45^\circ\). That is an angle.

The gasket itself has planar edge directions \(0^\circ,60^\circ,120^\circ\).
There is no intrinsic \(45^\circ\) slope in the graph.

Small-tilt shear on the level-2 gasket with a symmetric interior load:

- Sweep-138 geometric weights \(G=1/\ell^2\): \(\|F\|\approx 0.935\,\theta_{\rm rad}\)
- Sweep-159 constant-section conductance \(G=1/\ell\): \(\|F\|\approx 0.468\,\theta_{\rm rad}\)

Both are **geometric-asymmetry diagnostics / print-skew controls**.
They are not evidence of reactionless thrust.

\(+/-\theta\) decomposition (level 2, weighted Laplacian, Sweep-139 / Sweep-159):

- \(F_{\rm odd,x}\propto\theta\)
- \(F_{\rm even,x}\to 0\) to machine precision
- \(F_{\rm even,y}=O(\theta^2)\) is contamination from the one-sided shear map,
  classified as a numerical/geometry artifact, not new physics
- rigid rotation and isotropic scale have vanishing Jacobian (Sweep-159)

Satellite lock: [sierpinski-geometry-045 FINDINGS_2026-09-21](https://github.com/beyond-repair/sierpinski-geometry-045/blob/main/FINDINGS_2026-09-21_CONDUCTANCE_SHEAR.md)
