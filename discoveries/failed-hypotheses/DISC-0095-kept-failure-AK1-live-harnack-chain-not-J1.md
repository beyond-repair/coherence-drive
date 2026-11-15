# Discovery: Sharpening the constants of the one-step neighbor-Harnack chain reaches Conjecture J.1's 0.70 (Kept Failure AK.1)

## Discovery ID

DISC-0095

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0094.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit d45c90c7fb92ae96d70edbe73e73b42c3206e55e. Paths: GASKET.md Theorem AK → Kept Failure AK.1, NOT THIS; Conjecture J.1 evidence paragraph; CLAIM_STATUS.md ("Two-moment Jensen on spec(L)⊂[0,6]…" row: live-constant chain σ≈0.9529<1, below 0.70 from level 4); scripts/gasket_fractional_moment_jensen.py.

## Original Evidence

GASKET.md Kept Failure AK.1: "the chain σ_n ≥ 1/(w_n + ((L^α)_pp − w_pq)/2) used in Theorems AI–AK reaches ‖F(n,0.45)‖ ≥ 0.70 once its constants are made sharp" is false. With every constant live (live w_n, (L^α)_pp, w_pq) the chain gives σ ≈ (0.959907, 0.953175, 0.952875, 0.952863, 0.952863, 0.952863) on levels 1–6, all < 1, while live σ_n ≈ 1.3525. Times live ‖F_frac(n)‖: ≈ (0.962609, 0.812489, 0.725939, 0.673494, 0.640883, 0.620062), below 0.70 from level 4. The loss sits in w_pj+w_qj ≥ 2w_aj on Far and in dropping the Far-side structure of v.

## Discovery

Rejected hypothesis: sharpening constants inside the one-step neighbor-Harnack family (AI → AJ → AK and beyond) proves Conjecture J.1's 0.70. False even at the live-constant limit of that family.

## Why It Matters

Stronger than DISC-0091/0093: those rejected particular constants; this rejects the whole family's ceiling on the computed range. DISC-0034 stays OPEN; a route to 0.70 needs a different comparison than one-step harmonicity at p,q. Not thrust.

## Derivation

Direct computation of the live-constant chain against 0.70 at levels 1–6; checked; no gap.

## Assumptions

As DISC-0094.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AK.log`, EXIT 0, 186 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AK.py` / `indep_theorem_AK.log`, ALL PASS, 171 PASS) reproduce all six live chain σ values and all six chain·‖F_frac‖ values to 6 digits; chain σ < 1 at every level; live σ_n > 1.35 (L6 1.352483); chain·‖F_frac‖ ≥ 0.70 at L1–3 and < 0.70 at L4–6, strictly decreasing on L1–6; chain ≤ live σ_n (consistency). With AA's level-uniform floor instead of live ‖F_frac‖, AK floor 0.058941, Harnack-constant-0 ceilings 0.123005 (w_n ≤ 2^(α−1)) and 0.133577 (w_n ≤ w_n⁺) are all < 0.70.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed the live chain independently on my own build; matches GASKET.md and the commit message. Caveat recorded honestly: the rejection is over the computed levels 1–6 (the repo's "from level 4" statement is a computed-range statement, and the chain values are still decreasing at level 6); it is not claimed as a proof for all n, and no claim of this archive depends on it beyond the range.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. DISC-0094 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0094. Mathematical. Theorem AK.
- DISC-0093, DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

Which comparison beyond one-step harmonicity at p,q (e.g. keeping the Far-side structure of v) could reach 0.70; not addressed by the repository.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0094.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AK.1 at d45c90c7fb92ae96d70edbe73e73b42c3206e55e; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
