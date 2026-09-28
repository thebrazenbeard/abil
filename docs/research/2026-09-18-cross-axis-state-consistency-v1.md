# Cross-Axis State Consistency V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related research:
- Draft PR #4 — component/product evidence invalidation
- Draft PR #7 — deployment commissioning evidence currentness
- Draft PR #8 — support/recovery state currentness
- Draft PR #6 — write-capability admission design

## Purpose

The successor architecture explicitly separates:

1. `ProductCapabilityQualification`
2. `DeploymentCommissioningState`
3. `ExecutionAuthorityState`
4. `ControlArtifactLifecycle`
5. `SupportRecoveryState`

That separation prevents one stage number from laundering several different facts into a single "ready" state.

The remaining systems question is:

> What happens when every axis is individually well-formed but the combination is inconsistent, stale, or insufficient for the requested operation?

This research defines cross-axis consistency principles so no axis silently substitutes for another.

## 1. State vector, not stage

Represent the relevant operational subject conceptually as a state vector:

`OperationalStateVector = (product, deployment, authority, artifact, recovery)`

Optionally associated independent subjects include:

- safety-classification state;
- control-ownership/fencing state;
- target hardware/protocol identity;
- current topology generation;
- ambiguous-transaction ledger;
- current qualification/evidence timestamps.

There is no valid rule such as:

`stage >= 7 -> writes allowed`

A requested operation must satisfy the exact predicates required across the axes that govern it.

## 2. No cross-axis implication by default

The following implications are invalid unless separately evidenced:

- product qualified -> deployment commissioned;
- deployment commissioned -> execution authority granted;
- authority granted -> promoted artifact current;
- promoted artifact current -> deployment evidence current;
- recovery ready -> artifact current;
- recovery ready -> authority current;
- current authority -> recovery ready;
- active writer -> commissioning current;
- valid component certificate -> product capability qualified;
- successful rollback test -> current production authority;
- current product qualification -> machine-specific safety classification.

Each axis answers a different question.

## 3. Requested-operation predicate

A future decision surface should evaluate:

- exact requested operation;
- required capability;
- deployment subject;
- authority domain/output namespace;
- artifact/runtime subject;
- recovery/fallback dependency;
- safety/noninterference dependency;
- currentness cut for each required axis.

The result should be one of:

- `ADMISSIBLE`
- `DENIED_MISSING_REQUIRED_AXIS`
- `DENIED_STALE_AXIS`
- `DENIED_AXIS_MISMATCH`
- `DENIED_CONFLICT`
- `DENIED_UNKNOWN`

A human-facing summary such as "system ready" is not enough.

## 4. Cross-axis binding

Where one axis depends on another, the evidence should bind the exact subject.

Examples:

- a promotion manifest binds deployment identity/topology/evidence cut;
- an authority grant binds deployment and authority domain;
- support/recovery evidence binds deployment and artifact/runtime subject;
- deployment commissioning binds topology, semantic mappings, coverage, fallback policy;
- product qualification binds declared hardware/protocol profile.

"Current" independently on both sides is insufficient if the identities do not match.

## 5. Product versus deployment consistency

### Valid example

- product capability qualifies direct control for hardware profile H1;
- deployment D1 is commissioned for H1;
- target runtime/hardware matches H1.

### Invalid example

- product capability is current for H1;
- deployment was commissioned on H0;
- hardware was replaced with H1;
- deployment evidence was never re-established.

Product capability cannot repair stale deployment commissioning.

Expected:
`DENIED_AXIS_MISMATCH` or `DENIED_STALE_AXIS`.

## 6. Deployment versus authority consistency

Execution authority must not imply deployment currentness.

Examples that block stronger action:

- authority grant is current, but deployment currentness is `UNKNOWN_CURRENTNESS`;
- output namespace ownership is current, but commissioning envelope preconditions are stale;
- deployment identity matches but topology generation changed after the authority evidence cut;
- authority scope permits a command class that is now outside the reduced deployment envelope.

