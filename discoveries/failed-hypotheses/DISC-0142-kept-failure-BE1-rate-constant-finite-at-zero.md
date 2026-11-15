# Discovery: Kept Failure BE.1, the 3^−n constant does not blow up at α→0^+ (Conjecture BD.2's c(0^+)=∞ is false)

## Discovery ID

DISC-0142

## Status

REJECTED (repository's own Kept Failure BE.1). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~7:15pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b3ec0fef920f85fa1098074e22ee3bdafe73a26, README.md "KEPT FAILURE BE.1", CLAIM_STATUS.md Theorem BE row, GASKET.md Stage 2 item, scripts/mesh_noncentrality_monotone.py.

## Original Evidence

README: BD.2 guessed c(0^+)=∞ because the proved bound B_α diverges like 1/α (αJ_α→3125). That divergence belongs to the bound: BD.3 dominates 𝒴 by (1+τ/25)^−1(1+τ/125)^−1, whose first moment diverges at α=0, while the true 𝒴≤τ/(3ψ(τ)) decays faster than any power. Witness: certified c(0^+)∈[5.48553067,5.50249013], above certified c(0.45) and a coarse certified c(0.25)∈[4.416733,4.537510].

## Discovery

The rejected hypothesis: c(α)→∞ as α→0^+.

## Why It Matters

Shows that the 1/α blow-up of an upper bound was read as behaviour of the quantity; c is bounded on (0,1) by c_0.

## Derivation

BE.4 (DISC-0141): dominated convergence plus the interval enclosure of ∫T𝒴/∫𝒴.

## Assumptions

As DISC-0141.

## New Results

None beyond DISC-0141.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection).

## Falsification Attempts

Archive floats (own Schur recursion, n=24): c(0)≈5.494003464 inside the certified bracket; c(0.02)≈5.40863317, c(0.05)≈5.28174783, secants −4.2685 and −4.2295 (smooth, no blow-up); n=20 vs 24 agree to 8.7e−9. Archive also confirms αJ_α→3125 (the bound does diverge). Archive run2's one FAIL was an archive tolerance error (assumed c(0)−c(0.02)<0.05; true gap 0.085), kept in indep_theorem_BE.run2.log.

## Experimental Validation

Repository certification; archive floats agree.

## Mathematical Status

Rejected hypothesis (finite value certified).

## Patent Relevance

None.

## Related Discoveries

- DISC-0141 → DISC-0142 (failed hypothesis).
- DISC-0142 → DISC-0140 (failed hypothesis): refutes the c(0^+)=∞ part of Conjecture BD.2.

## Open Questions

Closed form of c_0.

## Next Experiments

None needed for the rejection.

## Reproduction Instructions

As DISC-0141.

## Evidence Log

- 2026-10-22 ~7:15pm EDT. Recorded from IFI 3b3ec0fef920f85fa1098074e22ee3bdafe73a26; repository witness EXIT 0; archive indep_theorem_BE.py 30/30 PASS.

## Change History

- 2026-10-22. Initial archive entry.
