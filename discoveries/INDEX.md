# Discovery index

This page is the graph for the 2026-10-01 read-only audit. It does not change the Stage-1 freeze. It does not raise any claim level. It only indexes what the named repositories already say.

The existing ledger is docs/SURVIVED_REJECTED_UNRESOLVED.md. This archive points at that file. It does not resolve the open items there.

The row-by-row table is DISCOVERY_LEDGER.md. Confirmed rows in that table are only DISC-0001 and DISC-0005.

## Graph

Each edge is labeled mathematical, computational, or historical.

- DISC-0005 → DISC-0003. Label: mathematical. The link is spectral, through lambda_max = 6.
- DISC-0003 → DISC-0002. Label: mathematical. The bound W < 1/6 does not select 0.08 and does not select thrust.
- DISC-0001 → DISC-0002. Label: mathematical. Signed flux 0 kills the absolute-flux thrust reading.
- DISC-0004 stands beside DISC-0001, DISC-0002, DISC-0003, and DISC-0005. Label: mathematical. It belongs to the same W family. It is not a thrust input.
- DISC-0006 hangs off DISC-0005. Label: computational. It is a failed detection on these graphs.

There is no historical edge in this pass. Description text that still disagrees with the files is recorded on DISC-0002 as provenance. Those descriptions were not edited.
