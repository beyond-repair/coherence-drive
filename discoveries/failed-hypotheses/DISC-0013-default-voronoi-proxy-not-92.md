# Discovery: Default Voronoi proxy is the historical 92% localization

## Discovery ID

DISC-0013

## Status

REJECTED as a measurement of historical 92% localization and as net thrust.

## Date Discovered

2026-10-02. Archive pass for topological-pinch after the DISC-0002 snapshot.

## Source Repositories

- beyond-repair/topological-pinch at commit 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3, branch main.
- Files: README.md, CLAIM_STATUS.md, GOVERNANCE.md, localization.py, tests/test_localization.py.
- Cross-link only: DISC-0002 recorded the earlier sentence that 92% is a hypothesis, at topological-pinch 5a7f2d04256d7400ce84f56dbc452511250df968. This row does not reopen that thrust reading.

## Original Evidence

README.md at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3 says: "The in-repo metric is a gasket-graph residual proxy (`localization.py`). Sweep-172 re-ran it locally: default boundary, levels 2–4, Voronoi corners partition as 0.5 / 0.4 / 0.1. That is not 0.92 and is not a Maxwell-stress integral."

CLAIM_STATUS.md at the same commit says: "On the public gasket with Voronoi-of-corner regions and residual current Lu, the measured eta is **not** 0.92. That number remains boxed as a hypothesis until a mesh-refined Maxwell-stress integral, with the region declared in advance, says otherwise." The same file tables region corners 0, 1, and 2 at eta 0.5, 0.4, and 0.1, each with historical_92_reproduced false, for the code default `u_corners = [1.0, -0.5, 0.0]`, levels 2, 3, and 4.

localization.py at the same commit says: "The historical 92% figure is a HYPOTHESIS and is not returned here." It also says the public response is nodal residual current r = L u, and "PROXY, not Maxwell stress divergence."

tests/test_localization.py at the same commit names `test_default_boundary_partition_is_stable_and_not_92` and says "Graph proxy only. Locked so a silent 0.92 return fails CI." The test sets expected corner fractions 0.5, 0.4, and 0.1 and asserts `historical_92_reproduced is False`.

GOVERNANCE.md at the same commit says the phrase "~92% aft-face localization" is unverified and must not be treated as an experimental result, and that the default-boundary Voronoi residual partition (levels 2–4: 0.5 / 0.4 / 0.1) "is a graph proxy observation. It is not a Maxwell-stress integral and is not the historical 92% figure."

## Discovery

The testable in-repo claim is the default gasket residual proxy, not the public repository description. That proxy does not return 0.92, and the repository forbids reading it as a Maxwell-stress integral or as thrust. The historical 92% figure stays boxed as a hypothesis. This row rejects only the identification of the proxy with that figure and with net thrust.

## Why It Matters

The GitHub description still says 92% of the stress divergence at fractal vertices produces net thrust. The files and the locked test say the opposite about the only metric this repository runs. DISC-0002 already rejected the thrust reading from the earlier prose. The later proxy lock is a separate witness and is not a new thrust mechanism.

## Derivation

No derivation of 92% or of thrust is recorded. localization.py defines eta_region as integrated absolute response in a pre-declared region divided by the domain integral. The tested response is L u on the gasket graph.

## Assumptions

The rejection uses the default boundary and Voronoi-of-corner regions named in CLAIM_STATUS.md and tests/test_localization.py. It does not assume a continuum stress tensor. It does not close a future mesh-refined Maxwell-stress integral.

## New Results

None. No claim level is raised. The proxy fractions are the repository's own test lock, not a new physical constant.

## Prior Art

DISC-0002 already records that 92% is not a measured pinch and is not a consequence of locked K. DISC-0005 already says not to read lambda_max = 6 as pinch 0.92. CLAIM_STATUS.md repeats that gasket lambda = 6 multiplicity shall not be substituted for the pinch hypothesis. This entry adds the Sweep-172 proxy witness only.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. Relation to DISC-0002 is historical: same 92% thrust reading, later evidence commit. Relation to DISC-0005 is mathematical: spectral multiplicity is not this eta.

## Falsification Attempts

tests/test_localization.py fails if the default proxy returns a value within 0.02 of 0.92 (`historical_92_reproduced`) or if the locked partition changes. CLAIM_STATUS.md states historical_92_reproduced false for every listed corner. This pass did not re-run pytest. The repository's own CLAIM_STATUS.md says local pytest was 5 passed, 0 failed, on 2026-10-01, and that this does not validate aft-face localization, thrust, or any continuum stress integral.

## Experimental Validation

None. CLAIM_STATUS.md sets experimental_validation false. README.md says green CI is not experimental validation.

## Mathematical Status

Rejected as an identification of the graph proxy with eta = 0.92 or with net thrust. The continuum 92% statement remains an unverified hypothesis in-file, not a theorem.

## Patent Relevance

None established. The repository contains no prior-art comparison that would support a patent reading.

## Related Discoveries

- DISC-0002. Historical. Thrust from the 92% pinch was already rejected. This row cross-links that rejection and does not reopen it.
- DISC-0005. Mathematical. Gasket spectrum locks are not a 0.92 pinch.

## Open Questions

Whether a mesh-refined Maxwell-stress integral, with the region declared in advance, could ever reproduce a localization fraction is open in CLAIM_STATUS.md. This archive does not run that integral and does not resolve the residual-force item in docs/SURVIVED_REJECTED_UNRESOLVED.md.

## Next Experiments

Do not cite localization.py, the 0.5 / 0.4 / 0.1 partition, or a green pytest run as aft-face thrust. Any later Maxwell-stress question stays outside this proxy.

## Reproduction Instructions

Read README.md, CLAIM_STATUS.md, GOVERNANCE.md, localization.py, and tests/test_localization.py in beyond-repair/topological-pinch at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3. Do not use the GitHub description as the measurement.

## Evidence Log

- 2026-10-02. Read the files named above at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3. Branch main. Default branch confirmed by the repository listing.
- 2026-10-02. Commit messages after the DISC-0002 pinch snapshot 5a7f2d04256d7400ce84f56dbc452511250df968 include 3e62e04d92ab26a426cdb1a448114097542cbf15, which states that the default Voronoi residual proxy is 0.5/0.4/0.1, not 0.92. The deciding sentences quoted above are the text at 0147a6f6344fda7cca818e037c5ad5e1a4b4b4b3.
- Provenance, not a physics result. The topological-pinch description fetched on 2026-10-02 still says: "The aft-face topological pinch — 92 % of the stress divergence is localized at fractal vertices. This is the physical mechanism that breaks symmetry and produces net thrust in the Coherence Drive." It was not edited. The same mismatch was already logged on DISC-0002.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
