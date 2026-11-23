# Discovery: Theorem FA, EY's constants certified end to end (and EY.2's 0.127 found false by a hair)

## Discovery ID
DISC-0266

## Status
THEOREM (mathematical sense only) for FA.1–FA.3 and FA.5; FA.4 is an Arb certificate. KEPT FAILURE FA.1: the constant 0.127 used in EY.2 (DISC-0264) is false; the sharp value is 4 − √15 = 0.12701665…; EY.2 and EY.3 still hold after the correction. Method KNOWN (completing the square, Taylor-coefficient majorant, geometric series, Arb quadrature). Whether the constants are new is UNRESOLVED (no literature search; the method is textbook). The true 3^-n rate (EY.4) is still OBSERVED only.

## Date Discovered
2026-11-23. The commit is from 2:11 AM EST and was indexed at about 3:00 AM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3aa8369c57c815b7cdac882e98a022cf4c51fb1c (2026-11-23T07:11:55Z = 2026-11-23 2:11:55 AM EST). Parent: 3a6c5e27648d (Theorem EZ, DISC-0265).

## Original Evidence
- GASKET.md §Theorem FA (+30 lines) and an in-place annotation of EY.2 ("false by a hair … re-proved with it in Theorem FA"); the original EY.2 text is kept.
- scripts/gasket_fractional_corner_h_alpha_constants.py (new, 169 lines; python-flint arb, exit 1 on failure).
- CLAIM_STATUS.md (+2 rows: EY, FA); tests/test_flux_identity.py (+28 lines).

