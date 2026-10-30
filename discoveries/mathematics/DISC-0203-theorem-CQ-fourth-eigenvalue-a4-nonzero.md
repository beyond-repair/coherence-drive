# Discovery: Theorem CQ — the fourth eigenvalue λ_4 of the level-sum transfer operator, a_4 ≠ 0, and the exact rate |λ_4| of CN.2's remainder

## Discovery ID
DISC-0203

## Status
THEOREM (mathematical sense only; proof and arb/rigorous-float witness are in the source repository). Method: KNOWN (Pellet's root-counting test, Krawczyk eigenvector enclosures, Riesz projections and the second resolvent identity, rigorous floating-point residual bounds after Higham). The specific constants for this operator: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~3:05 PM EDT; source commit 2026-10-30 14:40:01 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit cae1d855f3c79c6a7c2b109422adaaefe52e554c

## Original Evidence
- GASKET.md, new section "Theorem CQ" (line 4051, +35 lines).
- CLAIM_STATUS.md, new row 99 after Theorem CP.
- scripts/gasket_fractional_profile_level_fourth.py (new, 294 lines); scripts/cli.py (+1 entry); tests/test_cli.py (+35); README.md (+2).

## Discovery
For CE's transfer operator L̃ on H²(D), D = {|s − 83/50| < 8/5}, with M_N = P_N L̃ P_N:
- CQ.1 (arb, 1100 bits): Pellet passes at ρ = 1/1000 (k = 78, ratio 3.5348) and at ρ' = 1/20000 (k = 77, ratio 4.2343), so M_80 has exactly one eigenvalue in ρ' < |z| < 1/1000, and it is real.
- CQ.2 (rigorous floats + arb): resolvent circles |z + 2.164466·10⁻⁴| = 1/20000 and |z| = 1/20000 satisfy sup‖(z − L̃P_80)⁻¹‖·ε_80 < 1 (5.33·10⁻⁵ and 1.20·10⁻³). By CG.3's homotopy, L̃ has exactly one eigenvalue λ_4 inside G_4, real and simple, and every eigenvalue other than r, λ_2, λ_3, λ_4 has |μ| < 5·10⁻⁵.
- CQ.3 (N = 140, Krawczyk eigenvectors, rank-one resolvent split, maximum principle): λ_4 = −0.00021644655283736 ± 1.53·10⁻¹⁸; |λ_4|/r = 0.0005108108830 ± 2.54·10⁻¹⁴.
- CQ.4: a_4 = −2.204·10⁻⁷ ± 5.54·10⁻¹¹ ≠ 0 (negative); a_4^N = −2.20397513845781·10⁻⁷.
- CQ.5: s_{k+4} = a_1rᵏ + a_2λ_2ᵏ + a_3λ_3ᵏ + a_4λ_4ᵏ + e'_k with |e'_k| ≤ 9.817·10⁷·(1/20000)ᵏ; hence CN.2's remainder e_k = a_4λ_4ᵏ + e'_k has e_k/λ_4ᵏ → a_4 and sign e_k = (−1)^{k+1} for every k ≥ 24.

## Why It Matters
Resolves the "a_4 ≠ 0" and "certify λ_4" items left open in DISC-0201 and DISC-0202: the level-sum expansion now has four certified, nonzero eigen-terms, and the remainder that CN.2 bounded only crudely has an exact rate.

## Derivation
Checked by hand here:
- Pellet: a ratio > 1 at index k certifies exactly N + 1 − k roots outside ρ. With N = 80 (81 roots), k = 78 gives 3 and k = 77 gives 4, so exactly one root in the annulus. A real characteristic polynomial forces a lone root to be real. Correct.
- Homotopy z − L̃P_N − τL̃(I − P_N): if ‖(z − L̃P_N)⁻¹‖·ε_N < 1 on a circle, the eigenvalue count inside is constant in τ ∈ [0,1] (CG.3's argument). This is standard Kato-type perturbation counting. Correct.
- CQ.3 localisation: (1.598·10²¹)·(3.96·10⁻³⁰) ≈ 6·10⁻⁹ < 1 on |z − μ_4^140| = 10⁻¹⁸, so λ_4 lies within 10⁻¹⁸ of μ_4^140. Consistent with the stated ±1.53·10⁻¹⁸ (adds μ's own radius).
- CQ.5 threshold: need (ρ'/|λ_4|)ᵏ < |a_4|/ε_0' = 2.204·10⁻⁷/9.817·10⁷ = 2.245·10⁻¹⁵. ln(2.245·10⁻¹⁵)/ln(0.231004) = 23.02, so k ≥ 24, and k = 23 fails (0.231004²³ ≈ 2.33·10⁻¹⁵). The repo's k_0 = 24 is exactly right.
- Sign: a_4 < 0 and λ_4 < 0 give sign(a_4λ_4ᵏ) = (−1)^{k+1}. Correct.

## Assumptions
Imported as stated, not re-run by the repo: CE.1–CE.3; CG.3's |z| = 1/1000 circle and its count. Re-run in the witness: CN.1's box checks and S, CO.1's continuation, CO.2's Taylor enclosures. Textbook: Pellet, Krawczyk/Brouwer, Riesz projections, second resolvent identity, maximum principle, Higham's dot-product error bounds (Accuracy and Stability of Numerical Algorithms, Thm 3.5, §3.6).

## New Results
λ_4 to 18 digits; a_4 ≠ 0 with sign; all remaining spectrum in |μ| < 5·10⁻⁵; exact rate |λ_4| and explicit sign threshold k ≥ 24 for CN.2's remainder.

## Prior Art
Pellet's theorem (1881) and its use in validated root counting; Krawczyk (1969) and Rump's verified eigenpair methods; Riesz projections and resolvent perturbation (Kato, Perturbation Theory for Linear Operators); computer-assisted spectral enclosures of transfer operators (e.g. Jenkinson–Pollicott on Hausdorff dimension; Bahsoun–Galatolo et al. on rigorous transfer-operator approximation). Mechanism standard; no prior statement about this specific operator found, which is expected for a repository-specific object.

## Novelty Analysis
Method KNOWN. The constants are specific to this gasket level-sum operator. Not a first in any general sense.

## Falsification Attempts
- Repo witness: EXIT 0, 22 `ok`, 0 FAIL (see Evidence Log).
- Independent script `mathematics/scripts/indep_theorem_CQ.py` (numpy + mpmath, no repo imports; own matrix builder from the closed-form weights and branches by 8192-point FFT on |u| = 1, double-precision eig at N = 60, 100, 140, 180; data LSQ on CC's 12-digit s_4..s_14), 12/12 PASS: r, λ_2, λ_3 reproduced; λ_4 = −2.16446552839·10⁻⁴ (agrees to < 10⁻¹³), real; |λ_4|/r = 0.00051081088; exactly one float eigenvalue in 5·10⁻⁵ < |z| < 10⁻³ and every further eigenvalue below 5·10⁻⁵ at all four N; four-term LSQ on the data gives a_4 = −2.20419·10⁻⁷ (within 0.01% of CQ's −2.204·10⁻⁷), and the bare n = 4 residual s_4 − a_1 − a_2 − a_3 = −2.20407·10⁻⁷. Sign logic (−1)^{k+1} checked for k < 30.
- Two first-version checks failed and are kept in the script as comments: (1) demanding λ_4 stable to 10⁻¹⁵ across N failed because double-precision eig scatters it by ~2·10⁻¹⁴ (float noise, not a CQ defect; CQ's certified value uses arb); (2) the repo's float values for the next eigenvalues (−1.744·10⁻⁷ and a pair near −1.16·10⁻⁸ ± 1.55·10⁻⁷i) were NOT reproduced: in double precision eigenvalues of size ~10⁻⁷ move with N (non-normal matrix). CQ does not claim them (kept limit: only bounded by 5·10⁻⁵), so this does not break the theorem, but those float values in the docstring should be treated as unconfirmed.
- Attacked: whether CQ.5's k_0 = 24 is tight (yes, k = 23 fails); whether the G_4 circle could hold a second eigenvalue (CQ.1's count plus the |z| = ρ' circle exclude it); whether the CP result needs revision (no: CP's ε_n already contained the λ_4 term, as the repo says).
- Not checked independently: CG.3's |z| = 1/1000 count and CE.1–CE.3 (imported by the repo too).

## Experimental Validation
Computational only. The data LSQ agreement on a_4 (DISC-0201's earlier float fit suggested ≈ −2.2·10⁻⁷) is consistent with the certified value.

## Mathematical Status
Theorem (computer-assisted constants; CG.3 circle and CE.1–CE.3 imported).

## Patent Relevance
None. Pure spectral asymptotics; the repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0201 → DISC-0203 (mathematical): DISC-0201's float hint a_4 ≈ −2.2·10⁻⁷ certified. DISC-0202 → DISC-0203: DISC-0202's "certify λ_4 and a_4" next experiment done. DISC-0200 → DISC-0203: CN.2's remainder e_k gets the exact rate |λ_4|.

## Open Questions
Closed forms of λ_4, a_4; eigenvalues inside |z| < 5·10⁻⁵ (Pellet at 10⁻⁵ fails); C_G in CF.3; eigenvalues on |z| = ρ(L_k); inf R_n rate; Ψ_info and Stage 2 remain blocked in the repo.

## Next Experiments
Certify a fifth eigenvalue with a higher-precision (not double) eigen-solver at larger N; check whether the float cluster near 10⁻⁷ is real or a truncation artefact.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at cae1d855f3c7; `pip install python-flint mpmath sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_fourth.py` (about 4 min). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CQ.py` in this repo (under 1 s).

## Evidence Log
- 2026-10-30 ~3:00 PM EDT: repo witness at cae1d855f3c7 EXIT 0 (246.0 s script, 247 s wall), 22 `ok`, 0 FAIL, ends "all Theorem CQ checks passed"; Pellet ratios [3.5348 ± 4.7e-5], [4.2343 ± 4.5e-5]; μ_4^140 = [−0.0002164465528373605235665 ± 4.0e-26]; ‖P‖ = [1597.99 ± 4.4e-3]; a_4^N = [−2.20397513845781e-7 ± 4.2e-22]; |a_4 − a_4^N| ≤ [5.29e-11 ± 2.9e-14]; ε_0' = [9.817e7 ± 2.2e3]; ρ'/|λ_4| = [0.231004 ± 9.0e-8]. Independent check 12/12 PASS (two first-version checks failed and are documented above).

## Change History
- 2026-10-30: created from IFI cae1d855f3c7.
