# Discovery: Multi-scale resistance weights freeze the harmonic audit (Kept Failure W.1)

## Discovery ID

DISC-0064

## Status

REJECTED

## Date Discovered

2026-10-09 (America/New_York). Same archive pass as DISC-0063.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 92b869ede53c77d04e923e4cf9be4537572bbb67. Paths: GASKET.md Theorem W → "KEPT FAILURE W.1 (no multi-scale resistance freeze)"; scripts/gasket_multiscale_weights.py; CLAIM_STATUS.md.

## Original Evidence

The hoped-for law "resistance weights λ=5/3 on the multi-scale edge set freeze the harmonic audit at the finite nonzero constant √21/2 by the same cancellation as Theorem S" is false. Under Theorem W the multi-scale resistance audit is exactly (n+1)√21/2 (already past 16 at level 6), while the finest-only resistance value stays √21/2. Finite freeze on this graph sits at λ < 5/3 (e.g. λ=1 gives 5√21/4).

## Discovery

Rejected hypothesis: multi-scale resistance weights inherit Theorem S's finite nonzero harmonic freeze. False; multi-scale resistance diverges linearly.

## Why It Matters

Closes one multi-scale route to a finite nonzero harmonic dipole via resistance. Does not speak to L^{0.45} on either graph; DISC-0034 stays OPEN.

## Derivation

DISC-0063 / Theorem W at λ=5/3. Checked; no gap.

## Assumptions

Multi-scale edge set; resistance λ=5/3; Theorem W closed form.

## New Results

Archive witness: λ=5/3 through level 6 equals (n+1)√21/2; contrast finest-only stays √21/2. Independent log `/workspace/scratch-ifi/indep_theorem_W.log` reproduces the same and rejects the freeze reading by a gap >10 at n=6.

## Prior Art

Not applicable (rejection of a route).

## Novelty Analysis

None.

## Falsification Attempts

Tried the inheritance reading; multi-scale resistance grows linearly and already exceeds 16 at level 6.

## Experimental Validation

None.

## Mathematical Status

Correct as a negative result.

## Patent Relevance

None.

## Related Discoveries

- DISC-0063. Mathematical. Theorem W.
- DISC-0051 / DISC-0052. Finest-only resistance freeze and its fractional Kept Failure S.1.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Whether combinatorial ‖F(n, 0.45)‖ → 0 or a positive finite L (OPEN). Fractional calculus on the multi-scale graph not covered.

## Next Experiments

None from the archive.

## Reproduction Instructions

As DISC-0063.

## Evidence Log

- 2026-10-09. Recorded from GASKET.md Kept Failure W.1 at 92b869ede53c77d04e923e4cf9be4537572bbb67.

## Change History

- 2026-10-09. Initial archive entry.
