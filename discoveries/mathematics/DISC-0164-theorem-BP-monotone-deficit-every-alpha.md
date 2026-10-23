# Discovery: Theorem BP, the corner deficit δ_N^(n) increases in n for every α∈(0,1), also below a*

## Discovery ID

DISC-0164

## Status

THEOREM in the mathematical sense only (repository proof; analytic plus one arb constant). Method KNOWN (single-crossing covariance inequality). Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~11:55am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 4ee50b22193b5b24b0677a30e83403957f053f5b.

## Original Evidence

GASKET.md Theorem BP (BP.1–BP.5, proof of BP.3 at GASKET.md line 2621), CLAIM_STATUS.md new row, README.md, scripts/gasket_fractional_deficit_small_alpha.py (new, 203 lines), scripts/cli.py, tests/test_cli.py, all at 4ee50b22193b5b24b0677a30e83403957f053f5b. Builds on Theorem BN (DISC-0161, 335860e44ebf) and Theorem BO / Kept Failure BO.1 (DISC-0162, DISC-0163, 18bb38dcc368).

## Discovery

BP.1 (mean floor): ⟨ω_k⟩=D'_(k+1)/D'_k=ρ^−1 D_(k+1)/D_k>ρ^−1=3·5^−α for every α and k (from BK.1 and AQ (3) r_(k+1)≥r_k).

BP.2 (tail): BN.2's majorant d_k'−αd_k/(5+y)≤−P_α/(3(y+2)²(y+5)²) holds for every α≥0; P_α=y²(2αy+17α−1)+46αy+40α+10>0 on [Y_α,∞), Y_α=(1−17α)/(2α), so ω_k is strictly increasing on [Y_α,∞) at every level for α∈(0,1/17].

BP.3 (head): r_k(p)≤1/p gives d_k≥(y+4)(2y+5)/(3(y+2)(y+5)), and (8/5)(y+4)(2y+5)−3(y+2)(y+5)=(y²−y+10)/5>0, so ω_k<(8/5)(1+y/5)^α; on [0,Y_α], 5+Y_α<1/(2α) and (2α)^−α≤e^(1/(2e))<15/8 give ω_k<3·5^−α=ρ^−1<⟨ω_k⟩.

BP.4: so {ω_k≥⟨ω_k⟩}=[y_c,∞) for a single y_c>Y_α, and Cov_(μ_k)(ω_k,G_k)=∫(ω_k−m)(G_k−G_k(y_c))dμ_k>0 since G_k is strictly increasing (BL.1). Hence δ_N^(k+1)>δ_N^(k) for every α∈(0,1/17], N≥1, k≥N, and with BN.3 for every α∈(0,1).

BP.5 (derived from BG as stated): for α≤γ=log3/log5, δ_N^(n) increases strictly to 1.

## Why It Matters

Answers the open question left by DISC-0162/DISC-0163: the failure of monotone ω_k below a* (Kept Failure BO.1) does not propagate to the deficit. The monotonicity clause of Conjecture BL.6 (DISC-0159) is now a theorem for every N≥1 and every α∈(0,1).

## Derivation

GASKET.md Proof of BP (repository). Re-derived independently this slice: the single-crossing covariance step (if f−m changes sign once from − to + at y_c and g is increasing, ∫(f−m)(g−g(y_c))dμ≥0, strict unless degenerate) is the standard argument; the head identity, discriminant −39, the regrouping of P_α, 5+Y_α=1/(2α)−7/2 and the maximum of −α log(2α) at α=1/(2e) were checked in sympy.

## Assumptions

BN.1 (Stieltjes form, resting on Theorem AQ's identity, exact-checked by the repository only for n≤3); BK.1 and AQ (3) r_(k+1)≥r_k as stated (repository re-checked at five s values, k=0–3); BL.1 (G_k strictly increasing); BG for BP.5. d_k>0 (BK).

## New Results

δ_N^(n) strictly increasing in n for every N≥1 and every α∈(0,1). Monotone ω_k is not needed; only one crossing of its mean.

## Prior Art

Chebyshev's covariance inequality and its single-crossing generalisation (as used in stochastic-ordering arguments, e.g. Karlin's variation-diminishing / single-crossing lemmas) are textbook. Constants not searched.

## Novelty Analysis

Method KNOWN. The application to this gasket deficit is the repository's own; novelty of the statement UNRESOLVED. No world-first claim.

## Falsification Attempts

(1) Repository witness EXIT 0 in 29.8 s. (2) Independent sympy: head identity, discriminant, P_α regrouping, 5+Y_α identity: PASS. (3) Grid of 10,000 α∈(0,1/17]: max of (8/5)((5+Y_α)/5)^α/(3·5^−α)=0.586<1: PASS. (4) Own ω_k from AQ's recursion (no repository imports) at α=0.001, 0.01, 0.0167, k=3, 5: head max 1.5441, 1.5576, 1.5690 below ρ^−1=2.9952, 2.9521, 2.9204, and ω_k increasing on a grid of [Y_α,10.75 Y_α]: PASS, consistent with the repository floats. (5) Erratum found: GASKET.md says "e^(1/(2e))≤1.201943 is an arb enclosure", but e^(1/(2e))=1.2019433685…, so the printed bound is a round-down of the arb upper end (the script prints float(ub.upper()) with six decimals). The script's actual test ub.upper()<15/8 is unaffected and the theorem stands. 13/13 archive checks PASS.

## Experimental Validation

Repository witness /workspace/scratch-ifi/repo_theorem_BP.log (EXIT 0, 29.8 s). Archive check /workspace/scratch-ifi/indep_theorem_BP.py, log indep_theorem_BP.log.

## Mathematical Status

Theorem (mathematical sense).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0161 → DISC-0164 (mathematical: BN.2 majorant reused for every α≥0; BN.3 covers α>1/17). DISC-0163 → DISC-0164 (mathematical: the weight failure does not propagate to the deficit). DISC-0164 → DISC-0159 (mathematical: monotonicity clause widened to every α∈(0,1)).

## Open Questions

Rates of 1−δ_N^(n) below γ (floats suggest ratio → ρ≈0.3387); closed form for a*; existence and N-independence of C_δ (DISC-0159 limit clause); a certificate uniform in α.

## Next Experiments

Prove the ρ^n rate of 1−δ_N^(n) for α≤γ; extend the floats to N≥3 at α≤0.01.

## Reproduction Instructions

git -C informational-flux-identity checkout 4ee50b22193b5b24b0677a30e83403957f053f5b; python3 scripts/gasket_fractional_deficit_small_alpha.py (≈30 s; sympy, mpmath, python-flint). Archive: python3 /workspace/scratch-ifi/indep_theorem_BP.py.

## Evidence Log

- 2026-10-23 ~11:55am EDT. Indexed; repo witness EXIT 0; independent checks 13/13 PASS; erratum on the printed e^(1/(2e)) bound recorded.

## Change History

- 2026-10-23. Initial archive entry.
