# Discovery: Theorem CM — the open C^k disk |z| < ρ(L_k) is filled with eigenvalues of infinite multiplicity, for every k ≥ 1

## Discovery ID
DISC-0199

## Status
THEOREM (mathematical sense only; proof and arb/sympy witness are in the source repository). Method: KNOWN (Harnack/bounded-distortion almost-eigenfunction; right inverse with gap-bump kernel; analytic Fredholm alternative; that the whole open essential disk consists of eigenvalues for transfer operators of non-full-branch/expanding maps on C^k is a classical phenomenon, cf. Collet–Isola 1991, Keller 1984, Baladi 2000). Constants and this specific gapped two-branch operator: UNRESOLVED as to novelty. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~04:57 EDT; source commit 2026-10-30 04:04:22 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 46889b83fb0c16a0aa50d9cac586a53e25119dc5

## Original Evidence
- GASKET.md, section "Theorem CM" (line 3853 at 46889b8).
- CLAIM_STATUS.md row 95.
- scripts/gasket_fractional_profile_level_fill.py (new, 379 lines); scripts/cli.py; tests/test_cli.py; README.md.

## Discovery
- CM.1: for every k ≥ 1 and 0 < a < ρ(L_k) there is analytic h > 0 with L_k h ≥ a h on X, h = Σ_{j<J} L_k^j 1 / t^j. Uses a Harnack constant C_k = exp((D_w + k D_s)|X|) ≤ 28.04, 76.22, 207.2, 563.2 (k = 1..4, arb), built from CL.5's distortion constants.
- CM.2: the right inverse K with c_i = |σ_i'|^k h(σ_i)/L_k h and degree-(2k+1) Hermite gap fill has top-order part N with |c_i(T_i y)||T_i'(y)|^k = h(y)/L_k h(T_i y) exactly, so r(N) ≤ 1/a.
- CM.3: for |μ| < ρ(L_k), dim ker(L̃ − μ; C^k) = ∞ (analytic Fredholm on C^k ⊕ B(X), poles of (I − μK)^{-1} handled).
- CM.4: σ_e(L̃; C^k) = closed disk |z| ≤ ρ(L_k) (Fredholm sense) for every k; spec(C^1) = {r} ∪ disk; spec(C^2) = {r, λ_2} ∪ disk; spec(C^3), spec(C^4) = {r, λ_2, λ_3} ∪ disk.

## Why It Matters
Answers DISC-0198's open item "whether {|z| < ρ(L_k)} ⊂ spec(C^k) for k ≥ 2" (yes), and generalizes DISC-0196's C¹ gap-bump construction (CJ.4) to every k without CJ's cone certificate. The only remaining C^k spectral question for this operator is the boundary circles.

## Derivation
GASKET.md CM.1–CM.4 proofs. Checked by hand here:
- CM.1: each word term w̃_ω|σ_ω'|^k has log-derivative ≤ D_w + k D_s, hence varies by ≤ C_k across X; min h ≥ C_k^{-1} Σ (ρ/t)^j since ‖L_k^j 1‖ ≥ ρ^j. L_k h = t h − t + L_k^J 1/t^{J−1}, and the −t term is absorbed when (C_k − 1)(t − ρ) < ρ − a and J is large. Sound (the repo's stated condition gives the margin).
- CM.2: Σ w̃_i c_i = L_k h / L_k h = 1; σ_i(T_i y) = y and |σ_i'(T_i y)||T_i'(y)| = 1 give the identity; then N^n telescopes to products of h/L_k h ≤ a^{-1} times max h/min h. Sound.
- CM.3–CM.4: infinite kernel at every point of the open disk excludes Fredholmness there; closure plus CL.2's radius and CK.3(iii)'s isolated-eigenvalue statement give the exact spectrum. Sound, conditional only on the imported CG.3/CL.3 enclosures (|λ_3| < 0.0430702 ≤ ρ(L_2) puts λ_3 inside the C² disk).

