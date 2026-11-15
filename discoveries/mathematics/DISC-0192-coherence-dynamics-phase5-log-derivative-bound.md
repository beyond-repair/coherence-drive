# Discovery: Phase 5 finite-scale bound −2 < I(k) < 0 for positive spectral densities (coherence-dynamics)

## Discovery ID
DISC-0192

## Status
THEOREM (mathematical sense only; the repository contains a correct elementary proof, checked here). Method and result KNOWN: with z = k², Σ is a Stieltjes function of z, z·Σ(z) is a complete Bernstein function, and d ln Σ / d ln z ∈ [−1, 0] is classical (Schilling–Song–Vondraček, *Bernstein Functions*, ch. 6–7). The repo's I = d ln Σ / d ln k = 2·d ln Σ / d ln z, so the bound is that classical fact restated. Not a novelty candidate, not a patent candidate, no physical claim (the repo says the same).

## Date Discovered
2026-10-29 (~10:57pm EDT slice; first read of this repository by the corpus pass)

## Source Repositories
beyond-repair/coherence-dynamics, branch main, commit ca90e0a177864d6147d1903b203069cb87569f1d (tip; Phase 5 content from b5e687323072 / 6cbb0e4a85c8 / 44dc05186163, 2026-10-28).

## Original Evidence
- results/reports/phase5_robustness.md, section "Structural inequality from positivity" and "Verdict".
- research_log/falsification_ledger.md, "Established results", Phase 5 bullet.
- models/phase5_robustness.py, tests/test_phase5.py.

## Discovery
For ρ(s) ≥ 0 not identically zero and k > 0, Σ(k) = ∫ρ(s)/(k²+s) ds > 0 and −2 < I(k) ≤ 0, with I + 2 = 2∫ρ s/(k²+s)² ds / Σ.

## Why It Matters
It is the only finite-k constraint in the repository and is what survives after every universality candidate failed.

## Derivation
k dΣ/dk = −2k²∫ρ/(k²+s)² ds < 0, and 2Σ + k dΣ/dk = 2∫ρ s/(k²+s)² ds ≥ 0, equality iff ρ is supported at s = 0. Both lines check.

## Assumptions
ρ ≥ 0, nontrivial; k > 0; **Σ(k) finite**, i.e. ∫ρ/(1+s) ds < ∞ (not stated in the report; e.g. ρ ≡ 1 gives Σ = ∞). Differentiation under the integral then holds by dominated convergence.

## New Results (from this pass)
1. The upper bound is strict: I(k) < 0 for every nontrivial ρ (report writes ≤ 0).
2. The lower bound −2 is attained at finite k only for ρ = c·δ(s) (report states this).
3. The missing hypothesis is Σ finite, as above.

## Prior Art
Stieltjes functions / complete Bernstein functions (Schilling–Song–Vondraček 2012); Källén–Lehmann positivity of spectral functions in QFT. Not searched further.

## Novelty Analysis
None claimed; the repo itself labels it a model-class theorem with no physical interpretation. KNOWN.

## Falsification Attempts
Independent mpmath check (scripts/indep_coherence_dynamics_stieltjes.py): exponential, compact, s²e^{−s}, (1+s)^{−1/2} densities at k ∈ {0.3, 1, 3, 10}, all in (−2, 0). Signed density 3e^{−3s} − 0.9e^{−s} gives I(1) = −2.228, confirming the report's statement that the bound fails for signed measures. ALL PASS.

## Experimental Validation
None applicable. Repo CI (GitHub Actions pytest) green at ca90e0a177864d6147d1903b203069cb87569f1d; local pinned install failed on this box's Python, so repo tests were not re-run here.

## Mathematical Status
Theorem (elementary, KNOWN).

## Patent Relevance
None.

## Related Discoveries
DISC-0193 (finite-moment asymptotics in the same repo). Historical link only to the Ware-constant line (W ≈ 0.08), which this repo explicitly does not use.

## Open Questions
Whether a tighter bound follows from support or moment constraints (e.g. ρ supported on [m², ∞) gives I ≤ −2k²/(k²+m²)·… type bounds); the repo lists none.

## Next Experiments
None needed for the theorem.

## Reproduction Instructions
`python3 discoveries/mathematics/scripts/indep_coherence_dynamics_stieltjes.py` (needs mpmath); prints ALL PASS.

## Evidence Log
- 2026-10-29 ~10:57pm EDT: read report, checked proof by hand, ran independent script, ALL PASS.

## Change History
- 2026-10-29: created.
