# Discovery: Theorem DU, sharper certified D_7, D_8 on the second-order cone K_(2,6)

## Discovery ID
DISC-0233

## Status
THEOREM (mathematical sense only; computer-assisted, arb-certified; method KNOWN; constants UNRESOLVED). Answers DISC-0232's open item "sharper D_7, D_8". Kept failure DT.4 (k = 4..10) unchanged.

## Date Discovered
2026-11-12 (indexed ~11:59 PM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 95fbcc0b3ddfa59cf4952bb220b5346d4eea8d3d (2026-11-12 11:02 PM EST).

## Original Evidence
- GASKET.md §Theorem DU (line 5435; NOT THIS disclaimer at line 5466).
- CLAIM_STATUS.md (row at line 129, Theorem DU); README.md (+3/-1).
- scripts/gasket_fractional_profile_level_fine_diameters.py (new, 361 lines; imports DR's and DT's scripts); registered in scripts/cli.py; tests/test_cli.py (+31 lines).

## Discovery
- DU.1 (proved, elementary): with several positive reference functionals r_k, R(l,l') <= R(l,r_k) R(r_k,l'), so D_n <= max_(l,l') min_k (p_k(l) + p_k(l')), p_k(l) = log R(l,r_k) R(r_k,l). DR.3 is the one-reference case with the factor 2.
- DU.2 (certified): references delta_(9/5) and delta_(47/20) composed with Lt^n, 800 cells (n = 7) and 1600 cells (n = 8), DR.1/DR.2 chains replayed in arb: D_7 <= 0.00023483, D_8 <= 0.000041213 (DR.3: 0.00041195, 0.00017542). Worst pair joins the two ends of X.
- DU.3: per-level rate theta_8^(1/8) <= 0.2380246 (DT: 0.2694000); envelope tanh(D_n/4) <= 9.61008 * 0.2380246^n for n >= 5; tanh(D_n/4)^(1/n) <= 0.3060650 for every n >= 5 (DR.4: 0.3135158). DT.3's level-sum bound re-derived: B_U <= B_K for every k, strictly for k = 11, 12 and every k >= 14 (2.34x at k = 22, 1.29e5x at k = 103); equal for k <= 10 and k = 13.
- DU.4 (certified lower bounds): explicit f = exp(alpha s + beta s^2), g in K_(2,6) give D_7 >= 6.428e-5, D_8 >= 1.109e-5, so the uppers are within factors 3.65 and 3.72.

## Why It Matters
Tightens the certified contraction rate of the level sums on K_(2,6) from 0.2694 to 0.2380 per level, and for the first time in this line encloses D_7, D_8 two-sidedly. Still far from the spectral limit 0.1725 (DQ.4).

## Derivation
Hilbert projective metric read through Lambda = {2delta ± delta', 6delta ± delta''}; triangle inequality for the sup-ratio through a reference; DR.2 cell lemma (convexity in tau) on finer grids; CF.1 Birkhoff composition D_(a+b) <= theta_a D_b; CF.3/DT.3 telescoping.

## Assumptions
DR.1, DR.2 unchanged; CF.1; DQ.1; DR.3's D_3, D_5, D_6 and DS.3's D_4 used as stated (not re-run by DU); DT.2's Theta_K uppers used as stated; DT.3's proof/code; correctness of python-flint arb. The default witness certifies only the 5 end/middle cells per n; all-cell certification is DU_FULL=1 (repo reports all cells passed, 16032 s; not reproduced here).

## New Results
D_7 <= 0.00023483, D_8 <= 0.000041213 (two-sided within ~3.7x); per-level rate 0.2380246; uniform n >= 5 bound 0.3060650; sharper level-sum bound B_U.

## Prior Art
Birkhoff 1957; Bushell 1973; Liverani 1995; Lemmens–Nussbaum 2012 (Hilbert-metric cone contraction); multi-reference/triangle bounds in the projective metric are standard. Interval certification standard (Moore; Tucker 2011). Novelty of the constants UNRESOLVED; no external first claimed or supported.

## Novelty Analysis
Method KNOWN. Constants new to the corpus.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_fine_diameters.py` (default cells) EXIT 0, "all Theorem DU checks passed", 37.3 s elapsed on the archive box. Printed D_7 <= 0.00023482991, D_8 <= 4.1212584e-5 over the default cells; theta_8^(1/8) <= 0.23802456; DU.4 lower bounds 6.42826e-5, 1.10917e-5; DT.3/DT.4 checks re-run green.
- Independent composition check (mpmath, from the script's DBAR_DR values and DU's stated D_7, D_8): theta_7^(1/7) = 0.24861519, theta_8^(1/8) = 0.23802456, tanh(D_8/4) = 1.0303250e-5, all matching. The uniform n >= 5 bound recomputes to 0.30606499 and is attained at n = 9 via the split D_9 <= theta_4 D_5 (DS.3 + DR.3), so the improvement 0.3135158 -> 0.3060650 over DR.4 comes from DS's D_4, not from DU.2's new D_7, D_8. Attribution nit only; the number is correct. With the 5-digit rounded D values printed in DR's commit the same split gives 0.3060653 (> 0.3060650); the script's more precise uppers are needed. PASS.
- Consistency: DU.4 <= DU.2 <= DR.3 for n = 7, 8; per-level values above DQ.4's 0.1725476.
- Documentation nit: GASKET.md line 5468 still contains unfilled template placeholders "about FULLTIME" and "FULLRUN", and line 5470 "about DEFTIME" (the commit message gives 16032 s full and ~75 s default; test docstring says ~4.5 h and ~1.5 min). Same kind of placeholder DT fixed for DS.
- DU_FULL=1 (all 800 + 1600 cells, ~4.5 h) not run here.

## Experimental Validation
None applicable (pure mathematics). Not thrust; no flux; Stage 2 still blocked (no Psi_info).

## Mathematical Status
Theorem (computer-assisted) as stated in the repository, conditional on DR.3/DS.3 diameters and DT.2's uppers; all-cell certification per repo's DU_FULL run.

## Patent Relevance
None.

## Related Discoveries
DISC-0232 (DT, open item answered; level-sum bound re-derived), DISC-0231 (DS, D_4 drives the uniform bound), DISC-0230 (DR, chain/cell lemmas, single-reference case), DISC-0229 (DQ, spectral limit 0.1725).

## Open Questions
Certified D_n for n >= 9 (repo float probes ~5.4e-6, 2.9e-6 at end cells); DS.2 value-function certificate at n = 7, 8 to close the factor ~3.7; other invariant K_(a,b) for m = 0, 1 constants (DT.4); direct constants for m >= 6.

## Next Experiments
Run DU_FULL=1 on the archive box and record; certify D_9.

## Reproduction Instructions
Clone informational-flux-identity at 95fbcc0b3ddf; `pip install python-flint numpy scipy sympy`; `python3 scripts/gasket_fractional_profile_level_fine_diameters.py` (~40-75 s) or `DU_FULL=1 ...` (~4.5 h, 6 processes); or `python3 -m pytest -q tests/test_cli.py -k theorem_du`.

## Evidence Log
- 2026-11-12 ~11:59 PM EST: repo witness EXIT 0 (37.3 s, default cells); independent composition check PASS (attribution and placeholder nits noted).

## Change History
- 2026-11-12: created.
- note 2026-11-13 ~2:05 AM EST: GASKET placeholder nit closed by IFI 8ec657a289ec (DU_FULL 16032 s, default ~75 s now filled). See DISC-0234.
