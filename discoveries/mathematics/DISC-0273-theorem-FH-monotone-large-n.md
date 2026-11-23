# Discovery: Theorem FH, monotonicity in n for every n ≥ 11: G_{n+1}(α) > G_n(α) for every real α ∈ [−1, 1)

## Discovery ID
DISC-0273

## Status
THEOREM (mathematical sense only) for FH.1–FH.4 (analytic bounds plus Arb certificates; real α ∈ [−1, 1) only). FH.5 OBSERVED. Method KNOWN (two-sided asymptotic bounds L ≤ 3^n D_n ≤ U, cellwise Arb integration, the elementary inequality 3^n(G_{n+1} − G_n) = 3^n D_n − (1/3)·3^{n+1} D_{n+1}). Whether the constants are new is UNRESOLVED (no literature search). **Status change: DISC-0271 / DISC-0272 kept limit "monotonicity in n for n ≥ 11" OPEN → THEOREM.** No new kept failure; FF.2 (G_2 < G_1 on (−1, β_c)) stands.

## Date Discovered
2026-11-23. The commit is from 9:25 AM EST and was indexed at about 10:15 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 193d366ba0b33d3917b609371ee6a4eb4861b84c (2026-11-23T14:25:10Z = 2026-11-23 9:25:10 AM EST). Parent: 0a6f9431aee9 (Theorem FG, DISC-0272).

## Original Evidence
- GASKET.md §Theorem FH (+20 lines; also inline "closed by Theorem FH" notes added to FF's and FG's kept limits, original text kept).
- scripts/gasket_fractional_corner_h_alpha_monotone_large_n.py (new, 198 lines; python-flint arb 128 bits, tolerance 2^−30, exit 1 on any failure).
- CLAIM_STATUS.md (+1 row); tests/test_flux_identity.py (+14 lines, HAlphaMonotoneLargeNTests, floats only).

