# Discovery: Kept Failure AT.1, the slope at log3/log5 is not a pure-power constant

## Discovery ID

DISC-0114

## Status

REJECTED (the hypothesis r_∞(s)∼C s^(γ−1) with one constant C, so that c_R(γ)=(2 sin πγ/π)ln5·C). The rejection itself is a computer-assisted negative result in the repository. Not thrust.

## Date Discovered

2026-10-22 (America/New_York), corpus-discovery slice ~6:01am EDT.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, commit 68af4dd0c3989732a1b8b8ea0275948b7c33051a (2026-10-22 05:35:48 −0400). Paths: GASKET.md "Theorem AT", "KEPT FAILURE AT.1", "CONJECTURE AT.2"; CLAIM_STATUS.md row "Certified refinement-rate constants c_R, c_S of Theorem AR — VERIFIED (Theorem AT, Kept Failure AT.1)"; scripts/gasket_fractional_rate_constants.py (new, 410 lines); scripts/cli.py; README.md.

## Original Evidence

GASKET.md "KEPT FAILURE AT.1": with g(s)=s^(1−γ)r_∞(s), the fixed point r_∞=Φ_s(r_∞∘p) and 5^γ=3 give log(g(y)/g(p(y)))∈[−(1−γ)y/5, 1.82y^0.65] for y≤1e−3; Θ=lim g∘q^k exists, Θ∘q=Θ; certified Θ at s=5^(−40)5^(j/8), j=0..7, ≈0.600954332 … 0.600961578, enclosures separated by >1.465e−5.

## Discovery

s^(1−γ)r_∞(s) has no limit at 0; it is asymptotically log-periodic (period 1 in log_5 s) with relative amplitude ≈2.4e−5. No single power-law constant exists.

## Why It Matters

Rules out the simplest closed form for the critical slope c_R(γ) and identifies the correct object (the periodic function Θ), which feeds DISC-0115.

## Derivation

As in the repository; log-periodic oscillation of this type is the generic Koenigs/Poincaré-function behaviour for self-similar fractal spectra, so the failure is expected rather than surprising.

## Assumptions

Theorem AQ (4) enclosures of r_∞ (widths <1e−18) and the small-y remainder lemma (ratio 1.7896≤1.82, in-script).

## New Results

None beyond the rejection.

## Prior Art

Log-periodic oscillations in heat-kernel and spectral asymptotics on the Sierpinski gasket are classical (Kigami–Lapidus; Fukushima–Shima; Derfel–Grabner–Vogl). The specific function g is repository-defined.

## Novelty Analysis

Expected behaviour (KNOWN phenomenon) applied to a repository-defined quantity; not a novelty claim.

## Falsification Attempts

Archive check (C) in /workspace/scratch-ifi/indep_theorem_AT.py: own 40-digit g(s)=s^(1−γ)r_90(s) reproduces the 8 stated Θ values to 2e−9 with spread 1.465e−5, and g(5^(−30))≈g(5^(−40)) to 1e−12 (period confirmed). The rejection stands.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Counterexample (computer-assisted) to a pure-power hypothesis.

## Patent Relevance

None.

## Related Discoveries

- DISC-0113 → DISC-0114 (mathematical). DISC-0114 → DISC-0115 (mathematical; Θ is the object of AT.2). Sits beside DISC-0112 (failed hypothesis; shortcuts around certificates).

## Open Questions

Fourier coefficients of Θ; closed form of ⟨Θ⟩.

## Next Experiments

Certified Fourier expansion of Θ.

## Reproduction Instructions

`git -C informational-flux-identity checkout 68af4dd0c3989732a1b8b8ea0275948b7c33051a && python3 scripts/gasket_fractional_rate_constants.py` (~2.5 min, EXIT 0, 22 PASS). Archive: `python3 /workspace/scratch-ifi/indep_theorem_AT.py` (~82 s, EXIT 0, 19 PASS; mpmath float, no repo import).

## Evidence Log

- 2026-10-22. Repo witness and archive indep both PASS (logs as in DISC-0113).

## Change History

- 2026-10-22. Initial archive entry.
- 2026-10-23 ~5:01pm EDT. Re-confirmed by IFI Kept Failure BT.5 at 48a561c16bce15b0a0992015fa063d5311ebd5d5: F=u^(1−γ)Q_∞ is not constant (certified max F−min F≥1.465480e−5), the same hypothesis in Theorem BS's Q_∞ form; indexed under DISC-0170, no new ID; status stays REJECTED.
