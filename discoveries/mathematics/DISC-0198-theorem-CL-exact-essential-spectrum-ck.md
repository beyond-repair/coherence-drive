# Discovery: Theorem CL — exact essential spectral radius of CE's transfer operator on C^k, and the closed C¹ essential disk

## Discovery ID
DISC-0198

## Status
THEOREM (mathematical sense only; proof and arb witness are in the source repository). Method: KNOWN (Calkin-norm lower bound via weakly null disjoint bumps; Atkinson's theorem; Gelfand's formula in the Calkin algebra; analytic Fredholm alternative; the exact formula r_ess(C^k) = spectral radius of the |σ'|^k-weighted operator is classical for smooth expanding maps: Collet–Isola 1991, Gundlach–Latushkin 2003). Constants and this specific gapped two-branch operator: UNRESOLVED as to novelty. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~03:55 EDT; source commit 2026-10-30 03:13:51 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 0b34f9192458568d0624a673fd7e6de0d6157d62

## Original Evidence
- GASKET.md, section "Theorem CL" (line 3799 at 0b34f91); parenthetical retro-note added to CK's "Kept limits".
- CLAIM_STATUS.md row 94.
- scripts/gasket_fractional_profile_level_calkin.py (new, 321 lines); scripts/cli.py; tests/test_cli.py; README.md.

## Discovery
- CL.1: on C(X), the Calkin norm ‖M_k^n‖_e = ‖M_k^n‖ = ‖L_k^n 1‖_∞ (sign-matched tent bumps at the 2^n preimages of points s_m → s*, with pairwise disjoint supports, are weakly null, so compacts kill them).
- CL.2: with CK.3's splitting, lim ‖L̃^n‖_e^{1/n} = ρ(L_k) on C^k(X) for every k ≥ 1, so the essential spectral radius equals ρ(L_k) in both the Fredholm and CK's sense. The lower bound is new in-repo for k ≥ 2 (CK proved only ≤). 0 is in the Fredholm essential spectrum for every k (bumps supported in the gap G are in the kernel).
- CL.3 (arb, two-sided Collatz–Wielandt): ρ(L_2) ∈ [0.0430702, 0.0430704], ρ(L_3) ∈ [0.0139192, 0.0139193], ρ(L_4) ∈ [0.0045264, 0.0045265]. So on C², λ_3 lies inside the essential disk and the isolated spectrum is {r, λ_2}; on C³ and C⁴ it is {r, λ_2, λ_3}.
- CL.4: on C¹ the Fredholm essential spectrum is exactly the closed disk |z| ≤ ρ(L_1), and spec \ σ_e = {r}.
- CL.5: with N = {f ∈ C¹ : f = f' = 0 on the attractor Λ}, no nonzero f ∈ N satisfies L̃f = μf with |μ| ≥ ρ(L_1). All of CJ's gap-bump eigenfunctions lie in N, so that mechanism cannot reach the circle. Distortion constants D_w ≤ 1.6885, D_s ≤ 0.72361 (arb).

## Why It Matters
Answers DISC-0197's open item "r_ess(C^k) = ρ(L_k) for k ≥ 2" (yes, for the radius) and narrows the boundary-circle question: any circle eigenvalue would need an eigenfunction with nonzero 1-jet on Λ.

## Derivation
GASKET.md CL.1–CL.5 proofs. Checked by hand here:
- CL.1: M_k^n g_m(s_m) = Σ_ω c_ω(s_m) sgn c_ω(s_m) = Σ |c_ω(s_m)| = L_k^n 1(s_m) because w̃_i > 0; disjointness of the point sets follows from injectivity of (ω, s) ↦ σ_ω s (disjoint branch images). Sound.
- CL.2: compression to the C(X) summand is a norm-one operation and keeps compactness of the perturbation; ‖L_k^n‖ = ‖L_k^n 1‖ for a positive operator, so the n-th roots converge to ρ(L_k). Sound.
- CL.4: the boundary contradiction can be shortened (points of the open disk are non-Fredholm because the kernel is infinite-dimensional while the operator is onto, and any ball around a boundary point meets the open disk, so the Fredholm set being open already excludes boundary points). The repo's longer index argument also works.
- CL.5: the mean-value step |f(σ_ω s)| ≤ ε_n sup|σ_ω'| |X| uses f(σ_ω(5/2)) = 0 since σ_ω(5/2) ∈ Λ; the sum Σ w̃_ω|σ_ω'(s)| = L_1^n 1(s) ≤ C_ρ ρ(L_1)^n via CJ.2. D_w = 0.93338/(1 − 5^{-1/2}) = 1.68850, D_s = 0.4/(1 − 5^{-1/2}) = 0.72361. Sound.

## Assumptions
CK.3(ii)–(iii), CI.1, CI.3's right inverse K, CJ.2, CJ.4, CG.3 enclosures of r, λ_2, λ_3 and the 10⁻³ bound on the rest of the H² spectrum (imported constants). Textbook facts only (Riesz representation, Atkinson, Gelfand in the Calkin algebra, openness of the Fredholm set, local constancy of the index).

## New Results
r_ess(L̃; C^k) = ρ(L_k) exactly for every k ≥ 1 for this operator; two-sided enclosures of ρ(L_2..4); exact C¹ essential spectrum; exclusion of jet-zero eigenfunctions on the circle.

## Prior Art
- P. Collet, S. Isola, "On the essential spectrum of the transfer operator for expanding Markov maps", Comm. Math. Phys. 139 (1991): essential spectral radius on C^k for expanding Markov maps.
- V. M. Gundlach, Y. Latushkin, "A sharp formula for the essential spectral radius of the Ruelle transfer operator on smooth and Hölder spaces", Ergodic Theory Dynam. Systems 23 (2003): exact (two-sided) r_ess formula on C^k.
- D. Ruelle, Publ. IHÉS 1989; V. Baladi, "Positive Transfer Operators and Decay of Correlations", 2000.
The disjoint-bump Calkin lower bound is a standard device. The gapped (non-full-branch, Cantor-attractor) setting here differs from the full-branch manifold setting of those papers; whether their formula covers it directly was not checked.

## Novelty Analysis
Method KNOWN. What is specific: this operator, its certified constants, and CL.5's jet-zero exclusion as applied to the CI–CJ gap-bump mechanism. No claim of a mathematical first.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_calkin.py` EXIT 0 in 1.7 s at 0b34f91 (all CL.1–CL.5 checks ok).
- Independent script /workspace/ifi-cl-indep/indep_cl.py (box-local, numpy floats, own 80-node Chebyshev–Nyström discretization, not interval-certified), 11/11 PASS: ρ(L_1..4) = 0.134354983, 0.043070311, 0.013919255, 0.004526469, each inside the repo's enclosure; radius ordering against CG.3's λ_2, λ_3; true sups |(log w̃_1)'| = 0.933333, |(log w̃_2)'| = 0.507064 (below the repo's arb upper bounds 0.933372, 0.507357, so the bounds are conservative, not wrong), |(log|σ'|)'| = 0.4; D_w = 1.68842, D_s = 0.72361; brute force over all 2^10 words gives max |(log w̃_ω)'| = 0.9159 ≤ D_w; ‖L_2^4 1‖^{1/4} = 0.0534 ≥ ρ(L_2).
- One first attempt flagged a FAIL because my check expected the sup to equal the repo's printed figure; the repo prints an arb upper enclosure, which is consistent. Logged here for the audit trail.
- Logic attacked: CL.1 positivity of weights (holds, min w̃_2 ≈ 0.0599); CL.4 boundary argument (holds, and a shorter route exists); CL.5 reliance on f(σ_ω(5/2)) = 0 (holds since 5/2 = σ_2(5/2) ∈ Λ). No break found.

## Experimental Validation
Computational only. None needed for the theorem.

## Mathematical Status
Theorem (computer-assisted constants; CG.3 constants imported).

## Patent Relevance
None. Pure spectral theory; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0194 → DISC-0195 → DISC-0196 → DISC-0197 → DISC-0198 (mathematical). DISC-0198 answers the k ≥ 2 radius question left open by DISC-0197 and narrows DISC-0196's boundary-circle question.

## Open Questions
Circle eigenvalues |z| = ρ(L_1) with nonzero 1-jet on Λ; whether {|z| < ρ(L_k)} ⊂ spec(C^k) for k ≥ 2; B ≠ 0 in CG.4; explicit C_G; closed forms of r, λ_2, ρ(L_k).

## Next Experiments
Check whether Gundlach–Latushkin's hypotheses cover the gapped two-branch map (would make CL.2 a direct citation); attempt a C² gap-bump analogue of CJ.4.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 0b34f91; `pip install python-flint sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_calkin.py` (exits nonzero on any failed check).

## Evidence Log
- 2026-10-30 ~03:55 EDT: repo witness EXIT 0 (1.7 s); independent check 11/11 PASS.

## Change History
- 2026-10-30: created from IFI 0b34f9192458.
