# Effect Intent Binding and Anti-Replay V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #6 — write-capability admission design
- Draft PR #12 — currentness snapshot/revalidation
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md` — transactional command semantics

## Purpose

The architecture already requires physical command transactions to bind exact request identity, deployment, authority/ownership generation, semantic operation, parameters, expiry/replay policy, and execution receipts.

PR #12 separately requires a protected-effect admission decision to remain current at dispatch.

A composition question remains:

> How does a future implementation prove that the current, revalidated admission decision authorizes this exact physical transaction, rather than some other operation in the same broad authorized-effect class?

A valid admission must not become a reusable bearer token for arbitrary related effects.

## 1. Exact effect subject

A future protected-effect decision should bind an immutable effect-intent subject containing, as applicable:

- `request_id`;
- deployment/machine identity;
- authority domain;
- current authority epoch;
- current ownership generation;
- target/output namespace;
- exact semantic operation;
- exact parameters;
- expected state/precondition subject;
- commissioning-envelope action class;
- authorized effect identifier;
- artifact/promotion subject where applicable;
- effect count/cardinality;
- ordering/sequence position where applicable;
- expiry/freshness;
- duplicate/idempotency policy;
- target/protocol correlation identity where available.

A broad label such as `JOG_AXIS` or `WRITE_OUTPUT` is not sufficient if parameters materially affect physical consequence.

## 2. Decision-to-request binding

A decision receipt should bind:

- exact effect-intent digest;
- exact request ID;
- exact admitted currentness/version vector;
- exact authorized-effect scope;
- exact authority/ownership generation;
- exact target/deployment;
- exact validator identity;
- exact decision time/currentness bounds.

Dispatch should reject if the actual transaction envelope differs from the admitted effect-intent subject.

## 3. Parameter substitution

Reject cases where:

- decision admitted speed = 10%, request uses 40%;
- decision admitted duration = 500 ms, request uses 5 s;
- decision admitted output A, request uses output B;
- decision admitted forward direction, request uses reverse;
- decision admitted one axis, request adds another;
- decision admitted one recipe/state transition, request selects another.

Semantic equivalence must be explicit and mechanically defined; it must not be inferred by string similarity or operator intuition.

## 4. Request-ID uniqueness

A request ID is scoped by current authority state, conceptually:

`(deployment, authority_domain, authority_epoch, ownership_generation, request_id)`

The same tuple must not denote two different effect intents.

If a duplicate request ID arrives with a different effect-intent digest:

`DENIED_REQUEST_ID_CONFLICT`

or equivalent.

Duplicate-same-intent handling follows the target/idempotency contract.

## 5. Single-use versus reusable decisions

A future decision must explicitly declare whether it is:

### `SINGLE_EFFECT`

Valid for one exact effect attempt only.

### `BOUNDED_REPEAT`

Valid for a mechanically bounded number/rate/window of repeated identical or equivalently defined effects.

### `ATOMIC_BATCH`

Valid for one exact batch with defined ordering and cardinality.

### `SESSION_SCOPED`

Only if a separately qualified session contract exists with exact operation family, parameter bounds, authority/ownership binding, freshness, rate limits, and revocation semantics.

Default for non-idempotent physical effects should not be unlimited reuse.

## 6. Execution count

For `SINGLE_EFFECT`, once the effect is:

- accepted for dispatch;
- dispatched;
- known completed;
- failed after possible execution;
- unknown/ambiguous after possible execution;

the decision must not be usable to create a new physical attempt.

A retry requires either:

- exact idempotency semantics proving safe duplicate handling;
- target-side deduplication for the same logical request;
- or a new separately admitted request under a recovery rule.

## 7. Ambiguous outcome interaction

If an admitted transaction becomes:

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME`

then:

- the admission decision remains historical evidence;
- it does not authorize a new attempt;
- a new request must not silently reuse the old decision;
- semantically equivalent later action must consider the unresolved old physical effect;
- delayed acknowledgement remains tied to the original request/generation.

Admission freshness does not erase ambiguity.

## 8. Replay protection

A future dispatch guard should reject:

- old decision reused after completion;
- old decision reused after timeout with possible execution;
- old decision replayed after restart;
- old decision replayed after ownership transfer;
- old decision replayed after authority epoch advance;
- old decision replayed against a different deployment;
- old decision copied to another writer instance;
- old decision replayed after expiry;
- old decision replayed after target correlation/session changes.

Replay protection may use target-side deduplication, durable ledgers, nonces, counters, one-time tokens, or other qualified mechanisms.

This research does not select the mechanism.

## 9. Effect-intent canonicalization

If effect-intent digests are used, canonicalization must be deterministic and independently bound.

The profile should specify:

