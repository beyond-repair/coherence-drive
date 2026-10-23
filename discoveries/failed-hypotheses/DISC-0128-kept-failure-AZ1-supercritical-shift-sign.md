# Discovery: Kept Failure AZ.1, the endpoint level shift does not carry over with its sign above γ

## Discovery ID

DISC-0128

## Status

REJECTED (hypothesis). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~12:53pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 5404c3be371c35f0f2c571e218351cb574386b83. Paths: GASKET.md "KEPT FAILURE AZ.1"; scripts/gasket_fractional_supercritical_shift.py.

## Original Evidence

Hypothesis rejected by the repository: "above γ, as at γ, C_α>0, so ρ^n‖F(n,α)‖ increases to K_α from below with an error O(5^(−0.65n)) or at least smaller than (3·5^(−α))^n". Certified C_0.8 ≤ −1.74325717839, ν_0.8 ≤ −0.72744538444; by Theorem AZ (4) ρ^n(ρ^n‖F‖−K) → −νK = 0.5003854985… > 0. Repository witness ρ^m‖F(m,0.8)‖−K = 0.27089, 0.084985, 0.011628, 0.0017328 at m=5,10,20,30.

## Discovery

Both parts of the hypothesis fail: the sign of the shift flips (C_α<0, approach from above), and the unshifted renormalization error is Θ((3·5^(−α))^n), the same order as the shift. The flip is structural: C_α continues R_∞(α) through a simple pole with positive residue, so C_α → −∞ as α↓γ.

## Why It Matters

Prevents carrying AY's sign and correction size across the critical exponent.

## Derivation

Immediate from DISC-0127 (2) and (4).

## Assumptions

Theorem AZ (DISC-0127).

## New Results

None beyond the repository.

## Prior Art

Not applicable (a rejected route).

## Novelty Analysis

Not applicable.

## Falsification Attempts

Archive /workspace/scratch-ifi/indep_theorem_AZ.py: ρ^m‖F‖−K = 0.27089173, 0.084984971, 0.011627588, 0.0017328259, 0.00026138446 at m=5,10,20,30,40 (positive, decreasing); ρ^m(ρ^m‖F‖−K) = 0.69674, 0.56220, 0.50884, 0.50165, 0.50058, equal to −νKρ^m/(ρ^m+ν) within the proved remainder (residuals −1.0e−5, −1.0e−9, −1.9e−13 at m=10,20,30). C_{γ+0.01}=−31.11 < 0. The rejection stands.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Counterexample to a stated hypothesis (via DISC-0127, certified constants).

## Patent Relevance

None.

## Related Discoveries

DISC-0127 → DISC-0128 (mathematical). Sits beside DISC-0126 (AY.1, unshifted endpoint norm) and DISC-0114/DISC-0117 (simplest-form guesses that fail).

## Open Questions

Whether C_α<0 on all of (γ,1) (DISC-0127 open item).

## Next Experiments

None beyond DISC-0127.

## Reproduction Instructions

As DISC-0127.

## Evidence Log

- 2026-10-22. See DISC-0127 evidence log.

## Change History

- 2026-10-22. Initial archive entry.