## Assumptions
CL.5 distortion constants D_w ≤ 1.68855, D_s ≤ 0.723607 (arb); CL.2, CK.3, CL.3, CG.3 (imported). Textbook facts only (analytic Fredholm theorem, Taylor isomorphism C^k ≅ C^k-jet ⊕ C(X), Hermite interpolation).

## New Results
Exact C^k spectrum (as a set, up to the circle |z| = ρ(L_k)) of this operator for k = 1..4, and the infinite-multiplicity open-disk statement for every k.

## Prior Art
- P. Collet, S. Isola, Comm. Math. Phys. 139 (1991): essential spectrum of transfer operators of expanding Markov maps on C^k.
- G. Keller, "On the rate of convergence to equilibrium in one-dimensional systems", Comm. Math. Phys. 96 (1984): for piecewise expanding maps, every point inside the essential radius is an eigenvalue on BV/C^k-type spaces (infinite-dimensional kernels of Perron–Frobenius operators).
- V. M. Gundlach, Y. Latushkin, ETDS 23 (2003); V. Baladi, "Positive Transfer Operators and Decay of Correlations" (2000).
I did not verify that any of these states the open-disk-filling result for exactly this gapped, Cantor-attractor setting; the phenomenon and the mechanism are standard.

## Novelty Analysis
Method KNOWN. What is specific: this operator, its certified Harnack constants, and the all-k uniform construction. No claim of a mathematical first.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_fill.py` EXIT 0 in 32 s at 46889b8 (all CM.1–CM.4 and re-run CL.3/CL.5 checks ok; explicit C² eigenfunction residual 3.2e-27; top-derivative growth per level matches |μ|/ρ(L_k) at 0.70, 0.93, 0.90 and leaves C^k at 1.16).
- Independent script /workspace/ifi-cm-indep/indep_cm.py (box-local, numpy floats plus sympy, own 90-node Chebyshev–Nyström discretization, not interval-certified), 15/15 PASS: C_k recomputed as 28.037, 76.213, 207.167, 563.140 from the arb upper bounds of D_w, D_s (the last differs from the script's printed 563.138 in the fifth digit because I added the full arb radius; immaterial, any finite C_k suffices, and the commit message rounds up to 563.2); sympy confirms the CM.2 identity on both branches for k = 1..4; empirical Harnack ratios max/min L_k^j 1 (j < 40) = 2.63, 3.84, 5.65, 8.31, far below C_k; CM.1's h built with t = ρ(1 + ε/(2C_k)) gives min L_k h/h ≥ 0.9998 ρ ≥ (1 − ε)ρ for ε = 0.05, 0.01 and every k.
- Logic attacked: whether the series could be pushed past ρ(L_k) (no: CL.2 forbids it, and the repo's 1.16 row shows the predicted divergence); whether poles of (I − μK)^{-1} could break infinite multiplicity (handled by the analytic Fredholm theorem, poles still give kernel). No break found.

## Experimental Validation
Computational only. None needed for the theorem.

## Mathematical Status
Theorem (computer-assisted constants; CG.3 and CL.3 constants imported).

## Patent Relevance
None. Pure spectral theory; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0196 → DISC-0197 → DISC-0198 → DISC-0199 (mathematical). DISC-0199 answers DISC-0198's open C^k (k ≥ 2) disk question and generalizes DISC-0196's CJ.4.

## Open Questions
Eigenvalues on the circles |z| = ρ(L_k) (for k = 1 only those with nonzero 1-jet on Λ remain possible); B ≠ 0 in CG.4; explicit C_G; closed forms of r, λ_2, ρ(L_k).

## Next Experiments
Attack the boundary circle |z| = ρ(L_1) with eigenfunctions having nonzero 1-jet on Λ; check whether Keller 1984 / Collet–Isola hypotheses cover the gapped map so CM.3 becomes a direct citation.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 46889b8; `pip install python-flint sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_fill.py` (exits nonzero on any failed check).

## Evidence Log
- 2026-10-30 ~04:57 EDT: repo witness EXIT 0 (32 s); independent check 15/15 PASS.

## Change History
- 2026-10-30: created from IFI 46889b83fb0c.
