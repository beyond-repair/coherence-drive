# Discovery: Conjecture BS.4, the renormalised depth gap χ_N=(c_∞−ρ^N C_N)/ρ^N strictly decreases in N for every α∈(0,γ)

## Discovery ID

DISC-0169

## Status

CONJECTURE (repository's own; certified only for N=1–5 at α=0.45, floats otherwise). Do not cite as a theorem. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~3:57pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 316ee92917b18b6c95346b02c2e1fd7f7bb05dac, GASKET.md Theorem BS item 4 (line 2831), CLAIM_STATUS.md row 75, scripts/gasket_fractional_deficit_correction.py (check "A_N + B_N certified strictly decreasing for N = 1..5").

## Original Evidence

BS.3: at α=0.45 the arb enclosures of A_N+B_N (common D_∞) are strictly ordered for N=1..5; N=5 vs 6 not separated at the script's resolution. Repository floats: χ_N−χ_∞(0.45)≈0.0515, 0.0088, 0.0017 (N=1–3), scratch 0.00034 (N=4).

## Discovery

For every α∈(0,γ), χ_N=(A_N+B_N)/D_∞ strictly decreases in N, so ρ^N C_N approaches c_∞ from below with a monotone renormalised gap.

## Why It Matters

Would make the depth approach of DISC-0168 monotone, the depth analogue of the (failed) level monotonicity of V^(n) (DISC-0166).

## Derivation

None; certified for five values at one α and floats. B_N decreases (proved, B_(N+1)≤(3/5)B_N) but A_N increases, so the sign of the increment is not settled by DISC-0168.

## Assumptions

As DISC-0168.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED; repository's own conjecture.

## Falsification Attempts

Archive independent float model (/workspace/scratch-ifi/bs_floats.py via indep_theorem_BS.py; own route r_∞=1/(s+2(1−η)), no ⟨Θ⟩ approximation): χ_N strictly decreasing for N=1–6 at α=0.01, 0.1, 0.3, 0.45; gaps χ_N−χ_∞ = 0.00694…1.6e−6 (0.01), 0.0524…1.25e−5 (0.1), 0.074…1.88e−5 (0.3), 0.0515, 0.00884, 0.00172, 0.000342, 6.84e−5, 1.37e−5 (0.45); successive ratios →5.00 at every α tested (5.82, 5.14, 5.03, 5.005, 5.001 at 0.45), while B_(N+1)/B_N→0.600 — so the (3/5)^N parts of J−A_N and B_N appear to cancel, leaving ≈5^−N. No counterexample found. Floats only.

## Experimental Validation

Computational only (floats; five certified values at α=0.45).

## Mathematical Status

Conjecture.

## Patent Relevance

None. Not thrust.

## Related Discoveries

DISC-0168 → DISC-0169 (mathematical). DISC-0166 (related: the level-direction analogue V^(n) is not monotone).

## Open Questions

Proof for every N and α; whether χ_N−χ_∞ ∼ κ(α)5^−N (archive floats).

## Next Experiments

Tighten D_∞ or compare A_N+B_N directly to separate N=5/6; certify at α=0.01, 0.1, 0.3; analyse the cancellation between J−A_N and B_N at order (3/5)^N.

## Reproduction Instructions

As DISC-0168; archive python3 /workspace/scratch-ifi/indep_theorem_BS.py prints the float gaps and ratios.

## Evidence Log

- 2026-10-23 ~3:57pm EDT. Indexed; archive floats consistent at four α.

## Change History

- 2026-10-23. Initial archive entry.
