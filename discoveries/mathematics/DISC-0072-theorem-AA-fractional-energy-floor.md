# Discovery: Uniform fractional energy floor below α=1/2 on the gasket (Theorem AA)

## Discovery ID

DISC-0072

## Status

THEOREM

## Date Discovered

2026-10-15 (America/New_York). Archive pass after DISC-0070 / DISC-0071.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit e4be06f8fb772982dd9855fac6d9d5c2660eb9a7. Paths: GASKET.md "Theorem AA. Below α=1/2 the fractional energy has a uniform floor" (Assumption + CITED Löwner–Heinz, Theorem AA, Proof, Witness, Kept Failure AA.1, NOT THIS); scripts/gasket_fractional_energy_floor.py; CLAIM_STATUS.md (fractional energy Q_α / ‖F_frac‖ for α<1/2 VERIFIED; α=0.45 OPEN row updated that energy-collapse route is closed); README.md gasket summary pointing at Theorem AA.

## Original Evidence

Complete proof in GASKET.md. For every α∈(0,1/2) and every level n≥1,
(9/4)/C(α) ≤ Q_α(u_n) ≤ (7/6) 8^α, with C(α)=4^{-α}(8+(4/π)B(1/2−α,3/2)),
and therefore (9√21)/(28 C(α)) ≤ ‖F_frac(n,α)‖ ≤ (√21/6) 8^α via the Theorem K pairing.
At α=0.45: C≈17.532293, so Q≥0.128335 and ‖F_frac‖≥0.084015 at every level (ceilings 2.973975 and 1.946953).

## Discovery

A uniform two-sided bound on the L^α-Dirichlet energy (and fractional-current audit) for every α below the path spectral threshold 1/2, obtained by Löwner–Heinz comparison to the a–b boundary path, Cauchy–Schwarz duality, the closed-form Neumann-path resistance R_α(m), and a Beta-function integral majorant. Closes the energy-collapse route left open by Theorem L at α=0.45.

## Why It Matters

It brackets Q_{0.45} and ‖F_frac‖ away from 0 and from +∞ at every finite level. Combinatorial ‖F(n,0.45)‖ (Conjecture J.1 / DISC-0034) stays OPEN. Not thrust.

## Derivation

Repository proof, checked in this archive:
1. Side a–b is a path P_m with m=2^n edges; M ⪯ L ⇒ M^α ⪯ L^α (Löwner–Heinz, imported).
2. Duality: (u_a−u_b)^2 ≤ Q_α(u)·R_α(m) with R_α(m)=v^T (P_m^α)^+ v and |u_a−u_b|=3/2.
3. Closed-form cosine eigenbasis for the Neumann path; Riemann-sum comparison to ∫_0^{π/2} (2sinθ)^{-2α} cos²θ dθ = 4^{-α}(1/2)B(1/2−α,3/2) when 2α<1 gives R_α(m)≤C(α).
4. Ceiling: competitor with value 1/6 off corners; Gershgorin λ_max(L)≤8 ⇒ Q_α(u_n)≤(7/6)8^α.
5. Pairing Q_α=(7/5)I_a^α and ‖F_frac‖=I_a^α √21/5 convert both bounds.

## Assumptions

Spectral calculus (GASKET item 4); corner data (1,−1/2,0); Löwner–Heinz for t↦t^α on [0,1]; Theorems J/K/L pairing algebra.

## New Results

Archive `/workspace/scratch-ifi/repo_theorem_AA.log` (repository witness EXIT:0, all checks passed) and `/workspace/scratch-ifi/indep_theorem_AA.py` / `indep_theorem_AA.log`: C(0.45)/floors/ceilings match GASKET to 1e−6; closed-form R vs dense (P^α)^+ max err 1.3e−11 through m=2^7; R(2^n)≤C(α) and monotone toward the Riemann limit through n=22 for α∈{0.10,0.25,0.45,0.49}; α=1/2 control log growth (~3.53 per 4 levels); live levels 1–5 Loewner–Heinz + path duality + floor/ceiling + ‖F_frac‖=Q√21/7; recorded Q_9/Q_10 inside the band; Beta pole at α→1/2− confirmed.

## Prior Art

Löwner–Heinz operator monotonicity; spectral calculus on finite graph Laplacians; Neumann-path eigenbasis; Beta-function integral for fractional path resistance. Theorems J/K/L (DISC-0032). Not searched further; no novelty claimed.

## Novelty Analysis

THEOREM in the mathematical sense only (complete proof in the repository, verified here). Not a novelty claim and not a Stage-1 / claim-level raise. Specific constants are for this repository's audit functional.

## Falsification Attempts

Reran the witness; independent rebuild matched records; control at α=1/2 shows the path route needs α<1/2. No discrepancy.

## Experimental Validation

None (pure mathematics / finite numerical witness).

## Mathematical Status

Proved in-repo; proofs and witness verified. Does not bound combinatorial ‖F‖ from below; window α∈[1/2, log3/log5] stays OPEN.

## Patent Relevance

None.

## Related Discoveries

- DISC-0032. Mathematical. Theorems J, K, L (energy controls the audit; collapse would force zero).
- DISC-0073. Failed hypothesis. Energy collapse at α=0.45 rejected.
- DISC-0034. Conjecture. Combinatorial α=0.45 limit still OPEN.
- DISC-0033. Failed hypotheses. Earlier shortcut laws for closing the limit.

## Open Questions

Combinatorial ‖F(n,0.45)‖ zero vs positive (OPEN). Fractional energy/current for α∈[1/2, log3/log5] OPEN.

## Next Experiments

None from the archive.

## Reproduction Instructions

`git checkout e4be06f8fb772982dd9855fac6d9d5c2660eb9a7 && PYTHONPATH=scripts python3 scripts/gasket_fractional_energy_floor.py`. Archive logs: `/workspace/scratch-ifi/repo_theorem_AA.log`, `/workspace/scratch-ifi/indep_theorem_AA.log`.

## Evidence Log

- 2026-10-15. Recorded from GASKET.md Theorem AA at e4be06f8fb772982dd9855fac6d9d5c2660eb9a7; repo witness EXIT:0; independent check ARCHIVE_INDEP_THEOREM_AA_PASS. Repository description still matches its claim fence.

## Change History

- 2026-10-15. Initial archive entry.
