# Discovery: Discrete flux identity

## Discovery ID

DISC-0001

## Status

KNOWN

## Date Discovered

2026-10-01. This is the date of the archive pass, not a claim that the identity was first found on that day.

## Source Repositories

beyond-repair/informational-flux-identity at HEAD ce070589ca257e9b5c8158403606ace5dd183aea.

## Original Evidence

The README at that commit states Theorem A. On a finite rectangle, the sum of the cell divergences equals the outward signed flux. The identity is algebraic. It does not depend on which face carries the largest absolute flux.

witness.json, produced by scripts/flux_identity.py, records the witness integers. Signed outward fluxes are left 0, right +11, bottom -2, and top -9. Those four numbers sum to 0. Absolute fluxes are left 0, right 349, bottom 2, and top 15. Those four numbers total 366. The right face is 349/366 of the absolute flux.

Adding 17 to one boundary entry makes the array no longer divergence-free. The same note records that the sum of the cell divergences is 17 and the signed flux is 17.

## Discovery

On a finite rectangle, summed cell divergence equals outward signed flux. A face can hold 349/366 of the absolute flux while the signed flux is 0. A +17 boundary source makes the divergence sum and the signed flux both equal 17. This is the discrete divergence theorem.

## Why It Matters

The identity separates absolute flux on one face from net signed flux. The thrust reading of an aft-heavy absolute flux does not follow from it. That reading is recorded as failed in the same README, and it is DISC-0002.

## Derivation

The README proof sums the horizontal face differences in x and the vertical face differences in y. Each interior face cancels. What remains is the outward signed flux. No new derivation is added here.

## Assumptions

The rectangle is finite and partitioned into unit cells. Face fluxes are ordinary numbers on that grid. No continuum measure is used. The README labels that setting as established for this identity.

## New Results

None. This archive only restates the identity already proved in that README.

## Prior Art

This is the classical discrete divergence theorem, written in the repository as Theorem A. No external paper is cited in this archive entry.

## Novelty Analysis

There is no novelty claim. The relation recorded here is mathematical.

## Falsification Attempts

The README reports a failed first attempt at a one-dimensional corollary and says the script rejected it. That failed attempt is not part of Theorem A. The witness script exits nonzero if the quoted integers move.

## Experimental Validation

None. The witness is an integer check on an explicit array. The README sets experimental_validation, thrust_validated, and energy_extraction_validated to false.

## Mathematical Status

Known identity.

## Patent Relevance

None established.

## Related Discoveries

DISC-0002. The edge is mathematical. Signed flux 0 kills the absolute-flux thrust reading.

## Open Questions

The identity does not decide whether any later device array has a nonzero divergence sum. The README leaves that question open and points it at the coherence-drive ledger. This archive does not answer it.

## Next Experiments

Re-run python3 scripts/flux_identity.py at the named commit. Do not treat a large absolute face share as a net force.

## Reproduction Instructions

Check out beyond-repair/informational-flux-identity at ce070589ca257e9b5c8158403606ace5dd183aea. Read README.md Theorem A and Theorem B. Run python3 scripts/flux_identity.py. The script writes witness.json and exits nonzero if the integers quoted above move.

## Evidence Log

- 2026-10-01. Read README.md at ce070589ca257e9b5c8158403606ace5dd183aea. Blob SHA of that file was 2bbfc26f6cde3fa9e96bd9f741ce40609a38f8b2. Quoted the theorem statement and the witness integers from that file.
- The parent coherence-drive commit for this archive is 095d29d1a107d719f8aed9f89834d917b119ca4c.

## Change History

- 2026-10-01. Initial archive entry. No existing file was changed.
