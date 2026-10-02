# Discovery index

This page is the graph for the 2026-10-01 read-only audit. It does not change the Stage-1 freeze. It does not raise any claim level. It only indexes what the named repositories already say.

The existing ledger is docs/SURVIVED_REJECTED_UNRESOLVED.md. This archive points at that file. It does not resolve the open items there.

The row-by-row table is DISCOVERY_LEDGER.md. Confirmed rows in that table are DISC-0001, DISC-0005, and DISC-0012.

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

There is no historical edge from description text in this pass beyond the DISC-0003 → DISC-0007 HEAD advance. Description text that still disagrees with the files on older Coherence Drive repos is recorded on DISC-0002 as provenance. The stress-tensor-modification GitHub description mismatch with CLAIM_STATUS is recorded on DISC-0009 and DISC-0010 as the same known provenance class, not a new physics result. Those descriptions were not edited. The finite-gasket-spectral-derivatives description matches its claim fence.
