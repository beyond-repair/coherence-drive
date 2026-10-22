# Discovery: Theorem AY, certified intercept C_γ of the endpoint resistance and the level-shift law (n+ν_γ)‖F(n,γ)‖ → K_γ

## Discovery ID

DISC-0125

## Status

THEOREM (mathematical sense only). Part (1) has a complete written proof in the repository, conditional on Theorems AQ, AR, AS, AT, AU (DISC-0106, DISC-0109, DISC-0111, DISC-0113, DISC-0116). Part (2) is computer-assisted (outward-rounded `mpmath.iv` enclosures, 80 digits). Part (3) is DERIVED from (1)–(2) and Theorem AT's σ-side rate. Method KNOWN; novelty of the constants UNRESOLVED. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~11:53am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 8517f2bac0f79c5c76b1ef9d03517582bc8d06e2 (2026-10-22 11:35:48 −0400). Paths: GASKET.md "Theorem AY", "KEPT FAILURE AY.1", OPEN/NOT THIS after AY, AU's OPEN list ("a certified C_γ (now given by Theorem AY)"); CLAIM_STATUS.md new row "Intercept C_γ of R_γ(n) at γ=log3/log5; level shift of the endpoint audit norm — VERIFIED (Theorem AY, Kept Failure AY.1)"; scripts/gasket_fractional_endpoint_shift.py (new, 358 lines); scripts/cli.py; tests/test_cli.py; README.md "OPEN. Distributional flux on the infinite gasket" bullet and Sequel.

## Original Evidence

GASKET.md Theorem AY (1)–(3), proof, witness, Kept Failure AY.1 at 8517f2bac0f79c5c76b1ef9d03517582bc8d06e2.

## Discovery

At α=γ=log3/log5 (ρ=5^γ/3=1), with J_n=∫₀^∞ s^(−γ) r_n ds, R_γ(n)=κJ_n, κ=2 sin πγ/π, c=ln5⟨Θ⟩ (DISC-0116):

1. C'=lim(J_m−mc) exists and J_n−nc−C' ∈ [−E_n^−, E_n^+], E_n^± = ∫ t^(−γ)(r_∞−r_n)W_± dt, decreasing in n; C_γ=κC'.
2. Certified: E_60^+ ≤ 8.69e−28, E_60^− ≤ 5.9e−34, E_40^+ ≤ 1.06e−18; C_γ ∈ [0.70307046242185742992904816, …817]; ν_γ=C_γ/c_R ∈ [1.35946811514371162883271469, …470]; σ_∞(γ) ∈ [1.15191861167405417640547243, …244]; K_γ=√21σ_∞/(3c_R) ∈ [3.40236076383265507999048519, …520]. Theorem AU's float C_γ≈0.70307046242184 was low by 1.7e−14.
3. (n+ν_γ)‖F(n,γ)‖ = K_γ + O(5^(−0.65n)).

## Why It Matters

Closes the "certified C_γ" item left OPEN by Theorem AU (DISC-0116) and corrects AU's float in its 14th digit. Gives the exact renormalization of the vanishing endpoint audit norm at the critical exponent: a shifted hyperbola, not a pure 1/n law.

## Derivation

Repository proof, checked line by line: at ρ=1 Theorem AT (2)'s bracket weights B_∞ ≤ 1 ≤ A_∞^γ C̄ do not depend on the level j, and the k=0 term of AT (1) is Δ_j=J_(j+1)−J_j=∫t^(−γ)δ_(j+1) with weight 1. Hence −∫t^(−γ)δ_(j+1)W_− ≤ c−Δ_j ≤ ∫t^(−γ)δ_(j+1)W_+. Summing over j≥n (Tonelli; Σδ_(j+1)=r_∞−r_n, AQ (3)) gives Σ|Δ_j−c| ≤ E_n^+ + E_n^−; once finite, J_m−mc telescopes to C' and J_n−nc−C' = Σ_(j≥n)(c−Δ_j). Monotonicity of r_m gives E_m^± ↓. Part (3): ‖F‖=(√21/3)σ_n/R_γ(n) with σ_n−σ_∞=O(5^(−0.65n)) (AT (4a)) and R_γ(n)=c_R(n+ν_γ)+O(5^(−0.65n)).

## Assumptions

