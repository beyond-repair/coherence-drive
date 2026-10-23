# Discovery: Conjecture BG.2, uniform convergence and continuity of the fractional extension above γ

## Discovery ID

DISC-0148

## Status

THEOREM in the mathematical sense only (proved by IFI GASKET Theorem BI at 2e4d0d4ffe30a99ea0154e1aaa8b95069927b162; constants computer-assisted, see DISC-0151). Previously CONJECTURE (repository's own). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:55pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 073ace5091ac17b2adcd2eb956ef8f0bf0a14bce, GASKET.md "Conjecture BG.2".

## Original Evidence

"For α > γ, u_n → u_∞ uniformly on V_*, and u_∞ extends continuously to the gasket with u_∞ = d on C." Evidence cited: BG.5 (corner-neighbour mean → u_a = 1 above γ) and the non-flat V_1 limit at 0.8. Closed forms for W, U, κ_α, P_m open.

## Discovery

Open problem: regularity of the supercritical limit.

## Why It Matters

Would give the first continuous limit function of the corpus's fractional Dirichlet problem.

## Derivation

None; conjecture.

## Assumptions

As DISC-0146.

## New Results

None yet.

## Prior Art

Continuity of harmonic functions for Dirichlet forms whose order exceeds d_s/2 (points non-polar, resistance-form regime) is KNOWN in the continuum; the discrete uniform statement here is not proved.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

None beyond the repository's evidence; the archive checked only V_1–V_3 bounds and the m_ab limit (DISC-0146).

## Experimental Validation

Computational only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0146 → DISC-0148 (mathematical).

## Open Questions

Modulus of continuity; continuum equation for u_∞.

## Next Experiments

Dense sup-norm differences u_{n+1} − u_n on V_n at α = 0.8 for n ≤ 7.

## Reproduction Instructions

As DISC-0146.

## Evidence Log

- 2026-10-22. Recorded from the repository.

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-22 ~11:56pm EDT. Status CONJECTURE → THEOREM. IFI commit 2e4d0d4ffe30a99ea0154e1aaa8b95069927b162 (GASKET.md Theorem BI, CLAIM_STATUS.md new row, scripts/gasket_fractional_uniform_limit.py) proves uniform convergence u_n→ū and continuity of ū with ū=d on C for α>γ, via a cell-oscillation bound ≤‖x‖K_αρ^−N uniform in n (K_0.8≤47.109, certified). Repo witness EXIT 0 (25 ok, 382 s). Archive /workspace/scratch-ifi/indep_theorem_BI.py 24/24 PASS (own graph: ω-recursion, max principle, R_n≥1/(3+τ), orbit lemma, float sup g≈0.60096). Original conjecture text above kept unchanged. See DISC-0151.
