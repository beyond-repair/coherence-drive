# Discovery: Theorem CD, exact level counts of ν's atoms in one scale period

## Discovery ID
DISC-0187

## Status
THEOREM (mathematical sense only; elementary proof in the repository, endpoint orbit inequalities computer-assisted with arb). Method KNOWN (counting preimages of a real quadratic map in an interval by tracking the endpoint orbit). Novelty of the specific counts UNRESOLVED.

## Date Discovered
2026-10-29 (indexed ~12:56pm EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 09936074caa80ac880fdd1cd28b5730b9b1b6bee (2026-10-29 12:07:16 EDT).

## Original Evidence
- GASKET.md, section "Theorem CD" (line 3377), proof from line 3393.
- scripts/gasket_fractional_profile_level_counts.py (new, 204 lines); scripts/cli.py and tests/test_cli.py hooks; CLAIM_STATUS.md row (line 86).
- Builds on Theorem CC (DISC-0186, cb00b500b900), which certified the counts for k≤14 only as an observation.

## Discovery
With p(z)=z(z+5), O_k=p^−k(−3), a=ψ(−1)=−0.95082664382932600… and one scale period I=(p(a),a], the number of level-k atoms N_k=#(O_k∩I) is exactly 1, 0, 1, 3 for k=0..3 and 5·2^(k−4) for k≥4. One period holds exactly 5·2^(K−3) atoms of level ≤K (10240 at K=14, as CC.4 certified).

## Why It Matters
Turns CC's observed atom counts into a proof for every level, so the atom set of the pure point measure ν (DISC-0186) has a fully explicit level structure: the level-k atoms are a fixed fraction 5/16 of the 2^k points of O_k for k≥4.

## Derivation
1. CD.1: p(y)=t iff y=−5/2∓√(t+25/4); for t∈(−25/4,0) the two roots are distinct and lie on opposite sides of −5/2 inside (−5,0). Induction from −3 gives #O_k=2^k, all in (−5,0)∖{−5/2}.
2. CD.2 (certified): −5<a₂<a₁<−3<a₃<−5/2<a<0 and a₄=p⁴(a)<−5, where a_j=p^j(a). The endpoint orbit leaves [−5,0] in four steps.
3. CD.3: on each side of −5/2, p is a monotone bijection onto [−25/4,0], so C_m(J)=C_(m−1)(p(J)). Following the four images of the endpoint gives N_k=A_(k−1)+B_(k−1), A_m=G_(m−1), B_m=F_(m−1), G_j=E_(j−1)+2^(j−1), E_j=F_j=2^(j−1), with level-0 values fixed by where −3 sits. This closes to N_k=5·2^(k−4) for k≥4. No interval endpoint lies in O (a∈O would make λ=1 an atom, which CC.4 excludes).

## Assumptions
- CC.4 (one period parametrised by ψ on [−5,−1], ψ strictly increasing; atom set level by level), BD.4, BJ.6 and CA's psi_enc enclosure, all imported unchanged by the repository and not re-run here.
- The value of a=ψ(−1) to 17 digits is taken from the repository's certified enclosure.

## New Results
- The level counts for all k (previously certified only for k≤14).
- Archive observation (not a repository claim): across all levels k≤20, the closest point of O_k to either endpoint of I is 0.0147 away, consistent with the endpoint orbit escaping [−5,0] after four steps, so the counts are robust to the 17-digit value of a.

## Prior Art
Counting preimages of a real polynomial in an interval via the orbit of the interval's endpoints is standard one-dimensional symbolic dynamics (kneading-style bookkeeping). The quadratic p(z)=z(z+5) is the spectral-decimation map of the Sierpinski gasket under x=−z (Fukushima–Shima 1992; Teplyaev 1998), so the backward orbit of −3 is the classical 6-series shifted; see DISC-0182. A published count of this exact form for this corner vector was not found; the search was not exhaustive.

## Novelty Analysis
The technique is KNOWN. The specific sequence 1,0,1,3,5·2^(k−4) depends on the particular period endpoint ψ(−1) and is plausibly unpublished, but that is UNRESOLVED.

## Falsification Attempts
1. Repository witness run at 09936074caa8: all checks pass, exit 0 (3.1 s), including an arb recount of all 2^k points for k≤18.
2. Independent archive script discoveries/mathematics/scripts/indep_theorem_CD.py (mpmath, 60 digits, no repository code): rebuilds O_k from −3 by the two inverse branches and counts points in (p(a),a] for k≤20. Result: [1,0,1,3,5,10,…,327680], matches the formula through k=20; endpoint orbit −3.85006191253, −4.42733283233, −2.53538815341, −6.2487476786 matches CD.2. PASS (22 s).
3. Proof read line by line: each image interval in CD.3 checked against monotonicity of p on its side of −5/2 and the ordering in CD.2. No gap found. One point worth noting: CD.1's induction needs every point of O_k in (−25/4,0) for real preimages, which holds because they lie in (−5,0).

## Experimental Validation
Pure mathematics; numerical recount to k=20 independently.

## Mathematical Status
Theorem (elementary proof; four certified inequalities).

## Patent Relevance
None. Pure mathematics about a graph Laplacian's spectral measure. The repository itself states it is not a flux or thrust claim.

## Related Discoveries
- DISC-0186 (Theorem CC): counts observed there, now proved.
- DISC-0182 (Theorem CA): defines O and Λ_O.
- DISC-0184 (Conjecture CA.6, now THEOREM): atom set exactly Λ_O.

## Open Questions
- The level-sum ratio 0.42373129… of the masses (not touched by CD).
- Closed form of ψ, exact liminf ρ_k, θ̂_k≠0 for k≥22 (repository list).

## Next Experiments
- Whether the level-sum ratio equals a closed expression in the transfer weights (2−t)/(6−t) of DISC-0186 averaged over the 5/16 fraction of O_k.

## Reproduction Instructions
Clone beyond-repair/informational-flux-identity at 09936074caa80ac880fdd1cd28b5730b9b1b6bee; pip install python-flint mpmath sympy; run `python3 scripts/gasket_fractional_profile_level_counts.py` (about 3 s). Then run `python3 discoveries/mathematics/scripts/indep_theorem_CD.py` from this archive (about 22 s).

## Evidence Log
- 2026-10-29 ~12:56pm EDT. Indexed from commit 09936074caa80ac880fdd1cd28b5730b9b1b6bee. Repo witness EXIT 0 (3.1 s); independent check PASS to k=20.

## Change History
- 2026-10-29. Initial archive entry.
- 2026-10-29 ~2:58pm EDT. Note: the level-sum ratio listed under Open Questions is proved by Theorem CE at a056d01a82828425e6ddb624b13c31cbb737156a (DISC-0188): r = spectral radius of a twisted transfer operator, 0.42373128696260793985…, closed form open. Earlier text above is kept unchanged. Status of this entry unchanged.
