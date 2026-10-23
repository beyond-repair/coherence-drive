# Discovery: Kept Failure BO.1, ω_k is not monotone below a* at any level k≥3

## Discovery ID

DISC-0163

## Status

REJECTED (repository's own Kept Failure): the statement "ω_k is increasing in y" fails for every α<A_lo=0.016778880172852 at every level k≥3. The failure is certified by the repository with exact J=7/8 moment bounds. It does NOT show that δ_N^(n) fails to increase below a*.

## Date Discovered

2026-10-23 (America/New_York), ~10:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 18bb38dcc3688510f2ef44134db70aa8f47fb530.

## Original Evidence

GASKET.md Kept Failure BO.1 and scripts/gasket_fractional_weight_threshold.py at 18bb38dcc3688510f2ef44134db70aa8f47fb530.

## Discovery

At y*=13.778505644 the J=7/8 moment bounds give Φ_k(y*)≥0.0167788801728520 for every k≥3, so (log ω_k)'(y*)=(α−Φ_k(y*))/(5+y*)<0 for every α<A_lo. For α∈(a_0*,a*) the base level k=0 is monotone but no level k≥3 is.

## Why It Matters

Shows BN.2's α≥1/17 restriction (DISC-0161) was a method limit, and that the true threshold a* (DISC-0162) is sharp: BN.3's Chebyshev route to monotone δ_N^(n) is closed below a*.

## Derivation

BO.1's logarithmic derivative plus BO.2's lower moment bound at one point y*.

## Assumptions

As DISC-0162 (BN.1 Stieltjes form, AQ identity at every level).

## New Results

The threshold in DISC-0162 cannot be lowered for k≥3.

## Prior Art

None specific; standard moment bounds.

## Novelty Analysis

Repository's own negative result; novelty UNRESOLVED (constant not searched).

## Falsification Attempts

Independent mpmath (50 digits): Φ_k(13.778505644)>A_lo for k=3..7 (value 0.01677888017287613…, margin ≈2.4e−14 above A_lo); PASS. Repository witness line "KEPT FAILURE BO.1 ... ok".

## Experimental Validation

/workspace/scratch-ifi/indep_theorem_BO.log, /workspace/scratch-ifi/repo_theorem_BO.log.

## Mathematical Status

Theorem-backed refutation of the monotone-weight statement below A_lo (k≥3).

## Patent Relevance

None. Not thrust.

## Related Discoveries

DISC-0162 → DISC-0163 (mathematical). DISC-0161 → DISC-0163 (historical: BN.2's method limit at 1/17).

## Open Questions

Does δ_N^(n) still increase in n for α<a*?

## Next Experiments

Direct float/arb computation of δ_N^(n) at α=0.01.

## Reproduction Instructions

As DISC-0162.

## Evidence Log

- 2026-10-23 ~10:01am EDT. Indexed.

## Change History

- 2026-10-23. Initial archive entry.
