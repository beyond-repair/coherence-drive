# Discovery: Combinatorial audit limit equals vanishing of the two-neighbor fractional share (Theorem AB)

## Discovery ID

DISC-0076

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Archive pass after DISC-0074 / DISC-0075.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 46915585f71b8d3292fa26d32405d8ff112d3d3a. Paths: GASKET.md "Theorem AB. The combinatorial audit limit is the two-neighbor fractional share" (Assumption, Theorem AB items 1–4, Proof, Witness, Kept Failure AB.1, NOT THIS); scripts/gasket_fractional_share.py; scripts/cli.py (entry added); CLAIM_STATUS.md (new row "Combinatorial-to-fractional corner share σ_n = I_a/I_a^α = ρ_n/w_n" VERIFIED; α=0.45 OPEN row extended); README.md Sequel paragraph. Item 4 is extended from α<1/2 to α<log3/log5 at 51789b3ef3c56d6e678f9df35dd276a1c8657a87 (Theorem AC, DISC-0078).

## Original Evidence

For the L^α-Dirichlet minimizer u_n with corner data (1,−1/2,0), α∈(0,1), n≥1: the altitude reflection through the value-1 corner a is a graph automorphism, so both neighbor weights equal w_n(α)=−(L^α)_{ap}=−(L^α)_{aq}. With I_a=(Lu_n)_a, I_a^α=(L^α u_n)_a, ρ_n=w_n I_a/I_a^α (two-neighbor share) and σ_n=I_a/I_a^α=‖F‖/‖F_frac‖: σ_n=ρ_n/w_n, w_min(α)=α4^{α−1} ≤ w_n ≤ 8^α, ρ_n/8^α ≤ σ_n ≤ ρ_n/w_min ≤ 1/w_min. With the Theorem AA floor (α<1/2): ‖F(n,α)‖→0 ⇔ σ_n→0 ⇔ ρ_n→0, and liminf‖F‖>0 ⇔ liminf ρ_n>0.

## Discovery

An exact factorization of the combinatorial-to-fractional audit ratio into the two-neighbor share of the fractional corner current divided by a level-bounded neighbor weight. After AA (and AC) floor the fractional current, the open α=0.45 question (DISC-0034) is reduced exactly to whether ρ_n→0.

## Why It Matters

Names the single remaining route to ‖F(n,0.45)‖→0 after energy collapse was closed (DISC-0073). Does not evaluate lim ρ_n; DISC-0034 stays OPEN. Not thrust.

## Derivation

Repository proof, checked in this archive:
1. Reflection (i,j)↦(j,i) in lattice coordinates fixes a, swaps p,q, conjugates L and hence L^α ⇒ equal weights.
2. All off-diagonals of L^α are negative (subordination); with L^α𝟙=0 the maximum principle gives u_n∈[−1/2,1], so every term of I_a^α=Σ_j w_aj(u_a−u_j) is ≥0 and ρ_n∈(0,1].
3. Both corner-current triples lie on the S3 Schur shape 3·BC−ΣBC=(2.5,−2,−0.5), so ‖F‖=I_a√21/5 and ‖F_frac‖=I_a^α√21/5; σ_n=I_a/I_a^α=ρ_n/w_n.
4. w_n≥w_min is the Theorem J off-diagonal bound; w_n≤(L^α)_aa≤λ_max(L)^α≤8^α (archive: actually ≤8^α/2 since both neighbors share the diagonal).
5. Equivalence: ‖F‖=σ_n‖F_frac‖. "⇒" uses the AA floor; "⇐" (σ→0 ⇒ ‖F‖→0) also needs ‖F_frac‖ bounded above. The proof text cites only the floor; the ceiling is available (AA ceiling Q≤(7/6)8^α, or the competitor bound Q≤1.25·8^α valid for every α, checked here). Presentation gap only; claim holds.

## Assumptions

Spectral calculus (GASKET item 4); corner data (1,−1/2,0); Theorem J off-diagonal bound and Theorems J/K/L pairing (DISC-0032); Theorem AA floor (DISC-0072) for item 4, extended by Theorem AC (DISC-0078).

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AB.log` (repository witness at 46915585f, EXIT 0, 54 PASS, 0 FAIL; re-run at tip 51789b3ef also passes) and `/workspace/scratch-ifi/indep_theorem_AB.py` / `indep_theorem_AB.log` (own integer-lattice gasket builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; 218 PASS, ARCHIVE_INDEP_THEOREM_AB_PASS): levels 1–7 (level 7 not in repo) at α∈{0.30,0.45,0.60,0.68}: reflection is an automorphism; equal weights to 1e−12; all off-diagonals of L^α negative; u∈[−1/2,1]; both current triples on the Schur shape; σ=ρ/w_n to 1e−12; w_min≤w_n≤8^α/2; sandwich; Q=1.4·I_a^α and Q≤Q(competitor)≤1.25·8^α. α=0.45 values match GASKET to 1e−6 on levels 1–6: w_n≈(0.389568,…,0.332260), ρ_n≈(0.559247,0.470964,0.453153,0.449983,0.449460,0.449376), σ_n≈(1.435558,…,1.352483); archive level 7: ρ_7≈0.44936293, σ_7≈1.35247662.

## Prior Art

Graph-automorphism invariance of spectral functions; Bochner subordination (negative off-diagonals of L^α); discrete maximum principle; elementary algebra. Theorems J/K/L (DISC-0032), Theorem AA (DISC-0072). Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). A reformulation/reduction lemma, not a novelty claim and not a Stage-1 / claim-level raise.

## Falsification Attempts

Independent rebuild through level 7 and at four α values; tried max-principle and Schur-shape failure modes; none found. Numerical observation (not a claim, not a new row): ρ_n drops shrink by ≈0.158–0.20 per level (8.8e−2, 1.8e−2, 3.2e−3, 5.2e−4, 8.4e−5, 1.3e−5), Aitken extrapolation ρ_∞≈0.44936. That suggests a positive limit but proves nothing; DISC-0034 stays OPEN.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Minor presentation gap noted (ceiling needed for "⇐", available). Witness-doc mismatch: GASKET says "Passing `--through 7` recomputes one level higher", but the script parses `sys.argv[1]` as an integer and crashes on `--through` (the positional form `7` works). Does not decide lim ρ_n.

## Patent Relevance

None.

## Related Discoveries

- DISC-0072. Mathematical. Theorem AA floor used in item 4.
- DISC-0078. Mathematical. Theorem AC extends item 4 to every α<log3/log5.
- DISC-0077. Failed hypothesis. Geometric collapse of ρ rejected.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN, now equivalent to lim ρ_n.
- DISC-0032. Mathematical. Theorems J/K/L.

## Open Questions

Whether ρ_n(0.45)→0 (equivalently ‖F(n,0.45)‖→0) or stays positive.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout 46915585f71b8d3292fa26d32405d8ff112d3d3a && python3 scripts/gasket_fractional_share.py` (positional `7` for one more level). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AB.py 7`. Logs: `/workspace/scratch-ifi/repo_theorem_AB.log`, `/workspace/scratch-ifi/indep_theorem_AB.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AB at 46915585f71b8d3292fa26d32405d8ff112d3d3a; repo witness EXIT 0; independent check ARCHIVE_INDEP_THEOREM_AB_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
