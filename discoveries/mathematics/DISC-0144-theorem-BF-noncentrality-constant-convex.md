# Discovery: Theorem BF, smooth representation and certified strict convexity of the 3^−n constant c(α)

## Discovery ID

DISC-0144

## Status

THEOREM in the mathematical sense only (computer-assisted interval certificate in the repository, rerun here). Method KNOWN (exponential-family quotient representation and outward-rounded interval quadrature); the constant c'(0^+) and the sandwich constants: novelty UNRESOLVED (not searched). Not thrust.

## Date Discovered

2026-10-22 (America/New_York), ~8:00pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit b090826f15adc93d8ed6cbf352346dabb31ea136 (committed 2026-10-22 19:11:20 −0400). Files: scripts/mesh_noncentrality_convex.py (new, 299 lines), README.md "Theorem BF", CLAIM_STATUS.md (Conjecture BE.2 row), GASKET.md (Stage 2 item), scripts/cli.py, tests/test_cli.py.

## Original Evidence

Commit message and script docstring: with u = log τ, ε = 1 − α, P = (T − 2)𝒴 and any shift v = u − s0, c(1 − ε) − 2 = F(ε) = ε N/(1/3 + ε G), N = ∫ e^(εv) P dv, G = ∫ e^(εv)(𝒴 − (1/3)1[v<0]) dv. N and G are smooth on a neighbourhood of [0,1], so c extends C^2 to [0,1] with c''(α) = F''(1 − ε). The mpmath.iv certificate on 40 ε-intervals (14025 cells on u ∈ [−20, 8.05], T_60/𝒴_60 with BD.4's tail factors) gives c'' ≥ 0.52046 on [0,1].

## Discovery

(1) Quotient representation of c(α) − 2 valid for every shift. (2) c is C^2 on [0,1] and strictly convex on (0,1). (3) Certified c'(0^+) ∈ [−4.341285, −4.227515]. (4) Sandwich: max(2 + 2.70632481(1−α), 5.48553067 − 4.341285α) < c(α) < 2 + 3.50249013(1−α) on (0,1), sharpening BD.3's c ≤ 2 + B_α. Identities c' = −Cov(T, u), c'' = κ(T, u, u) (third joint cumulant) under ν_α ∝ τ^−α 𝒴 dτ do not fix the sign; the repository states this is a certificate, not a structural argument.

## Why It Matters

Completes the shape of α ↦ c(α) (decreasing by DISC-0141, convex here) between the certified endpoints, and gives explicit two-sided linear bounds usable without recomputing T and 𝒴.

## Derivation

Repository's: pull the 1/(3ε) contribution of the 𝒴 ≈ 1/3 head out of the denominator moment so that numerator and denominator are entire in ε; quotient rule gives F'' = (Φ'' − 2F'h' − Fh'')/h with Φ = εN, h = 1/3 + εG; outward interval enclosures of N, G and their ε-derivatives on cells (T increasing, 𝒴 decreasing hulls, exact head integrals ∫|v|^k e^v, polynomial tail from BD) bound F'' below on each ε-interval. Convexity plus the endpoint data (3S = F'(0) from BE.3, c_0 = 2 + F(1) from BE.4, certified F'(1)) gives the tangent/chord sandwich.

## Assumptions

Assumption BA / BC of the IFI README (frozen 0.45 gasket mesh, notation of Theorems BB–BE); correctness of mpmath.iv outward rounding; BD.4 tail factors and BE.3 head bound |𝒴 − 1/3| ≤ (e^0.1 + 0.3)τ/9 for τ ≤ 1.

## New Results

Strict convexity of c (proves Conjecture BE.2, DISC-0143). Certified c'(0^+) window of width < 0.12. Linear sandwich bounds above.

## Prior Art

Representation of tilted (Esscher / exponential-family) means as moment quotients and their derivatives as cumulants is classical; rigorous interval quadrature is standard computer-assisted-proof practice. The specific function c(α) is internal to the corpus; no literature search on its constants.

## Novelty Analysis

Method KNOWN. Whether the constants (c'(0^+), the sandwich) are new: UNRESOLVED, but they are defined only within this repository's construction, so external prior art is unlikely to address them directly.

## Falsification Attempts

- Repo witness rerun: `python3 scripts/mesh_noncentrality_convex.py` EXIT 0, 11 ok / 0 FAIL, about 100 s; smallest certified lower bound 0.52046 on ε ∈ [39/40, 1] (α ∈ [0, 0.025]); point enclosures F'(0) ∈ [2.702670, 2.713194], c_0 ∈ [5.472917, 5.515498], F'(1) ∈ [4.227516, 4.341284] (the commit message's window is outward-rounded by 1e−6; consistent).
- Archive /workspace/scratch-ifi/indep_theorem_BF.py (own Schur-gluing resolvent recursion from the BE archive, no IFI code imported, 60 digits): n=20 vs n=24 agree to 8.7e−9 on 41 α; all 38 centred second differences of c on α = k/40 lie in [1.5416, 1.5934] (positive, above 0.52046); c'(0^+) one-sided estimate −4.284122 inside the certified window; sandwich holds at 40 grid α with min margin 9.0e−5; c(0) = 5.494003464 inside BE's bracket. 7/7 PASS.
- Kept archive failures: run1 (script bug, missing helper, no result) and run2 (30-digit precision: the n=24 Schur recursion at s ~ 5^−24 loses all digits, giving nonsense c ~ 6e4). Both are archive errors, not repository errors; logs kept as indep_theorem_BF.run1.log and .run2.log.
- Weak point: the gap between the certified floor 0.52046 and the float values ~1.54 shows the enclosures are wide near α → 0; the theorem still only needs positivity.

## Experimental Validation

Computational only. No physical claim; not thrust.

## Mathematical Status

Theorem (computer-assisted proof).

## Patent Relevance

None.

## Related Discoveries

- DISC-0141 → DISC-0144 (mathematical): uses BE.3's 3S and BE.4's c_0.
- DISC-0138 → DISC-0144 (mathematical): uses BD.4's scaling limits and tails.
- DISC-0144 → DISC-0143 (mathematical): proves Conjecture BE.2 (status CONJECTURE → THEOREM).
- DISC-0144 → DISC-0145 (mathematical): Conjecture BF.2.

## Open Questions

A structural (non-certificate) reason for κ(T, u, u) > 0; closed forms for T, 𝒴, c, S, c_0, c'(0^+).

## Next Experiments

Tighten the enclosure near α → 0 (finer ε-intervals) to decide BF.2; look for a total-positivity / log-concavity property of T under the tilt family that implies a positive third cumulant.

## Reproduction Instructions

`git clone https://github.com/beyond-repair/informational-flux-identity && git checkout b090826f15adc93d8ed6cbf352346dabb31ea136 && python3 scripts/mesh_noncentrality_convex.py` (expects EXIT 0). Archive: `cd /workspace/scratch-ifi && python3 indep_theorem_BF.py 60` (needs sg_indep_common.py; use 60 digits, not 30).

## Evidence Log

- 2026-10-22 ~8:15pm EDT. Repo witness EXIT 0 (log /workspace/scratch-ifi/repo_theorem_BF.log); archive 7/7 PASS (/workspace/scratch-ifi/indep_theorem_BF.log).

## Change History

- 2026-10-22. Initial archive entry.
