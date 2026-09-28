# Transaction Reconciliation and Late Evidence V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #14 — replay-ledger anti-rollback
- Draft PR #15 — dispatch commit ordering
- Draft PR #16 — execution evidence and causal attribution
- Draft PR #13 — effect-intent binding and anti-replay

## Purpose

ABIL treats `UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` as durable and non-replayable.

Later evidence may arrive:

- delayed acknowledgement;
- target query/readback;
- physical sensor evidence;
- technician inspection;
- downstream process evidence;
- recovery/fault logs;
- target-side dedup state.

The open question is:

> How may later evidence narrow or resolve a historical transaction without rewriting history, restoring old authority, or making the old request reusable?

## 1. Historical transaction identity is immutable

A reconciliation record must bind the original:

- deployment identity;
- request ID;
- effect-intent digest;
- execution attempt identity;
- decision/admission receipt;
- authority epoch;
- ownership generation;
- writer identity;
- target/session correlation identity;
- dispatch reservation/commit evidence;
- original receipt/evidence state.

Reconciliation updates knowledge about the historical event.

It does not create a new historical event.

## 2. Original records are not overwritten

Preserve:

- original request;
- original admission decision;
- original dispatch attempt;
- original receipt(s);
- original ambiguity/conflict state;
- later reconciliation evidence.

Later evidence should append or supersede an interpretation record, not mutate the historical inputs into a cleaner story.

## 3. Reconciliation dispositions

Potential historical execution dispositions:

### `REMAINS_AMBIGUOUS`

Evidence still cannot establish whether the physical effect occurred.

### `KNOWN_NO_EFFECT`

Evidence proves the protected effect did not occur under the exact target semantics.

### `KNOWN_EFFECT_OCCURRED`

Evidence proves the requested physical effect occurred.

### `TARGET_REPORTS_EFFECT`

Target evidence supports execution, but independent physical proof is unavailable.

### `PHYSICAL_OBSERVATION_CONSISTENT`

Physical evidence matches expected consequence, while causation may remain unresolved.

### `CONFLICTING_EVIDENCE`

Evidence sources disagree materially.

### `RESOLUTION_RETRACTED_OR_SUPERSEDED`

A prior reconciliation conclusion is no longer supportable because newer evidence invalidated it.

These are evidence states, not authority states.

## 4. No return to UNUSED

A request that crossed the durable dispatch-reservation boundary must not become `UNUSED` after reconciliation.

Even if later evidence proves `KNOWN_NO_EFFECT`:

- the historical request remains a consumed historical transaction;
- any later attempt is a new request/decision subject unless an exact target dedup/idempotency contract says resubmission of the same logical request is the qualified recovery mechanism.

This prevents history rewrite.

## 5. Retry eligibility is separate

Reconciliation may establish facts that make a new attempt safe.

That is not the same as authorizing or automatically scheduling a retry.

A new attempt must satisfy:

- current authority;
- current ownership;
- current deployment/commissioning evidence;
- current effect intent;
- current replay state;
- current preconditions;
- exact recovery/idempotency rule where required.

Historical reconciliation cannot manufacture current write authority.

## 6. Late receipt binding

A delayed receipt should be accepted only if it can be bound to the exact original transaction.

Bind, where available:

- request/correlation ID;
- target/session identity;
- authority/ownership generation;
- attempt sequence;
- effect-intent digest;
- timestamp/order;
- target receipt semantics profile.

A delayed old receipt cannot complete a newer request.

## 7. Late physical observation

A later physical observation may narrow the outcome only within its evidence ceiling.

Example:
- cylinder is extended when inspected later.

Possible conclusions depend on:
- whether the cylinder could have moved for another reason;
- intervening commands;
- fallback/safety behavior;
- mechanical persistence;
- observation source/currentness.

Do not infer original causation automatically.

## 8. Known-no-effect proof

`KNOWN_NO_EFFECT` should require stronger evidence than "no expected telemetry appeared."

Potential valid evidence:
- target rejected before execution and target semantics prove no partial effect;
- target durable transaction log proves request never committed;
- qualified gateway/transport evidence proves dispatch never crossed effect boundary;
- independent physical/process evidence plus target semantics proves no effect could have occurred.

Absence of evidence is not automatically evidence of no effect.

## 9. Known-effect proof

`KNOWN_EFFECT_OCCURRED` may require different evidence by target/action class.

Potential sources:
- durable target execution record;
- exact target-side transaction state;
- independent physical sensor;
- device motion/state feedback;
- operator inspection;
- postcondition evidence with competing causes excluded sufficiently.

Target `SUCCESS` alone may only support `TARGET_REPORTS_EFFECT`.

## 10. Conflicting evidence

If:
- target reports completed;
- physical sensor indicates no change;
- operator observes a jam;

preserve conflict.

Do not choose the most convenient source automatically.

Potential outcome:
`CONFLICTING_EVIDENCE`.

Further recovery/reconciliation may be required.

## 11. Resolution generation

Reconciliation conclusions may evolve as new evidence arrives.

Use an immutable resolution generation/version concept.

Example:

- R0: ambiguous;
- R1: target reports completed;
- R2: physical inspection conflicts;
- R3: root cause establishes partial movement then jam.

Do not overwrite R1/R2; supersede them with retained provenance.

## 12. Resolution authority

A reconciliation evaluator/reviewer must be identified.

Depending on claim strength, valid sources may include:

- deterministic target semantics;
- qualified reconciliation engine;
- technician/operator;
- commissioning engineer;
- independent evaluator.

