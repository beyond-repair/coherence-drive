# Discovery ledger

Archive pass date: 2026-10-01. This table indexes existing repository statements. It does not change the Stage-1 freeze and it does not raise any claim level.

Confirmed rows are only DISC-0001 and DISC-0005. DISC-0003, DISC-0004, and DISC-0007 are derivative records, not new confirmations. DISC-0002, DISC-0006, and DISC-0008 are rejected readings.

GitHub repository descriptions are stale relative to CLAIM_STATUS for older Coherence Drive repos. They still say that W is about 0.08 is derived, that thrust is produced, and that the engine is physics-closed. Those descriptions were not edited. The mismatch is provenance, not a physics result. The file-level statements are the ones indexed here. The finite-gasket-spectral-derivatives description matches its claim fence. The existing narrative ledger remains docs/SURVIVED_REJECTED_UNRESOLVED.md.

| ID | Discovery | Repository | Type | Status | Evidence | Prior Art | Validation | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DISC-0001 | Discrete flux identity | beyond-repair/informational-flux-identity | mathematical | KNOWN | README Theorem A and witness.json at ce070589ca257e9b5c8158403606ace5dd183aea | classical discrete divergence theorem, stated in-repo | witness integers only; not a laboratory test | Re-run the existing flux script. Do not read absolute flux as thrust. |
| DISC-0002 | Thrust from aft-heavy flux | beyond-repair/informational-flux-identity | failed hypothesis | REJECTED | Theorem B; coherence-drive docs/SPECTRAL_ENDPOINT.md at 095d29d1a107d719f8aed9f89834d917b119ca4c | not a new identity | none | Leave residual force after classical subtraction unresolved. |
| DISC-0003 | Finite gasket trace identity | beyond-repair/finite-gasket-spectral-derivatives | mathematical | DERIVATIVE | prior HEAD 33dfec7db730c2dd7baf62892242835a2d25544b; repo now at 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 | classical scalar identity, as that repo states | none | Do not use the W < 1/6 bound to select 0.08 or thrust. |
| DISC-0004 | Two-mode factor two | beyond-repair/bloch-coherence-factor2 | mathematical | DERIVATIVE | TWO_MODE_PROOF.md at 52ff29d6dea7e2f4361ce04fdadc34128d9c88e0 | in-repo 2 by 2 diagonalization | none | Do not export the factor 2 as thrust or as 0.08. |
| DISC-0005 | Gasket spectrum locks | beyond-repair/sierpinski-geometry-045 | mathematical | KNOWN | SPECTRUM.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1 | in-repo combinatorial identities | none | Do not read lambda_max = 6 as pinch 0.92. |
| DISC-0006 | Log-periodic period | beyond-repair/sierpinski-geometry-045 | failed hypothesis | REJECTED | LOG_PERIODIC.md at 16cc0851185d2a38f63dcf53fea22fef7ef915e1 | in-repo pre-registered test | not measured | Do not treat the Dirichlet lock as a measured period. |
| DISC-0007 | Lambda = 6 eigenspace split | beyond-repair/finite-gasket-spectral-derivatives | mathematical | DERIVATIVE | README Lambda = 6 section and COMPLETION_LOG.md at 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 | elementary from locked defs; Dirichlet mult classical via Qiu arXiv:1206.1381 | none | Do not select W; free mult(6) for all n remains open. |
| DISC-0008 | Two-point {0, 6} as gasket theorem | beyond-repair/finite-gasket-spectral-derivatives | failed hypothesis | REJECTED | README negative-result subsection and COMPLETION_LOG.md at 7f66ef46ea65e5a368b852a0fb839ff1e9993ff0 | abstract extremal, not free gasket spectrum | none | Keep the V'' inequality; do not commit saturation on free graphs. |
