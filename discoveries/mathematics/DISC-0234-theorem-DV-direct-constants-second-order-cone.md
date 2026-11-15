# Discovery: Theorem DV, direct constants to m = 7 and the level-sum bound for k = 4..10 on K_(2,6)

## Discovery ID
DISC-0234

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Resolves DISC-0232's kept failure DT.4 ("for k = 4..10 DO.3 stays the bound") and answers DT/DU's open item "direct constants for m >= 6". Keeps a rejected claim DV.3' (strict improvement fails at k = 13, 16). Rate unchanged.

## Date Discovered
2026-11-13 (indexed ~2:05 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 8ec657a289ec7418adeed0e46b6df4f717482c60 (2026-11-13 1:09 AM EST).

## Original Evidence
- GASKET.md §Theorem DV (line 5477; NOT THIS disclaimer at line 5522). Same commit fills DU's placeholders (DU_FULL 16032 s, default ~75 s), closing the DISC-0233 documentation nit.
- CLAIM_STATUS.md (new row, Theorem DV); README.md (+2/-1).
- scripts/gasket_fractional_profile_level_direct_constants.py (new, 412 lines; imports DT's script chain); registered in scripts/cli.py; tests/test_cli.py `test_theorem_dv_profile_level_direct_constants` (+39 lines).

## Discovery
- DV.1 (certified): arb order-4 jets through up to 8 layers of Lt, DT.2's centred forms on adaptively bisected cells (64 initial, depth <= 8, 33 floor points): |F_m'|/F_m <= 0.830756, F_m''/F_m in [0.0962876, 1.77138], min_l l(F_m)/F_m >= 0.945732, so F_m in int K_(2,6) for m = 0..7 (DT.1: m <= 5). Two-sided Theta_K(F_m, F_(m+1)) and osc log R_m for m = 0..7; m = 6: Theta_K in (4.8402, 4.8865)e-6; m = 7: (8.3466, 8.4251)e-7; osc uppers 0.063415 .. 5.1065e-7 (new for every m; DO certified only floors).
- DV.2 (proved from DV.1): |log(s_(k+1)/(r s_k))| <= osc log R_(k-4) for k = 4..11, because s_(k+1)/s_k = R_(k-4)(x_0) and r lies in [inf R_m, sup R_m]. Beats DO.3 at k = 4..10 by 1.0246, 1.0172, 1.0148, 1.0144, 1.0149, 1.0141, 5.8837. By DO.4 it is within 0.5% of the floor of every CF.3-form bound.
- DV.3: B_V(k) <= min(B_DO(k), B_U(k)) for every k >= 4, equality exactly at k = 13, 16 (exact rationals, k <= 389 directly; 8-periodic ratio in [1.0296, 10.266] for k >= 25).
- DV.3' (rejected, kept): the strict form fails at k = 13, 16.

## Why It Matters
Closes the last kept failure of the K_(2,6) level-sum line for small k and extends certified direct constants two levels further. It does not move the per-level rate (DU's 0.2380, spectral limit 0.1725).

## Derivation
DV.2 is elementary: |log R(x_0) - log r| <= log sup R - log inf R when r is in [inf R, sup R]. DV.3: CF.1 Birkhoff composition with DU.3's knapsack G_U over theta_n = tanh(Dbar_n/4); tail periodicity from G_U(j+8) = theta_8 G_U(j) on 8 consecutive j, which propagates because the knapsack recursion looks back at most 8 steps (checked by the archive, valid).

## Assumptions
CF.1; CF.3's proof (including r in [inf R_m, sup R_m]); DQ.1; DU.3's Dbar_3..Dbar_8 and DT.2's Theta_K uppers for m <= 5 used as stated (not re-run); DO.3's table; python-flint arb correctness. For k > 24 the script compares against B_U only (DO's knapsack table stops at 24), relying on DU.3's stated B_U < B_DO for k >= 14.

## New Results
Certified F_m in int K_(2,6) for m = 6, 7; two-sided Theta_K, osc rows m = 0..7; best-known level-sum bound B_V for every k >= 4 in this corpus.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012 (Hilbert-metric contraction); centred-form interval enclosure (Moore; Neumaier); Tucker 2011. Novelty of constants UNRESOLVED; no external first claimed or supported.

## Novelty Analysis
Method KNOWN. Constants new to the corpus.

## Falsification Attempts
- Repo witness: `python3 -m pytest -q tests/test_cli.py -k direct` (runs the default DV witness) 1 passed in 183.2 s on the archive box (repo states 166 s).
- Independent recomputation (mpmath, using the script's DO_UPPER/DO_PAIRS and the GASKET-printed osc uppers, own knapsack): B_DO(k)/osc_(k-4) = 1.02462, 1.0172, 1.01475, 1.01436, 1.01485, 1.0141, 5.88366 for k = 4..10, matching DV.2. At k = 11, B_DO/osc = 34.16 while the repo's 16.936 is against min(B_DO, B_U), consistent. PASS.
- Consistency: osc <= Theta_K row by row; m <= 5 Theta_K rows overlap DT.2's.
- Scope check: the k > 24 comparison uses B_U only (see Assumptions); not a flaw, but the "min(B_DO, B_U)" wording for large k rests on DU.3.
- DV_FULL=1 not run here.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated, conditional on DU.3/DT.2/DO.3 inputs.

## Patent Relevance
None.

## Related Discoveries
DISC-0232 (DT; kept failure DT.4 resolved), DISC-0233 (DU; factors used, placeholders filled), DISC-0229 (DQ; spectral limit 0.1725).

## Open Questions
Direct constants for m >= 8; sharper D_n (n >= 9); a non-CF.3-form bound beating osc log R_(k-4) at k = 4..11.

## Next Experiments
Run DV_FULL=1; certify D_9.

## Reproduction Instructions
Clone informational-flux-identity at 8ec657a289ec; `pip install python-flint numpy scipy sympy`; `python3 scripts/gasket_fractional_profile_level_direct_constants.py` (~3 min) or `python3 -m pytest -q tests/test_cli.py -k theorem_dv`.

## Evidence Log
- 2026-11-13 ~2:05 AM EST: repo test passed (183.2 s); independent DV.2 factor recomputation PASS.

## Change History
- 2026-11-13: created.
- note 2026-11-13 ~4:10 AM EST: open item 'direct constants for m >= 8' answered by IFI 49f0fa0349fc (Theorem DW, rows m = 8..12). DV.3' stays rejected for B_V; its strict form holds for the new B_W. See DISC-0235.

## Dated note (2026-11-13, ~7:05 AM EST)
Theorem DY (informational-flux-identity 91838c872b39; DISC-0237) beats this record's k = 9 direct row with a spectral level-sum bound (1.71790e-5 < 1.7204e-5, ratio 1.0014584); the k = 8 row stays the best bound. The original text above is preserved unchanged.
