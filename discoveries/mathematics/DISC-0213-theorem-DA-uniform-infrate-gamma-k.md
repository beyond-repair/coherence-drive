# Discovery: Theorem DA — uniform-in-k rate for inf R_n^(k) → ρ(L_k); CU.4's constants Γ_±^(k) = ((2k+3)/12)·κ_∓ + O(δ_k) for every k ≥ 29

## Discovery ID
DISC-0213

## Status
THEOREM in the mathematical sense only (computer-assisted, interval-certified). Method KNOWN (left/right eigenvectors of a Schur-complemented composition operator, rank-one Riesz projections, Neumann-series remainders, Collatz–Wielandt two-sided bound of CT.5). Constants UNRESOLVED as to novelty. Closes, for k ≥ 29, the open item carried by DISC-0207, DISC-0208, DISC-0211 and DISC-0212 ("Γ_±^(k) uniformly in k"). k = 13..28 still OPEN; second-order term still OPEN. Not a flux, not thrust.

## Date Discovered
2026-10-31 (repo commit 03:20 EDT; indexed ~4:10 AM EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit ed74f6de3998d3ccfbc7f85f754d847e0c27489f

## Original Evidence
- GASKET.md §"Theorem DA" (+62 lines at ed74f6de3998)
- CLAIM_STATUS.md (+1 row)
- scripts/gasket_fractional_profile_level_infrate_uniform.py (new, 426 lines; imports CY's and CZ's scripts)
- tests/test_cli.py (+33), scripts/cli.py (+1), README.md

## Discovery
In CY's frame, h_n = L_k^n 1 = 3^{−(k+1)n} h_k F_n with F_n = L̃_k^n g, g = 1/h_k = 1/(P_0 P_1^k), so R_n^(k) = 3^{−k−1}F_{n+1}/F_n and h_k cancels. CZ's Schur complement transposed gives left eigenfunctionals ℓ̃ = ℓ + ℓE_kTQ (eigenvalue λ_1) and δ̃ = δ + δE_kT_0Q_0 (eigenvalue λ_0). Because P_0(s*) = P_1(s*) = 1, P_0'(s*) = 1/4, P_1'(s*) = 1/6 (s* = 3/2), ℓ(g) = g'(s*) = −(2k+3)/12 exactly, and B/A = m(κ + w)/(1 + w_0) with m = −(2k+3)/12 + small. Since κ is increasing on X = [√5/2, 5/2] and κ∘σ_1 = −κ/3 with σ_1(5/2) = √5/2, κ_+ = κ(5/2) = 3κ_- exactly, κ_- = −κ(√5/2) = 0.370860305428934.

- DA.2: for every k ≥ 29, |Γ_+^(k) − ((2k+3)/12)κ_-| ≤ δ_k and |Γ_-^(k) − ((2k+3)/12)κ_+| ≤ δ_k; e.g. Γ_+^(40) ∈ 2.565117 ± 0.226, Γ_+^(60) ∈ 3.801318 ± 0.00969, Γ_-^(100) ∈ 18.8211605 ± 2.1·10^{−5}; δ_k/(2k+3) ≤ 1.91·10^{−14} for k ≥ 200.
- DA.3: for every k ≥ 29 and n ≥ n_0(k), n_0(k) ≤ 16 + k/3, ρ(1−q)|q|^n(Γ_± − θ_n) ≤ ρ(L_k) − inf_X R_n^(k) ≤ ρ(1−q)|q|^n(Γ_± + θ_n) (+ even n, − odd n): exact rate |q^(k)| for every k ≥ 29.
- DA.4: normalised gap = ((2k+3)/12)κ_∓(1 + r), |r| ≤ rel_k (0.0894 at k = 40, ≤ 1% for k ≥ 53, ≤ 3.43·10^{−8} for k ≥ 200); hence (ρ − inf R_n)/(kρ|q|^n) → (2/9)κ_- = 0.0824134012 (even n), (2/3)κ_- = 0.2472402036 (odd n) as k → ∞.

## Why It Matters
CU/CV (DISC-0207, DISC-0208) certified the exact rate |q^(k)| of inf R_n^(k) → ρ(L_k) only for k ≤ 12, with n_0 growing 7 → 47 and nothing uniform in k. DA gives the constants for all k ≥ 29 with an explicit linear-in-k leading term whose coefficient is a single Koenigs-function value, and shows Γ_-/Γ_+ → 3 exactly. The linear growth in k traces to one exact number, ℓ(1/h_k) = −(2k+3)/12.

## Derivation
Checked by hand: (i) the limit in DA.4: dividing ((2k+3)/12)κ_∓·ρ(1−q)|q|^n by kρ|q|^n gives (1−q)(2k+3)κ_∓/(12k) → (4/3)(1/6)κ_∓ = (2/9)κ_∓, and κ_+ = 3κ_- gives the odd constant (2/3)κ_-; (ii) the sign bookkeeping: B/A ≈ −((2k+3)/12)κ, so max(B/A) uses −min κ = κ_- (Γ_+) and max(−B/A) uses κ_+ (Γ_-), consistent with the stated pairing; (iii) ℓ(1/h_k) = −(kP_1'(s*) + P_0'(s*)) = −(k/6 + 1/4) = −(2k+3)/12; (iv) σ_1(5/2) = √(15/4 − 5/2) = √5/2. The Neumann bounds δ_k, θ_n, n_0(k) are interval computations I did not re-derive.

## Assumptions
CY.1–CY.4 (DISC-0211) and CZ.1–CZ.2 (DISC-0212) imported and re-run; CW.3's λ_0 > 1 (DISC-0209); CT.5's algebra (DISC-0206). Standard: Riesz projections of simple eigenvalues, Neumann series, maximum modulus, Schwarz–Pick, Cauchy estimate.

## New Results
As above. Corollary stated in repo: CU/CV's limit constants c_±^(k) = ρ(1−q)Γ_± satisfy 3^{k+1}c_±^(k)/k → (2/9)κ_∓.

## Prior Art
Spectral (Ruelle–Perron–Frobenius) convergence of ratios L^{n+1}1/L^n1 with rate |λ_2/λ_1| and constant from the second Riesz projection is standard (Baladi, *Positive Transfer Operators*, 2000; Kato, *Perturbation Theory*, II–IV); Koenigs eigenfunctions of composition operators (Koenigs 1884; Cowen–MacCluer 1995). Method KNOWN.

## Novelty Analysis
Textbook machinery; the operator family and certified constants are corpus-specific. No literature search beyond this: UNRESOLVED.

## Falsification Attempts
- Independent check `scripts/indep_theorem_DA.py` (no repo code; reuses my own DISC-0211 frame collocation; Γ_± computed from my own left/right eigenvectors of the collocated frame operator with g = 1/(P_0P_1^k), interpolated to a 4001-point grid; κ, P_0', P_1' by mpmath with my own orbit products and Koenigs limit): **27/27 PASS**. Of these, 4 are trivially true placeholder checks (the "first-order centre" check at k = 29, 30, 50, 80, where no band is stated), so **23 substantive**; at k = 40, 60, 100 that check confirms the repo's band centres equal ((2k+3)/12)κ_- to 10^{−6}. Substantive passes: P_0'(s*) = 1/4, P_1'(s*) = 1/6 to 10^{−25}; ℓ(1/h_k) = −(2k+3)/12 at k = 0, 1, 7, 40; κ_+, κ_- to 10^{−14}; κ_+ = 3κ_- to 10^{−40}; sampled min κ' on X = 0.94435 ≥ 0.942; both DA.4 constants; DA.2 bands at k = 40, 60, 100 (float Γ_± inside each, N = 60/80 collocation stable to < 10^{−11}); repo's float observation at k = 30, 40, 60, 80 reproduced to 10^{−4}.
- Kept failure of my own first run (indep_da_v1): κ at 60 digits with n = 110 lost ~52 digits to cancellation in (−3)^n(σ_1^n(s) − s*), giving κ to 8 digits and 5 FAILs. Fixed with 160 digits. Cause is my check, not the theorem (same failure mode as my first CZ run, DISC-0212).
- Small-k sanity (floats, outside DA's range): Γ_+^(12) = 0.82493 vs first-order 0.83444 (1.2%), Γ_-^(12) = 2.33819 vs 2.50331 (6.6%), consistent with the repo's claim that DA does not cover k ≤ 28. At k = 29 the float Γ_+ = 1.89032 vs first order 1.88521.
- Float gap to first order decays fast (k = 60: 1.1·10^{−4}; k = 100: 2·10^{−7}), far inside δ_k: the certified bands are loose but correct, as the repo says.
None of these is a proof; they confirm the certified numbers.

## Experimental Validation
Computational only. No physical claim.

## Mathematical Status
Theorem (exact algebra + interval-certified constants, computer-assisted).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0212 → DISC-0213 (mathematical): CZ's Schur complement transposed supplies the left eigenfunctionals. DISC-0211 → DISC-0213 (mathematical): CY.1–CY.4 frame and localisation imported. DISC-0207 → DISC-0213 and DISC-0208 → DISC-0213 (mathematical): CU.4/CV.4's Γ_± extended from k ≤ 12 to every k ≥ 29. DISC-0206 → DISC-0213 (mathematical): CT.5's two-sided bound reused.

## Open Questions
k = 13..28 for the inf R_n rate; second-order term of Γ_±^(k) − ((2k+3)/12)κ_∓ (floats suggest ≈ 0.85^k); n < n_0(k); CU's routine underflow for k ≥ 30; circle eigenvalues; λ_6, a_6; Ψ_info / Stage 2 still blocked.

## Next Experiments
Close the k = 13..28 gap (e.g. CU's routine at higher precision, since CV's method reached k = 12); fit the float decay of Γ_± − first order to target a certified second-order constant.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at ed74f6de3998; `pip install python-flint mpmath`; `python3 scripts/gasket_fractional_profile_level_infrate_uniform.py`. Independent: `python3 discoveries/mathematics/scripts/indep_theorem_DA.py` (seconds; numpy + mpmath; needs `indep_theorem_CY.py` beside it).

## Evidence Log
- 2026-10-31 ~4:05 AM EDT: repo witness at ed74f6de3998 EXIT 0 ("elapsed 13.7s", "all Theorem DA checks passed"); the repo says about 95 s, so the run was faster than stated (not a discrepancy in content).
- 2026-10-31 ~4:07 AM EDT: independent check 27/27 PASS (23 substantive), after the documented κ-precision fix.
- 2026-10-31 ~4:15 AM EDT: repo pytest (tests/test_cli.py -k "DA or infrate") started; 2 tests passed so far, run not finished before this commit (not claimed as a pass).

## Change History
- 2026-10-31: created from IFI ed74f6de3998.
- 2026-10-31 (note, ~6:30 AM EDT): the kept limit k = 13..28 is closed by IFI Theorem DB at 22711f251b7a (DISC-0214); DA.2's first-order centres are within 2% of the certified Γ_± already for k ≥ 19. Text above unchanged.
