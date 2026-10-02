# Discovery: Pinch test or scale functional derives the M2 seed

## Discovery ID

DISC-0016

## Status

REJECTED as a derivation of the seed 0.08 and of xi = 0.23.

## Date Discovered

2026-10-02. Archive pass for m2-renormalization-law at the named evidence commit.

## Source Repositories

- beyond-repair/m2-renormalization-law at commit 73a1f161ea32655fb5fdb011d049aad6fe1f49e0, branch main.
- Files: ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, STATUS_LOCK_2026-10-01.md, PINCH_SEED_POINTER_2026-10-01.md, CLAIM_STATUS.md.
- SPECTRAL_ENDPOINT_POINTER.md at the same commit restates a sentence already indexed. It is not this row.
- Issue #1 remains open. It is cited only as the unchanged Sweep-137 gate, not as a new result.

## Original Evidence

ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md at 73a1f161ea32655fb5fdb011d049aad6fe1f49e0, blob 2272d5a3496ded59d6636584bb815d597d436202, says: "Claim level unchanged. Sweep-137 lock unchanged." It then says: "The declared scale functional in scale-functional-I does not produce a stationary point and does not derive the seed 0.08 or xi = 0.23."

STATUS_LOCK_2026-10-01.md at the same commit, blob 0d0a56ae52a68ca038bed66204f882105243cc12, says: "The seed W(3)=0.08 is a phenomenological pin, not a derived invariant. 0.08 is falsified as a universal consequence of the tested pinch sequences. The cubic route is closed unless beta is derived independently." The same file says: "The Neumann crossing is R(w_*)=0.08 with R'(w_*) ≠ 0. It does not supply this seed."

PINCH_SEED_POINTER_2026-10-01.md at the same commit, blob 95f39bbbbb072cee16960a5782acfbe9e01b61e2, says: "W(n) = 0.08 exp(0.23(n-3)) pins W(3)=0.08. The 2026-10-01 pinch-family test does not derive that seed and does not derive xi=0.23." It then says: "beta = -0.005888, sometimes fed to a cubic for delta, equals (2/25)^3 - (2/25)^2. It is not an independent beta function for this law." It also says: "Sweep-137 ratio lock is unchanged. The rejected hybrid 0.795:1:1.993 stays rejected."

CLAIM_STATUS.md at the same commit, blob bffd20cbe49f594926c76b9bdb84047d58532347, says: "Shared exponent xi = 0.23 is a model parameter, not a derived beta-function." The non-claims say: "The 2026-10-01 pinch-family heat trace does not derive the seed 0.08 or xi=0.23." They also say: "beta=-0.005888 is circular if used to recover 0.08." The same file says the law is "Not derived from first principles." Claim level remains 1.

SPECTRAL_ENDPOINT_POINTER.md at the same commit, blob 659ba2ebb1374cda91fc2ea101d30226d3ee648b, says: "The engineering weight W(n) = 0.08 exp(0.23(n-3)) is not a consequence of the locked kernel K = omega^2 I - W L." It also says: "The finite-gasket bound W < 1/6 is a different statement from the model cut W < 0.125." That pair of sentences is already DISC-0002. It is not reclassified here.

Issue #1 is open. Its body says: "Hybrid ratio 0.795 : 1 : 1.993 is rejected." It names the next allowed elevation as the dyadic Green function on the frozen 0.45 asymmetric Sierpinski tetrahedron, with no chi/eta/D_eff knobs. FALSIFICATION.md, blob c9cc0c98ae7052bc4c2e0083eb0ded4ae61e9f4d, is that Sweep-137 lock. This row does not add a second record of the hybrid rejection.

## Discovery

The testable claim at this HEAD, beyond the DISC-0002 kernel sentence, is whether the 2026-10-01 pinch-family test, the Neumann crossing, or the declared scale functional derives the M2 seed 0.08 or xi = 0.23. The repository says no. The seed stays a phenomenological pin. Claim level stays 1. The scale functional does not produce a stationary point on the sentence in the addendum. The recorded beta is not an independent beta function for this law.

## Why It Matters

The GitHub description still says the law is mesh-invariant and derived directly from the Coherence Drive baseline. The 2026-10 files say the seed is not derived by those tests. That is a failed derivation, not a new renormalization theorem.

## Derivation

No derivation of 0.08 or 0.23 is recorded in the cited files. This row does not supply a proof the repository does not contain. It does not recompute beta.

## Assumptions

The rejection uses the in-file sentences only. It does not import an unreviewed proof from scale-functional-I or from -ware-constant-derivation. Those repositories are pointers in the files, not evidence opened for a second classification.

## New Results

None. No claim level is raised.

## Prior Art

