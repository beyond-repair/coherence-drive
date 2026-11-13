# Discovery: Theorem DT, level-sum bound carried to the second-order cone K_(2,6)

## Discovery ID
DISC-0232

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED), with KEPT FAILURE DT.4 (no gain for k = 4..10). Closes the kept limit of DISC-0230/DISC-0231 ("level-sum bound of CF.3/DN.3/DO.3 form on K_(2,6) still not computed").

## Date Discovered
2026-11-12 (indexed ~6:10 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 84cb64b224d95f8ace598386c11dfaf69d4e2110 (2026-11-12 5:47 PM EST).

## Original Evidence
- GASKET.md §Theorem DT (line 5386; NOT THIS disclaimer at line 5427).
- CLAIM_STATUS.md (row at line 128, Theorem DT; also replaces DS's runtime placeholder "~RUNTIME min" with "~2.4 h").
- scripts/gasket_fractional_profile_level_second_order_sums.py (new, 410 lines); registered in scripts/cli.py; tests/test_cli.py (+37 lines).

## Discovery
With f_0 = F_0 = Lt^4 G and F_m = Lt^m f_0:
- DT.1: for m = 0..5, |F_m'|/F_m <= 0.79279 and F_m''/F_m in [0.20609, 1.68331], so every F_m lies in the interior of K_(2,6) = {f > 0 : |f'| <= 2f, |f''| <= 6f}.
- DT.2: 0.147313 < Theta_K(F_0, F_1) < 0.147314, two-sided enclosures for m = 0..5 (m = 5: (2.8125, 2.8163)e-5). Corollary: since K_(2,6) is inside C_2, these sharpen DO.2's Theta_2 uppers for m = 2..5.
- DT.3: |log(s_(k+1)/(r s_k))| <= B_K(k) = min_(m <= min(5,k-4)) Theta_K(F_m, F_(m+1)) G_K(k-4-m), G_K built from theta_n = tanh(Dbar_n/4) (n = 3..8, mixed blocks, DR.3/DS.3's diameters). Per-level rate theta_7^(1/7) < 0.2694000 (DO.3: 0.363657). B_K < B_DO for every k >= 11 (1.816x at k = 11, 151x at k = 22, 3.1e12x at k = 103).
- DT.4 (kept failure): for k = 4..10, DO.3's bound stays smaller (factors > 1.611), because Theta_K >= Theta_2 >= Theta_100 and no K block applies until k-4-m >= 3.

## Why It Matters
It turns DR/DS's certified cone-diameter contraction factors into an actual convergence bound for the level sums s_k, the first in this line below DP's C^1 cap 0.3170757 per level. The rate is still far from the spectral 0.1725476 (DQ.4).

## Derivation
Hilbert projective metric on a cone cut out by the functionals Lambda = {delta_s, 2delta_s ± delta_s', 6delta_s ± delta_s''}; Theta_K(u,v) = log(sup rho_l / inf rho_l), rho_l = l(v)/l(u). Birkhoff contraction (CF.1) by tanh(diam/4) per block; CF.3's telescoping argument with mixed block lengths. Theta_K enclosed with second-order centred forms on 1024 cells, using arb jets of order 4 built from CO.2's Taylor data with Cauchy tails.

## Assumptions
CF.1, CF.3's proof (DN.3/DO.3 form), DQ.1 (Lt K in K), DQ's/DP.1's description of Theta_K; DR.3's and DS.3's certified diameters used as stated (their scripts not re-run by DT); DO.3's constants for the comparison; CO.1/CO.2 Taylor data; CE.4's r; Birkhoff–Hopf as an assumption (DJ's remark); correctness of python-flint arb.

## New Results
A certified level-sum bound with per-level rate 0.2694 on K_(2,6) beating DO.3 for all k >= 11; sharper Theta_2 uppers for m = 2..5; a certified explanation (DT.4) why second-order constraints do not help the constants for m >= 2.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012 (Hilbert-metric cone contraction); interval/centred-form certification (Moore; Tucker 2011) is standard. Constants specific to this operator; novelty of the constants UNRESOLVED.

## Novelty Analysis
Method KNOWN. The bound and constants are new to the corpus; no external first claimed or supported.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_second_order_sums.py` (default 1024 cells) EXIT 0, "all Theorem DT checks passed", 319.8 s on the archive box (CLAIM_STATUS says ~3.3 min; slower box only). Printed B_K(11) = [9.6045e-6 ± 4.75e-11] < stated 9.6046e-6; B_DO/B_K(11) = 1.816; tail slope 0.300012 > 0; consistency with CC's s_4..s_13 max ratio 0.08782.
- Independent composition check (archive /workspace/ifi-dt-indep/indep_dt.py, mpmath, from stated D̄_n and the rounded Theta_K uppers): every stated theta_n bound holds; theta_7^(1/7) = 0.26939998 < 0.2694 (margin ~2e-8, tight but the arb run gives [0.26939998 ± 3.6e-9]); argmin block n = 7 confirmed; B_K(13, 22, 49, 103) below their stated bounds. With the 4-digit rounded upper 0.0010009, B_K(11) = 9.6048e-6 slightly exceeds the stated 9.6046e-6; the arb upper 0.001000862 gives 9.6045e-6, so this is presentation rounding only. PASS.
- Monotonicity attack: Theta_K floors exceed DO.2's Theta_100 uppers by > 1.61 for all m, as required by K in C_2 in C_100 (checked by the script).
- DT_FULL=1 (4096 cells, ~12 min) not run here.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated in the repository, conditional on DR.3/DS.3's diameters (DS.3's full 200-cell cover now reproduced independently, see DISC-0231 note); kept failure DT.4.

## Patent Relevance
None.

## Related Discoveries
DISC-0231 (DS, n = 4 factor), DISC-0230 (DR, factors n = 3, 5..8), DISC-0229 (DQ, cone and spectral limit), DISC-0228 (DP cap).

## Open Questions
Certified D_n for n >= 9 (or sharper D_7, D_8) to push 0.2694 toward 0.1725; other invariant K_(a,b) (b >= 4.936) with smaller m = 0, 1 constants; direct constants for m >= 6; a level-sum bound not of CF.3 (oscillation-of-ratio) form.

## Next Experiments
Run DT_FULL=1 on the archive box and record; certify D_9 on K_(2,6).

## Reproduction Instructions
Clone informational-flux-identity at 84cb64b224d9; `pip install python-flint sympy numpy`; `python3 scripts/gasket_fractional_profile_level_second_order_sums.py` (~3.3-5.3 min) or `DT_FULL=1 ...` (~12 min); or `python3 -m pytest -q tests/test_cli.py -k theorem_dt`.

## Evidence Log
- 2026-11-12 ~6:05 PM EST: repo witness EXIT 0 (319.8 s, 1024 cells); independent composition check PASS (rounding nit at k = 11 noted).

## Change History
- 2026-11-12: created.
- note 2026-11-13 ~2:05 AM EST: kept failure DT.4 resolved by Theorem DV (IFI 8ec657a289ec, DISC-0234): the direct bound osc log R_(k-4) beats DO.3 at k = 4..10. DT.4 stays true as a statement about DT.3-form bounds; original text above preserved.
