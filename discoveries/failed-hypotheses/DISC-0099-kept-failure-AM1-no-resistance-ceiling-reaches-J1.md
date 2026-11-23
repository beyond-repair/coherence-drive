# Discovery: The boundary-cycle ceiling (or any resistance ceiling) combined with AK's share floor reaches Conjecture J.1's 0.70 (Kept Failure AM.1)

## Discovery ID

DISC-0099

## Status

REJECTED

## Date Discovered

2026-10-15 (America/New_York). Same archive pass as DISC-0098.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 0a11b759297d446a05f203ae18aea505e6fa4e86. Paths: GASKET.md Theorem AM → Kept Failure AM.1, NOT THIS; Conjecture J.1 evidence paragraph; CLAIM_STATUS.md (boundary-cycle row); scripts/gasket_fractional_cycle_ceiling.py (section 7).

## Original Evidence

GASKET.md Kept Failure AM.1: the claim "replacing the path by the boundary cycle and combining with Theorem AK's share floor yields ‖F(n,0.45)‖≥0.70" is false. The chain gives σ_AK·0.209685≈0.147106. Even the absolute one-step envelope 2^(1−α)·0.209685≈0.3070, or the live share σ_n≈1.3525 times the new floor (≈0.2836), stays below 0.70. Stronger: with the exact live energy in place of any ceiling, σ_AK‖F_frac(n)‖_live≈0.598008, 0.534474, 0.495867, 0.471857, 0.456527 on levels 2–6 and ≈0.4355, 0.4325 from the recorded level-9/10 energies, all below 0.70; the route needs a share floor near the live σ_n≈1.35, not a better resistance ceiling. The cycle is still lossy (R^cyc_∞≈7.28 > 3× live R_α≈2.35).

## Discovery

Rejected hypothesis family: the energy-floor×σ_AK chain (any resistance ceiling, including the boundary cycle of DISC-0098 and the path of DISC-0097) proves Conjecture J.1's 0.70. False. This subsumes DISC-0097's narrower rejection.

## Why It Matters

Locates the obstruction to J.1 in the share floor σ_AK (≈0.70 vs live ≈1.35), not in the resistance comparison, so further ceiling sharpenings cannot close DISC-0034 along this chain. DISC-0034 stays OPEN. Not thrust.

## Derivation

Any ceiling-derived floor on ‖F_frac(n)‖ is at most the live value, so the chain's bound at level n is at most σ_AK·‖F_frac(n)‖_live. A uniform bound ≥0.70 is therefore refuted by a single level with σ_AK·‖F_frac(n)‖_live<0.70; level 2 already gives 0.598008 (level 1 gives 0.703531, consistent with "from level 2 on"). Checked; no gap.

## Assumptions

As DISC-0098.

## New Results

Repo witness (`/workspace/scratch-ifi/repo_theorem_AM.log`, EXIT 0, 164 PASS) and independent archive (`/workspace/scratch-ifi/indep_theorem_AM.py` / `indep_theorem_AM.log`, ALL PASS, 156 PASS) reproduce σ_AK·0.209685≈0.147106, 2^(1−α)·0.209685≈0.306997, live-σ·0.209685≈0.283599, all <0.70; live σ_AK·‖F_frac‖ on L2–6 match the recorded values to ≤2e-6 and decrease; recorded-energy values 0.435436, 0.432425; at level 6 a share floor ≥≈1.0757 would be needed (σ_AK≈0.7016); R^cyc_∞=7.2849 > 3×live R(L6)=2.3474.

## Prior Art

Not applicable.

## Novelty Analysis

Not applicable (rejection of a route).

## Falsification Attempts

Recomputed envelopes and the live chain independently with own builder; matches GASKET.md and the commit message. The rejection of a uniform ≥0.70 bound from this chain is rigorous (one computed level suffices); the "decreasing" trend of the live chain is an observation on L2–6 only.

## Experimental Validation

None.

## Mathematical Status

Rejected as a sufficient route to L≥0.70. DISC-0098 still supplies the positive floor. DISC-0034 stays CONJECTURE.

## Patent Relevance

None.

## Related Discoveries

- DISC-0098. Mathematical. Theorem AM.
- DISC-0097. Failed hypothesis. Path-ceiling route; subsumed here.
- DISC-0095, DISC-0093, DISC-0091, DISC-0089, DISC-0033. Failed hypotheses. Earlier rejected routes toward the α=0.45 limit / floor.
- DISC-0034. Conjecture. Convergence and L≥0.70 still OPEN.

## Open Questions

Whether a share floor near the live σ_n≈1.35 can be proved; not addressed by the repository.

## Next Experiments

None.

## Reproduction Instructions

Same as DISC-0098.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Kept Failure AM.1 at 0a11b759297d446a05f203ae18aea505e6fa4e86; repo and archive indep confirm rejection.

## Change History

- 2026-10-15. Initial archive entry.
