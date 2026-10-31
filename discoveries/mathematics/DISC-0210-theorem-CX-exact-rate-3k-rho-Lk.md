# Discovery: Theorem CX — exact rate of 3^(k+1)ρ(L_k) − 1 and monotonicity of 3^k ρ(L_k) for every k

## Discovery ID
DISC-0210

## Status
THEOREM in the mathematical sense only (computer-assisted, interval-certified). Method KNOWN (renewal-series test function + Collatz–Wielandt). Constants B*, G* UNRESOLVED as to novelty. q^(k) → −1/3 still HEURISTIC. Not a flux, not thrust.

## Date Discovered
2026-10-30 (repo commit 22:59 EDT; indexed ~11:10 PM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 4dc70c635d0b

## Original Evidence
- GASKET.md §"Theorem CX" (line 4387 at 4dc70c635d0b)
- CLAIM_STATUS.md line 106
- scripts/gasket_fractional_profile_level_rate_k.py (new, 326 lines; imports CW's script)
- tests/test_cli.py (+36)

## Discovery
With CW's conjugation L_k(h_k f) = 3^{−k−1} h_k L̃_k f, L̃_k f = f∘σ_1 + a·f∘σ_2, a = G B^k, the renewal test function u_ε = Σ_{n≥0} (1+ε)^{−n−1} a∘σ_1^n satisfies exactly L̃_k u_ε = (1+ε)u_ε + a(u_ε∘σ_2 − 1). So Collatz–Wielandt brackets ε_k = 3^{k+1}ρ(L_k) − 1 by whether sup/inf of u_ε over Y = σ_2(X) cross 1. Results: B* = B(3/2) = 0.77737602763333190375, G* = 0.28706524176038901924; c_k = ε_k/(G* B*^k) is bracketed for k = 0..40 and lies in [0.98, 1.02] for every real k ≥ 40; c_k → 1 (exact geometric rate B*), and 3^k ρ(L_k) strictly decreases to 1/3 for every integer k ≥ 0.

## Why It Matters
Collapses DISC-0209's rate bracket [0.5999, 0.8352] to the single value B* and closes DISC-0209's open item (monotonicity for k ≥ 13), extending DISC-0208's CV.7 from k ≤ 12 to all k.

## Derivation
Telescoping: (1+ε)u_ε = u_ε∘σ_1 + a, so L̃_k u_ε = u_ε∘σ_1 + a u_ε∘σ_2 = (1+ε)u_ε + a(u_ε∘σ_2 − 1). Since a > 0 and h_k u_ε > 0, sup_Y u_ε ≤ 1 ⇒ ρ(L_k) ≤ 3^{−k−1}(1+ε) and inf_Y u_ε ≥ 1 ⇒ ρ(L_k) ≥ 3^{−k−1}(1+ε). The tail of u_ε is ≈ G* B*^k/ε because σ_1^n t → s* = 3/2, which forces ε_k ~ G* B*^k. Checked by hand: the identity is exact algebra; B* = (3/√21)e^{Φ(√21/2)} since σ_2(3/2) = √21/2 and Φ(3/2) = 0; θ_0 = (3−√5)/2 = 1/(σ_1(5/2)+3/2) is the worst contraction factor of |σ_1x − s*| = |x − s*|/(σ_1x + 3/2).

## Assumptions
CW.1–CW.2 as certified in DISC-0209 (re-run unchanged by the CX script). For CX.5 only: CE/CT/CU/CV's certified ρ(L_k), k ≤ 12.

## New Results
CX.1–CX.5 as above; e.g. ρ(L_13) ∈ [2.113399, 2.113510]·10^{−7}, ρ(L_20) ∈ [9.577739, 9.577786]·10^{−11}, ρ(L_39) ∈ [8.2253915, 8.2253916]·10^{−20}; ε_{k+1}/ε_k ≤ 0.81359 for k ≤ 39 and ≤ 0.80911 for k ≥ 40.

## Prior Art
Collatz–Wielandt min-max (Collatz 1942; Wielandt 1950; Krasnosel'skii cones). Renewal/Neumann-series test functions and Koenigs-type asymptotics for weighted composition operators near an attracting fixed point (Cowen–MacCluer). Ruelle–Perron–Frobenius pressure asymptotics in a zero-temperature limit (dominant branch through a fixed point) are the standard analogue. Method KNOWN.

## Novelty Analysis
The method is standard. What is specific is the operator (the combinatorial-gasket level-sum transfer operator's k-th derivative family) and its certified constants B*, G*; no prior evaluation of these constants was found, but no literature search beyond this was done: UNRESOLVED.

## Falsification Attempts
- Repo witness re-run: EXIT 0, 10.7 s; repo tests 3 passed (331 s).
- Independent v1 (float Chebyshev collocation, numpy eigvals): FAILED for k ≳ 25 (c_39 ≈ 9·10^4). Cause: my check, not the theorem: branch weights span (2σ)^{−k} from 3.24^{−k} to 2.24^{−k}, the non-normal float matrix is ill-conditioned. Kept as `scripts/indep_theorem_CX_v1_float_failed.py`.
- Independent v2 (mpmath 60 digits, collocation N = 56, power iteration, no repo code): B*, G* to 1e-19, closed form for B*; every listed c_k inside the CX.2 brackets (c_0 = 0.94471159, c_13 = 0.99827247, c_20 = 1.00122335, c_39 = 1.00009217, c_40 = 1.00007731); ρ(L_13), ρ(L_39) inside brackets; 3^k ρ strictly decreasing k = 0..40; max ε_{k+1}/ε_k = 0.784309 < 0.81359. 44 PASS; 9 failures were my own N = 40 vs N = 56 stability tolerance at k ≥ 32.
- v3 resolution check (N = 56 vs 72, k = 30..40): agreement ≤ 9.1e-19 relative in ε_k; v2's failures are discretisation at N = 40 only.
None of these is a proof; they confirm the certified numbers.

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (exact construction + interval-certified constants, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0209 → DISC-0210 (mathematical): CW's kept limit (rate bracket) collapsed to B*; CW's open item (k ≥ 13 monotonicity) closed. DISC-0208 → DISC-0210 (mathematical): CV.7 extended to all k. DISC-0206, DISC-0207, DISC-0208 → DISC-0210 (mathematical): CX.5 consistency.

## Open Questions
q^(k) → −1/3 (needs a signed test function for ν_2); uniform-in-k rate for inf R_n^(k); the next term of c_k − 1 (floats show c_k < 1 for k ≤ 13 crossing above 1 by k = 20, then decreasing toward 1); CF.3 general-f constant; circle eigenvalues; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Second-order renewal expansion to get c_k = 1 + d·β^k + …; locate the sign change of c_k − 1 (between k = 13 and 20) with certified brackets.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 4dc70c635d0b; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_rate_k.py` (about 11 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CX.py` (about 20 s) and `indep_theorem_CX_resolution.py` (about 13 s).

## Evidence Log
- 2026-10-30 ~11:00 PM EDT: repo witness EXIT 0 (10.7 s), all CX checks ok; repo tests 3 passed, 60 deselected.
- Independent v1 float FAILED (documented); v2 44/53 with the 9 failures traced to N = 40; v3 0 unstable at N = 56 vs 72.

## Change History
- 2026-10-30: created from IFI 4dc70c635d0b.
- 2026-10-31 (note, DISC-0211): the kept limit "q^(k) → −1/3 still HEURISTIC" is proved by IFI Theorem CY (54ed04084f2e), with |q^(k) + 1/3| ≤ 4.8271·0.8529^k + 0.0958·0.8352^k for k ≥ 24 and CU-certified values for k = 13..23. This record's text above is unchanged.
