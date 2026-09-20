# ABIL Exodus V2 Freshness Delta

Marker:
`STARTING_SNAPSHOT — FRESHNESS REQUIRED BEFORE EFFECT`

Parent checkpoint:
`state/exodus/ABIL_EXODUS_20260920_V2.md`

Reason:
A concurrent BT2 Exodus write landed after the parent checkpoint was created and before the final retirement handoff.

Historical observation preserved in parent checkpoint:
- BT2 Draft PR #35 head observed: `ea0fcea92d829ee4a79628f8e50f31783d65b4ea`

Fresher observation:
- BT2 Draft PR #35 head: `0ea6b0167d4ea9bfd5a976737fa77471a59759a6`
- base: `30e81cadd94fae117a7f6875523c03251c7c9f6e`
- state: OPEN / DRAFT / UNMERGED / mergeable
- new commit message: `Exodus: persist BT2 Coordinator retirement checkpoint`
- new file: `docs/handoffs/BT2_COORDINATOR_EXODUS_RETIREMENT_2026-09-20.md`

Meaning:
- the earlier `ea0f...` tuple remains correct historical evidence for the instant at which the ABIL V2 checkpoint was written;
- `0ea6...` is the fresher observed BT2 PR #35 source head at this delta;
- the BT2 checkpoint itself is also a STARTING_SNAPSHOT and does not grant merge/install/activation/provider/protected-effect authority;
- future ABIL execution must fresh-read PR #35 again rather than treating either SHA as permanently current.

No ABIL architecture/source gate changed because of this BT2 checkpoint movement.

No protected effect was performed.
