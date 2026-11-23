# Discovery: Device-intrinsic residual from a nonlocal (convolution or fractional) Maxwell-form reading + C5 + static massless C6 (Kept Failure AV.1)

## Discovery ID

DISC-0119

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0118.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 9fc8c7a3e2d680395a095c36f0daf90df776d043. Paths: README.md Theorem AV → Kept Failure AV.1; CLAIM_STATUS.md; scripts/nonlocal_reading_flux.py.

## Original Evidence

Replacing Ψ by a translation-invariant nonlocal reading of it (heat kernel, Yukawa smearing, general finite radial measure, fractional Laplacian) does not open a surface-independent nonzero G for an isolated static device. The effective source leaks into the vacuum, so conservation fails for every kernel except cδ (AV.3). G is nonzero on some vacuum surfaces even for one point charge, but a centred sphere gives 0, an off-centre sphere gives a value directed along the offset, and dilation sends G to 0 (kernel tail for heat/Yukawa, R^{−3−2s} for (−Δ)^{s/2}). Newton's third law makes ∫div T=0 over all space. Interpretive step (labeled in the README, same as O.1–Z.1): a surface-dependent G cannot be read as a force on the device.

## Discovery

Rejected hypothesis: a nonlocal reading of Ψ produces a net, device-intrinsic residual after Maxwell removal. It does not.

## Why It Matters

With DISC-0060, DISC-0062, DISC-0069, and DISC-0071 it closes the nonlocal Maxwell-form gap for static massless A_0. The residual it does produce is an internal force of the smeared charge split by the audit surface.

## Derivation

See DISC-0118.

## Assumptions

As DISC-0118, plus the README's labeled interpretive step that a force on the device is independent of the audit surface.

## New Results

Archive surface quadrature reproduces heat and Yukawa single-charge values on (R,b)=(2,0),(2,½),(2,1),(3,1): zero centred, three different positive values off centre; s=1 negative off centre. Surface dependence confirmed independently.

## Prior Art

Not applicable (failed hypothesis); the mechanism is the classical vanishing static self-force.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Tried to find a surface-independent nonzero value: centred vs offset spheres for one charge give 0 vs nonzero; values shrink with R. Hypothesis fails.

## Experimental Validation

None.

## Mathematical Status

Kept Failure (rejected route), supported by DISC-0118's proofs plus a labeled interpretive step.

## Patent Relevance

None.

## Related Discoveries

- DISC-0118. Theorem AV.
- DISC-0071, DISC-0069, DISC-0062, DISC-0060, DISC-0058. Earlier kept failures of the same class.

## Open Questions

Readings outside (H)'s decay class, time-dependent fields, Ψ_info ≠ A_0, and the 0.45 mesh remain OPEN.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0118.

## Evidence Log

- 2026-10-22 ~7:58am EDT. Repo witness EXIT 0; independent check 23/23 PASS.

## Change History

- 2026-10-22. Initial archive entry.
