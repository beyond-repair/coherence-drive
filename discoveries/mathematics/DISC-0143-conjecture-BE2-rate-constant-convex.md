# Discovery: Conjecture BE.2, the 3^−n constant c(α) is convex on (0,1)

## Discovery ID

DISC-0143

## Status

THEOREM in the mathematical sense only (proved by IFI Theorem BF at b090826f15adc93d8ed6cbf352346dabb31ea136; interval certificate, see DISC-0144). Not thrust.

Status history: CONJECTURE 2026-10-22 ~7:15pm EDT (repository's own Conjecture BE.2, float secants only) → THEOREM 2026-10-22 ~8:15pm EDT via DISC-0144. The original CONJECTURE text below is kept as recorded.

## Date Discovered

2026-10-22 (America/New_York), ~7:15pm EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 3b3ec0fef920f85fa1098074e22ee3bdafe73a26, README.md "CONJECTURE BE.2", CLAIM_STATUS.md Theorem BE row ("Convexity of c (Conjecture BE.2, floats only) and closed forms OPEN").

## Original Evidence

README: secant slopes of 3^20 d_20(α) over α=0.1, 0.25, 0.45, 0.65, 0.8, 0.95 are −4.0095, −3.7321, −3.4136, −3.1361, −2.8983 (increasing), and the slope at 1 is −3S≈−2.708. No closed form for T, 𝒴, c, S or c_0.

## Discovery

Convexity of α↦c(α).

## Why It Matters

Would complete the shape of c between the certified endpoints c_0 and 2.

## Derivation

None (conjecture).

## Assumptions

As DISC-0141.

## New Results

None proved.

## Prior Art

Not searched.

## Novelty Analysis

UNRESOLVED.

## Falsification Attempts

Archive floats (own Schur recursion, n=24, 12-point grid α=0..0.99): secant slopes −4.26851, −4.22951, −4.16692, −4.00953, −3.73205, −3.41362, −3.13606, −2.93972, −2.82311, −2.76139, −2.73066, increasing (consistent with convexity), and (c−2)/(1−α) decreasing to 3S. The repository's last float secant −2.8983 (0.8→0.95) is −2.90085 in the archive (repository float d_n(0.95) is off by ~1e−5 to 2e−4 relative; see DISC-0141); the ordering of secants is unaffected. No counterexample; floats only.

## Experimental Validation

Floats only.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

- DISC-0141 → DISC-0143 (mathematical).

## Open Questions

Proof of convexity; closed forms.

## Next Experiments

Interval-certified second differences of c on a grid; a log-convexity argument for the tilt family.

## Reproduction Instructions

As DISC-0141.

## Evidence Log

- 2026-10-22 ~7:15pm EDT. Recorded from IFI 3b3ec0fef920f85fa1098074e22ee3bdafe73a26; archive floats as above.

## Change History

- 2026-10-22 ~8:15pm EDT. Status CONJECTURE → THEOREM. IFI commit b090826f15adc93d8ed6cbf352346dabb31ea136 (scripts/mesh_noncentrality_convex.py, README Theorem BF, CLAIM_STATUS.md Conjecture BE.2 row) certifies c''(α) ≥ 0.52046 on all of [0,1] with mpmath.iv on 40 closed ε-intervals, so c is strictly convex on (0,1). Repo witness EXIT 0 (11 ok, 0 FAIL). Archive /workspace/scratch-ifi/indep_theorem_BF.py (own Schur recursion, no IFI code) 7/7 PASS: all 38 second differences of 3^24 d_24 on α = k/40 lie in [1.5416, 1.5934], above the certified floor. The proof is a computer-assisted certificate, not a structural argument (the repository says so). See DISC-0144.

- 2026-10-22. Initial archive entry.
