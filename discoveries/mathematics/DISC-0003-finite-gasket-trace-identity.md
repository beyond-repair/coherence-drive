# Discovery: Finite gasket trace identity

## Discovery ID

DISC-0003

## Status

DERIVATIVE

## Date Discovered

2026-10-01. This is the date of the archive pass.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at HEAD 33dfec7db730c2dd7baf62892242835a2d25544b.

The shared spectral input lambda_max = 6 is DISC-0005, from beyond-repair/sierpinski-geometry-045.

## Original Evidence

At that HEAD the repository states the following. For W < 1/6, Gamma_loop plus the truncated trace series equals minus one half times the sum over k of the integral from 0 to W lambda_k of t^N / (1 - t) dt. The same quantity is also written with 2F1 and Lerch. The radius of the trace series is exactly 1/6. V double prime is negative on the positive-definite interval. K is positive definite if and only if W < 1/6 at omega = 1, where lambda_max = 6. The repository says the scalar identity is classical and does not select W. It states no continuum and no thrust.

The GitHub description of this repository, fetched on 2026-10-01, matches that limit: "W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum, no selected W, no thrust."

## Discovery

The finite-gasket trace identity above is a derivative of a classical scalar identity. It fixes the radius 1/6 and the positive-definite window W < 1/6. It does not choose a numerical W inside that window.

## Why It Matters

The bound W < 1/6 is real as a positive-definiteness condition at omega = 1 and lambda_max = 6. It does not select 0.08 and it does not select thrust. That is the mathematical edge from this row to DISC-0002.

## Derivation

No derivation is repeated here. The repository already writes the integral form and the 2F1 and Lerch forms. This archive does not add another form.

## Assumptions

The statement is for the finite gasket, at omega = 1, with lambda_max = 6. W is a prescribed scalar in the identity as used there. No continuum limit is assumed.

## New Results

None.

## Prior Art

The source repository says the scalar identity is classical. This archive does not name a further paper, because no additional citation was copied out of that file for this pass.

## Novelty Analysis

There is no novelty claim. The status is derivative. The relation to DISC-0005 is mathematical, through lambda_max = 6.

## Falsification Attempts

The repository already refuses two upgrades: it does not select W, and it does not give thrust. This archive does not attempt a third upgrade.

## Experimental Validation

None.

## Mathematical Status

Derivative classical identity.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0005. Mathematical. Spectral input lambda_max = 6.
- DISC-0002. Mathematical. The W bound does not select 0.08 or thrust.
- DISC-0004 stands beside this row. Same W family. Not a thrust input.

## Open Questions

The identity does not select a numerical W. Local W(x) is not settled by this scalar identity. No continuum limit is claimed.

## Next Experiments

Do not fit 0.08 into the interval W < 1/6 and call it selected. Read the source file at the named HEAD before any later use of the series.

## Reproduction Instructions

Check out beyond-repair/finite-gasket-spectral-derivatives at 33dfec7db730c2dd7baf62892242835a2d25544b and read the note that states the integral identity, the radius 1/6, and the positive-definite condition. Compare lambda_max = 6 with SPECTRUM.md in sierpinski-geometry-045 at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.

## Evidence Log

- 2026-10-01. Indexed from the verified audit facts for HEAD 33dfec7db730c2dd7baf62892242835a2d25544b. The description sentence quoted above was fetched from the GitHub repository record on the same day.
- coherence-drive docs/SPECTRAL_ENDPOINT.md at 095d29d1a107d719f8aed9f89834d917b119ca4c already says that on the finite gasket at omega = 1, lambda_max = 6, so K is positive definite if and only if W < 1/6, and that V double prime is negative. It also says stationarity does not select a numerical W.

## Change History

- 2026-10-01. Initial archive entry. No existing file was changed.
