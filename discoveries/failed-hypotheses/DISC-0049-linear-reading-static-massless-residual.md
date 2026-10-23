# Discovery: Device-intrinsic residual from any linear reading with static massless A_0 (Kept Failures P.1, P.2)

## Discovery ID

DISC-0049

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0048.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 9e0fee59ee966cceefa8bc7a88870d25d71e43f8. Paths: README.md Theorem P → Corollary 2 "KEPT FAILURE P.1" and Corollary 4 "KEPT FAILURE P.2"; GASKET.md Stage 2 OPEN bullet; scripts/linear_reading_flux.py.

## Original Evidence

P.1: every shift-invariant linear reading (q(0) = 0), of any order, with C5 and static massless C6 (ΔA_0 = 0 in vacuum) gives G = 0 on every vacuum surface. P.2: the undifferentiated term e δ^{ij}Ψ gives G = e∮A_0 n = −e∫_V E, which on an enclosing sphere is e·p(x_0)/(3ε₀) with p(x_0) = p − Q_tot x_0: it moves with the sphere centre for a charged device and grows linearly under dilation of an off-centre sphere; for a neutral device all enclosing spheres agree but ellipsoids around the same charges give different values; T itself shifts by eCδ^{ij} under Ψ ↦ Ψ + C.

## Discovery

Rejected hypothesis: some linear reading of the frozen symbol, of any order, combined with C5 and static massless C6, gives a net source attributable to an isolated device. Shift-invariant readings give exactly zero; the one non-shift-invariant term gives a surface-dependent quantity. The step "a force cannot depend on the audit surface" is labeled interpretive in the repository; the mathematics is not.

## Why It Matters

With DISC-0040, DISC-0043 and DISC-0045 it closes every linear reading (any order) and every two-derivative reading under static massless electrostatics.

## Derivation

DISC-0048 Corollaries 1 and 4; the sphere value follows from the mean-value/multipole expansion of the exterior potential (only the dipole survives ∮Ψ n on a sphere). Checked; no gap.

## Assumptions

Assumption P, C5, C6 static massless, isolated device.

## New Results

Archive `/workspace/scratch-ifi/indep_linear_P.py`: neutral cluster q = (3, −1, −2) gives (−10.47197551, 3.56047167, −1.67551608) on a centred radius-2 sphere and on an off-centre radius-5 sphere, equal to (4π/3)·dipole; ellipsoids (2,3,4) and (3,1.6,1.8)@(0.1,0,−0.2) give (−15.19676761, 3.25789843, −1.06193676) and (−6.20406442, 4.57011897, −1.88325372); charged cluster dilation magnitudes grow linearly (30.58, 54.99, 104.76, 204.86 at R = 4, 8, 16, 32). All match the repository.

## Prior Art

Not applicable (rejection of a route; underlying facts classical).

## Novelty Analysis

None.

## Falsification Attempts

Tried to find a surface-independent nonzero G within the linear family: none exists, since the shift-invariant part vanishes and ∫_V E depends on V even for a neutral device.

## Experimental Validation

None.

## Mathematical Status

Correct as a negative result inside Assumption P.

## Patent Relevance

None.

## Related Discoveries

- DISC-0048. Mathematical. Theorem P.
- DISC-0040, DISC-0043, DISC-0045. Failed hypothesis. Hessian, quadratic and two-derivative versions of the same route.
- DISC-0002. Failed hypothesis. Absolute flux is not a net force.

## Open Questions

Nonlinear higher-derivative readings (repository Theorems Q, R, not indexed in this pass); Ψ_info ≠ A_0; Stage 2 mesh computation.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0048.

## Evidence Log

- 2026-10-08. Recorded from README Theorem P Kept Failures P.1, P.2 at 9e0fee59ee966cceefa8bc7a88870d25d71e43f8.

## Change History

- 2026-10-08. Initial archive entry.
