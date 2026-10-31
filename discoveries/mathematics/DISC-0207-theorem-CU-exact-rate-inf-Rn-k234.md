# Discovery: Theorem CU — exact rates |ν_2^(k)|/ρ(L_k) = 0.2895670639, 0.3189949783, 0.3376293000 for inf R_n^(k) → ρ(L_k), k = 2, 3, 4, with two-sided constants for every n ≥ n_0 = 7, 9, 12

## Discovery ID
DISC-0207

## Status
THEOREM (mathematical sense only; interval-certified proof in the source repository). Method: KNOWN (CT's routine with the weight exponent k as a parameter: Galerkin truncation on a Hardy space, Krawczyk eigenpair enclosure, Riesz projections, second resolvent identity). Constants: UNRESOLVED as to novelty; no claim of a mathematical first. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~8:10 PM EDT; source commit 2026-10-30 19:03:04 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 8ea4fbef2a4c992311ec1f0a3f0cd858df344b5f

## Original Evidence
- GASKET.md, new section "Theorem CU" (line 4222; NOT THIS paragraph line 4276), +63 lines.
- CLAIM_STATUS.md, new row 103.
- scripts/gasket_fractional_profile_level_infrate_k.py (new, 510 lines; imports CR.1/CR.2's Krawczyk and Neumann routines unchanged; CT's script unchanged); scripts/cli.py (+1); tests/test_cli.py (+40, `test_theorem_cu_profile_level_infrate_k`); README.md (+2/−1).

## Discovery
Setting as in DISC-0206 (CT), with weights u_i = wt_i |σ_i'|^k = wt_i/(2σ_i)^k: (L_k f)(s) = u_1 f(σ_1) + u_2 f(σ_2), h_n = L_kⁿ1, R_n^(k) = h_{n+1}/h_n on X = [√5/2, 5/2]. CT listed the exact rate for k ≥ 2 as open.
- CU.1: on CG's H²(D) (c = 83/50, R = 8/5, N = 120), ‖L_k(I − P_120)‖ ≤ 6.08·10⁻²⁷, 2.57·10⁻²⁷, 1.39·10⁻²⁷ (k = 2, 3, 4).
- CU.2–CU.3: exactly two eigenvalues of L_k in |z| > ρ_in = 1/500, 1/1000, 1/2500, real and simple:

  | k | ρ(L_k) | ν_2^(k) | q = ν_2/ρ |
  |---|---|---|---|
  | 2 | 0.0430703112227101271 ± 1.3e-20 | −0.0124717435618530418 ± 3.8e-20 | −0.289567063896138 ± 2.7e-16 |
  | 3 | 0.0139192547691468646 ± 2.1e-20 | −0.0044401723728826436 ± 1.4e-20 | −0.318994978288970 ± 1.9e-16 |
  | 4 | 0.0045264690852562123 ± 2.8e-20 | −0.0015282685887826225 ± 3.6e-20 | −0.337629300012356 ± 4.2e-16 |

  each inside CL.3's interval (DISC-0198), ρ_H = ρ(L_k) on C(X) by CT.3's argument.
- CU.4: h_n = ρⁿA + ν_2ⁿB + E_n, sup_X|E_n| ≤ τ_1 ρ_inⁿ; Γ_+ = max B/A ≈ 0.2546354, 0.3087743, 0.3625751; Γ_− = max(−B/A) ≈ 0.6796090, 0.8310494, 0.9801676 (enclosed to ~3e-7).
- CU.5: for every n ≥ n_0 = 7, 9, 12, ρ(1−q)|q|ⁿ(Γ_par − θ_n) ≤ ρ − inf_X R_n ≤ ρ(1−q)|q|ⁿ(Γ_par + θ_n). Limit constants c_+ = 0.01414298, 0.00566892, 0.002195297 (even n), c_− = 0.03774688, 0.01525759, 0.00593466 (odd n); oscillation constants 0.0518899, 0.02092651, 0.00812996. Uniform windows (even / odd): k=2 [0.0120710, 0.0162149] n≥8 / [0.0248320, 0.0506618] n≥7; k=3 [0.00459104, 0.00674680] n≥10 / [0.0104718, 0.0200434] n≥9; k=4 [0.00117440, 0.00321619] n≥12 / [0.00566745, 0.00620186] n≥13.

## Why It Matters
Closes the open item recorded in DISC-0206 (CT): "L_k for k ≥ 2" is now done for k = 2, 3, 4. The Collatz–Wielandt brackets for ρ(L_k) converge at the exact rate |ν_2/ρ|, and ρ(L_k) is sharpened from CL.3's ~1e-7 to ~3e-20.

## Derivation
Read and checked here: the proof is CT.1–CT.5 verbatim with wt_i/(2σ_i) replaced by wt_i/(2σ_i)^k; holomorphy on the disk needs only σ_i ≠ 0 (|σ_i| ≥ 7/10 from CT.1), and positivity on X holds because σ_i > 0 there. Realness of ν_2 follows from L_k commuting with f ↦ conj(f(conj s)). The monotonicity of θ_n requires the three bases |q|, ρ_in/ρ, ρ_in/|ν_2| < 1; these are 0.29–0.34, 0.046–0.088, 0.16–0.26 (checked here too).

## Assumptions
Imported as stated (not re-run independently): CJ.2's R_n applied to L_k, CG.1's disk and tail formula (re-run in the repo for the weights u_i), CG.3's homotopy, CR.1/CR.2's Krawczyk and Neumann routines, CT.4–CT.5's algebra. CL.3 used for consistency only.

## New Results
Certified ρ(L_k) to ~20 digits and certified second eigenvalue ν_2^(k) for k = 2, 3, 4; exact rate and two-sided parity-dependent constants for inf R_n^(k), sup R_n^(k) and their oscillation from n_0(k).

## Prior Art
As for DISC-0206: standard spectral perturbation (Kato), validated numerics for transfer operators (Tucker 2011; Bandtlow–Slipantschuk-style Hardy-space truncation), Collatz–Wielandt brackets. No prior statement about these specific operators found; no literature search for the constants was done.

## Novelty Analysis
Method KNOWN (a parameterised rerun of CT). The constants are specific to this repository's operators; novelty of the numbers is UNRESOLVED. Not a first in any general sense.

## Falsification Attempts
- Repo witness at 8ea4fbef2a4c (fresh clone): EXIT 0, 72 `ok` (24 per k), 0 FAIL, script elapsed 34.3 s (wall 34 s), ends "all Theorem CU checks passed". Repo test `pytest tests/test_cli.py -k theorem_cu`: 1 passed in 36.7 s.
- Independent script `mathematics/scripts/indep_theorem_CU.py` (no repo code imported; different methods): 52/52 PASS on first run (~12 s, numpy only).
  - Chebyshev collocation on X itself (not H²(D)), N = 40 and 60: ρ and ν_2 agree with CU.3 to ≤ 3·10⁻¹⁶ for all three k; both real, ν_2 < 0; third eigenvalue modulus 7.3·10⁻⁴, 2.7·10⁻⁴, 1.8·10⁻⁴ (< ρ_in = 2·10⁻³, 1·10⁻³, 4·10⁻⁴); |q| agrees to 1e-14.
  - Exact path-sum evaluation of h_n = L_kⁿ1 on a 401-point grid for n ≤ 17: inf R_n ≤ ρ ≤ sup R_n for all n ≤ 16; (ρ − inf R_n)/|q|ⁿ lies in CU.5's windows at every n from n_0 to 16 for each parity, including the boundary values n = 7 (k=2, odd: 0.0377425), n = 8 (k=2, even: 0.0141428), n = 9/10 (k=3), n = 12/13 (k=4); normalized values → Γ_± within 2e-5; c_± = ρ(1−q)Γ_± reproduced to 1e-8; argmin at s = √5/2 (even) and s = 5/2 (odd) for n ≥ 8; oscillation constants reproduced to 1e-6.
  - k-pattern: |q| = 0.2441 (k=1, CT), 0.2896, 0.3190, 0.3376 is increasing, matching the repo's Observation; Γ_± increase with k from CT's 0.2001/0.5249; c_± scale down with ρ(L_k). No inconsistency with CT's k = 1 record.
- Sign-convention attack: ν_2 < 0 makes q < 0, so (−1)ⁿ selects Γ_+ for even n and Γ_− for odd n; numerically the infimum switches endpoint with parity exactly as claimed. Survived.
- Boundary attack on n_0: the certified statement starts at n_0, but for k = 4 the odd window is stated from n ≥ 13 (n_0 = 12 is even) — consistent, not a gap. Numerically the windows already hold well before n_0 (repo's own Observation), so nothing at the boundary fails.
- Cosmetic finding (not a mathematical defect): the script's opening banner prints "for k = 2, 3" although it runs and checks k = 2, 3, 4 (all three blocks present, 24 ok each).
- Not checked independently: the arb resolvent bounds, the Neumann bound ‖A⁷‖_F, and the CG.3 homotopy (imported).

## Experimental Validation
Computational only.

## Mathematical Status
Theorem (interval-certified computer-assisted proof in the repo), for k = 2, 3, 4 only.

## Patent Relevance
None. The repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0206 → DISC-0207 (mathematical): CT's open item "L_k for k ≥ 2" addressed for k = 2, 3, 4. DISC-0198 → DISC-0207 (mathematical): CL.3's intervals for ρ(L_k) sharpened to ~3e-20. DISC-0204 → DISC-0207 (computational): CR.1/CR.2 routines reused. DISC-0191 → DISC-0207 (mathematical): CG.1 tail formula and CG.3 homotopy.

## Open Questions
k ≥ 5 and anything uniform in k (or k → ∞); n < n_0(k) by certified constants; closed forms of ρ(L_k), ν_2^(k), Γ_±; eigenvalues on |z| = ρ(L_k); CF.3's Birkhoff constant for general f; λ_6, a_6; Ψ_info and Stage 2 remain blocked in the repo.

## Next Experiments
Whether |q^(k)| stays bounded below 1 uniformly in k (floats for k = 5..10 are cheap); certify n < n_0 with smaller inner circles.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 8ea4fbef2a4c; `pip install python-flint mpmath numpy`; `python3 scripts/gasket_fractional_profile_level_infrate_k.py` (about 35 s; `CU_KS=2` runs a single k). Independent: `python3 discoveries/mathematics/scripts/indep_theorem_CU.py` (about 12 s, numpy only).

## Evidence Log
- 2026-10-30 ~8:05 PM EDT: repo witness EXIT 0, 72 ok, 0 FAIL, 34.3 s; e.g. k=4 ρ_H mid 0.004526469085256212317, ν_2 mid −0.001528268588782622474, q = [−0.337629300012356 ± 4.15e-16], c_+ = [0.002195297 ± 8.99e-10].
- Repo test test_theorem_cu_profile_level_infrate_k: 1 passed (36.7 s).
- Independent check: 52/52 PASS on first run.

## Change History
- 2026-10-30: created from IFI 8ea4fbef2a4c.
- 2026-10-30 (~9:20 PM EDT) note, history above preserved: IFI 00df4a6ea6d7 (Theorem CV, DISC-0208) extends the exact rate to k = 5..12 and, in Kept Failure CV.6, refutes the extrapolation recorded above ("|q| increasing" for k ≤ 4): |q^(k)| peaks at k = 8 (0.3588353292) and decreases for k = 8..12 (|q^(8)| − |q^(9)| = 7.205e-4). The k ≤ 4 statement above remains true; only its extension fails. Reproduced independently in DISC-0208.
