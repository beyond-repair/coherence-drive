# Discovery: Theorem BU, the log-periodic profile F=u^(1−γ)Q_∞ of Theorems BS/BT is AU's θ itself (ψ_AU inverts BD.4's ψ), so F̂_k=θ̂_k for every k, and a convexity (chord) cell certificate pins max F, min F, ⟨F⟩ and F̂_1, F̂_2 to about 1e−12

## Discovery ID

DISC-0171

## Status

THEOREM in the mathematical sense only (repository proof; constants computer-assisted with python-flint arb). Method KNOWN (Koenigs-type linearising coordinate and its inverse for a map with a repelling/attracting fixed point at 0; chord/tangent sandwich for a convex function; closed-form cell integrals). The specific identification of BS's profile with AU's θ, and the sharpened constants: novelty UNRESOLVED (not searched). Closed form of F=θ: UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~5:58pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit ad459e306e19ac3ac4f1e3a74f6e7738ac9b5195 (committed 2026-10-23 5:14pm EDT).

## Original Evidence

GASKET.md Theorem BU (heading line 2923; BU.1 line 2931; BU.2 line 2936; BU.3 line 2937; Kept Failure BU.4 line 2950; proofs of BU.1–BU.3 lines 2952, 2954, 2956; float evidence line 2958; "What stays open" line 2960; NOT THIS fence line 2965), CLAIM_STATUS.md new row (line 77), README.md, scripts/gasket_fractional_profile_fourier.py (new, 295 lines), scripts/cli.py, tests/test_cli.py.

## Discovery

Setting as in AQ, AT, AU, BD, BN, BT: p(s)=s(s+5), q=p^−1, γ=log3/log5, g=s^(1−γ)r_∞, Θ=lim g∘q^k (BT.1), F(u)=u^(1−γ)Q_∞(u)=Θ(ψ(u)) (BT.2), ψ=ψ_BD=lim p^k(5^−k ·), ψ_AU=lim 5^k q^k, θ=Θ∘ψ_AU^−1 (AU), θ̂_k=a_k−i b_k on one period in log_5.

- BU.1: BD.4 gives q^k(ψ(v))=ψ(5^−k v)∈[5^−k v, 5^−k v e^(5^−k v/10)], so ψ_AU(ψ(v))=v; AU's bound s(log A_∞)′≤s/20 (Σ5^−i/5=1/20) makes ψ_AU strictly increasing, so ψ_AU^−1=ψ and F=θ identically. Hence F̂_k=θ̂_k for every k∈ℤ (AU certified k≤4 nonzero), and AU (2)'s Mellin residues of r_∞ are the Fourier coefficients of BS's profile.
- BU.2: r_∞ is convex and decreasing (limit of Stieltjes r_k, BN.1), so on each cell the chord through node ceilings is a ceiling and the neighbouring chords extended into the cell are floors; v^(1−γ)(c+dv) with c>0>d is strictly concave, extremes at ends, at a floor crossing, or at v*=−(1−γ)c/((2−γ)d); log-integral and Mellin moments in closed form. Cell errors O(h²) instead of BT.4's O(h).
- BU.3 (certified, outward, 2^18 cells, depth 5^−30): max F=G*=sup s^(1−γ)r_∞ ∈ [0.6009615785971, 0.6009615785983]; min F ∈ [0.6009469237907, 0.6009469237943]; ⟨F⟩ ∈ [0.60095425116719, 0.60095425116956] ∋ AU's 34-digit ⟨Θ⟩; max F−min F ∈ [1.4654802832, 1.4654807576]e−5; a_1 ∈ [4.042159, 4.042397]e−8, b_1 ∈ [−3.663479, −3.663477]e−6, a_2 ∈ [−1.465995, −1.228463]e−11, so F̂_1, F̂_2 ≠ 0 from F's own nodes, independently of AU.
- Kept Failure BU.4: half-period antisymmetry F(t+1/2)=2⟨F⟩−F(t) is false (recorded separately as DISC-0172).

## Why It Matters

BT (DISC-0170) left open whether BS's profile and AU's θ share Fourier modes beyond the mean. BU proves they are the same function, so every certified fact about θ (AU, DISC-0116) is now a fact about c_∞, C_N, P_N, χ_∞ and G* (DISC-0167, DISC-0168), and narrows BT.4's extremal brackets from width 1.6e−6 to 1.2e−12 and 3.6e−12.

## Derivation

Repository proof (GASKET.md lines 2952–2956), checked step by step here: BU.1 is a composition of the two limit definitions plus a monotonicity bound on ψ_AU; BU.2 rests on r_k′<0<r_k″ for Stieltjes functions (sympy in the repo), passes to the limit, and on the sign of φ″; BU.3 is outward arb arithmetic over the cell sandwich.

## Assumptions

As stated in the repository and not re-run there: AQ (3), BN.1, BJ.1, BH.2, BD.4 with BJ.6, AU's setting (ψ_AU=s/A_∞, ψ_AU∘q=ψ_AU/5, 0≤s(log A_∞)′≤s/20), BT.1–BT.2, BI.4 (G=0.6031). AU's table and BT.4's brackets for consistency only.

## New Results