## Discovery
EZ (DISC-0265) left EY.2's float constants and the constant W(α−1)/6 + 1 uncertified. FA certifies them:
- FA.1 (exact): with g(y) = (5/3)(y+3)/(y+5), d log g/d log y = 2y/((y+3)(y+5)), and sup over y > 0 is c* = 4 − √15, because c*(y² + 8y + 15) − 2y = c*(y − √15)². KEPT FAILURE: EY.2 used 0.127 < c*; witness y = 39/10 gives 780/6141 = 0.1270151… > 0.127. Harmless: the bound needed is c*/10 = 0.0127 ≤ 0.05.
- FA.2: from EV.1 (a_1 = 1, a_2 = 1/20, 0 ≤ a_m ≤ 20^(1−m)), ψ(w) ≤ w·e^(w/10) on [0, 10] (so BJ.6 is no longer needed); the tail sum Σ_{j>n} log g(ψ(5^-j t)) ≤ (e^(1/100)/30)·t·5^-n = 0.033668…·t·5^-n ≤ 0.037·t·5^-n.
- FA.3: EY.2 re-proved: log(P/P_n) ≤ 0.0337x, and e^0.1 − 1 = 0.10517… < 0.106.
- FA.4 (Arb): W(−2) ∈ [11291.83348548641137405157, 11291.83348548641137405205].
- FA.5: EY.3 holds with constant W(Re α − 1)/6 + 1 ≤ W(−2)/6 + 1 ≤ 1882.97224758106857 for n ≥ 11 and −1 ≤ Re α ≤ 9/10. Statement correction: the constant is W(Re α − 1), not the complex W(α − 1) (this record's DISC-0264 entry already flagged that caveat).

## Why It Matters
It turns DISC-0264's rate into a fully certified explicit bound: |ρ^-n H_n(α) − W(α)/2| ≤ 1882.98·(2/5)^n on the strip for n ≥ 11, with every constant either exact or Arb-enclosed. It also documents a real (if harmless) error in EY.2's write-up, which this archive's DISC-0264 record had accepted without catching.

## Derivation
Re-derived by hand this run:
- FA.1: d log g/d log y = y/(y+3) − y/(y+5) = 2y/((y+3)(y+5)). Setting the derivative to zero gives y = √15, value 2√15/(30 + 8√15) = √15/(15 + 4√15) = 4 − √15 after rationalising. The square identity: c*(y² + 8y + 15) − 2y = c*y² − 2√15·c*·y + 15c* requires 8c* − 2 = −2√15c*, i.e. c*(8 + 2√15) = 2, c* = 1/(4 + √15) = 4 − √15. Correct.
- FA.2: ψ(w) ≤ w(1 + u/(1−u)) with u = w/20 ∈ [0, 1/2]; u/(1−u) ≤ e^(2u) − 1 on that interval (series comparison; equality only at 0). Then log g(y) ≤ 2y/15 (since d log g/dy = 2/((y+3)(y+5)) ≤ 2/15), and 5^-j t ≤ 2^-n/5 ≤ 1/10 for j > n and t ≤ (5/2)^n, so each term is ≤ (2/15)5^-j t e^(1/100) and Σ_{j>n} 5^-j = 5^-n/4. Gives e^(1/100)/30. Correct.
- FA.5: |∫ F τ^(-α-1)…| ≤ ∫ F τ^(-Re α-1)…, and W is decreasing on (−∞, α*] with α* ∈ (3/5, 7/10) (EX.2/EX.3), so on Re α − 1 ∈ [−2, −1/10] the maximum is W(−2). Correct.

## Assumptions
- EV.1 Taylor-coefficient bounds (DISC-0261), EX.2/EX.3 monotonicity and α* location (DISC-0263), EY.1/EY.3's reduction (DISC-0264), EZ's tail (DISC-0265), all as stated in the repository.
- python-flint Arb correctness for FA.4.

## New Results
- EY.3 (DISC-0264) is now certified end to end with C ≤ 1882.97224758106857.
- EY.2's 0.127 is replaced by the exact 4 − √15.
- BJ.6 is no longer a dependency of EY.

## Prior Art
Elementary analysis and interval quadrature; textbook. No external search.

## Novelty Analysis
Method KNOWN. Statement specific to this repository's construction; novelty UNRESOLVED.

## Falsification Attempts
- Ran the repository's script at 3aa8369: all FA checks passed, exit 0, 16.6 s.
- Independent mpmath check (/workspace/corpus-discovery/fa_check.py, 30 digits, reusing this archive's own W quadrature from ex_check.py): W(−2) = 11291.83348548641137405181, inside FA.4's bracket; C = 1882.9722475810685623; c* = 0.127016653792583; witness 780/6141 = 0.1270151441 > 0.127 confirmed (so the KEPT FAILURE is real); grid max of 2y/((y+3)(y+5)) on (0, 20) = 0.1270166537920 ≤ c*; min of e^(2u) − 1 − u/(1−u) on a 1000-point grid of (0, 1/2] is positive; e^(0.01)/30 = 0.0336683389, e^0.1 − 1 = 0.1051709181; W(−0.1) = 2.1777 < W(−1) = 71.80 < W(−2), consistent with monotonicity.
Nothing broke beyond the kept failure the repository itself records.

## Experimental Validation
Not applicable (pure mathematics). Arb certificate in-repo; independent mpmath reproduction above.

## Mathematical Status
THEOREM (FA.1–FA.3, FA.5), certified computation (FA.4), KEPT FAILURE (EY.2's 0.127).

## Patent Relevance
None.

## Related Discoveries
- DISC-0264 (Theorem EY): FA certifies EY.2/EY.3's constants and finds EY.2's 0.127 false. Label: mathematical.
- DISC-0265 (Theorem EZ): FA closes EZ's remaining open item. Label: mathematical.
- DISC-0261 (Theorem EV): EV.1 is FA.2's input. Label: mathematical.
- DISC-0263 (Theorem EX): EX.2/EX.3 monotonicity used in FA.5. Label: mathematical.

## Open Questions
Prove the true 3^-n rate (EY.4); extend the strip beyond [−1, 9/10]; sharpen C (the true constants observed in DISC-0264 are 304.7 at α = −1, far below 1882.98).

## Next Experiments
Attempt a 3^-n rate via a second-order expansion of P/P_n; Arb-certify the observed limiting constants.

## Reproduction Instructions
In informational-flux-identity @ 3aa8369c57c8: `python3 scripts/gasket_fractional_corner_h_alpha_constants.py` (needs python-flint). Independent: fa_check.py (local to the research box, not committed).

## Evidence Log
- 2026-11-23 ~3:00 AM EST: repository script passed (exit 0); fa_check.py results above.

## Change History
- 2026-11-23 ~3:00 AM EST: created (THEOREM FA.1–FA.3, FA.5; Arb FA.4; KEPT FAILURE EY.2's 0.127; method KNOWN, constants UNRESOLVED).
