# Discovery: Theorem ER, the signs of H_n's residues at every level n (exactly 2^(n-2) negative for n >= 2)

## Discovery ID
DISC-0257

## Status
THEOREM (mathematical sense only). ER.1 is a pen-and-paper proof for every n >= 1, stated in GASKET.md §Theorem ER and in the script docstring. It uses only EQ.1 and EQ.2 (DISC-0256) and, through them, AQ (1) as stated in the repository. ER.2 contains certified arb checks for n <= 8 and float/rational checks for n <= 4. The method is KNOWN: interlacing of the zeros and poles of a Stieltjes function with positive residues, plus real preimages of the quadratic map p(s) = s(s+5). Whether the explicit count 2^(n-2) is new is UNRESOLVED; no external literature search was done. This closes DISC-0256's kept limit "residues of mixed sign, no sign claimed". It is a counting result only. It gives no magnitude, no sum, and no new sign of Y_n - Y_oo. No other status change.

## Date Discovered
2026-11-22. The commit is from 12:24 PM EST; it was indexed about 1:30 PM EST.

## Source Repositories
beyond-repair/informational-flux-identity, branch main, commit c02dafc238e53e96bc167d2cb0e6679fd979c797 (2026-11-22 12:24:29 PM EST; 17:24:29Z). Parent: 8966f3127ec0 (Theorem EQ, DISC-0256).

