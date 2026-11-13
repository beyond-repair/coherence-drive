# Discovery: Theorem BN, BK's one-level weight ω_k is increasing, so the ρ^−n rate is attained for every N≥1

## Discovery ID

DISC-0161

## Status

THEOREM in the mathematical sense only (repository proof; BN.1–BN.4 analytic given AQ/BI/BK/BL, BN.5 computer-assisted with python-flint arb). Method KNOWN; constants novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~8:00am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 335860e44ebff5d3ad55498d4efc9f96c5ff8d12.

## Original Evidence

GASKET.md Theorem BN (BN.1–BN.5), CLAIM_STATUS.md new row, README.md OPEN bullet, scripts/gasket_fractional_monotone_weight.py (new, 326 lines), scripts/cli.py, tests/test_cli.py, all at 335860e44ebff5d3ad55498d4efc9f96c5ff8d12. Builds on Theorem BM at c9ca93479dbee307e77705a052d995029938a630, Theorem BL at dfc145a9833f96b8960667c572aca38d48adfc17 and Theorem BK at 00d0d28b71db264b070be23c73f8e3f67de704db.

## Discovery

BN.1 (spectral lemma): r_k(s)=(1/2)vᵀ(L_k+s)^−1 v is a Stieltjes function of unit mass (L_k symmetric PSD, |v|²/2=1), so r_k≤1/s and 0≤−r_k'≤r_k/s at every level k.

