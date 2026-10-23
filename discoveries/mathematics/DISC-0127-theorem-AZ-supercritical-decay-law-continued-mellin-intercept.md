# Discovery: Theorem AZ, supercritical decay law (ρ^n+ν_α)‖F(n,α)‖ → K_α and the intercept as the continued Mellin transform

## Discovery ID

DISC-0127

## Status

THEOREM (mathematical sense only). Part (1) has a complete written proof in the repository, conditional on Theorems AQ, AR, AS, AT, AU, AY (DISC-0106, DISC-0109, DISC-0111, DISC-0113, DISC-0116, DISC-0125). Part (2) (intercept = continued Mellin transform) and part (4) (decay law) are labelled DERIVED in the repository and their written arguments were read here without finding a gap. Part (3) is computer-assisted (outward-rounded `mpmath.iv`, 80 digits). Method KNOWN; novelty of the constants UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~12:53pm EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 5404c3be371c35f0f2c571e218351cb574386b83 (2026-10-22 12:38:03 −0400). Paths: GASKET.md "Theorem AZ", "KEPT FAILURE AZ.1", OPEN/NOT THIS after AZ; CLAIM_STATUS.md new row "Supercritical decay law of the audit norm (α>log3/log5); intercept as continued Mellin transform — VERIFIED (Theorem AZ, Kept Failure AZ.1)"; scripts/gasket_fractional_supercritical_shift.py (new, 282 lines); scripts/cli.py; tests/test_cli.py; README.md OPEN bullet.

## Original Evidence

GASKET.md Theorem AZ (1)–(4), proof, witness, Kept Failure AZ.1 at 5404c3be371c35f0f2c571e218351cb574386b83.

## Discovery

For γ<α<1 (ρ=5^α/3>1), J_n=∫₀^∞ s^(−α) r_n ds, R_α(n)=κJ_n, κ=2 sin πα/π, c=c_R(α)/κ=lim ρ^(−j)Δ_j:

1. C'=lim(J_m−cρ^m/(ρ−1)) exists, J_n−cρ^n/(ρ−1)−C' ∈ [−E_n^−,E_n^+], E_n^±=∫t^(−α)(r_∞−r_n)W_± dt decreasing in n; R_α(m)=A_αρ^m+C_α+O(ρ^m 5^(−0.65m)), A_α=c_R/(ρ−1), C_α=κC'.
2. (DERIVED) M(z)=∫s^(z−1)r_∞ ds continues meromorphically to 0<Re z<1 via I_n(z)+c(z)ρ_z^n/(1−ρ_z)+Σ_(j≥n)e_j(z), with possible poles only at ρ_z=1; C_α=κM(1−α). So C_α is the continuation of R_∞(α) across its simple pole at γ: (α−γ)C_α → −c_R(γ)/ln5, and C_α+c_R(α)/(ρ−1) → C_γ (DISC-0125) from both sides.
3. Certified at α=0.8: c_R ∈ [0.4983719948274884072103,…104], A ∈ [2.3964097039792205270396,…397], C_0.8 ∈ [−1.7432571783920757239548,−…546], σ_∞ ∈ [1.0791380336973826964124,…125], ν_0.8 ∈ [−0.7274453844421553283991,−…990], K_0.8 ∈ [0.6878667584139920685497,…498]. At α=0.75: c_R(0.75) inside Theorem AT's independent enclosure; C_0.75 ∈ [−3.764208555814372066,−…065].
4. (DERIVED) (ρ^n+ν_α)‖F(n,α)‖ = K_α + O(5^(−0.65n)), K_α=√21σ_∞(ρ−1)/(3c_R): exact decay ratio 3·5^(−α), the square of Theorem K's majorant ratio; leading term constant, not log-periodic.

## Why It Matters

Upgrades Theorem AR (4c)'s ‖F(n,α)‖=Θ((3·5^(−α))^n) (DISC-0109) to an exact asymptotic with certified constants, and ties the three regimes (α<γ, α=γ, α>γ) together through one meromorphic function M(z): the subcritical limit, the critical intercept, and the supercritical intercept are values or regularized values of the same continued Mellin transform.

## Derivation

Repository proof, read line by line. (1) Theorem AT (2) at level j with k→∞ gives cρ^j as the limit of ∫t^(−α)δ_(j+1)A_k^αB_kC_k; the weight minus 1 lies in [−W_−, W_+] for every k, with W_± independent of j. Tonelli over j≥n bounds Σ|Δ_j−cρ^j| by E_n^++E_n^−; telescoping J_m gives C'. Finiteness of E_n^± uses the power ceiling r_m≤Bs^(−0.35) and W_±≤Ct^0.65 near 0 (integrand O(t^(0.3−α))) and AT's crude tail. (2) The change of variables in AT (1) is exponent-agnostic, so c(z) and e_j(z) are defined and locally uniformly dominated for Re z>−0.3; Fubini on 0.35<Re z<1 identifies the right side with M(z), and the right side is meromorphic on 0<Re z<1. (4) ‖F‖=(√21/3)σ_n/R_α(n) with σ_n−σ_∞=O(μ^n).

