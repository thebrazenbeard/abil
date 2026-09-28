# Replay Ledger Protected Head Witness and Dedup Currentness V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #14 predecessor exact head `fc9846e3eb82e3b0c8eccbf42769b09ba7eaaa2c`.

This companion closes the remaining restore/failover anti-rollback seam in Replay Ledger Anti-Rollback V1.

V1 correctly requires replay/consumption state to remain monotonic and blocks write resumption when replay state is unknown.

The missing structural predicate is:

> What independently proves which replay-ledger cut is current after restore, failover, replica lag, or storage replacement?

A locally highest replay generation is not enough when the local replay store itself may be stale.

## 1. Replay state identity and replay currentness are separate

A replay record may be internally valid and historically true while the local replay ledger is stale.

Therefore distinguish:
- request-consumption record integrity;
- replay-ledger continuity;
- current replay-ledger head;
- target-dedup currentness;
- write-scope admissibility.

A valid old replay prefix is not automatically current.

## 2. ReplayLedgerHeadWitness

A future replay ledger should bind a separately protected current-head subject:

`ReplayLedgerHeadWitness`

or mechanically equivalent anti-rollback commit record.

It binds at least:
- deployment/authority domain;
- exact replay-ledger generation/cut;
- current ledger root/checkpoint digest;
- predecessor/root lineage digest;
- canonical request namespace/profile;
- writer/ownership generation scope;
- witness sequence/generation;
- witness authority/profile;
- commit/verification evidence;
- immutable witness digest.

The witness rollback domain MUST be sufficiently independent from the replay storage it judges that restoring the replay database cannot silently restore the witness to the same stale point.

## 3. Local maximum replay generation is not proof of currentness

Do not infer current replay state solely from:
- highest local replay generation;
- highest local request sequence;
- newest backup timestamp;
- longest local log;
- most complete-looking local store;
- authority epoch still being current.

These may identify a candidate replay cut.

They do not prove that no later replay consumption exists elsewhere.

## 4. Current replay-state predicate

A replay cut is current for affected write scope only when:

- replay-ledger integrity/continuity valid;
- protected ReplayLedgerHeadWitness resolves;
- local/reconciled replay cut matches the exact witnessed head;
- no unresolved replay fork/conflict exists;
- required writer/ownership generation binding matches;
- target-dedup assumptions are current where relied upon;
- replay/evidence-ledger cross-check requirements pass where configured.

Otherwise write scope is:
`REPLAY_STATE_UNKNOWN`
or a stronger fail-closed disposition.

## 5. Missing witness fails closed

If replay-head witness is:
- unavailable;
- unverifiable;
- stale;
- scope-mismatched;
- conflicting;
- unable to establish one current replay cut;

then affected non-idempotent writes remain blocked unless an independently qualified target-dedup proof makes replay impossible for the exact request scope.

Do not initialize a fresh empty replay ledger as a substitute.

## 6. Replay checkpoint

A `ReplayLedgerCheckpoint` or equivalent may bind:

- replay domain;
- ledger generation;
- request namespace;
- start/end durable positions;
- predecessor checkpoint digest;
- current request-state root/digest;
- unresolved ambiguity set digest;
- bounded-repeat/session counter state;
- writer/ownership generation;
- evidence-ledger cross-reference;
- canonicalization profile;
- checkpoint digest.

Checkpoint identity alone does not make it current.

## 7. Restore procedure

A future replay restore should conceptually:

1. load restored replay bytes as candidate historical state;
2. independently resolve ReplayLedgerHeadWitness;
3. compare candidate cut to witnessed current cut;
4. fetch/reconcile missing newer replay records as permitted;
5. preserve all consumed/ambiguous/bounded-repeat counters;
6. cross-check target-dedup state where relied upon;
7. cross-check evidence-ledger records where required;
8. only then issue current replay-state receipt.

A backup's own replay generation is evidence of backup contents, not authority that it is current.

## 8. Failover / HA

A standby writer MUST NOT assume its local replay state is current merely because:
- authority/ownership transfer succeeded;
- its replica is internally consistent;
- it has a high generation.

Before write resumption it must reconcile against:
- ReplayLedgerHeadWitness;
- exact ownership/writer generation;
- required evidence/target dedup state.

Availability does not outrank replay currentness.

## 9. Replay fork handling

If two replay replicas present incompatible successors from the same witnessed predecessor and no protected commit establishes one unique current cut:

`REPLAY_STATE_CONFLICTING`.

Do not:
- union request states automatically;
- pick the more restrictive or more permissive copy by heuristic;
- choose the newest wall-clock timestamp;
- select whichever replica allows progress.

Explicit reconciliation must preserve conflict provenance.

## 10. More restrictive merge is not automatically safe

It may seem safe to merge replay states by choosing the most restrictive consumption state.

That is not universally valid.

Example:
- one branch records request R as DISPATCHED with target correlation X;
- another records a different request or different intent under the same ID.

A blind "take consumed" merge may hide identity conflict or target ambiguity.

Reconciliation must bind:
- exact request ID;
- effect-intent digest;
- execution-attempt identity;
- correlation identity;
- provenance of each branch.

Restriction ordering is only valid when the state machine/profile proves the states are about the same exact request subject.

## 11. Target-side dedup is its own currentness subject

`TARGET_DEDUP_PROVEN` is not a static product property.

