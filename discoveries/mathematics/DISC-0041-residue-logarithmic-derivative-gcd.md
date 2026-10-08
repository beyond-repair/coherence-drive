# Discovery: Logarithmic-derivative form of the residue sum and an F_2[t] gcd reformulation

## Discovery ID

DISC-0041

## Status

DERIVATIVE

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0038.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 8d2cddf338b1c08b436273c505ec3b2273972828. Paths: README.md "Residue condition: logarithmic-derivative form and a polynomial gcd certificate" (Lemma items 1–5, Corollary, Negative remarks, Exact finite verification); CLAIM_STATUS.md logarithmic-derivative row and the updated "Exact h_n for all n" row; COMPLETION_LOG.md seventh run; scripts/check_residue_logderiv.py.

## Original Evidence

With N(t) = t² + t, A_k = N^k(t) + 1 and Π_k = ∏_{j<k} N^j(t) in F_2[t]: S_k = Π_k′(z_k)/Π_k(z_k); the product of Π_k over all roots of A_k is 1, so the norm of S_k is Res(A_k, Π_k′) and the number of chains with S_k = 0 is deg gcd(A_k, Π_k′); Π_k = a_k² + t b_k² with Π_k′ = b_k². Corollary: the residue condition at length k holds ⇔ gcd(N^k + 1, Π_k′) = 1. Certificate gcd = 1 for 1 ≤ k ≤ 21 (schoolbook Euclid, k = 21 in 80 s). The repository states that this does not extend the k ≤ 45 range and claims no novelty.

## Discovery

An exact, proved reformulation of the residue conjecture DISC-0030 as a coprimality statement for two explicit polynomials over F_2, plus a chain-free finite certificate. It does not prove DISC-0030 for any new k.

## Why It Matters

It turns the open set of DISC-0030 (k ≥ 46, k ∉ {2^j, 2^j + 1}) into a single polynomial gcd per k, independent of any model of a large finite field. For k = 2^B − 1 the chain endpoints are exactly the trace-one elements of GF(2^{2^B}).

## Derivation

Checked line by line. (1) N is additive with N′ = 1, so (N^j)′ = 1 by the chain rule and N^j = (F + 1)^j = Σ_{i ⊆ j} t^{2^i} by Lucas. (2) A_k′ = 1, so A_k is separable; for k = 2^B − 1 all binary digits are set and N^k is the trace polynomial of GF(2^{2^B}). (3) z_i = N^{k−i}(z_k), so S_k = Σ_{j<k} 1/N^j(z_k) = Π_k′/Π_k at z_k. (4) N^j maps roots of A_k 2^j-to-1 onto roots of A_{k−j}, and A_m(0) = 1, so ∏_z Π_k(z) = ∏_j A_{k−j}(0)^{2^j} = 1; hence ∏_z S_k(z) = ∏_z Π_k′(z) = Res(A_k, Π_k′) (A_k monic), and zeros are counted by deg gcd since A_k is separable. (5) Π_k(t) = t Π_{k−1}(N(t)) gives Π_k = (t b_{k−1}(N))² + t (a_{k−1}(N) + t b_{k−1}(N))², which is the stated recursion; Π′ = b² in characteristic 2. No gap found.

## Assumptions

Characteristic 2; chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2 (the DISC-0028 setting).

## New Results

Archive independent checks (not repository code):

- `/workspace/scratch-res/indep_logderiv_flint.py`: FLINT `nmod_poly` (modulus 2, sub-quadratic gcd) builds N^j from the Lucas formula and Π_k as a product, and computes gcd(A_k, Π_k′). deg Π_k = 2^k − 1, deg Π_k′ = 2^k − 2, and deg gcd = 0 for every 1 ≤ k ≤ 23 (k = 22 in 40 s, k = 23 in 103 s). This reproduces the repository certificate (k ≤ 21) with a different gcd algorithm and slightly extends it; it does not extend the S_k ≠ 0 range, which is already k ≤ 45 by DISC-0038.
- `/workspace/scratch-res/indep_logderiv_enum.py`: in GF(2^8) mod x^8 + x^4 + x^3 + x + 1, the 128 roots of N^7(t) = 1 are exactly the 128 trace-one elements (item 2 for B = 3); no chain has S_7 = 0; exactly 8 chains have S_7 = z³. FLINT gives deg gcd(A_7, Π_7′ + t³ Π_7) = 8, matching the repository's positive control (k = 7, c = t³: 8 chains).
- Repository `scripts/check_residue_logderiv.py` rerun at 8d2cddf: all six checks OK, certificate k ≤ 20 (script default; README quotes k ≤ 21 with an argument), 17 nonzero positive-control cases including (k = 7, c = t³, 8).
- Archive note: the repository says no fast half-gcd library is installed on the box; python-flint is present in the archive's own audit venv (/workspace/fgsd-audit/venv). This is an environment remark, not a contradiction of any claim; even FLINT's gcd grows about 2.5× per k, so the gcd route does not reach k = 46 here either.

## Prior Art

Logarithmic derivatives of products and norms as resultants are standard (any algebra text). Not searched further; the repository claims no novelty.

## Novelty Analysis

None claimed. A standard-tool reformulation of an open repository conjecture; hence DERIVATIVE rather than THEOREM, even though the lemma is fully proved, because it settles no new case.

## Falsification Attempts

Tried to break item 4 and the counting claim with nonzero targets: the gcd count against direct enumeration matched (k = 7, c = t³). Tried the square decomposition on Π_k for k ≤ 12 through the FLINT build (deg Π_k′ = 2^k − 2 as required by deg b_k = 2^{k−1} − 1). None failed.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Reformulation proved. DISC-0030 stays CONJECTURE (open for k ≥ 46, k ∉ {2^j, 2^j + 1}), now equivalently gcd(N^k + 1, Π_k′) = 1. DISC-0027 stays CONJECTURE; exact h_n range unchanged at 3 ≤ n ≤ 47.

## Patent Relevance

None.

## Related Discoveries

- DISC-0030. Mathematical. The conjecture this reformulates.
- DISC-0036. Mathematical. Its norm form G_k(1, 0) = 1 is made explicit here as a resultant (no term-by-term identification claimed by the repository).
- DISC-0038. Computational. The range k ≤ 45 this does not extend.

## Open Questions

Whether the remainder-sequence regularity the repository records (stable top segments; about 0.375 · 2^k Euclid steps) can be turned into a proof of gcd = 1. Recorded by the repository as a numerical observation only.

## Next Experiments

A half-gcd at k ≥ 46 needs polynomials of degree ~2^46; not feasible on the box. A structural argument on b_k modulo A_k is the only visible route.

## Reproduction Instructions

`git checkout 8d2cddf338b1c08b436273c505ec3b2273972828 && python3 scripts/check_residue_logderiv.py`. Archive: `/workspace/fgsd-audit/venv/bin/python /workspace/scratch-res/indep_logderiv_flint.py 23` and `python3 /workspace/scratch-res/indep_logderiv_enum.py`.

## Evidence Log

- 2026-10-08. Recorded from README / CLAIM_STATUS at 8d2cddf338b1c08b436273c505ec3b2273972828; proof verified; archive FLINT certificate and GF(2^8) enumeration as above.

## Change History

- 2026-10-08. Initial archive entry.
