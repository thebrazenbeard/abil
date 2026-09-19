# Dispatch Reservation Protected Commit Barrier V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #15 predecessor exact head `88f1a232a7265e8713e4564260b28e35cf53369e`.

This companion reconciles Dispatch Commit Ordering V1 with the strengthened PR #14 replay-ledger anti-rollback model.

V1 requires a durable `DISPATCH_RESERVED_DURABLE` state before a non-idempotent physical effect can become possible.

The remaining crash seam is:

> A reservation may be durably written to local storage yet still be absent from the separately protected current replay cut. If physical dispatch proceeds before that protected cut commits the reservation, a failure/restore can resurrect a replayable pre-reservation state.

Therefore "durable local write before send" is necessary but not sufficient.

## 1. Protected reservation commit barrier

Before a non-idempotent physical effect can become possible, one of the exact operation profile's qualified barriers MUST be established:

### A. protected replay reservation commit

The reservation is:
- durably persisted;
- included in the exact replay checkpoint/cut;
- committed by the current `ReplayLedgerHeadWitness`;
- read back/verified under the exact request/effect-intent scope.

or:

### B. independently durable target-side prepare/dedup barrier

The target has durably established a request/transaction subject that independently prevents duplicate physical effect under a currently qualified target contract.

A merely local write that has not crossed either barrier does not satisfy the protected dispatch prerequisite.

## 2. Reservation commit receipt

A future `DispatchReservationCommitReceipt` or mechanically equivalent subject SHOULD bind:

- request ID;
- exact effect-intent digest;
- deployment/target/output scope;
- authority epoch;
- ownership/writer generation;
- admission/currentness cut digest;
- replay checkpoint/cut digest;
- ReplayLedgerHeadWitness digest;
- reservation state;
- target prepare/dedup subject if used;
- target correlation/session identity;
- commit mechanism/profile;
- durable-commit verification result;
- verifier identity/profile;
- immutable receipt digest.

The receipt does not claim physical effect occurred.

It proves the request crossed the no-blind-replay barrier before dispatch.

## 3. Local commit success is not sufficient by itself

A database/API/filesystem call returning success may prove only local persistence semantics.

If the operation profile requires the replay-head witness to survive:
- host loss;
- storage restore;
- failover;
- replica promotion;

then dispatch MUST wait until that stronger protected commit condition is established.

Examples of insufficient evidence by itself:
- process-memory state;
- buffered file write;
- un-fsynced local WAL;
- local DB commit not included in qualified replication/witness cut;
- async replica enqueue;
- local checkpoint not committed by the replay witness.

## 4. Reservation and witness ordering

For a protected replay-based barrier, conceptual ordering is:

1. exact effect intent validated;
2. current admission/revalidation cut validated;
3. reservation record constructed;
4. reservation durably appended;
5. replay checkpoint/cut including reservation constructed;
6. ReplayLedgerHeadWitness advances to commit that exact cut;
7. exact reservation/head readback succeeds;
8. physical dispatch may become possible.

If step 6 or 7 fails:
- do not dispatch;
- preserve candidate reservation as historical/pending evidence;
- reconcile before retry.

## 5. Crash windows with protected barrier

### Crash A — before protected reservation commit

No physical dispatch is permitted.

The request may be reconsidered later under fresh admission if no independent target prepare/effect barrier exists.

### Crash B — protected reservation committed, before physical send

The request is no longer freely reusable.

Recovery must determine whether send occurred.

Default:
`UNKNOWN_AMBIGUOUS_EFFECT`
or a narrower profile-specific pre-send reserved state that still blocks blind reuse.

### Crash C — after send

Replay remains blocked until reconciliation/qualified idempotency/dedup semantics resolve the exact request.

The protected replay witness must not regress below the reservation.

## 6. Target-side prepare as an alternative barrier

A target `PREPARE` can substitute for replay-head commit only if the exact target contract proves:

- PREPARE itself causes no protected physical effect;
- prepared request identity/effect intent is durably stored;
- duplicate prepare/commit semantics are defined;
- target restart persistence is qualified;
- target replacement invalidates the proof unless separately reconciled;
- commit/query/cancel semantics are exact;
- stale writer/session behavior is fenced;
- current target-dedup/transaction proof is available.

If these predicates are not established, PREPARE is not a qualified barrier.

## 7. Target-side dedup after dispatch is not automatically a pre-dispatch barrier

A target may support duplicate suppression during/after send.

That does not necessarily prove the local request reservation survived before the first send.

If replay safety relies on target dedup instead of protected replay commit, the target-dedup proof must be current and strong enough for:
- exact request identity;
- exact target;
- persistence;
- restart;
- replacement;
- retention;
- session/namespace scope.

PR #14 V2 currentness rules apply.

## 8. Admission/currentness race

PR #12 revalidation should bind the state cut used to authorize the reservation.

After protected reservation commit but before send, if a required admission/currentness dependency changes:

default:
- do not send;
- preserve the committed reservation;
- append cancellation/no-send/ambiguity evidence as exact protocol permits;
- require a fresh request/decision subject for later retry unless the recovery profile explicitly permits reuse.

A stale admission decision cannot be rescued by the fact that reservation is durable.

## 9. Authority/ownership loss after reservation

