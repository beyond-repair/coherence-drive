# Discovery: Theorem CV — exact rates |ν_2^(k)|/ρ(L_k) of inf R_n^(k) → ρ(L_k) for k = 5, …, 12, and Kept Failure CV.6 (|q^(k)| is not monotone in k; it peaks at k = 8)

## Discovery ID
DISC-0208

## Status
THEOREM (mathematical sense only; interval-certified proof in the source repository) for CV.1–CV.5 and CV.7. Method: KNOWN (CU's routine rerun with N = 180, Neumann power 20, per-k inner radii). Constants: UNRESOLVED as to novelty; no claim of a mathematical first. CV.6: REJECTED extrapolation (CU's observation "|q^(k)| increases with k" fails at k = 9; it was an observation, not a claim). The limits q^(k) → −1/3 and 3^k ρ(L_k) → 1/3: CONJECTURE-level observation only, not proved. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~9:12 PM EDT; source commit 2026-10-30 20:41:42 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 00df4a6ea6d77d67c95977738cb994b5c9f5e49e

## Original Evidence
- GASKET.md, new section "Theorem CV" (line 4285; NOT THIS paragraph line 4337), +60 lines.
- CLAIM_STATUS.md, new row 104.
- scripts/gasket_fractional_profile_level_infrate_k5.py (new, 138 lines; imports CU's script); scripts/gasket_fractional_profile_level_infrate_k.py (+11/−4: guard that skips CU.3's CL.3 consistency check when no CL.3 interval exists, i.e. k ≥ 5; k = 2, 3, 4 unchanged); scripts/cli.py (+1); tests/test_cli.py (+41, `test_theorem_cv_profile_level_infrate_k5`); README.md (+2/−1).

## Discovery
Setting as in DISC-0207 (CU): (L_k f)(s) = u_1 f(σ_1) + u_2 f(σ_2), u_i = wt_i/(2σ_i)^k, h_n = L_kⁿ1, R_n^(k) = h_{n+1}/h_n on X = [√5/2, 5/2], L_k on CG's H²(D). CU left k ≥ 5 open.
- CV.1–CV.3: ‖L_k(I − P_180)‖ ≤ 5.70·10⁻⁴¹; Krawczyk eigenpairs of M_180; ‖A²⁰‖_F < ρ_in²⁰ with ρ_in = 1/5000, 1/12500, 1/35000, 1/10⁵, 1/(3·10⁵), 1/(9·10⁵), 1/(2.6·10⁶), 1/(7.8·10⁶); exactly two eigenvalues in |z| > ρ_in, real and simple:

  | k | ρ(L_k) (±6e-20) | ν_2^(k) (±6e-20) | \|q\| |
  |---|---|---|---|
  | 5 | 0.0014792559239634748 | −0.0005161358132104635 | 0.3489158332 |
  | 6 | 0.0004853393939726874 | −0.0001723958039714274 | 0.3552066989 |
  | 7 | 0.0001597483711719488 | −0.0000572111535546882 | 0.3581329383 |
  | 8 | 0.0000527169494750854 | −0.0000189167039184835 | 0.3588353292 |
  | 9 | 0.0000174329038013139 | −0.0000062429809833751 | 0.3581148072 |
  | 10 | 0.0000057745266397710 | −0.0000020588085310616 | 0.3565328657 |
  | 11 | 0.0000019153320627478 | −0.0000006789469804583 | 0.3544800370 |
  | 12 | 0.0000006359658135257 | −0.0000002240022214049 | 0.3522236835 |

- CV.4: Γ_+ = 0.416558 … 0.824925, Γ_− = 1.129942 … 2.33819 (to ≤ 6e-6); c_± = ρ(1−q)Γ_±.
- CV.5: for every n ≥ n_0 = 16, 22, 26, 31, 34, 37, 43, 47, ρ(1−q)|q|ⁿ(Γ_par − θ_n) ≤ ρ − inf_X R_n ≤ ρ(1−q)|q|ⁿ(Γ_par + θ_n): exact rate |q^(k)|.
- CV.6 (Kept Failure): with CT.3/CU.3 (k ≤ 4), |q^(k)| strictly increases for k = 1..8 and strictly decreases for k = 8..12; |q^(8)| − |q^(9)| = 7.205·10⁻⁴.
- CV.7: 3^k ρ(L_k) strictly decreases for k = 1..12 (0.40306495 → 0.33797831) and stays > 1/3.

## Why It Matters
Closes CU's open item k ≥ 5 up to k = 12, and corrects a natural extrapolation (monotone |q^(k)|) that DISC-0207 had recorded as matching the data for k ≤ 4. The hump at k = 8 is explained heuristically by the fixed point s* = 3/2 of σ_1 (σ_1'(s*) = −1/3, wt_1(s*) = 1/3).

## Derivation
Read and checked here: CV.1–CV.5 are CU.1–CU.5 with three parameter changes (N, m, ρ_in); the only script edit is a guard around a consistency check, which removes a check, not a proof step (CL.3 never certified intervals for k ≥ 5). CV.6/CV.7 are finitely many interval comparisons. Heuristic for the observation: for large k the branch u_1 dominates near s*, and a single-branch weighted composition operator with attracting fixed point has nonzero spectrum {wt_1(s*)|σ_1'(s*)|^k σ_1'(s*)^j}, giving ρ ≈ 3^{−k}/3 and q ≈ −1/3. Not proved by the repo or here.

## Assumptions
Everything CU uses (DISC-0207), CU's script itself, CT.3's and CU.3's q^(k), ρ(L_k) for k ≤ 4 (as stated, for CV.6/CV.7 only).

