# Discovery: Tested necks and geometric I select 0.08

## Discovery ID

DISC-0014

## Status

REJECTED as a universal 0.08 consequence and as a neck fixed point on the tested sequences.

## Date Discovered

2026-10-02. Archive pass for topological-pinch at the named evidence commit.

## Source Repositories

- beyond-repair/topological-pinch at commit 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3, branch main.
- Files: FALSIFICATION_2026-10-01_PINCH.md, STATUS_LOCK_2026-10-01.md, ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, CLAIM_STATUS.md.
- The addendum points at beyond-repair/scale-functional-I. This row classifies only sentences present in topological-pinch. It does not import an unreviewed proof from that other repository.

## Original Evidence

STATUS_LOCK_2026-10-01.md at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3 says: "0.08 is falsified as a universal consequence of the tested neck sequences. Spectral collapse of the Neumann dumbbell remains real. It does not select 0.08."

The same file says: "Correction: the gap ratio meets 0.08 near w ≈ 2.4 as a level set, R(w_*)=0.08, with R'(w_*) ≠ 0. Recording R'(w_*)=0 or dR/d ln w = 0 for that crossing is wrong."

It also says: "A topological mouth that universally generates a counter-pressure constant is unsupported. Near-zero Neumann splitting with bulk scale O(1) is a spectral fact, not an 8% law."

FALSIFICATION_2026-10-01_PINCH.md at the same commit says the gap ratio lambda_1/lambda_2 "crosses 0.08 between w=2 and w=3. That crossing is a level set. Change chamber size or neck length and it moves. It is not a zero of partial_{ln w}." It also says: "Spectral collapse occurs. It occurs on a fixed topology with Neumann conditions. It does not prove a topological mouth." Non-claims in that file include "Not a measurement of eta = 0.92" and "Not a universal informational counter-pressure constant."

ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md at the same commit says: "Does not modify the 2026-10-01 lock. The neck claim stays a hypothesis." It then says: "Declared geometric I = Perimeter / sqrt(Area) has no stationary point under neck widening on the tested dumbbells. Spectral collapse remains a Neumann fact. Neither fact selects 0.08." The addendum sets Status: Unverified and experimental_validation false.

CLAIM_STATUS.md at the same commit says a Neumann neck collapses lambda_1 as width drops, that this is spectral and not a topological mouth, and that it does not select 0.08. It says the gap ratio crosses 0.08 only as a geometry-dependent level set. Status remains unverified.

## Discovery

The testable claim after the DISC-0002 snapshot is not "92% produces thrust." It is whether the tested neck family, or the declared ratio I = Perimeter / sqrt(Area), selects 0.08 as a fixed point. The repository says no. The 0.08 crossing is a level set with nonzero derivative on the recorded correction. I has no stationary point under neck widening on the tested dumbbells. Neither fact selects 0.08. The broader neck claim is left a hypothesis. Spectral collapse on the tested Neumann dumbbell is recorded as real and is not promoted to a mouth or an 8% law.

## Why It Matters

A level-set crossing can be misread as a stationary law, and a collapsing Neumann eigenvalue can be misread as a topological derivation of 0.08. The lock and the addendum block both readings without claiming a general theorem.

## Derivation

No derivation of 0.08 is recorded. The falsification file says 0.08 was not an input. The addendum says it does not modify the 2026-10-01 lock. This row does not supply a proof that the repository does not contain.

## Assumptions

The rejection is limited to the tested neck sequences and tested dumbbells named in those files. It uses the in-file correction that the crossing is not a zero of the scale derivative. It does not treat "spectral collapse remains real" as a theorem about every neck.

## New Results

None. No claim level is raised. experimental_validation stays false, as each cited file states.

## Prior Art

The falsification file points at the canonical note in beyond-repair/-ware-constant-derivation. This entry does not add an external citation and does not treat that pointer as a proof stored here. DISC-0011 already rejects an M2 pin of 0.08 as a theorem from K. This row is a different test, on neck sequences, not that pin.

## Novelty Analysis

There is no novelty claim. Status is REJECTED for the universal-0.08 and fixed-point readings. The repository does not contain a proof or a prior-art comparison that would support THEOREM or PATENT CANDIDATE. The neck claim that the addendum still calls a hypothesis is not reclassified upward.

## Falsification Attempts

The 2026-10-01 falsification note and the derivative correction in the status lock are the in-file attack on a fixed point at 0.08. The 2026-10-02 addendum is the in-file attack on a stationary point of I under neck widening, limited to the tested dumbbells. Both deny selection of 0.08.

## Experimental Validation

None. FALSIFICATION_2026-10-01_PINCH.md, STATUS_LOCK_2026-10-01.md, and ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md each set experimental_validation false, thrust_validated false, and energy_extraction_validated false.

## Mathematical Status

Rejected as a universal consequence and as a recorded fixed point. Not a theorem. The addendum's own status word remains Unverified.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. W = 0.08 is not a consequence of locked K. This row does not reopen that claim.
- DISC-0011. Mathematical. A different 0.08 pin, in stress-tensor-modification, is already rejected as a theorem from K.
- DISC-0013. Historical. Same repository and same evidence commit. The neck test is not a measurement of eta = 0.92.

## Open Questions

The addendum says the neck claim stays a hypothesis. What that hypothesis means once 0.08 and the tested fixed points are removed is not settled here. This row does not define a replacement constant.

## Next Experiments

Do not record R'(w_*)=0 for the 0.08 crossing. Do not cite spectral collapse or I as a derivation of 0.08. Do not modify the 2026-10-01 lock from the addendum.

## Reproduction Instructions

Read FALSIFICATION_2026-10-01_PINCH.md, STATUS_LOCK_2026-10-01.md, ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, and the 2026-10-01 pinch-family paragraph in CLAIM_STATUS.md at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3.

## Evidence Log

- 2026-10-02. Read the files named above at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3.
- 2026-10-02. Commit 261d215da8a82fe517a19c04f373d920eef5dba7 records the pinch-family spectral test. Commit b327af986fafa44647bf88d82cb564a0a8c424b8 corrects the neck crossing to a level set whose derivative is not zero. Commit 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3 adds the scale-functional addendum. Quoted sentences are the text at that last commit.
- scale-functional-I was not opened. Classification uses the addendum sentences only.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
