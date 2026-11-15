# Discovery: Theorem CS — sharp constants for the level-sum rate (D_n strictly decreasing from D_4 = 14.59509785 to L = 9.6274) and an explicit sharp C_G* = 0.02105127810 in CF.3's level-sum bound

## Discovery ID
DISC-0205

## Status
THEOREM (mathematical sense only; short proof from CP.2 plus arb-evaluated constants, all in the source repository). Method: KNOWN (elementary: dividing a certified two-sided bound, ratio test for monotonicity, supremum of a product of decreasing positive factors). Constants: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~5:19 PM EDT; source commit 2026-10-30 17:00:27 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 9cb3b84d6b2863320e2903993b9a31927af2d6ce

## Original Evidence
- GASKET.md, new section "Theorem CS" (line 4123, +43 lines).
- CLAIM_STATUS.md, new row 101 after Theorem CR.
- scripts/gasket_fractional_profile_level_sharp.py (new, 122 lines; imports CP's, CN's and CF's scripts unchanged); scripts/cli.py (+1 entry); tests/test_cli.py (+25); README.md (+2/−1).

## Discovery
With q_j = λ_j/r, B = (a_2/a_1)q_2⁻⁴ (CO.4), T_n = log(s_{n+1}/(rs_n)) − Bq_2ⁿ(q_2 − 1) (CP), D_n = log(s_{n+1}/(rs_n))/q_2ⁿ, L = B(q_2 − 1):
- CS.1: q_2 < 0 and CP.2's sign T_n = (−1)ⁿ give U_n = T_n/q_2ⁿ > 0, so 1360.9·ρ_32ⁿ ≤ D_n − L ≤ 1906.1·ρ_32ⁿ for every n ≥ 4, ρ_32 = |λ_3/λ_2| = 0.23343938 ± 2.3·10⁻⁹ (exact rate).
- CS.2: U_{n+1}/U_n ≤ (1906.1/1360.9)ρ_32 ≤ 0.326960 < 1, so D_n strictly decreases for every n ≥ 4 from D_4 = 14.59509785 ± 5.9·10⁻¹⁰ to L = 9.6274 ± 3.6·10⁻⁵; hence L|q_2|ⁿ < |log(s_{n+1}/(rs_n))| ≤ D_4|q_2|ⁿ for every n ≥ 4, both constants best possible (D_4 attained, L the unattained infimum). Sharpens CN.4 (14.60; lower bound 9.626 only for n ≥ 13).
- CS.3: |q_2|/θ^{1/5} = 0.19488027 < 1 (θ = tanh(Δ/4) = 0.5441333187 from CF.2), so the sharp constant in |log(s_{k+1}/(rs_k))| ≤ C_G θ^{k/5} (k ≥ 4) is C_G* = |log(s_5/(rs_4))| θ^{−4/5} = 0.02105127810 ± 2.1·10⁻¹², equality at k = 4 (0.0210492 for θ̄ = 0.5442).
- Consistency: CC's certified s_4..s_13 give D_4..D_12 and certify D_n > D_{n+1} directly for 4 ≤ n ≤ 11.
- Kept limit (repo): C_G is explicit only for the level sums via the spectral route; CF.3's Birkhoff-route constant Θ_a(f_0, L̃f_0) for general f is not computed.

## Why It Matters
Closes the "explicit C_G" item open since DISC-0190 (CF), for the level sums, and turns DISC-0200's CN.4 constants into best-possible ones with a lower bound valid from n = 4.

## Derivation
Checked by hand here:
- CS.1: sign(q_2ⁿ) = (−1)ⁿ = sign T_n, so T_n/q_2ⁿ = |T_n|/|q_2|ⁿ; dividing CP.2's 1360.9|q_3|ⁿ ≤ |T_n| ≤ 1906.1|q_3|ⁿ by |q_2|ⁿ gives the window. Correct.
- CS.2: U_{n+1}/U_n ≤ 1906.1|q_3|^{n+1}/(|q_2|·1360.9|q_3|ⁿ) = (C/c)ρ_32 = 1.400617·0.2334394 = 0.326959 ≤ 0.326960. A positive sequence with ratio < 1 strictly decreases to 0, so D_n ↓ L. D_n > 0 makes |log(s_{n+1}/(rs_n))| = D_n|q_2|ⁿ. Correct.
- CS.3: D_k(|q_2|/θ^{1/5})ᵏ is a product of two positive strictly decreasing sequences; its supremum over k ≥ 4 is the k = 4 value = |log(s_5/(rs_4))|θ^{−4/5}. Correct.
- Scope note (not a defect): the sharp constant is for the bound written with θ^{k/5}. DISC-0190 records CF.3's level-sum form as C_G·0.8855ᵏ (0.8855 > θ^{1/5}) and CF.3's general form uses θ^⌊m/5⌋; with a different base or the floor form the sharp constant would be a different number. CS states which form it sharpens.

## Assumptions
Imported as stated: CP.2's two-sided bound and signs for every n ≥ 4 (DISC-0202), CO.4's B (DISC-0201), CO.5's limit (only for the limit statement), CF.2's θ (DISC-0190; cone constants re-run). CC's level sums re-run.

## New Results
Sharp two-sided constants for the level-sum rate valid for every n ≥ 4; strict monotonicity of D_n; exact rate |λ_3/λ_2| of D_n − L; explicit sharp C_G* for the level sums.

## Prior Art
Elementary real analysis on top of the certified CP.2 bound; validated-numerics framework as in DISC-0202 (Tucker 2011). Birkhoff/Hilbert-metric cone contraction (Birkhoff 1957; Liverani 1995) for the θ-rate form. No prior statement about this specific operator found.

## Novelty Analysis
Method KNOWN (elementary). The improvement of CN.4's upper constant is small (14.60 → 14.5951), as the repo itself says; the content is sharpness and the lower bound from n = 4. Not a first in any general sense.

## Falsification Attempts
- Repo witness: EXIT 0, 14 `ok`, 0 FAIL, elapsed 17.1 s; prints D_n > D_{n+1} certified for n = 4..11, no reversal.
- Independent script `mathematics/scripts/indep_theorem_CR_CS.py` part C (shared with DISC-0204): ρ_32 = 0.233439377717 from my own Ritz values; (C/c)ρ_32 = 0.3269592166 ≤ 0.326960; θ^{1/5} and |q_2|/θ^{1/5} = 0.1948802663; L = 9.6274249 from B = −8.21069; from CC's 12-digit s_4..s_14: D_4 = 14.5950978494 (inside ±5.9·10⁻¹⁰ up to data error), D_4 − L = 4.9677 in [4.0413, 5.6604], D_n − L inside the CS.1 window for n = 4..10, C_G* = 0.0210512780984, θ̄ constant 0.0210492145, D_k(|q_2|/θ^{1/5})ᵏ decreasing for k = 4..13.
- Spectral reconstruction (uses part B's a_1..a_5^N, so it shares the repo's F0 input): s_n ≈ Σ_{i≤5} a_i^N λ_iⁿ⁻⁴ gives D_5..D_12 = 10.7534639, 9.89267977, 9.68897987, 9.64185506, 9.63078274, 9.62821029, 9.62760767, 9.62746735, matching CS.4's printed values to their last digit; B = −8.21068973; D_n strictly decreasing and inside the CS.1 window for 5 ≤ n ≤ 40 in this five-term model.
- Failed first-version checks, kept as script comments: with tolerance 2·10⁻¹²/|q_2|ⁿ for 12-significant-digit data, (1) the D_n match failed at n = 7 (|Δ| = 4.6·10⁻⁷ vs tolerance 4.4·10⁻⁷), and (2) the monotonicity check for n ≤ 11 failed because 12-digit data cannot separate D_n from D_{n+1} beyond n ≈ 9. Both were my tolerance errors: 12 significant digits mean relative error up to 5·10⁻¹² per sum, so the right tolerance is 10⁻¹¹/|q_2|ⁿ. With it the 12-digit data separate n = 4..9, and the spectral reconstruction plus the repo's certified sums cover the rest. These are not CS defects.
- Not checked independently: CP.2's bound itself (imported; see DISC-0202's independent check), CF.2's θ (taken as stated).

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (elementary proof from CP.2; constants arb-evaluated).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0202 → DISC-0205 (mathematical): CP.2's two-sided bound is the whole input. DISC-0200 → DISC-0205 (mathematical): CN.4's constants 14.60/9.626 made sharp, lower bound from n = 4. DISC-0201 → DISC-0205 (mathematical): CO.4's B gives L. DISC-0190 → DISC-0205 (mathematical): CF.3's open C_G made explicit and sharp for the level sums. DISC-0204 ↔ DISC-0205 (sibling, same session).