- Every Fourier mode of BS's profile is AU's: |F̂_3|=|θ̂_3|≥8.82e−17 (AU), so BT's float |F̂_3|=4.2e−16 was noise (the repo says so).
- G* (the sharp BI.4 constant) is now known to 12 digits.
- Float observation of mine (not a repo claim): with depth 5^−44 the refined argmax and argmin in t=log_5 u are 0.7517559618 and 0.2517561242, separated by 0.4999998376, not exactly 1/2; consistent with DISC-0172.

## Prior Art

Koenigs linearisation and its use for periodic oscillations in renormalisation/self-similar Green-function asymptotics are KNOWN (e.g. Grabner–Woess 1997 for the Sierpinski graph; standard holomorphic dynamics). Convex chord sandwiches for certified integration are KNOWN. No search for these specific constants.

## Novelty Analysis

Method KNOWN; identification and constants not located in prior work but not searched: UNRESOLVED.

## Falsification Attempts

Independent mpmath script (/workspace/scratch-ifi/indep_theorem_BU.py on the box; own η-series r_∞ at 40 digits), 18/18 PASS:
- ψ_AU(ψ_BD(v))=v at 27 points v=1e−6..700 to 2.3e−40; ψ_AU strictly increasing on 181 points; Σ5^−i/5=1/20 (sympy).
- F(u)=g(5^−30 u) agrees with Θ(ψ(u)) via q^40 to 2.5e−15, the expected O(3^−30) depth truncation.
- sympy: v^(1+γ)φ″=−(1−γ)γc+(2−γ)(1−γ)dv (negative for c>0>d) and v*=−(1−γ)c/((2−γ)d).
- r_∞ decreasing and convex (slopes increasing) on 111 points s=1e−8..1e3.
- 4096-node rectangle rule at depth 5^−44: ⟨F⟩=0.600954251168774, a_1=4.0422781e−8, b_1=−3.6634777e−6, a_2=−1.3472218e−11, b_2=6.3749789e−13, all inside the certified brackets and matching AU's table to ≤1e−16 (a float check of BU.1 by a different route than the repo's).
- Ternary-refined max F=0.6009615785971011 and min F=0.6009469237942656, both inside BU.3's brackets.
- Attack on the BU.4 bracket: from the printed outward brackets alone the lower end is exactly 2.4340e−11>0; the naive upper end is 2.911e−11, looser than the printed 2.9084e−11 (the repo combines unrounded arb enclosures). Consistent, no erratum.
- First run had 5 FAILs, all mine: depth 5^−30 floats carry a ~1e−15 one-sided bias (g underestimates Θ by O(s^γ)), and I had combined rounded brackets naively. With depth 5^−44 and the corrected bracket comparison, 18/18 PASS. Not a repository defect.

## Experimental Validation

Not applicable (pure mathematics on a graph). Computational: repo witness EXIT 0 (64.4 s, "all Theorem BU checks passed"; /workspace/scratch-ifi/repo_theorem_BU.log on the box); archive indep_theorem_BU.py 18/18 PASS (log beside it). Repo reports pytest -k "not reproduce": 34 passed (not re-run here).

## Mathematical Status

Theorem (repository proof) with computer-assisted certified constants (arb enclosures not re-certified here; reproduced in floats).

## Patent Relevance

None. Pure mathematics on a graph; the repository's NOT THIS fence says it is not a flux, force or thrust.

## Related Discoveries

DISC-0170 (Theorem BT; answers its open F̂_k=θ̂_k and narrower-bracket questions), DISC-0116 (Theorem AU; θ is now BS's profile), DISC-0168 (Theorem BS), DISC-0167 (Theorem BR, c_∞), DISC-0151 (Theorem BI, G sharp at G*), DISC-0161 (Theorem BN, Stieltjes r_k), DISC-0172 (Kept Failure BU.4).

## Open Questions

Closed form of F=θ (hence c_∞, C_N, P_N, χ_∞, G*); θ̂_k≠0 for k≥5 and the decay rate of |θ̂_k|; exact location of the extremes; Conjecture BS.4 (DISC-0169).
- 2026-10-23 note (no status change): DISC-0173 (Theorem BV, cec4aff731ce) answers the upper half of the decay rate (|θ̂_k|≤B_k~e^(−2π²k/ln5)), θ̂_k≠0 for k≤11, and the extremal locations; the half-period-offset next experiment is closed by DISC-0174 (offset −1.624e−7, not zero).

## Next Experiments

Certify the half-period offset of the extremes (float 0.4999998376) to settle whether it is exactly 1/2 minus a computable shift; push the cell certificate to k=3,4 (radius 1.19e−12 is far above |θ̂_3|).

## Reproduction Instructions

```
git clone https://github.com/beyond-repair/informational-flux-identity
git -C informational-flux-identity checkout ad459e306e19ac3ac4f1e3a74f6e7738ac9b5195
cd informational-flux-identity && python3 scripts/gasket_fractional_profile_fourier.py   # needs sympy, python-flint
```

## Evidence Log

- 2026-10-23 ~5:58pm EDT. Indexed; repo witness EXIT 0 (64.4 s); independent checks 18/18 PASS after fixing my own float depth and bracket arithmetic; no erratum.

## Change History

- 2026-10-23. Initial archive entry.
- 2026-10-23 ~6:56pm EDT. Note added under Open Questions (DISC-0173/DISC-0174); original text unchanged.
