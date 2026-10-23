# Discovery: Theorem BQ, below log3/log5 the corner deficit approaches 1 at the exact rate ρ^n at every level

## Discovery ID

DISC-0165

## Status

THEOREM in the mathematical sense only (repository proof; constants computer-assisted with python-flint arb, N=1 only). Method KNOWN (monotone numerator/denominator bracketing under BK.1's change of variables). Constants C_N novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~12:58pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 01c39d01aa86aa64eb165f85f28503f2e3209974.

## Original Evidence

GASKET.md Theorem BQ (heading at GASKET.md line 2643, NOT-THIS fence line 2705, arb list line 2710; BP's open "Rates below γ" item at line 2628 now marked answered), CLAIM_STATUS.md new row, README.md, scripts/gasket_fractional_deficit_rate_small_alpha.py (new, 421 lines), scripts/cli.py, tests/test_cli.py, all at 01c39d01aa86aa64eb165f85f28503f2e3209974. Builds on Theorem BP (DISC-0164, 4ee50b22193b), BK.1–BK.4 (DISC-0155), BG.3 (DISC-0146), AQ (3), AS, AY (DISC-0125).

## Discovery

Write 1−δ_N^(n)=ρ^n 𝒩_N^(n)/D_n with 𝒩^(n)=∫τ^−α R_n η_N(ψ_(n−N)(5^−N τ)) (ρ=5^α/3).

BQ.1: BK.1's transfer τ=5^(n+1)y, τ'=5^n p(y) gives 𝒩^(n+1)−𝒩^(n)=ρ^−n∫(ω_n−1)η_N(p^(n+1−N)y)p^−α r_n(p)p' dy>0 for every α∈(0,1), N≥1, since ω_n≥(1+y/5)^α>1 and η_N>0. So 𝒩^(n) increases strictly to P_N (BG.3).

BQ.2: for α<γ, D_n increases to D_∞<∞ (AQ (3)), so 𝒩^(m)ρ^n/D_∞<1−δ_N^(n)<P_Nρ^n/D_m for every n>m≥N, hence ρ^−n(1−δ_N^(n))→C_N=P_N/D_∞>0 and successive ratios →ρ. At γ (derived from AY as stated): n(1−δ_N^(n))→(2 sin(πγ)/π)P_N/c_R(γ).

BQ.3 (certified, N=1): C_1(0.01)∈[0.0078312,0.0078363], C_1(0.1)∈[0.0606923,0.0607522], C_1(0.3)∈[0.0933210,0.0934143], C_1(0.45)∈[0.0718892,0.0719611]; for every n≥1, 0.050648ρ^n<1−δ_1^(n)(0.45)<0.118859ρ^n; D_∞(0.45)∈[4.000301,4.002302] contains Theorem AS's value.

## Why It Matters

Answers the open "rates below γ" item that DISC-0164 (Theorem BP) left: BP's float ratios 0.44→0.34 at α=0.01 are explained as convergence to ρ. The limit itself is BG.3 specialised (the repository says so); the every-level bracket and the monotone numerator are the new parts.

## Derivation

Repository proof (GASKET.md Theorem BQ). Re-derived this slice: given 𝒩^(n)↑P_N and D_n↑D_∞, the bracket 𝒩^(m)/D_∞<ρ^−n(1−δ^(n))<P_N/D_m for n>m is immediate, and both ends converge to P_N/D_∞. ω_n>(1+y/5)^α follows from d_n≤B<1 with 1−B=y(y+4)/(3(y+2)(y+5))>0 (sympy).

## Assumptions

Used as stated by the repository, not re-run there or here: AQ (3), BG.3, BH.2/BJ.4, BI.4 (G=0.6031), BJ.1, BJ.3, BK.1–BK.4, BL.1, AY. α<γ for the ρ^n statement. Certificates are N=1 and pointwise in α.

## New Results

Exact order ρ^n of 1−δ_N^(n) below γ with explicit every-level brackets; n^−1 order at γ (derived).

## Prior Art

Monotone ratio bracketing and change-of-variables renormalisation are routine; no literature search on these specific gasket constants. Not searched further.

## Novelty Analysis

Method KNOWN. The limit is a specialisation of the repository's own BG.3. Novelty of the constants and the every-level bracket UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Repository witness EXIT 0 in 142.4 s (/workspace/scratch-ifi/repo_theorem_BQ.log), all checks "ok". (2) Archive /workspace/scratch-ifi/indep_theorem_BQ.py, 12/12 PASS: sympy 1−B>0; C_1 brackets at α=0.3 and 0.45 rebuilt from the printed cells as [𝒩^(30)_lo/D_∞,hi, (𝒩^(30)_hi+E_30)/D_∞,lo] agree with the printed brackets to the 3e−7 resolution of the six-digit printed cells (at α=0.3 the rebuilt lower end is 0.0933208 against printed 0.0933210, a rounding artifact of the printed cells, not evidence of an error); every-n lower bound 0.050648=𝒩^(1)_lo/D_∞,hi reproduced; D_∞(0.45) contains AS's 4.0013017734819; the printed float V^(n) equal ρ^−n(1−δ^(n)) with ρ=5^0.45/3 to 1e−5; V^(20) lies in the certified C_1(0.45) bracket; the float ratio (1−δ^(20)/1−δ^(12))^(1/8)=0.68714 against ρ=0.68773. (3) Logic attack: the lower bracket needs 𝒩 increasing and D_n<D_∞, the upper needs D_n>D_m; both are supplied. No failure found. Arb cells were not independently re-certified.

## Experimental Validation

Computational only. Repository witness log and archive log as above.

## Mathematical Status

Theorem (mathematical sense; constants computer-assisted).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0164 → DISC-0165 (mathematical: answers BP's open rate question). DISC-0146/DISC-0151 → DISC-0165 (mathematical: the limit is BG.3 specialised). DISC-0125 → DISC-0165 (mathematical: n^−1 rate at γ via AY). DISC-0165 → DISC-0166 (mathematical: renormalised deficit not monotone).

## Open Questions

Eventual monotonicity of V^(n); closed forms for C_N and P_N; N-dependence of C_N; certificates for N≥2 or uniform in α; DISC-0159's limit clause above γ stays CONJECTURE (BQ is below γ only).

## Next Experiments

Certify N=2 at α=0.45; float V^(n) for n up to 40 at α=0.3, 0.45 to test eventual monotonicity.

## Reproduction Instructions

git -C informational-flux-identity checkout 01c39d01aa86aa64eb165f85f28503f2e3209974; python3 scripts/gasket_fractional_deficit_rate_small_alpha.py (≈140 s; sympy, mpmath, python-flint). Archive: python3 /workspace/scratch-ifi/indep_theorem_BQ.py.

## Evidence Log

- 2026-10-23 ~12:58pm EDT. Indexed; repo witness EXIT 0; independent checks 12/12 PASS.
- 2026-10-23 ~1:59pm EDT. Consistency with DISC-0167 (Theorem BR at bed41594e18c): BQ.3's ρC_1 lies below the certified c_∞ at α=0.01, 0.1, 0.3, 0.45 (archive indep_theorem_BR.py PASS).

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-23 ~1:59pm EDT. Open question "N-dependence of C_N" answered by DISC-0167 (Theorem BR at bed41594e18c): ρ^N C_N strictly increases in N to a finite c_∞(α), so C_N has exact order ρ^−N (c_∞(0.45)≈0.5204 vs ρC_1(0.45)≈0.0494). BR.1 also proves the ceiling η_N≤2/(2+z) that BQ quoted from BH.2/BJ.4. No status change; other open questions (closed forms, eventual monotonicity of V^(n), N≥2 certificates) remain.
