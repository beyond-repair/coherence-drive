# Discovery: Theorem CT — exact rate |ν_2|/ρ(L_1) = 0.2440800701 for inf R_n → ρ(L_1), with two-sided constants for every n ≥ 10

## Discovery ID
DISC-0206

## Status
THEOREM (mathematical sense only; interval-certified proof in the source repository). Method: KNOWN (Galerkin truncation on a Hardy space, Krawczyk eigenpair enclosure, Riesz projections, second resolvent identity). Constants: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~7:05 PM EDT; source commit 2026-10-30 18:11:26 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 219b29ba779b20a37938273d508acaf37ced84fd

## Original Evidence
- GASKET.md, new section "Theorem CT" (line 4166; NOT THIS paragraph line 4213), +56 lines.
- CLAIM_STATUS.md, new row 102.
- scripts/gasket_fractional_profile_level_infrate.py (new, 470 lines; imports CR.1/CR.2's Krawczyk and Neumann routines unchanged); scripts/cli.py (+1); tests/test_cli.py (+26); README.md (+2).

## Discovery
Setting: s ∈ X = [√5/2, 5/2], σ_{1,2}(s) = √(15/4 ∓ s), (L_1 f)(s) = u_1 f(σ_1 s) + u_2 f(σ_2 s), u_i = wt_i/(2σ_i), h_n = L_1ⁿ1, R_n = h_{n+1}/h_n. CJ.2 (DISC-0196) proved inf R_n ≤ ρ(L_1) ≤ sup R_n with only a Birkhoff rate ≈ 0.9974 and left the true rate open.
- CT.1: on CG's H²(D) (c = 83/50, R = 8/5), ‖L_1(I − P_120)‖ ≤ 1.82·10⁻²⁶.
- CT.2–CT.3: exactly two eigenvalues of L_1 in |z| > 1/100, real and simple: ρ_H = 0.1343549829703998131 ± 2.9·10⁻²⁰ (= ρ(L_1) on C(X), inside CI.1's interval), ν_2 = −0.0327933736640408162 ± 4.0·10⁻²⁰; q = ν_2/ρ = −0.244080070117426 ± 4·10⁻¹⁶.
- CT.4: h_n = ρⁿA + ν_2ⁿB + E_n, sup_X|E_n| ≤ e_X K_in (1/100)^{n+1}; min_X A ≥ 0.833891; Γ_+ = max B/A ∈ [0.2000641183, 0.2000642055], Γ_− = max(−B/A) ∈ [0.5249039315, 0.5249041376].
- CT.5: for every n ≥ 10, ρ(1−q)|q|ⁿ(Γ_par − θ_n) ≤ ρ − inf_X R_n ≤ ρ(1−q)|q|ⁿ(Γ_par + θ_n), θ_10 ≤ 0.0702; explicitly 0.0217|q|ⁿ ≤ ρ − inf R_n ≤ 0.0914|q|ⁿ. Limit constants c_+ = 0.0334404 ± 1.2·10⁻⁸ (even n), c_− = 0.0877368 ± 6.4·10⁻⁸ (odd n); sup R_n − inf R_n has the same rate, constant 0.1211772.

## Why It Matters
Closes the open item recorded in DISC-0196 (CJ): the Collatz–Wielandt brackets for ρ(L_1) converge at the exact rate 0.2441 rather than the proved Birkhoff rate 0.9974, and ρ(L_1) itself is now known to ±2.9·10⁻²⁰ instead of CI.1's ±10⁻⁷.

## Derivation
Read and checked here: the CT.5 identity (ρ − R_n)/(ρ(1−q)|q|ⁿ) = [(−1)ⁿG + (η_n − η_{n+1})/((1−q)|q|ⁿA)]/[1 + (qⁿB + η_n)/A] follows by substituting h_n = ρⁿ(A + qⁿB + η_n) into R_n = h_{n+1}/h_n; the perturbation θ_n bound is the standard ratio estimate. The passage from H²(D) to C(X) (ρ_H = ρ(L_1)) uses point evaluation ≤ e_X‖·‖_{H²} and Gelfand's formula on 1 ∈ H²(D), plus the analytic eigenfunction being nonzero on X; this is correct as stated. The parity split is real: B/A changes sign on X, so the infimum sits at s = √5/2 for even n and s = 5/2 for odd n.

## Assumptions
Imported as stated (not re-run independently): CJ.2's R_n, CG.1's disk and tail formula (constants re-run for u_i), CG.3's homotopy argument, CR.1/CR.2's Krawczyk and Neumann routines. CI.1 used for consistency only.

## New Results
Certified ρ(L_1) to 20 digits; certified second eigenvalue ν_2 of L_1; exact rate and two-sided parity-dependent constants for inf R_n, sup R_n and their oscillation from n = 10.

## Prior Art
Standard spectral perturbation (Kato), validated numerics for transfer operators (Tucker 2011; Bandtlow–Slipantschuk style Hardy-space truncation), Collatz–Wielandt brackets for positive operators. No prior statement about this specific operator found; no literature search for the constants was done.

## Novelty Analysis
Method KNOWN. The constants are specific to this repository's operator; novelty of the numbers is UNRESOLVED. Not a first in any general sense.

## Falsification Attempts
- Repo witness at 219b29ba779b: EXIT 0, 22 `ok`, 0 FAIL, elapsed 10.1 s (wall 11 s).
- Independent script `mathematics/scripts/indep_theorem_CT.py` (no repo code imported; different methods): 18/18 PASS.
  - Chebyshev collocation on X itself (not H²(D)), N = 40 and 60: ρ = 0.13435498297039983, ν_2 = −0.032793373664039886 (agree with CT.3 to 1e-13), both real, third eigenvalue modulus 1.65·10⁻³ < 1/100 (a complex pair in collocation), q = −0.24408007011741945.
  - Exact path-sum evaluation of h_n = L_1ⁿ1 (2ⁿ branches) on a 401-point grid for n ≤ 17: inf R_n ≤ ρ ≤ sup R_n for all n; (ρ − inf R_n)/|q|ⁿ = 0.0334404 (even) and 0.0877368 (odd) for n = 10..15, inside CT.5's windows; normalized values → 0.2000641 and 0.5249040 (Γ_±); argmin at s = √5/2 (even) and s = 5/2 (odd); oscillation constant 0.1211772.
  - Observation (floats, no claim): the CT.5 windows already hold numerically from n = 4 (n = 4: 0.0334167; n = 5: 0.0876970), consistent with the repo's own kept limit that n < 10 is simply not covered by its constants.
- Attack on the C(X) vs H²(D) identification: a spurious H²-only eigenvalue above ρ would break CI.1's interval; ρ_H falls inside it, and collocation on X gives the same ρ. Survived.
- Not checked independently: the arb resolvent bounds and the CG.3 homotopy (imported).

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (interval-certified computer-assisted proof in the repo).

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0196 → DISC-0206 (mathematical): CJ's open rate item closed. DISC-0195 → DISC-0206 (mathematical): CI.1's interval for ρ(L_1) sharpened to ±2.9·10⁻²⁰. DISC-0204 → DISC-0206 (computational): CR.1/CR.2 routines reused. DISC-0190 ↔ DISC-0206 (conceptual): Birkhoff cone rate vs exact spectral rate, same pattern as CF → CN.

## Open Questions
n < 10 by certified constants; closed forms of ρ(L_1), ν_2, Γ_±; L_k for k ≥ 2; eigenvalues on |z| = ρ(L_k); CF.3's Birkhoff constant for general f; λ_6, a_6; Ψ_info and Stage 2 remain blocked in the repo.

## Next Experiments
Certify n = 4..9 with sharper E_n bounds (smaller inner circle); third eigenvalue of L_1 (collocation suggests a complex pair near |z| ≈ 1.65·10⁻³).

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 219b29ba779b; `pip install python-flint mpmath numpy`; `cd scripts && python3 gasket_fractional_profile_level_infrate.py` (about 11 s). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CT.py` (about 6 s, numpy only).

## Evidence Log
- 2026-10-30 ~7:00 PM EDT: repo witness EXIT 0, 22 ok, 0 FAIL, ends "all Theorem CT checks passed"; ρ_H = [0.1343549829703998131 ± 2.84e-20], ν_2 = [−0.0327933736640408162 ± 3.99e-20], q = [−0.244080070117426 ± 4.00e-16], oscillation constant [0.1211772 ± 6.72e-8].
- Independent check: 18/18 PASS on first run.

## Change History
- 2026-10-30: created from IFI 219b29ba779b.
- 2026-10-30 (~8:10 PM EDT): note added, earlier text unchanged. Theorem CU (IFI 8ea4fbef2a4c, DISC-0207) addresses this record's open item "L_k for k ≥ 2" for k = 2, 3, 4: exact rates |ν_2/ρ| = 0.2895670639, 0.3189949783, 0.3376293000 from n_0 = 7, 9, 12. k ≥ 5 and uniform-in-k statements stay open.
