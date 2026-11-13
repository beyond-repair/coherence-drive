# Discovery: Conjecture J.2, ‖F(n,0.10)‖ ≥ 1.410 for every n (carried forward from DISC-0034)

## Discovery ID

DISC-0108

## Status

THEOREM (from 2026-10-22, via DISC-0111; computer-assisted, mathematical sense only)

Status history (not rewritten): CONJECTURE from 2026-10-22 (split from DISC-0034) until the same day, when IFI Theorem AS (5) at a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7 proved it: ‖F(n,0.10)‖ strictly decreases (Theorem AQ (3)) to 𝓛(0.10)∈[1.410638933063,1.410638933065] (outward-rounded mpmath.iv interpolation-sandwich certificate), so ‖F(n,0.10)‖>1.410 at every level, margin 6.4e−4. The sections below are the original record and are kept as written.

## Date Discovered

2026-10-22 (America/New_York). Split out of DISC-0034 when DISC-0034's J.1 part changed status (DISC-0106). Originally recorded 2026-10-08 inside DISC-0034.

## Source Repositories

beyond-repair/informational-flux-identity, branch main. Originally GASKET.md "CONJECTURE J.2" at 81ab02b501aef7df2f5478f55d67d50f93595d56 (via DISC-0034); unchanged and still a conjecture at 4b4509f6f086f3f52b034f55508862f130381f2b (GASKET.md, paragraph after the α=0.10 table: "CONJECTURE J.2. ‖F(n,0.10)‖≥1.410 for every n. Falsified by the first level with ‖F‖<1.410.").

## Original Evidence

As DISC-0034 (J.2 part): computed α=0.10 levels; the α→0 profile has audit norm √(7/3)≈1.527525 for n≥1, which the repository says is a different operator.

## Discovery

Repository conjecture, recorded as stated. Since Theorem AQ (3) (DISC-0106) proves ‖F(n,α)‖ strictly decreasing for every α∈(0,1), J.2 is now equivalent to lim_n ‖F(n,0.10)‖ ≥ 1.410.

## Why It Matters

It is the remaining open item of the former DISC-0034 record. Not thrust.

## Derivation

None in-repo. The repository's AQ certificate at α=0.10 (grid ratio 1.02) gives only 𝓛(0.10)∈[1.292150, 1.583120], which does not decide J.2.

## Assumptions

As DISC-0034 / DISC-0106.

## New Results

Archive (`/workspace/scratch-ifi/indep_theorem_AQ.log`, recursion-Stieltjes quadrature, not a certificate): ‖F(n,0.10)‖ = 1.410949855 (n=7; matches DISC-0034's archive level-7 value), 1.410657602 (n=10), 1.410638935 (n=20), 1.410638933 (n=40). The limit ≈1.4106389 is above 1.410 by ≈6.4e−4, consistent with DISC-0035's prediction ≈1.4106, but not certified.

## Prior Art

Not searched; no novelty claimed.

## Novelty Analysis

CONJECTURE (repository's own open item).

## Falsification Attempts

Recursion values to n=40 above 1.410; not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Open. Decrease and convergence are proved (DISC-0106 (3)); only the value bound ≥1.410 is open.

## Patent Relevance

None.

## Related Discoveries

- DISC-0034. Parent record (J.1 part now THEOREM via DISC-0106).
- DISC-0106. Mathematical. Theorem AQ (monotonicity for every α; 0.10 bracket too wide).
- DISC-0035. Conjecture (archive-derived). Predicts L(0.10)≈1.4106.

## Open Questions

Certify 𝓛(0.10)≥1.410 (needs a bracket of relative width below ≈4e−4).

## Next Experiments

A finer interval certificate at α=0.10 (much finer grid, larger upper cutoff, certified tail 1−s r_n≥2/(4+s)).

## Reproduction Instructions

`python3 /workspace/scratch-ifi/indep_theorem_AQ.py` (section I). Repository: `git checkout 4b4509f6f086f3f52b034f55508862f130381f2b && python3 scripts/gasket_fractional_decimation.py` (α=0.10 certificate line).

## Evidence Log

- 2026-10-22 (later slice). IFI a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7 GASKET.md "Status of J.2 below: PROVED by Theorem AS (5)"; J.2 statement text byte-identical to parent 3ec0a064caa5. Repo witness scripts/gasket_fractional_limit_digits.py EXIT 0 (25 PASS); archive /workspace/scratch-ifi/indep_theorem_AS.py EXIT 0 (9 PASS): own 30-digit recursion quadrature ‖F(80,0.10)‖=1.410638933063971, inside the AS enclosure, margin over 1.410 = 6.389e−4.

- 2026-10-22. Split from DISC-0034 at its J.1 status change; repository J.2 text unchanged at 4b4509f6f086f3f52b034f55508862f130381f2b.

## Change History

- 2026-10-22. Initial archive entry (carried forward from DISC-0034, where J.2 was recorded on 2026-10-08).
- 2026-10-22. Status change CONJECTURE → THEOREM (DISC-0111, IFI Theorem AS at a6e6c74b680d6ef126b5e4b7cc1de3a939c2dcc7). Earlier text retained.