## Open Questions
CF.3's Birkhoff-route constant for general f (needs a Lipschitz bound for log L̃⁴G); closed forms of D_4, L, C_G*; λ_6, a_6; eigenvalues on |z| = ρ(L_k); inf R_n rate; Ψ_info and Stage 2 remain blocked in the repo.

## Next Experiments
Narrow L (limited by CO.4's ±10⁻⁵ on B); compute the Birkhoff-route Θ_a for f_0 = L̃⁴G.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 9cb3b84d6b28; `pip install python-flint mpmath sympy`; `cd scripts && python3 gasket_fractional_profile_level_sharp.py` (about 18 s). Independent: see DISC-0204.

## Evidence Log
- 2026-10-30 ~5:02 PM EDT: repo witness at 9cb3b84d6b28 EXIT 0, 14 `ok`, 0 FAIL, elapsed 17.1 s, ends "all Theorem CS checks passed"; L = [9.6274 ± 3.60e-5]; |q_3/q_2| = [0.23343938 ± 2.30e-9]; (C/c)|q_3/q_2| = [0.326959 ± 2.17e-7]; D_4 − L = [4.9677 ± 3.82e-5] in [4.04131, 5.66034]; D_4 = [14.59509785 ± 5.83e-10]; |q_2|/θ^{1/5} = [0.19488027 ± 3.71e-9]; C_G* = [0.02105127810 ± 2.04e-12].
- Independent check: final run 38/38 PASS (57 s, combined CR/CS script); v2 31/34 (three tolerance failures documented above).

## Change History
- 2026-10-30: created from IFI 9cb3b84d6b28.

## Note (2026-10-31, appended; text above unchanged)
The kept item "Birkhoff-route constant Θ_a(f_0, L̃f_0) not computed" is answered by IFI Theorem DC at 4996a9fca8782a8a80ceb41494872f85dacbb55d (DISC-0215): Θ_G ≤ 0.28154093, C_G^B ≤ 0.74544057 = 35.411·C_G*. CS's sharp constant stands; the Birkhoff route is provably above a floor of 0.0633864 for this f_0 and cone. Status unchanged.
