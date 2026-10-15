# Discovery: Corner-channel closed forms, c_n = 5·2^{n−1}+1, and exact h_n for small n on build_gasket(n)

## Discovery ID

DISC-0026

## Status

DERIVATIVE

## Date Discovered

2026-10-08. Archive pass for beyond-repair/finite-gasket-spectral-derivatives corner-channel commit (second repository run of the day).

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives, branch main, evidence commit 7b1495fe1dd322d17f7b7d840b22c7d9f29faf10 (HEAD at indexing). Paths: README.md section "Corner channels and coincidental hits on build_gasket(n)"; COMPLETION_LOG.md "Proved this run (2026-10-08, second run: corner channels and coincidental hits)"; CLAIM_STATUS.md; scripts/check_corner_channels.py.

Depends on DISC-0025 (decimation identity with corner defect, DN isomorphism, recursion c_n = 2c_{n−1} − 1 − dim DN_n(2)) and, through it, on DISC-0020.

## Original Evidence

CLAIM_STATUS.md at 7b1495f replaces the row "Exact h_n = 1 − μ_exc − 5·2^n/(3^{n+1}+3) (no coincidental hits): NOT CLAIMED, numerical n = 3..6 only" with:

- Corner channels: s_n = Q_n/(2 − R^{n−1}), t_n = Qt_n/Π_{k<n}(5 − R^k), c_n = 5·2^{n−1}+1 (n ≥ 1), dim DN_n(2) = 0 (n ≥ 3): **CLAIMED**, prose argument in README; exact checks in scripts/check_corner_channels.py (not a test).
- Exact h_n = 1 − μ_exc − 5·2^n/(3^{n+1}+3) for 3 ≤ n ≤ 11: **CLAIMED (finite exact computation)**, F_p gcd certificate with p = 2^61 − 1.
- Exact h_n for all n: **NOT CLAIMED**, open.

Proof skeleton (README Steps 1–4): the S_3 symmetry of the triangle forces the corner Schur complement S_n(λ) = t_n I + ((s_n − t_n)/3) J; composing Schur complements through the DISC-0025 corner-defect identity gives the affine recursion s_n = [(6 − λ)s_{n−1}(R) + 2R]/Δ (same for t_n), R(z) = z(5 − z), Δ = (2 − λ)(5 − λ); 1/s_n and 1/t_n are Herglotz-type, so reduced numerator degree counts distinct channel-visible eigenvalues; exact cancellations happen only at λ = 5 (symmetric channel, since s(0) = 0) and λ = 2 (since s_m(6) = t_m(6) = −3). Hence σ_n = 2^{n−1}+1, τ_n = 2^n, c_n = σ_n + 2τ_n. Coincidental hits reduce to nonzero roots of gcd(Q_n Qt_n, H_{n−1}∘R), with H_{n−1} = Q_{n−1}Qt_{n−1}Π_{j≤n−3}Π_{a∈{2,5,6}}(R^j − a).

## Discovery

On the free D − A gasket graph, the corner Green function splits into a symmetric and a two-dimensional standard channel, each with an explicit rational closed form whose reduced numerator degrees are 2^{n−1}+1 and 2^n. That gives the corner-visible dimension c_n = 5·2^{n−1}+1 for every n ≥ 1 and dim DN_n(2) = 0 for n ≥ 3 by an elementary argument. DISC-0025's c_n corollary no longer rests on Qiu §2, and its c_2 = 11 base is no longer a scripted Krylov rank. With an exact gcd certificate, the DISC-0025 lower bound on h_n is an equality for 3 ≤ n ≤ 11.

## Why It Matters

It turns DISC-0025's floating-point "no coincidental hits, n = 3..6" observation into a finite exact statement, and it isolates the remaining all-n question as a single polynomial gcd identity (recorded separately as DISC-0027).

## Derivation

Not repeated here; see README "Corner channels and coincidental hits" at 7b1495f. Archive checks below.

## Assumptions

Free L_n = D − A on build_gasket(n); the S_3 action on the constructor; DISC-0025 Steps 1–4; DISC-0020 vanishing of free 3-, 5-, 6-eigenfunctions on V_0 (n ≥ 2 or 3 as stated). No W, force, stress, momentum, or continuum input.

## New Results

None in the repository's statement beyond what it claims. Archive-side, the exact certificate is extended from n ≤ 11 to n ≤ 14 over Z (below). That extension is evidence for DISC-0027, not a proof.

## Prior Art

