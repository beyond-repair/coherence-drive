# Layer map — frozen vs derived vs hypothesized

This file exists so the six layers cannot be collapsed into one sentence.

| Layer | Code | What may be written | What may not be written |
|-------|------|---------------------|-------------------------|
| **A. Frozen inputs** | `FROZEN` | \(W(n)=0.08\,e^{0.23(n-3)}\), \(\alpha_{\rm geom}=0.45\) as a design ratio, \(W_\star=1/(4\pi)\) as a galactic phenomenology anchor, target \(3\times10^{-8}\,\mathrm{N/W}\) as a *design goal* | That any of these is a measured law of nature |
| **B. Derived quantities** | `DERIVED` | \(W(2)\approx0.063563\), \(W(4)\approx0.100688\), Model A ratios \(0.795:1:1.259\), gasket \(N,E,\mathrm{Tr}(L^k)\), Kigami \(3/5\) and \(5/3\), \(\lambda_{\max}=6\), Dirichlet \(\lambda_{\min}\) ratio \(\to 1/5\) | Fusing those four gasket recurrences into one law; a derived number promoted to an independent measurement |
| **C. Numerical measurements** | `NUM` | Flux diagnostics, dual-surface residuals, LDOS histograms, FD checks, \(\eta_{\rm region}\) on a named proxy, conductance/shear Jacobian | “The simulation produced thrust” |
| **D. Hypotheses** | `HYP` | Discrete-scale-invariance / log-periodic vacuum response; pinch localization; modified \(\Delta T_W\); measure-normalized tilt limit | Hypothesis restated as fact |
| **E. Engineering targets** | `TGT` | \(30\,\mu\mathrm{N/kW}\) | Fitting \(\kappa,\chi,\eta,D_{\rm eff}\) to hit it |
| **F. Experimental validation** | `EXP` | The three flags below, all false | Changing the flags because a residual is nonzero in software |

Four gasket recurrences stay in **separate** rows of B/C. See [PORTFOLIO_MATH_2026-09-21.md](PORTFOLIO_MATH_2026-09-21.md).

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
