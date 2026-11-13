# Discovery: Conjecture AT.2, the critical slope is the log-mean of the periodic profile

## Discovery ID

DISC-0115

## Status

THEOREM (from 2026-10-22, via DISC-0116; mathematical sense only). Novelty UNRESOLVED. Not thrust.

Status history (not rewritten): CONJECTURE (repository's own) from 2026-10-22 ~6:01am EDT until the same day, when IFI Theorem AU (1) at b036dcfb89e66ffa51ebf8407c08996d7fa3d17e proved it: ∫s^(−γ)r_m = m ln5⟨Θ⟩+O(1), so c_R(γ)=(2 sin πγ/π)ln5⟨Θ⟩, with ⟨Θ⟩ certified in [0.6009542511687736078237051500999942, …9943]. The sections below are the original record and are kept as written.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~6:01am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 68af4dd0c3989732a1b8b8ea0275948b7c33051a (2026-10-22 05:35:48 −0400). Paths: GASKET.md "Theorem AT", "KEPT FAILURE AT.1", "CONJECTURE AT.2"; CLAIM_STATUS.md row "Certified refinement-rate constants c_R, c_S of Theorem AR — VERIFIED (Theorem AT, Kept Failure AT.1)"; scripts/gasket_fractional_rate_constants.py (new, 410 lines); scripts/cli.py; README.md.

## Original Evidence

GASKET.md "CONJECTURE AT.2": c_R(γ)=(2 sin πγ/π)ln5·⟨Θ⟩, ⟨Θ⟩ the mean of Θ over one period in log_5 s. Evidence: 32-point trapezoid (40-digit float, not interval) gives 0.517165834630505244, matching the certified c_R(γ) to 5e−22. Stated falsifier: a certified enclosure of ⟨Θ⟩ excluding c_R(γ)π/(2 sin πγ ln5).

## Discovery

The critical-exponent resistance slope equals the averaged log-periodic amplitude of r_∞ at 0.

## Why It Matters

Would give a structural formula for c_R(γ) (DISC-0113) via the profile of DISC-0114.

## Derivation

Heuristic only (R_γ(n) gains one period of ∫g d log s per level). Note: a trapezoid rule on a smooth periodic function converges exponentially, so 22-digit agreement is strong numerical evidence but not proof.

## Assumptions

Existence and smoothness of Θ (DISC-0114).

## New Results

None proved.

## Prior Art

Averaged log-periodic constants in fractal spectral asymptotics (Kigami–Lapidus; Derfel–Grabner–Vogl) are a known pattern; not searched for this quantity.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive check (D): own 32-point log-mean of g=s^(1−γ)r_90 over s∈5^(−40)[1,5) gives 0.5171658346305052439, inside the certified c_R(γ) interval. Survived first attack (float only).

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

- DISC-0113 → DISC-0115, DISC-0114 → DISC-0115 (mathematical).

## Open Questions

Proof via the transfer identity at α=γ; certified ⟨Θ⟩.

## Next Experiments

Interval enclosure of ⟨Θ⟩ to 1e−15 (would test the falsifier).

## Reproduction Instructions

`git -C informational-flux-identity checkout 68af4dd0c3989732a1b8b8ea0275948b7c33051a && python3 scripts/gasket_fractional_rate_constants.py` (~2.5 min, EXIT 0, 22 PASS). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AT.py` (~82 s, EXIT 0, 19 PASS; mpmath float, no repo import).

## Evidence Log

- 2026-10-22 (later slice). IFI b036dcfb89e66ffa51ebf8407c08996d7fa3d17e GASKET.md Conjecture AT.2 header "Status: PROVED by Theorem AU"; statement text kept. Repo witness scripts/gasket_fractional_log_mean.py EXIT 0; archive /workspace/scratch-ifi/indep_theorem_AU.py EXIT 0 (11 PASS): 128-point log-mean at depth 5^(−141) gives c_R(γ)=0.5171658346305052439259804856731272 inside both enclosures.

- 2026-10-22. Repo observation PASS; archive check (D) PASS.

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22. Status change CONJECTURE → THEOREM (DISC-0116, IFI Theorem AU at b036dcfb89e66ffa51ebf8407c08996d7fa3d17e). Earlier text retained.