Writing spectral decimation through a Schur complement onto the boundary is standard (Fukushima–Shima; Shima; Malozemoff–Teplyaev; Strichartz's book; Qiu arXiv:1206.1381). Corner-visible (non-Dirichlet–Neumann) eigenvalue counts follow from that classical picture. The repository says no literature was opened for this subsection and that it does not claim the closed forms are new. The specific unnormalized-free-D − A constants (c_n = 5·2^{n−1}+1, the P_n and Pt_n pole forms) were not found stated in a short search; that is not evidence of novelty.

## Novelty Analysis

DERIVATIVE. Classical Schur-complement decimation plus elementary degree and cancellation bookkeeping, applied to the free D − A graph. Not a THEOREM in the archive: the general-n proof is prose in README, and the exact computations are a script, not a test. If DISC-0025 Steps 1–4 fail, this row fails with them.

## Falsification Attempts

All archive-side, independent of the repository constructor and of its polynomial code.

- Own gasket constructor (integer lattice recursion, not build_gasket) and exact sympy Schur complements onto the three corners at λ = 37/100 and λ = −7/3 for n = 1, 2, 3: symmetric and standard channels equal s_n, t_n from the recursion exactly (difference 0).
- Recursion re-implemented two ways (sympy cancel to n = 6; python-flint fmpz_poly with gcd-based reduction to n = 11, not assuming which factors cancel): deg Q_n = 2^{n−1}+1, deg Qt_n = 2^n, leading coefficients −1, reduced denominators proportional to 2 − R^{n−1} and Π_{k<n}(5 − R^k) for every n = 1..11. c_n = 6, 11, 21, 41, 81, 161, … = 5·2^{n−1}+1.
- Direct coincidental-hit check bypassing H: exact characteristic polynomial χ_{n−1} of own-constructor L_{n−1} (flint), gcd(Q_n, χ_{n−1}∘R) = λ and gcd(Qt_n, χ_{n−1}∘R) = 1 for n = 3, 4, 5, 6.
- Reduction check: the squarefree part of χ_m divides H_m for m = 2..5, so Spec(L_m) ⊂ roots(H_m) as the README states.
- H-based certificate exactly over Z (not mod p): deg gcd(Q_n, H_{n−1}∘R) = 1 with λ dividing it, and deg gcd(Qt_n, H_{n−1}∘R) = 0, for every n = 3..14. This covers the repository's n ≤ 11 and extends it.
- Repository script re-run at 7b1495f: same degrees, Schur residuals ≤ 2·10^{−14}, F_p certificate n = 3..11 as stated.
- Not broken.

## Experimental Validation

None. Pure graph spectral statement.

## Mathematical Status

Derivative of classical decimation; prose proof in-repo for c_n and DN_n(2) = 0; exact finite computation for h_n, 3 ≤ n ≤ 11 in-repo (archive: 3 ≤ n ≤ 14 over Z). All-n exact h_n remains open (DISC-0027).

## Patent Relevance

None established.

## Related Discoveries

- DISC-0025. Mathematical. Its lower bound is an equality for 3 ≤ n ≤ 11 (repository) and 3 ≤ n ≤ 14 (archive); its Qiu §2 dependence for c_n is removed.
- DISC-0020. Mathematical. Supplies vanishing of exceptional eigenfunctions on V_0.
- DISC-0022. Mathematical. The symmetric-channel poles 2 − R^{n−1} are not identified with a Dirichlet spectrum by the repository; do not conflate.
- DISC-0027. Mathematical. The open all-n statement.

## Open Questions

A general-n proof that gcd(Q_n Qt_n, H_{n−1}∘R) = λ.

## Next Experiments

Cite c_n = 5·2^{n−1}+1 and dim DN_n(2) = 0 as CLAIMED prose results; cite exact h_n only for 3 ≤ n ≤ 11 as the repository does. Do not read any of it as a physical rate or as selecting W.

## Reproduction Instructions

Clone beyond-repair/finite-gasket-spectral-derivatives at 7b1495fe1dd322d17f7b7d840b22c7d9f29faf10 and run `python3 scripts/check_corner_channels.py 11` (about one minute on CPU, pure Python). The archive's n ≤ 14 exact-Z run used python-flint 0.9.0 fmpz_poly gcd (n = 14 about two minutes).

## Evidence Log

- 2026-10-08. Read CLAIM_STATUS, COMPLETION_LOG, README diff at 7b1495f; re-ran repository script; independent constructor, sympy and flint checks above. GitHub description still matches the claim fence ("W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum, no selected W, no thrust.").

## Change History

- 2026-10-08. Initial archive entry.