DISC-0002 already records that W = 0.08 and xi = 0.23 are not consequences of locked K, and that W < 1/6 is not the model cut W < 0.125. DISC-0011 already rejects the same exponential pin as a theorem from K in stress-tensor-modification. DISC-0014 records the neck-side refusal to select 0.08 and the scale-functional addendum in topological-pinch. DISC-0015 records the momentum-closure pointer that beta equals (2/25)^3 - (2/25)^2 and that a Ware surface integral does not derive 0.08. This entry indexes only the m2-renormalization-law statements at 73a1f161ea32655fb5fdb011d049aad6fe1f49e0.

## Novelty Analysis

There is no novelty claim. Status is REJECTED. The repository does not contain a proof or a prior-art comparison that would support THEOREM or PATENT CANDIDATE. The provisional ansatz is not reclassified as KNOWN or DERIVATIVE.

## Falsification Attempts

The 2026-10-01 status lock and pinch pointer are the in-file attack on a derived seed. The 2026-10-02 addendum is the in-file attack on a stationary point of the declared scale functional and on derivation of 0.08 and 0.23 from it. Issue #1 and FALSIFICATION.md remain the Sweep-137 attack on the hybrid ratio. That attack is not this row's result.

## Experimental Validation

None. The addendum, the status lock, and the pinch pointer each set experimental_validation false, thrust_validated false, and energy_extraction_validated false.

## Mathematical Status

Rejected as a derivation. Not a theorem. Claim level in CLAIM_STATUS.md remains 1 (provisional scaling ansatz).

## Patent Relevance

None established.

## Related Discoveries

- DISC-0002. Mathematical. The kernel sentence in SPECTRAL_ENDPOINT_POINTER.md stays there. Not duplicated.
- DISC-0011. Historical. Same pin, different repository, already rejected as a theorem from K.
- DISC-0014. Historical. Neck and geometric I do not select 0.08. This row does not reopen that test.
- DISC-0015. Historical. The beta identity is already quoted on the momentum-closure pointer. This row quotes the M2 file's own sentence and does not recompute it.
- DISC-0005. Mathematical. SPECTRUM_POINTER.md says the gasket locks are not F_n. That spectrum stays on DISC-0005.

## Open Questions

Stage 2 remains unexecuted. Issue #1 names the next gate G_n to LDOS_n to F_n with no fitted n parameters. FALSIFICATION.md says the same chain is the only elevation. This row does not claim that chain was run. The hybrid 0.795:1:1.993 stays the rejection already stated in issue #1. Model A and Model B ratios in FALSIFICATION.md are left as the repository's published arithmetic and are not promoted.

## Next Experiments

Do not cite the pinch test, the Neumann crossing, or the scale functional as a derivation of 0.08 or 0.23. Do not treat SPECTRAL_ENDPOINT_POINTER.md as a new discovery. Do not close issue #1.

## Reproduction Instructions

Read ADDENDUM_2026-10-02_SCALE_FUNCTIONAL.md, STATUS_LOCK_2026-10-01.md, PINCH_SEED_POINTER_2026-10-01.md, and the non-claims in CLAIM_STATUS.md at 73a1f161ea32655fb5fdb011d049aad6fe1f49e0. Read issue #1. Do not reclassify SPECTRAL_ENDPOINT_POINTER.md.

## Evidence Log

- 2026-10-02. list_commits on main: HEAD 73a1f161ea32655fb5fdb011d049aad6fe1f49e0, message "Addendum: scale functional does not derive the M2 seed." Author date 2026-10-02T06:31:55Z.
- 2026-10-02. Read the files named above. Blob SHAs: addendum 2272d5a3496ded59d6636584bb815d597d436202; status lock 0d0a56ae52a68ca038bed66204f882105243cc12; pinch pointer 95f39bbbbb072cee16960a5782acfbe9e01b61e2; CLAIM_STATUS bffd20cbe49f594926c76b9bdb84047d58532347; SPECTRAL_ENDPOINT_POINTER 659ba2ebb1374cda91fc2ea101d30226d3ee648b; FALSIFICATION c9cc0c98ae7052bc4c2e0083eb0ded4ae61e9f4d.
- 2026-10-02. Issue #1 is open. Created 2026-09-13T02:45:40Z. It rejects the hybrid ratio and names the Stage 2 gate. Not closed.
- Provenance, not a physics result. The m2-renormalization-law description fetched on 2026-10-02 still says: "Exponential renormalization law that scales the Ware Constant with fractal iteration depth. Mesh-invariant and derived directly from the Coherence Drive baseline." It was not edited.

## Change History

- 2026-10-02. Initial archive entry. No Stage-1 freeze file was changed. No repository description was edited.
