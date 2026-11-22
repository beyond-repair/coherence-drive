# Discovery: Theorem EQ, EP.1's pole structure (degrees 2^n, simple real negative poles, positive residues) at every level n

## Discovery ID
DISC-0256

## Status
THEOREM (mathematical sense only). EQ.1 and EQ.2 are pen-and-paper proofs by induction for every n >= 0, stated in the script docstring and GASKET.md §Theorem EQ. They take AQ (1) (the level recursion for r_n) and AQ's setting r_n = 1/2 v^T (L_n + s)^-1 v as given. EQ.3 is exact and certified checks. Method KNOWN: an induction on a polynomial recursion, the spectral (Stieltjes) form of a graph resolvent, uniqueness of reduced rational forms, and gasket spectral decimation with p(s) = s(s+5). Novelty of the explicit form (B_n = prod_(k<n) (p^k + 5), exact division by s + 2, exactly 2^n v-weighted eigenvalues) is UNRESOLVED; no external literature search was done. This closes DISC-0255's kept limit "pole structure n <= 6 only" and its open item "pole structure for all n". Structural only: it gives no new om_n, D'_n or sign. No other status change.

## Date Discovered
2026-11-22 (indexed ~10:15 AM EST; the commit is 2026-11-22 9:07 AM EST).

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit 8966f3127ec07affdde4fe0cc4137b4cbf9d17dc (2026-11-22 9:07:06 AM EST; 14:07:06Z). Parent: 1a5d6a76e74d (Theorem EP, DISC-0255).

## Original Evidence
- GASKET.md §Theorem EQ (+41/-2), with in-place marks on EP's kept limit and open item. Also README.md EP paragraph (+1/-1) and CLAIM_STATUS.md EP kept limit (+1/-1).
- scripts/gasket_fractional_corner_pole_structure.py (new, 234 lines), registered in scripts/cli.py (+1). Also tests/test_cli.py (+15) and tests/test_flux_identity.py (+30; pure-Python/numpy test).

## Discovery
- EQ.1 (THEOREM, every n >= 0). Put p(s) = s(s+5), A_0 = s + 3, B_0 = 1, A_(n+1)(s) = [(s+6) A_n(p(s)) - 2s(s+5) B_n(p(s))]/(s+2) and B_(n+1)(s) = (s+5) B_n(p(s)). Then the division is exact in Z[s], A_n and B_n are monic and coprime, and r_n = B_n/A_n is EP's gcd-reduced pair. Also deg A_n = 2^n, deg B_n = 2^n - 1, B_n = prod_(k=0)^(n-1) (p^k(s) + 5), A_n(0) = 3^(n+1), B_n(0) = 5^n, and A_n(-6) = -3 B_n(-6) != 0.
- EQ.2 (THEOREM, every n >= 0). Write r_n = sum over distinct mu of m_mu/(s+mu), with m_mu = |P_mu v|^2/2 and v = e_a - e_b orthogonal to the constants. This sum is already reduced. So A_n = prod (s + mu) over exactly 2^n distinct eigenvalues mu > 0 of L_n with P_mu v != 0. That gives 2^n simple real negative poles, residues m_mu > 0, sum of residues 1, and sum c_j/w_j = r_n(0) = (5/3)^n/3. The reduced form of H_n's integrand is prod_(k<=n-2)(p^k + 5)/(2 A_n). It has the same poles; its residues have mixed sign, and no sign is claimed. EP.1's residue formulas for J_n, H_n, om_n and D'_n therefore hold at every level n >= 1.
- EQ.3 (checks). Exact identities for n = 0..10 (deg A_10 = 1024), coprime and squarefree. Agreement with EP's rn_exact/h_exact for n = 1..7. Certified arb isolation (1024 bits) at n = 7 and 8: 128 and 256 simple real roots in [-5.17927, -4.6e-5], minimum residues 6.5e-7 and 4.4e-8. Gasket Laplacian floats for n = 1..5 (6..366 vertices): 4, 8, 18, 36 and 70 distinct eigenvalues, of which exactly 2^n carry v-weight.

## Why It Matters
EP's exact-residue route for Y_n - Y_oo (DISC-0255) needed the pole structure of r_n, which had been certified only for n <= 6. EQ removes that limit, so the residue formulas are valid at every level. It does not by itself decide any new sign: thin cases such as (0.88, n = 9) still need certified evaluation at degree 2^9.

