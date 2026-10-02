# Discovery index

This page is the graph for the 2026-10-01 read-only audit. It does not change the Stage-1 freeze. It does not raise any claim level. It only indexes what the named repositories already say. A 2026-10-02 append adds DISC-0013, DISC-0014, and DISC-0015 on the same terms. A later 2026-10-02 append adds DISC-0016 on the same terms.

The existing ledger is docs/SURVIVED_REJECTED_UNRESOLVED.md. This archive points at that file. It does not resolve the open items there.

The row-by-row table is DISCOVERY_LEDGER.md. Confirmed rows in that table are DISC-0001, DISC-0005, and DISC-0012. DISC-0013, DISC-0014, DISC-0015, and DISC-0016 are rejected readings, not confirmed rows.

## Graph

Each edge is labeled mathematical, computational, or historical.

- DISC-0005 → DISC-0003. Label: mathematical. The link is spectral, through lambda_max = 6.
- DISC-0005 → DISC-0007. Label: mathematical. The link is spectral, through lambda_max = 6 and free mult(6) for n = 2..5.
- DISC-0003 → DISC-0007. Label: historical. Same repository; later HEAD adds the eigenspace split.
- DISC-0007 → DISC-0008. Label: mathematical. The V'' bound is what the rejected two-point reading would saturate.
- DISC-0003 → DISC-0002. Label: mathematical. The bound W < 1/6 does not select 0.08 and does not select thrust.
- DISC-0007 → DISC-0002. Label: mathematical. The split and V'' bound do not select 0.08 and do not select thrust.
- DISC-0001 → DISC-0002. Label: mathematical. Signed flux 0 kills the absolute-flux thrust reading.
- DISC-0004 stands beside DISC-0001, DISC-0002, DISC-0003, DISC-0005, and DISC-0007. Label: mathematical. It belongs to the same W family. It is not a thrust input.
- DISC-0006 hangs off DISC-0005. Label: computational. It is a failed detection on these graphs.
- DISC-0008 hangs off DISC-0007. Label: mathematical. It is a rejected gasket-theorem reading of an abstract extremal.
- DISC-0009 hangs off DISC-0002. Label: mathematical. Ware-modified stress as a force law is not a consequence of K.
- DISC-0010 hangs off DISC-0009. Label: historical. Same stress-tensor evidence commit; net-integral thrust reading rejected by claim flags and photon ceiling.
- DISC-0011 hangs off DISC-0002 and DISC-0009. Label: mathematical. M2 W(n)=0.08 pin is not a theorem from K.
- DISC-0012 stands beside DISC-0009 and DISC-0010. Label: historical. Classical Maxwell evaluator is the Survived infrastructure in the same repository.
- DISC-0013 hangs off DISC-0002. Label: computational. Later gasket-proxy witness that the default partition is not historical 92% and is not thrust. It does not reopen DISC-0002.
- DISC-0013 hangs off DISC-0005. Label: mathematical. Lambda = 6 multiplicity is not eta = 0.92.
- DISC-0014 hangs off DISC-0002 and DISC-0011. Label: mathematical. Tested necks and declared geometric I do not select 0.08.
- DISC-0015 hangs off DISC-0014 and DISC-0002. Label: historical. momentum-closure HEAD moved; the new pointer does not inherit 0.08 and does not certify the calculation.
- DISC-0016 hangs off DISC-0002, DISC-0011, and DISC-0014. Label: historical. m2-renormalization-law at 73a1f161 says the pinch test, the Neumann crossing, and the declared scale functional do not derive the seed 0.08 or xi = 0.23. The kernel sentence in SPECTRAL_ENDPOINT_POINTER.md stays on DISC-0002.

There is no historical edge from description text in this pass beyond the DISC-0003 → DISC-0007 HEAD advance. Description text that still disagrees with the files on older Coherence Drive repos is recorded on DISC-0002 as provenance. The stress-tensor-modification GitHub description mismatch with CLAIM_STATUS is recorded on DISC-0009 and DISC-0010 as the same known provenance class, not a new physics result. Those descriptions were not edited. The finite-gasket-spectral-derivatives description matches its claim fence. On 2026-10-02 the topological-pinch description still states a 92% thrust mechanism; that mismatch stays the DISC-0002 provenance note and is cited again on DISC-0013. The momentum-closure description still says the Ware term supplies real net momentum flux; that mismatch stays the DISC-0002 provenance note and is cited again on DISC-0015. On 2026-10-02 the m2-renormalization-law description still says the law is mesh-invariant and derived directly from the Coherence Drive baseline; that mismatch is cited on DISC-0016. None of those descriptions was edited. The sentence that W(n) is not a consequence of locked K, and that W < 1/6 is not the model cut W < 0.125, is not a new row.
