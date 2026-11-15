# Discovery: Theorem CP — explicit n_0 = 4 for the sign of CO.5's residual, and the exact rate λ_2²/(r|λ_3|) of CO.5's convergence

## Discovery ID
DISC-0202

## Status
THEOREM (mathematical sense only; proof and arb witness are in the source repository). Method: KNOWN (explicit Taylor remainder of log(1+x), geometric tail bounds on an eigen-expansion, interval arithmetic). The specific constants for this operator: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~1:05 PM EDT; source commit 2026-10-30 12:09:34 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit f7845ada80f95ebb7af3a4d77664a073abc4d561

## Original Evidence
- GASKET.md, new section "Theorem CP" (line 4004, +47 lines).
- CLAIM_STATUS.md, new row 98 after Theorem CO.
- scripts/gasket_fractional_profile_level_threshold.py (new, 166 lines); scripts/cli.py; tests/test_cli.py (+24); README.md.

## Discovery
With T_n = log(s_{n+1}/(r s_n)) − B q_2ⁿ(q_2 − 1), q_j = λ_j/r:
- CP.1 (arb on CC's certified s_4..s_13): sign T_n = (−1)ⁿ for 4 ≤ n ≤ 12.
- CP.2: for n ≥ 12, T_n/q_3ⁿ = B_3(q_3 − 1) + (B²/2)(1 − q_2²) wⁿ + R_n, w = q_2²/q_3 = −0.73915380, |R_n| ≤ P_1θⁿ + P_2|q_2|ⁿ + P_3|q_3|ⁿ + P_4(|q_2|³/|q_3|)ⁿ, θ = 0.058590, P_1 ≤ 1.6405e17, P_2 ≤ 1.53e4, P_3 ≤ 1.70e6, P_4 ≤ 185.461; E_1(12) ≤ 269.33 < 1630.28 ≤ B_3(q_3 − 1). Hence sign T_n = (−1)ⁿ for every n ≥ 4 and 1360.9|q_3|ⁿ ≤ |T_n| ≤ 1906.1|q_3|ⁿ.
- CP.3: E_2(15)/|w|¹⁵ ≤ 5.028 < 32.704 = (B²/2)(1 − q_2²), so from n = 15 the deviation T_n/q_3ⁿ − B_3(q_3 − 1) has sign (−1)ⁿ and, divided by wⁿ, tends to 32.7041 ≠ 0: CO.5's limit is approached at the exact rate λ_2²/(r|λ_3|) = 0.7391537958.

## Why It Matters
Supplies the explicit n_0 and constant that DISC-0201 (CO.5) listed as open, and identifies the third-order term in the level-sum ratio asymptotics as the (λ_2/r)² cross term, not θ or |q_2|.

## Derivation
GASKET.md CP proof, checked by hand here:
- Exact identity T_n = B_3q_3ⁿ(q_3 − 1) + (ε_{n+1} − ε_n) − (Q(β_{n+1}) − Q(β_n)), Q(x) = x − log(1+x): correct from β_n = Bq_2ⁿ + B_3q_3ⁿ + ε_n.
- The q_2^{2m} parts of Q give +(B²/2)q_2^{2n}(1 − q_2²), i.e. (B²/2)(1 − q_2²)wⁿ after division by q_3ⁿ: correct sign.
- ε_m ≤ (ε_0/a_1)(ρ/r)^{m−4} = Eθ^m|q_3|^m with E = (ε_0/a_1)(r/ρ)⁴, since θ|q_3| = ρ/r: correct.
- |γ_m| ≤ G_*|q_3|^m and |β_m| ≤ B_*|q_2|^m for m ≥ n_0 use |q_3/q_2| < 1: correct.
- Each P_i term matches summing m = n, n+1 and dividing by |q_3|ⁿ. Taylor remainder Σ_{k≥3}|x|^k/k ≤ |x|³/(3(1 − |x|)): correct.
- Monotonicity: each term is a positive constant times a power of a base < 1, so the n = 12 and n = 15 inequalities propagate. Sound.

## Assumptions
CG.3 enclosures of r, λ_2, λ_3; CN.2 expansion with ε_0 ≤ 2.9·10⁴ (imported, not re-run); CO.4 a_1, a_2, a_3 (mid values re-run, radii as stated); CC level sums s_4..s_13 (re-run). Textbook Taylor bound.

## New Results
Explicit sign pattern for every n ≥ 4; explicit two-sided bound on |T_n|; exact third-order rate 0.7391538 with limit constant 32.7041.

## Prior Art
Explicit remainder bounds for log-ratio asymptotics of eigen-expansions are textbook (e.g. de Bruijn, "Asymptotic Methods in Analysis"); computer-assisted interval verification: Tucker, "Validated Numerics" (2011). Mechanism standard; no prior statement about this specific operator found, which is expected for a repository-specific object.

## Novelty Analysis
Method KNOWN. Specific constants for this gasket level-sum operator only. Not a first in any general sense.

## Falsification Attempts
- Repo witness: see Evidence Log.
- Independent script `mathematics/scripts/indep_theorem_CP.py` (mpmath, no repo imports; inputs CG/CO midpoints and CO.4 radii, CC's 12-digit s_4..s_10), 21/21 PASS: w, θ; B_3(q_3 − 1) = 1633.47 ± 3.18 (lower 1630.29); E = 1.6365e17, G_* = 1841.1, B_* = 8.21075; P_1 = 1.6404e17, P_2 = 1.522e4, P_3 = 1.6976e6, P_4 = 185.4609 (all under the stated bounds); (B²/2)(1 − q_2²) = 32.70414; E_1(11) = 4583.05 (so the tail bound alone needs n ≥ 12, as the repo says), E_1(12) = 269.324; bases of E_2/|w|ⁿ 0.0793, 0.2334, 0.0545, 0.1725; E_2(15)/|w|¹⁵ ≤ 5.028, E_2(14)/|w|¹⁴ = 63.42; two-sided bounds 1360.9/1906.1 reproduced; sign T_n = (−1)ⁿ and |T_n|/|q_3|ⁿ ∈ [1360.9, 1906.1] for n = 4..9 from float data.
- Attacked: whether n_0 = 12 is really reached (E_1(11) fails, E_1(12) passes with margin ~6×); whether the λ_4 term could spoil CP (it sits inside ε_n and is covered by P_1θⁿ); whether the B radius could flip CP.3 (32.704 ± 2·10⁻⁴ vs 5.028). No break found. Minor: the repo prints the fourth base as 0.1726, arb gives 0.1725 ± 5·10⁻⁵ (rounding up, harmless).
- Not checked independently: CN.2's ε_0 (imported by the repo too).

## Experimental Validation
Computational only. The repo notes data cannot test CP.3 directly because B_3(q_3 − 1) is enclosed only to ±3.2.

## Mathematical Status
Theorem (computer-assisted constants; CG/CN/CO enclosures imported).

## Patent Relevance
None. Pure spectral asymptotics; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0201 → DISC-0202 (mathematical): CO.5's "no explicit n_0" item answered. DISC-0200 → DISC-0202: CN.2's ε_0 is the input that sets n_0 = 12.

## Open Questions
λ_4 and a_4 ≠ 0; optimal n_0, n_1; C_G in CF.3; eigenvalues on |z| = ρ(L_k); rate for inf R_n; closed forms.

## Next Experiments
Certify λ_4 ≈ −2.16·10⁻⁴ and a_4 (float fit in DISC-0201 suggests a_4 ≈ −2.2·10⁻⁷); a sharper ε_0 would lower n_0 below 12 without the data step.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at f7845ada80f9; `pip install python-flint mpmath sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_threshold.py` (about 17 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CP.py` in this repo.

## Evidence Log
- 2026-10-30 ~1:00 PM EDT: repo witness at f7845ada80f9 EXIT 0 (16.3 s script, wall 16.9 s), 11 `ok` checks, ends "all Theorem CP checks passed"; arb two-sided bounds [1361.0 ± 0.034], [1906.0 ± 0.022]; E_2(15)/|w|¹⁵ = [5.027 ± 2.1e-4]; rate [0.7391537958 ± 4.6e-11]. Independent check 21/21 PASS.

## Change History
- 2026-10-30: created from IFI f7845ada80f9.

## Note (2026-10-30, appended; text above unchanged)
The next experiment "certify λ_4 and a_4" is done by IFI Theorem CQ at cae1d855f3c79c6a7c2b109422adaaefe52e554c: λ_4 = −0.00021644655283736 ± 1.53·10⁻¹⁸, a_4 = −2.204·10⁻⁷ ± 5.54·10⁻¹¹ ≠ 0. CP is unchanged (its ε_n already contained the λ_4 term). See DISC-0203.