## Original Evidence
- GASKET.md §Theorem ER (+22/-2), with in-place marks on EQ.2 and EQ's kept limit. Also README.md (+1/-1) and CLAIM_STATUS.md (+3/-1).
- scripts/gasket_fractional_corner_h_residue_signs.py (new, 121 lines; imports EQ's gasket_fractional_corner_pole_structure.py unchanged), registered in scripts/cli.py (+1). Also tests/test_cli.py (+13) and tests/test_flux_identity.py (+24).

## Discovery
- Setting (from EQ). p(s) = s(s+5), q_k = p^k + 5, r_n = B_n/A_n with B_n = prod_(k<n) q_k. A_n has 2^n simple real negative roots z_j with residues c_j > 0. H_n's reduced integrand is Q_n/(2 A_n) with Q_n = B_n/q_(n-1), so Res_(z_j) H_n = h_j = c_j/(2 q_(n-1)(z_j)) and sign h_j = sign q_(n-1)(z_j).
- ER.1 (THEOREM, every n >= 1). The number of negative residues of H_n is N_1 = 1, and N_n = 2^(n-2) for n >= 2. The other 2^n - N_n residues are positive. There is exactly one negative-residue pole in each bounded open interval of {p^(n-1) < -5}. For n = 1 it is the pole left of -5.
- ER.2 (checks). (a) arb at 1024 bits, n = 1..8: every sign is decided and the negative counts are 1, 1, 2, 4, 8, 16, 32, 64. q_(n-1) has 2^(n-1) real roots, the zeros of B_n alternate with the poles, and each interval holds exactly one pole. (b) Float gasket-Laplacian eigenvalues with exact rational evaluation of q_(n-1), n <= 4, give the same counts. (c) p^m(-5) = 0 for m >= 1.

## Why It Matters
EQ (DISC-0256) put H_n on the same every-level residue footing as J_n, but it left the signs of H_n's residues open. ER fixes that sign pattern exactly. That is a precondition for any monotonicity or sign argument on om_n = H_n/J_n built from residue sums. On its own it does not decide any thin level (0.88, n = 9 is unchanged).

## Derivation
This slice re-checked the proof step by step (reviewer check, not new mathematics):
1. Interlacing. r_n = sum c_j/(s - z_j) with c_j > 0, so r_n' < 0 off the poles. On each of the 2^n - 1 gaps, r_n runs from +inf to -inf. Left of the first pole r_n < 0, and right of the last pole r_n > 0. So B_n (degree 2^n - 1) has exactly one simple real zero per gap, and zeros and poles strictly alternate.
2. Real roots of q_(n-1). For t > -25/4, p(y) = t has the roots y = (-5 +- sqrt(25+4t))/2. For t in [-5, 0) we have 25 + 4t in [5, 25), so both roots lie in (-5, 0). By induction from -5, all iterated preimages lie in (-5, 0), and distinct targets have disjoint preimages. So p^(n-1)(y) = -5 has 2^(n-1) distinct real roots. q_(n-1) is monic of even degree for n >= 2, so it is negative on exactly 2^(n-2) open intervals (a_i, b_i) between adjacent roots.
3. No other zero of B_n lies inside {q_(n-1) < 0}. If q_k(w) = 0 with k < n-1, then p^(k+1)(w) = p(-5) = 0, and 0 is fixed by p, so p^(n-1)(w) = 0 and q_(n-1)(w) = 5 > 0. Hence a_i and b_i are adjacent zeros of B_n, and step 1 puts exactly one pole between them. Every other pole has q_(n-1) > 0 (nonzero by gcd(A_n, B_n) = 1).
4. n = 1. The poles (-7 -+ sqrt13)/2 are about -5.303 and -1.697, and q_0 = s + 5. Exactly one is negative, matching EO.1 and EQ.2's example.
No gap was found. The only external inputs are EQ.1 (B_n's product form, coprimality) and EQ.2 (simple real negative poles, c_j > 0).

## Assumptions
- EQ.1 and EQ.2 as proved in the repository (DISC-0256). Through them, AQ (1) and AQ's setting r_n = 1/2 v^T (L_n + s)^-1 v with v = e_a - e_b.
- H_n's reduced integrand is Q_n/(2 A_n) as stated in EQ.2 (this slice did not re-derive H_n's definition from earlier theorems).
- ER.2 (a) only: arb root isolation in python-flint 0.9.0 is correct.

## New Results
For every n >= 2: exactly 2^(n-2) negative and 3·2^(n-2) positive residues of H_n, one negative residue in each component of {p^(n-1) < -5}. For n = 1: one negative and one positive.

## Prior Art
Interlacing of zeros and poles for Stieltjes / Herglotz-type rational functions with positive residues is textbook (Cauchy interlacing, Pick/Nevanlinna functions). Real preimage trees of p(s) = s(s+5) under iteration are standard in gasket spectral decimation (Rammal-Toulouse, Fukushima-Shima, Teplyaev). No external search was done for this specific count.

## Novelty Analysis
The method is KNOWN. The explicit sign count for this H_n (a corner-flux numerator specific to the repository's construction) may not appear in the literature in this form. Its novelty is UNRESOLVED.

## Falsification Attempts
- Repository witness rerun from a fresh clone at c02dafc238e5 (niced, shared box): EXIT 0 in 843.3 s wall, all ER checks passed; arb counts 1, 1, 2, 4, 8, 16, 32, 64 reproduced (n = 8 alone 775 s), Laplacian checks n = 1..4 passed.
- Independent mpmath check (400 digits, n = 1..6). It takes A_n, B_n from EQ's eq1_pair. It does not use the formula h_j = c_j/(2 q_(n-1)): residues were computed directly as Q_n(z_j)/(2 A_n'(z_j)), with Q_n = prod_(k<=n-2) q_k built independently. Results: all roots real, all c_j = B_n/A_n' > 0, negative counts 1, 1, 2, 4, 8, 16 = ER.1. The smallest |h_j| was 2.96e-9 at n = 6, so no sign sits near zero at working precision. n = 7 did not finish in this check's 800 s budget; the repository arb run covers n = 7 and 8.
- Proof attack: the n = 1 boundary case, the even-degree sign of q_(n-1), the possibility of a zero of q_k (k < n-1) inside a negative interval (excluded by p^m(-5) = 0), and a possible multiple root of q_(n-1) (excluded by disjoint preimages). All held.

## Experimental Validation
None applicable (pure mathematics on a finite graph). Computer checks as above.

## Mathematical Status
Theorem (proof every n >= 1, conditional on EQ and therefore on AQ (1) as stated). ER.2: certified checks for n <= 8.

## Patent Relevance
None. A counting statement about a rational function on the combinatorial gasket. Not a flux, not thrust.

## Related Discoveries
- DISC-0256 (Theorem EQ): the source of the pole structure and of H_n's reduced form. Its kept limit on H_n residue signs is closed here.
- DISC-0255 (Theorem EP), DISC-0254 (Theorem EO): the residue route for om_n and the n = 1 closed form.

## Open Questions
- Magnitudes and sums of the negative residues. Whether the sign pattern yields monotonicity of om_n or decides thin levels (0.88, n = 9).
- N = 2, 3 and alpha-cells. The poles of r_n versus r_(n+1). Stage 2 is still BLOCKED (no Psi_info).
- A prior-art search for the explicit count.

## Next Experiments
- Use the sign pattern to bound H_n by its positive part, and test whether that tightens EP's residue route at (0.88, n = 9).

## Reproduction Instructions
1. Clone informational-flux-identity and check out c02dafc238e5.
2. Run pip install python-flint (0.9.0 was used here).
3. Run python3 scripts/gasket_fractional_corner_h_residue_signs.py. Exit 0 means every check passed. n = 8 dominates the run time.

## Evidence Log
- 2026-11-22: commit c02dafc238e5 read (GASKET.md §Theorem ER, new script, CLAIM_STATUS row). Witness rerun and independent mpmath residue check done here.

## Change History
- 2026-11-22: created.


- 2026-11-22 ~5:50 PM EST note (appended; the history above is unchanged): DISC-0258 (Theorem ES, informational-flux-identity 361b25c217af) closes the kept limit "counting only, no magnitude or sum": sum_j h_j = 0 (so S_n^- = S_n^+), the first 2^(n-1) residue moments are fixed, and S_n^- >= (2/5) C_n^- for n >= 2 (S_1^- = 1/(2 sqrt13)). ER's statements are unchanged.
