# Discovery: SPARC χ² validates W ≈ 0.08 as a universal galactic coupling

## Discovery ID

DISC-0017

## Status

REJECTED as a SPARC χ² pass and as experimental support for a universal dimensionless W ≈ 0.08 coupling.

## Date Discovered

2026-10-02. Archive pass for ware-constant-phenomenology at the named evidence commit (tip merge of the Lelli+2016 default-table PR).

## Source Repositories

- beyond-repair/ware-constant-phenomenology at commit 8db3fc8cbd80f5f4ae725dc67c4748fe799fcc35, branch main.
- Files: CLAIM_STATUS.md, README.md, SPARC_CHI2_REPORT.md, data/README.md, STATUS_LOCK_2026-10-01.md, ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, CONSTANT_W_ACTION_PRINCIPLE.md, AUDIT_2026-10-01_PINCH.md, WSTAR_FIRST_PRINCIPLES_NOTE.md, sparc_run.py, killgate_verification.py, spectral_Wstar.py, verify_constant_W_action.py, tests/test_claim0.py, data/sparc_flat.csv.
- Parent merge commit message: "Merge pull request #2 from beyond-repair/repair/default-lelli-table". Squashed content commit: d6bd80de1684dd5203a26418f35824e1d740aafd.

## Original Evidence

CLAIM_STATUS.md at 8db3fc8cbd80f5f4ae725dc67c4748fe799fcc35, blob 68eb30062700ec1850d881cd05d630a216e313d9, says: "SPARC χ² as a pass | **UNSUPPORTED** (committed Lelli+2016 table, median χ²_red = 9.098, not O(1))". The same table says: "Numerical W=0.08 from this action | **NOT DERIVED**"; "Pinch-family heat trace selects 0.08 | **NOT DERIVED**"; "Experimental validation | **false**"; "Thrust validated | **false**". Addendum line: "2026-10-02 committed-table recompute prints median χ²_red = 9.098 (does not raise claim level)".

SPARC_CHI2_REPORT.md at the same commit, blob 023d9c07c83f31170c4db3451751b6fc8ff32b7f, recomputes `python sparc_run.py --mode o1` on `data/sparc_flat.csv` (Lelli+2016 Rotmod_LTG adapter; 3391 points; 175 galaxies; 165 with ≥6 points) and prints median χ²_red = 9.098, fraction < 5 = 35.8%, fraction < 10 = 52.7%. It states: "Still not O(1). SPARC χ² as a pass remains **UNSUPPORTED**." W stayed 1/(4π). Macro r0(Mb) stayed frozen.

README.md at the same commit, blob 85171f0305a19eb357030b2b0c2a23c3c11722e1, classifies the tree as "RUNNABLE SKETCH — NOT A COMPLETE PRODUCT (Claim-0 phenomenology)" and repeats the UNSUPPORTED SPARC χ² status, the median 9.098 numbers, and that kill-gate `v_∞` (10^11 M_sun, W=0.08) prints 276.5 km/s and **misses** the script's stated 100–250 km/s band. Pipeline W is 1/(4π) ≈ 0.079577, not 0.08. `spectral_Wstar.py` "still reports honestly: **no clean derivation of 0.08** from the mesh."

data/README.md at the same commit, blob 2d79ee23bae2d755614207bb729534117f4762eb, pins sha256 `84723347aa1b0ce7c6cf55b0d53016f2216723379058b9926d95fd434accf07a` for the default Lelli+2016 table and repeats median χ²_red = 9.098 / 35.8% < 5 / 52.7% < 10. "Not an O(1) pass."

STATUS_LOCK_2026-10-01.md, blob 54e15d24412515da2b4754738d619ca6d9699f7b: "0.08 remains a phenomenological candidate, not a derived invariant." ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, blob 966e044b8700e947709b3c8db2b70778b2d3b92b: scale functional I has no stationary point on tested pinch families. CONSTANT_W_ACTION_PRINCIPLE.md, blob 1a6f879a0c08baa760dc03d8e3d9e109e6216ef4: constant-W spectral source derived; parameters 0.08 and 0.23 **NOT DERIVED**. AUDIT_2026-10-01_PINCH.md, blob 146b861984a81b6d0908d8fea780962d882f47f8: pinch-family does not derive 0.08; beta = -0.005888 is circular. WSTAR_FIRST_PRINCIPLES_NOTE.md, blob cad2156a5a54ae8e6fba220b5ebe0c36b544ce54: "No completed derivation."

tests/test_claim0.py asserts the default table hash, median χ²_red ≈ 9.098, killgate "276.5" and "MISS — outside", and spectral stdout "No clean first-principles derivation of 0.08".

## Discovery

The testable claim at this HEAD is whether the committed SPARC scoring, or the Claim-0 phenomenology stack, validates W ≈ 0.08 as a universal dimensionless coupling across galactic anomalies. The repository says no. Median reduced χ² on the real Lelli+2016 table is 9.098, not O(1). SPARC χ² as a pass is UNSUPPORTED. Numerical 0.08 is not derived from the constant-W action, the pinch family, the scale functional, or the finite mesh. Kill-gate v_∞ at locked W=0.08 misses the script's own 100–250 km/s band. Claim level stays ≤2. experimental_validation stays false.

## Why It Matters

The GitHub description still says W ≈ 0.08 is a universal dimensionless coupling across subatomic, galactic, and cosmological anomalies. The 2026-10 claim files and the Lelli+2016 default recompute say the galactic SPARC pass is unsupported and 0.08 is not derived. That is a failed phenomenology claim, not a new universal constant.

## Derivation

