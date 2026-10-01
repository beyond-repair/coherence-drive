# Discovery: Gasket spectrum locks

## Discovery ID

DISC-0005

## Status

KNOWN

## Date Discovered

2026-10-01. This is the date of the archive pass.

## Source Repositories

beyond-repair/sierpinski-geometry-045 at HEAD 16cc0851185d2a38f63dcf53fea22fef7ef915e1. The file is SPECTRUM.md.

## Original Evidence

SPECTRUM.md at that commit records these locks. lambda_max = 6 for n greater than or equal to 2. The trace of L is 6 times 3 to the n. The multiplicity of lambda = 6 is (3/2) times (3 to the n-1, minus 1). The Dirichlet lambda_min ratio tends to 1/5.

The same statement is not thrust and is not pinch eta = 0.92. Continuum spectral dimension is cited literature in that file. It is not proved from these graphs.

coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at 095d29d1a107d719f8aed9f89834d917b119ca4c lists the same combinatorial locks under survived items, and lists lambda = 6 multiplicity as pinch eta = 0.92 under rejected items.

## Discovery

On these finite graphs the four spectral locks above hold as stated in SPECTRUM.md. They are combinatorial facts about the graphs. They are not a measured pinch and they are not a thrust result.

## Why It Matters

DISC-0003 uses lambda_max = 6 as the spectral input for the positive-definite window W < 1/6. That edge is mathematical. The locks do not select 0.08, do not establish eta = 0.92, and do not establish thrust.

## Derivation

No derivation is repeated here. The counts are the ones already written in SPECTRUM.md.

## Assumptions

The locks are for the finite graphs in that repository, with n at least 2 for lambda_max = 6. The Dirichlet ratio is a limit statement about lambda_min on those graphs, as written in SPECTRUM.md. No continuum identification is assumed.

## New Results

None.

## Prior Art

The locks are in-repo combinatorial identities. Continuum spectral dimension is cited literature in SPECTRUM.md. This archive does not copy that citation and does not treat it as a proof from these graphs.

## Novelty Analysis

There is no novelty claim. The relation to DISC-0003 is mathematical.

## Falsification Attempts

Reading the multiplicity of lambda = 6 as pinch eta = 0.92 is already rejected in docs/SURVIVED_REJECTED_UNRESOLVED.md. This archive keeps that rejection.

## Experimental Validation

None. These are exact graph counts, not a laboratory measurement of a pinch.

## Mathematical Status

Known identity.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0003. Mathematical. Spectral link through lambda_max = 6.
- DISC-0006. Computational. A failed period detection hanging off these graphs.
- DISC-0002. The locks are not the 92% pinch and are not thrust.

## Open Questions

Continuum spectral dimension is not proved from these graphs. The Dirichlet ratio tending to 1/5 is not a pinch measurement.

## Next Experiments

Do not convert lambda_max = 6 or the multiplicity formula into eta = 0.92. Read SPECTRUM.md at the named HEAD before any later spectral claim.

## Reproduction Instructions

Check out beyond-repair/sierpinski-geometry-045 at 16cc0851185d2a38f63dcf53fea22fef7ef915e1 and read SPECTRUM.md. Compare the survived and rejected lines in coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at 095d29d1a107d719f8aed9f89834d917b119ca4c.

## Evidence Log

- 2026-10-01. Indexed from the verified audit facts for SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.
- 2026-10-01. Read coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at 095d29d1a107d719f8aed9f89834d917b119ca4c. It lists the combinatorial spectrum locks as survived and lists "lambda=6 multiplicity as pinch eta=0.92" as rejected.
- Provenance only. The GitHub description of sierpinski-geometry-045, fetched the same day, still says the geometry "creates the LDOS gradient and topological pinch in the Coherence Drive." That description was not edited and is not a measurement. topological-pinch's description, also fetched that day, still states a 92% pinch that produces net thrust. The file-level statement used here is that 92% is a hypothesis, not a measured pinch.

## Change History

- 2026-10-01. Initial archive entry. No existing file was changed.
