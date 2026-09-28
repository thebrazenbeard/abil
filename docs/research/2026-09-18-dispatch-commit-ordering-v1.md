# Dispatch Commit Ordering V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #13 — effect-intent binding and anti-replay
- Draft PR #14 — replay-ledger anti-rollback
- Draft PR #12 — currentness snapshot/revalidation
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`

## Purpose

Effect intent can be exact.
Admission can be current.
Replay state can be monotonic.

A crash-order question still remains:

> What durable transaction state must exist before a physical effect can become possible, and how is recovery handled if failure occurs at any point around that boundary?

Two naïve orderings are both unsafe:

### Persist after dispatch

1. send physical command;
2. target may act;
3. persist "consumed/dispatched";
4. crash between 2 and 3.

Risk:
request can look unused after restart and be duplicated.

### Persist consumed before dispatch

1. persist "consumed";
2. send physical command;
3. crash between 1 and 2.

Risk:
a request that never reached the target appears definitely executed/consumed.

The safe contract needs an intermediate durable state that means:

> This request has crossed the point where a physical effect may occur; replay is no longer allowed without reconciliation.

## 1. Transaction states

A future transaction state machine could distinguish:

- `ADMITTED`
- `DISPATCH_RESERVED_DURABLE`
- `DISPATCH_ATTEMPTED`
- `TARGET_ACCEPTED`
- `COMPLETED_KNOWN`
- `FAILED_KNOWN_NO_EFFECT`
- `FAILED_POSSIBLE_EFFECT`
- `UNKNOWN_AMBIGUOUS_EFFECT`
- `CANCELLED_BEFORE_DISPATCH`

Exact naming is open.

The key distinction is that `DISPATCH_RESERVED_DURABLE` is not "completed."

It means:
- the request may imminently reach the target;
- replay must not occur blindly;
- recovery must reconcile before another physical attempt.

## 2. Pre-dispatch durable reservation

Before issuing a non-idempotent physical command, future implementation should durably record at least:

- request ID;
- effect-intent digest;
- decision/admission receipt digest;
- deployment identity;
- authority epoch;
- ownership generation;
- target/output namespace;
- precondition/currentness cut;
- dispatch-reservation sequence/generation;
- time/order;
- writer identity;
- target correlation/session identity where available.

If the durable reservation cannot be established:
do not dispatch.

## 3. Reservation semantics

A durable reservation means:

- this logical request is no longer freely reusable;
- a crash may have occurred before or after physical send;
- recovery must conservatively treat effect outcome as unresolved unless evidence proves no send/effect occurred;
- another request with same ID must not be admitted as new intent;
- a semantically equivalent replacement request must consider the unresolved reservation.

Reservation itself does not claim the target acted.

## 4. Dispatch attempt linkage

The actual dispatch attempt should bind:

- reservation ID/digest;
- exact request/effect intent;
- target correlation identity;
- local attempt sequence;
- send timestamp;
- writer/connection/session identity.

A dispatch attempt without a valid durable reservation is invalid for protected effects.

## 5. Crash windows

### Crash A — before reservation

No physical dispatch is permitted.

Safe outcome:
request remains unconsumed and may be reconsidered under fresh admission.

### Crash B — after durable reservation, before known send

Outcome:
`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` unless independent evidence proves send never occurred.

Do not automatically retry.

### Crash C — after send, before acknowledgement

Outcome:
ambiguous until reconciled.

### Crash D — after target acceptance, before local receipt persistence

Outcome:
possible/likely effect; replay blocked.

### Crash E — after known completion, before final local status update

If durable target receipt or dedup state proves completion, reconcile to completed.
Otherwise remain conservative/ambiguous.

## 6. Known-no-effect proof

A reserved request may return to a safely retryable state only if evidence proves no physical effect could have occurred.

Potential proof examples:

- target explicitly rejected before execution;
- transport/session contract proves bytes never crossed dispatch boundary;
- target dedup/readback proves request not accepted;
- qualified gateway journal proves no send occurred.

Local absence of an acknowledgement is not proof.

## 7. Idempotent exception

For a mechanically idempotent operation under the exact target contract, retry semantics may be less restrictive.

The idempotency proof should bind:

- exact operation;
- exact parameters;
- target semantics;
- duplicate behavior;
- relevant state preconditions;
- authority/ownership generation;
- dedup/session assumptions.

"Usually harmless to retry" is not sufficient.

## 8. Target-side transaction support

If the target protocol supports prepare/commit, dedup, transaction IDs, or readback, future implementations may use those capabilities.

Examples:
- prepare then commit;
- durable target request ID;
- exactly-once target dedup;
- commit acknowledgement;
- query-by-request-ID.

The ABIL contract should still preserve local evidence of:
- what was admitted;
- what was reserved;
- what target transaction was used;
- what result was observed.

## 9. Two-phase style interaction

Some targets may permit a two-phase pattern:

1. `PREPARE` target-side intent without physical effect;
2. persist local reservation and target prepare receipt;
3. `COMMIT` physical effect;
4. persist result.

This can narrow ambiguity.

It is not universally available and is not required by this research.

## 10. Protocols without transactional support

Many industrial protocols cannot provide atomic exactly-once physical semantics.

For those systems, the contract should admit the limitation explicitly.

Required fallback posture may include:

- durable local reservation before send;
- target correlation where available;
- readback/reconciliation;
- no blind retry after uncertain send;
- operator/technician recovery for unresolved effects;
- operation-specific safe retry rules only when independently proven.

"Exactly once" must not be claimed when the protocol cannot support it.

## 11. Write-ahead durability

A future implementation may use a write-ahead log or equivalent.

Safety requirement:

> Before the system crosses the software boundary where a non-idempotent physical effect can become possible, durable state must already make blind replay impossible.

Durability should survive:
- process crash;
- host reboot;
- storage/controller restart according to qualified failure assumptions.

## 12. Durability acknowledgement

The writer should not assume a database/API call is durable merely because it returned success.

Qualification may need to establish:
- transaction commit semantics;
- fsync/storage guarantees;
- replication commit point;
- WAL durability;
- power-loss behavior;
- corruption detection.

This research does not mandate one database/storage technology.

## 13. Replication / HA

In replicated writers:

- reservation must reach the qualified durable commit point before dispatch;
- failover must observe the reservation;
- a standby missing the reservation must not dispatch the same request;
- quorum/leader generation should bind the reservation where applicable.

A primary may not send first and replicate replay state later if failover can duplicate the effect.

## 14. Storage failure after reservation

If durable replay state becomes unavailable after reservation:

- do not assume request unused;
- do not reinitialize empty state;
- affected writes remain blocked until replay state is reconciled or target dedup independently guarantees no duplicate effect.

Read-only operation may continue if otherwise qualified.

## 15. Cancellation

A request can become `CANCELLED_BEFORE_DISPATCH` only if evidence proves it did not cross the physical dispatch boundary.

If cancellation races with send:
outcome may be ambiguous.

"User clicked cancel" is not enough to prove no effect.

## 16. Timeout

Timeout is a local observation, not an execution result.

After a durable reservation:
- timeout does not return request to unused;
- timeout does not authorize new attempt;
- target/state reconciliation is required.

## 17. Batches

For ordered/atomic batches:

- reserve exact batch subject durably;
- preserve per-member dispatch state;
- commit/dispatch ordering should be explicit;
- crash after member N must not restart from member 1 blindly;
- remaining members require fresh/revalidated semantics unless the batch protocol itself guarantees atomicity.

## 18. Bounded-repeat / sessions

For bounded-repeat/session authorization:

- durable counters/budgets should be decremented/reserved before corresponding physical effects can occur;
- crash must not restore consumed budget;
- failed reservation that definitely caused no effect may be recovered under exact rules;
- ambiguous reservations consume budget conservatively until reconciled.

## 19. Decision/currentness integration

PR #12 revalidation should occur before or as part of the dispatch reservation.

If required state changes after reservation but before send:
the transaction needs an exact rule.

Conservative default:
- invalidate dispatch;
- retain reservation as no-effect/ambiguous until evidence establishes whether send occurred;
- create a new decision if retry is later permitted.

## 20. Effect-intent integration

PR #13's exact effect-intent digest should be bound into the reservation.

A reservation for intent X cannot be reused for intent Y.

Any parameter mutation after reservation invalidates the request and requires a new transaction subject.

## 21. Replay-ledger integration

PR #14 replay state should treat `DISPATCH_RESERVED_DURABLE` as non-replayable by default.

Restore must not regress:
- reserved -> unused;
- dispatched -> unused;
- possible-effect -> unused;
- consumed -> unused.

## 22. Hostile research cases

A future implementation should fail closed on at least:

1. physical send occurs before durable reservation;
2. crash after send but before ledger commit makes request unused;
3. durable "completed" written before send and crash occurs before effect;
4. reservation lost on failover;
5. primary sends before replication quorum;
6. DB returns success but write is lost on power failure;
7. timeout resets reserved request to unused;
8. cancel races with send and is treated as known-no-effect;
9. target rejects after partial physical action but system records no-effect;
10. batch partially executes and restarts from first member;
11. session counter decremented after send and rolls back on crash;
12. state changes after reservation and old request sends without revalidation rule;
13. reservation effect-intent digest differs from actual payload;
14. target correlation ID changes after reservation;
15. old reservation is reused for new authority/ownership generation;
16. local state says unsent while target durable dedup says accepted;
17. target dedup is assumed durable but resets on reboot;
18. unavailable replay ledger causes system to initialize empty and resume writes.

## 23. Evidence ceiling

This research defines failure semantics and ordering invariants only.

It does not prove:
- exactly-once execution;
- any protocol's transactional guarantees;
- storage durability;
- target deduplication;
- hardware power-loss behavior.

Those are future implementation/qualification subjects.

## 24. Research disposition

The practical rule is:

> Durable replay state must cross its conservative "effect may occur" commit point before the physical effect can become possible.

No dispatch-commit implementation, storage/WAL implementation, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