A future target-dedup proof should bind:
- target identity;
- firmware/software/configuration identity;
- dedup namespace/profile;
- dedup key semantics;
- retention window;
- persistence class;
- restart behavior;
- replacement behavior;
- current session/generation;
- currentness evidence;
- exact request/operation scope;
- qualification profile.

If target restart/replacement/configuration invalidates the dedup guarantee, local replay state cannot continue relying on the old proof.

## 12. TargetDedupCurrentnessReceipt

A future receipt may bind:
- target subject;
- dedup profile;
- current target generation/session;
- persistence/restart evidence;
- retention/expiry boundary;
- qualification evidence;
- time source where retention is temporal;
- verifier identity/profile;
- final disposition;
- immutable digest.

This receipt does not grant write authority.

It only proves the bounded dedup property used by replay admission.

## 13. Dedup retention and time uncertainty

If target dedup is valid only for a time window, the window must bind qualified PR #24-style time evidence.

Clock uncertainty must not silently extend dedup retention.

If the dedup window may have expired, target-side dedup can no longer substitute for current replay-ledger proof unless another profile establishes safety.

## 14. Replay namespace rotation

Namespace rotation is safe only if the profile proves:
- old writers are fenced;
- old queued requests cannot reappear;
- target dedup/session namespaces cannot collide;
- delayed receipts are bound to the historical namespace;
- current ReplayLedgerHeadWitness advances coherently to the new namespace subject.

Changing a string prefix is not anti-replay.

## 15. Bounded-repeat/session counters

For repeatable/session grants, replay currentness includes:
- consumed count;
- remaining budget;
- rate/window counters;
- exact operation family;
- parameter bounds;
- session generation;
- expiry/revocation state.

Rollback of any counter to a more permissive state is replay rollback even if request IDs themselves do not repeat.

## 16. Replay and evidence ledger remain distinct axes

PR #18 evidence ledger may prove transaction/effect history.

PR #14 replay ledger controls whether logical effect requests remain reusable.

Cross-bind enough to detect:
- replay says UNUSED while evidence shows dispatch/ambiguity;
- replay says CONSUMED but evidence history is missing;
- one store advanced beyond the other;
- restore recovered only one store.

Neither silently repairs the other.

## 17. Replay currentness and authority remain distinct

A current authority epoch does not prove current replay state.

A current replay state does not grant authority.

A write path requiring both must bind both exact current subjects in one operation cut.

## 18. Ambiguous outcome permanence

Once a request crosses the profile's "effect may have occurred" boundary, restoring older state cannot make it UNUSED unless an independent reconciliation produces qualified KNOWN_NO_EFFECT evidence for that exact request/attempt.

Absence of receipt after restore is not KNOWN_NO_EFFECT.

## 19. Garbage collection

Garbage collection must preserve replay safety through a qualified proof.

A future GC receipt should bind:
- exact replay cut;
- exact retired request/namespace scope;
- reason;
- target-dedup/expiry/fencing evidence;
- time/currentness evidence where required;
- unresolved ambiguity check;
- resulting replay cut/head witness.

Deleting old replay rows does not erase historical evidence that the request was consumed.

## 20. Replay current-cut receipt

A future `ReplayStateCurrentCutReceipt` may bind:
- replay domain;
- ReplayLedgerHeadWitness;
- exact replay checkpoint/cut;
- request namespace/profile;
- ownership/writer generation;
- target-dedup currentness receipt where relied upon;
- evidence-ledger cross-check receipt where required;
- conflict/gap disposition;
- verifier identity/profile;
- final replay-currentness disposition;
- immutable digest.

A caller-supplied `CURRENT` label is insufficient.

## 21. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. restore R8 while protected replay witness proves R10; R8 cannot become current.
2. restore replay DB and local resolver from same old backup; missing independent witness blocks writes.
3. authority remains current A12 while replay witness detects rollback; writes remain blocked.
4. failover replica is internally valid but behind witnessed head; no write resumption.
5. two replay successors conflict under same generation; do not pick by timestamp/locality.
6. same request ID appears with different intent on two branches; "most restrictive state wins" must not hide identity conflict.
7. target dedup proof predates target restart that clears cache; TARGET_DEDUP_PROVEN becomes stale.
8. target replacement at same address inherits old dedup claim; reject identity mismatch.
9. dedup retention expiry falls inside time uncertainty; do not extend dedup window.
10. replay namespace rotates while stale writer can still send old requests; reject/fence.
11. bounded-repeat counter restored backward; replay rollback detected.
12. replay says UNUSED but current evidence ledger proves ambiguous dispatch; block reuse.
13. evidence ledger missing while replay says CONSUMED; preserve consumed state but downgrade completeness/audit claim.
14. garbage collection deletes ambiguous request before qualified resolution; reject GC/currentness.
15. historical replay checkpoint restored after newer consumption; remains historical only.
16. local component appends `generation=999` to stale replay store; no currentness without protected witness.

## 22. Practical rule

> Replay safety depends on a uniquely witnessed current replay cut, not on local maximum generation. A target dedup guarantee may substitute only when that exact dedup property is independently current for the exact target/request scope.

## 23. Authority boundary

This document does not:
- implement replay storage;
- create a live witness service;
- change target configuration;
- authorize target writes;
- perform recovery/failover;
- mutate providers/credentials;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