The learner/candidate plane should not self-promote its own favored causal interpretation into authoritative reconciliation without the required evidence/process.

## 13. Physical-effect versus causal resolution

Two questions remain distinct:

### execution question
Did the requested physical effect occur?

### causal question
Did this request cause the observed downstream consequence?

Example:
- valve opened: known effect occurred;
- pressure rose: observed;
- whether valve caused the pressure rise may still be only plausible.

Do not collapse these.

## 14. Partial effects

Some commands may partially execute.

Examples:
- axis moves 20 mm of requested 100 mm;
- valve opens then immediately faults closed;
- batch executes A and B, fails before C.

Reconciliation should represent partial effect explicitly.

A binary success/fail may lose safety-relevant history.

Potential disposition:
`PARTIAL_EFFECT_OCCURRED`.

## 15. Batch reconciliation

For a batch:
- preserve per-member attempt/result;
- preserve order;
- preserve unknown members;
- resolve members independently where evidence allows;
- do not mark whole batch completed because final state looks correct;
- do not restart whole batch from member one without exact recovery semantics.

## 16. Session / bounded-repeat reconciliation

For bounded-repeat/session actions:
- preserve count reserved;
- count dispatched;
- count known effects;
- count ambiguous;
- budget remaining;
- superseded/revoked session state.

Ambiguous attempts should conservatively consume effect budget until exact evidence permits a safe adjustment.

## 17. Cross-generation late evidence

Historical evidence may arrive after:
- authority epoch advanced;
- ownership transferred;
- artifact changed;
- deployment recommissioned.

It may resolve the historical transaction.

It must not:
- modify current authority;
- satisfy a current request;
- restore old ownership;
- reactivate old artifact selection.

Historical truth and current authority remain separate.

## 18. Recovery integration

On restart/recovery, unresolved transactions should be loaded before affected writes resume.

Later reconciliation can narrow them.

Write resumption should depend on:
- exact unresolved transaction set;
- affected output/effect scope;
- current target-specific blocking policy;
- current replay ledger;
- current authority/currentness.

One unrelated historical ambiguity need not necessarily block every output if dependency scope proves independence.

## 19. Garbage collection

Historical reconciliation data should not be discarded while it can still affect:

- replay safety;
- causal attribution;
- control coverage;
- audit/root cause;
- current recovery scope;
- delayed receipt correlation.

A future retention policy should prove when a historical request is no longer operationally relevant.

## 20. Control-coverage update

Reconciled historical evidence may improve or weaken control coverage.

Examples:

- known physical effect supports tested behavior;
- conflicting evidence downgrades a prior claim;
- known-no-effect reveals a missing precondition;
- partial effect reveals unmodeled fault path.

Coverage update must preserve source/provenance and evidence class.

It must not automatically widen executable authority.

## 21. Machine-model correction

A later reconciliation may require machine-model correction.

The corrected model should preserve:
- prior hypothesis;
- contradicting evidence;
- correction;
- affected behaviors;
- confidence/provenance.

Do not rewrite the learning history to pretend the earlier model was always correct.

## 22. Reconciliation receipt concept

A future `TransactionReconciliationReceipt` could bind:

- original transaction identity;
- prior historical disposition;
- newly received evidence identities;
- target-semantics profile;
- physical-effect disposition;
- causal-attribution disposition;
- conflict/uncertainty;
- reviewer/evaluator identity;
- resolution generation;
- superseded resolution ID where applicable;
- exact time/as-of;
- downstream coverage/model impacts;
- immutable digest.

This is a research shape, not a required schema.

## 23. Hostile research cases

A future implementation should fail closed or preserve ambiguity for at least:

1. delayed old receipt completes a new request;
2. known-no-effect based only on absent telemetry;
3. target success upgrades directly to known physical effect without semantics;
4. later physical state is attributed to old request despite intervening actions;
5. ambiguous request becomes unused after reconciliation;
6. known-no-effect automatically triggers retry;
7. historical resolution updates current authority epoch;
8. old receipt from prior ownership generation mutates current request state;
9. conflicting physical evidence is discarded because target reports success;
10. partial effect collapsed into failed/no-effect;
11. batch final state causes all members to be labeled completed;
12. session ambiguity does not consume budget;
13. learner self-labels favored causal hypothesis as reconciled truth;
14. new evidence contradicts old reconciliation but history is overwritten;
15. garbage collection removes unresolved request before delayed receipt window closes;
16. control coverage upgrades beyond reconciliation evidence ceiling;
17. historical evidence after recommissioning is attached to new deployment generation;
18. same request ID collision causes evidence to join wrong effect intent.

## 24. Relationship to PR #14–#16

PR #14:
- keeps replay/consumption history monotonic.

PR #15:
- creates a conservative durable commit point before physical effect can become possible.

PR #16:
- grades execution, observation, and causal evidence.

This research:
- defines how later evidence updates historical transaction knowledge without changing historical authority or request reuse semantics.

## 25. Evidence ceiling

This research does not guarantee:
- ambiguity is always resolvable;
- physical effects are always observable;
- target receipts are trustworthy;
- causal attribution is always possible;
- historical evidence can safely authorize a new attempt.

It defines how to preserve uncertainty and update historical knowledge without creating new authority.

## 26. Research disposition

The practical rule is:

> Reconciliation may refine historical knowledge, but it must not rewrite transaction identity, restore consumed requests, or manufacture current authority.

No reconciliation implementation, machine access/write, commissioning, recovery action, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
