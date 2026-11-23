# Discovery: Positive limit of the α = 0.45 gasket audit norm (Conjectures J.1, J.2)

## Discovery ID

DISC-0034

## Status

THEOREM (Conjecture J.1, since 2026-10-22, via DISC-0106 / IFI Theorem AQ at 4b4509f6f086f3f52b034f55508862f130381f2b). J.2 (α = 0.10) was not decided and is carried forward as DISC-0108 (CONJECTURE).

Status history (not rewritten): CONJECTURE from 2026-10-08 (recorded at 81ab02b501aef7df2f5478f55d67d50f93595d56) through 2026-10-15 (DISC-0072…DISC-0103 recorded as edges, "DISC-0034 stays CONJECTURE"); THEOREM for J.1 from 2026-10-22. The sections below are the original 2026-10-08 record and are kept as written.

## Date Discovered

2026-10-08 (America/New_York). Same archive pass as DISC-0031.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56. Path: GASKET.md "Conjecture J.1" and the α = 0.10 Conjecture J.2; CLAIM_STATUS.md row "Fractional audit norm, α = 0.45, zero vs positive — OPEN". Witness: scripts/gasket_fractional_level10.py (prints conjecture_J1_still_open_above_0.70 True).

## Original Evidence

GASKET.md: "CONJECTURE, not a theorem. For α = 0.45 … ‖F(n)‖ decreases for every n ≥ 1 and lim ‖F(n)‖ = L with L ≥ 0.70." Falsifier: first level with ‖F‖ < 0.70 or a rise above 10^{−8}. Through level 10, ‖F(10)‖ ≈ 0.833640, not fired. J.2: ‖F(n, 0.10)‖ ≥ 1.410 for every n.

## Discovery

Repository conjectures, recorded as stated.

## Why It Matters

It is the repository's single open mathematical question in the gasket note. A positive limit would be a finite neutral dipole, not thrust; the repository says so.

## Derivation

None in-repo. Open.

## Assumptions

As DISC-0032.

## New Results

Archive evidence (DISC-0035, a separate conjecture): the fitted law 1/‖F(n,α)‖ ≈ A(α) + B(α)(5^α/3)^n predicts L(0.45) ≈ 0.8211 and L(0.10) ≈ 1.4106. Both are consistent with J.1 (L ≥ 0.70) and with J.2 (≥ 1.410, margin only about 6·10^{−4}). Archive independent levels 1–7 at α = 0.10 give ‖F(7, 0.10)‖ = 1.410949855, still above 1.410.

## Prior Art

Not searched for this functional. No novelty claimed.

## Novelty Analysis

CONJECTURE (repository's own open item).

## Falsification Attempts

Independent recomputation of levels 1–7 at α = 0.10 and 0.45; repository level-10 replay rerun. Not broken.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

2026-10-22 status change: J.1 proved by IFI Theorem AQ (DISC-0106): ‖F(n,0.45)‖ strictly decreases for every n ≥ 1 (exact spectral-decimation recursion for the corner resolvent plus Stieltjes integrals; algebraic, all n) and converges to 𝓛 ∈ [0.819255, 0.822959] (outward-rounded interval certificate), so L ≥ 0.70; archive re-certification with exact α = 9/20 gives 𝓛 ∈ [0.819784, 0.822494] and ‖F(n,0.45)‖ ≥ 0.819784 at every level. Closed form of 𝓛 open. J.2 open (DISC-0108). Original 2026-10-08 text follows.

Open. Divergence excluded (DISC-0032, Theorem J); zero would follow from energy collapse (Theorem L), which is not proved and not seen (Q_{0.45}(u_10) ≈ 0.941537).

## Patent Relevance

None.

## Related Discoveries

- DISC-0032. Mathematical. Bounds bracketing the limit.
- DISC-0033. Mathematical. Rejected shortcut laws.
- DISC-0035. Computational. Scaling law predicting L ≈ 0.821.

## Open Questions

Prove a positive lower bound on ‖F(n, 0.45)‖ uniform in n.

## Next Experiments

Level 11 (N = 265,722) with the repository's matrix-free code; DISC-0035 predicts ‖F(11)‖ ≈ 0.82970.

## Reproduction Instructions

`git checkout 81ab02b501aef7df2f5478f55d67d50f93595d56 && python3 scripts/gasket_fractional_level10.py`

## Evidence Log

- 2026-10-08. Recorded from GASKET.md at 81ab02b.
- 2026-10-22. IFI 4b4509f6f086f3f52b034f55508862f130381f2b (Theorem AQ) proves J.1; GASKET.md's J.1 header now reads "Status: PROVED by Theorem AQ (formerly a conjecture; the text below records it as first stated)" with the statement body unchanged (archive diff check vs 7f0099c). Repo witness scripts/gasket_fractional_decimation.py EXIT 0 (69 PASS); archive /workspace/scratch-ifi/indep_theorem_AQ.py independent first-principles levels 1–7 and own interval certificate agree. Falsifiers can no longer fire (‖F(n)‖ > 0.819255 and strictly decreasing). Prior commit a1486faddc997650ce5b786104490aa6d13d2104 (Theorem AP, DISC-0104/0105) had left J.1 open.

## Change History

- 2026-10-08. Initial archive entry.
- 2026-10-22. Status change CONJECTURE → THEOREM for J.1 (DISC-0106); J.2 carried forward as DISC-0108 (CONJECTURE). Earlier text retained.
