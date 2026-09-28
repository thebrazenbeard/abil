# Evidence Ledger Integrity and Continuity V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #14 — replay-ledger anti-rollback
- Draft PR #16 — execution evidence and causal attribution
- Draft PR #17 — transaction reconciliation and late evidence
- Draft PR #12 — currentness snapshot/revalidation

## Purpose

ABIL increasingly relies on durable evidence:

- command requests;
- gateway decisions;
- dispatch reservations;
- execution attempts;
- target receipts;
- telemetry observations;
- ambiguity records;
- replay-consumption state;
- reconciliation generations;
- control-coverage evidence;
- currentness receipts.

A new systems question follows:

> How can a future implementation prove that the evidence history itself has not been silently truncated, reordered, deleted, rewritten, selectively restored, or split across divergent replicas?

A valid individual record does not prove the evidence set is complete.

## 1. Integrity, completeness, and availability are separate

Distinguish:

### `RECORD_INTEGRITY`

The retained bytes for a record match its exact immutable identity.

### `LEDGER_CONTINUITY`

The retained ordered history proves no required predecessor/event position is silently missing within the declared ledger scope.

### `LEDGER_COMPLETENESS`

The system has the required evidence classes/partitions needed for the claim or operation.

### `LEDGER_AVAILABILITY`

The evidence can currently be read.

A readable ledger can be incomplete.

An intact record can live inside a truncated history.

## 2. Evidence history is not ordinary mutable application state

For evidence that affects:

- replay safety;
- ambiguity resolution;
- currentness;
- commissioning claims;
- control coverage;
- causal attribution;
- audit/root cause;
- protected-effect admission;

ordinary update-in-place semantics are dangerous.

Corrections should preferably append/supersede rather than rewrite the original record.

## 3. Immutable evidence record identity

A future evidence record should bind, as applicable:

- schema/type;
- deployment identity;
- record ID;
- subject/request/transaction identity;
- event generation/sequence;
- producer identity;
- source identity;
- timestamp/order metadata;
- payload digest;
- canonicalization profile identity;
- prior-link / segment identity where applicable;
- partition/ledger identity.

Exact representation is open.

## 4. Ledger sequence / continuity

A future ledger should make ordering gaps detectable.

Possible mechanisms include:

- monotonic sequence numbers;
- hash chaining;
- Merkle segments;
- signed checkpoints;
- database log sequence numbers;
- append-only object manifests;
- external checkpoint anchors.

This research does not select one mechanism.

The requirement is:

> A verifier should be able to distinguish "no event existed" from "history is missing or unverifiable" when that distinction matters.

## 5. Truncation detection

Hostile case:

1. request dispatched;
2. ambiguous receipt recorded;
3. physical observation conflicts;
4. later reconciliation remains unresolved;
5. ledger is restored from an older snapshot ending before steps 3–4;
6. surviving history now looks cleaner.

A future verifier should detect that the ledger cut regressed or is incomplete.

A stale but internally consistent prefix must not silently masquerade as current complete history.

## 6. Negative/conflicting evidence preservation

Evidence systems are vulnerable to selective deletion.

A future design should preserve:

- failed validations;
- denied requests;
- conflicting observations;
- negative controls;
- rejected causal hypotheses;
- superseded reconciliation results;
- stale/currentness failures;
- replay conflicts;
- manual corrections.

"Only keep successful evidence" creates systematic claim laundering.

## 7. Correction semantics

If a record is wrong:

- retain original record;
- append correction/supersession;
- bind reason;
- bind reviewer/producer;
- bind corrected subject;
- preserve the old identity for audit.

A corrected record should not erase the fact that downstream decisions may have consumed the old one.

## 8. Evidence partitioning

Large systems may partition by:

- deployment;
- authority domain;
- writer/gateway;
- signal/source;
- transaction;
- time segment;
- evidence class.

A currentness/decision verifier must know which partitions are required.

A complete partition A does not prove partition B is present.

## 9. Required partition profile

A future operation may resolve an evidence-ledger profile identifying:

- required partitions;
- required evidence classes;
- minimum continuity point;
- current checkpoint IDs;
- retention horizon;
- acceptable source replicas;
- expected producer identities.

