# Currentness Snapshot / Revalidation V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related research:
- Draft PR #9 — cross-axis state consistency
- Draft PR #10 — dependency-cycle resolution
- Draft PR #11 — non-authority currentness proof
- Draft PR #6 — write-capability admission design

## Purpose

The currentness research now defines:

- exact state axes;
- coherent currentness cuts;
- dependency graphs;
- cycle-safe grounding;
- exact subject generations;
- currentness receipts;
- operation-scoped admissibility.

One race remains:

> What prevents the checked currentness cut from becoming stale after validation but before a protected effect is dispatched?

A decision can be correct at time T1 and wrong at T2.

This research defines snapshot/revalidation principles for that time-of-check/time-of-use boundary.

## 1. Decision subject versus dispatch subject

A protected-effect decision should bind a concrete checked subject set.

Conceptually:

`AdmissionReadSet = {subject_id, generation, digest, predicate_result}*`

A later dispatch must prove that every required subject still matches the admitted read set, or must recompute admission.

A prior boolean `ADMISSIBLE=true` is not timeless authority.

## 2. Version vector

A future decision receipt may bind a version vector such as:

- product qualification generation;
- deployment commissioning generation;
- authority epoch;
- artifact/promotion generation;
- support/recovery generation;
- ownership/fencing generation;
- safety-classification generation;
- ambiguous-transaction ledger generation;
- dependency-graph/currentness-cut generation.

The exact fields depend on the requested operation.

The vector should bind exact identities, not only counters.

## 3. Required-subject read set

For each required dependency, retain:

- subject type;
- immutable subject ID/digest;
- currentness generation;
- read/evaluation time;
- freshness deadline where applicable;
- source/reader identity;
- predicate result;
- dependency edges that made it required.

A missing required subject is not a partial success.

## 4. Dispatch revalidation

Before a protected effect is dispatched, future implementation should use one of:

### `ATOMIC_COMPARE_AND_DISPATCH`

The decision is committed only if every required subject still equals the checked vector inside an atomic or mechanically equivalent boundary.

### `REVALIDATE_THEN_DISPATCH`

All required subjects are re-read/revalidated immediately before dispatch under a bounded protocol, and any changed generation/digest causes rejection/restart.

### `TARGET_TRANSACTION_GUARD`

The target/gateway enforces a guard token bound to the exact admitted subject vector and rejects the action if the guard no longer matches current state.

This research does not select one mechanism.

## 5. No partial vector reuse

If one required subject changes:

- do not retain the old overall ADMISSIBLE result;
- do not reuse unaffected predicate PASS values unless the validation protocol explicitly permits stable sub-result reuse;
- recompute affected dependency graph/SCC/currentness cut;
- preserve historical decision evidence.

A cached green aggregate cannot outlive its required subject vector.

## 6. Authority revocation race

Example:

1. admission checks authority epoch A12;
2. authority is revoked/superseded to A13;
3. dispatch occurs using old decision.

Expected:
reject old dispatch.

The dispatch boundary must verify current authority generation, not merely prove it was current earlier.

## 7. Deployment-change race

Example:

1. commissioning evidence D7 is current;
2. maintenance changes I/O mapping and creates D8/unknown currentness;
3. old D7-based write decision dispatches.

Expected:
reject/revalidate.

A valid old commissioning receipt is historical evidence, not current dispatch proof.

## 8. Artifact supersession race

Example:

1. artifact C5 is current and promoted;
2. C5 is revoked/superseded by C6 before dispatch;
3. old C5 admission executes.

Expected:
reject old decision.

Exact active-artifact/promotion identity must remain current at dispatch.

## 9. Ownership-transfer race

Example:

1. writer W1 owns namespace N at generation O7;
2. ownership transfers to W2/O8;
3. delayed W1 request arrives with previously valid admission.

Expected:
reject stale owner/generation.

Single-writer enforcement must operate at effect time.

## 10. Recovery/fallback race

Example:

1. recovery readiness R4 supports fallback F2;
2. recovery state changes to R5 because hardware replacement invalidates F2;
3. old admission assumes R4/F2 still available.

If the requested operation depends on that fallback/recovery guarantee:
reject/revalidate.

## 11. Safety-classification race

Example:

