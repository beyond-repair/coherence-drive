# Discovery: Kept Failure DZ.4, the limit of the renormalised corner deficit is not independent of N (BL.6's "independent of N" is false)

## Discovery ID
DISC-0239

## Status
REJECTED (the repository's own Kept Failure DZ.4 of the N-independence clause of Conjecture BL.6, DISC-0159). The general failure (every alpha in (gamma, 1)) follows from DZ.2 and DZ.3 (DISC-0238) with delta_N non-constant; the numbers are arb-certified at alpha = 0.8 only. Not thrust.

## Date Discovered
2026-11-13 (indexed ~8:15 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 6630f9bcfbfaa421c133ec52339a3a0c41fbe7e3 (2026-11-13 7:12 AM EST).

## Original Evidence
GASKET.md §Theorem DZ item DZ.4 (line 5716, table 5718–5724, remark 5726); GASKET.md line 2398 (BL.6 header annotated "independent of N FALSE, Kept Failure DZ.4"); scripts/gasket_fractional_corner_limit.py (DZ.4 bracket section); tests/test_cli.py test_theorem_dz_corner_limit (asserts the five enclosures are disjoint and increasing and that 0.6025 lies in the N = 10 one).

## Discovery
The claim "for alpha > gamma, lim rho^n (delta_N - delta_N^(n)) is the same for every N >= 1" (BL.6, floats C_delta(0.8) ~ 0.6025) is false. By DZ.2 the limit is -nu_alpha (1 - delta_N) with -nu_alpha > 0 (DZ.3), and delta_N is not constant in N (delta_1 >= delta_1^(1) > 0, delta_N -> 0 by BJ (6)). Certified at alpha = 0.8 (arb monotone brackets of delta_N^(60) on 69052 dyadic cells of [5^-80, 1e4], plus DZ.2's ceiling): C_delta(0.8, N) in [0.030733, 0.031869] (N = 1), [0.158436, 0.159369] (2), [0.257779, 0.258555] (3), [0.461214, 0.461662] (6), [0.602405, 0.602621] (10): disjoint, increasing toward -nu_0.8 = 0.72744538... BL's float 0.6025 is the N = 10 value.

## Why It Matters
BL.6's floats were all taken at one depth (N = 10 at 0.8, N = 6 at 0.9); the apparent constant was a depth-specific value.

## Derivation
As in DISC-0238 (DZ.2/DZ.3) plus BJ (6).

## Assumptions
As DISC-0238; AZ (3)'s nu_0.8 as stated.

## New Results
None beyond the rejection and the certified brackets.

## Prior Art
Not applicable.

## Novelty Analysis
Not applicable (a rejected repository conjecture).

## Falsification Attempts
- Independent numpy quadrature (/workspace/ifi-dz-indep/indep.py): -nu (1 - delta_N^(80)) at 0.8 = 0.031310, 0.158939, 0.258215, 0.461481, 0.602535 for N = 1, 2, 3, 6, 10; each inside its certified bracket, clearly N-dependent. PASS.
- mpmath: -nu_0.8 (1 - delta_N) on the stated delta_N brackets reproduces each stated C_delta bracket to 1e-6; brackets disjoint and increasing; 0.6025 in [0.602405, 0.602621]; N = 10 upper end < -nu_0.8. PASS.
- Scope: "false at every alpha in (gamma, 1)" rests on DZ.2/DZ.3 and BJ (6) as stated; certified values only at 0.8.

## Experimental Validation
Not applicable.

## Mathematical Status
Rejected claim (BL.6's N-independence clause).

## Patent Relevance
None.

## Related Discoveries
DISC-0159 (BL.6), DISC-0238 (Theorem DZ), DISC-0160 (BM's 0.3643 is the N = 6 value at 0.9).

## Open Questions
None for the rejected clause.

## Next Experiments
None.

## Reproduction Instructions
As DISC-0238.

## Evidence Log
- 2026-11-13 ~8:05 AM EST: see DISC-0238 evidence log (repo witness EXIT 0, 6.8 s).

## Change History
- 2026-11-13: created.
