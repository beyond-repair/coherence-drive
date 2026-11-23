# Discovery: Theorem CY — q^(k) = ν_2^(k)/ρ(L_k) → −1/3 with an explicit geometric rate; ν_2^(k) real, simple, isolated for every k

## Discovery ID
DISC-0211

## Status
THEOREM in the mathematical sense only (computer-assisted, interval-certified). Method KNOWN (Koenigs linearisation of a composition operator + Neumann-series resolvent bound + Kato continuity of Riesz projections). Constants UNRESOLVED as to novelty. The heuristic q^(k) → −1/3 carried by DISC-0208/0209/0210 is now proved. Exact rate and sign of q^(k) + 1/3 for k ≥ 24 remain OPEN (float observation only). Not a flux, not thrust.

## Date Discovered
2026-10-31 (repo commit 01:35 EDT; indexed ~2:15 AM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 54ed04084f2e5ebff865067106d251214d4905be

## Original Evidence
- GASKET.md §"Theorem CY" (line 4428 at 54ed04084f2e)
- CLAIM_STATUS.md line 107
- scripts/gasket_fractional_profile_level_ratio_k.py (new, 493 lines; imports CU's script for CY.5)
- tests/test_cli.py (+37), scripts/cli.py (+1), README.md

## Discovery
Continuing CW's h_k holomorphically as h_k = P_0 P_1^k (convergent orbit products along σ_1 to s* = 3/2) gives exactly 3^{k+1} h_k^{−1} L_k h_k = C_1 + (G B^k) C_2, C_i f = f∘σ_i. On H^∞(D), D = {|s − 9/5| < 4/5}, the Koenigs function κ = (s − s*)∏ 3/(σ_1(x_j) + 3/2) satisfies κ∘σ_1 = −κ/3, so C_1 = 1 ⊕ (−1/3) ⊕ C_1|_{V_2}. Certified sups (sup_D|B| < 0.8529, sup_D|G| < 0.3572, ‖κ‖ < 1.2426, resolvent constant A < 91.40) and a Kato homotopy give, for every integer k ≥ 24, exactly two eigenvalues of L_k in |z| ≥ (9/40)3^{−k−1}, both real and simple, with |3^{k+1}ν_2^(k) + 1/3| ≤ 4.8271·0.8529^k and |q^(k) + 1/3| ≤ 4.8271·0.8529^k + 0.0958·0.8352^k; uniform gap |ν/ν_2| < 0.9897. CY.4 transfers the spectrum to CG's H^2(D_CG); CY.5 (CU's routine, unchanged) certifies k = 13..23; CY.6: |q^(k)| strictly decreasing and > 1/3 for k = 8..23.

## Why It Matters
Closes the last open item of the DISC-0206 → DISC-0210 chain about the second eigenvalue: together with CG/CT/CU/CV, ν_2^(k) is a real, simple, negative, isolated eigenvalue for every k ≥ 0, and q^(k) → −1/3 = σ_1'(s*). The limit is exactly what the Koenigs eigenvalue of the dominant branch predicts.

## Derivation
Telescoping identities P_0∘σ_1 = P_0/(3w̃_1), P_1∘σ_1 = P_1·2σ_1/3, κ∘σ_1 = −κ/3 (from σ_1(x) − 3/2 = −(x − 3/2)/(σ_1(x) + 3/2)) give the frame identity. C_1's splitting f = f(s*) + f'(s*)κ + g, g ∈ V_2, is invariant; Schwarz's lemma bounds C_1^n on V_2. ‖M_a C_2‖ ≤ η_k = sup|G|·(sup|B|)^k → 0, so the perturbation is small and the Riesz projections keep rank 1 near 1 and near −1/3. Reality from the symmetry f ↦ conj(f(conj s)). Checked by hand: the κ identity and κ'(s*) = 1; the q-bound decomposition q + 1/3 = (λ_1 + 1/3)/λ_0 + (λ_0 − 1)/(3λ_0) with CW.3's λ_0 bound gives the 0.2873/3 term.

## Assumptions
CW.3 (DISC-0209) only to pass from ν_2 to q. CU.1–CU.3 (DISC-0207), run unchanged, for CY.5. CV.5 (DISC-0208) and CX.2 (DISC-0210) brackets for CY.6 only. Standard: Schwarz/Schwarz–Pick, Montel compactness, Kato's rank continuity of Riesz projections.

## New Results
CY.1–CY.6 and the Corollary as above; e.g. |q^(k) + 1/3| ≤ 0.1073 at k = 24, 2.430·10^{−3} at k = 40, 9.440·10^{−5} at k = 60; q^(13) = −0.349942106203, q^(23) = −0.33622604.

## Prior Art
Koenigs' linearisation theorem and the spectrum {λ^n} of composition operators with an interior attracting fixed point (Koenigs 1884; Kamowitz; Cowen–MacCluer, *Composition Operators on Spaces of Analytic Functions*, 1995). Perturbation of isolated eigenvalues via Riesz projections (Kato, *Perturbation Theory*, IV §3). Weighted transfer operators in a zero-temperature-like limit where one branch dominates are a standard analogue. Method KNOWN.

## Novelty Analysis
The method is textbook. Specific to this corpus: the operator family and the certified constants. No prior evaluation found, but no literature search beyond this: UNRESOLVED.

## Falsification Attempts
- Repo witness re-run at 54ed04084f2e: see Evidence Log.
- Independent v1 (`scripts/indep_theorem_CY_v1_direct_float_failed.py`, direct float Chebyshev collocation of 3^{k+1}L_k): 111/128; FAILED for k ≳ 31 (N = 70 vs 90 unstable; at k ≥ 56 eigenvalue garbage). Cause is my check (same ill-conditioning as DISC-0210's v1), not the theorem; agreement with CY.5 for k = 13..23 and with CY.3's bound for k = 24..55 held.
- Independent v2 (`scripts/indep_theorem_CY.py`, my own orbit products for G, B on X, collocation of C_1 + diag(GB^k)C_2, cross-checked against direct collocation for k ≤ 25; no repo code): 182/182 PASS. CY.5's |q^(13..23)| to < 2·10^{−8}; CY.6 monotonicity; CY.3's bound, |λ_3| < 9/40, |λ_0 − 1| < 1/2 for every k = 24..80; the repo's float observation (q + 1/3 at k = 23, 30, 40) reproduced to < 10^{−3} relative; B*, G* to 10^{−13}.
- Float observation (no claim): q^(k) + 1/3 < 0 for all k = 8..80; successive ratios 0.7987, 0.7912, 0.7877 at k = 40, 60, 79 vs B*(1 + 1/k) = 0.7968, 0.7903, 0.7872 — consistent with the repo's suggested k·B*^k law. The certified rate 0.8529 is crude, as the repo itself states.
None of these is a proof; they confirm the certified numbers.

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (exact construction + interval-certified constants, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0210 → DISC-0211 (mathematical): CX's kept limit (q^(k) → −1/3 heuristic) proved. DISC-0209 → DISC-0211 (mathematical): CW's h_k continued holomorphically as the conjugating frame; CW.3 used for q. DISC-0208 → DISC-0211 (mathematical): CV's q → −1/3 observation proved; CV.6's decreasing half extended to k = 8..23. DISC-0207 → DISC-0211 (computational): CU's routine reused for CY.5. DISC-0206 → DISC-0211 (mathematical): CT's isolation statement extended to every k.

## Open Questions
Exact rate and sign of q^(k) + 1/3 for k ≥ 24 (first-order perturbation in CY's frame; floats suggest −C·k·B*^k); uniform-in-k rate for inf R_n^(k) (Γ_± not tracked in k); next term of c_k − 1; circle eigenvalues; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Certified first-order formula for 3^{k+1}ν_2 + 1/3 = ⟨κ-coefficient of a C_2 κ⟩ + O(η_k^2) to get the exact k B*^k constant and the sign for all k; bound Γ_±^(k) from CY.3's resolvent.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 54ed04084f2e; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_ratio_k.py` (about 8 min; `CY_KS=` empty skips CY.5/CY.6). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CY.py` (about 1 s, numpy).

## Evidence Log
- 2026-10-31 ~2:10 AM EDT: independent v1 111/128 (documented failure), v2 182/182 PASS.
- 2026-10-31 ~2:20 AM EDT: repo witness at 54ed04084f2e EXIT 0 (7 min 27 s), 183 ok lines, 'all Theorem CY checks passed'; repo pytest subset started but not finished within this run (not claimed).

## Change History
- 2026-10-31: created from IFI 54ed04084f2e.
- 2026-10-31 (note, DISC-0212): the open item "exact rate/sign of q^(k) + 1/3 for k ≥ 24" is closed by IFI Theorem CZ (3e743609c293): (q + 1/3)/(k B*^k) → α* = −0.0491613043, q^(k) < −1/3 for every k ≥ 4, |q^(k)| strictly decreasing for k ≥ 8. The float observation "−C·k·B*^k" above is confirmed with C = |α*|. This record's text above is unchanged.
