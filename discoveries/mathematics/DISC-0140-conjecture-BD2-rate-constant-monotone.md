# Discovery: Conjecture BD.2, c(α) decreases on (0,1) with c(1^−)=2 and c(0^+)=∞

## Discovery ID

DISC-0140

## Status

Decided in part by IFI Theorem BE at 3b3ec0f (DISC-0141): the monotone part (c(α) strictly decreasing on (0,1)) and c(1^−)=2 are THEOREM (with (c−2)/(1−α)→3S, 3S∈[2.70632481,2.70903118] certified); the c(0^+)=∞ part is REJECTED (c(0^+) finite, certified in [5.48553067,5.50249013]; Kept Failure BE.1, DISC-0142). Ledger status column THEOREM refers to the surviving parts only. Originally CONJECTURE (repository's own Conjecture BD.2); history below. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~6:05pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 30bee3aab038a818c28144ef7d9787eaccdedf5a, README.md "CONJECTURE BD.2", CLAIM_STATUS.md Theorem BD row ("Monotonicity of c(α) and closed forms OPEN").

## Original Evidence

README: c(α) decreases, c(1^−)=2 (weight τ^−α concentrates at τ=0 where T=2), c(0^+)=∞ (B_α diverges like 1/α). Only three float values support it; no closed form for T, 𝒴 or c.

## Discovery

Monotone decreasing rate constant with the stated endpoint behaviour.

## Why It Matters

Would complete the description of the non-centrality approach rate.

## Derivation

None (conjecture); heuristic endpoint arguments in the README. Note the c(0^+)=∞ argument uses only that the upper bound B_α diverges, which does not by itself force c to diverge.

## Assumptions

As DISC-0138.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive floats at n=7 order the three tested α consistently (0.45 above 0.8); repository floats c(0.25)≈4.472>c(0.45)≈3.726>c(0.8)≈2.572. No counterexample; three points cannot test monotonicity.

## Experimental Validation

Floats only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

- DISC-0138 → DISC-0140 (mathematical).

## Open Questions

Closed form of T(τ), 𝒴(τ), c(α); proof of monotonicity.

## Next Experiments

Dense α scan of c(α) with the repository's interval pipeline; α near 0 and 1.

## Reproduction Instructions

As DISC-0138.

## Evidence Log

- 2026-10-22 ~6:05pm EDT. Recorded from IFI 30bee3aab038a818c28144ef7d9787eaccdedf5a.
- 2026-10-22 ~7:15pm EDT. IFI 3b3ec0fef920 Theorem BE (DISC-0141) proves the decrease (tilt identity, BE.1–BE.2) and c(1^−)=2 (BE.3), and refutes c(0^+)=∞ (BE.4, Kept Failure BE.1, DISC-0142). The Derivation note above (the c(0^+)=∞ heuristic only used divergence of the bound B_α) is what BE.1 confirms. Archive /workspace/scratch-ifi/indep_theorem_BE.py 30/30 PASS: 3^n d_n(α) at n=24 strictly decreasing on 12 α in [0,0.99], c(0)≈5.494003 finite and inside the certified bracket, c(0.99)−2≈0.0272.

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22 ~7:15pm EDT. Status CONJECTURE → THEOREM for the monotone part and c(1^−)=2; the c(0^+)=∞ part REJECTED (DISC-0142), after IFI 3b3ec0fef920 (Theorem BE, DISC-0141). Earlier text preserved (Mathematical Status section below reflects the original entry).
