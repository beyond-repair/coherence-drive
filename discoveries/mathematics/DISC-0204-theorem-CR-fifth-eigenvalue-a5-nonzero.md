# Discovery: Theorem CR — the fifth eigenvalue λ_5 of the level-sum transfer operator, a_5 ≠ 0, every further eigenvalue below 10⁻⁸, and the exact rate |λ_5| of CQ's remainder

## Discovery ID
DISC-0204

## Status
THEOREM (mathematical sense only; proof and arb witness are in the source repository). Method: KNOWN (Krawczyk eigenpair enclosures, rank-one Riesz projections, Neumann-series resolvent bounds, Kato-type homotopy eigenvalue counting, the second resolvent identity). The specific constants for this operator: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~5:25 PM EDT; source commit 2026-10-30 16:31:12 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit f847490267b123a24efcbbb066aa08308d9a192d (checked at descendant 9cb3b84d6b2863320e2903993b9a31927af2d6ce, which leaves CR unchanged)

## Original Evidence
- GASKET.md, new section "Theorem CR" (line 4086 at 9cb3b84d6b28, +37 lines).
- CLAIM_STATUS.md, new row 100 after Theorem CQ.
- scripts/gasket_fractional_profile_level_fifth.py (new, 334 lines; imports CN's, CG's and CO's scripts unchanged; `CR_N=200` reproduces Kept Failure CR.6); scripts/cli.py (+1 entry); tests/test_cli.py (+25); README.md (+2/−1).

## Discovery
For CE's transfer operator L̃ on H²(D), D = {|s − 83/50| < 8/5}, M_N = P_N L̃ P_N, N = 300 (ε_300 ≤ 1.141·10⁻⁶³), arb at 512 bits:
- CR.1: Krawczyk encloses right/left eigenpairs of M_300 at r, λ_2, λ_3, λ_4, λ_5 (radii 10⁻¹³⁰); the enclosures are real and disjoint, so the rank-one projectors P_i are exact. μ_5^300 = −4.550141188008649836529478·10⁻⁸ ± 2.1·10⁻³³, ‖P_5‖ ≤ 1.0717·10¹².
- CR.2: with Q = I − ΣP_i, A = MQ: ‖A^jQ‖_F for j = 0..6 and ‖A⁷‖_F ≤ 1.40·10⁻⁶⁶, so the Neumann series bounds ‖(z − M)⁻¹Q‖ on every circle in |z| ≥ 10⁻⁸ without a cover: every other eigenvalue of M_300 has |z| < 10⁻⁸.
- CR.3: resolvent circles (|z| = 10⁻⁸, |z| = 6, four circles of radius 10⁻²⁰, G_5 of radius 10⁻²¹) satisfy K_T ε_300 < 1; by CG.3's homotopy L̃ has exactly five eigenvalues in |z| > 10⁻⁸, real and simple: r, λ_2, λ_3, λ_4 and λ_5 = −4.550141188009·10⁻⁸ ± 4.51·10⁻²¹, |λ_5|/r = 1.073827052·10⁻⁷ ± 1.93·10⁻¹⁷. Every other eigenvalue has |μ| < 10⁻⁸ (CQ had 5·10⁻⁵).
- CR.4: CO.3/CO.4's projection formula and the second resolvent identity on |z − μ_5| = 10⁻⁸: |a_5 − a_5^N| ≤ 2.83·10⁻¹⁶, a_5^N = −2.13234993568815·10⁻¹¹, so a_5 = −2.1323·10⁻¹¹ ± 7.9·10⁻¹⁶ ≠ 0 (negative).
- CR.5: s_{k+4} = Σ_{i≤5} a_iλ_iᵏ + e''_k, |e''_k| ≤ 6.79·10²⁰·10⁻⁸ᵏ; CQ's remainder e'_k = a_5λ_5ᵏ + e''_k has e'_k/λ_5ᵏ → a_5 and sign e'_k = (−1)^{k+1} for every k ≥ 48: exact rate |λ_5|.
- Kept Failure CR.6 (repo): at N = 200 the a_5 bound is 2.55·10⁵ against |a_5^N| = 2.13·10⁻¹¹, so N = 200 cannot decide the sign; N = 300 gains ~10²¹ in ε_N.

## Why It Matters
Closes DISC-0203's next experiment ("certify a fifth eigenvalue with a higher-precision solver; is the float cluster near 10⁻⁷ real?"). Answer: the cluster was float noise; the true fifth eigenvalue is ≈ −4.55·10⁻⁸ and the next ones are below 10⁻⁸ (≈ −2.07·10⁻¹⁵ by uncertified Ritz values). The level-sum expansion now has five certified nonzero eigen-terms.

## Derivation
Checked by hand here:
- CR.5 threshold: ρ_in/|λ_5| = 10⁻⁸/4.5501411880·10⁻⁸ = 0.2197734. Need 6.79·10²⁰·0.2197734ᵏ < |a_5| ≥ 2.1315·10⁻¹¹; k = 47 gives 8.03·10⁻¹¹ (fails), k = 48 gives 1.77·10⁻¹¹ (holds). So k_0 = 48 is what the bounds give, as stated (the repo does not claim optimality).
- Sign: a_5 < 0 and λ_5 < 0 give sign(a_5λ_5ᵏ) = (−1)^{k+1}. Correct.
- CR.6 arithmetic: ε_200/ε_300 = 1.03·10⁻⁴²/1.141·10⁻⁶³ ≈ 9·10²⁰, matching "N = 300 gains 10²¹".
- The λ_5 enclosure is μ_5^300 ± (10⁻²¹ circle + rounding); the stated midpoint −4.550141188009·10⁻⁸ is the 13-digit rounding of μ_5^300, 3.5·10⁻²¹ away, inside ± 4.51·10⁻²¹.

## Assumptions
Imported as stated: CE.1–CE.3, CG.1's tail formula (constants re-run at N = 300), CG.3's homotopy argument, CN.1's box argument (box checks and S re-run), CO.1–CO.2 (re-run at N = 300), CQ.3's λ_4 (identification only). Textbook: Krawczyk/Brouwer, Riesz projections, Neumann series, second resolvent identity, maximum principle, trapezoid aliasing.

## New Results
λ_5 to ~20 digits; a_5 ≠ 0 with sign; every remaining eigenvalue in |μ| < 10⁻⁸; exact rate |λ_5| and sign threshold k ≥ 48 for CQ's remainder; documentation that N = 200 is insufficient for a_5.

## Prior Art
Krawczyk (1969) and Rump's verified eigenpair methods; Riesz projections and resolvent perturbation (Kato, Perturbation Theory for Linear Operators); Neumann-series resolvent bounds; computer-assisted spectral enclosures of transfer operators (Jenkinson–Pollicott; Bahsoun–Galatolo et al.). Mechanism standard; no prior statement about this specific operator found, as expected for a repository-specific object.

## Novelty Analysis
Method KNOWN. The constants are specific to this gasket level-sum operator. Not a first in any general sense.

## Falsification Attempts
- Repo witness: EXIT 0, 29 `ok`, 0 FAIL, "elapsed 541.2s" (see Evidence Log).
- Independent script `mathematics/scripts/indep_theorem_CR_CS.py` part A (python-flint + mpmath, no repo imports): own matrix builder (closed-form weights and branches, DFT on |u| = 1 in acb at 600 bits, K = 1024 and 2048), own eigen-solver (block subspace iteration with 8 vectors and Rayleigh–Ritz, not Krawczyk), N = 140 and 200. Results: r, λ_2, λ_3, λ_4 reproduced; μ_5 = −4.550141188008649836529478·10⁻⁸, equal to CR.1's μ_5^300 to < 10⁻³¹ and stable across N and K to < 10⁻³⁰; |λ_5|/r = 1.07382705219·10⁻⁷; |λ_5|/|λ_4| = 0.0002102200810; exactly five Ritz values above 10⁻⁸, sixth = −2.0695·10⁻¹⁵ (agrees with the repo's uncertified mpmath remark). k_0 = 48 and the sign logic recomputed.
- Part B (semi-independent; F0's Taylor coefficients and c_0 = 3σ_{−3} are taken from the repo's own evaluator, dumped by `indep_theorem_CR_CS_dump_f0.py` at M = 4096): with my own right/left eigenvectors at N = 300, a_1..a_5^N = 0.00571256871089, −4.15763912994·10⁻⁵, −2.36115967884·10⁻⁵, −2.20397513846·10⁻⁷, −2.13234993569·10⁻¹¹; a_5^N agrees with CR.4's printed a_5^N to 2.9·10⁻²⁶ and is negative; a_1..a_4^N lie inside CN/CO/CQ's enclosures; a_1 + … + a_5 = s_4 − 4.13·10⁻¹⁵ (inside the 5·10⁻¹⁵ rounding of the 14-decimal s_4).
- Failed first versions, kept in the script comments: v1 built c = 83/50 and R = 8/5 at 53 bits by mistake; this moved μ_5 by ~3·10⁻¹⁵ and pushed the sixth Ritz value from 2·10⁻¹⁵ to −1.4·10⁻¹⁰, a direct illustration of the non-normality the repo describes (not a CR defect). v2 compared Σa_i with s_4 at 10⁻¹⁶, below the data's own rounding (my error; fixed to 5·10⁻¹⁵).
- Not checked independently: the arb certification itself (Krawczyk, Neumann bound ‖A⁷‖_F, the resolvent circles, the 2.83·10⁻¹⁶ projection-error bound), CE.1–CE.3, CG.3's homotopy. The independent agreement is float evidence, not a certificate.

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (computer-assisted constants; CE.1–CE.3 and CG.3's homotopy imported).

## Patent Relevance
None. Pure spectral asymptotics; the repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0203 → DISC-0204 (mathematical): CQ's remainder e'_k gets the exact rate |λ_5|; DISC-0203's next experiment done and its float cluster near 10⁻⁷ confirmed as noise. DISC-0201 → DISC-0204 (mathematical): CO.3/CO.4's projection formula reused for a_5. DISC-0191 → DISC-0204 (mathematical): CG.1/CG.3's tail formula and homotopy carry the count. DISC-0204 → DISC-0205 (sibling, same session).

## Open Questions
Closed forms of λ_5, a_5; λ_6 and a_6 (only |μ| < 10⁻⁸ certified); eigenvalues on |z| = ρ(L_k); inf R_n rate; Ψ_info and Stage 2 remain blocked in the repo.

## Next Experiments
Certify λ_6 ≈ −2.07·10⁻¹⁵ (would need ε_N far below 10⁻⁶³·(non-normality), i.e. N well above 300); check whether k_0 = 48 can be lowered by a sharper inner-circle bound.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at f847490267b1 (or 9cb3b84d6b28); `pip install python-flint mpmath sympy numpy`; `cd scripts && python3 gasket_fractional_profile_level_fifth.py` (about 9 min). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CR_CS.py` in this repo (about 1 min; part B needs `IFI_SCRIPTS=<IFI>/scripts python3 indep_theorem_CR_CS_dump_f0.py 4096 300` first, about 80 s, and `F0FILE=f0_M4096_N300.txt`).

## Evidence Log
- 2026-10-30 ~5:11 PM EDT: repo witness at 9cb3b84d6b28 (CR unchanged since f847490267b1) EXIT 0, 29 `ok`, 0 FAIL, elapsed 541.2 s, ends "all Theorem CR checks passed"; ε_300 = [1.141e-63 ± 8.66e-68]; μ_5^300 = [−4.550141188008649836529478e-8 ± 2.05e-33], ‖P_5‖ = [1.0717e12 ± 4.07e7]; ‖A⁷‖_F ≤ [1.40e-66 ± 3.36e-69]; K_T ε_300 on G_5 = [1.16e-22 ± 4.37e-25]; λ_5 = [−4.550141188009e-8 ± 4.51e-21]; a_5^N = [−2.13234993568815e-11 ± 2.86e-26], |a_5 − a_5^N| ≤ [2.83e-16 ± 2.77e-19]; ε_0'' = [6.785e20 ± 1.06e16]; ρ_in/|λ_5| = [0.219773 ± 4.01e-7]; k_0 = 48. CR_N=200 (Kept Failure CR.6) not rerun here.
- Independent check (combined with DISC-0205): final run 38/38 PASS (57 s); earlier v2 run 31/34 with three failures caused by my own tolerances (documented above and in DISC-0205).

## Change History
- 2026-10-30: created from IFI f847490267b1.
