# Discovery: Residue sums are nonzero for every power-of-two chain length

## Discovery ID

DISC-0029

## Status

THEOREM

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0028.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 7856c09ad9d566ab1cd6f10598aab660d352f635. Paths: README.md "Residue condition: power-of-two lemma and exhaustive check to k = 31" → Derivation / Lemma; CLAIM_STATUS.md row "Residue sums S_k ≠ 0 for every chain when k = 2^j (all j) — CLAIMED"; COMPLETION_LOG.md "fourth run".

## Original Evidence

README Lemma (power-of-two lengths) with a complete proof in the repository.

## Discovery

Let N(x) = x² + x on the algebraic closure of F_2, and let z_0 = 1, N(z_i) = z_{i−1}. For every j ≥ 0 and every such chain, S_{2^j} = Σ_{i=1}^{2^j} 1/z_i ≠ 0.

## Why It Matters

Via DISC-0028, it rules out coincidental decimation hits whose chain length k is a power of two, for every n. Together with the k ≤ 31 computation it gives exact h_n for 3 ≤ n ≤ 34 (DISC-0027 range).

## Derivation

Repository proof, checked line by line in this archive:
1. N = F + 1 as F_2-linear operators (F = Frobenius). F and 1 commute and the characteristic is 2, so N^{2^j} = F^{2^j} + 1, and ker N^{2^j} = {x : x^{2^{2^j}} = x} = GF(2^{2^j}) =: E_j, a field.
2. Along a chain, N^i(z_i) = 1 and N(1) = 0, so N^m(z_i) = 0 exactly when m ≥ i + 1. Hence z_i ∈ E_j iff i + 1 ≤ 2^j.
3. For k = 2^j: z_1, …, z_{k−1} ∈ E_j, so S_{k−1} ∈ E_j; z_k ∉ E_j, so 1/z_k ∉ E_j (E_j is a field). Therefore S_k = S_{k−1} + 1/z_k ∉ E_j, and in particular S_k ≠ 0.

## Assumptions

Elementary finite-field facts only. No W, no physics input.

## New Results

None beyond the repository's lemma. Archive check: no gap found; each step is standard.

## Prior Art

Not searched. The argument is elementary (Frobenius linearity, subfield membership). The repository states that no literature was opened and that no novelty is claimed. This archive also claims none.

## Novelty Analysis

THEOREM as a mathematical status (complete proof in the repository, verified). Not a novelty claim and not a novelty candidate: the method is textbook, and whether the statement appears in the literature was not checked.

## Falsification Attempts

Proof read step by step (above). Numerical consistency: the independent GF(2^16) exhaustive check (DISC-0030) covers k = 1, 2, 4, 8 and found S_k ≠ 0 everywhere; the repository's GF(2^32) enumeration covers k = 16 as well.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proved.

## Patent Relevance

None.

## Related Discoveries

- DISC-0028. Mathematical. The reduction that makes this lemma relevant to h_n.
- DISC-0030. Mathematical. The remaining non-power-of-two cases.
- DISC-0036. Mathematical. Same method extended to k = 2^j + 1 via the pairing identity.
- DISC-0037. Mathematical. The method fails for k = 6, 11, 13, 14, 15.

## Open Questions

Whether the same subfield argument extends to k = 2^j + r for small r. The repository records that Galois conjugation by F^{2^{j−1}} gave no contradiction at k = 2^{j−1} + 1.

## Next Experiments

See DISC-0030.

## Reproduction Instructions

Proof is self-contained (Derivation above). Numerical cross-checks as in DISC-0030.

## Evidence Log

- 2026-10-08. Recorded from README at 7856c09ad9d566ab1cd6f10598aab660d352f635; proof verified by reading.
- 2026-10-08 (later). Open question answered for r = 1 at bd212e6da68d4c71940c977400c66c507b40862a (DISC-0036); shown not to extend in general (DISC-0037). Status unchanged.

## Change History

- 2026-10-08. Initial archive entry.
- 2026-10-08 (later). Related links and Evidence Log appended; status unchanged.
