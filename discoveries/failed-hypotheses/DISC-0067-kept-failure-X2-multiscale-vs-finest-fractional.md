# Discovery: Multi-scale L_ms^{0.45} coincides with finest-edge L^{0.45} (Kept Failure X.2)

## Discovery ID

DISC-0067

## Status

REJECTED

## Date Discovered

2026-10-09 (America/New_York). Same archive pass as DISC-0065.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3959241bfd57e6f68e7e906fe10351f446163666. Paths: GASKET.md Theorem X → "KEPT FAILURE X.2 (no coincidence with finest-only fractional)"; scripts/gasket_multiscale_fractional.py; CLAIM_STATUS.md.

## Original Evidence

The hoped-for law "multi-scale L_ms^{0.45} coincides with finest-edge L^{0.45} up to a level-independent constant (same audit sequence up to scaling)" is false. On levels 1–5 the finest-edge audit decreases (Theorem J record), while the multi-scale L_ms-audit increases; their ratio ‖F_ms,L‖/‖F_fin‖ ≈(2.604, 4.339, 6.165, 8.070, 10.033) is strictly increasing and already past 10 at level 5. Pointwise ‖u_ms,0.45 − u_fin,0.45‖_∞ grows from ~0.02 to ~0.19. Opposite monotonicity rules out any constant factor relating the two sequences.

## Discovery

Rejected hypothesis: multi-scale spectral fractional is a constant multiple of finest-edge fractional. False; opposite monotonicity and growing ratio.

## Why It Matters

Separates the multi-scale fractional graph from the finest-edge α=0.45 question (DISC-0034). Closing one does not close the other by a universal scale factor.

## Derivation

DISC-0065 / Theorem X contrasted with Theorem J finest-edge sequence. Checked; no gap.

## Assumptions

Multi-scale vs finest-only edge sets on the same vertex set; α=0.45; λ=1 for multi-scale.

## New Results

Archive witness and `/workspace/scratch-ifi/indep_theorem_X.log`: finest decreases, multi-scale increases, ratio grows 3.85× from n=1 to n=5; pointwise potential gap >0.01 at every level 1..5.

## Prior Art

Not applicable (rejection of a route).

## Novelty Analysis

None.

## Falsification Attempts

Tried a level-independent constant; ratio is strictly increasing past 10 at n=5.

## Experimental Validation

None.

## Mathematical Status

Correct as a negative result (finite-level witness through n=5; opposite monotonicity is decisive).

## Patent Relevance

None.

## Related Discoveries

- DISC-0065. Mathematical. Theorem X.
- DISC-0032 / DISC-0034. Finest-edge fractional bounds and open α=0.45 limit.
- DISC-0066. Failed hypothesis. λ=1 freeze inheritance also rejected.

## Open Questions

Whether combinatorial ‖F(n, 0.45)‖ → 0 or a positive finite L (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

Same as DISC-0065. Archive: `/workspace/scratch-ifi/repo_theorem_X.log`, `/workspace/scratch-ifi/indep_theorem_X.log`.

## Evidence Log

- 2026-10-09. Recorded from GASKET.md Kept Failure X.2 at 3959241bfd57e6f68e7e906fe10351f446163666; ARCHIVE_INDEP_THEOREM_X_PASS.

## Change History

- 2026-10-09. Initial archive entry.
- 2026-10-15. Indexed on PR #3 branch (verified 2026-10-09 ~3:10am EDT; not pushed in that slice). No content change to the classification.
