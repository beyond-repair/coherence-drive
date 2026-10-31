# Discovery: Theorem AT, certified refinement-rate constants of the gasket corner resolvent

## Discovery ID

DISC-0113

## Status

THEOREM (mathematical sense only; computer-assisted, conditional on DISC-0106 (Theorem AQ), DISC-0109 (Theorem AR) and DISC-0111 (Theorem AS) as stated in-repo). Novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~6:01am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 68af4dd0c3989732a1b8b8ea0275948b7c33051a (2026-10-22 05:35:48 −0400). Paths: GASKET.md "Theorem AT", "KEPT FAILURE AT.1", "CONJECTURE AT.2"; CLAIM_STATUS.md row "Certified refinement-rate constants c_R, c_S of Theorem AR — VERIFIED (Theorem AT, Kept Failure AT.1)"; scripts/gasket_fractional_rate_constants.py (new, 410 lines); scripts/cli.py; README.md.

## Original Evidence

GASKET.md Theorem AT (1) exact transfer ρ^(−m)∫s^(−α)δ_(m+1)=ρ^(−n)∫t^(−α)δ_(n+1)A_k^α B_k C_k with A_k=∏(1+q^i/5), B_k=∏5/√(25+4q^i), C_k=∏(3/5)D_(n+i)(q^i); (2) level-n bracket between B_∞ and A_∞^α C̄ (C̄ from AQ (4)'s ceilings); (3) mpmath.iv 60-digit certificate at n=40 (2811 nodes; nodes 5^(−40)2^(−110)(33/32)^k); (4) consequences.

## Discovery

Certified (widths <2e−17): c_R(0.45)∈[0.497802650763560354, 0.497802650763560356], c_S(0.45)∈[0.927092638569461377, 0.927092638569461384], c_R(γ)∈[0.517165834630505243, 0.517165834630505245], c_S(γ)∈[0.481399003768729118, 0.481399003768729121], plus α=0.25, 0.60, 0.75 (valid for all α∈(0,1), no power window). Derived: ρ^(−n)ΔR_n=c_R+O(5^(−0.65n)); R_γ(n)=c_R(γ)n+C_γ+O(5^(−0.65n)); ‖F(n,0.45)‖−𝓛∼c_F ρ^n with c_F∈[0.52027873061815, 0.52027873061821]. Correction: AR's float c_S(0.45)=0.927091 was low by 1.6e−6 (inside AR's stated 1e−3).

## Why It Matters

Certifies the constants that DISC-0109 left as computed floats, upgrades AR's o(1)/o(n) to exponential error, and gives the certified leading coefficient of the approach to the audit limit of DISC-0111.

## Derivation

As in the repository. (1) iterate AR's step δ_(j+1)(s)=D_j(s)δ_j(p(s)), substitute s=q^k(t), use q(x)(5+q(x))=x and q'=1/√(25+4x); scalars collect to 1 (archive-checked). (2) (3/5)D_j≥1 and D_j≤D̄ via z r_∞(z) increasing and den≥4+y, then monotone limits. (3) outward-rounded computation; (4a) weight difference ≤C t^0.65 near 0. Archive re-read (1), (2), (4a); no gap found. (3) not independently re-certified in interval arithmetic.

## Assumptions

Theorems AQ (1)–(4) incl. power ceiling r_m≤Bs^(−0.35) (B≈0.892577, re-certified in-script), AR (1)–(2), AS (2)–(3); correctness of mpmath.iv outward rounding; the 0.45 used is the nearest double (as in DISC-0106/0111).

## New Results

- DISC-0109's constants certified (DISC-0109 stays THEOREM; edge only).
- Observation (repo, reproduced in archive, NOT a theorem): true correction is Θ(3^(−m)) (ratio 81 per 4 levels), faster than the proved O(5^(−0.65m)).

## Prior Art

Spectral decimation on the Sierpinski gasket (Rammal–Toulouse; Fukushima–Shima; Strichartz; Teplyaev) and Koenigs/Poincaré-function linearization are classical; validated numerics via interval arithmetic standard. Repository-defined audit quantities; no targeted literature search for these constants.

## Novelty Analysis

Method: KNOWN components. Certified constants for this repository-defined quantity: UNRESOLVED.

## Falsification Attempts

Archive /workspace/scratch-ifi/indep_theorem_AT.py (mpmath 40-digit float quadrature of the decimation recursion, no repo import): (A) ρ^(−m)ΔR_m and μ^(−m)Δσ_m at m=12,16,20,24 for α∈{0.45, γ, 0.75} converge to the certified c_R, c_S (m=24 deviations −1.8e−12/−1.3e−11 at 0.45, −1.0e−12/−5.2e−12 at γ, −7.6e−13/−3.6e−12 at 0.75), with deviation ratio 81.00–81.04 per 4 levels, reproducing the repo's 3^(−m) observation; (B) from own deep R_90, σ_90: c_R/(1−ρ)=1.594119764546743 and c_F=0.5202787306181774, both inside the stated enclosures, and (‖F(30)‖−𝓛)/ρ^30=0.5202831; (C) g(s)=s^(1−γ)r_90(s) at s=5^(−40)5^(j/8) reproduces all 8 stated Θ values to 2e−9, spread 1.465e−5, and g(5^(−30))≈g(5^(−40)) to 1e−12; (D) 32-point log-mean gives (2 sin πγ/π)ln5⟨g⟩=0.5171658346305052439; (E) transfer scalars collect to 1 at α=0.25,0.45,0.75. Not broken. Limitation: float evidence, no independent interval re-certification.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Theorem (computer-assisted).

## Patent Relevance

None identified.

## Related Discoveries

- DISC-0106 → DISC-0113, DISC-0109 → DISC-0113, DISC-0111 → DISC-0113 (mathematical; inputs).
- DISC-0113 → DISC-0109 (computational; certifies AR's constants, corrects c_S float).
- DISC-0113 → DISC-0114 (Kept Failure AT.1), DISC-0113 → DISC-0115 (Conjecture AT.2).
- DISC-0113 → DISC-0035 (computational; approach coefficient; law stays CONJECTURE).

## Open Questions

Closed forms for c_R, c_S, c_F, C_γ, 𝓛; sharp correction exponent (observed 3^(−m)); certified 𝓛(α) for 0.65≤α<γ.

## Next Experiments

Prove the 3^(−m) correction from r_∞≍s^(γ−1); independent interval re-certification at a different n and grid ratio.

## Reproduction Instructions

`git -C informational-flux-identity checkout 68af4dd0c3989732a1b8b8ea0275948b7c33051a && python3 scripts/gasket_fractional_rate_constants.py` (~2.5 min, EXIT 0, 22 PASS). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AT.py` (~82 s, EXIT 0, 19 PASS; mpmath float, no repo import).

## Evidence Log

- 2026-10-22. Repo witness EXIT 0, 22 PASS (/workspace/scratch-ifi/repo_theorem_AT.log). Archive indep EXIT 0, 19 PASS (/workspace/scratch-ifi/indep_theorem_AT.log).

## Change History

- 2026-10-22. Initial archive entry.
