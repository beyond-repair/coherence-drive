# Discovery: Residue sums nonzero for every chain length 2^j + 2 (relative-trace argument)

## Discovery ID

DISC-0047

## Status

THEOREM (mathematical status only; complete elementary proof in the repository, verified here; no novelty claimed)

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0046.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 80e28408da5ef676833297167e998744ce0c6b55. Paths: README.md "Residue condition: lengths 2^j + 2 (relative-trace argument)" (Assumptions, Derivation Steps 1–3, Lemma, Exact finite verification, Corollary, Remark, Still open, Not a consequence); CLAIM_STATUS.md new row "Residue sums S_k ≠ 0 (indeed S_k ∉ GF(2^{2^j})) … k = 2^j + 2"; COMPLETION_LOG.md; scripts/check_residue_p_plus_two.py.

## Original Evidence

Fix p = 2^j, j ≥ 2, c = z_{p−1}, ω = z_1, ζ = z_2, σ = F^p generating Gal(GF(2^{2p})/GF(2^p)). Coordinates α_i = z_{p+i} + z_i z_p ∈ GF(2^p) satisfy α_i² + α_i = α_{i−1} + c z_i². Relative norms Nm(z_p) = c, Nm(z_{p+1}) = ω²α_1, Nm(z_{p+2}) = α_1 + (1+ζ)α_2 give S_{p+2} = S_0′ + C_1 z_p with C_1 = ω²/(α_1+1) + ζ/(α_1 + (1+ζ)α_2). C_1 = 0 is linear in α_2; substituting gives a quadratic Q(α_1) over GF(16) whose linear coefficient vanishes and whose constant μ² + μ is nonzero, so any solution has α_1 ∈ GF(16), hence c ∈ GF(16). Since c has degree p ≥ 8, S_{p+2} ∉ GF(2^p) for j ≥ 3; with k = 4, 6 every k = 2^j + 2 has S_k ≠ 0. Repository counts of chains with S_{p+2} ∈ GF(2^p): 8 (k = 6), 0 (k = 10), 0 (k = 18, one chain per Frobenius orbit).

## Discovery

A third infinite family of chain lengths for the residue conjecture (DISC-0030), after powers of two (DISC-0029) and 2^j + 1 (DISC-0036). It does not move the smallest open length (47) or the exact h_n range (3 ≤ n ≤ 48). First lengths newly covered by proof rather than computation: 66, 130, 258, ….

## Why It Matters

It shows the subfield method can be pushed past 2^j + 1 by working in coordinates over GF(2^p) and reducing to a single z_p-coefficient equation. The repository's Remark proposes extending this to 2^j + m when the C_1-system is zero-dimensional; that is a strategy only and is not checked for any m ≥ 3.

## Derivation

Checked line by line. Step 1: squaring z_{p+i} = α_i + z_i z_p with z_p² = z_p + c and matching the 1 and z_p coefficients gives the stated recursion; σ-invariance of α_i uses σ(z_{p+i}) = z_{p+i} + z_i and σ(z_p) = z_p + 1. Step 2: Nm(a + b z_p) = a² + ab + b²c and the z_p-coordinate of 1/x is b/Nm(x); the three norms reduce as stated using c = ω(α_1² + α_1) and α_2² = α_2 + α_1 + ζ²c; the combination 1/c + ω²/α_1 = ω²/(α_1 + 1) is correct. Step 3: solving C_1 = 0 gives α_2 = λα_1 + μ with λ = ω(ζ + ω²)/(1 + ζ), μ = ωζ/(1 + ζ); substitution gives Q exactly as written. If the linear coefficient were nonzero the argument would still bound α_1 to GF(256), so the lemma for p ≥ 16 does not even depend on that cancellation; for p = 8 it does, and it holds. Degree claim: z_{p−1} has degree exactly p because 2^{j−1} ≤ p − 1 < 2^j. No gap found.

## Assumptions

Chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2; S_k = Σ_{i=1}^k 1/z_i; the Galois action from the repository's sixth run (DISC-0038); elementary characteristic-2 algebra. S_W is not an input; no W is selected.

## New Results

Archive `/workspace/scratch-res/indep_pplus2.py` (own field model GF(2^32) mod x^32+x^22+x^2+x+1 and GF(2^64) mod x^64+x^4+x^3+x^2+1, own upward solver; not the repository's code): (1) for all four choices of (z_1, z_2), λ, μ ∈ GF(16), the linear coefficient of Q is 0, μ² + μ ≠ 0, A ≠ 0; (2) exhaustive upward enumeration of all chains: k = 6 (64 chains) has exactly 8 with S_6 ∈ GF(16), k = 10 (1024 chains) has 0 with S_10 ∈ GF(2^8), and the C_1 = 0 ⇔ S ∈ GF(2^p) equivalence and α_1 ∈ GF(16) when C_1 = 0 hold on every chain; k = 18 (all 262144 chains, not one per orbit) has 0 with S_18 ∈ GF(2^16), 0 zeros, and the C_1 equivalence holds on every chain; (3) 300 random chains in GF(2^64): S_34 ≠ 0 and S_34 ∉ GF(2^32) on all of them. Repository script rerun at 80e2840: "all checks OK" (counts 8, 0, 0; A ≠ 0, B = 0, C ≠ 0 for all four (z_1, z_2)).

## Prior Art

Elementary Galois theory of finite fields (relative norm and trace for a quadratic extension GF(2^{2p})/GF(2^p), Artin–Schreier equations). Not searched for this specific residue sum; the repository opened no literature and claims no novelty.

## Novelty Analysis

None claimed. Classified THEOREM only because the repository contains a complete proof that survives line-by-line checking and independent computation.

## Falsification Attempts

Re-derived every identity; tested the critical GF(16) cancellations in a different field model; checked that the argument fails exactly where it must (p = 4, where 8 chains have S_6 ∈ GF(16)); exhaustive k = 10 and k = 18 counts in an independent field; random k = 34 in GF(2^64). No discrepancy.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proof correct. Lemma: for every j ≥ 3 and every chain, S_{2^j+2} ∉ GF(2^{2^j}), so S_{2^j+2} ≠ 0; with k = 4 and k = 6, S_k ≠ 0 for every k = 2^j + 2.

## Patent Relevance

None.

## Related Discoveries

- DISC-0029. Mathematical. Power-of-two lengths, same subfield method.
- DISC-0036. Mathematical. Lengths 2^j + 1; this run is one step further.
- DISC-0037. Computational. The k = 6 count 8 that this argument must (and does) allow at p = 4.
- DISC-0038. Mathematical. Galois action σ(z_i) = z_i + z_{i−p} used in Step 1; computation k ≤ 46.
- DISC-0030. Mathematical. Conjecture still open for k ≥ 47 outside {2^j, 2^j + 1, 2^j + 2}.

## Open Questions

Zero-dimensionality of the C_1-system for k = 2^j + m, m ≥ 3 (repository Remark, not checked); the residue conjecture for k = 47 and beyond; exact h_n for n ≥ 49.

## Next Experiments

Gröbner-basis dimension test of the m = 3 C_1-system over GF(64) (the field generated by z_1, z_2, z_3). Archive suggestion only.

## Reproduction Instructions

`git checkout 80e28408da5ef676833297167e998744ce0c6b55 && python3 scripts/check_residue_p_plus_two.py`. Archive: `python3 /workspace/scratch-res/indep_pplus2.py alg`, `… ex`, `… rnd 300`.

## Evidence Log

- 2026-10-08. Recorded from README "Residue condition: lengths 2^j + 2" at 80e28408da5ef676833297167e998744ce0c6b55; proof verified; archive checks as above. Repository description still matches its claim fence.

## Change History

- 2026-10-08. Initial archive entry.
