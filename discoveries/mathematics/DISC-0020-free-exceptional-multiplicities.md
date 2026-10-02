# Discovery: Free exceptional multiplicities mult(3), mult(5), mult(6) on build_gasket

## Discovery ID

DISC-0020

## Status

NOVELTY CANDIDATE

## Date Discovered

2026-10-02. Archive pass for beyond-repair/finite-gasket-spectral-derivatives after HEAD moved past the DISC-0007/0008 evidence commit.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at HEAD 19a1264e4511a2ff2e60e55040590e250372d3f0 (head audited at Dirichlet commit 9aa404950322594069bf91547ea2cb34c253eaae).

Evidence commits for the three free-multiplicity claims:

- Free mult(6): 393c59aa4f521187ba3d5b7f809dfdf4ce494f77
- Free mult(5): e42497657a230b276af5a47f130d8c93446becf2
- Free mult(3): 72fec06b8a86cf58f92bfbff711b9ffddbca1a84

Files: README.md sections “Free mult(6)”, “Free mult(5)”, “Free mult(3)”; COMPLETION_LOG.md; CLAIM_STATUS.md at the same HEAD.

Graph constructor: beyond-repair/sierpinski-geometry-045 `gasket_graph.py` `build_gasket` (not in the finite-gasket tree). SPECTRUM.md numerical lines for n = 2..5 are the prior DISC-0005 inputs that these claims upgrade from observation to claimed theorem for free L = D − A.

## Original Evidence

CLAIM_STATUS.md at 19a1264e4511a2ff2e60e55040590e250372d3f0 marks all three free multiplicities **CLAIMED** (prose argument in README / COMPLETION_LOG; constructor lives in sierpinski-geometry-045). Claim cap ≤ 1. Kernel tests in `tests/test_spectral_derivatives.py` do **not** assert multiplicities.

README theorems (quoted structure, not re-proved here):

- For every integer n ≥ 2, free L = D − A on build_gasket(n) has mult(6) = (3^n − 3)/2 = |V_{n−1} \ V_0|, via localized modes u_x and injectivity of restriction to V_{n−1} \ V_0.
- For every integer n ≥ 3, mult(5) = (3^{n−1} − 1)/2, via DN_5 ⊂ free, free ∩ {u|_{V_0}=0} = DN_5, and a free corner obstruction that forces c = 0 for n ≥ 3 (n = 2 exception: free mult(5) = 2).
- For every integer n ≥ 2, mult(3) = (3^{n−1} − 3)/2, via midpoint extension of free 6-modes at λ = 3 (Qiu extension formula) and injective restriction back to free 6-space.

Classical comparison in-repo: Dirichlet mult(6) and Dirichlet mult(3) carry the **same integers** on a different operator (corners grounded); Neumann counts differ; free L is not identified with either. Opened sources cited: Qiu arXiv:1206.1381; Okoudjou–Strichartz–Tuley arXiv:1110.1554; UConn REU Neumann/Dirichlet writeups 2025. CLAIM_STATUS and COMPLETION_LOG state those sources do not by themselves prove the free D − A statements.

## Discovery

The free (finest-upward-edge, corner degree 2) combinatorial Laplacian on build_gasket(n) is claimed to obey closed multiplicity formulas for the exceptional values {3, 5, 6} for all n in the stated ranges. This closes the free mult(6) open item left on DISC-0007 at HEAD 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 and adds free mult(5) and free mult(3).

## Why It Matters

DISC-0007’s V'' bound used free mult(6) only numerically for n = 2..5. A uniform free-multiplicity theorem would firm that input without selecting W or thrust. Classification stays below THEOREM because the proofs are prose-only, the constructor is out-of-tree, CLAIM_STATUS marks CLAIMED rather than CI-locked, and the integers coincide with classical Dirichlet counts on a neighboring operator.

## Derivation

No derivation is repeated here. The repository already writes the three subsections. This archive does not add another form.

## Assumptions

build_gasket(n) as in sierpinski-geometry-045/gasket_graph.py: finest upward edges only; corners deg 2; all other vertices deg 4; L = D − A free on all of V_n. Classical DN / Dirichlet / Neumann counts are inputs only where the README says so (especially free mult(5)).

