# Discovery: Free decimation hit mass h_n → 4/9 on build_gasket(n)

## Discovery ID

DISC-0025

## Status

DERIVATIVE

## Date Discovered

2026-10-08. Archive pass for beyond-repair/finite-gasket-spectral-derivatives hit-predicate commit.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, evidence commit e1b8f2737ecf1aa8fc21b999560b648dff087b57 (indexed under HEAD a0439980b5, the merge of PR #1 that adds the CLI at 5d273d7af4 and does not change the claim cap). Paths: README.md section "Free decimation hit predicate on build_gasket(n)"; COMPLETION_LOG.md "Proved this run (2026-10-08, free decimation hit predicate)"; CLAIM_STATUS.md; scripts/check_decimation_hits.py.

Depends on DISC-0020 (free mult(5), mult(6)) and DISC-0021 (μ_exc). The exact c_n = 5·2^{n−1}+1 corollary additionally rests on classical Qiu §2 Dirichlet structure (arXiv:1206.1381), the same input used by DISC-0022.

## Original Evidence

CLAIM_STATUS.md at e1b8f27 replaces the row "Decimation hit rate equals 1 − μ_exc — NOT CLAIMED" with:

- Hit mass h_n → 4/9, bound 1 − μ_exc − 5·2^n/(3^{n+1}+3) ≤ h_n ≤ 1 − μ_exc (n ≥ 3), for the README-defined hit predicate: **CLAIMED**, prose argument; supporting numerics in scripts/check_decimation_hits.py (not a test).
- Exact h_n = 1 − μ_exc − 5·2^n/(3^{n+1}+3) (no coincidental hits): **NOT CLAIMED**, numerical n = 3..6 only.
- SPECTRUM.md informal "0.4–0.7" string: **NOT CLAIMED** as identified with h_n.

Definition (README): for λ ∈ Spec(L_n) \ {3,5,6}, λ is a hit iff R(λ) = λ(5−λ) ∈ Spec(L_{n−1}); h_n is hit multiplicity over N(n) = (3^{n+1}+3)/2.

Proof skeleton (README Steps 1–6): midpoint extension for λ ∉ {2,5}; decimation identity with a free-corner defect term (2λ/(2−λ))·v(c); DN_n(λ) ≅ DN_{n−1}(R(λ)) for λ ∉ {2,5,6}; recursion c_n = 2c_{n−1} − 1 − dim DN_n(2) for the corner-visible dimension c_n; exact base c_2 = 11 (rational Krylov rank); every DN mode off {3,5,6} is a hit, so non-hit mass ≤ (c_n − 1)/N(n) ≤ 5·2^{n−1}/N(n) = O((2/3)^n).

## Discovery

For the unnormalized free Laplacian D − A on the finite gasket graph (corners of degree 2), the eigenvalues that fail to decimate, outside the exceptional set {3,5,6}, carry vanishing spectral mass, bounded by the corner-visible dimension. The hit mass therefore tends to 1 − lim μ_exc = 4/9. The repository refusal recorded on DISC-0021 ("does not prove any hit-rate equals 1 − μ_exc") is superseded for this specific predicate: the limit is now claimed, while exact equality at finite n is still not claimed.

## Why It Matters

It closes the open hit-rate note on DISC-0021 with a defined predicate and an explicit error bound, and it explains why free D − A does not decimate on corner-visible modes (the corner defect). It also separates h_n (→ 4/9) from the old SPECTRUM.md "0.4–0.7" string, which the repository explicitly declines to identify with h_n.

## Derivation

Not repeated here; see README Steps 1–6 at e1b8f27. Archive checks below.

## Assumptions

Free L_n = D − A on build_gasket(n); DISC-0020 free mult(5) and mult(6) formulas and the fact that free 5- and 6-eigenfunctions vanish on V_0 (n ≥ 3); N(n) from the constructor. No W, force, stress, momentum, or continuum input.

## New Results

None beyond the repository's statement. Archive-side checks extend the numerical support from n ≤ 6 to n = 7 (below).

## Prior Art

Spectral decimation with R(z) = z(5 − z) and exceptional set {3,5,6} is classical (Rammal–Toulouse; Fukushima–Shima; Qiu arXiv:1206.1381; Malozemoff–Teplyaev; survey arXiv:1302.4007). Domination of the spectrum by Dirichlet–Neumann eigenfunctions on nested-fractal graphs is classical context (cited e.g. in "Spectrum of the Laplacian of an asymmetric fractal graph", Proc. Edinburgh Math. Soc.). The repository itself says it does not claim the hit predicate or the corner-defect formula is new. The specific count c_n = 5·2^{n−1}+1 and the bound for unnormalized free D − A are elementary consequences of DISC-0020 plus classical decimation; a 2026-10-08 web search found no statement of this exact bound, which is not evidence of novelty.

## Novelty Analysis

DERIVATIVE. Granted DISC-0020, the argument is classical decimation and DN-mode counting applied to the free D − A graph. If DISC-0020's free mult(5)/mult(6) prose proofs fail, this row fails with them. Not a THEOREM in the archive: the proof is prose in README, the c_2 base is a scripted exact computation, and there is no in-repo test of the bound.

## Falsification Attempts

- Symbolic (sympy, archive-side): interior coefficient (4−λ)Δ − 4(4−λ) = (6−λ)(4−R(λ)) holds identically; κ = 2λ(5−λ); κ/Δ − (6−λ)(2−R)/Δ reduces to the stated defect 2λ/(2−λ); the corner row of (L_n − λ)u, with midpoints from the extension formula, equals ((6−λ)/Δ)((L_{n−1} − R)v)(c) + (2λ/(2−λ))v(c) identically. All residuals 0.
- Recursion bookkeeping re-derived by hand: N(n) − 2N(n−1) − 3^{n−1} − m5_n = −1, so c_n = 2c_{n−1} − 1 − dim DN_n(2) for n ≥ 3 as stated. Roots of R(λ) = μ in {2,5,6} occur only for μ ∈ {0, 6}, and DN_{n−1}(0) = 0, as stated.
- Repository script re-run at e1b8f27: c_n = 6, 11, 21, 41, 81, 161; dim DN_n(2) = 0; non-hits 5, 9, 20, 40, 80, 160; identity residual ≤ 2.2e−15; exact rational Krylov ranks c_2 = 11, c_3 = 21.
- Extension to n = 7 (N = 3282, eigh on the same constructor): exceptional mass 1819 = (5·3^6 − 7)/2 (also extends DISC-0020/0021 numerics to n = 7); hits 1143; non-hits 320; c_7 = 321 = 5·2^6 + 1; h_7 = 0.348263, equal to the lower bound 1 − μ_exc − 5·2^7/(3^8+3) = 0.348263 and below the upper bound 0.445765; zero corner-visible coincidental hits.
- Not broken. The attack did not find a counterexample to the bound, the recursion, or the identity.

## Experimental Validation

None. Pure graph spectral statement.

## Mathematical Status

Derivative corollary of DISC-0020 plus classical decimation; prose proof in-repo; numerics n = 1..7. Exact finite-n equality (no coincidental hits) remains open in-repo and is observed for n = 3..7.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0020. Mathematical. Supplies free mult(5), mult(6) and their vanishing on V_0.
- DISC-0021. Mathematical. Its hit-rate refusal is superseded for this predicate; μ_exc is the upper bound.
- DISC-0022. Mathematical. Same classical Qiu §2 input for the exact c_n corollary.
- DISC-0005. Computational. SPECTRUM.md "0.4–0.7" string is not identified with h_n.
- DISC-0002. Mathematical. A spectral mass fraction is not thrust and does not select W.

## Open Questions

Whether a corner-visible eigenvalue can ever be a coincidental hit (exact h_n). An elementary proof of DN_n(2) = 0 without Qiu §2.

## Next Experiments

Cite h_n → 4/9 only with the README-defined predicate and as a CLAIMED prose result. Do not cite exact finite-n h_n, do not identify h_n with the SPECTRUM.md string, and do not read 4/9 as a physical rate.

## Reproduction Instructions

Clone beyond-repair/finite-gasket-spectral-derivatives at e1b8f2737ecf1aa8fc21b999560b648dff087b57 and run `python3 scripts/check_decimation_hits.py`. For n = 7, call the script's build_gasket/laplacian/eigenspaces with nmax 7 (about one minute on CPU).

## Evidence Log

- 2026-10-08. Read README, COMPLETION_LOG, CLAIM_STATUS diff at e1b8f27; re-ran repository script; sympy identity checks; n = 7 extension. GitHub description still matches the claim fence ("W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum, no selected W, no thrust.").
- 2026-10-08 (later). finite-gasket-spectral-derivatives at 7b1495fe1dd322d17f7b7d840b22c7d9f29faf10 proves c_n = 5·2^{n−1}+1 and dim DN_n(2) = 0 by corner channels without Qiu §2, and certifies exactly that the lower bound above is an equality for 3 ≤ n ≤ 11 (archive: 3 ≤ n ≤ 14 over Z). The Open Questions above are partly superseded; indexed as DISC-0026 and DISC-0027. Status of this row unchanged (DERIVATIVE).

## Change History

- 2026-10-08. Initial archive entry.
- 2026-10-08. Evidence-log append pointing to DISC-0026/0027. Earlier text left as recorded.
