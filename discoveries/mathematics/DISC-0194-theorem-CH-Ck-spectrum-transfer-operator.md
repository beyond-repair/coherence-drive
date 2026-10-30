# Discovery: Theorem CH, the C^k spectrum of the level-sum transfer operator, and Kept Failure CH.4 (λ_2 is not the second C¹ eigenvalue)

## Discovery ID
DISC-0194

## Status
THEOREM in the mathematical sense only (computer-assisted with arb interval arithmetic; conditional on Hennion's theorem, cited as Assumption CH). Method KNOWN. Constants novelty UNRESOLVED. CH.4 is a proved negative result recorded by the repository as a Kept Failure; its mechanism is KNOWN.

## Date Discovered
2026-10-30 (commit time 2026-10-29 22:58 EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 127df7ca9fb82f0bb0ec70766b3eb3dcd1862009

## Original Evidence
- GASKET.md "## Theorem CH" (line 3585), CH.1–CH.4, proof and Kept limits.
- CLAIM_STATUS.md new row "Spectrum of the level-sum transfer operator on C^k(X)".
- scripts/gasket_fractional_profile_level_regularity.py (added, 291 lines); tests/test_cli.py, scripts/cli.py, README.md updated.

## Discovery
Same operator as DISC-0188/0190/0191: in s=√(t+25/4), (L̃f)(s)=w̃_1 f(σ_1 s)+w̃_2 f(σ_2 s), σ_{1,2}=√(15/4∓s) on X=[√5/2, 5/2]. The branch images leave a gap G=(g_a,g_b)=(1.62233…, 2.20636…).
- CH.1 (exact): |σ_i'|σ_i=1/2, w̃_1+w̃_2=16/(49−4s²).
- CH.2 (arb Collatz–Wielandt): ρ(L_k) ≤ 0.1345, 0.0432, 0.01396, 0.00454 for weights w̃_i|σ_i'|^k, k=1..4.
- CH.3: by Hennion, outside those radii the C^k(X) spectrum is exactly CG's H² eigenvalues with multiplicity. So λ_2 is the second eigenvalue on C², and every C¹ eigenvalue μ≠r has |μ|<0.1345<0.3175 r (improves CF.5's 0.8855 r).
- CH.4 (Kept Failure): on C¹(X) every |μ|≤0.1089 is an eigenvalue. L̃ never reads G, so a C¹ bump g supported in G has L̃g=0; an explicit right inverse K (L̃K=I) with certified majorant ρ(A)<9.18 makes v=Σμ^nK^ng a C¹ eigenfunction. Hence ±1/10, ±1/12 are C¹ eigenvalues with modulus above |λ_2|, and λ_2 is not the second C¹ eigenvalue.

## Why It Matters
It answers DISC-0191's open question "whether λ_2 is second on C¹(X)": no on C¹, yes on C^k for k≥2. The level-sum rate C·0.17255^k from CG.4 is untouched, because it concerns an analytic vector.

## Derivation
Repository proof (GASKET.md Theorem CH): Faà di Bruno gives a Lasota–Yorke inequality ‖L̃^n f‖_{C^k} ≤ ‖L_k^n 1‖‖f‖_{C^k}+B_n‖f‖_{C^{k−1}}; Hennion bounds the essential radius; Riesz projections commute with the restriction H²(D)→C^k(X), and density of polynomials matches the eigenvalues. CH.4: L̃v=Σμ^n L̃K^n g = L̃g + μΣμ^{n−1}K^{n−1}g = μv.

## Assumptions
- Hennion 1993 (Proc. AMS 118, 627–634), cited not reproved.
- CG.1–CG.3 constants imported (not re-run by CH; CG itself was verified for DISC-0191).
- The proof text of CH.3 in GASKET.md ends mid-sentence ("…dense in C^k(X). So") before the Observation paragraph. The remaining step (equal multiplicities from the finite-rank projections) is standard, but the printed proof is truncated. Presentation erratum, not a mathematical failure.

## New Results
For this archive: DISC-0191's open C¹ question is closed in the negative; the C¹ subdominant spectrum lies in 0.1089 ≤ sup|μ| ≤ 0.1345 (ratio to r in [0.2569, 0.3175]).

## Prior Art
- Ruelle 1989 and Collet–Isola 1991 (Commun. Math. Phys. 139): for expanding maps the C^k essential spectral radius is governed by ρ(L_k), and the C¹ spectrum can fill a disk. The repository's own Observation names Collet–Isola.
- Hennion 1993; Lasota–Yorke; Baladi, "Positive Transfer Operators and Decay of Correlations" (2000).
- A transfer operator of a non-onto (gapped) IFS having a kernel and hence every small μ as eigenvalue on C^k is a standard mechanism.
Constants specific to this operator: not found in a search; search not exhaustive.

## Novelty Analysis
Method KNOWN. Only the specific certified radii for this gasket-derived operator could be new; UNRESOLVED.

## Falsification Attempts
- Recomputed ρ(L_k), k=0..4, by power iteration on a 4001-point grid: 0.4237313, 0.1343550, 0.0430703, 0.0139193, 0.0045265, matching the repo floats and below each certified bound.
- Checked L̃Kf=f pointwise (error <1e−12), L̃g=0 exactly, gap endpoints, ρ(A)=9.1788910 and 0.1089·ρ(A)<1.
- Tried to break CH.3 against CH.4: consistent, since 0.1089 < 0.1345 = the C¹ essential bound. No failure found.

## Experimental Validation
Repo witness `python3 scripts/gasket_fractional_profile_level_regularity.py` EXIT 0 (2.0 s), all checks passed. Independent `indep_theorem_CH.py` 12/12 PASS (floats and sympy only; does not re-certify the arb covers).

## Mathematical Status
Theorem (computer-assisted, conditional on a cited classical theorem). C¹ spectrum in 0.1089<|z|≤0.1345 OPEN.

## Patent Relevance
None. Pure spectral theory; the repository states it is not a flux and not thrust.

## Related Discoveries
- DISC-0191 (Theorem CG): CH lifts CG's eigenvalues to C^k, k≥2, and shows they are not the full C¹ picture.
- DISC-0190 (Theorem CF): CF.5's C¹ bound 0.8855 r improved to 0.3175 r.
- DISC-0188 (Theorem CE): same operator L̃ and r.

## Open Questions
- Exact C¹ essential radius (float ρ(L_1)=0.1343550) and the C¹ spectrum in 0.1089<|z|≤0.1345.
- Explicit C_G; whether B≠0 in CG.4.

## Next Experiments
- Certify a lower bound for the C¹ essential radius matching ρ(L_1) (close the 0.1089 to 0.1345 window).

## Reproduction Instructions
`git clone https://github.com/beyond-repair/informational-flux-identity && git checkout 127df7ca9fb82f0bb0ec70766b3eb3dcd1862009 && python3 scripts/gasket_fractional_profile_level_regularity.py`; then `python3 discoveries/mathematics/scripts/indep_theorem_CH.py` from this repository.

## Evidence Log
- 2026-10-30 ~12:05am EDT. Verified from 127df7ca9fb82f0bb0ec70766b3eb3dcd1862009: repo witness EXIT 0; independent check 12/12 PASS.

## Change History
- 2026-10-30: created.

## Note (2026-10-30, DISC-0195)
Theorem CI (IFI 80f30b8a01728fb48e805b8163cde04b979075dd) narrows the C¹ open band (0.1089, 0.1345] to (0.1343547, 0.1343551] and certifies r_ess(C¹)=ρ(L_1) to 4·10⁻⁷. Status of DISC-0194 unchanged. The CH.3 truncation erratum is still present at GASKET.md line 3610.

## Correction (2026-10-30, retraction of erratum)
The erratum claiming CH.3's printed proof breaks off after "dense in C^k(X). So" is retracted: at 127df7ca9fb8 the sentence continues and the proof is complete ("…So Π_{C^k} maps them onto a dense subset of its finite-dimensional range, that is, onto the whole range, and that range lies in R(ran Π_{H²}). The two ranks are therefore equal."). The earlier reading was truncated by a display limit. Status unchanged. Also: Theorem CJ (DISC-0196) completes the C¹ picture.
