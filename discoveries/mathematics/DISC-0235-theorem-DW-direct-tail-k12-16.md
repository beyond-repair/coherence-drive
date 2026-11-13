# Discovery: Theorem DW, the direct level-sum bound carried to k = 12..16 (osc log R_m for m = 8..12)

## Discovery ID
DISC-0235

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Answers DISC-0234's open item "direct constants for m >= 8". DISC-0234's rejected claim DV.3' stays rejected for B_V; the strict form now holds for the new combined bound B_W. Proved rate unchanged (0.2380). The observed ratio ~0.1725 between consecutive rows is an observation on six rows, not a proved rate.

## Date Discovered
2026-11-13 (indexed ~4:10 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 49f0fa0349fc1f09842a7eda3694befae90b1114 (2026-11-13 3:12 AM EST).

## Original Evidence
- GASKET.md §Theorem DW (line 5533; NOT THIS disclaimer at line 5570).
- CLAIM_STATUS.md (new row, Theorem DW); README.md (+2/-1).
- scripts/gasket_fractional_profile_level_direct_tail.py (new, 285 lines; imports DV's script `gasket_fractional_profile_level_direct_constants.py` unchanged); registered in scripts/cli.py; tests/test_cli.py `test_theorem_dw_profile_level_direct_tail` (+44 lines).

## Discovery
- DW.1 (certified): arb order-4 jets through up to 13 layers of Lt; fourth-order centred forms of R_m = F_(m+1)/F_m intersected with the direct quotient on adaptively bisected cells (64 initial, depth <= 8, tol 0.002, 33 floor points). F_m > 0 on X and two-sided osc log R_m: m = 8 [8.77884, 8.78161]e-8; m = 9 [1.51472, 1.51524]e-8; m = 10 [2.61359, 2.61600]e-9; m = 11 [4.50968, 4.51126]e-10; m = 12 [7.78134, 7.79092]e-11. Rows m = 6, 7 recomputed meet DV.1's and sharpen their uppers. No cone membership claimed for m >= 8.
- DW.2 (proved from DW.1 plus r in [inf R_m, sup R_m], same argument as DV.2): |log(s_(k+1)/(r s_k))| <= osc log R_(k-4) for k = 12..16; beats B_V by 9.594, 17.836, 17.925, 17.922, 21.222; within 1.00032..1.00123 of DO.4's floor (optimal among CF.3-form bounds to 0.13%).
- DW.3 (exact rationals, DV's constants as stated): B_W(k) < min(B_DO(k), B_U(k)) strictly for every k >= 4 (k < 390 directly; 8-periodic ratio in [1.0296, 10.265] for k >= 25; smallest 1.0115 at k = 17).
- Observation (not a theorem): consecutive ratios osc_(m+1)/osc_m for m = 6..11 lie in [0.17239, 0.17276], matching DQ.4's spectral 0.1725.

## Why It Matters
Extends certified direct constants five levels past DISC-0234 and removes the k = 13, 16 ties, so the strict improvement DV.3' becomes true for the combined bound. The near-constant row ratio is strong numerical evidence that the true per-level rate is the spectral 0.1725, but the proved rate stays 0.2380.

## Derivation
DW.2: s_(k+1)/s_k = R_(k-4)(x_0) and r in [inf R, sup R] give |log R(x_0) - log r| <= log(sup R / inf R). Only F_m > 0 is needed, not F_m in K_(2,6). DW.1: Taylor with Lagrange remainder at order 4 on each cell, inclusion-monotone jet arithmetic, quotient jet R = v * (1/u); accepted cells tile X. DW.3: minimum over more candidates; strictness in exact rationals; tail periodicity as in DV.3.

## Assumptions
CF.3's proof (r in [inf R_m, sup R_m]); DO.4 (floor of CF.3-form bounds); DV's, DU.3's, DT.2's and DO.3's constants used as stated (not re-derived here); CO.1/CO.2 Taylor data; CE.4's certificate for r; python-flint arb correctness. In the default run, rows m = 10..12 enter DW.2/DW.3 as stated uppers certified only by the DW_FULL=1 run (repo log /tmp/dw_run1.log, not in the repository). Inherits DISC-0234's scope note that large-k comparison rests on DU.3's B_U < B_DO.

## New Results
Two-sided osc log R_m for m = 8..12; best-known level-sum bound B_W for every k >= 4 in this corpus; DV.3' true for B_W.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012 (Hilbert-metric contraction); centred-form and Taylor-model interval enclosure (Moore; Neumaier; Berz–Makino); Tucker 2011. Novelty of the constants UNRESOLVED; no external first claimed or supported.

## Novelty Analysis
Method KNOWN (higher-order centred forms are standard). Constants new to the corpus.

## Falsification Attempts
- Repo witness (default, rows m = 6..9; stated uppers for m = 10..12): see Evidence Log for exit status and runtime.
- Independent arithmetic from the GASKET table: upper/lower ratios 1.00032, 1.00034, 1.00092, 1.00035, 1.00123 (match DW.2's optimality factors); consecutive-row ratio intervals for m = 6..11 span [0.17239, 0.17276] (match the stated range). PASS.
- Cross-method check: fourth-order rows m = 6, 7 meet DV.1's second-order rows (repo claim; reproduced by the default run).
- Attack on the "rate" reading: six rows with ratio ~0.1725 do not bound any k > 16; the repo states this itself. Kept as observation, not promoted.
- DW_FULL=1 (~44 min) not run here; rows m = 10..12 rest on the repo's full run.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated, conditional on DV/DU.3/DT.2/DO.3 inputs; rate observation is a heuristic/open problem.

## Patent Relevance
None.

## Related Discoveries
DISC-0234 (DV; open item answered, DV.3' strict form now holds for B_W), DISC-0233 (DU; theta_n factors, rate 0.2380 unchanged), DISC-0232 (DT), DISC-0229 (DQ; spectral 0.1725).

## Open Questions
A proved rate near 0.1725 (sharper D_n for n >= 9 or a non-cone spectral argument); direct rows beyond m = 12; whether a non-CF.3-form bound beats osc log R_(k-4).

## Next Experiments
Run DW_FULL=1 independently; try extrapolating the row ratio into a rigorous tail bound (would need a proved contraction, not six samples).

## Reproduction Instructions
Clone informational-flux-identity at 49f0fa0349fc; `pip install python-flint numpy scipy sympy`; `python3 scripts/gasket_fractional_profile_level_direct_tail.py` (~2.3 min) or `DW_FULL=1 python3 scripts/gasket_fractional_profile_level_direct_tail.py` (~44 min); test `python3 -m pytest -q tests/test_cli.py -k theorem_dw`.

## Evidence Log
- 2026-11-13 ~4:10 AM EST: repo default witness `python3 scripts/gasket_fractional_profile_level_direct_tail.py` EXIT 0, all Theorem DW checks passed, 138.6 s (repo states 136 s). Rows m = 6..9 reproduced to the printed digits. Nit: the default run reports B_V factors 17.891, 17.875, 21.184 at k = 14..16 because it uses the looser stated uppers; GASKET's 17.925, 17.922, 21.222 come from the DW_FULL=1 rows. Consistent, not a contradiction.
- 2026-11-13 ~4:10 AM EST: independent ratio arithmetic from the GASKET table PASS (see Falsification Attempts).

## Change History
- 2026-11-13: created.


## Dated note (2026-11-13, ~5:10 AM EST)
The observation above (consecutive row ratios ~0.1725, not a proved rate) is superseded for the orbit F_m by Theorem DX (informational-flux-identity 3b72f8e0bc10; DISC-0236): two-sided L_5|q|^m <= osc log R_m <= U_5|q|^m for every m >= 5 with |q| = 0.1725476. DX's spectral intervals meet DW.1's rows m = 6..12. The original text above is preserved unchanged; the cone rate 0.2380 stays as stated.