A caller should not be able to omit an inconvenient partition.

## 10. Replica divergence

Replicated evidence stores may diverge.

Potential states:

- `REPLICA_CONSISTENT`
- `REPLICA_LAGGING`
- `REPLICA_CONFLICTING`
- `REPLICA_PARTIAL`
- `REPLICA_UNKNOWN`

A verifier should not select the replica with the most favorable evidence.

Conflict/reconciliation must be explicit.

## 11. Restore / backup cut

A backup should bind its evidence-ledger cut.

Potential metadata:

- ledger generation;
- last sequence/event position;
- segment/checkpoint digest;
- required partition cuts;
- replay-ledger generation;
- reconciliation generation;
- authority/currentness generation references.

Restore should compare the backup cut against current protected/current evidence state.

## 12. Evidence anti-rollback

Evidence anti-rollback is distinct from authority anti-rollback.

Authority may stay current while evidence history rolls backward.

Example:

- authority A12 remains valid;
- evidence ledger L20 contains one ambiguous and one conflicting transaction;
- restore returns evidence ledger L16;
- current authority still A12.

A future system must not treat L16 as complete current evidence merely because authority is current.

## 13. Selective restore

Restoring only:

- positive target receipts;
while omitting:
- physical sensor conflicts;
- operator corrections;
- negative controls;

must be detectable as an incomplete evidence cut.

Evidence restore should be profile-aware, not best-effort cherry-picking.

## 14. Record producer identity

Evidence quality depends on source.

Bind producer/source identities such as:

- gateway;
- target adapter;
- deterministic runtime;
- telemetry collector;
- technician/operator;
- evaluator;
- reconciliation engine;
- learner/candidate plane.

The learner should not be able to forge an independent-evaluator record merely by matching schema.

## 15. Trust domains

Different evidence types may require different trust.

Examples:

- target receipt;
- independent physical sensor;
- technician assertion;
- learner hypothesis;
- evaluator verdict;
- safety-classification record.

One storage system can hold them all, but provenance/trust must remain distinct.

## 16. Canonicalization

Any digest/chaining scheme needs deterministic canonicalization.

Bind:

- schema version;
- field ordering;
- null/omitted semantics;
- numeric representation;
- unit representation;
- timestamp encoding;
- binary/string encoding;
- collection order;
- nested reference encoding.

Digest equality under unknown canonicalization is weak evidence.

## 17. Clock/order uncertainty

Distributed systems may not have perfect clocks.

Do not infer absolute causal order solely from wall-clock timestamps when:

- clocks differ;
- NTP/PTP is degraded;
- devices timestamp independently;
- buffering delays events.

Where ordering matters, use additional sequence/correlation evidence.

## 18. Gap semantics

If continuity cannot be proven:

Potential status:
`EVIDENCE_GAP_UNKNOWN`.

A gap may block:

- replay resolution;
- causal attribution;
- strong control-coverage claim;
- write resumption for affected scope;
- benchmark claim.

Do not fill gaps with "nothing happened."

## 19. Retention and compaction

Evidence cannot grow forever.

Future retention/compaction may:

- move old records to archive;
- compact segments;
- retain roots/checkpoints;
- retain derived summaries with proof links;
- delete data after a qualified irrelevance/expiry rule.

But compaction must not silently destroy evidence required to:

- prove replay history;
- resolve ambiguity;
- audit a current model;
- support current control coverage;
- detect selective omission.

## 20. Tombstones

If evidence is intentionally deleted under policy, retain a tombstone/manifest when needed.

A tombstone may bind:

- deleted record/segment identity;
- reason/policy;
- deletion time;
- authorizer;
- retention rule;
- retained summary/proof root;
- affected claims.

"File missing" and "policy-deleted with proof" are different states.

## 21. Reconciliation history

PR #17's reconciliation generations should remain auditable.

A later resolution should bind:

- prior resolution;
- new evidence;
- supersession reason;
- resulting disposition.

Deleting prior reconciliation generations would hide uncertainty evolution.

## 22. Replay-ledger linkage

PR #14 replay state and evidence ledger may be separate stores.

They should still cross-bind enough to detect:

