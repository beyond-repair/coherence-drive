# Discovery: Kept Failure BA.1, the nonzero mesh residual is a discrete Newton's-third-law defect, not an informational residual

## Discovery ID

DISC-0130

## Status

REJECTED (hypothesis). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~1:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit fe388f3b633ff0cafbfd653758afde0ab7284b93. Paths: README.md "KEPT FAILURE BA.1"; CLAIM_STATUS.md Theorem BA row; scripts/mesh_maxwell_residual.py.

## Original Evidence

Hypothesis rejected: the nonzero D of Theorem BA (DISC-0129) is a Stage 2 informational residual. Repository witnesses: (i) the same L^0.45 and one-sided cell gradient on the boundaryless translation-invariant 6×6 triangular torus give certified D=(2.8976275758051…, 1.6729460609024…) for d=(1,−½,−½), while the centred six-neighbour stencil gives D∋0 (width <1e−75), as BA.5 requires; (ii) on the gasket the residual is almost all self-force, κ^self_4=−18.53032 of κ_4=−18.52634; (iii) no refinement-stable value: 2^−nκ_n=−2.0214, −1.6535, −1.3423, −1.1579, −1.0488, −0.9818 (n=1..6), so |κ_n| grows like the inverse mesh spacing.

## Discovery

The residual is produced by the asymmetric (one-sided) gradient stencil and grows with refinement, so it is a discretisation artefact of the pair force, not a device property. The repository labels the final step "interpretive".

## Why It Matters

Prevents citing Theorem BA's "Σ div ≠ 0" as support for a thrust or informational force.

## Derivation

Witness (i) plus BA.5; witnesses (ii)–(iii) numerical.

## Assumptions

Assumption BA (DISC-0129). The rejection is of the interpretation, not of the arithmetic.

## New Results

None beyond the repository.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Archive reproduced witness (ii) (κ^self_4=−18.530321 vs κ_4=−18.526340) and (iii) at n=5,6 (−1.048791, −0.981791). Witness (i) taken from the repository run (EXIT 0), not independently re-implemented. The rejection stands.

## Experimental Validation

None.

## Mathematical Status

Counterexample/interpretive rejection, labelled as such by the repository.

## Patent Relevance

None.

## Related Discoveries

DISC-0129 → DISC-0130 (failed hypothesis). Same family as DISC-0043, DISC-0045, DISC-0119, DISC-0121, DISC-0124.

## Open Questions

Whether a symmetric gasket gradient rule removes D (no gasket analogue of BA.5 is proved).

## Next Experiments

Re-implement the torus witness independently.

## Reproduction Instructions

As DISC-0129.

## Evidence Log

- 2026-10-22. See DISC-0129.

## Change History

- 2026-10-22. Initial archive entry.
