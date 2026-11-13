# Discovery: Theorem DB — exact rate of inf R_n^(k) → ρ(L_k) for k = 13..28, closing DA's gap so CT.5's two-sided bound holds for every k ≥ 1

## Discovery ID
DISC-0214

## Status
THEOREM in the mathematical sense only (computer-assisted, interval-certified, run locally, not in CI). Method KNOWN (CU's certified Galerkin/Krawczyk/Riesz-projection pipeline, DISC-0207, re-run unchanged on the rescaled operator 3^(k+1)L_k at 1024 bits). Constants UNRESOLVED as to novelty. Closes DISC-0213's kept limit (k = 13..28). Second-order terms still OPEN. Not a flux, not thrust.

## Date Discovered
2026-10-31 (repo commit 05:53 EDT; indexed ~6:30 AM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 22711f251b7ad1854886a8d27a303f4a2f350170

## Original Evidence
- GASKET.md §"Theorem DB" (+38 lines at 22711f251b7a)
- CLAIM_STATUS.md (+1 row)
- scripts/gasket_fractional_profile_level_infrate_mid.py (new, 276 lines; imports CU's `gasket_fractional_profile_level_infrate_k.py` unchanged)
- tests/test_cli.py (+28), scripts/cli.py (+1), README.md

## Discovery
CU's script is run unchanged per k on L̂_k = 3^(k+1)L_k (every quantity CU.5 compares is homogeneous of degree 0, so rescaling by an exact integer changes nothing but keeps numbers O(1)). The repo diagnoses CZ's "underflow for k ≥ 30" as interval wrapping in the Neumann powers, not underflow, and fixes it with 1024-bit balls. N(k) = 60 + 10k for k = 14..19, max(180, 30 + 10k) otherwise; at N = 30 + 10k the k = 14..19 runs failed CU.4's 10^−12 projection-error threshold (kept failure, recorded in GASKET.md), fixed by more modes, not a looser threshold.

- DB.1–DB.3: two real simple eigenvalues outside ρ_in = 0.6|ν_2| for each k = 13..28; q^(13) = −0.349942106203, q^(20) = −0.338508371108, q^(28) = −0.334370141255.
- DB.4: Γ_+^(k) = 0.887577 … 1.82873, Γ_-^(k) = 2.53383 … 5.469.
- DB.5: CT.5's two-sided bound for every n ≥ n_0(k), n_0 = 48..100: exact rate |q^(k)|.
- DB.6: Γ_±/((2k+3)/12 κ_∓) within 2% of 1 for k ≥ 19 (0.99033, 0.94239 at k = 13).
- DB.7: Γ_± strictly increasing on k = 1..28.
- Corollary (CT, CU, CV, DB, DA): inf R_n^(k) → ρ(L_k) at the exact rate |q^(k)| for every integer k ≥ 1.

## Why It Matters
It closes the last finite gap in the k-family: together with DISC-0206/0207/0208 (k ≤ 12) and DISC-0213 (k ≥ 29), the rate statement is now certified for every k ≥ 1. It also shows DA's first-order formula is already within 2% from k = 19, where DA's own error bound is void.

## Derivation
Checked by hand: homogeneity of q, B/A, Γ_±, θ_n under L → cL (c = 3^(k+1)), and ρ̂ − inf R̂_n = c(ρ − inf R_n). The interval enclosures are machine computations I did not re-derive; I re-ran them (Evidence Log) and reproduced the values independently (Falsification Attempts).

## Assumptions
Everything CU uses (imported unchanged); DA.1's κ_- = 0.370860305428934 ± 10^−14 (DB.6 only); CT.4/CU.4/CV.4's Γ_± for k ≤ 12 (DB.7 only); CY.5/CZ.6's q (consistency only).

## New Results
As above. Arithmetic check of DB.6 from the published Γ_± lists (mine): ratios + rise 0.99033 → 1.00335 (k = 24–25) → 1.00293; ratios − rise monotonically 0.94239 → 0.99978. DB.7's strict increase on 12 → 28 confirmed from the published values with CV.4's k = 12 values.

## Prior Art
Same as DISC-0207/DISC-0213: Ruelle–Perron–Frobenius ratio convergence with rate |λ_2/λ_1| and constant from the second Riesz projection (Baladi 2000; Kato); validated numerics with Krawczyk enclosures (Moore, Krawczyk; Tucker, *Validated Numerics*, 2011). Method KNOWN.

## Novelty Analysis
No new method: a parameter/precision change to an existing certified routine. The certified constants are corpus-specific. Novelty UNRESOLVED (no literature search beyond this).

## Falsification Attempts
- Independent check `mathematics/scripts/indep_theorem_DB.py` (own code, no repo imports; mpmath Chebyshev collocation of L̂_k on X with barycentric interpolation, right eigenvectors and inverse-eigenvector left functionals, Γ_± = max_X(±B/A) on a 401-point grid): **9/9 PASS** at k = 13, 20, 28, stable between (M, dps) = (60, 60) and (90, 80). q matches to 13 digits; Γ_+ = 0.88757698, 1.3314028, 1.8287341; Γ_- = 2.5338273, 3.9330325, 5.469188 (repo 0.887577, 1.331403, 1.82873; 2.53383, 3.9330, 5.469); DB.6 ratios reproduced (0.990328/0.942386 at k = 13; 1.00293/0.999817 at k = 28).
- Kept failure of my own first attempt: estimating Γ_± by power iteration at n = 138–139 with 60 digits gave garbage (|q|^n ≈ 10^−63, below working precision). Cause is my check, not the theorem; replaced by the spectral decomposition above.
- Not checked independently: n_0(k) and θ_n (interval Neumann bounds).

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (interval-certified, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0213 → DISC-0214 (mathematical): DA's kept limit k = 13..28 closed; DA.1's κ_- used in DB.6. DISC-0207 → DISC-0214 (computational): CU's routine re-run unchanged at 1024 bits. DISC-0208 → DISC-0214 (mathematical): CV.4's Γ_± used in DB.7. DISC-0211/DISC-0212 → DISC-0214 (computational): CY.5/CZ.6's q used for consistency. DISC-0206 → DISC-0214 (mathematical): CT.5's bound.

## Open Questions
Second-order terms of Γ_±^(k) − ((2k+3)/12)κ_∓ and of q^(k) + 1/3; n < n_0(k); closed forms; circle eigenvalues; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Fit the float decay of Γ_± − first order across k = 13..100 to target a certified second-order constant; check whether the repo's 1024-bit fix extends CU's routine past k = 30 (it would give a second, independent certification of DA's range).

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 22711f251b7a; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_infrate_mid.py` (about 27 min on 8 processes). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DB.py 60 60` (about 1.5 min).

## Evidence Log
- 2026-10-31 ~6:20 AM EDT: repo witness at 22711f251b7a EXIT 0 ("elapsed 869.4s", 387 ok lines, 0 failures, "all Theorem DB checks passed") on 8 processes; faster than the stated ~27 min, no content discrepancy. Repo pytest not run (would repeat the same 15-min computation).
- 2026-10-31 ~6:10 AM EDT: independent check 9/9 PASS at (60, 60) and (90, 80), after the documented power-iteration failure.

## Change History
- 2026-10-31: created from IFI 22711f251b7a.
