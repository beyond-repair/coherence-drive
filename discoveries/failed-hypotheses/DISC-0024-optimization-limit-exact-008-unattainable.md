# Discovery: Theorem D exact target matching to W* = 0.08 on k-ary trees

## Discovery ID

DISC-0024

## Status

REJECTED

## Date Discovered

2026-10-08. Same archive pass as DISC-0023.

## Source Repositories

beyond-repair/optimization-limit-conjecture, branch main, HEAD 9d3aed5077369e2cc89d58814a2b95c152568199. CONJECTURE.md "Optimization Target" and "Theorem D (Target Matching): Prove existence/uniqueness of parameters satisfying f(...) ≈ 0.08". experiments/core.py at the same HEAD already refuses the removed 0.08 search. PROOF_13A_LIMIT_CORRECTION.md already calls min_Θ |W(Θ) − 0.08| matching, not a theorem.

## Original Evidence

The repository quarantines the 0.08 search and reports the default miss |R_D − 0.08| = 0.697777 and the sweep's best |R_D − 0.08| = 0.031111 at R_D = 0.111111. It does not say whether 0.08 is reachable at all.

## Discovery

By DISC-0023, on k-ary trees with generic parameters R_∞ lies in {0, 1} ∪ { 1 − k^{-j_1} + k^{-(j_2+1)} : 0 ≤ j_1 ≤ j_2 }. If j_1 ≥ 1 the value is at least 1 − 1/k ≥ 1/2. If j_1 = 0 the value is k^{-(j_2+1)}, and k^m = 25/2 has no integer solution. So R_∞ = 0.08 = 2/25 exactly is unattainable for every k ≥ 1, a ∈ (0, 1), ε, x̄ off the boundary set. Approximate matches come only from choosing k: 1/12 ≈ 0.0833 or 1/13 ≈ 0.0769 at j_1 = 0, j_2 = 0; for k = 3 the nearest values are 1/9 and 1/27, and 1/9 is the sweep's 0.111111.

## Why It Matters

Theorem D as an exact statement is false on the implemented model, and any approximate hit is a free choice of the discrete datum k, not a derivation. This strengthens the repository's own quarantine; it does not reopen the 0.08 story.

## Derivation

Corollary of the DISC-0023 closed form plus the integer argument above.

## Assumptions

As DISC-0023. Other graph families G are not covered.

## New Results

Exact unattainability of 0.08 for the implemented tree model. Archive-derived.

## Prior Art

Elementary. The repository already quarantines the target as matching.

## Novelty Analysis

REJECTED reading (exact Theorem D on the implemented model). No novelty claimed.

## Falsification Attempts

The 3000-draw check in DISC-0023 never produced a limit outside the stated set. The sweep's best value 0.111111 equals 1/9 from the set.

## Experimental Validation

None.

## Mathematical Status

Rejected as stated for k-ary trees.

## Patent Relevance

None.

## Related Discoveries

- DISC-0023. Mathematical. Source closed form.
- DISC-0002, DISC-0011, DISC-0016, DISC-0018. Historical. Other rejected routes to 0.08 in the corpus.

## Open Questions

Non-tree families G in CONJECTURE.md.

## Next Experiments

None proposed. Do not refine the sweep grid to chase 0.08.

## Reproduction Instructions

As DISC-0023.

## Evidence Log

- 2026-10-08. Initial check at 9d3aed5077369e2cc89d58814a2b95c152568199.

## Change History

- 2026-10-08. Initial archive entry.