## Assumptions

Theorems AQ (1)–(4), AR (1)–(3), AS (1)–(3), AT (1)–(4a), AU (2), AY. Part (3) relies on the repository's outward-rounded interval arithmetic; the archive check below is float only and does not re-certify the intervals. Part (2)'s "only possible poles" and the continuity statement were checked here only numerically at γ±0.01 (coarse).

## New Results

None beyond the repository. Archive float reproduction of the repository OBSERVATION that R(m)−Aρ^m−C decays like (ρ/3)^m (ratio m=10→20: 1.11905e−4 vs (ρ/3)^10=1.12030e−4), i.e. the 3^(−m) correction of DISC-0113/DISC-0125 carried by ρ^m. Not a theorem.

## Prior Art

Renormalized resistance/Dirichlet-form asymptotics on the Sierpiński gasket via spectral decimation (Rammal–Toulouse, Fukushima–Shima, Strichartz, Kigami) and meromorphic continuation of Mellin transforms with poles on a vertical line at log-periodic points (standard in fractal spectral zeta functions, e.g. Lapidus–van Frankenhuijsen complex dimensions; Teplyaev's spectral zeta for the gasket) are classical. Method KNOWN. The specific constants for this corner resolvent were not found and were not exhaustively searched.

## Novelty Analysis

UNRESOLVED for the constants; DERIVATIVE in method. The identification "supercritical intercept = continued Mellin transform" is the standard regularized-value mechanism; no novelty claimed.

## Falsification Attempts

- Proof read: level-independence of the AT (2) weights is used exactly as in AY; the geometric factor is summed with ρ5^(−0.65)=5^(α−0.65)/3<1, true for all α<1. No gap found.
- Archive independent check /workspace/scratch-ifi/indep_theorem_AZ.py (mpmath 45 digits, own decimation recursion r_n, own log-variable quadrature, no repo import). α=0.8: ρ^(−39)Δ_39 matches repo c_R/κ to 8.6e−20 (independent of the repo's c); J_m−cρ^m/(ρ−1)−C' = 7.92e−3, 8.31e−5, 9.30e−9, 1.04e−12, 7.23e−17 at m=5,10,20,30,40 (κ times these equals the repository table 2.964e−3, 3.110e−5, 3.480e−9, 3.899e−13); σ_40 matches σ_∞ enclosure to 4e−23; ν=C/A and K closed form consistent; (ρ^40+ν)‖F(40)‖−K = −3.9e−21. α=0.75: ρ^(−39)Δ_39 matches, J_40 residual 1.5e−17 against C_0.75. Pole check at α=γ+0.01 (levels 29–30): C_α=−31.1134, (α−γ)C_α=−0.31113 vs −c_R(γ)/ln5=−0.32133 (coarse, O(α−γ) offset expected), regular part 0.697329 vs C_γ=0.70307 (one-sided, expected O(0.01) offset). 14/14 PASS.
- A first archive run failed one check because its AZ.1 tolerance (fixed 1e−6) was tighter than the proved remainder at m=10 (observed residual 1.0e−5 against bound ρ^(2m)5^(−0.65m)=1.25e−3). The tolerance was corrected to the proved bound and the run repeated; the first log is kept as indep_theorem_AZ.run1_tolerance_fail.log. This was an archive test-design error, not a repository defect.
- Repository witness rerun at 5404c3b (see Evidence Log).

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Theorem (part 1 proof; part 3 computer-assisted; parts 2 and 4 derived with written arguments).

## Patent Relevance

None.

## Related Discoveries

- DISC-0109 → DISC-0127 (mathematical): sharpens AR (4c)'s Θ bound to an exact asymptotic.
- DISC-0113 → DISC-0127, DISC-0116 → DISC-0127, DISC-0125 → DISC-0127 (mathematical): level-free AT weights, AU's Mellin pole and residue ⟨Θ⟩, AY's C_γ as the continuity value.
- DISC-0127 → DISC-0128 (Kept Failure AZ.1).

## Open Questions

Closed forms for c_R(α), C_α, σ_∞(α), K_α; whether C_α<0 on all of (γ,1) (proved only near γ, certified at 0.75 and 0.8); a proof of the observed (ρ/3)^m correction; whether θ̂_k≠0 for every k (complex poles); a flux functional on the infinite gasket.

## Next Experiments

Certify C_α on a grid in (γ,1) to test the sign question; certify the (ρ/3)^m correction coefficient.

## Reproduction Instructions

`git -C informational-flux-identity checkout 5404c3be371c35f0f2c571e218351cb574386b83 && python3 scripts/gasket_fractional_supercritical_shift.py` (about 6 min). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AZ.py` (about 5 min).

## Evidence Log

- 2026-10-22. Repository witness at 5404c3b EXIT 0 (21 PASS lines, 0 FAIL, 6m11s; log /workspace/scratch-ifi/repo_theorem_AZ.log). Archive EXIT 0 (14 PASS, /workspace/scratch-ifi/indep_theorem_AZ.log). IFI repository description still matches its claim fence.

## Change History

- 2026-10-22. Initial archive entry.
