# Portfolio math — 2026-09-21

What this session actually moves, by repository. Stage 1 freeze is not edited.

## Chain roles (unchanged)

| Repo | Layer | Math that may enter | Math that may not |
|------|-------|---------------------|-------------------|
| coherence-drive | index | pointers, claim caps | new symbolic chain |
| m2-renormalization-law | B/D | \(W(n)\) ratios A/B; graph spectrum as *input* to a named LDOS | hybrid 0.795:1:1.993; spectrum as \(F_n\) |
| sierpinski-geometry-045 | B/C | gasket \(N,E,L\); tilt diagnostic; Kigami 3/5 and 5/3; \(\lambda(L)\) | thrust; continuum Weyl law from \(n\le 5\) |
| topological-pinch | D | graph proxy \(\eta\) | 92% as measured; \(\lambda=6\) multiplicity as pinch |
| stress-tensor-modification | C | Maxwell stress on a mesh | graph \(F\) as \(\oint T\cdot n\) |
| momentum-closure | C | two-surface ledger | print-skew lever arm as residual force |
| thrust-target-30 | E | 30 μN/kW as goal | any derived coupling to hit it |
| ware-constant-phenomenology | A/B | \(W_\star\) phenomenology | gasket eigenvalues as galactic \(W\) |

## Identities that help, and where

1. **Four distinct recurrences** (do not fuse):
   - harmonic energy \(\mathcal{E}_n/\mathcal{E}_{n-1}=3/5\)
   - two-corner resistance \(R_n/R_{n-1}=5/3\)
   - Dirichlet \(\lambda_{\min}\) of raw \(L_n\) \(\to 1/5\)
   - unit-load tilt \(\|F\|_{n+1}/\|F\|_n\approx 2.80,2.57,2.48\)
   Owner: sierpinski-geometry-045. Pointer only in m2.

2. **\(F\propto\gamma\)** for small shear on equal-rest-length edges.
   Explains why Sweep-138 (\(\gamma=2\)) is twice Sweep-159 (\(\gamma=1\)).
   Owner: geometry satellite. Not an M2 amplifier.

3. **\(\lambda_{\max}=6\), \(\mathrm{Tr} L=6\cdot 3^n\)** already implicit in m2/sierpinski graph code.
   Now explicit. Useful as a unit-test lock on `m2.spectral.spectrum`.
   Does not choose Model A vs B.

4. **Metric blindness of \(\gamma=0\)** under the lever-arm flux.
   Forbids combinatorial \(L\) as a print-skew sensor. Does not forbid
   combinatorial \(L\) as the Stage-2 *graph* Green-function operator
   (that operator was never a strain gauge).

## Identities that do not help the other satellites

- \(K_n=\theta/\|F\|_n\) — tautology / generation-dependent. Do not export.
- Localized \(\mathrm{mult}(6)\) — not topological-pinch \(\eta=0.92\).
- Hierarchical buses / width invariance — manufacturing diagnostic only.
- Rotation-blind Jacobian — same.
- Measure-normalized tilt sequence — unproven limit; do not freeze.

## Still the only Stage-2 gate

Frozen hardware + named LDOS + no extra \(n\)-knobs:
\(G_n\to\rho_n\to T\to F_n\).
Absent that execution, Model A or Model B remain the only published ratio sets.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
