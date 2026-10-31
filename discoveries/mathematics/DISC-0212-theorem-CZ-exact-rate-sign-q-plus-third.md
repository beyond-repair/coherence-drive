# Discovery: Theorem CZ — exact rate k·B*^k and sign of q^(k) + 1/3; q^(k) < −1/3 for every k ≥ 4 and |q^(k)| unimodal

## Discovery ID
DISC-0212

## Status
THEOREM in the mathematical sense only (computer-assisted, interval-certified). Method KNOWN (Schur complement / first-order eigenvalue perturbation along left eigenfunctionals of a composition operator, Neumann-series remainders). Constants UNRESOLVED as to novelty. Closes the open item of DISC-0211 (exact rate and sign of q^(k) + 1/3 for k ≥ 24). Second-order constant still OPEN. Not a flux, not thrust.

## Date Discovered
2026-10-31 (repo commit 02:30 EDT; indexed ~3:15 AM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 3e743609c293f1ba920b2af15946e21194732ae6

## Original Evidence
- GASKET.md §"Theorem CZ" (line 4480 at 3e743609c293)
- CLAIM_STATUS.md line 108
- scripts/gasket_fractional_profile_level_ratio_rate.py (new, 449 lines; imports CY's and CU's scripts)
- tests/test_cli.py (+31), scripts/cli.py (+1), README.md

## Discovery
In CY's frame L̃_k = C + E_k on H^∞(D), D = {|s − 9/5| < 4/5}, with Cf = f∘σ_1, E_k f = a_k·(f∘σ_2), a_k = G B^k, the left eigenfunctionals of C are δf = f(s*) (eigenvalue 1) and ℓf = f'(s*) (eigenvalue −1/3, right eigenvector the Koenigs function κ), s* = 3/2, t = σ_2(s*) = √21/2. Exact Schur identities λ_1 = −1/3 + ℓ(E_kκ) + ℓ(E_k w), λ_0 = 1 + a_k(s*) + δ(E_k w_0) with ℓ(E_k f) = a_k'(s*) f(t) + a_k(s*) f'(t)/(2t), a_k'(s*) = G*B*^k(k b_1 + g_1). Result (CZ.3), for every integer k ≥ 24:

|q^(k) + 1/3 − (α* k + γ*) B*^k| ≤ Err_k B*^k, α* = G* b_1 κ(t) = −0.0491613043141717, γ* = G*(g_1κ(t) + κ'(t)/(2t) + 1/3) = 0.179336821291891,

Err_k = 0.4151, 0.1316, 0.02475, 0.005054, 0.001086 at k = 24, 30, 40, 50, 60, Err_k/k → 0. Hence (q + 1/3)/(k B*^k) → α*. CZ.2 sharpens CX.3: |c_k − 1| ≤ 0.1058 (k = 24), 0.006823 (k = 40). CZ.4: q^(k) < −1/3 for every k ≥ 24. CZ.5: |q^(k)| strictly decreasing for k ≥ 30. CZ.6: CU's routine (circle radius 10^{−7}|ν_2|, Neumann power 24) certifies q^(24..29) inside the band, linking to CY.5. Corollary: q^(k) < −1/3 for every k ≥ 4; |q^(k)| strictly increases on 1..8 and strictly decreases to 1/3 for every k ≥ 8.

## Why It Matters
Ends the DISC-0206 → DISC-0211 second-eigenvalue chain with an exact asymptotic: the polynomial factor k comes from ∂_s(B^k) at the fixed point, and the sign of the leading coefficient (b_1 = B'/B(s*) < 0, κ(t) > 0) fixes q^(k) < −1/3. The whole profile of |q^(k)| over k ≥ 1 is now certified (unimodal, peak at k = 8).

## Derivation
Checked by hand: (i) C maps W = ker ℓ to itself because ℓ(Cw) = −ℓ(w)/3; (ii) the chain/product rule for ℓ(E_k f) with σ_2'(s*) = 1/(2t); (iii) q + 1/3 = N_k/λ_0 with N_k = λ_1 + 1/3 + (λ_0 − 1)/3 (direct algebra from q = λ_1/λ_0), whose first-order part is G*B*^k(kα' + γ' − 1/3) + G*B*^k/3 = G*B*^k(kα' + γ'), matching α*, γ*. (iv) The step 1 − 1/λ_0 ≤ λ_0 − 1 holds for λ_0 > 0. The reduction of CZ.4/CZ.5 to finite interval inequalities at k = 24 and 30 relies on monotonicity facts the repo states and checks (B*(1 + |b_1|/Λ_24) < 1 etc.); I did not re-prove those monotonicities.

## Assumptions
CY.1–CY.4 (DISC-0211) imported and re-run; CU.1–CU.3 (DISC-0207) at changed parameters for CZ.6 only; CY.5's |q^(23)| and CU.3/CV.5/CY.5–CY.6 values for the corollary. Standard: Schwarz–Pick and Cauchy bounds, maximum modulus, Neumann series.

## New Results
As above. Examples: q^(k) + 1/3 ∈ −6.7822·10^{−4} ± 6.9·10^{−5} (k = 30), −7.5405·10^{−5} ± 1.1·10^{−6} (k = 40), −7.5928·10^{−7} ± 3.0·10^{−10} (k = 60). Observation only (repo says so): the sign change of α*k + γ* at γ*/|α*| = 3.648 falls between k = 3 and 4, matching the certified sign change of q + 1/3; CZ's formula is not proved for k < 24.

## Prior Art
First-order (Rayleigh–Schrödinger / Schur-complement) perturbation of simple isolated eigenvalues (Kato, *Perturbation Theory*, II §2, IV §3); Koenigs eigenfunctions and spectra of composition operators (Koenigs 1884; Cowen–MacCluer 1995). Method KNOWN.

## Novelty Analysis
Textbook method; specific operator family and certified constants are corpus-specific. No literature search beyond this: UNRESOLVED.

## Falsification Attempts
- Independent check `scripts/indep_theorem_CZ.py` (no repo code; reuses my own DISC-0211 frame collocation for q^(k), and mpmath at 90 digits with my own orbit products for B, G, b_1, g_1 and my own Koenigs limit κ(s) = lim (−3)^n(σ_1^n(s) − s*)): **31/31 PASS**. All CZ.1 constants reproduced to < 5·10^{−14} (α*, γ* to < 5·10^{−15}); CZ.3 band holds at k = 24, 30, 40, 50, 60 with float residual/Err_k between 0.001 and 0.027 (the certified band is loose but correct); the three CZ.3 examples lie in their intervals; CZ.2 |c_k − 1| far inside w_0(k); q < −1/3 for k = 24..100 and |q| strictly decreasing for k = 23..70 (float); CZ.6's six values matched to < 10^{−9}.
- Kept failure of my own first run: κ evaluated as (−3)^150(σ_1^150(s) − s*) at 40 digits underflowed to 0 (cancellation), giving α* = 0 and spurious CZ.3 FAILs. Fixed by 90 digits and n = 75. Cause is my check, not the theorem.
- Float consistency: (q + 1/3)/(k B*^k) = −0.04617, −0.04692, −0.04737 at k = 60, 80, 100, matching α* + γ*/k (−0.04737 at k = 100), so the approach to α* is the predicted 1/k correction.
- Minor labelling note: the witness log prints CU's routine step as "CZ.4 (k = 24…)" whereas GASKET.md calls it CZ.6; same content, label mismatch only.
None of these is a proof; they confirm the certified numbers.

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (exact algebra + interval-certified constants, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0211 → DISC-0212 (mathematical): CY's kept limits (crude rate 0.8529, sign/monotonicity only k ≤ 23) closed. DISC-0210 → DISC-0212 (mathematical): CX.3's c_k bracket sharpened (CZ.2). DISC-0208 → DISC-0212 (mathematical): CV.6's rise on 1..8 completed to a certified unimodal profile. DISC-0207 → DISC-0212 (computational): CU's routine reused at new parameters for CZ.6.

## Open Questions
Second-order constant of q + 1/3; closed-form rate for Err_k; uniform-in-k rate for inf R_n^(k) (Γ_±^(k) via eigenvectors κ + w, 1 + w_0); circle eigenvalues; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Bound Γ_±^(k) from CZ's eigenvector representations; compute the next term (float residuals here are ~10^{−4}–10^{−3}·B*^k at k = 30..60, a target for a certified second-order constant).

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 3e743609c293; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_ratio_rate.py` (about 4 min; `CZ_SKIP_CU=1` skips CZ.6). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CZ.py` (about 1 s; numpy + mpmath; needs `indep_theorem_CY.py` beside it).

## Evidence Log
- 2026-10-31 ~3:08 AM EDT: independent check 31/31 PASS (after the documented κ-underflow fix).
- 2026-10-31 ~3:12 AM EDT: repo witness at 3e743609c293 EXIT 0 (204.6 s), 108 ok lines, "all Theorem CZ checks passed"; repo pytest not run (not claimed).

## Change History
- 2026-10-31: created from IFI 3e743609c293.
- 2026-10-31 (note, DISC-0213): the open item "uniform-in-k rate for inf R_n^(k) (Γ_±^(k) via eigenvectors κ + w, 1 + w_0)" is closed for k ≥ 29 by IFI Theorem DA (ed74f6de3998): Γ_±^(k) = ((2k+3)/12)κ_∓ + O(δ_k), κ_+ = 3κ_-. k = 13..28 remain open. This record's text above is unchanged.
