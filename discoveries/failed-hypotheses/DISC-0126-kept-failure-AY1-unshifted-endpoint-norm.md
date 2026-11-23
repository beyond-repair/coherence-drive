# Discovery: Kept Failure AY.1, the unshifted endpoint audit norm n‖F(n,γ)‖ does not converge exponentially

## Discovery ID

DISC-0126

## Status

REJECTED (hypothesis). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~11:53am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 8517f2bac0f79c5c76b1ef9d03517582bc8d06e2. Paths: GASKET.md "KEPT FAILURE AY.1"; scripts/gasket_fractional_endpoint_shift.py.

## Original Evidence

By Theorem AY (3) (DISC-0125), n‖F(n,γ)‖−K_γ = −ν_γK_γ/(n+ν_γ) + O(5^(−0.65n)) with ν_γK_γ ≥ 4.625400 certified. Repository witness: n‖F‖−K_γ = −0.728312, −0.407188, −0.216550, −0.147496 at n=5,10,20,30; n(n‖F‖−K_γ) = −4.4249 at n=30, matching −ν_γK_γ n/(n+ν_γ) to 1e−10.

## Discovery

The tempting endpoint analogue of the sub-critical law ‖F(n,α)‖−𝓛 = O(ρ^n), namely n‖F(n,γ)‖ = K_γ + O(θ^n) with θ<1, is false. The error is Θ(1/n); the renormalization that converges exponentially is n+ν_γ, ν_γ=1.3594681…

## Why It Matters

Pins down exactly which renormalization of the critical audit norm is exponentially accurate, and prevents extrapolating the 1/n law with an unshifted level.

## Derivation

Immediate from DISC-0125 (3): K/(n+ν) = K/n − νK/(n(n+ν)).

## Assumptions

Theorem AY (DISC-0125).

## New Results

None beyond the repository.

## Prior Art

Not applicable (a rejected route).

## Novelty Analysis

Not applicable.

## Falsification Attempts

Archive /workspace/scratch-ifi/indep_theorem_AY.py: m(m‖F‖−K) = −4.071881, −4.331008, −4.424885, −4.473366 at m=10,20,30,40, each equal to −νK·m/(m+ν) to <1e−3, moving toward −νK ≈ −4.6254. The rejection stands.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Counterexample to a stated hypothesis (proved via DISC-0125).

## Patent Relevance

None.

## Related Discoveries

DISC-0125 → DISC-0126 (mathematical). Sits beside DISC-0114 and DISC-0117 (earlier "simplest form" hypotheses at γ that failed).

## Open Questions

None specific.

## Next Experiments

None.

## Reproduction Instructions

As DISC-0125.

## Evidence Log

- 2026-10-22. See DISC-0125 evidence log.

## Change History

- 2026-10-22. Initial archive entry.
