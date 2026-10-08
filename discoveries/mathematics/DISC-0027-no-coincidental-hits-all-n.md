# Discovery: No coincidental decimation hits for all n (exact h_n on build_gasket(n))

## Discovery ID

DISC-0027

## Status

CONJECTURE

## Date Discovered

2026-10-08. Same archive pass as DISC-0026.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, commit 7b1495fe1dd322d17f7b7d840b22c7d9f29faf10. Paths: README.md "Corner channels and coincidental hits on build_gasket(n)" → "Still open"; CLAIM_STATUS.md row "Exact h_n formula for all n — NOT CLAIMED, open"; scripts/check_corner_channels.py.

## Original Evidence

README "Still open" at 7b1495f: coincidental hits for general n ≥ 12, i.e. gcd(Q_n Qt_n, H_{n−1}∘R) = λ for all n, is not proved; mod 23 gave minimal gcd degrees for n = 3..9 but no inductive structure mod a fixed prime was found.

## Discovery

Conjecture (repository open item, recorded with its evidence): for every n ≥ 3, no corner-visible eigenvalue λ ≠ 0 of free L_n has R(λ) = λ(5 − λ) ∈ Spec(L_{n−1}). Equivalently gcd(Q_n Qt_n, H_{n−1}∘R) = λ, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly.

## Why It Matters

It would make DISC-0025's lower bound an identity for all n and give a closed form for h_n.

## Derivation

None. This is an open statement.

## Assumptions

As DISC-0026.

## New Results

Archive-side exact evidence only: the gcd identity holds over Z for every n = 3..14 (DISC-0026 falsification attempts). The repository's own evidence is n = 3..11 over F_p with p = 2^61 − 1.

## Prior Art

Not searched beyond DISC-0026. The question is a finite-graph refinement of classical decimation bookkeeping; no novelty is claimed.

## Novelty Analysis

CONJECTURE. Not a candidate for novelty, not a THEOREM: no proof exists in the repository or the archive.

## Falsification Attempts

Exact Z gcds for n = 3..14 (archive) and direct characteristic-polynomial gcds for n = 3..6 found no coincidental hit. Not broken; not proved. Floating point is not usable here: the repository notes the minimum distance from R(λ) to Spec(L_{n−1}) shrinks to about 4·10^{−4} by n = 5.

## Experimental Validation

None.

## Mathematical Status

Open. Exact evidence n = 3..14.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0026. Mathematical. Supplies the reduction and the finite certificate.
- DISC-0025. Mathematical. The bound this would make exact.

## Open Questions

An inductive argument: e.g. a resultant or valuation structure of Q_n, Qt_n under composition with R that excludes common roots with H_{n−1}∘R.

## Next Experiments

Push the exact gcd past n = 14 only as evidence; look for a proof via the factorization of H_{n−1}∘R and the interlacing of channel poles.

## Reproduction Instructions

See DISC-0026.

## Evidence Log

- 2026-10-08. Recorded from README "Still open" at 7b1495f; archive exact-Z certificate n = 3..14.

## Change History

- 2026-10-08. Initial archive entry.
