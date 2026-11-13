# Discovery: Device-intrinsic residual from any two-derivative reading with static massless A_0 (Kept Failure O.1)

## Discovery ID

DISC-0045

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0044.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit a1de4d9cf64fd360075d63f8a0a054871513fb2a. Paths: README.md Theorem O → Corollary 4 "KEPT FAILURE O.1"; GASKET.md Stage 2 OPEN bullet; scripts/general_reading_flux.py.

## Original Evidence

If c + 2d = 0 (Hessian, ∂∂Ψ − δΔΨ, Q), G = 0 on every vacuum surface. If c + 2d ≠ 0 (∂_iΨ∂_jΨ alone, its trace-free part, δ_{ij}|∇Ψ|²), G = (c/2 + d)∮|E|²n is nonzero on a finite surface, but takes three different values on three vacuum spheres around the same cluster, equals minus the exterior integrated divergence, and decays as R^{−2}.

## Discovery

Rejected hypothesis: some reading in the two-derivative family, combined with C5 and static massless C6, gives a net source attributable to an isolated device. Either G vanishes identically or it is a property of the drawn audit surface rather than of the device. The step "a force must be surface-independent" is labeled in the repository as interpretive; the mathematics (surface dependence, total zero over ℝ³, R^{−2} decay) is not.

## Why It Matters

With DISC-0040 and DISC-0043 it closes the whole two-derivative family under static massless electrostatics, not only the two named readings.

## Derivation

DISC-0044 (O.1, O.2, asymptotics). Checked; no gap.

## Assumptions

Assumption O, C5, C6 static massless, isolated device (no charge outside S).

## New Results

Archive `/workspace/scratch-ifi/indep_general_O.py` reproduces the three distinct trace fluxes on the three spheres and the R^{−2} dilation law (see DISC-0044). Repository script rerun OK.

## Prior Art

Not applicable.

## Novelty Analysis

REJECTED as a thrust route. No novelty claimed.

## Falsification Attempts

Looked for a reading with c + 2d ≠ 0 whose flux is surface-independent; none exists in the family, since the flux equals ∫_V (c/2 + d)∂_i|E|² over the vacuum shell between any two such surfaces, which is generically nonzero (three spheres differ numerically).

## Experimental Validation

None.

## Mathematical Status

Rejection of one route only; Stage 2 stays OPEN. Not thrust.

## Patent Relevance

None.

## Related Discoveries

- DISC-0044. Mathematical. The theorem behind the rejection.
- DISC-0040, DISC-0043. Failed hypothesis. The Hessian and quadratic members of the same route.
- DISC-0002. Failed hypothesis. Earlier flux route to thrust.

## Open Questions

Readings outside Assumption O; Ψ_info ≠ A_0; time-dependent or screened C6 with undifferentiated Ψ.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0044.

## Evidence Log

- 2026-10-08. Recorded from README Kept Failure O.1 at a1de4d9cf64fd360075d63f8a0a054871513fb2a.

## Change History

- 2026-10-08. Initial archive entry.