1. ordinary-control action is admissible under safety classification S3;
2. preserved safety interface changes, classification becomes S4/UNKNOWN;
3. old admission dispatches.

Expected:
reject/revalidate.

Ordinary ABIL state cannot freeze an obsolete safety assumption.

## 12. Ambiguous-transaction race

Example:

1. no blocking ambiguous transaction at decision time;
2. another operation becomes `UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME`;
3. old decision dispatches semantically conflicting action.

If the ambiguity is a required blocker for the requested operation:
reject/revalidate.

## 13. Freshness deadline versus generation change

Freshness deadlines and generation checks solve different problems.

A receipt may be temporally fresh but semantically stale because a newer generation appeared.

A generation may be unchanged but time-based evidence may expire.

Dispatch requires both where both apply.

## 14. Clock trust

A future time-based revalidation mechanism should bind:

- evaluation clock/profile identity;
- dispatch time;
- freshness comparison semantics;
- tolerance/uncertainty where needed.

A caller-provided timestamp must not extend currentness.

This research does not choose a time-synchronization system.

## 15. Decision receipt

A future decision receipt could include:

- decision ID;
- requested operation;
- target/deployment;
- exact required read-set/vector;
- dependency graph/currentness-cut digest;
- evaluation time/profile;
- predicate outcomes;
- final disposition;
- expiry/freshness bound if applicable;
- revalidation requirement;
- validator identity/version.

A decision receipt is evidence.

It is not itself an authority grant.

## 16. Dispatch receipt

A protected-effect attempt should retain:

- decision receipt ID/digest;
- dispatch-time read-set/vector;
- compare/revalidation result;
- exact current authority/ownership generation;
- effect request identity;
- target correlation identity;
- dispatched/not-dispatched result;
- ambiguity/result receipt where applicable.

This provides evidence that admission remained valid at the effect boundary.

## 17. Optimistic versus locked evaluation

Future implementation may use optimistic concurrency:

1. read required subjects;
2. evaluate;
3. compare generations/digests;
4. dispatch only if unchanged.

Or stronger transactional/locking techniques.

The safety property is not the locking technology.

The safety property is:

> Any relevant required-state change between evaluation and effect invalidates or re-runs admission.

## 18. Livelock / churn

Repeated state changes can prevent admission.

That is preferable to using a stale decision.

A future implementation may need:
- bounded retries;
- backoff;
- operator-visible denial reason;
- state-stabilization requirements.

It must not eventually "just use the old green decision."

## 19. Multi-effect batches

One decision covering multiple physical effects requires explicit semantics.

Possible rules:

- one vector for whole atomic batch;
- per-effect revalidation;
- transactional sequence with abort boundary;
- operation-specific compensation/recovery.

Partial execution must preserve exact effect/receipt state.

A batch must not assume all later effects remain admitted merely because the first effect dispatched.

## 20. Hostile research cases

A future implementation should reject at least:

1. authority revoked after validation, before dispatch;
2. deployment generation changes after validation;
3. artifact superseded after validation;
4. ownership transfers after validation;
5. recovery/fallback generation changes after validation;
6. safety classification changes after validation;
7. new ambiguous transaction appears after validation;
8. receipt is time-fresh but newer generation exists;
9. generation unchanged but freshness deadline expires;
10. cached ADMISSIBLE reused after one dependency changes;
11. decision vector omits a required subject;
12. compare checks generation but not subject identity;
13. dispatch uses caller-provided old currentness receipt without revalidation;
14. first effect in a batch succeeds, later effect dispatches after state change without new check;
15. failed revalidation falls back to old decision;
16. revalidation detects conflict but dispatch still occurs;
17. delayed request from prior ownership generation carries a once-valid decision;
18. validator/revalidator identity differs from expected profile without detection.

## 21. Relationship to PR #6

PR #6 already requires execution-time stateful validation and current authority evidence.

This research does not reopen its design PASS.

It extends the downstream implementation question:

> How does a future writer ensure that the complete non-authority + authority currentness cut used by admission still holds at the exact dispatch boundary?

## 22. Research disposition

The practical rule is:

> An admissibility decision is valid only for the exact checked state vector and only while that vector remains current.

No snapshot/revalidation implementation, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