If authority or ownership is revoked/transferred after protected reservation commit but before send:

- reservation remains historical consumed/reserved evidence;
- send is blocked;
- new authority does not inherit the old reservation as a bearer token;
- later reconciliation determines whether old writer could have dispatched.

The reservation's historical truth survives authority change.

## 10. Payload binding at send

Immediately before physical send, bind/verify:

- request ID;
- effect-intent digest;
- exact encoded payload digest or deterministic encoding profile;
- target identity;
- current writer/session identity;
- reservation commit receipt;
- applicable admission/currentness cut.

A valid reservation for intent X MUST NOT authorize payload Y.

## 11. Dispatch transport handoff boundary

The exact operation profile must define when "physical effect can become possible."

Examples:
- bytes handed to an OS/socket may be too early or too late depending on transport semantics;
- gateway durable send queue insertion may itself cross the effect-possible boundary;
- target acceptance/prepare may define a stronger boundary.

The system must not use a convenient software call boundary that understates the real possibility of effect.

## 12. Queued and buffered transports

If commands can persist in:
- OS buffers;
- gateway queues;
- broker queues;
- fieldbus adapter memory;
- retrying transport middleware;

then recovery must treat queued-but-unconfirmed commands as possible future effects.

The protected reservation remains non-replayable until those queues are reconciled/fenced/drained under exact profile semantics.

## 13. Failover

A standby may dispatch a reserved request only if it proves:

- current authority/ownership;
- current ReplayLedgerHeadWitness including the reservation;
- exact request/effect-intent match;
- no unresolved prior send possibility;
- current target session/dedup state;
- operation-specific retry eligibility.

Failover does not turn a protected reservation back into UNUSED.

## 14. Batch reservations

For batches, protected commit should bind:
- exact batch subject;
- exact members/order;
- per-member reservation state;
- atomicity/partial-execution profile;
- replay checkpoint containing the whole required pre-dispatch state.

If the target cannot guarantee atomic batch behavior, per-member effect-possible boundaries remain explicit.

## 15. Bounded-repeat/session operations

A protected commit must reserve/decrement:
- effect count/budget;
- rate/window token;
- session sequence;
- exact operation/parameter scope

before the corresponding physical effect can become possible.

A crash must not replenish the budget by restoring a pre-reservation cut.

## 16. Known-no-effect recovery

A protected reservation can later support a new attempt only if the exact recovery profile establishes KNOWN_NO_EFFECT or an independently qualified safe reuse rule.

Acceptable proof may include:
- target durable log proves never committed;
- transport/gateway evidence proves bytes never crossed effect boundary;
- target prepared subject was cancelled before commit and contract proves no effect;
- another qualified mechanism.

Local absence of acknowledgement is not sufficient.

## 17. Evidence-ledger cross-binding

The protected replay reservation commit SHOULD cross-bind the current PR #18 evidence-ledger cut where evidence completeness is required.

After dispatch, evidence history should be able to prove:
- reservation existed before effect boundary;
- exact attempt/correlation identity;
- later receipt/ambiguity/reconciliation records.

A replay witness alone proves replay currentness, not evidence-history completeness.

## 18. No exactly-once overclaim

Even with:
- protected replay reservation;
- durable witness;
- target dedup;
- exact ordering;

do not claim exactly-once physical execution unless the complete target/protocol semantics prove it.

This design primarily proves:
- no blind replay after the effect-possible barrier;
- conservative crash recovery.

## 19. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. local DB reservation commits but replay witness does not advance; dispatch must not occur.
2. reservation is asynchronously replicating when primary sends and crashes; failover cannot replay from stale replica.
3. replay witness commits reservation; crash occurs before send; request remains non-reusable pending qualified no-send proof.
4. target PREPARE is assumed no-effect but device can actuate during prepare; barrier invalid.
5. target dedup resets on reboot after being used as substitute barrier; dedup proof becomes stale.
6. admission is revoked after reservation commit but before send; dispatch blocks.
7. payload parameters change after reservation; send rejects intent mismatch.
8. gateway queue accepts command after reservation, host crashes before receipt; queued command remains possible effect.
9. standby sees reservation but cannot exclude prior send; no blind duplicate.
10. reservation commit survives but evidence ledger is stale; replay remains conservative while evidence-completeness claim downgrades.
11. batch reservation commits only first members but system treats whole batch protected; reject incomplete barrier.
12. bounded-repeat budget is decremented only after send; crash can replenish it; reject ordering.
13. target address same but physical device replaced; old prepare/dedup proof cannot transfer.
14. current replay cut exists but wrong deployment/output scope; reject.
15. writer uses old reservation after ownership generation transfer; reject.
16. local API says fsync success but qualified durability profile requires quorum/witness not reached; no dispatch.

## 20. Practical rule

> Before a non-idempotent physical effect can become possible, ABIL must establish a protected no-blind-replay barrier for that exact request: either the current replay-head witness has committed the durable reservation, or an independently qualified target-side transaction/dedup mechanism provides an equivalent stronger barrier.

## 21. Authority boundary

This document does not:
- implement dispatch/WAL/storage;
- create replay witness infrastructure;
- configure target dedup/transactions;
- send machine commands;
- perform failover/recovery;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
