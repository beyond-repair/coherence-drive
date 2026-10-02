# Discovery: Log-periodic period

## Discovery ID

DISC-0006

## Status

REJECTED as a detection on these graphs.

## Date Discovered

2026-10-01. This is the date of the archive pass.

## Source Repositories

beyond-repair/sierpinski-geometry-045 at HEAD 16cc0851185d2a38f63dcf53fea22fef7ef915e1. The file is LOG_PERIODIC.md. The graph locks it hangs from are in SPECTRUM.md at the same commit, which is DISC-0005.

## Original Evidence

LOG_PERIODIC.md records a pre-registered test for n at most 6. The test does not measure period log 5. Two-period slopes are about -0.837, -0.885, and -0.934. The target slope is -0.683. A(tau) is monotone. The number 5 to the 6 times lambda_min^D equals 11.21026, and that product is only the Dirichlet lock.

The in-file status is not measured, and unresolved for the limit kernel.

## Discovery

On these graphs the pre-registered test does not detect a log-periodic period of log 5. The slopes do not match the target -0.683. The Dirichlet product 11.21026 is not that detection.

## Why It Matters

DISC-0005 locks the finite-graph spectrum, including the Dirichlet lambda_min ratio. Those locks do not by themselves measure a log-periodic period. This row hangs off DISC-0005 as a failed detection. The edge is computational.

## Derivation

There is no successful derivation of the period. The recorded comparison is the pre-registered slope test in LOG_PERIODIC.md.

## Assumptions

The rejection applies to the pre-registered n at most 6 test on these graphs. It does not claim a result about a limit kernel that the file itself leaves unresolved.

## New Results

None. The failure is the result already written in the file.

## Prior Art

The test is in-repo. No external citation was fetched from LOG_PERIODIC.md for this pass, so none is named here.

## Novelty Analysis

There is no novelty claim. A failed detection is not a new physical period.

## Falsification Attempts

The pre-registered test is the falsification for these graphs. The measured two-period slopes about -0.837, -0.885, and -0.934 miss the target -0.683. A(tau) being monotone is part of that record.

## Experimental Validation

None. This is a graph computation. The period was not measured. The in-file status for the limit kernel is unresolved.

## Mathematical Status

Rejected.

## Patent Relevance

None established.

## Related Discoveries

DISC-0005. Computational. This failed detection hangs off the gasket spectrum locks. It does not change those locks, and it does not touch thrust.

## Open Questions

The limit kernel remains unresolved in LOG_PERIODIC.md. This archive does not measure a period there and does not close that status.

## Next Experiments

Do not report 5^6 lambda_min^D = 11.21026 as a detection of period log 5. Any later test has to be a new pre-registered check. This pass does not define one.

## Reproduction Instructions

Check out beyond-repair/sierpinski-geometry-045 at 16cc0851185d2a38f63dcf53fea22fef7ef915e1. Read LOG_PERIODIC.md for the n at most 6 test, the three slopes, the target -0.683, the monotone A(tau), and the Dirichlet product 11.21026. Read SPECTRUM.md at the same commit for the graph locks that this test does not replace.

## Evidence Log

- 2026-10-01. Indexed from the verified audit facts for LOG_PERIODIC.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.
- coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at 095d29d1a107d719f8aed9f89834d917b119ca4c lists log-periodic amplitude, frequency, and phase on a heat kernel as not measured here, and lists the DSI / log-periodic direction as a research direction rather than a demonstrated measurement.

## Change History

- 2026-10-01. Initial archive entry. No existing file was changed.