## New Results
Certified ρ(L_k), ν_2^(k) to ~20 digits for k = 5..12; exact rates and two-sided constants from n_0(k); finite-range monotonicity of 3^k ρ(L_k); a certified non-monotonicity of |q^(k)|.

## Prior Art
Same as DISC-0206/0207: Hardy-space Galerkin truncation and validated numerics for transfer operators (e.g. Bandtlow–Slipantschuk; Tucker 2011), Krawczyk, Kato perturbation, Collatz–Wielandt brackets. The k → ∞ heuristic is the standard spectrum of a weighted composition operator at an attracting fixed point (Koenigs-type eigenvalues; cf. Cowen–MacCluer, Composition Operators on Spaces of Analytic Functions). No literature search for these constants was done.

## Novelty Analysis
Method KNOWN. Constants specific to this repository's operators; novelty UNRESOLVED. The non-monotonicity is a fact about these operators, not a new phenomenon class.

## Falsification Attempts
- Repo witness at 00df4a6ea6d7: see Evidence Log.
- Independent script `mathematics/scripts/indep_theorem_CV.py` (numpy only, no repo code; Chebyshev collocation on X, not H²(D), N = 60 and 80, plus collocation power iteration for R_n): 71/71 PASS on the second version.
  - ρ and ν_2 agree with CV.3 to ≤ 6·10⁻¹⁴ (ρ) and ≤ 1.1·10⁻¹² (ν_2) relative for all k = 5..12; both real, ν_2 < 0; third eigenvalue |ν_3| < ρ_in < |ν_2| for every k (e.g. k = 12: 7.35·10⁻⁸ < 1.28·10⁻⁷ < 2.24·10⁻⁷), so the radii are well placed.
  - Γ_+ (n = 20) and Γ_− (n = 21) reproduced within 1e-4 for every k (e.g. k = 12: 0.824927, 2.338197 vs claimed 0.824925, 2.33819); c_± = ρ(1−q)Γ_± reproduced to 2e-5 relative.
  - CV.6 reproduced independently from collocation for all k = 1..12 (including CT/CU's k ≤ 4 values to 1e-9): up to k = 8, down to k = 12, gap 7.2052·10⁻⁴. CV.7 reproduced (same 12 values to 8 digits).
  - **Kept first-version failure (my check, not the repo):** v1 computed Γ_− with the repo's ρ against my N = 80 collocation's iterates and failed at k = 12 (2.338346 vs 2.33819). Cause: N = 80 collocation differs from the true ρ(L_12) by ~6·10⁻¹⁴ relative, which is 1.2·10⁻⁴ of |q|²¹. A 60-digit mpmath iteration at N = 70 (`indep_theorem_CV_gamma_mp.py`) shows the same floor blowing up for n ≥ 25 (logged). v2 uses the collocation's own ρ, ν_2 and passes. No defect in CV.
- Beyond-range probe (floats, not claimed): k = 13..16 give |q| = 0.34994, 0.34775, 0.34571, 0.34387 and 3^k ρ = 0.33695, 0.33615, 0.33552, 0.33504, continuing towards 1/3 as the repo's observation predicts. Consistent; not a proof.
- Script-edit attack: the guard only skips a check when no CL.3 interval exists; k = 2..4 path unchanged. Survived.
- Not checked independently: arb resolvent bounds, Neumann bound ‖A²⁰‖_F, CG.3 homotopy, θ_n windows at n_0 (n = 16..47 needs > float precision against a collocation floor).

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (interval-certified, computer-assisted) for k = 5..12; Kept Failure CV.6 is a certified counterexample to an extrapolation; the k → ∞ limits are open.

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0207 → DISC-0208 (mathematical): CU's open item k ≥ 5 addressed for k ≤ 12; CU's monotone-|q| observation refuted at k = 9. DISC-0206 → DISC-0208 (mathematical): CT.3's k = 1 values used in CV.6/CV.7. DISC-0204 → DISC-0208 (computational): CR's Krawczyk/Neumann routines via CU. DISC-0191 → DISC-0208 (mathematical): CG.3 homotopy.

## Open Questions
Uniform-in-k rate; proof of q^(k) → −1/3 and 3^k ρ(L_k) → 1/3; k ≥ 13 certified; n < n_0(k); closed forms; circle eigenvalues; CF.3's general-f constant; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
A single-branch comparison operator at s* = 3/2 could turn the k → ∞ heuristic into a perturbation bound (the second branch weight is ~ (2σ_2)^{−k}, exponentially smaller); certify k = 13..16 to confirm the descent.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 00df4a6ea6d7; `pip install python-flint mpmath numpy`; `python3 scripts/gasket_fractional_profile_level_infrate_k5.py` (about 300 s; `CV_KS=5,6` runs a subset). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CV.py` (about 4 s); `python3 discoveries/mathematics/scripts/indep_theorem_CV_gamma_mp.py 12` (about 6 s; shows the collocation floor).

## Evidence Log
- 2026-10-30 ~9:11 PM EDT: repo witness at 00df4a6ea6d7 EXIT 0, 194 `ok`, 0 FAIL, script elapsed 279.0 s (wall 4m39s, box shared with other jobs), ends "all Theorem CV checks passed"; e.g. k = 10 ρ_H = [5.7745266397710e-6 ± 4.23e-20], ν_2 = [−2.0588085310616e-6 ± 5.71e-20], |q| = [0.3565328657 ± 2.14e-11], n_0 = 37; |q^(12)| − 1/3 = [0.0188904 ± 5e-8]. Repo test `test_theorem_cv_profile_level_infrate_k5` not run this slice (it reruns the same ~300 s witness).
- Independent check: v1 70/71 (k = 12 Γ_− failed, cause above), v2 71/71 PASS.

## Change History
- 2026-10-30: created from IFI 00df4a6ea6d7.
