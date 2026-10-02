# Discovery: Lambda = 6 eigenspace split of Gamma_loop and V''

## Discovery ID

DISC-0007

## Status

DERIVATIVE

## Date Discovered

2026-10-01. This is the date of the archive pass that indexed the new HEAD content.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0. The section is "Lambda = 6 eigenspace split" in README.md. COMPLETION_LOG.md at the same HEAD restates the identities and the bound.

The spectral inputs lambda_max = 6 and free mult(6) for n = 2..5 are DISC-0005, from beyond-repair/sierpinski-geometry-045 SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.

The earlier finite-gasket trace identity at the prior HEAD is DISC-0003.

## Original Evidence

At HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 the repository splits the locked sums. Write m_6 = mult(6) >= 1 and {mu_j} for complementary eigenvalues in [0, 6). For every real W < 1/6,

    Gamma_loop(W) = (m_6 / 2) ln(1 - 6W) + (1/2) sum_j ln(1 - W mu_j),

    V''(W) = - 18 m_6 / (1 - 6W)^2 - (1/2) sum_j mu_j^2 / (1 - W mu_j)^2.

Bound. For every W in [0, 1/6),

    V''(W) <= - 18 m_6 / (1 - 6W)^2 < 0,

with equality in <= if and only if every mu_j equals 0.

On free gasket graphs of SPECTRUM.md with n >= 2, eigenvalues lie in (0, 6), so the inequality is strict. With Tr L = 6 * 3^n and the SPECTRUM.md multiplicity formula m_6 = (3^n - 3)/2 for n = 2..5, Tr L - 6 m_6 = 3^{n+1} + 9 > 0.

The repository states that the split is elementary from the locked definitions once lambda = 6 is factored out. It does not select W, does not state a continuum limit, and does not state a force.

COMPLETION_LOG.md marks free mult(6) = (3^n - 3)/2 for all n >= 2 as still open: numerical for n = 2..5 in SPECTRUM.md; the Dirichlet analogue is classical (Qiu arXiv:1206.1381 Section 2), and is not a free-graph proof.

## Discovery

The eigenspace split and the V'' bound above follow by factoring lambda = 6 out of the locked finite-gasket formulas. They are derivative of those definitions and of DISC-0005. They do not select W and they do not give thrust.

## Why It Matters

The bound shows that the lambda = 6 eigenspace alone already forces V'' < 0 on [0, 1/6). Complementary eigenvalues on the free gasket make the inequality strict. That still does not select 0.08 or thrust. The open free-multiplicity proof is recorded as open, not as proved.

## Derivation

No derivation is repeated here. The repository already writes the split and the bound. This archive does not add another form.

## Assumptions

omega = 1, K = I - W L, spectrum real in [0, 6] with lambda_max = 6 attained, finitely many eigenvalues, W a prescribed scalar. Free-graph strictness uses SPECTRUM.md eigenvalues in (0, 6) for n >= 2. No continuum limit is assumed.

## New Results

None beyond what that HEAD already states.

## Prior Art

Dirichlet multiplicity of the initial eigenvalue 6 on -Delta_m with corners grounded equals (3^m - 3)/2 for m >= 2: Qiu, arXiv:1206.1381, Section 2, after Fukushima–Shima / Shima. The source repository cites that and says it is not a free-graph statement. The split itself is elementary algebra on the locked sums.

## Novelty Analysis

There is no novelty claim. Status is DERIVATIVE. Relation to DISC-0005 is mathematical through lambda_max = 6 and free mult(6) for n = 2..5. Relation to DISC-0003 is historical: same repository, later HEAD section.

## Falsification Attempts

The repository already refuses upgrades to selected W, continuum, force, stress, or momentum. Free mult(6) for all n >= 2 is left open. This archive does not close that open item.

## Experimental Validation

None.

## Mathematical Status

Derivative elementary identity on the locked kernel.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0003. Historical. Earlier finite-gasket identities at the prior HEAD.
- DISC-0005. Mathematical. Spectral inputs lambda_max = 6 and free mult(6) for n = 2..5.
- DISC-0008. Mathematical. Rejection of two-point {0, 6} saturation as a gasket theorem.
- DISC-0002. Mathematical. The split and bound do not select 0.08 or thrust.

## Open Questions

Rigorous proof that free L = D - A on build_gasket(n) has mult(6) = (3^n - 3)/2 for all n >= 2 remains open in COMPLETION_LOG.md. Local W(x) is not settled. No continuum limit is claimed.

## Next Experiments

Do not convert the V'' bound into a selected W or into thrust. Do not treat free mult(6) as proved for all n. Read README.md and COMPLETION_LOG.md at the named HEAD before any later use.

## Reproduction Instructions

Check out beyond-repair/finite-gasket-spectral-derivatives at 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 and read the "Lambda = 6 eigenspace split" section and COMPLETION_LOG.md. Compare free mult(6) and eigenvalues in (0, 6) with SPECTRUM.md in sierpinski-geometry-045 at 16cc0851185d2a38f63dcf53fea22fef7ef915e1.

## Evidence Log

- 2026-10-01. Indexed from README.md and COMPLETION_LOG.md at HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0. Commit message: "Record the lambda=6 eigenspace split of Gamma_loop and V'' and reject two-point abstract bounds as gasket theorems."
- 2026-10-01. SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1 records Tr L = 6 * 3^n, mult(lambda=6) = (3/2)(3^{n-1} - 1), and exceptional eigenvalues including 3 and 5.
- The GitHub description of finite-gasket-spectral-derivatives, fetched the same day, matches the claim fence: "W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum, no selected W, no thrust."

## Change History

- 2026-10-01. Initial archive entry for the new HEAD section. No existing discovery file was overwritten.