BN.2 (monotone weight): with d_k=B−C·r_k(p), C=(5/3)(1+2y/5)e, one has exactly d_k'−αd_k/(5+y)=B'−αB/(5+y)+r(−C'+αC/(5+y))+Cp'(−r_k'(p)), K₀=−C'+Cp'/p=2y(2y²+10y+15)/(3(y+2)²(y+5))≥0, hence d_k'−αd_k/(5+y)≤−P_α/(3(y+2)²(y+5)²) with P_α=2αy³+(17α−1)y²+46αy+40α+10, which is positive for α≥1/17. So ω_k=(1+y/5)^α/d_k is strictly increasing in y at every level for every α∈[1/17,1). This was floats-only in BL.

BN.3: Chebyshev's covariance inequality gives δ_N^(k+1)>δ_N^(k) for every N≥1, k≥N, α≥1/17.

BN.4: a pair form of the covariance restricted to {τ'≤τ₀}×{y≥y₀} gives δ^(k+1)−δ^(k)≥ρ^−k·MΛ_N/(D'_k D'_(k+1)), Λ_N>0, so for every α∈(γ,1), every N≥1 and n≥N: c_Nρ^−n≤δ_N−δ_N^(n)≤(3/2)J_α/((1−ρ^−1)D'_0)·ρ^−n with c_N=MΛ_N/(D'_∞²(1−ρ^−1))>0. No deficit ceiling is needed, so BL/BM's thresholds N₀(α) disappear.

BN.5 (certified, y₀=1/10, τ₀=51/100, N=1..19 direct, N≥20 uniform): c_N>0 at α=0.7, 0.75, 0.8, 0.85, 0.9, 0.95; e.g. at α=0.8, c_1≥1.758e−3 and c_N≥1.965e−2 for N≥20.

## Why It Matters

Closes the gap DISC-0157/DISC-0160 left at small N (N=1..8 at α=0.8, N=1..60 at α=0.7): the corner-deficit rate ρ^−n is two-sided for every N≥1 and every α above log3/log5, and the n-monotonicity of δ_N^(n) is now a theorem for every α≥1/17 (including below γ). It also settles the "monotone ω_k" open question listed in DISC-0160 for α≥1/17.

## Derivation

GASKET.md Proof of BN (repository). Independently re-derived this slice: d=(1+2y/5)(5/3)β−Cr equals B−Cr; K₀ closed form; Ψ_α=B'−αB/(5+y)+K/p=−P_α/(3(y+2)²(y+5)²) (sympy, from scratch, no repository imports); P_(1/17) coefficients (2/17, 0, 46/17, 210/17)≥0; the a=0 numerator carries the factor y²−10 (so the a=0 part alone does not close, as the repository says).

## Assumptions

Theorem AQ's identity r_k(s)=(1/2)vᵀ(L_k+s)^−1 v at every level (the repository re-checks it with exact rationals only for n=0..3); d_k>0 (BK); BI.3, BI.4, BK.4, BL.1, BL.4(ii) and the orbit lemma as stated; arb enclosures in the script (re-run by the repository witness, not re-certified in this archive). BN.4 is qualitative for every α∈(γ,1); certified constants exist only at six exponents. BN.2's method needs α≥1/17 (at α=1/100 the majorant P_α has positive roots y≈4.05 and 40.6, a method limit, not a counterexample).

## New Results

For every α∈(γ,1) and every N≥1, n≥N: δ_N^(n) strictly increases in n and c_Nρ^−n≤δ_N−δ_N^(n)≤Cρ^−n. DISC-0156's THEOREM part (sharpness half of BK.6) now covers every N≥1, not just N≥N₀(α). Conjecture BL.6 (DISC-0159) splits: its monotonicity clause is proved for every N≥1 and α≥1/17; its limit clause (existence and N-independence of C_δ) stays a conjecture.

## Prior Art

Stieltjes/Pick-function representations of resolvent quadratic forms vᵀ(L+s)^−1 v for PSD L are textbook (spectral theorem; Krein–Stieltjes classes). Chebyshev's covariance (association) inequality for co-monotone functions is classical. Decimation for p.c.f. fractals as in DISC-0157. Constants not searched.

## Novelty Analysis

Method KNOWN. The specific polynomial P_α and the certified constants are the repository's own; novelty UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Independent sympy re-derivation of BN.2 (no repository imports): PASS. (2) BN.1 inequalities r_k≤1/s, 0≤−r_k'≤r_k/s checked beyond the repository's exact n≤3, for k=4..7 on 101 log-spaced s∈[1e−6,1e4] with mpmath 50 digits via AQ's recursion: 0 violations. (3) ω_k increasing in y for k=0..6 at α=1/17 (the method's edge) and 0.8, 71 log-spaced points: 0 violations. (4) Random unit-mass Stieltjes sums satisfy the BN.1 inequalities (2000 trials): PASS. (5) Repository witness EXIT 0 in 71 s, every certified bracket positive. (6) Presentation erratum, same class as DISC-0160: the script prints arb lower bounds with round-to-nearest %.3e, so 68 of the 120 printed "c_N≥" decimals sit above the actual lower bound in the last digit (e.g. α=0.7 c_1: printed 3.253e−4, arb lower bound 3.252544e−4; α=0.8 N≥20: printed 1.966e−2, bound 1.965993e−2; full list /workspace/scratch-ifi/bn_rounding.log). Only positivity of c_N is used, so the theorem is unaffected. (7) No conflict with DISC-0157's larger floor c_N≥0.1240 (N≥40, α=0.8): both are lower bounds from different arguments.

## Experimental Validation

Repository witness EXIT 0 (/workspace/scratch-ifi/repo_theorem_BN.log, 71.2 s). Repository floats at α=0.8: δ_N^(n) increases over n=8, 12, 20 for N=1..8 (N=1: 0.9487→0.9562, N=8: 0.1183→0.2379) with gaps above c_N(ρ^−8−ρ^−20).

## Mathematical Status

Theorem (mathematical sense; BN.1–BN.4 analytic given AQ/BI/BK/BL, BN.5 computer-assisted).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0155 → DISC-0161 (mathematical: BK.1's weight ω_k and BK.4's ceiling). DISC-0157 → DISC-0161 (mathematical: BL.1's monotone G_k and BL.4(ii)'s pointwise bound). DISC-0161 → DISC-0156 (mathematical: sharpness half for every N≥1). DISC-0161 → DISC-0159 (mathematical: monotonicity clause of BL.6 proved; limit clause open). DISC-0161 → DISC-0160 (mathematical: removes N₀(α)).

## Open Questions

Existence and N-independence of C_δ(α) (DISC-0159); monotone ω_k for α<1/17; a certificate uniform in α; whether AQ's identity at every level should be stated as a separate lemma (the repository checks it exactly only for n≤3).

## Next Experiments

Try the second-order expansion of δ^(k+1)−δ^(k) to attack the limit C_δ; extend BN.2 below 1/17 with a sharper bound on −r_k' than r_k/s.

## Reproduction Instructions

git -C informational-flux-identity checkout 335860e44ebff5d3ad55498d4efc9f96c5ff8d12; python3 scripts/gasket_fractional_monotone_weight.py (≈71 s, needs python-flint and sympy). Archive checks: python3 /workspace/scratch-ifi/indep_theorem_BN.py; cd scripts && python3 /workspace/scratch-ifi/bn_rounding.py (rounding audit).

## Evidence Log

- 2026-10-23 ~8:00am EDT. Indexed; repo witness EXIT 0; independent sympy/mpmath checks PASS; rounding erratum recorded.

## Change History

- 2026-10-23. Initial archive entry.
