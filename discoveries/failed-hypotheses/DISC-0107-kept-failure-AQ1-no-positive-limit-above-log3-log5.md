# Discovery: The decimation ceiling gives a level-uniform resistance bound and a positive audit limit for every α∈(0,1) (Kept Failure AQ.1)

## Discovery ID

DISC-0107

## Status

REJECTED

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0106.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 4b4509f6f086f3f52b034f55508862f130381f2b. Paths: GASKET.md Theorem AQ → Kept Failure AQ.1, OBSERVATION, NOT THIS; CLAIM_STATUS.md AQ row; scripts/gasket_fractional_decimation.py (Kept Failure AQ.1 section).

## Original Evidence

GASKET.md Kept Failure AQ.1: the claim "the decimation ceiling of (4)–(5) gives a level-uniform bound on R_α(n), hence a positive limit of ‖F(n,α)‖, for every α∈(0,1)" is false. Item (3) holds for every α, but the power window (1−γ, 1−α), γ=log3/log5, is empty for α≥γ; r_n(s)≈(5/3)^n/3 for s≲5^(−n) makes ∫s^(−α)r_n unbounded; R_γ(n) grows linearly (≈0.5172 per level on n=8–24, Theorem AD's Θ(n)); at α=0.75 R grows geometrically (ratio ≈1.125 on n=20–24, → 5^α/3≈1.1146); there ‖F‖→0 (Theorems AD, K), so the decreasing limit of (3) is 0.

## Discovery

Rejected hypothesis: AQ's positive-limit mechanism extends to all α. False at and above log3/log5, consistent with DISC-0080 (AD) and DISC-0032 (K).

## Why It Matters

Marks the exact scope of DISC-0106: monotone decrease for every α, positive limit only for α<log3/log5 (certified at 0.10, 0.25, 0.45, 0.49, 0.55 in the repository). Not thrust.

## Derivation

Window: β′>1−γ≈0.3174 is needed for (C1) as s→0 (2·5^(1−β′)<6) and β′<1−α for integrability; empty iff α≥γ. Growth rates from the recursion. Checked; no gap.

## Assumptions

As DISC-0106.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AQ.log`, EXIT 0, 69 PASS): R_γ(8,12,16,20,24)=4.8405, 6.9091, 8.9777, 11.0464, 13.1151, increments 0.5171–0.5172; R_0.75(16,20,24)=21.383, 35.043, 56.124, ratio 1.12496. Independent archive (`/workspace/scratch-ifi/indep_theorem_AQ.py` / `indep_theorem_AQ.log`, own recursion quadrature): same values to 4 digits; ‖F(n,0.75)‖ decreasing toward 0 (n=10→30).

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of an extension).

## Falsification Attempts

Recomputed both growth laws with an independent quadrature; checked the window algebra.

## Experimental Validation

None.

## Mathematical Status

Rejected as stated. DISC-0106 stands for α<log3/log5.

## Patent Relevance

None.

## Related Discoveries

- DISC-0106. Mathematical. Theorem AQ.
- DISC-0080, DISC-0081. Mathematical / failed hypothesis. Theorem AD (endpoint, Θ(n)) and AD.1.
- DISC-0078, DISC-0079. Mathematical / failed hypothesis. Theorem AC floor below log3/log5; AC.1.
- DISC-0032. Mathematical. Theorem K (α>log3/log5 → 0).

## Open Questions

None.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0106.

## Evidence Log

- 2026-10-22. Recorded from GASKET.md Kept Failure AQ.1 at 4b4509f6f086f3f52b034f55508862f130381f2b; repo and archive indep confirm rejection.

## Change History

- 2026-10-22. Initial archive entry.
