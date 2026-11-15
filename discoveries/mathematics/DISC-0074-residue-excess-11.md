# Discovery: Residue sums nonzero for every chain with excess k − 2^⌊log2 k⌋ ≤ 11 (elimination + lifted zeros)

## Discovery ID

DISC-0074

## Status

THEOREM (mathematical status only; complete elementary proof in the repository, structure verified here; no novelty claimed)

## Date Discovered

2026-10-15 (America/New_York), ~4:00am EDT archive pass.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, HEAD 35b3b90e3130ee620fa07556f88ef3a63f3c8141. Evidence commits: e821373250744928c708d5dacb2bcce69c48aa3d (lifted form of `direct`; p = 256 zero), ffda804fb4406452fc79771a8d2d2b90a52550fb (theorem excess ≤ 11: lift S = 0 count 0 at k = 523, 1035), 7bfe3e00b026353dd4ae2e682a55fddf83cd75b2 and 35b3b90e3130ee620fa07556f88ef3a63f3c8141 (k = 520 lift-vs-direct control; mode label fix). Paths: README.md "Residue condition: excess m=11 (partial: filter + directs through p=128)" and "Residue condition: excess m=11, lifted form of `direct` (2026-10-15)"; CLAIM_STATUS.md; COMPLETION_LOG.md 2026-10-15 entries; scripts/check_residue_p_plus_m.py, scripts/check_residue_lifted.py.

## Original Evidence

m = 11, e = 16, 128 orbit prefixes: R ≠ 0 on every prefix, deg R = 2046; surviving chain-condition counts {16: 66, 32: 24, 64: 21, 128: 6, 256: 5, 512: 3, 1024: 1}. Exact S = 0 counts are 0 at every survivor: `direct` at k = 27, 43, 75, 139 (2026-10-09) and `lift rep` at k = 267 (5 factors, 20480 chains, 10 with S ∈ GF(2^p)), k = 523 (3 factors, 12288 chains, 6 in GF(2^p), 4494.2 s) and k = 1035 (1 factor, 4096 chains, 2 in GF(2^p), 3145.2 s), all EXIT 0 in /workspace/scratch-res/lifted_rep_m11_p{256,512,1024}.log.

## Discovery

S_k ≠ 0 for every chain whenever k − 2^⌊log2 k⌋ ≤ 11. This extends DISC-0050 (excess ≤ 10) by one excess. First lengths newly covered by a proof: 27, 43, 75, 139, 267, 523, 1035, … (every 2^j + 11 with 2^j > 11). Range of exact h_n unchanged (3 ≤ n ≤ 48); smallest open length still 47 = 32 + 15.

## Why It Matters

It closes another band around every power of two by the same finite reduction as DISC-0050 and shows the lifted count is a usable replacement for `direct` at large p. It does not move the exact h_n range, which is blocked at k = 47 (excess 15).

## Derivation

Checked the new lemma (README "Lemma (reduction used by scripts/check_residue_lifted.py)") line by line. (1) Restriction to surviving factors: on a chain with S ∈ GF(2^p), c = z_1(α_1² + α_1) has degree p, so α_1 is a root of an irreducible factor f of R over GF(2^e) with deg f = p/e, and evaluation at a root is injective on GF(2^e)[x]/(f), so the chain condition at the root is the same as `filter`'s test mod f. Sound. (2) One root per factor: σ = Frob^e fixes GF(2^e), hence the prefix and f; it permutes the roots of f transitively and carries chains attached to r onto chains attached to σ(r) because the chain relations are over F_2; S = 0 and S ∈ GF(2^p) are σ-invariant. Sound. The theorem then rests on the DISC-0050 elimination plus zero counts at the seven m = 11 survivors.

## Assumptions

Chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2; S_k = Σ 1/z_i; prefix z_1..z_m ∈ GF(2^e) with e = 2^⌈log2(m+1)⌉; Frobenius orbit reduction of prefixes (DISC-0038); exact FLINT arithmetic (python-flint). S_W is not an input; no W is selected.

## New Results

Archive checks: (1) /workspace/scratch-res/indep_excess.py `filter 11 orbit` (own tower layout; log indep_excess_filter_m11.log) reproduces R_zero = 0, deg R = 2046, and the candidate and survivor counts exactly. (2) Repository positive controls of `lift all` against recorded `direct` (adm_c, chains, S ∈ GF(2^p), S = 0) agree in all recorded cases, including m = 11 at p = 16..128, m = 7 at p = 256 (k = 263), and m = 8 at p = 512 (k = 520; 5704.8 s vs 9069.6 s), from logs lifted_ctrl.log and big_8_512.log. (3) `verify` mode (every root) at m = 11, p = 32 and 64 gives identical per-root counts within each factor, as point (2) of the lemma predicts. The p = 512 and p = 1024 `rep` counts were not independently rerun in this pass (about 75 and 52 CPU-minutes); they are taken from the repository's EXIT 0 logs.

## Prior Art

Elementary Galois theory (relative norms in Artin–Schreier towers over finite fields; Frobenius equivariance). Not searched for this specific residue sum; the repository opened no literature and claims no novelty.

## Novelty Analysis

None claimed. Classified THEOREM only because the repository contains a complete proof (elimination lemma, lifted-count lemma, finite exact computation) that survives line-by-line checking, with the filter reproduced independently.

## Falsification Attempts

Looked for a gap between `lift` and `direct`: the restriction to surviving factors and the one-root-per-factor reduction both hold, and every recorded control matches, including the largest (k = 520). Looked for a missing survivor: the independent filter gives the same survivor set {16, …, 1024}, and on every orbit prefix the largest power-of-two-degree factor of R over GF(2^16) has degree 64 (p = 1024), so no larger p is a candidate. No discrepancy.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proof correct. Theorem: S_k ≠ 0 for every chain when k − 2^⌊log2 k⌋ ≤ 11. Exact h_n range unchanged (3 ≤ n ≤ 48).

## Patent Relevance

None.

## Related Discoveries

- DISC-0050. Mathematical. Excess ≤ 10 theorem; this entry adds excess 11 by the same proof structure.
- DISC-0029, DISC-0036, DISC-0047. Mathematical. Excess 0, 1, 2 lemmas.
- DISC-0038. Mathematical. Orbit reduction used by filter, direct, and lift.
- DISC-0030. Mathematical. Conjecture still open for excess ≥ 12 at k ≥ 47.
- DISC-0075. Mathematical. deg R = 2^m − 2 observed through m = 11; conjecture for all m.

## Open Questions

Residue conjecture for k ≥ 47 with excess ≥ 12; the k = 47 reduced walk (2^41 chains) the repository started at 03:56 EDT is pending and not claimed.

## Next Experiments

Archive suggestion only: independent rerun of `lift rep` at p = 1024 when the box is idle.

## Reproduction Instructions

`git checkout ffda804fb4406452fc79771a8d2d2b90a52550fb && python3 scripts/check_residue_lifted.py prepare 11 && python3 scripts/check_residue_lifted.py lift 11 1024 rep` (python-flint; see README for cache paths). Archive: `python3 /workspace/scratch-res/indep_excess.py filter 11 orbit`.

## Evidence Log

- 2026-10-15. Recorded from README excess-11 subsections at ffda804fb4406452fc79771a8d2d2b90a52550fb (HEAD 35b3b90e3130ee620fa07556f88ef3a63f3c8141); lemma verified; archive filter reproduced. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
