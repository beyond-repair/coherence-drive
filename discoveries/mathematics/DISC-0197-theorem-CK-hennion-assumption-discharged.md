# Discovery: Theorem CK — Assumption CH (Hennion) discharged for CE's transfer operator

## Discovery ID
DISC-0197

## Status
THEOREM (mathematical sense only; proof and arb witness are in the source repository). Method: KNOWN (compact-perturbation / quasi-compactness argument for smooth expanding transfer operators, Ruelle 1989, Collet–Isola 1991, Baladi 2000; analytic Fredholm alternative). Constants and this specific operator: UNRESOLVED as to novelty. Not a flux, not thrust.

## Date Discovered
2026-10-30 (indexed ~03:00 EDT; source commit 2026-10-30 02:09:40 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit b5a09a39c0381750e8c1d8126ae52dd2befcd949

## Original Evidence
- GASKET.md, section "Theorem CK" (line 3736 at b5a09a39c038); retro-notes on CH/CJ "Assumptions used as stated" (line 3589) and CJ "Kept limits" (line 3721).
- CLAIM_STATUS.md row 93.
- scripts/gasket_fractional_profile_level_fredholm.py (new, 311 lines); scripts/cli.py; tests/test_cli.py.

## Discovery
On C^k(X), X=[√5/2, 5/2], with Φf=(f(s0),…,f^(k−1)(s0), f^(k)), the operator L̃ is conjugate to (0⊕M_k)+compact, where M_k g = Σ w̃_i (σ_i')^k g∘σ_i is the signed version of L_k. Because the branch images σ_1X=[√5/2, g_a] and σ_2X=[g_b, 5/2] are disjoint (g_a≈1.6223335 < g_b≈2.2063622), ‖M_k^n‖=‖L_k^n 1‖ exactly, so ρ(M_k)=ρ(L_k). A finite-rank approximation plus analytic Fredholm argument gives r_ess(L̃; C^k)≤ρ(L_k) with finite-rank Riesz projections outside. This removes the only literature assumption (Hennion 1993) from CH.3, CI.5 and CJ.5. Consequence: spec(L̃; C¹(X)) = {r} ∪ {|z|≤ρ(L_1)}, ρ(L_1)∈[0.1343549, 0.1343551], unconditionally; λ_2=−0.0731138175124… is the second eigenvalue on C² unconditionally.

## Why It Matters
Closes open item (d) after CJ: DISC-0194/0195/0196 no longer depend on a cited theorem whose hypotheses were never checked in-repo. Their outer-spectrum halves become unconditional within the repository's proof chain.

## Derivation
As in GASKET.md CK.1–CK.4: chain-rule recursion b_{m+1,j}=b_{m,j}'+b_{m,j−1}σ' gives leading coefficient w̃_i(σ_i')^k; Taylor's formula with integral remainder makes Φ a Banach isomorphism; lower-order terms are Volterra integrals of f^(k), compact by Arzelà–Ascoli; Gelfand + sign-matched test function gives ρ(M_k)=ρ(L_k); local reduction z−T=(z−M−(K−F))(I−A(z)F) with F finite rank, discreteness from det(I−D(z)) holomorphic, connectedness of Ω_k.

## Assumptions
CH.2 and CI.1 radii (re-run by the script); CG.3 enclosures of r, λ_2, λ_3 and the 10⁻³ bound on the rest of the H²(D) spectrum (constants imported, not re-certified here); CH.3's restriction argument; CJ.4. Classical textbook facts only (chain/Leibniz rule, Taylor, Arzelà–Ascoli, Gelfand, identity theorem, Neumann series).

## New Results
r_ess(C^k)≤ρ(L_k) for every k≥1 for this operator without Hennion; equality only for k=1 (via CJ.4).

## Prior Art
The splitting "C^k transfer operator = operator on top derivative + compact" with essential radius governed by the |σ'|^k-weighted operator is the standard proof of Ruelle's theorem (D. Ruelle, Publ. IHÉS 1989; Collet–Isola, CMP 1991; V. Baladi, "Positive Transfer Operators and Decay of Correlations", 2000). Hennion 1993 is the abstract version. The exact identity ‖M_k^n‖=‖L_k^n 1‖ from disjoint branch images is an elementary observation.

## Novelty Analysis
Method KNOWN. What is specific: the certified constants for this gapped two-branch map and the completion of the in-repo chain CH→CK. No claim of a mathematical first.

## Falsification Attempts
- Repo witness: `python3 scripts/gasket_fractional_profile_level_fredholm.py` EXIT 0 in 11.0 s at b5a09a39c038 (all CK.1–CK.4, CI.1, CH.2 checks ok).
- Independent script /workspace/ifi-ck-indep/indep_ck.py (box-local, sympy + numpy floats, not interval-certified), 17/17 PASS: generic sympy leading coefficient w(σ')^k for k=1..4; σ_1(5/2)=√5/2; g_a=1.6223335<g_b=2.2063622; min w̃_1=0.30379>0.3035, min w̃_2=0.059851>0.0598; sup L_1 1=0.281661; k=1 lower-order Lasota–Yorke constant sup Σ|w̃_i'|=0.56444≤0.56446; for n=1..8 the 2^n preimages of the maximiser are distinct and a sign-matched g attains ‖M_1^n g‖=‖L_1^n 1‖ (n-th roots 0.2817→0.1452, decreasing toward ρ(L_1)).
- Logic attacked: (i) the C^k-coordinate block is k bounded functionals, so finite rank — holds; (ii) cross terms f^(j)∘σ_i, j<k, are polynomial-in-coordinates plus Volterra integrals of f^(k), compact — holds; (iii) sup of the resolvent of 0⊕M_k on a closed disk inside |z|>ρ(L_k) is finite (spectrum of 0⊕M_k is {0}∪spec M_k) — holds; (iv) the open/closed connectedness argument needs U to miss |z|>‖L̃‖ — holds by Neumann series. No break found.
- Note: the repo's "min gap" observation is a grid minimum; mine is at the maximiser, so the figures differ but do not contradict.

## Experimental Validation
Computational only. Needed: none for the theorem; the open items are mathematical.

## Mathematical Status
Theorem (computer-assisted constants imported from CG.3, CH.2, CI.1).

## Patent Relevance
None. Pure spectral theory; repo states it is not a flux and not thrust.

## Related Discoveries
DISC-0191 → DISC-0194 → DISC-0195 → DISC-0196 → DISC-0197 (mathematical). DISC-0197 removes the Hennion condition from DISC-0194 (CH.3), DISC-0195 (CI.5) and DISC-0196 (CJ.5).

## Open Questions
Boundary circle |z|=ρ(L_1) in C¹; r_ess(C^k)=ρ(L_k) for k≥2 (C^k analogue of CJ.4); B≠0 in CG.4; explicit C_G; closed form of ρ(L_1).

## Next Experiments
Attempt a C² analogue of CJ.4 (gap-bump witness for |μ|<ρ(L_2)); re-certify CG.3 in the same run to remove imported constants.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at b5a09a39c038; `pip install python-flint sympy numpy`; run `python3 scripts/gasket_fractional_profile_level_fredholm.py` (exits nonzero on any failed check).

## Evidence Log
- 2026-10-30 ~02:58 EDT: repo witness EXIT 0 (11.0 s); independent check 17/17 PASS.

## Change History
- 2026-10-30: created from IFI b5a09a39c038.
