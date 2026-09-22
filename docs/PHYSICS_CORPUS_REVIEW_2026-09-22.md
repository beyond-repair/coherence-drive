# Physics corpus review — 2026-09-22

**Coverage statement.** The org has 77 public repositories. Most are agents, OS, trading, or tools. This review is the *theoretical-physics subset*, file-inventoried. It is not a line-by-line audit of FortiTrade, SEEM, LegionOS, or BlockSwarm.

Stage 1 freeze (`MATH_THEORY_CLOSURE.md`) is not edited.

## 1. Corpus

| Repo | Role | What is actually in-tree |
|------|------|--------------------------|
| coherence-drive | index + freeze | markdown only |
| ware-constant-phenomenology | galactic scoring + W notes | scripts + TeX + audits |
| m2-renormalization-law | W(n) ratios + graph LDOS scaffold | Python |
| sierpinski-geometry-045 | mesh + graph algebra | generator + audits |
| stress-tensor-modification | Maxwell T + BEM sketches | `physics_evaluator.py` |
| momentum-closure | ledger scaffolding | geometry/RF helpers, no residual CI |
| topological-pinch | η proxy | `localization.py` |
| thrust-target-30 | design goal | claim level 0 |
| CFTv3.3-IQG-Unified-Framework | ledger | markdown/TeX, no executables |
| CFT-v3.1 | screened-metric papers | 2 short TeX files |
| CFT-v3.0 | archived predecessor | out of this pass |
| -ware-constant-derivation | stub | README only |
| The-Origin-Point-Hypothesis. | separate hypothesis | short TeX + PDF |
| optimization-limit-conjecture | graph-cost conjecture | Theorem A + experiments |
| -Entanglement-and-Emergence | tensor-network gravity note | not re-derived this pass |
| sovereign-clean-room | offline numerical bridge | not line-read this pass |

## 2. Proofs that stand

Already locked elsewhere, still valid:

- E1–E4 ⇒ \(1/(4\pi)\) (conditional).
- \(Y_{00}\) integrals; free-monopole DtN \(\kappa=m\coth(mR)-1/R\).
- Model A/B algebra; hybrid rejected.
- Kigami 3/5 and 5/3; gasket \(\lambda_{\max}=6\); Dirichlet \(\lambda_{\min}\to 1/5\); \(F\propto\gamma\).
- Log-ansatz circular orbits: \(v_c^2=GM/r+W GM/r_0\).

**New, closed this pass**

1. **Photon Class B ceiling** (`PHOTON_CLASS_B_CEILING.md`).  
   Radiation force on a complete absorber satisfies \(F\le P/c\).  
   \(1/c\approx 3.3356\times10^{-9}\,\mathrm{N/W}\).  
   Target \(3\times10^{-8}\approx 9.0\times(1/c)\).  
   Pure EM photon momentum cannot hit the published target. Ordinary.

2. **Maxwell nulls in `physics_evaluator.py`.**  
   \(E=B=0\Rightarrow F_{\rm EM}=0\).  
   Uniform \(E\) on the coded unit-sphere quadrature \(\Rightarrow F_{\rm EM}\approx 0\)  
   (closed-surface discrete identity for that field).  
   Default `W_STAR=0.08` is the rounded lock, not \(1/(4\pi)\).

3. **Optimization-limit Theorem A** (`Proofs/TheoremA.tex`).  
   On a depth-\(D\) \(k\)-ary tree with \(x_d=a^d x_0\) and  
   \(\Phi=\sum_d k^d(a^d x_0-\bar x)^2\),
   \[
   x_0^*=\bar x\,\frac{\sum_{d=0}^D (ka)^d}{\sum_{d=0}^D (ka^2)^d}.
   \]
   Unique minimum because \(\partial^2\Phi/\partial x_0^2>0\).  
   Infinite-\(D\) reduction to \(\bar x(1-ka)/(1-ka^2)\) needs \(|ka|<1\).  
   This does **not** derive \(W_\star\). Fitting \((k,a)\) so that a residual equals 0.08 is calibration (CONJECTURE.md “Optimization Target”).

4. **Pinch proxy.** `localization.py` defines η before evaluation. Historical 0.92 is not returned as a default. \(\lambda=6\) multiplicity is not η.

## 3. Written as theory, not proved

| Item | Repo | Status |
|------|------|--------|
| \(c_\star=1\) from bulk Proca | phenomenology | convention |
| Log metric from Proca \(T_{\mu\nu}\) | phenomenology TeX | ansatz |
| Unique weak-field law | Math.md vs Ware-Full-Action | conflict |
| \(\zeta=0.08\) vacuum elasticity | CFT-v3.1 Paper 1 | postulated |
| \(S(\rho,L)\approx\tanh(\rho/\rho_{th})\) | CFT-v3.1 | postulated |
| SPARC as validation | phenomenology / CFT ledger | \(\chi^2\sim 9\), not O(1) |
| \(\Delta T_W\) as derived Maxwell piece | stress-tensor | hook; info stress is a dyad template |
| Mesh-converged residual force | momentum-closure | UNSUPPORTED |
| 30 μN/kW | thrust-target-30 | goal |
| Origin-point hypothesis | that repo | separate; not a Ware proof |

CFT-v3.1 Paper 1 is six pages of postulates. It does not derive \(\zeta\).

## 4. Code that must not be mistaken for proofs

- `physics_evaluator.informational_stress` is a scaled dyad, not \(\delta S/\delta g_{\mu\nu}\).
- BEM / full-wave files are sketches; CLAIM_STATUS says ε_F not reported.
- m2 `spectral.py` builds LDOS weights; none is designated force.
- SPARC scripts score a model; they do not derive W.
- June TeX still contains deprecated M2 indexing and hybrid 1.993.

## 5. What is still the only elevation path

Same as the freeze: geometry → field → \(\mathcal{G}\) → \(\Delta F\) without fitting the target, **or** an honest INCONCLUSIVE. Photon Class B is already excluded as a target-matching branch.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
