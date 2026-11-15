# Discovery: Degree of the residue elimination polynomial, deg R = 2^m − 2 (finite lemma m ≤ 11; conjecture for all m)

## Discovery ID

DISC-0075

## Status

CONJECTURE (for general m; the finite cases m ≤ 11 are exact computations, verified independently here; no novelty claimed)

## Date Discovered

2026-10-15 (America/New_York), ~4:00am EDT archive pass.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit ffda804fb4406452fc79771a8d2d2b90a52550fb (HEAD 35b3b90e3130ee620fa07556f88ef3a63f3c8141). Paths: README.md "Residue condition: degree of the elimination polynomial R"; CLAIM_STATUS.md row "deg R = 2^m − 2 … PARTIAL"; scripts/check_residue_p_plus_m.py (`filter`).

## Original Evidence

For the elimination polynomial R = N_2(⋯N_m(G)⋯) ∈ GF(2^e)[x] of the excess-m argument (DISC-0050), the repository records deg R = 2^m − 2 on every checked prefix for m ≤ 11 (all prefixes for m ≤ 6, Frobenius-orbit prefixes for m ≥ 7), the degree recurrence d_0 = m − 1, d_r = 2 d_{r−1} − (m − r − 1) with closed form d_r = 2^{r+1} + m − r − 3, and R ∈ GF(2^e)[x²], both for m ≤ 8. The general statement for all m ≥ 2 is labelled a conjecture.

## Discovery

Conjecture: for every m ≥ 2 and every admissible prefix, deg R = 2^m − 2. Finite lemma: true for 2 ≤ m ≤ 11 on every prefix the repository checks.

## Why It Matters

R's degree bounds the number and size of surviving factors, hence the finite work needed to close each excess. A uniform degree formula is one ingredient toward handling excess ≥ 12 without per-m computation. On its own it does not prove any new residue length.

## Derivation

The crude bound is correct: A_m is free of rank 2^{m−1} over A_1, R is the determinant of multiplication by G, so deg R ≤ d_0 · 2^{m−1}. The repository's recurrence is an algebraic identity once d_0 = m − 1 and the stated leading-term cancellation at each norm step hold; those two facts are checked, not proved. Note that R ∈ GF(2^e)[x²] means R is a perfect square over the perfect field GF(2^e), so every irreducible factor occurs with even multiplicity; this is consistent with, but not used by, the filter.

## Assumptions

As in DISC-0050: tower A_1 = GF(2^e)[x], A_i = A_{i−1}[α_i]/(α_i² + α_i + β_i), e = 2^⌈log2(m+1)⌉; exact FLINT arithmetic. No W is selected.

## New Results

Archive script /workspace/scratch-res/indep_degR.py (uses the independent tower of /workspace/scratch-res/indep_excess.py; one process per m because python-flint segfaulted when several field contexts were created in one process). Log /workspace/scratch-res/indep_degR.log: m = 2..6 all prefixes (4, 8, 16, 32, 64) and m = 7..10 orbit prefixes (16, 16, 32, 64): every prefix has R ≠ 0 and deg R = 2^m − 2 (2, 6, 14, 30, 62, 126, 254, 510, 1022), and no prefix has a nonzero odd-degree coefficient, so R ∈ GF(2^e)[x²] holds through m = 10, two steps further than the repository records. m = 11, 128 orbit prefixes (log indep_degR_m11.log, 352.5 s): deg R = 2046 on all 128, R_zero = 0, no odd-degree coefficient, so R ∈ GF(2^e)[x²] holds through m = 11. The intermediate recurrence d_r was not independently checked.

## Prior Art

Norms in Artin–Schreier towers over finite fields are classical. This particular degree formula was not searched; the repository opened no literature and claims no novelty.

## Novelty Analysis

None claimed. A finite pattern with no general proof; recorded as CONJECTURE.

## Falsification Attempts

Searched every recorded prefix for m ≤ 10 and m = 11 for a degree drop or an odd-degree coefficient. None found.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Finite lemma (m ≤ 11) correct by exact computation. General statement open.

## Patent Relevance

None.

## Related Discoveries

- DISC-0050. Mathematical. The elimination whose R this describes.
- DISC-0074. Mathematical. Excess 11 closed with deg R = 2046.
- DISC-0030. Mathematical. A general degree formula would be one step toward excess ≥ 12.

## Open Questions

A proof of d_0 = m − 1 and the leading-term cancellation for general m; why R is a square.

## Next Experiments

Archive suggestion only: record d_r for m = 9, 10 orbit prefixes.

## Reproduction Instructions

`for m in 2 3 4 5 6 7 8 9 10 11; do python3 /workspace/scratch-res/indep_degR.py $m; done` with python-flint (/workspace/scratch-res/.venv-flint). Repository: `python3 scripts/check_residue_p_plus_m.py filter M [orbit]` at ffda804fb4406452fc79771a8d2d2b90a52550fb.

## Evidence Log

- 2026-10-15. Recorded from README "degree of the elimination polynomial R" at ffda804fb4406452fc79771a8d2d2b90a52550fb; archive degree and parity check as above.

## Change History

- 2026-10-15. Initial archive entry.
