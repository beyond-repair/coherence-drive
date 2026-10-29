# Discovery: Theorem CE, exact geometric ratio of ν's level sums via a twisted transfer operator

## Discovery ID
DISC-0188

## Status
THEOREM (mathematical sense only; analytic proof plus an exact-rational Bernstein certificate for the digits; conditional on Birkhoff's cone contraction theorem, a classical result the repository cites as Assumption CE). Method KNOWN (Ruelle–Perron–Frobenius transfer operator, Birkhoff/Hilbert-metric cone contraction, Collatz–Wielandt bounds). Novelty of the constant r and of this twisting device for this measure UNRESOLVED.

## Date Discovered
2026-10-29 (indexed ~2:58pm EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit a056d01a82828425e6ddb624b13c31cbb737156a (2026-10-29 14:12:36 EDT).

## Original Evidence
- GASKET.md, section "Theorem CE" (line 3421), proof from line 3451, Observation (no claim) line 3465.
- scripts/gasket_fractional_profile_level_ratio.py (new, 397 lines); scripts/cli.py and tests/test_cli.py hooks; CLAIM_STATUS.md row (line 87); README.md.
- Answers the level-sum ratio 0.42373… that Theorem CC (DISC-0186) observed and Theorem CD (DISC-0187) explicitly left open.

## Discovery
With p(z)=z(z+5), O the backward orbit of −3, one scale period I=(p(a),a], a=ψ(−1), and level sums s_k=Σ_{t∈O_k∩I} λ_t^(−γ) ν({λ_t}):
1. CE.1: the masses factor multiplicatively along O: σ_y=w(y)σ_{p(y)} with σ_t=1/H'(t), w(y)=(y+2)(y+5)/((y+6)(2y+5)), σ_{−3}=0.55919355244702178956…, so s_k=σ_{−3}(L^kG_0)(−3) for the transfer operator (Lh)(t)=Σ_{p(y)=t} w(y)h(y).
2. CE.2: twisting by q(t)=−t gives an operator L̃ on X=[−5,0] with weights w̃_1=(s+½)/(2s(7/2−s)), w̃_2=(s−½)/(2s(s+7/2)), s=√(t+25/4), both strictly positive and analytic on X, with w̃_1+w̃_2=4/(6−t).
3. CE.3: s_(k+1)/s_k → r = spectral radius of L̃, exponentially fast, and the same limit holds for any positive C¹ weight in place of λ^(−γ); δ_K/s_K → r/(1−r); mean mass per level-k atom has ratio r/2.
4. CE.4: r = 0.42373128696260793985253216132843923…, certified by exact-rational Bernstein bounds lo·f ≤ L̃f ≤ hi·f with hi−lo = 2·10^(−38).

## Why It Matters
Completes the level-by-level description of the pure point measure ν (DISC-0186): CD gave the atom counts per level, CE gives the exact geometric decay of the mass per level and identifies its rate as a transfer-operator eigenvalue that does not involve ψ.

## Derivation
As in the repository (GASKET.md lines 3451–3461): CE.1 from H=c·H∘p differentiated at points of O; CE.2 by substitution φ_{1,2}=−5/2∓s; CE.3 from a Lipschitz-log cone C_b, |φ_i'|=1/(2s)≤1/√5, finite projective diameter, then Birkhoff contraction; CE.4 from Collatz–Wielandt with a degree-48 rational polynomial f. Not re-derived independently beyond the checks below.

## Assumptions
- Birkhoff's contraction theorem (Assumption CE; classical).
- CB.2, CB.5, CC.4, CD.2–CD.3 and the BZ/CA/CB/CC enclosure routines, imported unchanged by the repository.

## New Results
- Archive observation (not a repository claim): both twisted weights and their sum 4/(6−t) were re-derived symbolically from w; w(0)=1/3 and w(−5)=0 confirmed exactly. The sum 4/(6−t) shares the (6−t) denominator of CC's Herglotz transfer weight (2−t)/(6−t) (DISC-0186); whether that is more than a shared pole at the decimation value 6 was not investigated.

## Prior Art
Transfer operators with positive weights over the inverse branches of an expanding interval map, their Perron–Frobenius eigenvalue as a decay rate of weighted preimage sums, and Birkhoff cone contraction (Birkhoff 1957; Liverani 1995 style cones) are textbook material. Twisting by a positive function (a coboundary / ground-state conjugation) to remove a vanishing weight is a standard device. Spectral-decimation measures on the gasket (Fukushima–Shima 1992; Teplyaev 1998) are related; no source giving this r was found in this run, and no literature search for the constant was done.

## Novelty Analysis
Method KNOWN. The constant r and the explicit twisted weights for this specific corner measure appear only in this repository as far as checked; novelty UNRESOLVED. The repository's own integer-relation search found no closed form; that is not evidence none exists.

## Falsification Attempts
1. Repository witness at a056d01a82828425e6ddb624b13c31cbb737156a: all checks pass, EXIT 0 (24.3 s wall).
2. Independent archive script discoveries/mathematics/scripts/indep_theorem_CE.py (sympy + mpmath, no repository code): re-derives w̃_1, w̃_2 from w and q (difference 0), the sum identity 4/(6−t) (difference 0), w̃_i(0)=3/5, 1/15, w(0)=1/3, w(−5)=0; builds its own barycentric Chebyshev collocation of L̃ on 40 and 60 nodes at 50 digits. Result: r=0.42373128696260793985253216132843923183 (60 nodes), |r−claim| = 1.8·10^(−36); second eigenvalue −0.0731138175123996, matching the repository's uncertified observation. PASS.
3. Proof attack: the cone argument needs strict positivity of the weights on all of X, which holds since s∈[√5/2, 5/2] keeps s±½, 7/2±s positive; the removable singularity at t=0 is genuine (values above). The untwisted operator does fail, as the repository itself records (DISC-0189). No gap found.

## Experimental Validation
Pure mathematics; numerics reproduced independently to 36 digits.

## Mathematical Status
Theorem (analytic proof given classical Birkhoff contraction; digits by exact-rational certificate).

## Patent Relevance
None. Pure mathematics about a graph Laplacian's spectral measure. The repository states it is not a flux or thrust claim.

## Related Discoveries
- DISC-0186 (Theorem CC): ratio observed there, now proved.
- DISC-0187 (Theorem CD): counts per level; CE gives masses per level. Its "Next Experiments" item is answered (as a transfer-operator eigenvalue, not a closed expression).
- DISC-0185 (Theorem CB): product masses used in CE.1.
- DISC-0189: Kept Failure CE.6 (untwisted route).

## Open Questions
- Closed form of r. Certified second eigenvalue of L̃ (float value −0.07311381751…).
- Repository's carried list: closed form of ψ, exact liminf ρ_k, θ̂_k≠0 for k≥22.

## Next Experiments
- Certify λ_2 with a deflated Collatz–Wielandt or interval Galerkin bound.
- Test whether r is algebraic of higher degree than the repository's search (degree ≤8).

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at a056d01a82828425e6ddb624b13c31cbb737156a; pip install python-flint mpmath sympy; run `python3 scripts/gasket_fractional_profile_level_ratio.py` (about 25 s). Then run `python3 discoveries/mathematics/scripts/indep_theorem_CE.py` from this archive (about 25 s).

## Evidence Log
- 2026-10-29 ~2:58pm EDT. Indexed from commit a056d01a82828425e6ddb624b13c31cbb737156a. Repo witness EXIT 0 (24.3 s); independent check PASS (r to 1.8e−36).

## Change History
- 2026-10-29. Initial archive entry.
