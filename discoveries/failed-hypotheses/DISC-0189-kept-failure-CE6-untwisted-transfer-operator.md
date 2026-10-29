# Discovery: Kept Failure CE.6, the untwisted transfer operator is not a strictly positive Ruelle operator

## Discovery ID
DISC-0189

## Status
REJECTED (the repository's own Kept Failure; the naive Perron–Frobenius route to the level-sum ratio fails as stated).

## Date Discovered
2026-10-29 (indexed ~2:58pm EDT)

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit a056d01a82828425e6ddb624b13c31cbb737156a.

## Original Evidence
GASKET.md, Kept Failure CE.6 (line 3463); checks in scripts/gasket_fractional_profile_level_ratio.py.

## Discovery
The untwisted operator (Lh)(t)=Σ_{p(y)=t} w(y)h(y) has p^(−1)(0)={0,−5}, w(0)=1/3, w(−5)=0, so (Lh)(0)=h(0)/3 for every h: 1/3 is an eigenvalue with left eigenvector δ_0, every r-eigenfunction vanishes at 0, and Birkhoff cones do not apply directly. The untwisted Herglotz masses σ(O_k) have ratio 0.42614585… at k=14, still 2.4·10^(−3) from r.

## Why It Matters
Records exactly where the obvious approach breaks and why the twist q=−t (DISC-0188) is needed. The level sums s_k avoid the parasitic mode because I stays away from 0 and −5.

## Derivation
w(0)=(2·5)/(6·5)=1/3, w(−5)=0 directly from w(y)=(y+2)(y+5)/((y+6)(2y+5)).

## Assumptions
Same as DISC-0188.

## Prior Art
Vanishing weights and parasitic point-mass modes in transfer operators are a known obstruction; ground-state conjugation is the standard fix.

## Falsification Attempts
w(0)=1/3 and w(−5)=0 confirmed exactly in indep_theorem_CE.py; (Lh)(0)=h(0)/3 follows. Repository witness checks L^k1(0)=3^(−k) for k≤10, EXIT 0.

## Mathematical Status
Counterexample to the naive route (exact).

## Patent Relevance
None.

## Related Discoveries
DISC-0188 (fix), DISC-0186, DISC-0187.

## Open Questions
None for the rejection itself.

## Next Experiments
None.

## Reproduction Instructions
As DISC-0188.

## Evidence Log
- 2026-10-29 ~2:58pm EDT. Indexed from a056d01a82828425e6ddb624b13c31cbb737156a.

## Change History
- 2026-10-29. Initial archive entry.
