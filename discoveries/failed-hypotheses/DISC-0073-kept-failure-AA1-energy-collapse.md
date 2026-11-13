# Discovery: Energy collapse at α=0.45 (Kept Failure AA.1)

## Discovery ID

DISC-0073

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0072.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e4be06f8fb772982dd9855fac6d9d5c2660eb9a7. Paths: GASKET.md Theorem AA → Kept Failure AA.1; CLAIM_STATUS.md (energy collapse ruled out); scripts/gasket_fractional_energy_floor.py.

## Original Evidence

Theorem L left one route to ‖F(n,0.45)‖→0: energy collapse Q_{0.45}(u_n)→0. Theorem AA proves Q_{0.45}(u_n)≥0.128335 at every level, so no subsequence collapses. The same floor makes ‖F_frac(n,0.45)‖→0 false. If the combinatorial audit tends to 0, vanishing must come from the two-neighbor share I_a/I_a^α of the fractional current, with the current itself bounded below.

## Discovery

Rejected hypothesis: Q_{0.45}(u_n)→0 (the Theorem L energy-collapse route to zero audit). It does not.

## Why It Matters

Closes every energy-collapse shortcut after Kept Failures J.1–J.4. Does not decide combinatorial ‖F‖ (DISC-0034 stays OPEN). Not thrust.

## Derivation

DISC-0072 Theorem AA lower bound. Checked; no gap.

## Assumptions

As DISC-0072.

## New Results

Archive `/workspace/scratch-ifi/indep_theorem_AA.py`: live levels 1–5 and recorded levels 9–10 all sit strictly above the floor 0.128335; ‖F_frac‖ pairing holds.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Tried to break the floor via the α=1/2 control (log growth of R) — confirms the proof needs α<1/2, does not reopen collapse at 0.45.

## Experimental Validation

None.

## Mathematical Status

Rejection of one route only; combinatorial α=0.45 zero-versus-positive stays OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0072. Theorem AA.
- DISC-0032. Theorem L (the route being closed).
- DISC-0033. Earlier kept failures for closing the α=0.45 limit.
- DISC-0034. Conjecture. Still OPEN.

## Open Questions

As DISC-0072.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0072.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AA.1 at e4be06f8fb772982dd9855fac6d9d5c2660eb9a7; repo witness EXIT:0; indep PASS.

## Change History

- 2026-10-15. Initial archive entry.