## New Results

None beyond what those commits already state. This row indexes them.

## Prior Art

Dirichlet and Neumann multiplicities for {3, 5, 6} on SG graph approximations are classical (Qiu; Fukushima–Shima; Okoudjou–Strichartz–Tuley; UConn REU 2025). The free operator with deg-2 corners is distinguished in-repo. A 2026-10-02 prior-art skim did not turn up a standard free-L multiplicity theorem matching these formulas; that skim is not a complete literature search.

## Novelty Analysis

Status is NOVELTY CANDIDATE, not THEOREM and not DERIVATIVE. The free-side corner / restriction arguments are the candidate content. Same integers as Dirichlet for mult(6) and mult(3) keep the elevation conservative.

## Falsification Attempts

- Algebra: formulas match SPECTRUM.md n = 2..5 lines and the exceptional-mass algebra used in DISC-0021.
- Local numerics on sierpinski-geometry-045 `gasket_graph.py` at 0742f00ed275969547925da430c1041bc58b9754: for n = 2..5, eigvalsh free multiplicities match the claimed formulas exactly (n = 2 mult(5) = 2 exception included). Supporting only; not a substitute for the all-n injectivity arguments.
- Break attempts that failed to reject: no counterexample on n = 2..5; CLAIM_STATUS already refuses continuum / W / thrust upgrades.
- Residual risks: prose-only proof; constructor not in finite-gasket tree; tests do not cover multiplicities; Actions conclusion “not yet observed” per CLAIM_STATUS.

## Experimental Validation

None. experimental_validation false. Local eigvalsh support only.

## Mathematical Status

Claimed combinatorial theorems on free L for build_gasket; archived here as NOVELTY CANDIDATE pending stronger verification or independent prior-art closure.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0007. Historical / mathematical. Earlier HEAD left free mult(6) open; eigenspace split remains DERIVATIVE.
- DISC-0005. Mathematical. SPECTRUM.md numerical locks that these claims upgrade.
- DISC-0008. Mathematical. Two-point {0, 6} saturation remains REJECTED; free spectra still carry 3 and 5.
- DISC-0021. Mathematical. Exceptional-mass corollary of these three formulas.
- DISC-0022. Mathematical. Dirichlet bottom ratio on L_D (different operator).
- DISC-0002. Mathematical. Free multiplicities do not select 0.08 or thrust.

## Open Questions

Decimation hit-rate predicate on free Spec(L_n) \ {3, 5, 6} and whether hit mass equals 1 − μ_exc remain open (repo refuses that upgrade). Independent refereeing of the free injectivity / corner-obstruction arguments remains open.

## Next Experiments

Do not promote to THEOREM without an in-tree constructor or machine-checked proof. Do not identify free L with Dirichlet or Neumann. Do not select W or thrust from multiplicities.

## Reproduction Instructions

Check out beyond-repair/finite-gasket-spectral-derivatives at 19a1264e4511a2ff2e60e55040590e250372d3f0. Read README Free mult(6)/(5)/(3), COMPLETION_LOG.md, CLAIM_STATUS.md. Compare against sierpinski-geometry-045 gasket_graph.py and SPECTRUM.md. Optional: eigvalsh free multiplicities for n = 2..5.

## Evidence Log

- 2026-10-02. Diff 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0...19a1264e4511a2ff2e60e55040590e250372d3f0: +7 commits; CLAIM_STATUS.md added; README / COMPLETION_LOG record the three free-multiplicity theorems.
- 2026-10-02. Local eigvalsh on gasket_graph.py @ 0742f00ed275969547925da430c1041bc58b9754 matches claimed mult(3,5,6) for n = 2..5.
- 2026-10-02. GitHub description still matches claim fence: “W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum, no selected W, no thrust.” No new description mismatch.

## Change History

- 2026-10-02. Initial archive entry. Closes the free mult(6) open note on DISC-0007 by indexing the later HEAD claims; does not change DISC-0007’s DERIVATIVE status for the eigenspace split.
