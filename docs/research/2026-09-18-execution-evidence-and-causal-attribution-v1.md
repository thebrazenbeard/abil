# Execution Evidence and Causal Attribution V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #13 — effect-intent binding and anti-replay
- Draft PR #14 — replay-ledger anti-rollback
- Draft PR #15 — dispatch commit ordering
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`
- `docs/FIELD_VALIDATION_ROADMAP.md`

## Purpose

The architecture correctly separates:

- `OperatorCommand`;
- `ActionProposal`;
- `GatewayDecision`;
- `ActionExecutionAttempt`;
- `ExecutionReceipt`;
- `TelemetryObservation`;
- `CausalHypothesis / Attribution`.

It also explicitly states:

> A subsequent observation is not automatically a proven action consequence.

This research makes that distinction operational.

The question is:

> After a protected effect is dispatched, what exactly may ABIL claim happened, based on which evidence, and how should that evidence affect ambiguity resolution, control coverage, commissioning, and future learning?

## 1. Evidence ladder

Different observations support different claim ceilings.

A future system should distinguish at least:

### `DISPATCH_RECORDED`

Evidence:
- local writer crossed the qualified dispatch boundary;
- exact request/effect intent recorded.

Supports:
- "ABIL attempted to dispatch this exact request."

Does **not** prove:
- target received it;
- target accepted it;
- physical effect occurred.

### `TRANSPORT_DELIVERED`

Evidence:
- transport/protocol semantics prove delivery to the target endpoint/session.

Supports:
- "The command reached the target communication endpoint."

Does **not** automatically prove:
- target application accepted it;
- target applied it;
- machine state changed.

### `TARGET_ACCEPTED`

Evidence:
- target acknowledged acceptance of the exact request/correlation identity.

Supports:
- "The target accepted the request."

Does **not** automatically prove:
- execution completed;
- actuator moved;
- process consequence occurred.

### `TARGET_EXECUTION_REPORTED`

Evidence:
- target reports started/completed/success for exact request.

Supports:
- "The target reported execution success."

Claim ceiling depends on target semantics.

A target success bit is not automatically independent physical proof.

### `TARGET_STATE_READBACK_CONFIRMED`

Evidence:
- a target/controller state readback, independently correlated, matches expected postcondition.

Supports:
- stronger evidence that internal target state reached the claimed value.

Does **not** necessarily prove:
- physical actuator/process consequence occurred;
- external mechanism responded correctly.

### `PHYSICAL_OBSERVATION_CONFIRMED`

Evidence:
- current, independently identified physical sensor/measurement evidence matches the expected postcondition.

Supports:
- "The physical observation is consistent with the expected effect."

Still does not automatically prove causation if competing causes are plausible.

### `CAUSAL_ATTRIBUTION_SUPPORTED`

Evidence:
- effect intent, timing, source identity, precondition/currentness cut, counterfactual/negative-control context where applicable, competing-cause analysis, and observation evidence support attribution.

Supports:
- bounded claim that the action caused or materially contributed to the observed consequence.

The exact strength of the claim should remain explicit.

## 2. Receipt class is not physical truth

An `ExecutionReceipt` should identify its evidence class.

Examples:

- transport ACK;
- controller ACK;
- command accepted;
- command started;
- command completed;
- target state readback;
- drive status readback;
- physical sensor confirmation;
- operator observation;
- later causal analysis.

A field named `success=true` without semantics is insufficient.

## 3. Target-semantics profile

Each target/protocol adapter should declare what each receipt/status means.

A future profile should bind:

- protocol/adapter identity;
- command class;
- acknowledgement type;
- whether ACK occurs before/after application;
- whether "complete" means queued, applied, or physically complete;
- correlation identity;
- failure/exception semantics;
- restart/reconnect behavior;
- duplicate behavior;
- readback semantics;
- latency bounds/uncertainty where known.

Without this profile, receipt claims should stay conservative.

## 4. Observation identity/currentness

A telemetry or readback observation should bind:

- deployment identity;
- topology generation;
- node/source identity;
- signal/channel identity;
- adapter identity;
- acquisition time;
- acquisition sequence/generation;
- quality/status;
- units/scaling profile;
- current semantic mapping;
- transport/source provenance;
- relevant calibration/currentness where applicable.

A sensor value without source/currentness identity is weak evidence.

## 5. Pre-effect baseline

Where causal attribution matters, retain the relevant pre-effect state.

Potential baseline evidence:

- exact precondition snapshot;
- target state before command;
- physical sensor values before command;
- active mode/state;
- competing writer/command activity;
- known external disturbances;
- recent maintenance/configuration changes.

Attribution without a pre-effect baseline may be weaker or impossible.

## 6. Time windows

Causal analysis should distinguish:

- command/admission time;
- dispatch reservation time;
- dispatch attempt time;
- target acceptance time;
- target execution report time;
- observation time;
- expected response latency/window;
- competing-event window.

A post-command observation outside the qualified causal window should not be promoted automatically.

## 7. Correlation is not causation

The architecture already prohibits answer-bearing `ACTION_CONSEQUENCE` labels from temporal succession alone.

This research strengthens that rule.

Reject causal overclaim when:

- sensor changed before dispatch;
- same change occurs frequently without the action;
- another writer/action could explain the observation;
- operator/manual intervention occurred;
- upstream process caused the change;
- observation is only a correlated proxy;
- sensor is stale/replayed;
- target reports success but physical observation conflicts.

## 8. Competing causes

Attribution evidence should record known plausible alternatives.

Examples:

- legacy PLC command;
- operator manual action;
- mechanical inertia;
- process pressure/temperature drift;
- upstream/downstream machine interaction;
- watchdog/fallback action;
- independent safety/protective action;
- automatic drive/controller logic;
- another ABIL request.

A strong attribution claim should explain why relevant alternatives were excluded, bounded, or remain unresolved.

## 9. Readback is not always independent

A target readback may share the same internal state or software path that produced the command acknowledgement.

Therefore distinguish:

### same-path readback

Useful but not independent physical confirmation.

### independent controller/drive state

Stronger, depending on architecture.

### independent physical sensor

Potentially stronger physical evidence.

### technician/operator observation

Human evidence with explicit provenance.

Do not label all readbacks "independent confirmation."

## 10. Physical observation conflict

If target reports success but physical evidence contradicts it:

- do not overwrite the conflict;
- preserve both evidence streams;
- mark execution/physical-effect result as conflicting or unknown;
- do not use target success alone to close ambiguity;
- trigger target-specific reconciliation/fault handling where authorized.

A green target receipt cannot erase red physical evidence.

## 11. No-observation case

Some valid actions have no independent observable consequence.

Examples:
- internal mode bit;
- latent configuration change;
- timing parameter update;
- command whose physical effect is deferred.

In these cases:
- preserve the evidence ceiling;
- do not invent physical confirmation;
- qualification may require a different readback/test method.

## 12. Delayed observation

A late observation may still be relevant.

But it should retain:
- exact timestamp/order;
- intervening actions/events;
- expected latency profile;
- competing-cause context.

Do not automatically attach the nearest earlier request.

## 13. Delayed receipt

A delayed target receipt must remain tied to:

- exact request ID;
- authority epoch;
- ownership generation;
- target/session correlation identity;
- original execution attempt.

It cannot close a newer request merely because operation/parameters are similar.

## 14. Ambiguity resolution

An `UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` may be narrowed only by evidence sufficient for the exact target/action semantics.

Possible outcomes:

- `KNOWN_NO_EFFECT`
- `KNOWN_EFFECT_OCCURRED`
- `TARGET_REPORTS_EFFECT`
- `PHYSICAL_OBSERVATION_CONSISTENT`
- `CONFLICTING_EVIDENCE`
- `REMAINS_AMBIGUOUS`

Do not collapse these into one boolean.

## 15. Attribution confidence is not authority

A high-confidence causal attribution:

- does not grant write authority;
- does not expand commissioning envelope;
- does not widen effect scope;
- does not promote an artifact;
- does not classify safety semantics.

Evidence and authority remain separate.

## 16. Learning-plane separation

Post-dispatch evidence can train or update the learner only through an explicit evidence projection.

The learner-facing projection should distinguish:

- raw observation;
- target receipt;
- technician assertion;
- independently established semantic label;
- evaluator-only causal ground truth where synthetic/holdout context permits it;
- inferred causal hypothesis.

Do not leak evaluator-only or independently adjudicated causal truth into a benchmark participant/learner when the experiment is supposed to test whether it can infer that structure.

## 17. Commissioning evidence use

A commissioning action may produce evidence for semantic grounding, but only within the supported claim ceiling.

Example:

Command:
`OPEN_VALVE_V17`

Observation:
pressure rises.

Possible evidence:
- target accepted command;
- valve-output readback changed;
- pressure changed in expected window.

Still unresolved:
- whether V17 caused the pressure rise if another valve/process event could explain it.

Technician confirmation may strengthen semantics with explicit provenance.

## 18. Control-coverage integration

A control-coverage ledger entry should record how behavior was supported.

Potential evidence classes:

- observed naturally;
- target-reported execution;
- physically observed after intervention;
- technician-specified;
- vendor-specified;
- simulated;
- tested with causal attribution;
- inferred only.

A transition supported only by target ACK should not be labeled physically proven.

## 19. Recovery/fault-path integration

Fault/recovery behavior often has ambiguous causal chains.

Evidence should preserve:

- initiating fault;
- requested recovery action;
- target acknowledgement;
- intermediate state;
- physical observation;
- fallback/protective action;
- operator intervention;
- final recovered state;
- unresolved attribution.

This prevents recovery qualification from over-crediting the requested action when another mechanism actually restored the system.

## 20. Sensor failure and disagreement

If multiple physical observations disagree:

- preserve each source;
- retain quality/currentness;
- do not majority-vote blindly;
- use target-specific sensor/provenance policy;
- mark physical effect as conflicting/unknown if unresolved.

A failed/stuck sensor can otherwise create false causal confidence.

## 21. Observation replay/staleness

After reconnect/restart, stale buffered telemetry must not be attached to a new action as fresh effect evidence.

Observation currentness should include enough ordering/session/source information to detect:

- duplicate samples;
- late samples;
- replayed samples;
- reordered samples;
- old buffered state.

## 22. Counterfactual / negative controls

Where practical and safe in simulation/shadow/controlled commissioning:

- compare action versus no-action intervals;
- compare unrelated outputs;
- vary timing/order;
- use withheld transitions;
- use correlated-but-noncausal signals.

This is especially useful before promoting causal claims into machine-model structure.

No unsafe physical experiment is implied.

## 23. Evidence receipt concept

A future `EffectEvidenceReceipt` could bind:

- request/effect-intent identity;
- execution attempt identity;
- target receipt(s);
- target-semantics profile;
- relevant pre-effect baseline;
- telemetry/readback observation identities;
- observation currentness;
- causal window/profile;
- competing-cause record;
- physical-effect disposition;
- causal-attribution disposition;
- unresolved conflicts;
- evaluator/reviewer identity;
- immutable evidence digest.

This is a research shape, not a required schema.

## 24. Claim dispositions

Suggested dispositions:

### execution layer
- `DISPATCH_ONLY`
- `TARGET_ACCEPTED`
- `TARGET_REPORTS_SUCCESS`
- `TARGET_READBACK_MATCHES`
- `PHYSICAL_OBSERVATION_MATCHES`
- `CONFLICTING_EXECUTION_EVIDENCE`
- `EXECUTION_OUTCOME_UNKNOWN`

### causal layer
- `CAUSAL_ATTRIBUTION_SUPPORTED`
- `CAUSAL_ATTRIBUTION_PLAUSIBLE`
- `CORRELATED_ONLY`
- `COMPETING_CAUSE_UNRESOLVED`
- `CAUSAL_ATTRIBUTION_REFUTED`
- `CAUSAL_ATTRIBUTION_UNKNOWN`

These layers should not be collapsed.

## 25. Hostile research cases

A future implementation should fail closed or downgrade claims for at least:

1. transport ACK treated as physical completion;
2. target "success" treated as actuator movement with no physical evidence;
3. sensor changes before dispatch but is credited to command;
4. correlated upstream signal treated as causal effect;
5. delayed old telemetry attached to newest command;
6. delayed old receipt completes a new request;
7. target readback shares same internal bit as ACK but is labeled independent confirmation;
8. target reports success while physical sensor contradicts it;
9. sensor is stale but used as fresh effect proof;
10. technician intervention occurs during causal window but is omitted;
11. competing writer command occurs during causal window;
12. safety/protective system causes state change but ABIL action gets credit;
13. ambiguous outcome becomes "success" merely because expected telemetry later appears;
14. no independent observable exists but physical effect is claimed anyway;
15. majority sensor vote hides common-mode provenance failure;
16. learner receives evaluator-only causal label during benchmark;
17. control coverage upgrades from ACK-only evidence to physically tested;
18. same semantic command under different parameter regime reuses old causal evidence;
19. recovery succeeds due to fallback logic but requested recovery command gets sole credit;
20. time-correlated proxy is promoted into a control-model causal edge.

## 26. Relationship to PR #13–#15

PR #13 asks:
- is this exact physical effect intent the one admitted?

PR #14 asks:
- can consumed/replay state roll backward and enable another effect?

PR #15 asks:
- did durable transaction state cross the conservative commit point before the physical effect became possible?

This research asks:
- after the attempt, what evidence supports which execution and causal claims?

All four concerns are independent.

## 27. Evidence ceiling

This research does not claim that:
- a target receipt proves physical motion;
- a physical observation alone proves causation;
- any one sensor is authoritative;
- exactly-once physical execution is solved;
- causal attribution can always be resolved.

It defines how to avoid overclaiming when evidence is weaker than the desired conclusion.

## 28. Research disposition

The practical rule is:

> Record execution, observation, and causal attribution as separate evidence layers, and never let a stronger claim outrun the weakest evidence actually established.

No execution-evidence implementation, causal-attribution implementation, machine access/write, commissioning, recovery action, product selection, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
