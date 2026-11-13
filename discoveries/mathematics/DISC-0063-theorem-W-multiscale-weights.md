# Discovery: Multi-scale multiplicative gasket weights geometric-series trichotomy (Theorem W)

## Discovery ID

DISC-0063

## Status

DERIVATIVE

## Date Discovered

2026-10-09 (America/New_York). Archive pass after DISC-0061 / DISC-0062.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 92b869ede53c77d04e923e4cf9be4537572bbb67. Paths: GASKET.md "Theorem W. Multi-scale multiplicative weights: harmonic audit is a geometric series" (Assumption item 7, Theorem W, Proof, Kept Failure W.1, NOT THIS); scripts/gasket_multiscale_weights.py; CLAIM_STATUS.md (multi-scale multiplicative weights row VERIFIED); README.md gasket summary pointing at Theorem W.

## Original Evidence

Vertices are the level-n gasket points; edges are retained at every generation g=0..n with weight w=λ^g. Write L^(g) for the unit-weight Laplacian of generation-g edges alone, so L_ms = Σ_{g=0}^n λ^g L^(g). Let u be the combinatorial harmonic extension of Theorem G. Then nested harmonicity gives L^(g)u = 0 on the fine interior for each g, so u solves the multi-scale Dirichlet problem. Corner currents add by linearity: I_ms = Σ_g λ^g I^(g) with I^(g) = (3/5)^g I(0) from Theorem G, and

‖F_ms,λ(n)‖ = (√21/2) Σ_{k=0}^n (λ · 3/5)^k.

Trichotomy (r = λ·3/5): λ < 5/3 → finite nonzero limit 5√21/(2(5−3λ)); λ = 5/3 → (n+1)√21/2 → +∞; λ > 5/3 → +∞. Opposite of Theorem S on the finest-only build, where resistance λ=5/3 was the unique finite freeze.

## Discovery

A geometric-series lift of Theorem G on the multi-scale edge set (edges at every generation), via Kigami nested harmonicity / decimation. Isolates multi-scale combinatorial λ=1 as a finite freeze (5√21/4) and shows multi-scale resistance diverges linearly.

## Why It Matters

Settles the harmonic audit on the multi-scale graph left open by DISC-0051. Does not decide α=0.45 on either graph (DISC-0034 stays OPEN). Not thrust.

## Derivation

Checked. Nested harmonicity ⇒ L_ms u = 0 on fine interior; I_ms = Σ λ^g (3/5)^g I(0); audit map linear with ‖audit(I(0))‖ = √21/2. Geometric series and trichotomy are elementary. Same substance class as DISC-0051 (scalar/sum lift of G), not analogous to Theorems J/K/L.

## Assumptions

Multi-scale edge set (Assumption item 7); corner data (1, −1/2, 0); Theorem G; combinatorial harmonic u.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_W.log` (repository witness EXIT:0, all checks passed) and `/workspace/scratch-ifi/indep_theorem_W.py` / `indep_theorem_W.log`: nested annihilation through level 4; I_ms = Σ (λ·3/5)^g I(0) and closed-form ‖F‖ through level 4 for λ ∈ {1, 1.2, 5/3, 2, 4}; resistance linear growth through level 6; contrast finest-only resistance freeze √21/2; freeze-break attempt fails by >10.

## Prior Art

Theorem G / Kigami nested harmonicity and resistance renormalization; Theorem S (DISC-0051) on the finest-only build. Classical gasket harmonic extension / decimation.

## Novelty Analysis

DERIVATIVE: sum/nested lift of DISC-0031 Theorem G on a different edge set. No novelty claimed. Not elevated to THEOREM (elementary relative to J/K/L).

## Falsification Attempts

Reran the witness; independent rebuild matched closed form and nested harmonicity; attempted multi-scale resistance freeze at √21/2 fails (‖F(6)‖ ≈ 16.04). No discrepancy with the repository claim.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Correct elementary corollary of Theorem G + nested harmonicity.

## Patent Relevance

None.

## Related Discoveries

- DISC-0031. Mathematical. Theorem G supplies I^(g) = (3/5)^g I(0).
- DISC-0051. Mathematical. Finest-only uniform-λ trichotomy (resistance freezes).
- DISC-0064. Failed hypothesis. Multi-scale resistance does not freeze.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.

## Open Questions

Spectral fractional operators on the multi-scale graph (NOT THIS); combinatorial α=0.45 limit (OPEN).

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 92b869ede53c77d04e923e4cf9be4537572bbb67 && PYTHONPATH=scripts python3 scripts/gasket_multiscale_weights.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_W.log`, `/workspace/scratch-ifi/indep_theorem_W.log`.

## Evidence Log

- 2026-10-09. Recorded from GASKET.md Theorem W at 92b869ede53c77d04e923e4cf9be4537572bbb67; repo witness EXIT:0; independent check ARCHIVE_INDEP_THEOREM_W_PASS. Repository description still matches its claim fence. Prior tip 5bcebf3 was hygiene-only (no status change for DISC-0061/0062).

## Change History

- 2026-10-09. Initial archive entry.
