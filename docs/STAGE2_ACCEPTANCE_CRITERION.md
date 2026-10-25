# Stage-2 Acceptance Criterion (Repository Invariant)

**Status:** Permanent governance rule for Coherence Drive numerical work.  
**Claim flags:** remain false until a separate claim-validation process succeeds.

---

## Principle

A constitutive map is **tested** only after all of the following are completed.  
Until then it is **untested**, regardless of symbolic elegance or proxy numerics.

---

## Five-step acceptance test

A constitutive map / BVP is considered **tested** only after:

1. **Continuum formulation is frozen**  
   Field equations, domain, and boundary data are written down and not altered during the study to chase a residual.

2. **Spherical control is solved**  
   The identical PDE and BC class on a sphere (or other symmetry-null geometry) is solved; continuum net surface integral must be consistent with zero (or with a known analytic null).

3. **Joint refinement study is completed**  
   Mesh (and truncation radius, if applicable) are refined together; residual behaviour is reported as a table, not a single run.

4. **Residual exceeds control floor**  
   The asymmetric (or gasket) residual remains **significantly above** the spherical-control noise floor under joint refinement.  
   Residuals at or below the floor are classified as **consistent with zero**, not as continuum signals.

5. **No parameter is selected using the thrust target**  
   Couplings, masses, amplitudes, and boundary strengths are not chosen to match \(3\times10^{-8}\,\mathrm{N/W}\) or any other force design goal.

---

## Classification of outcomes

| Outcome | Label |
|---------|--------|
| Steps 1–3 done; residual ≤ floor under refinement | **Null** (tested; continuum G not established) |
| Steps 1–5 done; residual stably above floor | **Candidate prediction** (still not thrust_validated) |
| Any of 1–5 missing | **Untested** |
| Parameter chosen via thrust target | **Invalid study** (target_fitting_performed) |

---

## Explicit non-equivalences

- An unrefuted Stage-1 equation is **not** experimental support.  
- A geometric proxy that is not a PDE solution is **not** a continuum G.  
- Lowering discretisation error (e.g. Nédélec) on a path already at or below the floor is **not** evidence of a physical effect.  
- A candidate prediction is **not** `thrust_validated` or `experimental_validation`.

---

## Relation to archived Stage-2 work

Scalar interior/exterior Yukawa and Proca P-E2 nodal studies completed steps 1–4 with residuals at or below the control floor → archived as **null**.  
Those branches do not justify Stage-3 experiment under the maps tested.

Further Stage-2 work requires **new** constitutive/BVP content, then this criterion again from step 1.

---

*This document is an acceptance gate, not a physics claim.*
