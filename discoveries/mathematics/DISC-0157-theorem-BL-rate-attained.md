# Discovery: Theorem BL, the ρ^−n rate of Theorem BK is attained at the corner neighbours (α=0.8, N≥9)

## Discovery ID

DISC-0157

## Status

THEOREM in the mathematical sense only (repository proof; constants computer-assisted at α=0.8 with python-flint arb). Method KNOWN; constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~4:54am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit dfc145a9833f96b8960667c572aca38d48adfc17.

## Original Evidence

GASKET.md Theorem BL (BL.1–BL.5), CLAIM_STATUS.md new row (PROVED), README.md OPEN bullet, scripts/gasket_fractional_rate_sharpness.py (new, 369 lines), scripts/cli.py, tests/test_cli.py::test_theorem_bl_rate_sharpness, all at dfc145a9833f96b8960667c572aca38d48adfc17. Builds on Theorem BK at 00d0d28b71db264b070be23c73f8e3f67de704db.

## Discovery

BL.1 (exact, every N≥1): 1−α₁−β=z/(z+2), so 1−η_N(z)=z/(z+2)+β(z)(1−η_(N−1)(p(z))), with every term of the unrolled sum ≥0. α₁ and β are positive and strictly decreasing (derivative numerators −(z²+8z+18) and −(z+4)(z+8)); η₁=1/(2(z+5)); so every η_N (N≥1) is positive and strictly decreasing, η_N(0)=1−(9/10)(3/5)^(N−1), and the deficit integrand G_k(τ)=1−η_N(p^(k−N)(5^−kτ)) increases in τ. BL.2: by BK.1 the one-level deficit increment is a covariance against ω_k−1≥0, δ^(k+1)−δ^(k)=⟨(ω_k−1)(G_k−⟨G_k⟩)⟩/⟨ω_k⟩ ≥ ρ^−k[(g−Δ)L(y₀)−ΔJ(y₀)]/D'_(k+1), with ω_k≥ω_lo=(1+y/5)^α/(1−y(y+4)/(3(y+2)(y+5))). BL.3: AZ-free floor D'_N≥D'_0+L(0)(1−ρ^−N)/(1−ρ^−1). BL.4: direct and N-uniform ceilings Δ_N on δ^(k). BL.5 (certified at α=0.8, y₀=1/10): the bracket is positive for N=9..13 (direct) and every N≥14 (uniform), so for every N≥9 and n≥N, δ_N^(n) strictly increases in n and c_Nρ^−n ≤ δ_N−δ_N^(n) ≤ 4.6644ρ^−n, with c_9≥2.095e−3, c_13≥6.960e−2, c_N≥5.653e−2 (N≥14), c_N≥0.1240 (N≥40). Hence sup_(V_n)|u_n−ū| ≥ c_9‖x‖ρ^−n for symmetric data, so BK's order ρ^−n is exact.

## Why It Matters

Closes the sharpness half of Conjecture BK.6 without the unproved monotonicity of ω_k that BK suggested: only the deficit integrand needs a sign. Together with DISC-0155 (upper bound) it pins the uniform-convergence rate of the L^α Dirichlet extension above log3/log5 at exactly ρ^−n (at α=0.8, N≥9).

## Derivation

In GASKET.md Theorem BL (repository). Independently re-derived this slice: the identity 1−α₁−β=z/(z+2), the derivative numerators, η₁, η_N(0) for N=1..5 and the recursion for N=1..3 (sympy, exact). The covariance step is BK.1 applied to G_k; the split at y₀ uses G_k≥g on y≥y₀ (monotonicity) and BK.4's ceiling below y₀.

## Assumptions

BK.1–BK.4 and BI.1/BI.4 as stated in the repository (re-run there); the arb enclosures in the script (not re-certified in this archive); AZ is not needed for the lower bound (AZ-free floor BL.3).

## New Results

Two-sided rate c_Nρ^−n ≤ δ_N−δ_N^(n) ≤ 4.6644ρ^−n at α=0.8 for every N≥9; monotone increase of the corner deficit in n. Not covered: N=1..8 at α=0.8, α≠0.8, existence of the limit ρ^n(δ_N−δ_N^(n)).

## Prior Art

Decimation and resolvent-integral representations of fractional powers on p.c.f. fractals and covariance (Chebyshev/Harris-type) lower bounds under a change of measure are standard. Constants not searched.

## Novelty Analysis

Method KNOWN. The specific two-sided constants are the repository's own; novelty UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Sympy identities re-derived independently: PASS. (2) η_N>0 and strictly decreasing on a 4001-point grid of [0,10^6], N=1..12 (floats): PASS. (3) Own gasket graph with spectral L^−0.8 extension, levels ≤7, two data vectors: δ_N^(n) strictly increasing in n for N=1..6 (floats, outside the theorem's N≥9 range, consistent): PASS. (4) Repository witness EXIT 0 in 215 s, 16 ok lines, bracket ≥3.290e−3 at N=9. (5) Attack found a presentation erratum, not a proof gap: GASKET.md BL.5 and the commit message state 1−η_N(p(1/10)) ≥ 0.584124 for every N≥9, but the value is 0.58412365942187402… (mpmath, 50 digits; identical for N=9..39), so the stated decimal is 3.4e−7 too high. The script uses the arb lower bound itself (the printed 0.584124 is a %.6f round-to-nearest of that lower bound), and the smallest bracket margin (3.290e−3 at N=9) is far larger than the effect (≈0.335×3.4e−7), so the theorem is unaffected. The text should read ≥0.584123.

## Experimental Validation

Repository witness EXIT 0 (/workspace/scratch-ifi/repo_theorem_BL.log, 215 s). Archive checks: /workspace/scratch-ifi/indep_theorem_BL.py (graph part, 4/4 PASS) and indep_theorem_BL_fix.py (sympy and grid part, 6/6 PASS after fixing two harness bugs in my own first draft: a misparenthesised N=1 recursion test and a float overflow at p^j(z)>10^120). The one remaining FAIL is the 0.584124 erratum above, confirmed at 50 digits.

## Mathematical Status

Theorem (mathematical sense; computer-assisted constants at α=0.8).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0155 → DISC-0157 (mathematical: BK.1 transfer and BK.4 ceiling are inputs). DISC-0157 → DISC-0156 (mathematical: proves the sharpness half at α=0.8, N≥9). DISC-0153 → DISC-0157 (mathematical: BJ.4's data-free deficit and η_N). DISC-0151 → DISC-0157 (mathematical: BI.1 orbit lemma, BI.4 ceiling). DISC-0157 → DISC-0158, DISC-0159.

## Open Questions

N=1..8 at α=0.8; other α∈(γ,1); whether ω_k is monotone in y (floats say yes at k=0..20, unproved); the limit constant (DISC-0159).

## Next Experiments

Run the script's bracket at y₀ other than 1/10 to try to reach N<9; repeat at α=0.75 and 0.9.

## Reproduction Instructions

git -C informational-flux-identity checkout dfc145a9833f96b8960667c572aca38d48adfc17; python3 scripts/gasket_fractional_rate_sharpness.py (≈3.5 min, needs python-flint). Archive check: python3 /workspace/scratch-ifi/indep_theorem_BL.py.

## Evidence Log

- 2026-10-23 ~4:54am EDT. Indexed; repo witness EXIT 0; independent sympy/graph checks PASS; 0.584124 presentation erratum recorded.

## Change History

- 2026-10-23. Initial archive entry.
