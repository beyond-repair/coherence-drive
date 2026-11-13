# Discovery: Dirichlet bottom ratio λ_min(n)/λ_min(n−1) → 1/5

## Discovery ID

DISC-0022

## Status

DERIVATIVE

## Date Discovered

2026-10-02. Archive pass for beyond-repair/finite-gasket-spectral-derivatives Dirichlet bottom-ratio commit.

## Source Repositories

beyond-repair/finite-gasket-spectral-derivatives at commit 9aa404950322594069bf91547ea2cb34c253eaae (HEAD audit 19a1264e4511a2ff2e60e55040590e250372d3f0). README section “Dirichlet bottom ratio”; COMPLETION_LOG.md; CLAIM_STATUS.md.

Operator: Dirichlet principal submatrix L_D on I_n = V_n \ V_0 of build_gasket(n). Not free L (free λ_min = 0).

## Original Evidence

CLAIM_STATUS.md marks Dirichlet λ_min(n)=φ_−^{(n−1)}(2), ratio → 1/5 as **CLAIMED**, citing Qiu §2 structure (opened) plus branch comparison.

README theorem: for every integer n ≥ 1,
    λ_min(n) = φ_−^{(n−1)}(2), φ_−(x) = (5 − √(25 − 4x))/2;
for n ≥ 2,
    λ_min(n)/λ_min(n−1) = 2/(5 + √(25 − 4 λ_min(n−1))) → 1/5.

COMPLETION_LOG / README classical note: Qiu arXiv:1206.1381 §2 already records D_1 = {2, 5}, initial 5 and 6 for m ≥ 2, and φ_−(x) = x/5 + O(x²) as x → 0. The identification and ratio limit “use that classical structure plus elementary branch comparison; they are not a new discovery of spectral decimation.”

## Discovery

Upgrading the SPECTRUM.md Dirichlet ratio table / “→ 1/5” numerical line to a theorem for L_D of gasket_graph.py is derivative of classical spectral decimation plus elementary branch comparison and rationalization. Free hit rates are not upgraded.

## Why It Matters

Records that the Dirichlet bottom-ratio claim is classical-structure derivative, so it is not a novelty row and does not select W or thrust.

## Derivation

No derivation is repeated here. Induction on φ_− branch geometry and rationalization of φ_−(x)/x are in the README.

## Assumptions

L_D is the Dirichlet principal submatrix of free L on build_gasket(n), identified in-repo with Qiu’s −Δ_n on Γ_n \ V_0. Classical decimation rules from Qiu (Fukushima–Shima 1992 not opened).

## New Results

None.

## Prior Art

Qiu arXiv:1206.1381 §2 / Prop. 2.1 and (2.3)–(2.6); Fukushima–Shima / Shima spectral decimation. Repo states this explicitly.

## Novelty Analysis

Status is DERIVATIVE. The repository itself disclaims novelty of spectral decimation.

## Falsification Attempts

Local eigvalsh of L_D on gasket_graph.py @ 0742f00ed275969547925da430c1041bc58b9754 for n = 1..5 matches φ_−^{(n−1)}(2) to machine precision; successive ratios match the closed form. Supporting only. No attempt to elevate beyond DERIVATIVE.

## Experimental Validation

None.

## Mathematical Status

Derivative of classical Dirichlet spectral decimation applied to gasket_graph.py.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0005. Mathematical. SPECTRUM.md Dirichlet ratio table being upgraded.
- DISC-0020. Mathematical. Free multiplicities on a different operator.
- DISC-0007. Mathematical. Free V'' split does not use Dirichlet λ_min.
- DISC-0002. Mathematical. Ratio limit is not thrust / not 0.08.

## Open Questions

None opened by this row. Free hit-rate predicate remains open on DISC-0020/0021.

## Next Experiments

Do not cite as a new spectral-decimation discovery. Keep Dirichlet statements separate from free L.

## Reproduction Instructions

Read README “Dirichlet bottom ratio” at 9aa404950322594069bf91547ea2cb34c253eaae. Compare SPECTRUM.md Dirichlet table. Optional: eigvalsh L_D for n = 1..5.

## Evidence Log

- 2026-10-02. Read Dirichlet section at 9aa404950322594069bf91547ea2cb34c253eaae; local L_D bottoms match φ_− iteration for n = 1..5.

## Change History

- 2026-10-02. Initial archive entry.