The system should not widen commissioning state to match authority.

## 7. Authority versus artifact consistency

A current authority grant is necessary but not sufficient for artifact activation.

Block activation if:

- artifact is only a candidate;
- promotion receipt is stale/superseded/revoked;
- artifact digest does not match promotion;
- deployment binding differs;
- authority generation differs;
- target runtime/hardware identity differs;
- artifact operating envelope exceeds current deployment envelope.

Likewise, a valid promoted artifact cannot manufacture current authority.

## 8. Artifact versus deployment consistency

A historically valid promoted artifact can become inadmissible when machine-specific evidence changes.

Examples:

- semantic mapping changed;
- I/O ownership changed;
- topology changed;
- control coverage downgraded;
- fallback policy changed;
- relevant commissioning evidence became stale.

The artifact remains historical evidence.

Its prior successful promotion does not imply current activation admissibility.

## 9. Recovery versus authority consistency

Recovery state must not be used to bypass authority.

Examples:

- `ROLLBACK_READY` does not authorize rollback;
- manual recovery UI being current does not grant output ownership;
- appliance restore capability does not restore authority epoch;
- replacement hardware recovery does not inherit writer status;
- a known-good image does not reactivate an old promotion automatically.

Recovery may restore capability/evidence, but authority must come from the current authority subject.

## 10. Recovery versus deployment consistency

Recovery evidence can be current while machine-specific commissioning is stale.

Examples:

- appliance can restore correctly, but I/O was rewired;
- rollback artifact is readable, but tooling changed;
- manual recovery interface works, but semantic mapping changed;
- degraded mode mechanism works, but operating envelope changed.

In these cases, recovery can remain partially qualified while stronger machine action remains blocked.

## 11. Recovery versus product consistency

A recovery path may depend on a product/runtime profile.

Block or downgrade recovery when:

- restored image targets unsupported hardware;
- driver/runtime changed beyond recovery evidence;
- backup format can no longer be consumed;
- trusted loader/verifier assumptions changed;
- external recovery tooling disappeared.

Conversely, current product qualification does not prove the recovery path was exercised on the current deployment.

## 12. Ownership / fencing overlay

Control ownership is related to `ExecutionAuthorityState` but should remain mechanically evidenced.

Even if all five state axes appear current, write dispatch should fail if:

- prior writer quiescence is unknown;
- dual-authority conflict exists;
- ownership outcome is unknown;
- stale writer fencing cannot be proven;
- requested namespace does not match the owned namespace;
- delayed stale writer/session may still write.

A state vector cannot paper over split brain.

## 13. Ambiguous transaction overlay

An unresolved prior-generation physical action can constrain later operations even when other state axes are current.

Examples:

- restart completes;
- new authority generation is current;
- promoted artifact is valid;
- deployment is current;

but a prior physical action outcome is unresolved.

The new generation must not blindly reissue a semantically equivalent non-idempotent operation if the old physical effect remains possible.

Ambiguity is not erased by a healthy state vector.

## 14. Safety classification overlay

Independent safety/noninterference state cannot be inferred from ordinary control readiness.

Block ordinary-control assumptions when:

- protective/interlock semantics are unknown;
- safety classification is stale;
- preserved safety interface changed;
- requested operation crosses a safety-owned boundary;
- ordinary commissioning tries to classify its own protective preconditions.

No combination of the five ordinary state axes grants safety ownership.

## 15. Cross-axis stale propagation

A change should not blindly invalidate every axis.

Instead:

1. detect changed subject;
2. follow dependency edges;
3. downgrade affected axes;
4. recompute admissibility for requested operations;
5. preserve unaffected historical/current evidence;
6. block only what no longer has a complete current predicate.

This avoids both unsafe carryover and unnecessary global reset.

## 16. Contradictory-state cases

A future consistency checker should explicitly represent contradictions such as:

### Case A — Current authority + stale deployment

- product: current
- deployment: stale
- authority: current
- artifact: current
- recovery: current

Write-capable operation:
`DENIED_STALE_AXIS`

