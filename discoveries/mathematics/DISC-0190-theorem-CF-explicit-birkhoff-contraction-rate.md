# Discovery: Theorem CF, Birkhoff contraction proved for CE's transfer operator with an explicit rate and spectral-gap bound

## Discovery ID
DISC-0190

## Status
THEOREM (mathematical sense only; elementary proof in the repository plus `arb` interval certificates for the cone constants). Discharges Assumption CE, so DISC-0188 no longer depends on a cited literature result. Method KNOWN (Birkhoff 1957 / Bushell 1973 Hilbert-metric contraction tanh(Δ/4); Liverani-style cones of log-Lipschitz functions for transfer operators). The specific constants (θ<0.5442, θ^(1/5)<0.8855, gap bound |μ|<0.3752) are novelty UNRESOLVED, and they are proved bounds, not sharp values. Not a patent candidate. Not thrust.

## Date Discovered
2026-10-29 (indexed ~4:55pm EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit dab0578773f99a6c5fa928773b72118fc5d7b2a5 (2026-10-29 16:08:11 EDT).

## Original Evidence
- GASKET.md section "Theorem CF" (line 3481), statement line 3487, proof line 3502, Observation (no claim) line 3512, "What stays open" line 3514.
- GASKET.md line 3425: Assumption CE now marked "DISCHARGED by Theorem CF" (original wording preserved in place).
- scripts/gasket_fractional_profile_level_rate.py (new, 274 lines); scripts/cli.py and tests/test_cli.py hooks; CLAIM_STATUS.md row (line 88); README.md.

## Discovery
In s=√(t+25/4) ∈ [√5/2, 5/2], the branches of CE's twisted operator L̃ become σ_(1,2)(s)=√(15/4∓s) with |σ_1'|≤1/√5, |σ_2'|<0.2267, and |(log w̃_1)'|≤14/15, |(log w̃_2)'|<0.5071.
1. CF.1: elementary proof of Birkhoff's contraction (positive map, image of cone has Hilbert diameter ≤Δ ⇒ contraction by tanh(Δ/4)).
2. CF.2: for the cone C_(47/2) of functions log-Lipschitz in s with constant 47/2, diam L̃^5 C_a ≤ Δ = 2.44003534…, θ=tanh(Δ/4)=0.5441333…, θ^(1/5)=0.8854031…; b*=7(5+√5)/30 is absorbing.
3. CF.3: |log(L̃^(m+1)f/L̃^m f) − log r| ≤ θ^⌊m/5⌋ Θ_a(f, L̃f); positive eigenfunction h̃ exists; for the level sums |log(s_(k+1)/(r s_k))| ≤ C_G·0.8855^k (C_G finite, not explicit).
4. CF.4: certified consistency for f=1, m<12.
5. CF.5: any other eigenvalue with a C¹ eigenfunction has |μ| ≤ θ^(1/5) r < 0.3752.

## Why It Matters
Removes the only literature assumption from DISC-0188 and gives an explicit (if loose) convergence rate for the geometric decay of ν's level sums.

## Derivation
As in the repository (GASKET.md line 3502 onward): CF.1 via the sympy identity (z+m)(z+M)−z(√m+√M)² = (z−√(mM))²; CF.2 by mean-value cone step, oscillation recursion over the 32 level-5 s-intervals, and CE.3's cone lemma; CF.3 by monotone inf/sup ratio sandwich plus Gelfand; CF.5 by perturbing h̃ with Re v and comparing oscillation growth |ρ|^m against θ^(m/5).

## Assumptions
- CE.1, CE.2, CE.4's rational certificate, and the non-Assumption-CE part of CE.3 (L̃^4G positive and C¹), imported unchanged.
- CF.5 covers only eigenvalues with C¹ eigenfunctions (as stated).

## New Results
- Archive observation (not a repository claim): the oscillation bound of log(Σ terms) by the max of term oscillations (used in CF.2) is the mediant inequality and holds; the proof's chain is internally consistent.
- The proved rate 0.8855 is far from the observed rate |λ_2|/r ≈ 0.1725 (collocation), as the repository itself says.

## Prior Art
Birkhoff (1957) and Bushell (1973) give the tanh(Δ/4) contraction; Liverani (1995) and the "Birkhoff cones" literature use log-Lipschitz cones for transfer operators exactly in this way. No targeted search for these specific constants.

## Novelty Analysis
Method KNOWN. What is specific: the s-coordinate making the branches √(15/4∓s), the cone parameter a=47/2 and five-step diameter certificate. Novelty of these constants UNRESOLVED; they are bounds, not a new invariant.

## Falsification Attempts
- Independent script (`mathematics/scripts/indep_theorem_CF.py`, no repo imports): re-derived M_1=14/15 symbolically, checked 0<(log w̃_1)'≤14/15 and |(log w̃_2)'|≤M_2=0.5070644331 on a 200001-point grid, c_2=0.2266173744, b_1=11.442853<a, b_5=2.07859334, own oscillation recursion gives V_5=1.042652601, Δ=2.440035344, θ=0.5441333187, θ^(1/5)=0.8854031525 (match repo). CF.3 bound tested for L̃^m 1 by full branch tree at 9 points for m≤16 (repo checked m<12): max used fraction 0.592, deviation 2.8e−13 at m=16 against bound 0.123. Chebyshev collocation (80 nodes) gives r=0.4237312869626079 (matches CE) and λ_2=−0.0731138175, inside the CF.5 bound. All 13 checks PASS.
- Attack on CF.5: checked that the real-eigenvalue case avoids the two zero phases; argument holds as written. No contradiction found.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_rate.py` EXIT 0 (5.95 s), all checks passed. Independent check PASS (3.4 s).

## Mathematical Status
Theorem (proof in repository; constants by interval arithmetic). C_G not explicit; λ_2 not certified.

## Patent Relevance
None. Pure mathematics on a graph Laplacian spectral measure.

## Related Discoveries
- DISC-0188 (Theorem CE): Assumption CE discharged; DISC-0188 now unconditional.
- DISC-0186 (Theorem CC), DISC-0187 (Theorem CD): level structure of ν.
- DISC-0189 (Kept Failure CE.6): the twist that makes L̃ strictly positive is what lets the cone argument work.

## Open Questions
- Certified value or sharp bound for λ_2 ≈ −0.0731 (ratio 0.1725).
- Explicit C_G (needs a Lipschitz bound on log L̃^4G, hence ψ'').
- Closed form for r.

## Next Experiments
- Certify λ_2 by a rigorous Chebyshev/Ulam enclosure; try larger iterate n or smaller a to tighten θ.

## Reproduction Instructions
`git clone https://github.com/beyond-repair/informational-flux-identity && git checkout dab0578773f99a6c5fa928773b72118fc5d7b2a5 && python3 scripts/gasket_fractional_profile_level_rate.py`; then `python3 discoveries/mathematics/scripts/indep_theorem_CF.py` from this repository (needs mpmath, numpy, sympy).

## Evidence Log
- 2026-10-29 ~4:55pm EDT. Indexed from commit dab0578773f99a6c5fa928773b72118fc5d7b2a5. Repo witness EXIT 0 (5.95 s); independent check 13/13 PASS.

## Change History
- 2026-10-29. Initial archive entry.
- 2026-10-29 ~8:58pm EDT: note added. The observed λ_2 ≈ −0.0731 is now certified by Theorem CG (DISC-0191, IFI 8364d9497c57) on holomorphic functions; CF.5's C¹ bound is not replaced on C¹(X), but CG.4 replaces CF.3's level-sum rate 0.8855 with 0.17255. Status unchanged.

## Note (2026-10-30, appended; text above unchanged)
The open item "explicit C_G" is answered for the level sums only by IFI Theorem CS at 9cb3b84d6b2863320e2903993b9a31927af2d6ce: in the form |log(s_{k+1}/(rs_k))| ≤ C_G θ^{k/5} (k ≥ 4) the sharp constant is C_G* = |log(s_5/(rs_4))|θ^{−4/5} = 0.02105127810 ± 2.1·10⁻¹² (0.0210492 for θ̄ = 0.5442), via the spectral route (CG–CP), not via this record's Birkhoff bound. The Birkhoff-route constant Θ_a(f_0, L̃f_0) for general f (Lipschitz bound for log L̃⁴G) is still not computed. Status unchanged. See DISC-0205.

## Note (2026-10-31, appended; text above unchanged)
CF.3's constant C_G is now explicit on the Birkhoff route by IFI Theorem DC at 4996a9fca8782a8a80ceb41494872f85dacbb55d (DISC-0215): |log(s_{k+1}/(rs_k))| ≤ θ^{⌊(k−4)/5⌋}·0.28154093 ≤ 0.74544057·θ^{k/5} for k ≥ 4, and for a general f with b-Lipschitz log, θ^{⌊(m−j)/5⌋}K(β_j) with explicit K. Status unchanged.
