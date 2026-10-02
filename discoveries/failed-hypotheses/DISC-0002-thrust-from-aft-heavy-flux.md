# Discovery: Thrust from aft-heavy flux

## Discovery ID

DISC-0002

## Status

REJECTED as a thrust claim.

## Date Discovered

2026-10-01. This is the date of the archive pass.

## Source Repositories

- beyond-repair/informational-flux-identity at HEAD ce070589ca257e9b5c8158403606ace5dd183aea.
- beyond-repair/coherence-drive at HEAD 095d29d1a107d719f8aed9f89834d917b119ca4c, file docs/SPECTRAL_ENDPOINT.md.
- beyond-repair/thrust-target-30 at HEAD 30d030aa36556e18403a961391e98b2d06e91c5a, file constants/target.json.
- beyond-repair/-ware-constant-derivation at HEAD 2fdc5f600a1ad9881e973e5fe2d32f25ae95efdd.
- beyond-repair/momentum-closure at HEAD 36949d00023eef7edabd875ca5836ad1ca39f312.
- beyond-repair/topological-pinch at HEAD 5a7f2d04256d7400ce84f56dbc452511250df968.

## Original Evidence

Theorem B in the flux README is a divergence-free witness whose right face holds 349/366 of the absolute boundary flux while the signed outward flux is 0. The README says localizing absolute stress on an aft face does not produce a net Delta F. It marks the thrust reading as failed.

The same README says that if the informational array is divergence-free, Delta F is 0 for any constant W and any constant chi_vac.

docs/SPECTRAL_ENDPOINT.md at the coherence-drive HEAD says the following are not consequences of the locked kernel K. The sentence in that file is: "W = 0.08, xi = 0.23, W_star = 1/(4 pi), the 92% pinch, galactic acceleration, W(x) as an operator, thrust, 30 uN/kW as physics, and Delta F = W chi_vac G." The same file says: "Momentum is undefined, not measured to be zero."

constants/target.json in thrust-target-30 has kind design_goal, value_uN_per_kW 30, and experimental_validation false.

The README in -ware-constant-derivation says the constant-W action is derived, local W(x) is open, and 0.08 is not derived.

momentum-closure says momentum for this K is undefined, not measured to be zero.

topological-pinch says 92% is a hypothesis, not a measured pinch.

## Discovery

Aft-heavy absolute flux is not a net force. The claim that this flux is thrust is rejected. W = 0.08, the 92% pinch, thrust, 30 uN/kW as physics, and Delta F = W chi_vac G are not consequences of the locked kernel K.

## Why It Matters

The rejected reading is the one that treats a large absolute share on one face as a net force. DISC-0001 shows that share can be 349/366 while the signed flux is 0. The spectral endpoint file says the thrust numbers are not consequences of K.

## Derivation

No thrust derivation is recorded, because the claim is rejected. The flux note is the one already in the README: a divergence-free informational array gives Delta F = 0 for any constant W and chi_vac.

## Assumptions

The rejection uses the finite-rectangle identity in DISC-0001 and the locked statement in docs/SPECTRAL_ENDPOINT.md. It does not assume a continuum stress tensor. It does not assume that momentum has been measured.

## New Results

None. No claim level is raised.

## Prior Art

The obstruction is the classical discrete divergence theorem already stated in the flux repository. This entry does not add an external citation.

## Novelty Analysis

There is no novelty claim. The relation to DISC-0001 is mathematical.

## Falsification Attempts

The aft-heavy witness itself is the falsification of the thrust reading. Signed fluxes (0, +11, -2, -9) sum to 0 while absolute fluxes (0, 349, 2, 15) total 366. The README calls the thrust reading failed. The spectral endpoint file denies that thrust follows from K.

## Experimental Validation

None. thrust-target-30 records experimental_validation false. The value 30 uN/kW is a design goal in constants/target.json, not a measured force.

## Mathematical Status

Rejected.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0001. Mathematical. Signed flux 0 kills the absolute-flux thrust reading.
- DISC-0003. Mathematical. The bound W < 1/6 does not select 0.08 or thrust.
- DISC-0004 stands beside this row. It is the same W family and is not a thrust input.
- DISC-0005. The spectrum locks are not a pinch of 0.92 and are not thrust.

## Open Questions

Whether any residual force remains after classical subtraction is open. Momentum for the locked K is undefined rather than measured zero. The existing ledger is coherence-drive/docs/SURVIVED_REJECTED_UNRESOLVED.md, which already lists genuine residual force after classical subtraction as unresolved. This archive does not resolve it.

## Next Experiments

Do not run a new thrust demonstration from this note. Any later question about residual force has to stay on that unresolved ledger item. This pass does not define that check and does not claim it was done.

## Reproduction Instructions

Read Theorem B in informational-flux-identity at ce070589ca257e9b5c8158403606ace5dd183aea. Read docs/SPECTRAL_ENDPOINT.md in coherence-drive at 095d29d1a107d719f8aed9f89834d917b119ca4c. Read constants/target.json in thrust-target-30 at 30d030aa36556e18403a961391e98b2d06e91c5a. Read the README statements cited above in -ware-constant-derivation at 2fdc5f600a1ad9881e973e5fe2d32f25ae95efdd, momentum-closure at 36949d00023eef7edabd875ca5836ad1ca39f312, and topological-pinch at 5a7f2d04256d7400ce84f56dbc452511250df968.

## Evidence Log

- 2026-10-01. Read informational-flux-identity README.md at ce070589ca257e9b5c8158403606ace5dd183aea.
- 2026-10-01. Read coherence-drive docs/SPECTRAL_ENDPOINT.md at 095d29d1a107d719f8aed9f89834d917b119ca4c. Blob SHA be85ceab6fa39cc359811b2a533f0588ed72792a. Quoted the "not consequences of K" sentence and the momentum sentence.
- 2026-10-01. Read coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at the same HEAD. Blob SHA 9bf3a9329ec9263abe2e739996e9b67519f61cd1. The unresolved list includes "Genuine residual force after classical subtraction".
- Provenance, not a physics result. GitHub descriptions fetched on 2026-10-01 still state the opposite and were not edited. coherence-drive: "Official master repository for the Coherence Drive propulsion system. Integrates all seven groundbreaking findings into a complete, physics-closed vacuum-coherent engine." -ware-constant-derivation: "Rigorous mathematical derivation of the Ware Constant W approximately 0.08 from the Coherence Drive thrust target and fractal LDOS asymmetry." momentum-closure: "Full momentum closure for the Coherence Drive using surface integral of the stress tensor + Poynting flux. Proves the Ware term supplies real net momentum flux." thrust-target-30: "The non-negotiable engineering target of 30 μN/kW that anchors the entire Coherence Drive derivation, including the Ware Constant and all scaling laws." topological-pinch: "The aft-face topological pinch — 92 % of the stress divergence is localized at fractal vertices. This is the physical mechanism that breaks symmetry and produces net thrust in the Coherence Drive." Those sentences disagree with the files named above. They are not measurements.

## Change History

- 2026-10-01. Initial archive entry. Descriptions were not edited. No existing file was changed.
