# Discovery: Theorem BM, the ρ^−n rate is attained at every α∈(γ,1) for all large N

## Discovery ID

DISC-0160

## Status

THEOREM in the mathematical sense only (repository proof; BM.1 qualitative for every α∈(log3/log5,1), BM.2 thresholds computer-assisted with python-flint arb). Method KNOWN; constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~6:53am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit c9ca93479dbee307e77705a052d995029938a630.

## Original Evidence

GASKET.md Theorem BM (BM.1, BM.2, "What stays open"), CLAIM_STATUS.md row, README.md OPEN bullet, scripts/gasket_fractional_rate_sharpness_alpha.py (new, 167 lines), scripts/cli.py, tests/test_cli.py, all at c9ca93479dbee307e77705a052d995029938a630. Builds on Theorem BL at dfc145a9833f96b8960667c572aca38d48adfc17 and Theorem BK at 00d0d28b71db264b070be23c73f8e3f67de704db.

## Discovery

BM.1 (qualitative, every α∈(γ,1), every y₀>0): BL.2–BL.4 are stated for every α in (γ,1), and their inputs are finite and positive there. L(y₀)>0 because ω_lo=(1+y/5)^α/B with B=1−y(y+4)/(3(y+2)(y+5))∈(0,1) for y>0; J(y₀)≤J_α<∞ (BK.4); Q<∞ (head K_S t^−α integrable since α<1, tail t^(γ−1−α) integrable since α>γ); I₀<∞; D'_N≥D'_0>0; and the j=0 term of BL.1's positive series gives g_N=1−η_N(p(y₀))≥p(y₀)/(p(y₀)+2)>0 for every N≥1. BL.4(ii)'s N-uniform ceiling (GQρ^−N+(3/2)(3/5)^N I₀)/D'_0 tends to 0, so BL.2's bracket is positive for all N≥N₀(α). Hence for every N≥N₀(α) and n≥N, δ_N^(n) strictly increases in n and c_Nρ^−n ≤ δ_N−δ_N^(n) ≤ (3/2)J_α/((1−ρ^−1)D'_0)·ρ^−n, with liminf_N c_N>0. BK.4's order ρ^−n is exact at every α above γ (for large N).

BM.2 (certified thresholds): N₀=61, 16, 7, 6, 5 at α=0.7, 0.75, 0.85, 0.9, 0.95 (with BL's N₀=9 at 0.8); upper coefficients ≤40.6260, 9.4106, 2.6545, 1.4794, 0.6559. N₀→∞ as α→γ in this method because ρ→1; the repository calls this a method limit, not evidence against sharpness.

## Why It Matters

Removes the α=0.8 restriction of DISC-0157: the uniform-convergence rate of the L^α Dirichlet extension on the gasket is exactly ρ^−n at the corner neighbours for every exponent above log3/log5, not only at one certified exponent.

## Derivation

GASKET.md Proof of BM.1 and BM.2 (repository). Independently re-checked this slice: B's numerator 3(y+2)(y+5)−y(y+4)=2y²+17y+30>0 (sympy), so 0<B<1 for y>0; ω_lo>1 on a grid for α∈{0.69,…,0.999}; the j=0 floor 1−η_N(p(y₀))≥p(y₀)/(p(y₀)+2) for N=1..59 at y₀=1/10 and 1/50; the integrability exponents of Q; and liminf c_N at α=0.7 recomputed from the printed L, D'_∞ and the N→∞ value of 1−η_N(0.51).

## Assumptions

BL.2–BL.4, BK.1–BK.4, BI.1/BI.4 as stated in the repository; the arb enclosures in the script (re-run by the repository witness, not re-certified in this archive). BM.1 is pointwise in α: no certificate covers an α-interval and N₀(α) has no explicit formula.

## New Results

Two-sided ρ^−n rate for the corner deficit at every α∈(γ,1) and N≥N₀(α); certified N₀ at five further exponents. Not covered: N<N₀(α) (N=1..60 at 0.7, 1..8 at 0.8, …), uniformity in α, the limit C_δ (DISC-0159).

## Prior Art

Same as DISC-0157: decimation and resolvent-integral representations of fractional powers on p.c.f. fractals, covariance lower bounds under a change of measure. The extension from one exponent to all exponents by a limiting argument is routine. Constants not searched.

## Novelty Analysis

Method KNOWN. Thresholds and constants are the repository's own; novelty UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Sympy and float re-checks of every BM.1 lemma: PASS (/workspace/scratch-ifi/indep_theorem_BM.py, 11/11). (2) Own gasket graph with spectral L^−α extension, levels ≤7, α=0.7, 0.75, 0.85, 0.9, 0.95: δ_N^(n) strictly increasing in n for N=1..6 (floats; below the certified N₀, consistency only): PASS. (3) Repository witness EXIT 0 in 71 s, every certified bracket positive. (4) Attack found two presentation errata, not proof gaps. First, the printed g≥0.584124 at y₀=1/10 repeats DISC-0157's erratum (value 0.5841236594…). Second, the stated liminf c_N≥0.1902 at α=0.7 is a %.4f round-to-nearest of an arb lower bound near 0.190187 (recomputed from the printed inputs: 0.5841236594×0.454305/(50.543638×(1−1/1.028390))=0.19019), so as a lower bound the decimal should read ≥0.1901. The same round-up affects α=0.85 (stated 0.0636, recomputed 0.063596) and α=0.9 (stated 0.0673, recomputed 0.067271); α=0.75 (0.155502) and α=0.95 (0.037133) are correctly rounded down. Only positivity of c_N is used, so the theorem is unaffected. (5) The qualitative argument was checked for a hidden N-dependence in J(y₀) and L(y₀): both are N-free, and g_N's floor is N-free, so the limit argument holds.

## Experimental Validation

Repository witness EXIT 0 (/workspace/scratch-ifi/repo_theorem_BM.log, 70.4 s). Repository floats at α=0.9, N=6: ρ^n(δ^(60)−δ^(n))=0.3277..0.3659..0.3643 at n=6..20, inside [c_6, 1.4794].

## Mathematical Status

Theorem (mathematical sense; BM.1 analytic given BL/BK, BM.2 computer-assisted).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0157 → DISC-0160 (mathematical: BL.2–BL.4 are the inputs). DISC-0155 → DISC-0160 (mathematical: BK.4's J_α and upper ceiling). DISC-0160 → DISC-0156 (mathematical: sharpness half now for every α∈(γ,1), N≥N₀(α)). DISC-0160 → DISC-0159 (experimental: floats ≈0.364 at α=0.9 vs ≈0.6025 at 0.8, so a limit C_δ, if it exists, depends on α).

## Open Questions

N<N₀(α); a certificate uniform over an α-interval or an explicit N₀(α); whether N₀(α)→∞ as α→γ is real or a method artefact; the limit C_δ(α) (DISC-0159); monotone ω_k.

## Next Experiments

Scan y₀ more finely at α=0.7 to lower N₀=61; try an interval-arithmetic certificate over α∈[0.75,0.95] with α as a ball.

## Reproduction Instructions

git -C informational-flux-identity checkout c9ca93479dbee307e77705a052d995029938a630; python3 scripts/gasket_fractional_rate_sharpness_alpha.py (≈70 s, needs python-flint and sympy). Archive check: python3 /workspace/scratch-ifi/indep_theorem_BM.py.

## Evidence Log

- 2026-10-23 ~6:53am EDT. Indexed; repo witness EXIT 0; independent sympy/float/graph checks 11/11 PASS; liminf rounding errata at α=0.7, 0.85, 0.9 recorded.

## Change History

- 2026-10-23. Initial archive entry.