## Derivation
This slice re-checked the induction step by hand (reviewer check, not new mathematics):
- Invariant A_n(-6) = -3 B_n(-6). p(-6) = 6, so A_(n+1)(-6) = [0 - 2(-6)(-1) B_n(6)]/(-4) = 3 B_n(6), and B_(n+1)(-6) = -B_n(6). Base: A_0(-6) = -3, B_0 = 1. The invariant holds, and B_n(6) = prod (p^k(6) + 5) > 0, so it is nonzero.
- Exact division. p(-2) = -6, so D(-2) = 4 A_n(-6) - 2(-2)(3) B_n(-6) = 4(A_n(-6) + 3 B_n(-6)) = 0.
- Coprimality. A common root z = -5 is impossible because A_(n+1)(-5) = A_n(0)/(-3) = -3^n != 0. A common root z = -2 is impossible because B_(n+1)(-2) = 3 B_n(-6) != 0 (B_n(-6) = 0 would force A_n(-6) = 0, contradicting coprimality at level n). Otherwise B_n(p(z)) = 0, so A_n(p(z)) != 0. Then D(z) = 0 forces z = -6, which needs B_n(6) = 0, which is impossible.
- Monic and degree. The leading term of (s+6) A_n(p) has degree 2^(n+1) + 1 and exceeds that of 2s(s+5) B_n(p), which has degree 2^(n+1).
- EQ.2 uses only that a sum of m/(s+mu) with distinct mu and m > 0 is reduced, together with uniqueness of the reduced form.

## Assumptions
- AQ (1) as stated in the repository: r_n satisfies the recursion that produces the numerator/denominator recursion above. Not re-derived here.
- AQ's graph setting: G_n is connected, L_n is its graph Laplacian, and v = e_a - e_b.
- arb root isolation and python-flint are correct (EQ.3 only).

## New Results
Every-level pole structure for r_n and for H_n's integrand. Explicit B_n, A_n(0), B_n(0), and the invariant r_n(-6) = -1/3. The number of v-weighted distinct eigenvalues of the level-n gasket Laplacian is exactly 2^n.

## Prior Art
Spectral decimation on the Sierpinski gasket (Rammal-Toulouse; Fukushima-Shima; Shima; Teplyaev; Malozemov-Teplyaev) uses the same quadratic map up to sign and normalization. The Stieltjes/resolvent form of graph Green's functions is textbook. Counting the eigenvalues that carry weight on a given vector is standard in spectral decimation. No external search was done.

## Novelty Analysis
The method is KNOWN. The specific identities (exact s + 2 division, the product B_n, r_n(-6) = -1/3, the 2^n count for v = e_a - e_b) may already appear in spectral decimation literature. Their novelty is UNRESOLVED.

## Falsification Attempts
- The repository witness was rerun from a fresh clone at 8966f3127ec0: EXIT 0 in 25.6 s wall, all EQ checks passed.
- pytest -k 'pole_structure or EQ or eq_': 2 passed, 125 deselected (54.7 s). The full tests/ suite did not finish within 280 s here because of other heavy tests. That is a timeout, not a failure.
- Independent sympy re-implementation (/workspace/eq_indep.py on the box; not the repo code) for n = 0..6: exact division by s + 2, monic, degrees 2^n and 2^n - 1, coprime, squarefree, A_n(0) = 3^(n+1), B_n(0) = 5^n, and A_n(-6) = -3 B_n(-6) != 0. nroots for n <= 5 gave all roots real and negative.
- The hand check of the induction above found no gap.
- Result: survived. KEPT FAILURE in the repository: none.

## Experimental Validation
Not applicable (pure mathematics). Computational validation as above.

## Mathematical Status
Theorem (proof by induction for every n, conditional on AQ (1) and AQ's setting as stated in the repository). EQ.3 is a computer check.

## Patent Relevance
None. These are functions on a graph, not a flux and not thrust.

## Related Discoveries
- DISC-0255 → DISC-0256 (mathematical): EP.1's structure, certified for n <= 6, is proved for every n.
- DISC-0254 → DISC-0256 (mathematical): EO.1's level-1 r_1 = (s+5)/(s^2+7s+9) and eta_1 = 1/(2(z+5)) are the n = 1 case of EQ.1 and of H_n's integrand.

## Open Questions
- Sign of H_n's residues (mixed at n = 1). Is there a structural pattern?
- Certified evaluation at thin levels (0.88, n = 9; degree 512) via the residue route.
- Is the explicit form already in the spectral decimation literature? A prior-art search is needed.

## Next Experiments
Run the residue route at (0.88, n = 9) with arb at higher precision now that the pole structure is proved. Search the literature for B_n = prod (p^k + 5) and the s + 2 cancellation.

## Reproduction Instructions
Clone informational-flux-identity at 8966f3127ec0. Run pip install python-flint numpy, then python3 scripts/gasket_fractional_corner_pole_structure.py (about 25-32 s; expect "all EQ checks passed"). Then run python3 -m pytest -q tests -k 'pole_structure or EQ or eq_'.

## Evidence Log
- 2026-11-22 ~10:05 AM EST: fresh clone at 8966f3127ec0. Witness EXIT 0 (25.6 s). Targeted pytest 2 passed. Independent sympy check n = 0..6 ok.

## Change History
- 2026-11-22: created.
