# Discovery: Theorem BV, the log-periodic profile F=θ is holomorphic and bounded on the strip |Im t|<π/ln5, so |θ̂_k|≤B_k~e^(−2π²k/ln5); θ̂_5..θ̂_11 certified nonzero; F has exactly one maximum and one minimum per period, located to ~1e−55

## Discovery ID

DISC-0173

## Status

THEOREM in the mathematical sense only (repository proof; BV.4–BV.5 computer-assisted with outward mpmath.iv and python-flint arb). Method KNOWN (sector bound for Stieltjes functions, Vitali continuation, contour shift for Fourier coefficients of a function holomorphic in a strip, certified critical-point counting). The specific strip width, constants and extremal locations: novelty UNRESOLVED (not searched). Closed form of F=θ: UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~6:56pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit cec4aff731cef6bb581c318f736de79d68d90b1f (committed 2026-10-23 6:17pm EDT).

## Original Evidence

GASKET.md Theorem BV (heading line 2975; BV.1 line 2981; BV.2 line 2982; BV.3 line 2987; BV.4 line 2992; BV.5 line 3005; Kept Failure BV.5 line 3017; Conjecture BV.6 line 3019; proofs lines 3021–3029; open list line 3032; NOT THIS fence line 3036; evidence lines 3040–3042), CLAIM_STATUS.md new row (line 78), README.md, scripts/gasket_fractional_profile_analytic.py (new, 370 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in BS/BT/BU (DISC-0168, DISC-0170, DISC-0171): F(t)=5^((1−γ)t)Q_∞(5^t)=θ(5^t), 1-periodic in t=log_5 u, θ̂_k its Fourier coefficients, G*=max F.

- BV.1: every Stieltjes f=c+∫dμ(λ)/(λ+z) satisfies |f(z)|≤f(|z|)/cos(φ/2), φ=arg z, from |λ+z|²−(λ+|z|)²cos²(φ/2)=(1−cos φ)(λ−|z|)²/2.
- BV.2: BN.1's r_k are Stieltjes and increase to r_∞, so by Vitali r_∞ and Q_∞ continue holomorphically to ℂ∖(−∞,0] with the same bound; F is holomorphic and 1-periodic on |Im t|<π/ln5 with |F(x+iy)|≤F(x)/cos(y ln5/2)≤G*/cos(y ln5/2).
- BV.3: shifting the contour, |θ̂_k|≤B_k=G*√(1+T_k²)e^(−T_k arctan T_k)≤eG*(1+T_k)e^(−2π²k/ln5), T_k=4πk/ln5; so limsup|θ̂_k|^(1/k)≤e^(−2π²/ln5)=4.7155e−6.
- BV.4 (certified, AU (3)'s routine with new parameters, 170 digits): ⟨F⟩ to ±4.1e−63, a_k,b_k to ±8.2e−63 for k≤11; θ̂_k≠0 for every k≤11 (AU had k≤4); |θ̂_k|≤B_k for k≤11.
- BV.5 (certified, arb 400 bits, 4096 cells, with BV.3's tail beyond k=11): F′ changes sign exactly twice per period; t_max=0.751755961790317558778029332738…(±9.1e−56), t_min=0.251756124192213928849302877000…(±3.5e−55), G*=0.600961578597101089042056184134616926770…(±4.5e−61), min F=0.600946923794265612104226188172129248411…(±6.7e−61).
- Kept Failure BV.5 (DISC-0174) and Conjecture BV.6 (DISC-0175) recorded separately.

## Why It Matters

Answers three of BU's (DISC-0171) open questions: the upper half of the decay rate of |θ̂_k|, θ̂_k≠0 up to k=11, and the location of the extremes. G* (the sharp BI.4 constant, DISC-0151/0170) is now known to ~60 digits, and the extremes' half-period offset I flagged as a next experiment in DISC-0171 is now certified non-zero.

## Derivation

Repository proof (GASKET.md lines 3021–3029). Checked here: the BV.1 identity (sympy); the BV.3 optimisation (dy of −2πky−log cos(y ln5/2) vanishes at tan(y ln5/2)=4πk/ln5, giving B_k; the e(1+T) envelope uses √(1+T²)≤1+T and e^(−T arctan T)≤e·e^(−πT/2), since T(π/2−arctan T)=T·arctan(1/T)≤1); BV.5 is outward interval arithmetic over a trig polynomial plus a tail bound.

## Assumptions

As stated in the repository and not re-run there: AQ (3), BN.1, BS.1, BT.2, BU.1, BU.3 (G*≤0.6009615785983); AU (3)'s certified routine (AQ (4) node enclosures, AS (2) sandwich, AT.1 orbit lemma, AU's ψ and endpoint corrections) imported unchanged with new parameters. AU's table and BU.3/BU.4 brackets for consistency only.

## New Results

- Fourier data of F with exponential-decay guarantee: |θ̂_k|/B_k falls from 0.061 (k=1) to 0.0050 (k=11) (my floats match the repo's printed ratios).
- G* and min F to ~60 digits; max F−min F=1.4654802835476937830e−5.
- Observation of mine (floats, not a repo claim): the printed |θ̂_11|≥1.807336e−59 is a valid but loose lower bound; my 110-digit float value is 1.808283e−59 (the gap, 9.5e−63, is of the order of the printed coefficient radius). Not an erratum.

## Prior Art

Analyticity of the periodic factor in a strip and exponentially decaying Fourier coefficients for log-periodic oscillations of self-similar Green functions/partition functions are KNOWN in kind (Grabner–Woess 1997 on the Sierpinski graph; Mellin–Perron/Flajolet-style analyses of periodic fluctuations). The Stieltjes sector bound and Vitali's theorem are textbook. No search for these specific constants.

## Novelty Analysis

Method KNOWN; this strip width, these constants and the extremal locations were not located in prior work but were not searched: UNRESOLVED.

## Falsification Attempts

Independent mpmath script /workspace/scratch-ifi/indep_theorem_BV.py on the box (own η-series r_∞, no repo code imported, 110 digits, depth 5^−150, 32-node rectangle rule, whose aliasing error is ~|θ̂_21|), 16/16 PASS:
- BV.1 identity (sympy plus spot values).
- BV.2 directly on r_∞ (not just r_0..r_3): |r_∞(z)|cos(φ/2)/r_∞(|z|)≤0.9948 at 30 complex points, |z|=1e−4..20, arg z up to 0.97π.
- θ̂_1..θ̂_11 all far above noise; |θ̂_5|=1.698341145e−27, |θ̂_8|=1.648056069e−43, |θ̂_11|=1.80828e−59, each ≥ the printed lower bound; |θ̂_k|≤B_k for all k≤11; |θ̂_k|e^(2π²k/ln5)∈[0.6066,0.9268].
- BV.3 closed form of the optimum checked against perturbed y, and the envelope; e^(−2π²/ln5)=4.71548e−6.
- ⟨F⟩=0.6009542511687736078… inside BU.3's bracket.
- Extremes from the 13-mode trig polynomial: F′ has exactly two sign changes on a 512-grid; Newton t_max, t_min agree with the printed values to <1e−35; max F and min F agree to <1e−50; (max F+min F)/2−⟨F⟩=2.6909742749436036e−11 as printed.
- First run had 2 FAILs, both my own tolerances (I compared ⟨F⟩ to a truncated constant and demanded the lower bound be within 1e−5 relative); corrected to the BU bracket and to "≥ printed lower bound, within 0.1%". Not a repository defect.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness scripts/gasket_fractional_profile_analytic.py EXIT 0 (46.0 s, "all Theorem BV checks passed"; /workspace/scratch-ifi/repo_theorem_BV.log on the box); archive indep_theorem_BV.py 16/16 PASS. Repo reports pytest -k "not reproduce": 35 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) with computer-assisted certified constants (interval enclosures not re-certified here; reproduced in 110-digit floats).

## Patent Relevance

None. Pure mathematics on a graph; the repository's NOT THIS fence says it is not a flux, force or thrust.

## Related Discoveries

DISC-0171 (Theorem BU; answers its open decay, θ̂_k≠0 and extremes questions), DISC-0116 (Theorem AU; routine reused, table extended to k=11), DISC-0161 (Theorem BN; Stieltjes r_k), DISC-0170 (Theorem BT), DISC-0151 (BI.4 constant now G* to ~60 digits), DISC-0172 (Kept Failure BU.4), DISC-0174 (Kept Failure BV.5), DISC-0175 (Conjecture BV.6).

## Open Questions

Closed form of F=θ (hence c_∞, C_N, P_N, χ_∞, G*, t_max, t_min); θ̂_k≠0 for k≥12; Conjecture BV.6 (lower half of the rate; whether Q_∞ has poles on (−∞,0)); feeding G* back into BI.4/BJ.

## Next Experiments

Locate singularities of the continued r_∞ on the negative axis (e.g. zeros of 2+s−2η(s)) to test whether the strip π/ln5 is maximal; extend the certified table past k=11.

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout cec4aff731cef6bb581c318f736de79d68d90b1f
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_analytic.py   # needs mpmath, sympy, python-flint
```

## Evidence Log

- 2026-10-23 ~6:56pm EDT. Indexed; repo witness EXIT 0 (46.0 s); independent checks 16/16 PASS after fixing two of my own tolerances; no erratum.

- 2026-10-29 ~1:00am EDT. Note: Theorem BW (IFI 14686342bd14, DISC-0176) extends BV.4 to k≤20 and BV.5's extremes to ~109 digits, all agreeing with BV's printed digits; no status change. Erratum found while checking BW: BV's printed |θ̂_k|≥ column rounds to nearest, so k=6 (8.621962e−33 vs float 8.6219618346e−33) and k=7 (4.321505e−38 vs 4.32150483175e−38) print values slightly above the true modulus; my BV check had only tested k=5, 8, 11. θ̂_k≠0 is unaffected. The 'No erratum' line in New Results above stands for k=11 only.

- 2026-10-29 ~1:57am EDT. Note: Theorem BX (IFI 06eddfa75600, DISC-0177) replaces BV.3's B_k by the exact-factorisation bound ⟨F⟩ sin πγ/|sin π(γ+iωk)|, 12.7–252.7 times smaller for k≤20, with sharp limsup constant πc_R(γ)/ln5=1.00949802…; no status change.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-29. Note added for DISC-0176 (history above kept unchanged).
- 2026-10-29. Note added for DISC-0177/0178 (history above kept unchanged).