- replay says request consumed;
- evidence ledger has no corresponding dispatch/attempt history;
- evidence says ambiguous request existed;
- replay ledger lost it.

Cross-store inconsistency should not be silently ignored.

## 23. Currentness proof linkage

PR #11 currentness proofs should identify the evidence-ledger cut they rely on.

If the evidence ledger later regresses below that cut, the old currentness proof may no longer be safely reusable.

## 24. Snapshot/revalidation linkage

PR #12 version vectors may need an evidence-ledger generation/checkpoint when protected-effect admission depends on evidence completeness.

A decision validated against L20 should not dispatch after restore to L16 without revalidation.

## 25. Evidence export / migration

Moving evidence across storage systems should preserve:

- record identities;
- ordering/continuity;
- provenance;
- partition boundaries;
- checkpoint roots;
- supersession links;
- deletion/tombstone metadata.

A "successful export" should not mean only that files copied.

## 26. Corruption handling

If corruption is detected:

- identify affected segment/partition;
- preserve available evidence;
- mark uncertainty;
- avoid silently dropping corrupt records;
- determine affected claims/operations;
- reconcile from independent replicas if possible.

Do not replace corrupted evidence with guessed reconstruction and label it original.

## 27. Learner/adaptive-plane constraints

The learner may consume evidence.

It must not be able to:

- erase negative evidence;
- rewrite provenance;
- delete conflicting observations;
- reorder history to improve apparent performance;
- create fake independent-evaluator receipts;
- mutate audit roots.

Learning output is not audit authority.

## 28. Benchmark integrity

Research/qualification benchmarks also depend on evidence completeness.

Retain:

- participant-visible inputs;
- evaluator-only context;
- frozen outputs;
- scoring records;
- hostile cases;
- failed runs;
- invalidations;
- resource accounting.

A benchmark packet missing failed profiles must not support the same claim as the complete packet.

## 29. Evidence checkpoint concept

A future `EvidenceLedgerCheckpoint` could bind:

- ledger/partition identity;
- deployment;
- start/end sequence;
- prior checkpoint identity;
- segment/root digest;
- producer/aggregator identity;
- required partition profile;
- completeness disposition;
- corruption/gap disposition;
- timestamp/as-of;
- immutable checkpoint digest.

This is a research shape, not a mandated schema.

## 30. Claim use

A claim should bind the evidence cut it used.

Examples:

- currentness receipt -> ledger checkpoint L20;
- control coverage -> evidence cut C17;
- reconciliation receipt -> transaction evidence set E42;
- benchmark claim -> package checkpoint B9.

If the evidence cut is later invalidated, downstream claims need review.

## 31. Hostile research cases

A future implementation should detect or fail closed on at least:

1. old ledger snapshot restored as current complete history;
2. negative/conflicting record deleted while positive receipt remains;
3. sequence gap silently treated as no event;
4. one replica omits failed transaction and is selected because it looks clean;
5. correction overwrites original record;
6. reconciliation history is rewritten to remove earlier ambiguity;
7. replay ledger and evidence ledger disagree on whether request existed;
8. currentness proof references ledger generation newer than restored store;
9. learner deletes evidence that reduced its score;
10. evaluator-only receipt forged by learner schema mimicry;
11. benchmark packet drops failed hostile profile;
12. archive compaction removes request identity needed for replay safety;
13. tombstone is missing so intentional deletion looks like unknown loss;
14. evidence partitions are selectively restored;
15. hash/digest verifies record bytes but continuity before it is missing;
16. timestamp order is trusted despite known clock discontinuity;
17. replica lag is mistaken for complete state;
18. corruption is repaired by replacing original with reconstructed guess;
19. export preserves files but loses supersession/provenance graph;
20. cleanup job deletes unresolved ambiguity as "old."

## 32. Evidence ceiling

This research does not choose:
- a database;
- a cryptographic signature scheme;
- a Merkle implementation;
- retention durations;
- replication technology;
- external notarization.

It establishes the integrity/completeness properties required before evidence can support stronger claims.

## 33. Research disposition

The practical rule is:

> Evidence is trustworthy only when both the records and the required history around them are integrity- and completeness-aware.

No evidence-ledger implementation, storage design, machine access/write, commissioning, recovery action, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
