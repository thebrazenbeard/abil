# Replay Ledger Anti-Rollback V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #8 — support/recovery currentness
- Draft PR #13 — effect-intent binding and anti-replay
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`

## Purpose

ABIL already protects authority-bearing state from rollback and treats unresolved physical command outcomes as durable.

A separate replay-state problem remains:

> What prevents restore of an older non-authority transaction/replay ledger from making an already consumed same-generation request appear unused again?

Authority may legitimately remain current across a process/storage recovery.

Therefore authority anti-rollback alone does not prove replay-state monotonicity.

## 1. Replay state is not ordinary cache

For physical-effect requests, replay/dedup state can become safety-relevant operational evidence.

At minimum retain durable state for requests that are:

- admitted but not yet dispatched;
- dispatched;
- accepted by target;
- known completed;
- known failed;
- failed after possible execution;
- unknown/ambiguous;
- cancelled before dispatch;
- superseded by recovery procedure;
- intentionally repeatable under a bounded-repeat/session contract.

A replay ledger must not be treated as disposable performance cache when losing it can enable duplicate physical effects.

## 2. Request consumption state

For a `SINGLE_EFFECT` request, define conceptually:

- `UNUSED`
- `RESERVED_FOR_DISPATCH`
- `DISPATCHED`
- `CONSUMED_KNOWN_RESULT`
- `CONSUMED_POSSIBLE_EFFECT`
- `CANCELLED_BEFORE_EFFECT`

Once a request reaches:
- `DISPATCHED`,
- `CONSUMED_KNOWN_RESULT`, or
- `CONSUMED_POSSIBLE_EFFECT`;

it must not return to `UNUSED` through process restart, backup restore, storage replacement, or ordinary state rollback.

## 3. Monotonic replay generation

A future replay ledger may need a monotonic generation or append-only sequence independent from ordinary backups.

Potential concept:

`ReplayLedgerGeneration`

Each durable consumption/event update advances or appends state.

A restored snapshot whose replay generation is behind the protected/current replay generation should not silently become authoritative.

This research does not choose storage technology.

## 4. Same-authority-generation restore case

Critical hostile case:

1. authority epoch = A12;
2. ownership generation = O7;
3. request R1 is admitted and executed;
4. R1 becomes consumed in replay state;
5. appliance/storage is restored from snapshot S0 taken before R1;
6. authority still legitimately remains A12/O7;
7. S0 says R1 is unused.

Authority checks alone cannot detect this replay-state rollback.

Expected:
- reject restored replay state as stale/incomplete;
- or rely on independently durable target-side dedup proving R1 cannot produce another physical effect;
- or require reconciliation before any affected write path resumes.

## 5. Replay ledger subject

A future replay state subject should bind:

- deployment identity;
- authority domain;
- authority epoch;
- ownership generation;
- writer/gateway identity;
- ledger generation;
- canonical request identity;
- effect-intent digest;
- consumption state;
- execution-attempt identity;
- target correlation identity;
- relevant decision receipt;
- timestamps/order;
- result/ambiguity state;
- supersession/recovery links.

Exact fields depend on the target contract.

## 6. Append-only versus mutable implementation

The safety requirement can be satisfied by different implementations:

- append-only journal;
- monotonic counter plus durable request set;
- write-ahead log;
- database transaction log;
- protected remote ledger;
- target-side deduplication;
- replicated quorum state;
- hardware-backed monotonic state.

The mechanism is not prescribed.

The invariant is:

> Restore cannot make a request more reusable than it was before failure.

## 7. Restore admissibility

Before write-capable recovery resumes, future implementation should establish one of:

### `REPLAY_STATE_CURRENT`

Restored replay ledger is proven current and complete.

### `REPLAY_STATE_RECONCILED`

Local state was stale/incomplete but reconciled against independent durable evidence sufficient to reconstruct safe consumption state.

### `TARGET_DEDUP_PROVEN`

Target independently guarantees duplicate submission of affected logical requests cannot cause an extra physical effect.

Otherwise:

`REPLAY_STATE_UNKNOWN`

should block affected writes.

## 8. Missing replay state

Missing ledger is not equivalent to no prior requests.

If replay state is lost:

- do not initialize an empty ledger and resume;
- do not assume all request IDs are unused;
- do not infer non-execution from absent receipts;
- do not silently rotate request namespace unless target/recovery contract proves old requests cannot reappear or collide.

Missing evidence should fail closed for affected write scope.

## 9. Backup/snapshot relationship

A backup should record the replay-ledger cut it contains.

Potential fields:

- backup ID;
- creation time;
- replay-ledger generation/digest;
- authority epoch;
- ownership generation;
- last durable request/event position.

On restore, compare backup replay state against the current protected/reconciled replay subject.

A byte-valid backup may still contain stale replay state.

## 10. Storage replacement

Replacing storage hardware must not reset replay history.

Recovery should prove:

- ledger state restored/reconciled;
- ledger generation not regressed;
- consumed request identities preserved;
- unresolved ambiguity preserved;
- target dedup/session state reconciled where applicable.

If not provable, affected write paths remain blocked.

## 11. Target-side deduplication

Target-side dedup can reduce dependence on local replay state only if the exact target contract proves:

- dedup key identity;
- dedup retention window;
- persistence across target restart;
- persistence across target replacement;
- behavior on duplicate same-intent request;
- behavior on same request ID with changed intent;
- authority/ownership generation scoping;
- expiry/garbage-collection semantics.

A transient in-memory target cache is not durable proof.

## 12. Garbage collection

Replay state cannot grow forever without policy.

Future garbage collection should remove request history only when a qualified rule proves replay is no longer possible or harmful.

Potential conditions:

- request namespace/generation permanently retired;
- authority/ownership generation superseded and old writer fenced;
- target dedup retention guarantees expiry safety;
- maximum network/session replay window exceeded under qualified assumptions;
- physical recovery procedure establishes no delayed effect/receipt remains relevant.

Deletion policy itself is part of the replay contract.

## 13. Request namespace rotation

Rotating request IDs or writer instance IDs after recovery does not automatically solve replay.

Old requests may still:
- arrive late;
- be retried by stale processes;
- exist in restored queues;
- receive delayed acknowledgements;
- collide under reused namespaces.

Namespace rotation must be paired with fencing/reconciliation semantics.

## 14. Multi-writer / HA systems

If multiple writer instances can fail over, replay state must be shared or otherwise coordinated sufficiently to prevent duplicate physical effects.

A standby writer must not see a request as unused merely because the primary's local ledger had not replicated.

Failover semantics should bind:

- leader/writer generation;
- durable commit point;
- request consumption state;
- ownership transfer;
- target dedup state.

## 15. Batch replay state

For an atomic/ordered batch, ledger state should preserve per-member status.

Example:

- A completed;
- B dispatched/unknown;
- C not dispatched.

Restore must not collapse that to:
- batch unused,
- batch completed,
- or restart from A,

unless exact batch protocol proves it safe.

## 16. Session-scoped decisions

For bounded-repeat/session authorization, replay state should track:

- total count consumed;
- rate/window counters;
- effect budget remaining;
- exact operation family;
- parameter bounds;
- last durable sequence position;
- expiry/revocation state.

Restore must not replenish consumed budget by rolling counters backward.

## 17. Currentness / snapshot integration

PR #12 currentness revalidation should treat replay-ledger generation/currentness as a required dispatch dependency when replay state affects safety.

A decision made against replay ledger L10 should not dispatch against restored L8.

A changed replay generation can require revalidation even if authority/deployment/artifact subjects remain unchanged.

## 18. Effect-intent integration

PR #13 effect-intent binding should link:

`request_id -> effect_intent_digest -> replay_consumption_state`

If same request ID appears with different intent:
reject conflict.

If same request ID + same intent appears after consumption:
apply exact idempotency/dedup contract; do not create a new physical attempt by default.

## 19. Recovery integration

PR #8 support/recovery currentness should consider replay-ledger durability/reconciliation part of recovery qualification for write-capable modes.

A recovery procedure that restores the machine but loses consumed-request evidence is not fully qualified for write resumption.

It may still qualify for:
- read-only diagnostics;
- non-operating fallback;
- separately safe manual inspection.

## 20. Hostile research cases

A future implementation should reject or fail closed on at least:

1. restore pre-execution ledger after completed same-generation request;
2. restore pre-dispatch ledger after possibly executed ambiguous request;
3. initialize empty replay ledger after database loss;
4. rollback session counter and regain consumed effect budget;
5. failover to standby missing latest request consumption;
6. target dedup cache resets on target restart but local system assumes it persists;
7. old request arrives after local garbage collection;
8. request-ID namespace rotates but stale writer remains able to send;
9. batch restores as unused after partial execution;
10. same request ID reused with changed effect intent;
11. replay ledger generation behind backup metadata but accepted;
12. authority remains current, so stale replay ledger is incorrectly accepted;
13. storage replacement loses replay ledger while preserving authority state;
14. local ledger says consumed but target indicates unknown and system downgrades to unused;
15. garbage collection removes ambiguous request before reconciliation;
16. bounded-repeat counter rolls backward after restore;
17. active/passive writer failover duplicates last physical effect;
18. decision receipt validated against L10 is dispatched after rollback to L8.

## 21. Relationship to authority anti-rollback

Authority anti-rollback answers:

> Is this principal still allowed to hold write authority?

Replay-ledger anti-rollback answers:

> Given that authority may still be valid, which logical physical-effect requests have already consumed their allowed execution?

Both are required.

Neither substitutes for the other.

## 22. Research disposition

The practical rule is:

> Replay/consumption state for physical effects must not become less restrictive after recovery.

No replay-ledger implementation, storage design, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
