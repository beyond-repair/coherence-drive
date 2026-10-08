# Discovery: Residue sums nonzero for every chain with excess k − 2^⌊log2 k⌋ ≤ 10 (elimination + direct zeros)

## Discovery ID

DISC-0050

## Status

THEOREM (mathematical status only; complete elementary proof in the repository, verified here; no novelty claimed)

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0047 / DISC-0049.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, HEAD b0cc73b9d0a550cff97477508d0e670665186a84. Evidence commits: a7ea28016bbad2731d57fc15f2da9b7518468825 (excess 3..6/7 pending 263), cc2e0f035f69b99dbf0e5146fa35c22e83269ff2 (direct zeros 73/136/137; excess 8–9 pending), cbc9a2817850728fc4463a6fc07e7f2fce000637 (k=264 zero), b0cc73b9d0a550cff97477508d0e670665186a84 (close 263/265/266/520 and m=10; none pending for excess ≤ 10). Paths: README.md "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)"; CLAIM_STATUS.md; COMPLETION_LOG.md tenth run; scripts/check_residue_p_plus_m.py.

## Original Evidence

For fixed excess m = k − 2^⌊log2 k⌋, with e = 2^⌈log2(m+1)⌉, the z_p-coordinate equation C_1 = 0 of the p+2 argument clears to an element G in a rank-2^{m−1} Artin–Schreier tower over GF(2^e)[x]; its iterated relative norm R ∈ GF(2^e)[x] is nonzero on every prefix for m ≤ 10. Surviving p = e·deg f (power-of-two factor degrees that pass the chain condition N^{p−1−m}(c) = z_m) are finite. Exact `direct` counts of S = 0 among chains with S ∈ GF(2^p) are 0 at all survivors including k = 71–74, 136–138, 263–266, 520. Positive control: naive vs direct S ∈ GF(2^p) counts at k = 6, 7, 11–15 equal 8, 0, 32, 0, 48, 32, 176. Exact h_n range unchanged (3 ≤ n ≤ 48); smallest open length still 47 = 32 + 15.

## Discovery

S_k ≠ 0 for every chain whenever k − 2^⌊log2 k⌋ ≤ 10. With earlier lemmas (excess 0, 1, 2 = DISC-0029/0036/0047), every such k is proved. First lengths newly covered by a proof: 67–74, 131–138, 263–266, 520, …. Pending none for excess ≤ 10. Conjecture remainder: excess ≥ 11 for k ≥ 47 (DISC-0030).

## Why It Matters

It closes a uniform band of lengths around every power of two by a finite-reduction argument, without extending the exact h_n range (still blocked at k = 47).

## Derivation

Checked line by line against README Steps 1–4 and the two lemmas (finite reduction; complete list of remaining chains). Coordinates α_i = z_{p+i} + z_i z_p, relative norms Nm_i, C_1 = ω²/(α_1+1) + Σ z_i/Nm_i, and R = Norm(G) with G clearing the denominator of C_1 match the p+2 special case (DISC-0047) at m = 2. Frobenius orbit reduction (DISC-0038) justifies one prefix per orbit. No gap found in the reduction; the theorem then rests on R ≠ 0 (filter) and S = 0 counts (direct) for the finite survivor list.

## Assumptions

Chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2; S_k = Σ 1/z_i; Galois action σ = F^p from DISC-0038; exact FLINT arithmetic via python-flint. S_W is not an input; no W is selected.

## New Results

Archive `/workspace/scratch-res/indep_excess.py` (own tower layout; naive positive control in bit-packed GF(2^32) mod x^32+x^22+x^2+x+1, independent of the repository field): (1) naive counts match 8/0/32/0/48/32/176 at k = 6,7,11–15; (2) filter m = 2..10: R_zero = 0, deg R = 2^m − 2, survivors match the README table; (3) direct S = 0 at k = 11,13–15,22,23,38,39,71–74,136,263 (orbit where noted). Repository script spot-check at b0cc73b: filter m = 3 and direct k = 11 match (surv = {8: 8}; S_in = 32, S = 0 = 0). Larger survivors 137–138, 264–266, 520: same algorithm; repository records zeros; mid-range + logic reproduction support the classification.

## Prior Art

Elementary Galois theory (relative norms in Artin–Schreier towers over finite fields). Not searched for this specific residue sum; the repository opened no literature and claims no novelty.

## Novelty Analysis

None claimed. Classified THEOREM only because the repository contains a complete proof (elimination + finite exact computation) that survives line-by-line checking and independent computation.

## Falsification Attempts

Re-derived the elimination; reproduced positive controls in an independent field model; reproduced filter survivors and mid-range direct zeros. No discrepancy. The subfield test alone fails at those mid-range lengths (nonzero S ∈ GF(2^p) counts), as the repository records.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proof correct. Theorem: S_k ≠ 0 for every chain when k − 2^⌊log2 k⌋ ≤ 10. Range of exact h_n unchanged (3 ≤ n ≤ 48).

## Patent Relevance

None.

## Related Discoveries

- DISC-0029, DISC-0036, DISC-0047. Mathematical. Excess 0, 1, 2 lemmas this run completes through excess 10.
- DISC-0038. Mathematical. Orbit reduction used in filter/direct.
- DISC-0030. Mathematical. Conjecture still open for excess ≥ 11 at k ≥ 47.
- DISC-0037, DISC-0046. Failed hypothesis. Other proof shapes that do not close the conjecture.

## Open Questions

Residue conjecture for k ≥ 47 with excess ≥ 11; m = 11 filter survivors (including p = 1024) not closed; exact h_n for n ≥ 49.

## Next Experiments

Archive suggestion only: orbit-reduced direct at m = 11 survivors if feasible.

## Reproduction Instructions

`git checkout b0cc73b9d0a550cff97477508d0e670665186a84 && python3 scripts/check_residue_p_plus_m.py filter 3 && python3 scripts/check_residue_p_plus_m.py direct 3 8`. Archive: `python3 /workspace/scratch-res/indep_excess.py naive`, `… filter M [orbit]`, `… direct M P [orbit]`.

## Evidence Log

- 2026-10-08. Recorded from README excess-m section at b0cc73b9d0a550cff97477508d0e670665186a84; proof verified; archive checks as above. Repository description still matches its claim fence.

## Change History

- 2026-10-08. Initial archive entry.
