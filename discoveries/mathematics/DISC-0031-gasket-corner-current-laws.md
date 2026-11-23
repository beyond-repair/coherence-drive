# Discovery: Gasket corner-current laws (cut identity, 3/5 harmonic law, fractional neutrality, 12/5 geometric scaling)

## Discovery ID

DISC-0031

## Status

DERIVATIVE

## Date Discovered

2026-10-08 (America/New_York). First archive index of GASKET.md.

## Source Repositories

beyond-repair/informational-flux-identity, branch main, HEAD 81ab02b501aef7df2f5478f55d67d50f93595d56. Path: GASKET.md Theorems F, G, H, I and "Explicit dipole". Evidence commits: 7041a0552183f70fc0c35bbb333e7a550120cdc1 (Theorem G), 3f5c655092b39f5a4a970cb98a5321f05ec00839 (Theorem H), a5094e16f32a857e00334eaebb02da35b200b642 (Theorem I). Scripts: scripts/gasket_corner_current.py, scripts/gasket_fractional_currents.py, scripts/gasket_geometric_currents.py. CLAIM_STATUS.md row "Geometric 1/d^2 harmonic audit norm … VERIFIED diverge".

## Original Evidence

On the combinatorial Sierpinski gasket graph (N(n) = (3^{n+1}+3)/2), the corner currents I_c = (Lu)_c and the audit vector F = Σ_c I_c (P_c − P̄) used by sierpinski-geometry-045's net_flux.

## Discovery

- Theorem F: Σ_{i∈S}(Lu)_i equals the edge cut flux; corner currents of an interior-harmonic u sum to 0.
- Theorem G: harmonic corner currents scale by exactly 3/5 per refinement; for data (1, −1/2, 0), ‖F(n)‖ = (3/5)^n √21/2.
- Theorem H: for L^α (spectral calculus), L^α-Dirichlet corner currents still sum to 0; by S_3/Schur both fractional and combinatorial current triples lie on (1, −4/5, −1/5). Kept Failure H.1: the 3/5 law does not carry over.
- Theorem I: with w = 1/d² on the finest-edge build, L_geom = 4^n L_comb, so currents scale by 12/5 and ‖F_geom(n)‖ = (12/5)^n √21/2 → ∞.

## Why It Matters

It is the scaffold every later statement in GASKET.md (DISC-0032 to DISC-0035) is built on. None of it is a force or thrust; the repository says so.

## Derivation

Repository proofs read and checked. F: telescoping of oriented edge terms. G: the level-1 three-midpoint solve m_ab = (2a+2b+c)/5 and induction through the boundary cell. H: L^α 1 = 0 plus Schur's lemma on the standard S_3 representation. I: uniform edge length 2^{−n}.

## Assumptions

Combinatorial gasket, unit weights (Theorem I: uniform 4^n weights), spectral calculus with 0^α := 0.

## New Results

None beyond reproduction. The dipole algebra ‖F‖ = I_a √21/5 was re-derived here (F = I_a(−9/10, −√3/10)).

## Prior Art

Theorem F is the discrete Gauss/Kirchhoff identity. Theorem G is the classical gasket harmonic extension rule (the "2/5, 2/5, 1/5" rule) and the 5/3 renormalization of the normal derivative (Kigami; Strichartz, Differential Equations on Fractals, 2006). Theorems H and I are elementary corollaries (Schur's lemma; scalar rescaling).

## Novelty Analysis

DERIVATIVE: repository-specific restatement of classical gasket facts plus two short corollaries. No novelty claimed.

## Falsification Attempts

Repository scripts rerun at 81ab02b (gasket_corner_current.py, gasket_geometric_currents.py: exit 0). Archive independent dense computation (DISC-0035 script) reproduces the Schur line (1, −4/5, −1/5) for the fractional currents to 3·10^{−11} at α ∈ {0.1, 0.2, 0.3, 0.45, 0.55, 0.9}, levels 1–7.

## Experimental Validation

None (pure mathematics).

## Mathematical Status

Proved in-repo; classical.

## Patent Relevance

None.

## Related Discoveries

- DISC-0001. Mathematical. Same repository; rectangle identity this note continues.
- DISC-0032. Mathematical. Theorems J/K/L use the Schur line and dipole algebra from here.

## Open Questions

None here.

## Next Experiments

None.

## Reproduction Instructions

`git checkout 81ab02b501aef7df2f5478f55d67d50f93595d56 && python3 scripts/gasket_corner_current.py && python3 scripts/gasket_geometric_currents.py && python3 scripts/gasket_fractional_currents.py`

## Evidence Log

- 2026-10-08. GASKET.md read at 81ab02b; proofs checked; two scripts rerun (exit 0).

## Change History

- 2026-10-08. Initial archive entry.
