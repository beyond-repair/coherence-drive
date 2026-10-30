# Discovery: Theorem CI, the C¹ essential spectral radius of the level-sum transfer operator equals ρ(L_1)

## Discovery ID
DISC-0195

## Status
THEOREM in the mathematical sense only (computer-assisted with arb interval arithmetic; the upper bound is conditional on Hennion's theorem, cited as Assumption CH). Method KNOWN. Constants novelty UNRESOLVED. Conjecture CI.6 is a CONJECTURE (its expected form matches the Collet–Isola picture; whether their theorem applies directly to this gapped two-branch system is UNRESOLVED).

## Date Discovered
2026-10-30 (commit time 2026-10-30 00:07 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 80f30b8a01728fb48e805b8163cde04b979075dd

## Original Evidence
- GASKET.md "## Theorem CI" (line 3629): CI.1–CI.5, proof, Observation, Conjecture CI.6, Kept limits.
- GASKET.md Theorem CH Kept limits paragraph amended with a pointer to CI.
- CLAIM_STATUS.md row 91, "C¹ essential spectral radius of the level-sum transfer operator".
- scripts/gasket_fractional_profile_level_essential.py (added, 315 lines); scripts/cli.py, tests/test_cli.py, README.md updated.

## Discovery
Same operator as DISC-0188/0190/0191/0194: in s=√(t+25/4), (L̃f)(s)=w̃_1 f(σ_1 s)+w̃_2 f(σ_2 s), σ_{1,2}=√(15/4∓s) on X=[√5/2, 5/2], with gap G=(g_a,g_b) between the branch images; L_1 has weights w̃_i|σ_i'|.
- CI.1 (arb): a degree-12 rational polynomial h>0 with 0.1343549 h < L_1 h < 0.1343551 h on X, so ρ(L_1) ∈ [0.1343549, 0.1343551].
- CI.2 (sympy): with c_i=|σ_i'|h(σ_i)/L_1h, Σw̃_i c_i=1 and 2σ_i c_i/h(σ_i)=1/L_1h for every positive h.
- CI.3: a right inverse K of L̃ on C¹(X) (multiplier c_i on the branch images, width-10⁻⁶ slope windows with profile p(u)=(1−u)(1−3u) and cubic fill ψ=6τ(1−τ) on G) with certified 2×2 majorant ρ(A)<7.44297805367 in the norm (sup|f|, sup|f'|/h). CH.4's right inverse had growth 9.18.
- CI.4: every |μ|≤0.1343547 is a C¹ eigenvalue (v=ΣμⁿKⁿg with CH.4's gap bump g).
- CI.5: 0.1343547 ≤ r_ess(L̃; C¹(X)) ≤ ρ(L_1) ≤ 0.1343551, and every C¹ eigenvalue μ≠r has |μ| ≤ 0.1343551; ratio to r in [0.3170752, 0.3170762]. CH's undecided annulus (0.1089, 0.1345] shrinks to (0.1343547, 0.1343551].

## Why It Matters
It closes, up to a 4·10⁻⁷ annulus, the C¹ question DISC-0194 left open: the C¹ subdominant spectrum is essentially the full closed disk of radius ρ(L_1). The level sums are untouched (CG.4 concerns an analytic vector; rate |λ_2|/r<0.17255 stands).

## Derivation
Repository proof (GASKET.md Theorem CI). Lower bound: an open disk of eigenvalues contains no isolated spectral point, so r_ess is at least its radius. Upper bound: CH.3's Lasota–Yorke estimate plus Hennion. Key improvement over CH.4: choosing c_i proportional to |σ_i'|h(σ_i)/L_1h makes the f'-coefficient of (Kf)'/h exactly h/L_1h ≤ 1/0.1343549, so the derivative growth of K matches 1/ρ(L_1) up to the window factor κ ≤ 1.000000463.

## Assumptions
- Hennion 1993 (Proc. AMS 118, 627–634), cited not reproved (upper bound only).
- CH.3 restriction argument and CG.3's enclosures of r and λ_2 imported, not re-run.
- CH.3's printed proof in GASKET.md (line 3610) still breaks off mid-sentence ("…dense in C^k(X). So"); erratum first noted in DISC-0194, not fixed by 80f30b8.

## New Results
For this archive: DISC-0194's C¹ open band (0.1089, 0.1345] narrowed to (0.1343547, 0.1343551]. r_ess(C¹) = ρ(L_1) to 4·10⁻⁷.

## Prior Art
Essential spectrum on C^k equal to the disk of radius given by a weighted transfer operator with |T'|^{-k} weights: Ruelle 1989; Collet–Isola 1991 (Commun. Math. Phys. 139, 551–557) for expanding maps; Hennion 1993; Baladi's monograph treats the general picture. Building a right inverse on a gap where the operator never reads (kernel from bumps) is a standard device. The method is KNOWN; the specific constants for this operator have no comparison and stay UNRESOLVED.

## Novelty Analysis
Nothing here is a new theorem type. What is specific: the certified two-sided enclosure of ρ(L_1) and the sharp right inverse that reaches 0.99999908 of it, for an operator arising from a graph-Laplacian corner resolvent on the combinatorial gasket. Novelty of the constants is UNRESOLVED.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_essential.py`, EXIT 0, 1.95 s wall, all checks ok.
- Independent script /workspace/ifi-ci-indep/indep_ci.py (box-local), 10/10 PASS: sympy re-derivation of |σ_i'|=1/(2σ_i), Σw̃_i c_i=1, 2σ_1c_1/h(σ_1)=1/L_1h for symbolic h; p, P=u(1−u)², ψ profile facts; independent Chebyshev power iteration gives ρ(L_1)≈0.134354982970, inside [0.1343549, 0.1343551]; recomputing ρ(A) from the displayed entries padded by their radii gives 7.442978054 and 0.1343547·ρ(A)<1 still holds.
- Observation from the attack: the 11-digit bound ρ(A)<7.44297805367 cannot be reproduced from the 9-digit displayed A_11 (midpoint entries give 7.4429780539); it rests on the repo's arb computation, which passed. The conclusion CI.4 only needs 0.1343547·ρ(A)<1, which has a 9·10⁻⁷ margin and survives the rounding.
- Logic checked: v≠0 because on the middle of G every KⁿG (n≥1) is a cubic and g is a monic quartic; convergence from entrywise N(Kf)≤A·N(f) with A≥0. No failure found.

## Experimental Validation
Computational only. Required: rerun at higher precision with a smaller δ and better h to test Conjecture CI.6.

## Mathematical Status
Theorem (computer-assisted; upper bound conditional on Hennion). Conjecture CI.6 open.

## Patent Relevance
None. Pure spectral theory of a transfer operator; the repository itself states it is not a flux and not thrust.

## Related Discoveries
DISC-0188 → DISC-0190 → DISC-0191 → DISC-0194 → DISC-0195 (mathematical).

## Open Questions
Conjecture CI.6 (C¹ spectrum is {r} ∪ closed disk of radius ρ(L_1), interior all eigenvalues); closed form of ρ(L_1); Assumption CH from scratch; explicit C_G and whether B≠0 in CG.4.

## Next Experiments
Push δ→0 and refine h to reach |μ|<ρ(L_1)−ε for smaller ε; check whether Collet–Isola's hypotheses cover the gapped (non-onto) two-branch map.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 80f30b8a01728fb48e805b8163cde04b979075dd; `pip install python-flint sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_essential.py` (exits nonzero on any failed check).

## Evidence Log
- 2026-10-30 ~00:55 EDT: repo witness EXIT 0; independent check 10/10 PASS.

## Change History
- 2026-10-30: created from IFI 80f30b8a0172.
