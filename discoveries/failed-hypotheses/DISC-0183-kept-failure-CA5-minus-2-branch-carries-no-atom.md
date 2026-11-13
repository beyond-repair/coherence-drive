# Discovery: Kept Failure CA.5, the −2 branch of p^−1(−6) does not seed atoms of ν

## Discovery ID

DISC-0183

## Status

REJECTED (the repository's own Kept Failure, certified witness).

## Date Discovered

2026-10-29 (America/New_York), ~7:59am EDT corpus slice.

## Source Repositories

beyond-repair/informational-flux-identity, main, commit 0d83dde51ff38c5ec4bf8f0e8f2a854e2e033b71.

## Original Evidence

GASKET.md Kept Failure CA.5 (line 3258), witness paragraph (line 3272), scripts/gasket_fractional_profile_atom_law.py.

## Discovery

Claim tested and rejected: "every λ with ψ(−5^k λ)∈p^−1(−6)={−2,−3} is an atom of ν". Witness: u=−2.242133185246453863226262… with ψ(u)=−2 has f(u)=1/Q_∞(u)∈[2.1979467595912, 2.1979467595913], so λ=2.2421331852464538… is not an atom. Reason: c and e have their poles at −2, so CA.1's induction cannot start there; two steps of the recursion give the regular form D(z)=(z+6)(z+3)D(p²z)/((z+5)(p(z)+2)(p(z)+5))−2z(z+4)/(p(z)+2) and D(−2)=D(6)/3−2.

## Why It Matters

It pins exactly where the atom law of DISC-0182 stops: only the −3 branch of the preimage of −6 seeds atoms. This matches the classical "forbidden value 2" of Sierpinski-gasket spectral decimation (x=−z; see DISC-0182 Prior Art).

## Derivation

Repository, line 3258. I re-derived the two-step regular form with sympy: c(z)(c(p(z))X−e(p(z)))−e(z) minus the printed form simplifies to 0, and at z=−2 it gives X/3−2 with X=D(p²(−2))=D(6). PASS.

## Assumptions

Those of DISC-0182.

## Falsification Attempts

Independent: /workspace/scratch-ifi/indep_theorem_CA.py solves ψ(u)=−2 from scratch (u=−2.242133185246453863226, all printed digits) and evaluates 1/Q_∞(u) by the finite-level route (no repository code): 2.19794675959126, inside the repository's interval. The rejection stands.

## Prior Art

Forbidden eigenvalue 2 in Fukushima–Shima spectral decimation (identification not verified).

## Mathematical Status

Certified counterexample (REJECTED claim).

## Patent Relevance

None.

## Related Discoveries

DISC-0182 (Theorem CA), DISC-0184 (Conjecture CA.6), DISC-0180.

## Open Questions

None beyond DISC-0184.

## Next Experiments

None needed.

## Reproduction Instructions

As DISC-0182.

## Evidence Log

- 2026-10-29 ~7:59am EDT. Indexed; independent reproduction of the witness PASS.

- 2026-10-29 ~10:00am EDT. Theorem CB.4 (DISC-0185, 0d9944c015fb1ab192f9abe98096dfa8e1060b2c) extends the rejection from the single witness to the whole −2 branch: no λ with ψ(−5^kλ)∈⋃p^−j(−2) is an atom. Witness value re-obtained from the product alone. Stays REJECTED.

## Change History

- 2026-10-29. Initial archive entry.
