# Discovery: Conjecture CA.6, the atoms of ν are exactly Λ_O and ν is pure point (ν(−Z)=0)

## Discovery ID

DISC-0184

## Status

SPLIT (2026-10-29 ~10:00am EDT). Part (i) restricted to (0,∞)∖(−Z), "every atom off −Z lies in Λ_O", is THEOREM via Theorem CB.4 (DISC-0185, commit 0d9944c015fb1ab192f9abe98096dfa8e1060b2c). Part (i) on −Z and part (ii) ν(−Z)=0 remain CONJECTURE. Was CONJECTURE 2026-10-29 7:59am to 10:00am EDT (original text preserved below). Prior-art lead may decide (ii) (Teplyaev 1998), identification not verified.

## Date Discovered

2026-10-29 (America/New_York), ~7:59am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 0d83dde51ff38c5ec4bf8f0e8f2a854e2e033b71.

## Original Evidence

GASKET.md Conjecture CA.6 (line 3260); open list (line 3265); commit message observation: BZ's atoms by depth k are 1,0,1,3,5,10,20,39,72,94,53,10,2,1 for k=0..13.

## Discovery

Two statements: (i) every atom of ν lies in Λ_O (converse of CA.2); (ii) ν(−Z)=0, so ν is pure point. Evidence: all 311 certified atoms lie in Λ_O (CA.4); BZ's uncaptured mass δ≤4.03e−5.

## Why It Matters

If true, limsup ρ_k=1 exactly (DISC-0175/DISC-0180), and the spectral measure is fully described by one backward orbit.

## Assumptions

Those of DISC-0182.

## Falsification Attempts

None decisive. The depth counts rising to 94 at k=9 and then falling look like grid resolution (the repository says so), not a finite atom set: CA.3 already proves infinitely many atoms. No counterexample found in the 311 certified atoms.

## Prior Art

Teplyaev 1998 (pure point spectrum, Neumann infinite gasket) and his later remark on singular continuous parts on the Julia-set preimage in other infinite-gasket settings; which applies depends on matching the corner vector and boundary condition. See DISC-0180, DISC-0182.

## Mathematical Status

Conjecture.

## Patent Relevance

None.

## Related Discoveries

DISC-0182, DISC-0183, DISC-0180, DISC-0175.

## Open Questions

As stated. Also whether even-order critical points of ψ in Z are limits of atoms.

## Next Experiments

Literature identification (Next Experiments of DISC-0182). Numerically: lower δ with a finer scan seeded from Λ_O directly (enumerate p^−k(−3) and solve ψ(−λ)=w), which would test (ii) much more cheaply than the blind 128000-cell scan.

## Reproduction Instructions

As DISC-0182.

## Evidence Log

- 2026-10-29 ~7:59am EDT. Indexed as the repository's own conjecture.
- 2026-10-29 ~10:00am EDT. informational-flux-identity 0d9944c015fb1ab192f9abe98096dfa8e1060b2c (Theorem CB) proves (i) off −Z: f is an explicit product whose only zeros off Z are on Λ_O. Repo witness EXIT 0; independent archive check PASS (see DISC-0185).

## Change History

- 2026-10-29. Initial archive entry.
- 2026-10-29 ~10:00am EDT. STATUS CHANGE CONJECTURE → SPLIT (off −Z part THEOREM via DISC-0185; −Z part and pure point stay CONJECTURE). Earlier text of Status was: "CONJECTURE (the repository's own, explicitly \"not claimed\"). Prior-art lead may decide part of it (Teplyaev 1998), identification not verified."
