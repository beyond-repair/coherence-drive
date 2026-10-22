# Discovery: A share floor close to the live σ_n, times the proved fractional floors, reaches Conjecture J.1's 0.70 (Kept Failure AP.1)

## Discovery ID

DISC-0105

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0104.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit a1486faddc997650ce5b786104490aa6d13d2104. Paths: GASKET.md Theorem AP → Kept Failure AP.1, OBSERVATION, NOT THIS; CLAIM_STATUS.md AP row; scripts/gasket_fractional_moment_share.py (Kept Failure AP.1 section).

## Original Evidence

GASKET.md Kept Failure AP.1: the claim "with a share floor close enough to the live σ_n, ‖F‖=σ_n‖F_frac‖ and the proved fractional floors of Theorems AM–AO yield ‖F(n,0.45)‖≥0.70" is false. Any level-uniform share floor is at most the live σ_6≈1.352483, and 1.352483·0.316911≈0.428617<0.70 (AM: ≈0.283595). With S_AP, J.1's 0.70 would follow from ‖F_frac‖≥0.534242, i.e. a level-uniform resistance ceiling R_α(n)≤2.859237 (live ≤2.347382 through level 6; best proved ceiling ≈4.820047), "which is OPEN".

## Discovery

Rejected hypothesis: the share side alone (with the then-proved fractional floors) reaches 0.70. False; the bottleneck is the fractional/resistance side. Continues DISC-0099/0101/0103 from the other factor.

## Why It Matters

Re-reads Kept Failures AM.1–AO.1 ("a share floor near 1.35 is needed"): the share floor is now supplied to ≈3.1%, and what was missing is exactly a resistance ceiling ≤2.859237. That missing step is supplied one commit later by Theorem AQ (DISC-0106: R̄=2.518955), so AP.1's "OPEN" remark is superseded; the rejection of the route as stated (share floor × AM–AO floors) stands.

## Derivation

Level-uniform σ floor ≤ inf_n σ_n = lim σ_n ≈1.352476 (σ_n decreasing; DISC-0106 (3)); 1.352476·0.316911≈0.4286<0.70 and ·0.209685≈0.2836<0.70. Needed fractional floor 0.70/S_AP=0.534242; needed resistance ceiling S_AP·√21/(3·0.70)=2.859237. Checked; no gap.

## Assumptions

As DISC-0104.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AP.log`, EXIT 0, 97 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AP.py` / `indep_theorem_AP.log`, ALL PASS, 84 PASS): σ_7=1.352477 (own builder) ×0.316911=0.428615, ×0.209685=0.283594 (both <0.70); needed ‖F_frac‖ 0.534242 and R ceiling 2.859237 reproduced; S_AP within 3.12% of σ_7.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed with the level-7 share and both fractional floors; the AO floor's finite-range caveat makes the product only smaller-or-equal in a corrected reading, so the rejection is robust.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. The "resistance ceiling OPEN" remark is superseded by DISC-0106 (archive note; repository commit 4b4509f6f086 says the same: "This also closes the step Kept Failure AP.1 left open").

## Patent Relevance

None.

## Related Discoveries

- DISC-0104. Mathematical. Theorem AP.
- DISC-0103, DISC-0101, DISC-0099. Failed hypotheses. Resistance-ceiling × σ_AK family (the other factor).
- DISC-0106. Mathematical. Theorem AQ supplies the resistance ceiling AP.1 called open.
- DISC-0034. J.1 (status changed by DISC-0106).

## Open Questions

None (closed by DISC-0106).

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0104.

## Evidence Log

- 2026-10-22. Recorded from GASKET.md Kept Failure AP.1 at a1486faddc997650ce5b786104490aa6d13d2104; repo and archive indep confirm rejection.

## Change History

- 2026-10-22. Initial archive entry.
