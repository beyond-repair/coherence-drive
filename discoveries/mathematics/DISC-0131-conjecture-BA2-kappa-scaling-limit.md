# Discovery: Conjecture BA.2, 2^−n κ_n(0.45) has a nonzero limit

## Discovery ID

DISC-0131

## Status

THEOREM for every α<log3/log5 (proved by IFI Theorem BB at 3b98cd7, DISC-0132; limit K(0.45)∈[−0.854646905120924,−0.854646905120848], not ≈−0.86). Originally CONJECTURE (repository's own); history below. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~1:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit fe388f3b633ff0cafbfd653758afde0ab7284b93. Path: README.md "CONJECTURE BA.2".

## Original Evidence

Float 2^−nκ_n=−2.0214, −1.6535, −1.3423, −1.1579, −1.0488, −0.9818 (n=1..6); Aitken on float levels 5–7 gives about −0.86 (not certified). Mechanism offered: the corner jump u_{c0}−(u_p+u_r)/2 runs 0.942, 0.763, …, 0.564 (n=1..7), apparently to a positive limit, with q_{c0}>0, so g_c∼2^n. Falsified by a certified sequence tending to 0 or −∞.

## Discovery

A scaling law for the mesh residual of DISC-0129.

## Why It Matters

Quantifies DISC-0130 witness (iii): the residual diverges like 1/h.

## Derivation

None (numerical).

## Assumptions

Assumption BA.

## New Results

Archive floats agree at n=5,6 (−1.0487908, −0.9817914). Successive ratios of increments (−1.0488+1.1579)/(−1.1579+1.3423)=0.592, (−0.9818+1.0488)/(…)=0.614: consistent with geometric convergence but not proof.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable.

## Falsification Attempts

Only the float agreement above; level 7 not re-run in the archive.

## Experimental Validation

None.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0129 → DISC-0131 (mathematical); DISC-0130 (uses witness iii); DISC-0132 → DISC-0131 (mathematical, proof).

## Open Questions

Certified κ_5..κ_7; a proof of the corner-jump limit.

## Next Experiments

Interval-certify κ_5, κ_6 with the repository's Krylov pipeline.

## Reproduction Instructions

As DISC-0129.

## Evidence Log

- 2026-10-22 ~3:55pm EDT. Proved by Theorem BB at IFI 3b98cd7aa7c102a5b9c44cedeef3ed123c53f23d: lim 2^−nκ_n=−4σ_∞/R_∞², certified at 0.45; limit 0 for α≥γ. The original falsifier (certified sequence →0 or −∞) is not met for α<γ; it IS met for α≥γ (limit 0), which the original 0.45-only statement did not cover. The Aitken ≈−0.86 was 0.005 low.
- 2026-10-22. Archive floats n=5,6 match.

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22 ~3:55pm EDT. Status CONJECTURE → THEOREM after IFI 3b98cd7aa7c1 (Theorem BB, DISC-0132); repo witness EXIT 0, archive /workspace/scratch-ifi/indep_theorem_BB.py 64/64 PASS. Earlier text preserved.
