# Discovery: Finite-moment and regular-variation asymptotics of Σ(k), with the J(∞) constant pinned (coherence-dynamics)

## Discovery ID
DISC-0193

## Status
KNOWN (Phase 4A/4B results are standard Stieltjes-transform asymptotics, Abelian theorem / Karamata regular variation). This pass adds one DERIVATIVE correction: J(∞) = 2·M1/M0 exactly, where the repo writes "M1/M0 (up to a conventional factor of order 1)". The repo's universality candidates (I, J as universal constants) are already FAILED in its own ledger; recorded here as REJECTED. Not a patent candidate.

## Date Discovered
2026-10-29 (~10:57pm EDT slice)

## Source Repositories
beyond-repair/coherence-dynamics, main, commit ca90e0a177864d6147d1903b203069cb87569f1d.

## Original Evidence
- theory/derivations/finite_moment_theorem.md §1–4 (Phase 4A).
- theory/derivations/phase4b_regular_variation.md (Phase 4B closure, borderline example ρ = 1/(1+s)).
- research_log/falsification_ledger.md "Rejected candidates".

## Discovery
If M0 = ∫ρ < ∞ then k²Σ → M0 and I → −2 (dominated convergence). For ρ ~ s^{−α}L(s), 0<α<1, I → −2α. Borderline ρ = 1/(1+s): Σ = ln(1+x)/x (x = k²), I = −2 + 2x/((1+x)ln(1+x)), J → ∞. All checked.

## Derivation (new constant)
From DISC-0192, I + 2 = 2∫ρ s/(k²+s)² / Σ. With M0, M1 finite, k⁴∫ρ s/(k²+s)² → M1 and k²Σ → M0, so J = k²(I+2) → 2·M1/M0. The factor 2 is definite under the repo's own definitions of I and J; it is not a convention.

## Assumptions
ρ ≥ 0; M0, M1 finite for the J limit; regular-variation conditions as stated in phase4b for α ∈ (0,1).

## Prior Art
Abelian/Tauberian theorems for Stieltjes transforms (Widder; Bingham–Goldie–Teugels, *Regular Variation*, §1.7).

## Falsification Attempts
Independent script: J at k = 300 equals 1.99993 for e^{−s} (2M1/M0 = 2) and 5.99967 for s²e^{−s} (= 6); I(10⁴) = −0.99994 for (1+s)^{−1/2} (−2α = −1). ALL PASS. Phase 4A table's ρ ~ 1/s rate −2 + 1/ln k agrees with the 4B exact formula.

## Mathematical Status
Known theorems; J(∞) constant derived here.

## Patent Relevance
None.

## Related Discoveries
DISC-0192.

## Open Questions
Repo's own follow-ups: α = 1 rates with general slowly varying L; higher normalized corrections; finite-graph moment ratios.

## Next Experiments
Suggest the repo replace "up to a conventional factor" with 2·M1/M0 in finite_moment_theorem.md §3 and the falsification ledger (suggestion only; this pass does not edit that repo).

## Reproduction Instructions
Same script as DISC-0192.

## Evidence Log
- 2026-10-29 ~10:57pm EDT: read, derived, checked.

## Change History
- 2026-10-29: created.