## Discovery
Notation of FB: D_n = W/2 − G_n = ∫ t^−α (f − f_n), G_{n+1} − G_n = D_n − D_{n+1}, M = max(1,t)^{log_5 2}.
- FH.1: for m ≥ 12 and α in a cell [a0, a1] ⊂ [−1, 1), 3^m D_m ≤ U = ½∫t^{1−a′} f R + (χ*/2) 5^−12 β_12 ∫t^{2−a′} f R M + ((3/5)^12/6) ∫t^{1−a′} f + τ_11^max, from f − f_n ≤ fE and 1/P_n ≤ 3R e^{Λ_n}. U → V(α) on point cells; U ≤ 306.99 on [−1, 1) (FB.2 had C ≤ 1095.75).
- FH.2: for n ≥ 11, 3^n D_n ≥ L (FB.4's lower bound with the exact M; δ_11 ≤ 0.0014352, E_up ≤ 0.0029508).
- FH.3 (Arb, 40 cells of width 1/20): L > U/3 on every cell, so 3^n(G_{n+1} − G_n) ≥ L − U/3 ≥ 0.048434 > 0 for every n ≥ 11 (margins 36.566 on [−1, −0.95], 0.8710 on [0, 0.05], minimum 0.0484337 on [0.95, 1]).
- FH.4: with FF.1 (2 ≤ n ≤ 10) and FG.4 (n = 1), G_n is strictly increasing in n ≥ 2 for every real α ∈ [−1, 1), and in n ≥ 1 exactly when α > β_c; it increases to W/2. Two-sided L ≤ 3^n D_n ≤ U for n ≥ 12 (e.g. 3^n D_n(0) ∈ [1.766, 2.685]).
- FH.5 (OBSERVED): FB.5's floats respect the bounds for n ≥ 12 and violate U only below the threshold (α = 0, n = 6: 2.7010 > U), so m ≥ 12 is needed by the method.

## Why It Matters
It closes the last open range of the monotonicity-in-n question opened by FC.4 (DISC-0268): on real α ∈ [−1, 1) the sequence G_n is now proved monotone for all n ≥ 2, and for all n ≥ 1 exactly on (β_c, 1). It also replaces FB's uniform rate constant 1095.75 with 306.99.

## Derivation
Checked here, not re-derived in full. The key step is elementary: 3^n(D_n − D_{n+1}) = 3^n D_n − (1/3)·3^{n+1} D_{n+1} ≥ L − U/3, valid when L bounds level n ≥ 11 from below and U bounds level n+1 ≥ 12 from above. FH.1's chain (f_n/f = e^Δ/(1+E) ≥ 1 − E; e^{Λ_n} ≤ 1 + χ*Λ_n on t ≤ 3^n; Λ_n ≤ 5^−n t β_n M; tail τ_n beyond 3^n; 5^−m β_m and (3/5)^m decreasing) was read and is consistent. The cell rule (a′ = a1 on t < 1, a0 on t > 1) gives the sup of t^{1−α} over the cell, so cellwise bounds are valid for every α in the cell.

## Assumptions
As stated by the repository: FB's list (FB.1 split and 0 ≤ log(P/P_n) ≤ Δ ≤ Λ_n; FB.2's sup_{n≥9} Λ_n(3^n) ≤ 0.2374, χ*, tail τ_n; FB.4's lower routine; EV.1/EV.2 ball evaluator); EX.3's high-tail bound as used in FB's W routine; FF.1; FG.4. Inherits the conditional chain of earlier gasket theorems (BG.3, BI.4). Rigour of python-flint 0.9.0's integrator assumed (textbook tool). Real α only.

## New Results
Strict monotonicity of G_n in n for all n ≥ 2 on real α ∈ [−1, 1); a uniform two-sided bracket L ≤ 3^n D_n ≤ U for n ≥ 12 with U ≤ 306.99.

## Prior Art
Two-sided asymptotic bounds plus interval-arithmetic certification are standard. No literature search on these specific constants.

## Novelty Analysis
Method KNOWN. Constants specific to this construction; novelty UNRESOLVED.

## Falsification Attempts
- Repository script rerun on the box at 193d366ba0b3: EXIT 0, 110.6 s elapsed (1m51s wall, box load ~45), 'all FH checks passed', worst margin min_cells (L − U/3) ≥ 0.0484337 on [0.95, 1], matching the commit.
- Repository CI test HAlphaMonotoneLargeNTests: 1 passed (1.51 s).
- Independent of repository code: /workspace/corpus-discovery/fh_check.py (mpmath 30 digits, the DISC-0271 ff_check.py evaluator of f and f_n, direct quadrature of D_n and D_{n+1}):
  - α = −1, n = 11: 3^11 D_11 = 304.5735 (≥ L 138.896 ✓), 3^12 D_12 = 304.7255 (≤ U 306.989 ✓), 3^11(G_12 − G_11) = 202.998 > 0.
  - α = 0, n = 11 / 12: 3^n D_n = 2.676062, 2.674393, 3^13 D_13 = 2.673374 (all ≤ U 2.684920 on [0, 0.05], ≥ 1.766 ✓; matches FH.5's 2.67439 at n = 12); 3^n ΔG = 1.7846, 1.7833.
  - α = 0.9, n = 11: 3^n ΔG = 0.07695; α = 0.99, n = 11: 3^11 D_11 = 0.091120, 3^12 D_12 = 0.091021 (inside the certified [0.0822, 0.1013] on [0.95, 1] ✓), 3^n ΔG = 0.06078 ≥ 0.048434 ✓.
  - α = 0.975, n = 13: 3^n ΔG = 0.06301 ✓; α = −0.5, n = 15: 3^n ΔG = 16.593 ✓.
  - **Held** at every point; no counterexample.
- Logic: checked the L − U/3 step, the n = 11 / m = 12 indexing, and that FH.4 composes FF.1, FG.4 and FH.3 without a gap at n = 10 → 11 (FF.1 covers 2 ≤ n ≤ 10, i.e. G_11 > G_10; FH.3 covers n ≥ 11). No contradiction between commit message, GASKET.md, CLAIM_STATUS.md and the test.

## Experimental Validation
Not applicable (pure mathematics). Functions on a graph, not a flux, not thrust; the repo's Stage 2 remains blocked.

## Mathematical Status
THEOREM (FH.1–FH.4); OBSERVED (FH.5); OPEN (α < −1, non-real α, closed form of V and of the next-order term; U − L does not shrink with n).

## Patent Relevance
None.

## Related Discoveries
- DISC-0271 (Theorem FF): kept limit "n ≥ 11 OPEN" → THEOREM; FF.1 used in FH.4. Label: mathematical.
- DISC-0272 (Theorem FG): kept limit "n ≥ 11 OPEN" → THEOREM; FG.4 used in FH.4. Label: mathematical.
- DISC-0267 (Theorem FB): FB.2 constant 1095.75 sharpened to 306.99; FB.4 lower bound reused. Label: mathematical.
- DISC-0268 (Theorem FC): FC.4 monotone-in-n question now settled on all n ≥ 2. Label: mathematical.

## Open Questions
α < −1 and non-real α; a lower bound whose gap to U shrinks with n; closed form of V(α).

## Next Experiments
Extend the cell certificate below α = −1 (needs a different tail than t^−a ≤ t); a complex-α version.

## Reproduction Instructions
`python3 scripts/gasket_fractional_corner_h_alpha_monotone_large_n.py` at informational-flux-identity 193d366ba0b3 (~2–14 min, python-flint 0.9.0, FH_JOBS workers). Independent: `python3 fh_check.py <alpha> <n>` (mpmath).

## Evidence Log
- 2026-11-23 ~10:15 AM EST: commit read; logic checked; CI test passed; repo script rerun EXIT 0 (110.6 s); independent mpmath checks held at 7 (α, n) points.

## Change History
- 2026-11-23 ~10:15 AM EST: created.
