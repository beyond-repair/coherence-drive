# Discovery: Two-point {0, 6} saturation as a gasket theorem

## Discovery ID

DISC-0008

## Status

REJECTED as a gasket theorem.

## Date Discovered

2026-10-01. This is the date of the archive pass that indexed the negative result at the new HEAD.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0. The section is "Negative result (abstract, not a gasket theorem)" under "Lambda = 6 eigenspace split" in README.md. COMPLETION_LOG.md at the same HEAD lists two-point spectra supported on {0, 6} under "Abstract-only (not committed as gasket theorems)."

Free-spectrum facts used to show those graphs are off the extremal are DISC-0005, from beyond-repair/sierpinski-geometry-045 SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.

The elementary bound that the extremal would saturate is DISC-0007.

## Original Evidence

At that HEAD the repository states that the upper bound V''(W) = -18 m_6 / (1 - 6W)^2 is saturated precisely when the spectrum is supported on {0, 6}. That two-point support, together with Tr L, mult(6), and the box [0, 6], defines an abstract extremal problem on finite spectra. It is not the spectrum of free L = D - A on build_gasket(n): those graphs carry eigenvalues in (0, 6). The file says: do not commit two-point {0, 6} extremals as gasket theorems. The bound remains valid as an inequality for every spectrum in the assumed box; saturation is off the gasket.

COMPLETION_LOG.md repeats that those extremals are abstract-only and are not free gasket spectra.

SPECTRUM.md records eigenvalues 3 and 5 present for n = 2..5, so free spectra are not supported on {0, 6}.

## Discovery

Reading the V'' upper bound as saturated on the free gasket, or committing two-point {0, 6} extremals as gasket theorems, is rejected by the source repository itself. The inequality bound of DISC-0007 remains; equality on the free gasket does not.

## Why It Matters

This fence stops an upgrade from the elementary V'' bound to a two-point spectral model of the gasket. That upgrade is not in the files and must not be invented later. It also does not select W or thrust.

## Derivation

No gasket derivation of two-point support is recorded, because the claim is rejected. The source note is that free graphs carry eigenvalues in (0, 6).

## Assumptions

The rejection is for free L = D - A on build_gasket(n) as used in SPECTRUM.md. The abstract extremal problem on spectra in [0, 6] with fixed Tr L and mult(6) is acknowledged as abstract and is not indexed as a gasket theorem.

## New Results

None. This row records a negative result already written in the source.

## Prior Art

Not claimed as new. The rejection is in-repo claim hygiene.

## Novelty Analysis

There is no novelty claim. Status is REJECTED for the gasket-theorem reading.

## Falsification Attempts

The source already falsifies saturation on the free gasket by citing eigenvalues in (0, 6). This archive does not attempt to revive the two-point model.

## Experimental Validation

None.

## Mathematical Status

Rejected reading. The inequality of DISC-0007 stands; equality on free gasket spectra does not.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0007. Mathematical. The bound that the extremal would saturate.
- DISC-0005. Mathematical. Free spectra with eigenvalues in (0, 6).
- DISC-0003. Historical. Same repository family.
- DISC-0002. Mathematical. Separate rejected upgrade; neither selects thrust.

## Open Questions

Abstract extremal problems on finite spectra in [0, 6] are outside the gasket commit. Free mult(6) for all n >= 2 remains open as in DISC-0007.

## Next Experiments

Do not commit two-point {0, 6} models as free-gasket theorems. Do not convert the V'' bound into selected W or thrust.

## Reproduction Instructions

Check out beyond-repair/finite-gasket-spectral-derivatives at 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 and read the negative-result subsection and COMPLETION_LOG.md. Confirm eigenvalues in (0, 6) in sierpinski-geometry-045 SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.

## Evidence Log

- 2026-10-01. Indexed from README.md negative-result subsection and COMPLETION_LOG.md at HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0.
- 2026-10-01. SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1 lists exceptional eigenvalues including 3 and 5 for n = 2..5.

## Change History

- 2026-10-01. Initial archive entry. No existing discovery file was overwritten.
