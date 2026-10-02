# Discovery: Ware-modified stress as consequence of locked K

## Discovery ID

DISC-0009

## Status

REJECTED as a consequence of the locked spectral kernel K.

## Date Discovered

2026-10-01. This is the date of the archive pass that indexed stress-tensor-modification at the named evidence commit.

## Source Repositories

- beyond-repair/stress-tensor-modification at commit adab20380b2d2e35776aeed249d39229b8a06fdd. Files: SPECTRAL_ENDPOINT_POINTER.md; physics_evaluator.py (optional informational_stress / Ware-weight hooks); CLAIM_STATUS.md.
- beyond-repair/coherence-drive docs/SPECTRAL_ENDPOINT.md at 095d29d1a107d719f8aed9f89834d917b119ca4c (blob be85ceab6fa39cc359811b2a533f0588ed72792a).
- beyond-repair/coherence-drive docs/SURVIVED_REJECTED_UNRESOLVED.md at the same freeze HEAD: Unresolved row "Modified stress tensor as a derived ΔT_W (hook exists; not certified)"; Survived row "Maxwell stress infrastructure (classical evaluator + sphere nulls)".

## Original Evidence

SPECTRAL_ENDPOINT_POINTER.md at adab20380b2d2e35776aeed249d39229b8a06fdd states, verbatim: "A modified stress used as a force law does not follow from K = omega^2 I - W L. Delta F = W chi_vac G stays outside that chain. See coherence-drive docs/SPECTRAL_ENDPOINT.md."

docs/SPECTRAL_ENDPOINT.md lists among items that are not consequences of locked K: "thrust, 30 uN/kW as physics, and Delta F = W chi_vac G."

physics_evaluator.py implements classical Maxwell T_ij and an optional informational_stress term scaled by W(n) * chi_vac. The optional term is a code hook. The pointer file denies that using that hook as a force law follows from K.

CLAIM_STATUS.md marks Experimental validation false, Thrust validated false, Reactionless closed thrust false, and says GitHub description text that implies proven thrust is out of date.

## Discovery

Reading the Ware-weight / modified-stress force law as a consequence of the locked kernel K is rejected. The repository itself fences Delta F = W chi_vac G outside that chain. Whether a later independent Delta T_W can be certified remains the unresolved ledger item already named in docs/SURVIVED_REJECTED_UNRESOLVED.md. This archive does not certify that hook and does not raise it.

## Why It Matters

The GitHub description of this repository still presents modified Maxwell stress with Ware injection as the equation that produces a net non-zero surface integral for thrust. The in-repo pointer and CLAIM_STATUS disagree. The disagreement is indexed here as a rejected reading of K, not as a new physics result.

## Derivation

No derivation from K is recorded, because the claim is rejected. Classical Maxwell T_ij in physics_evaluator.py is ordinary EM (see DISC-0012). The optional informational_stress term is not promoted to a spectral consequence.

## Assumptions

The rejection uses the pointer file and docs/SPECTRAL_ENDPOINT.md. It does not assume that an independent continuum Delta T_W is impossible. It does not assume momentum has been measured.

## New Results

None. No claim level is raised.

## Prior Art

The locked spectral endpoint and the narrative Unresolved row for derived Delta T_W already exist in coherence-drive. This entry does not add an external citation.

## Novelty Analysis

There is no novelty claim. Status is REJECTED for the "follows from K" reading. Relation to DISC-0002 is mathematical: both deny Delta F / thrust as consequences of K. Relation to DISC-0012 is historical: same repository separates classical Maxwell infrastructure from the Ware force-law reading.

## Falsification Attempts

The pointer file is the recorded refusal. CLAIM_STATUS keeps thrust flags false. Dual-surface epsilon_F docs in this repository report residuals not closed and say huge epsilon_F is numerical error, not reactionless discovery.

## Experimental Validation

None. CLAIM_STATUS: Experimental validation false.

## Mathematical Status

Rejected as a consequence of K. Independent Delta T_W certification remains unresolved elsewhere.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. Thrust and Delta F = W chi_vac G are not consequences of K.
- DISC-0010. Historical. Same repository; the net-integral / thrust description claim.
- DISC-0011. Mathematical. M2 W(n)=0.08 pin is not a theorem from K.
- DISC-0012. Historical. Classical Maxwell evaluator is the survived infrastructure in the same repo.

## Open Questions

Whether any residual force remains after classical subtraction is open (existing unresolved ledger). Whether a derived Delta T_W can be certified is open. This archive does not resolve either item.

## Next Experiments

Do not treat the optional Ware hook in physics_evaluator.py as a spectral theorem. Any later Delta T_W work must stay on the unresolved ledger item and must not cite K as the derivation.

## Reproduction Instructions

Read SPECTRAL_ENDPOINT_POINTER.md and CLAIM_STATUS.md in stress-tensor-modification at adab20380b2d2e35776aeed249d39229b8a06fdd. Read docs/SPECTRAL_ENDPOINT.md and the Unresolved Delta T_W row in docs/SURVIVED_REJECTED_UNRESOLVED.md in coherence-drive at 095d29d1a107d719f8aed9f89834d917b119ca4c. Inspect informational_stress in physics_evaluator.py at the same stress-tensor evidence commit.

## Evidence Log

- 2026-10-01. Read stress-tensor-modification SPECTRAL_ENDPOINT_POINTER.md, CLAIM_STATUS.md, README.md, docs/BEM_EPSILON_F_EXPLORATION.md, docs/MAXWELL_EPSILON_F_RUN.md, docs/PHOTON_CLASS_B_CEILING.md, physics_evaluator.py, closure.py at adab20380b2d2e35776aeed249d39229b8a06fdd.
- 2026-10-01. Confirmed coherence-drive docs/SPECTRAL_ENDPOINT.md "not consequences of K" sentence and SURVIVED_REJECTED_UNRESOLVED.md Unresolved Delta T_W row.
- Provenance, not a physics result. GitHub description fetched 2026-10-01 ET for stress-tensor-modification: "Modified Maxwell stress tensor with Ware Constant injection — the exact equation that produces the net non-zero surface integral responsible for thrust in the Coherence Drive." That sentence disagrees with CLAIM_STATUS.md and SPECTRAL_ENDPOINT_POINTER.md. It was not edited.

- 2026-10-02. Verification re-check: stress-tensor-modification origin/main had advanced to 09cd4862ea7ec4796b7ff96873e00c5295a92717 (pinch pointer). Cited fences at adab20380b2d2e35776aeed249d39229b8a06fdd still hold; SPECTRAL_ENDPOINT_POINTER.md text unchanged through 953097c. Evidence SHA remains adab203; not re-baselined to newer main.

## Change History

- 2026-10-02. Verification pass: confirmed claims at adab203; noted origin/main advance to 09cd486 without changing cited fences. Wording adjusted from HEAD to evidence commit.
- 2026-10-01. Initial archive entry. Descriptions were not edited. No Stage-1 freeze file was changed.
