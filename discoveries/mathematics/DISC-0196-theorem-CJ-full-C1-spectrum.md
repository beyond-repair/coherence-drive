# Discovery: Theorem CJ, the full C¹ spectrum of the level-sum transfer operator (Conjecture CI.6 proved)

## Discovery ID
DISC-0196

## Status
THEOREM in the mathematical sense only (computer-assisted with arb interval arithmetic). The disk half (every |μ|<ρ(L_1) is a C¹ eigenvalue) is unconditional given CI.3 and CF.1; "nothing but r outside ρ(L_1)" is conditional on Hennion's theorem (Assumption CH). Method KNOWN. Constants novelty UNRESOLVED. Supersedes the CONJECTURE label on Conjecture CI.6 in DISC-0195.

## Date Discovered
2026-10-30 (commit time 2026-10-30 00:59 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 94ae1e7d93e5 (parent 80f30b8a0172)

## Original Evidence
- GASKET.md "## Theorem CJ" (line 3691): CJ.1–CJ.5, proof, Observation, Kept limits; Conjecture CI.6 header (line 3674) relabelled "now Theorem CJ".
- CLAIM_STATUS.md row 92, "Full C¹ spectrum of the level-sum transfer operator, Conjecture CI.6".
- scripts/gasket_fractional_profile_level_disk.py (added, 178 lines); scripts/cli.py, tests/test_cli.py (+22), README.md updated.

## Discovery
Same operator as DISC-0188/0190/0191/0194/0195: L̃f = w̃_1 f(σ_1) + w̃_2 f(σ_2) on X=[√5/2, 5/2], σ_{1,2}=√(15/4∓s), gap G=(g_a,g_b); L_1 has weights u_i=w̃_i|σ_i'|.
- CJ.1 (sympy): closed forms for (log u_i)'; (log u_1)'(5/2)=4/3.
- CJ.2 (arb): M_1≤1.33335, M_2≤0.4045, B=max M_i/(1−c_i)≤2.4121, so h_n=L_1ⁿ1 stays in one log-Lipschitz cone; Hilbert diameter of L_1 C_{2B} < 13.31, so inf R_n → ρ(L_1) with R_n=h_{n+1}/h_n (Birkhoff, CF.1).
- CJ.3 (arb): with gap weight λ=2, Q=max(1/√5, 0.80488, 0.63037) ≤ 0.8050 < 1.
- CJ.4: CI.3's right inverse rebuilt with h=h_n and window δ→0 has majorant spectral radius → sup h_n/L_1h_n = 1/inf R_n, so every |μ|<ρ(L_1) is a C¹ eigenvalue.
- CJ.5: spec(L̃; C¹(X)) = {r} ∪ {|z|≤ρ(L_1)}, r_ess = ρ(L_1) ∈ [0.1343549, 0.1343551], ratio to r in [0.3170757, 0.3170762]. CI's undecided annulus (0.1343547, 0.1343551] is closed.

## Why It Matters
It finishes the C¹ question opened in DISC-0191/0194: the whole C¹ spectrum is now determined (modulo the boundary circle's point-spectrum status). The level sums are untouched; CG.4's rate |λ_2|/r<0.17255 on the analytic vector stands.

## Derivation
Repository proof (GASKET.md Theorem CJ). The improvement over CI is structural, not numeric: instead of one fixed polynomial h, use the iterates h_n of L_1, whose uniform cone bound controls the sup-norm row across the gap, and weight the gap by λ=2 so that row contracts (Q<1). The majorant matrix becomes lower triangular in the limit δ→0 with diagonal (≤QS, S), so its spectral radius tends to S = 1/inf R_n, which tends to 1/ρ(L_1).

## Assumptions
- Hennion 1993 (Assumption CH), cited not reproved, for the outer part only.
- Imported from earlier theorems, not re-run here: CI.1, CI.2, CI.3 (construction of K, Kf∈C¹, L̃K=I), CH.4's gap bump, CF.1, CG.3's enclosures of r and λ_2, CH.3's restriction argument.

## New Results
For this archive: DISC-0195's open annulus is closed and Conjecture CI.6 becomes a theorem (outer part conditional on Hennion). Remaining open: point-spectrum status of the circle |z|=ρ(L_1), multiplicities, closed form of ρ(L_1), whether B≠0 in CG.4, explicit C_G.

## Prior Art
The result is the expected Collet–Isola/Ruelle picture: for C¹ the essential spectrum of a transfer operator of an expanding system fills the disk of radius given by the |T'|-weighted operator (Ruelle 1989; Collet–Isola 1991, Commun. Math. Phys. 139; Hennion 1993; Baladi's monographs). Birkhoff cone contraction (Birkhoff 1957; Liverani 1995 for transfer operators) is standard. Method KNOWN; whether the published theorems cover this gapped, non-onto two-branch system directly is not checked here, and novelty of the constants is UNRESOLVED.

## Novelty Analysis
No new theorem type. Specific to this repo: the gap-weighted norm (λ=2) that makes the right-inverse construction close, and certified constants for an operator coming from a graph-Laplacian corner resolvent on the combinatorial gasket. Novelty UNRESOLVED.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_disk.py`, EXIT 0, 1.06 s wall, all checks ok. `pytest tests/test_cli.py -k disk` 1 passed.
- Independent script /workspace/ifi-cj-indep/indep_cj.py (box-local, mpmath/numpy, not interval-certified), 8/8 PASS: M_1=1.333333 (sup attained at s=5/2, matching CJ.1's 4/3), M_2=0.404354, B=2.412023, b'=3.490712<a, Δ=13.30879<13.31, Q=0.804873≤0.8050, Chebyshev power iteration ρ(L_1)=0.13435498297 inside CI.1's window, ρ(L_1)/r=0.3170759 inside CJ.5's window.
- Logic checked: (i) on Y_i the bound |Kf|/h_0 ≤ |σ_i'|·(h_0/L_1h)·|f|/h_0 uses h_0=h on the images, which holds since σ_iX=Y_i; (ii) on G, h(g_j)/h(x)≤e^{Bℓ} needs h∈C_B, supplied by CJ.2 for every h_n; (iii) A_10 and O(δ) constants depend on n but n is fixed before δ→0, so the order of limits is valid; (iv) λ=1 would give E/(2g_a)≈1.26>1, confirming the weight is load-bearing. No failure found.
- Attack not completed: Assumption CH remains a literature citation; the disk half does not depend on it.

## Experimental Validation
Computational only. Possible next check: a direct numerical exhibition of an eigenfunction for some |μ| between 0.1343547 and 0.1343549 (the band CI could not reach).

## Mathematical Status
Theorem (computer-assisted; outer part conditional on Hennion). Boundary circle open.

## Patent Relevance
None. Pure spectral theory; the repository states it is not a flux and not thrust.

## Related Discoveries
DISC-0188 → DISC-0190 → DISC-0191 → DISC-0194 → DISC-0195 → DISC-0196 (mathematical).

## Open Questions
Eigenvalue status on |z|=ρ(L_1); multiplicities in the disk; closed form of ρ(L_1); Assumption CH from scratch; B≠0 in CG.4; explicit C_G.

## Next Experiments
Check whether Collet–Isola's or Baladi's published hypotheses cover the gapped two-branch map, which would make CJ.5 a direct corollary; attempt the boundary circle.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 94ae1e7d93e5; `pip install python-flint sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_disk.py` (exits nonzero on any failed check).

## Evidence Log
- 2026-10-30 ~02:05 EDT: repo witness EXIT 0 (1.06 s); independent check 8/8 PASS; CLI test passed.

## Change History
- 2026-10-30 (~03:00 EDT, preserved original): status note — IFI b5a09a39c038 Theorem CK discharges Assumption CH for this operator (DISC-0197). Status moves THEOREM (outer part conditional on Hennion) → THEOREM (unconditional within the repo's proof chain). Original conditional wording above is kept as history.
- 2026-10-30: created from IFI 94ae1e7d93e5.
- 2026-10-30 (~03:55 EDT): note added, earlier text unchanged. Theorem CL (IFI 0b34f91, DISC-0198) shows the C¹ Fredholm essential spectrum is the closed disk |z|≤ρ(L_1) and that CJ's gap-bump eigenfunctions cannot reach the circle; circle eigenvalues with nonzero 1-jet on Λ remain open.
