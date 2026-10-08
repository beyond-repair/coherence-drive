# Discovery: Two-adic reduction of coincidental decimation hits on build_gasket(n)

## Discovery ID

DISC-0028

## Status

DERIVATIVE

## Date Discovered

2026-10-08 (America/New_York). Archive pass after the repository's third and fourth runs of the day.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, evidence commit 246a351291f9fea13ba87f29753ac3b2e0b7b1c0, indexed at HEAD 7856c09ad9d566ab1cd6f10598aab660d352f635. Paths: README.md "Two-adic reduction of coincidental hits on build_gasket(n)"; CLAIM_STATUS.md row "Two-adic reduction … CLAIMED"; COMPLETION_LOG.md "third run"; scripts/check_coincidental_reduction.py.

## Original Evidence

README theorem (two-adic reduction), with a six-step prose proof: (1) mod 2, Qt_n ≡ T^n(x) + 1 and Q_n ≡ x·T^{n−1}(x) with T(x) = x² + x; (2) same-channel exclusion from the reduced numerator (6 − λ)q(R) + 2R p(R); (3) cross-channel and standard-DN cases contradict the mod-2 forms; (4) s_n(2) = (s_{n−2}(−6) − 6)/3 > 0 by a Herglotz-type bound; (5)–(6) symmetric DN chains ending at 6 have v_2(y_i) = −1, chains ending at 5 with m odd have v_2(y_i) = 0, and for m even the residue of y_k/2 telescopes to z_k·Σ 1/z_i.

## Discovery

For every n ≥ 3, a coincidental hit (DISC-0027) can only be seen by the symmetric channel, must satisfy R^k(λ) = 5 with 1 ≤ k ≤ n − 2 and n − k even, and its residue chain z_0 = 1, z_{i−1} = z_i² + z_i over F̄_2 must have S_k = Σ_{i=1}^k 1/z_i = 0. The standard channel never has coincidental hits for any n, and λ = 2 is not corner-visible for n ≥ 3. The all-n question of DISC-0027 is thereby reduced to a characteristic-2 statement that depends only on k (DISC-0029, DISC-0030).

## Why It Matters

It replaces an n-dependent polynomial gcd with a single finite-field condition indexed by chain length, and it is the step that lets the exact-h_n range jump from n ≤ 11 (DISC-0026) to n ≤ 18 and then n ≤ 34.

## Derivation

In the repository README, steps 1–6 as summarized above. Archive read the steps line by line: R ≡ T mod 2 so the residue chain is z_{i−1} = z_i² + z_i with z_0 = 5̄ = 1; the identity 1/z_i = (1 + z_i)/z_{i−1} that drives the telescoping follows from z_{i−1} = z_i(z_i + 1); the valuation claims for a = 5 use v_2(3^{m−2} − 1) = 1 for m odd and ≥ 3 for m even, which checks.

## Assumptions

Everything in DISC-0026 (corner-channel recursion, reduced forms, cancellation analysis, s_m(6) = t_m(6) = −3, poles in (0, 6)); DN_m(2) = 0 for all m.

## New Results

None archive-side beyond reproduction. The repository's script reproduces the mod-2 congruences of Step 1 and the values s_m(6), s_m(5) = 5(3^{m−2} − 1)/2, s_n(2) exactly for n, m ≤ 8 (run at 7856c09: OK). Its default argument checks residue chains only to k = 13; the CLAIM_STATUS "k ≤ 16 in GF(2^64)" row needs `python scripts/check_coincidental_reduction.py 16`. The k ≤ 31 extension supersedes that range anyway (DISC-0030).

## Prior Art

Not searched beyond DISC-0026. Reducing spectral-decimation questions mod 2 is a standard move; the repository explicitly disclaims novelty of the method.

## Novelty Analysis

DERIVATIVE. A careful, repository-proved reduction built on classical decimation; no novelty claimed by the repository or by this archive.

## Falsification Attempts

Step-by-step read of the prose proof (no gap found in the steps checked: mod-2 forms, telescoping identity, valuation bookkeeping). Consistency with the archive's exact-Z gcd certificate n = 3..14 (DISC-0027): agrees. Exact ingredient checks rerun at 7856c09: pass.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Repository-proved (prose) reduction; ingredients exactly checked for small n, m. Not elevated to THEOREM in this archive because Steps 2–6 depend on DISC-0026's cancellation analysis, which is itself prose plus finite checks.

## Patent Relevance

None.

## Related Discoveries

- DISC-0027. Mathematical. The all-n statement this reduces.
- DISC-0029. Mathematical. Residue condition settled for every power-of-two k.
- DISC-0030. Mathematical. The remaining residue conjecture.

## Open Questions

The a = 5, m even case has no 3-adic or 5-adic argument (the repository notes the valuations tie at every step).

## Next Experiments

An independent symbolic re-derivation of Step 5 (s_n(2) formula) for general n.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/finite-gasket-spectral-derivatives
cd finite-gasket-spectral-derivatives && git checkout 7856c09
python scripts/check_coincidental_reduction.py 16
```

## Evidence Log

- 2026-10-08. Evidence commit 246a351291f9fea13ba87f29753ac3b2e0b7b1c0 (two-adic reduction), indexed at HEAD 7856c09 (residue extension). Script rerun at 7856c09: mod-2 congruences and channel values OK; residue chains k ≤ 13 OK.

## Change History

- 2026-10-08. Initial archive entry.
