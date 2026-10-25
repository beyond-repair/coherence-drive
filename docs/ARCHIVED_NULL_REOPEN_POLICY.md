# Archived Null Reopen Policy (Long-Term Invariant)

**Status:** Permanent repository governance rule  
**Applies to:** Scalar Stage-2 nulls, Proca P-E2 null, and any future branch classified **null** under STAGE2_ACCEPTANCE_CRITERION.md  
**Claim flags:** remain false

---

## Rule

**No archived null branch may be reopened solely through:**

- mesh refinement,
- solver replacement,
- element-family substitution (e.g. nodal → Nédélec),
- post-processing changes,
- stress-tensor reinterpretation,

**unless the governing constitutive map or boundary-value problem changes.**

---

## Rationale

Archived nulls are completed **negative controls**. They established that, under a frozen map and BVP, residuals did not exceed the spherical-control floor under joint refinement.

Procedural changes that leave the physics problem identical do not create new evidence. Re-running them is re-litigation, not research progress.

---

## What *does* justify a new Stage-2 cycle

All of the following specified **before** solving:

1. New constitutive law, and/or  
2. New boundary-condition class, and/or  
3. New stress definition (if altered),  
4. Independent physical motivation,  
5. No target-derived parameter selection,  

then the full five-step acceptance criterion from the start.

---

## Classification reminder

| Outcome | Meaning |
|---------|--------|
| Untested | Acceptance steps incomplete |
| Invalid | Target-derived parameter selection |
| Null | Tested; residual ≤ control floor |
| Candidate prediction | Tested; residual stably above floor (still not thrust_validated) |

---

## Programme layers (do not collapse)

| Layer | Status |
|-------|--------|
| Mathematical framework | Open in principle |
| Tested numerical realizations | Negative closure |
| Experimental validation | Absent |

---

*This policy protects the archive as a set of negative controls against which future proposals are measured — not as a license for propulsion claims, and not as a proof that every future map must fail.*