Theorems AQ (1)–(4), AR (2), AS (2), AT (1),(2),(4a), AU (1). Part (2) relies on the repository's outward-rounded interval arithmetic; the archive check below is float only and does not re-certify the intervals.

## New Results

Archive (float) reproduction of the repository OBSERVATION that J_m−mc−C' decays like 3^(−m) (ratio over ten levels 1.6916e−5 vs 3^(−10)=1.6935e−5), faster than the proved 5^(−0.65m). Not a theorem.

## Prior Art

Renormalized resistance asymptotics R(n)=cn+C+o(1) at a critical exponent and the bracket/telescoping argument are standard (Tonelli summation of per-level defects; spectral decimation on the Sierpiński gasket: Rammal–Toulouse, Fukushima–Shima, Strichartz; Kigami's resistance forms). Method KNOWN. The specific constants C_γ, ν_γ, σ_∞(γ), K_γ for this corner resolvent were not found in a search and were not exhaustively searched.

## Novelty Analysis

UNRESOLVED for the constants; DERIVATIVE in method.

## Falsification Attempts

- Proof read: the level-independence of the AT (2) weights at ρ=1 is what makes the defects summable; each step (sign of weights, Tonelli on nonnegative terms, telescoping) holds. No gap found.
- Archive independent check /workspace/scratch-ifi/indep_theorem_AY.py (mpmath 45 digits, own decimation recursion, own log-variable quadrature, no repo import; c taken from AU's 34-digit enclosure): J_m−mc−C' = 1.34264e−5, 2.27121e−10, 3.84628e−15, 6.50014e−20 at m=10,20,30,40 (positive, matches the repository table, and inside E_40^+); σ_40 matches σ_∞(γ) to 1.4e−27; ν=C_γ/c_R and K=√21σ/(3c_R) consistent with the stated enclosures to 1e−26; (40+ν)‖F(40,γ)‖−K = −5.5e−21; νK ≥ 4.6254. A first version of the AY.1 check used too tight a tolerance against the limit −νK at m=40 (it should compare with −νK·m/(m+ν)); fixed and rerun, see the log.
- Repository witness rerun at 8517f2b (see Evidence Log).

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Theorem (part 1 proof; part 2 computer-assisted; part 3 derived).

## Patent Relevance

None.

## Related Discoveries

- DISC-0113 → DISC-0125, DISC-0116 → DISC-0125 (mathematical): AY uses AT's level-independent weights at ρ=1 and AU's slope.
- DISC-0125 → DISC-0116 (mathematical): resolves AU's open "certified C_γ" and corrects AU's float C_γ by 1.7e−14.
- DISC-0125 → DISC-0126 (Kept Failure AY.1).

## Open Questions

Closed forms for C_γ, ν_γ, σ_∞(γ), K_γ; a proof of the observed 3^(−n) correction; a flux functional (not one scalar norm) on the infinite gasket.

## Next Experiments

Certify the 3^(−n) correction coefficient; test whether the ratio of the correction is exactly 1/3 (float ratio 1.6916e−5 vs 1.6935e−5 over ten levels suggests a slowly converging prefactor).

## Reproduction Instructions

`git -C informational-flux-identity checkout 8517f2bac0f79c5c76b1ef9d03517582bc8d06e2 && python3 scripts/gasket_fractional_endpoint_shift.py` (about 3–4 min). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AY.py`.

## Evidence Log

- 2026-10-22. Repository witness at 8517f2b EXIT 0 (17 PASS lines, 0 FAIL; log /workspace/scratch-ifi/repo_theorem_AY.log). Archive EXIT 0 (9 PASS, /workspace/scratch-ifi/indep_theorem_AY.log). IFI repository description still matches its claim fence.
- 2026-10-22. Minor float-witness discrepancy (does not touch the theorem): the repository's 30-digit quadrature table gives J_30−30c−C' = 3.356e−15 and σ_30−σ_∞ = 5.591e−22, while the archive's 45-digit log-variable quadrature gives 3.846e−15 and 6.461e−22. The archive values continue the 3^(−10) ratio exactly (dev30/dev20 = 1.693e−5, dev40/dev30 = 1.690e−5); the repository's m=30 entry gives 1.478e−5. Both sit far inside the proved bound 5·5^(−0.65m), so every repository check and the certified enclosures are unaffected; the m=30 float row is likely quadrature-limited. Recorded, not a contradiction of any claim.

## Change History

- 2026-10-22. Initial archive entry.
