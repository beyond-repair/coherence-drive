# Discovery: No uniform monomial trace certificate Tr_d(z_k^a z_{k−1}^b S_k) = 1 for the residue conjecture

## Discovery ID

DISC-0046

## Status

REJECTED

## Date Discovered

2026-10-08 (America/New_York). Archive pass after DISC-0041.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 649cab9dd38be1818588424b3b02bdb3b75b04b6. Paths: README.md "Residue condition: exact check to k = 46 and no monomial trace certificate" → Negative result; CLAIM_STATUS.md "Uniform monomial trace certificate" row (NOT CLAIMED, negative search); COMPLETION_LOG.md eighth run; scripts/check_residue_trace_monomials.py.

## Original Evidence

Exhaustive over all 2^k chains in GF(2^64) for k ≤ 8, d = 2^⌈log₂(k+1)⌉, f = z_k^a z_{k−1}^b or (z_k + 1)^a z_{k−1}^b with |a| ≤ 6, |b| ≤ 4: certificate counts 18, 120, 63, 49, 12, 0, 0, 4 for k = 1..8 (k = 8: f = z_7², z_7³, either sibling); none common to 2 ≤ k ≤ 8.

## Discovery

Rejected proof route: a uniform identity Tr_d(f·S_k) = 1 with f in this monomial family, which would prove S_k ≠ 0 for every k (DISC-0030). No member works even for 2 ≤ k ≤ 8, and k = 6, 7 admit none. Only this family is ruled out; nothing against the conjecture.

## Why It Matters

Like DISC-0037 for the subfield test, it closes an obvious proof shape for DISC-0030 and points the next attempt elsewhere.

## Derivation

Not applicable (finite exhaustive search).

## Assumptions

As DISC-0028 / DISC-0038 (chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ 1/z_i).

## New Results

Archive `/workspace/scratch-res/indep_trace_monomials.py`: independent field model GF(2^64) = F_2[x]/(x^64 + x^31 + x^30 + x^19 + 1), own GF(2)-elimination root solver and trace, same (a, b, sibling) grid. Counts 18, 120, 63, 49, 12, 0, 0, 4 for k = 1..8; k = 8 certificates exactly {(0,2,·), (0,3,·)} for both siblings, i.e. f = z_7², z_7³; common set for 2 ≤ k ≤ 8 empty. Exactly matches the repository.

## Prior Art

Not applicable.

## Novelty Analysis

REJECTED as a proof route. No novelty claimed.

## Falsification Attempts

The negative result was reproduced in a second field model with independent code.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Negative search, finite and exhaustive in its family. DISC-0030 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0030. Mathematical. The conjecture this route would have proved.
- DISC-0037. Failed hypothesis. The earlier rejected subfield route.
- DISC-0038. Computational. Exact range extended to k ≤ 46 in the same commit.

## Open Questions

Certificates with other f; the k = 2^j + 2 split into two equations over GF(2^{2^j}) recorded without conclusion in the repository.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 649cab9dd38be1818588424b3b02bdb3b75b04b6 && python3 scripts/check_residue_trace_monomials.py`. Archive: `python3 /workspace/scratch-res/indep_trace_monomials.py 8`.

## Evidence Log

- 2026-10-08. Recorded from README / CLAIM_STATUS / COMPLETION_LOG at 649cab9dd38be1818588424b3b02bdb3b75b04b6; archive reproduction as above.

## Change History

- 2026-10-08. Initial archive entry.
