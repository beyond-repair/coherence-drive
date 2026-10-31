# Discovery: Exact share identity and corner-moment Gauss–Radau share floor σ_n ≥ 1.310267 (Theorem AP)

## Discovery ID

DISC-0104

## Status

THEOREM

## Date Discovered

2026-10-22 (America/New_York). Same archive pass as DISC-0105, DISC-0106, DISC-0107, and DISC-0108.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit a1486faddc997650ce5b786104490aa6d13d2104 (main tip 2026-10-22 00:58 EDT, before 4b4509f6f086f3f52b034f55508862f130381f2b). Paths: GASKET.md "Theorem AP. Exact share identity and a corner-moment floor: the combinatorial share exceeds 1" (ASSUMPTION, THEOREM AP items 1–5, Proof (1)–(5), Witness, Kept Failure AP.1, OBSERVATION, NOT THIS; Conjecture J.1 evidence paragraph and OPEN bullet updated); CLAIM_STATUS.md (audit-norm row ‖F(n,0.45)‖≥0.415238 / 0.274743; new AP row); README.md Sequel; scripts/gasket_fractional_moment_share.py (new); scripts/cli.py.

## Original Evidence

GASKET.md Theorem AP, for every α∈(0,1) and every level n≥1 (corner data (1,−1/2,0); β=1−α; Theorems J, AD (i), AK (0) used as stated; AM, AO only for the floors in item 5):
1. Exact share identity: Lu=L^β(L^α u) and I^α=I^α_a(1,−4/5,−1/5), so σ_n=(L^β)_aa+ω_n with ω_n=−(L^β)_ab=−(L^β)_ac>0.
2. Corner moments m_k=(L^k)_aa: 1,2,6,22,92 at every n≥1; m_5=414 (n=1), 418 (n≥2).
3. Gauss–Radau floor: σ_n>(L^β)_aa≥S_AP(α)=(1+33^(−1/2))t_1^(−α)+(1−33^(−1/2))t_2^(−α), t_{1,2}=(13∓√33)/4.
4. Lobatto refinement (n≥2) on {0,s_1,s_2,6}, s_{1,2}=(61∓√685)/22, using spec(L)⊂[0,6].
5. At α=0.45: S_AP≈1.310267, S_Lob≈1.319222 (vs σ_AK≈0.701556 and AK.1's cap ≈0.9529); ‖F(n,0.45)‖≥0.274743 with AM's floor 0.209685 and ≥0.415238 with AO's floor 0.316911 "as stated".

## Discovery

The combinatorial-to-fractional share is exactly a diagonal entry of the complementary power L^(1−α) plus a positive corner-to-corner term, and five level-independent corner moments give a Gauss–Radau floor σ_n≥1.310267>1 at α=0.45. This leaves the one-step neighbor-Harnack family (DISC-0088…0094) entirely and lifts the proved audit floor from 0.222331 (DISC-0102) to 0.274743 (AM route) / 0.415238 (AO as stated). It does not prove convergence or L≥0.70 (Kept Failure AP.1, DISC-0105). Not thrust.

## Why It Matters

It is the share half of the factorization ‖F‖=σ_n‖F_frac‖ (DISC-0076), now within ≈3.1% of the live σ_n. Kept Failure AP.1 isolates the remaining step as a resistance ceiling R_α(n)≤2.859237, which the next commit (Theorem AQ, DISC-0106) supplies. AP (1) is also used by AQ (σ_n=½vᵀL^βv).

## Derivation

Repository proof, checked step by step in this archive:
1. L^βL^α=L in the eigenbasis; L^αu is supported on the corners (L^α-harmonic off corners); AD (i) gives I^α=κ(5/2,−2,−1/2). By corner S₃ symmetry the corner block of L^β is pI+qJ, so in fact the whole vector satisfies I=(p−q)·I^α (archive: this also re-derives AB's ‖F‖=σ‖F_frac‖ directly). Theorem J gives ω_n>0.
2. Le_a and L²e_a live in the level-1 corner cell, so m_0…m_4 are level-independent; m_5 depends on deg f_1.
3. x^β has f^(5)>0; the Hermite quartic interpolating at 0 (simple) and t_1,t_2 (double) is a minorant (ε-limit at 0); its integral against μ_a depends only on m_0…m_4 and equals the Radau sum. Orthogonal quadratic of x dμ_a is x²−13x/2+17/2; Radau weight at 0 is 3/17.
4. f^(6)<0 and x(x−s_1)²(x−s_2)²(x−6)≤0 on [0,6] give the Lobatto minorant for n≥2.
5. Arithmetic with AM/AO floors.

## Assumptions

Spectral calculus (GASKET item 4); corner data (1,−1/2,0); Theorems J (DISC-0032), AB (DISC-0076), AD (DISC-0080), AK (0) (DISC-0094) as stated. The 0.274743 floor uses AM (DISC-0098); the 0.415238 floor uses AO "as stated" (DISC-0102), whose three-corner defect δ₂<0.55 is a finite-range witness, so 0.415238 inherits that caveat (the repository itself flags "AO as stated"). Items 1–4 need neither.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AP.log` (repository witness `python3 scripts/gasket_fractional_moment_share.py` at a1486faddc997650ce5b786104490aa6d13d2104 — script unchanged at 4b4509f6f086 — EXIT 0, 97 PASS, 0 FAIL, ~31 s) and `/workspace/scratch-ifi/indep_theorem_AP.py` / `indep_theorem_AP.log` (own builder `/workspace/scratch-ifi/sg_indep_common.py`, no repo import; numpy + mpmath + fractions; EXIT 0, 84 PASS, 0 FAIL, ALL PASS):
- exact integer corner moments (L^k)_aa, k=0..5, on levels 1–9: [1,2,6,22,92,414] at n=1 and [1,2,6,22,92,418] for n=2..9;
- orthogonal quadratic rebuilt in Fractions (p,q)=(−13/2,17/2); Gauss weights 1±33^(−1/2); Radau weight at 0 = 3/17 (exact algebra: (t_1+t_2+(t_2−t_1)/√33)/(t_1t_2)=14/17); Radau law reproduces 1,2,6,22,92 to 1e−24;
- S_AP(0.45)=1.3102673… (30 digits), S_Lob(0.45)=1.319222; Lobatto weights positive, moments 1,2,6,22,92,418;
- Hermite quartic ≤x^β on (0,60] and Lobatto quintic ≤x^β on (0,6] at five / three α (min gap ≥0 to 1e−20); f^(5)>0, f^(6)<0;
- live levels 1–7 at α=0.45 and 1–5 at α∈{0.1,0.3,0.5,0.6,0.8,0.95}: harmonicity, Lu=L^βL^αu, I^α∝(1,−4/5,−1/5), ω_b=ω_c>0, σ=(L^β)_aa+ω and the vector identity I=σI^α to ≤2e−12; σ_n>(L^β)_aa≥S_AP (≥S_Lob for n≥2); level 1 (L^β)_aa=1.314296<S_Lob (Lobatto genuinely needs n≥2);
- repository table reproduced to 6 digits ((L^0.55)_aa 1.314296…1.352472; σ_n 1.435558…1.352483); level 7: (L^0.55)_aa=1.352475, ω=1.468e−6, σ=1.352477, ‖F‖=0.860818;
- floors 0.274743, 0.415238, 0.418076 (S_Lob·AO) and ratios 1.236×AO, 1.868×σ_AK reproduced.

## Prior Art

Elementary: Löwner–Heinz-free spectral calculus, Gauss–Radau / Gauss–Lobatto quadrature bounds for functions with sign-definite high derivatives (classical moment-problem technique). Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete elementary proof in the repository, verified here). Not a novelty claim.

## Falsification Attempts

Independent graph; exact integer moments to level 9 (beyond the repository's level 6); Radau/Lobatto data rebuilt from moments in exact arithmetic; minorant checks at several α; vector form of the share identity checked (stronger than the a-component). No gap found in items 1–4. Only caveat: item 5's 0.415238 inherits AO's finite-range defect step.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proof and witness verified. Supersedes DISC-0102's numerical audit floor (DISC-0102 row not edited). Itself superseded as a floor by DISC-0106 (Theorem AQ: ‖F(n,0.45)‖>0.819255) in the next commit; AP (1) remains an ingredient of AQ.

## Patent Relevance

None.

## Related Discoveries

- DISC-0076. Mathematical. Theorem AB factorization ‖F‖=σ_n‖F_frac‖; AP gives σ_n exactly.
- DISC-0094, DISC-0095. Mathematical / failed hypothesis. AK's σ_AK and AK.1's 0.9529 cap; AP's 1.310267 exceeds both.
- DISC-0098, DISC-0102. Mathematical. Fractional floors used in item 5.
- DISC-0105. Failed hypothesis. Kept Failure AP.1.
- DISC-0106. Mathematical. Theorem AQ uses AP (1) and closes AP.1's open step.
- DISC-0034. Conjecture J.1 (status changed by DISC-0106, not by this row).

## Open Questions

None left by AP itself; the open step it named (resistance ceiling ≤2.859237) is closed by DISC-0106.

## Next Experiments

None.

## Reproduction Instructions

`git checkout a1486faddc997650ce5b786104490aa6d13d2104 && python3 scripts/gasket_fractional_moment_share.py`. Archive: `python3 /workspace/scratch-ifi/indep_theorem_AP.py`. Logs: `/workspace/scratch-ifi/repo_theorem_AP.log`, `/workspace/scratch-ifi/indep_theorem_AP.log`.

## Evidence Log

- 2026-10-22. Recorded from GASKET.md Theorem AP at a1486faddc997650ce5b786104490aa6d13d2104; repo witness EXIT 0 (97 PASS); independent check ALL PASS (84 PASS). Repository description still matches its claim fence (closed-surface identity / not a net force).

## Change History

- 2026-10-22. Initial archive entry.