### Case B — Current deployment + no authority

- product: current
- deployment: current
- authority: none
- artifact: promoted
- recovery: current

Production write:
`DENIED_MISSING_REQUIRED_AXIS`

Read-only diagnostics may remain admissible.

### Case C — Current authority + stale artifact

- product: current
- deployment: current
- authority: current
- artifact: superseded
- recovery: current

Activation:
`DENIED_STALE_AXIS`

### Case D — Current artifact + unknown ownership

- product: current
- deployment: current
- authority: current
- artifact: current
- recovery: current
- ownership: `AUTHORITY_OUTCOME_UNKNOWN`

Write:
`DENIED_UNKNOWN`

### Case E — Recovery current + deployment stale

Manual recovery action that depends on stale semantic mapping:
`DENIED_STALE_AXIS`

Appliance read-only restore diagnostics may remain admissible if independently safe.

### Case F — Product qualification stale

Deployment, authority, artifact, and recovery may all still carry historical "current" labels.

Requested operation requiring the stale product capability:
`DENIED_STALE_AXIS`

No other axis can repair product qualification.

## 17. Reduced-envelope operation

Cross-axis invalidation should permit a smaller operation when its exact predicate remains satisfied.

Example:

- direct-control deployment evidence becomes stale for one actuator group;
- read-only telemetry remains current;
- manual diagnostics remain current;
- recovery remains current.

The system may continue the narrower qualified capabilities while blocking affected writes.

This must be explicit; "degraded" cannot mean "ignore the failed predicate."

## 18. Currentness cut

A future decision receipt should bind a coherent currentness cut across required evidence.

Potential fields:

- decision timestamp;
- requested operation;
- product qualification subject/currentness;
- deployment commissioning subject/currentness;
- authority grant/admission subject/currentness;
- artifact/promotion subject/currentness;
- support/recovery subject/currentness;
- ownership/fencing subject;
- safety-classification subject where relevant;
- ambiguous-transaction disposition where relevant;
- dependency identities;
- final admissibility result;
- denial reason(s).

This prevents a decision from mixing individually valid facts from incompatible historical moments.

## 19. Time-of-check / time-of-use

Even a coherent currentness cut can become stale before action.

A future implementation must consider:

- authority revoked after decision;
- topology changes after decision;
- ownership transfers after decision;
- commissioning envelope changes;
- artifact superseded;
- recovery/fallback state changes.

This research does not select a locking/transaction mechanism.

It establishes only that a prior decision receipt cannot be treated as indefinitely reusable authority.

## 20. Hostile research cases

A future cross-axis consistency contract should fail closed on at least:

1. current authority used to bypass stale deployment commissioning;
2. current product qualification used to bypass stale component evidence;
3. valid promoted artifact activated for a different topology generation;
4. rollback-ready recovery used as authority to activate old bytes;
5. current manual recovery UI used after I/O rewiring invalidated semantics;
6. replacement hardware inherits prior writer ownership from restored state;
7. all five axes current but dual-writer ownership unresolved;
8. all five axes current but ambiguous non-idempotent transaction unresolved;
9. all ordinary axes current but safety classification stale/unknown;
10. one stale dependency omitted from currentness cut;
11. current facts from incompatible historical cuts combined into one "ready" result;
12. authority revoked after decision receipt but before dispatch;
13. degraded mode silently widens the operating envelope;
14. product/deployment identities match by human-readable name but not immutable subject;
15. one axis transitions to unknown and cached "ready" result remains reusable;
16. partial recommission is treated as full deployment currentness;
17. successful appliance restore is treated as artifact promotion;
18. active artifact is used as proof that current authority must exist.

## 21. Research disposition

The practical rule is:

> Orthogonal state domains are safe only if requested operations are evaluated against a coherent, current, identity-matched cross-axis predicate.

No individual "green" axis and no human-friendly aggregate status may substitute for that predicate.

No cross-axis checker implementation, write admission implementation, machine access/write, commissioning, restore/recovery action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
