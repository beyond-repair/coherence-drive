# Discovery: Theorem BO, exact exponent threshold a* for the monotone one-level weight ω_k

## Discovery ID

DISC-0162

## Status

THEOREM in the mathematical sense only (repository proof; BO.1–BO.3 analytic, BO.4–BO.5 computer-assisted with exact rationals, sympy root isolation and Sturm sequences). Method KNOWN; the constant a* and its brackets novelty UNRESOLVED. Not thrust.

## Date Discovered

2026-10-23 (America/New_York), ~10:01am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 18bb38dcc3688510f2ef44134db70aa8f47fb530.

## Original Evidence

GASKET.md Theorem BO (BO.1–BO.6) and Kept Failure BO.1, CLAIM_STATUS.md new row, README.md OPEN bullet, scripts/gasket_fractional_weight_threshold.py (new, 251 lines), scripts/cli.py, tests/test_cli.py, all at 18bb38dcc3688510f2ef44134db70aa8f47fb530. Builds on Theorem BN at 335860e44ebff5d3ad55498d4efc9f96c5ff8d12 (DISC-0161).

## Discovery

BO.1: (log ω_k)'=(α−Φ_k)/(5+y) with Φ_k=(5+y)d_k'/d_k, so ω_k=(1+y/5)^α/d_k is strictly increasing in y iff α≥a_k*=sup_y Φ_k (the condition is linear in α).

BO.2: from BN.1's unit-mass Stieltjes form with moments m_j=(1/2)vᵀL_k^j v, exact geometric remainders of 1/(s+λ) and 1/(s+λ)² (J≤8) give two-sided bounds on r_k and −r_k' (odd J upper, even J lower); spectrum in [0,8] (Gershgorin) with m_1≥2 gives k-uniform chord bounds r_k≤1/s−2/(s(s+8)), −r_k'≤r_k/s−2/(s(s+8)²).

BO.3: m_j(k)=m_j(k+1) for j<2^k (closed walks of length j from a corner stay in the corner subcell), so m_0..m_7=1,2,6,22,92,418,1994,9780 at every k≥3.

BO.4–BO.5: at A_hi=0.0167788801732, chord bounds off (12.5408,14.7913), J=7/8 moment bounds on [12,15] for every k≥3, and exact rational d_k for k=0,1,2 give ω_k strictly increasing at every level k≥0 for every α≥A_hi. Brackets: a_0*∈[0.0155298932937,0.0155298932938], a_1*∈[0.0167694660209,0.0167694660210], a_2*∈[0.0167788799215,0.0167788799216], a_k*∈[A_lo,A_hi] for k≥3, A_lo=0.016778880172852.

BO.6 (derived): BN.3's Chebyshev monotonicity δ_N^(k+1)>δ_N^(k) holds for every N≥1 and α∈[A_hi,1).

## Why It Matters

BN.2's threshold 1/17≈0.0588 was a method limit. BO lowers it to the exact threshold a*≈0.01677888017 (to within 3.5e−13) and, with Kept Failure BO.1 (DISC-0163), shows the monotone-weight statement really does fail just below a* at every level k≥3. This answers DISC-0161's open question "monotone ω_k for α<1/17".

## Derivation

GASKET.md Proof of BO (repository). Re-derived independently this slice: BO.1 is the logarithmic derivative of ω_k; the s→∞ series of AQ's recursion reproduces the moment lists for k=1, 2, 3; a graph-Laplacian construction of the level-k gasket reproduces m_0..m_7 at k=3, 4, 5 from a corner (no repository imports).

## Assumptions

BN.1 (Stieltjes form of r_k, which rests on Theorem AQ's identity r_k(s)=(1/2)vᵀ(L_k+s)^−1 v, exact-checked by the repository only for n≤3); d_k>0 (BK); Gershgorin spectrum bound; correctness of sympy root isolation/Sturm in the script (re-run, not re-implemented). BO.6 inherits BN.3's assumptions.

## New Results

ω_k is monotone at every level iff α≥a* (with a*=lim a_k*, a_k* constant to 3.5e−13 for k≥3). δ_N^(n) increasing in n is now a theorem for every N≥1 and α≥A_hi (was α≥1/17). DISC-0159's monotonicity clause widens to α≥A_hi. Below a* the Chebyshev route is closed; whether δ_N^(n) still increases there is open (the repository's float run at α=0.01 did not finish).

## Prior Art

Moment/Taylor bounds for Stieltjes functions (Padé-type two-sided bounds, Stieltjes moment problem) and Gershgorin are textbook; locality of closed-walk counts on self-similar graphs is standard. Constant a* not searched.

## Novelty Analysis

Method KNOWN. The threshold a*≈0.0167788801729 and its brackets are the repository's own; novelty UNRESOLVED. No closed form for a* is known (repository says OPEN). No world-first claim.

## Falsification Attempts

(1) Independent mpmath (50 digits) sup Φ_k for k=0..7 from AQ's recursion and BN's B, C, p: 0.0155298932937551, 0.0167694660209228, 0.0167788799215301, and 0.0167788801728761 for k=3..7 at y*=13.778505644; all inside the stated brackets. (2) Moments from the recursion's s→∞ series (k=0..3) and from explicit gasket graph Laplacians (k=3, 4, 5): match BO.3 exactly. (3) Chord bound r_k≤1/s−2/(s(s+8)) at 121 log-spaced s∈[1e−6,1e6], k=0..7: 0 violations. (4) Exact sympy at A_hi for k=0, 1, 2: numerator of αd_k−(5+y)d_k' (degrees 5, 9, 17) has no positive real root and is positive: PASS. (5) Repository witness EXIT 0 in 12 s. Archive script 16/16 PASS. No contradiction found.

## Experimental Validation

Repository witness /workspace/scratch-ifi/repo_theorem_BO.log (EXIT 0, 12.1 s). Archive check /workspace/scratch-ifi/indep_theorem_BO.py, log indep_theorem_BO.log (16/16 PASS, 8 s).

## Mathematical Status

Theorem (mathematical sense; computer-assisted with exact rational arithmetic).

## Patent Relevance

None. Pure mathematics on a graph; not a mechanism. Not thrust.

## Related Discoveries

DISC-0161 → DISC-0162 (mathematical: BN.1 Stieltjes form and BN.2 identity; 1/17 lowered to a*). DISC-0162 → DISC-0163 (mathematical: matching failure below a*). DISC-0162 → DISC-0159 (mathematical: monotonicity clause widened to α≥A_hi).

## Open Questions

Closed form for a*; whether δ_N^(n) is still increasing in n for α<a*; whether a_k* is exactly constant for k≥3 or only to 3.5e−13; a separate lemma for AQ's identity at every level.

## Next Experiments

Finish the float δ_N^(n) run at α=0.01 (repository reports it did not finish); tighten the k≥3 bracket with J>8 moments (m_j stable for j<2^k).

## Reproduction Instructions

git -C informational-flux-identity checkout 18bb38dcc3688510f2ef44134db70aa8f47fb530; python3 scripts/gasket_fractional_weight_threshold.py (≈12 s, needs sympy, mpmath). Archive: python3 /workspace/scratch-ifi/indep_theorem_BO.py.

## Evidence Log

- 2026-10-23 ~10:01am EDT. Indexed; repo witness EXIT 0; independent checks 16/16 PASS.

## Change History

- 2026-10-23. Initial archive entry.