No derivation of 0.08, of universality, or of an O(1) SPARC pass is recorded in the cited files. This row does not supply a proof the repository does not contain. It does not refit Υ, β, γ, W, or r0(Mb).

## Assumptions

The rejection uses the in-file sentences and the printed continuous o1 score on the committed table only. It does not treat the four-galaxy demo CSV as SPARC. It does not import an unreviewed proof from -ware-constant-derivation or scale-functional-I beyond the pointers already present in this tree.

## New Results

None. No claim level is raised. Local reproduction at 8db3fc8 printed median χ²_red = 9.098, Frac <5 35.8%, <10 52.7%; killgate v_∞ = 276.5 km/s MISS; verify_constant_W_action PASS; spectral_Wstar "No clean first-principles derivation of 0.08"; data/sparc_flat.csv sha256 matches data/README.md.

## Prior Art

DISC-0002 already fences W = 0.08 and thrust off locked K. DISC-0011 rejects the M2 W(n)=0.08 pin as a theorem from K. DISC-0014 and DISC-0016 reject pinch / Neumann / scale-functional routes to the seed. This entry indexes only the ware-constant-phenomenology SPARC and Claim-0 statements at 8db3fc8cbd80f5f4ae725dc67c4748fe799fcc35. Constant-W spectral source remaining DERIVED in CONSTANT_W_ACTION_PRINCIPLE.md is already in the finite-gasket / action neighborhood of DISC-0003 and is not reclassified here as a new confirmation.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. The repository does not contain a proof or a prior-art comparison that would support THEOREM or PATENT CANDIDATE. SPARC scoring and kill-gates are attackable calculations, not experimental confirmation.

## Falsification Attempts

The 2026-10-02 committed-table recompute is the in-file attack on an O(1) SPARC pass. STATUS_LOCK_2026-10-01 and AUDIT_2026-10-01_PINCH are the in-file attack on a derived 0.08. killgate_verification.py prints MISS for v_∞ under locked W=0.08. spectral_Wstar.py prints no clean mesh derivation. tests/test_claim0.py locks those honest numbers.

## Experimental Validation

None. CLAIM_STATUS.md and the status lock set experimental_validation false, thrust_validated false, and energy_extraction_validated false.

## Mathematical Status

Rejected as a SPARC χ² pass and as support for universal W ≈ 0.08. Not a theorem. Default claim level in CLAIM_STATUS.md remains 1–2.

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. Kernel sentence that 0.08 is not a consequence of locked K stays there.
- DISC-0011. Historical. Same pin, different repository, already rejected as a theorem from K.
- DISC-0014. Historical. Neck and geometric I do not select 0.08.
- DISC-0016. Historical. Pinch test and scale functional do not derive the M2 seed.
- DISC-0003. Mathematical. Finite-gasket / W < 1/6 neighborhood; constant-W action copy is not a new 0.08 derivation.

## Open Questions

Further profile structure or limited galaxy-to-galaxy physics is named in SPARC_CHI2_REPORT.md as still needed for O(1). Local dynamical W(x) remains OPEN in CLAIM_STATUS.md. Those are not elevated by this row.

## Next Experiments

Do not cite SPARC median χ²_red ≈ 9 as a pass. Do not cite the GitHub description as in-repo claim status. Do not promote kill-gate lensing saturation or muonic order-of-magnitude match as experimental validation. Prefer CLAIM_STATUS.md over the repository description.

## Reproduction Instructions

At 8db3fc8cbd80f5f4ae725dc67c4748fe799fcc35: `python sparc_run.py --mode o1`; `python killgate_verification.py`; `python verify_constant_W_action.py`; `python spectral_Wstar.py`; `pytest -q`. Read CLAIM_STATUS.md, SPARC_CHI2_REPORT.md, README.md, and data/README.md.

## Evidence Log

- 2026-10-02. list_commits on main: HEAD merge 8db3fc8cbd80f5f4ae725dc67c4748fe799fcc35, message "Merge pull request #2 from beyond-repair/repair/default-lelli-table". Author date 2026-10-02T19:38:21Z. Content commit d6bd80de1684dd5203a26418f35824e1d740aafd prints median chi2_red 9.098.
- 2026-10-02. Read the files named above. Blob SHAs: CLAIM_STATUS 68eb30062700ec1850d881cd05d630a216e313d9; README 85171f0305a19eb357030b2b0c2a23c3c11722e1; SPARC_CHI2_REPORT 023d9c07c83f31170c4db3451751b6fc8ff32b7f; data/README 2d79ee23bae2d755614207bb729534117f4762eb; STATUS_LOCK 54e15d24412515da2b4754738d619ca6d9699f7b; ADDENDUM 966e044b8700e947709b3c8db2b70778b2d3b92b; CONSTANT_W_ACTION 1a6f879a0c08baa760dc03d8e3d9e109e6216ef4; PINCH audit 146b861984a81b6d0908d8fea780962d882f47f8.
- 2026-10-02. Local run at 8db3fc8: Continuous SPARC median χ²_red = 9.098; Frac <5 35.8%; <10 52.7%; killgate v_∞ = 276.5 km/s MISS; verify_constant_W_action PASS; spectral_Wstar no clean derivation; data/sparc_flat.csv sha256 84723347aa1b0ce7c6cf55b0d53016f2216723379058b9926d95fd434accf07a.
- Provenance, not a physics result. The ware-constant-phenomenology description fetched on 2026-10-02 still says: "Phenomenological study of the Ware Constant (W ≈ 0.08) as a universal dimensionless coupling across subatomic, galactic, and cosmological anomalies." It was not edited.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