- field ordering;
- numeric encoding;
- unit normalization;
- string encoding;
- null/omitted semantics;
- collection ordering;
- parameter precision;
- target/output identity encoding;
- sequence/batch encoding.

Equivalent-looking JSON under different canonicalization rules must not create ambiguous intent identity.

## 10. Units and representation

Physical parameters require exact units and representation.

Examples:

- milliseconds versus seconds;
- percent versus engineering units;
- raw counts versus scaled units;
- degrees versus radians;
- signed versus unsigned values;
- absolute versus relative move;
- speed versus torque mode.

The admitted effect intent should bind unit/profile identity.

## 11. Preconditions

If an action depends on an expected state/precondition snapshot, the decision should bind that exact snapshot or generation.

If the precondition changes before dispatch:

- PR #12 revalidation should fail;
- the request should not silently rebind to the new state.

A new decision may be required even if the semantic command name is unchanged.

## 12. Batch binding

An atomic or ordered batch should bind:

- exact member effect intents;
- exact order;
- exact cardinality;
- batch ID;
- authority/ownership generation;
- batch-level preconditions;
- per-member preconditions where applicable;
- failure/abort semantics;
- partial-execution semantics;
- ambiguity handling;
- compensation/recovery policy where applicable.

A decision for batch [A,B,C] must not authorize [A,C,B] or [A,B,C,D].

## 13. Partial batch execution

If a batch partially executes:

- record exactly which members were dispatched;
- preserve which members are known completed/failed/unknown;
- do not replay the whole batch blindly;
- any continuation/recovery should be a new transaction subject unless exact target semantics prove safe resume.

## 14. Session-scoped authorization

A session-scoped decision is higher risk because it intentionally authorizes more than one effect.

If ever supported, it should bind:

- exact deployment;
- writer identity;
- authority epoch;
- ownership generation;
- operation family;
- parameter ranges;
- rate limits;
- total effect count/budget;
- time window;
- commissioning envelope;
- target namespace;
- revocation/readback mechanism;
- audit ledger.

A session contract must not be inferred from one successful command.

## 15. Cross-axis currentness integration

The effect-intent subject should be evaluated against the exact currentness cut required for that operation.

If the effect changes, required dependencies may also change.

Example:
- low-speed jog may be current under one envelope;
- high-speed move may require stronger deployment/recovery/safety evidence.

A decision for one operation must not inherit the other operation's currentness proof.

## 16. Dispatch guard

Conceptually:

`DispatchAllowed = AdmissionCurrent AND EffectIntentMatches AND ReplayStateAllows AND OwnershipCurrent AND NoBlockingAmbiguity`

All required predicates must hold at effect time.

No single positive predicate repairs another failed predicate.

## 17. Decision and transaction receipts

Future evidence should preserve linkage:

`effect_intent -> admission_decision -> dispatch_revalidation -> execution_attempt -> execution_receipt -> telemetry/attribution`

Each link should bind exact immutable identities.

A narrative log line is insufficient provenance for protected effects.

## 18. Hostile research cases

A future implementation should reject at least:

1. valid decision for output A reused for output B;
2. speed parameter increased after admission;
3. duration increased after admission;
4. same request ID reused with changed parameters;
5. completed single-effect decision replayed;
6. timed-out possibly executed decision replayed;
7. old decision replayed after authority epoch advance;
8. old decision replayed after ownership transfer;
9. old decision copied to another deployment;
10. old decision replayed after restart;
11. batch member order changed;
12. extra batch member appended;
13. first batch member executes, batch replay starts from member one;
14. session scope inferred from one admitted command;
15. session rate/effect budget exceeded;
16. semantic operation unchanged but precondition snapshot changed;
17. physical unit representation changes without digest/profile mismatch;
18. same numeric parameter interpreted under different unit profile;
19. effect-intent digest uses caller-selected canonicalization;
20. currentness proof for low-consequence operation reused for stronger operation;
21. delayed acknowledgement is attached to a new request;
22. target correlation identity changes but old decision remains usable.

## 19. Relationship to PR #6 and PR #12

PR #6 remains a valid design/governance admission contract.

PR #12 remains the state-vector TOCTOU research boundary.

This research composes them with the architecture's transactional-command semantics:

- PR #6: is write capability currently admissible?
- PR #12: is the checked state vector still current at dispatch?
- this research: is the dispatched transaction exactly the effect that was admitted, exactly once or within the explicitly admitted reuse contract?

No existing PASS is reopened by this research.

## 20. Research disposition

The practical rule is:

> A write-admission decision must be bound to an exact effect intent and exact reuse cardinality; it must not function as a generic reusable token for related physical actions.

No effect-intent implementation, anti-replay implementation, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
