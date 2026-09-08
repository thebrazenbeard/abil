# ABIL Field Validation Roadmap

Status: **working validation sequence; no deployment authorization implied**

The roadmap is intentionally ordered so each stage can fail cheaply before ABIL earns access to a harder environment or stronger capability.

Passing one stage does not imply authority for the next.

## Stage 0 — Synthetic headless process

Build a small non-rendered industrial process simulator with hidden state, noisy sensors, controllable actuators, delays, recurring regimes, faults, drift, and confounding relationships.

ABIL should receive only declared learner-visible signals.

Goals:

- verify the telemetry/event model;
- compare candidate learners against simple baselines;
- test online adaptation and persistent state;
- prove that late regime changes can still be learned;
- test recurring old regimes after newer learning;
- measure compute and memory cost;
- keep exact simulator truth evaluator-side;
- prove learner/evaluator noninterference and closed information boundaries.

The simulator should be fast enough to generate long histories without GPU-expensive visual rendering.

## Stage 1 — Recorded telemetry replay

Feed ABIL recorded industrial-style telemetry through the same declared learner-facing event boundary used by the simulator.

Replay must support original timing and accelerated timing where the model permits it without changing analytical outcomes that should be pacing-independent.

Goals:

- test missing values, jitter, asynchronous signals, resets, duplicates, late events, and real-world noise;
- test schema drift and tag additions/removals;
- measure whether the learner finds stable predictive structure;
- compare performance with conventional forecasting/change-detection baselines;
- evaluate restart/checkpoint behavior;
- preserve exact replay/corpus identity and deterministic evidence;
- exercise opaque-label/semantic-ablation controls.

No live equipment connection is required at this stage.

## Stage 2 — Live isolated shadow mode

Deploy ABIL on a separate PC connected to a real isolated machine/process environment in externally enforced read-only mode.

The first live objective is deliberately narrow:

> Can ABIL observe an unfamiliar real system long enough to learn machine-specific predictive relationships that are useful to an experienced human without exhaustive manual mapping?

Expected evidence package:

- exact adapter/protocol/deployment identity;
- list/schema of observed signals;
- acquisition timing and drop statistics;
- model/checkpoint version;
- prediction accuracy against preregistered baselines;
- regime/change detections;
- examples of correct and incorrect inferred relationships;
- opaque-label/semantic-ablation comparison where feasible;
- operator assessment of whether surfaced findings are useful, obvious, wrong, or novel;
- resource consumption and stability over long runs;
- external evidence that the deployed profile cannot issue machine writes.

## Stage 3 — Operator-facing advisory mode

ABIL remains unable to directly change machine state but may surface:

- near-term predictions;
- detected changes;
- ranked hypotheses;
- evidence supporting or weakening each hypothesis;
- unresolved uncertainty;
- suggested additional observations;
- proposed discriminating tests;
- topology/device relationships and confidence;
- candidate semantic groupings.

The operator interface should make it easy to mark findings as useful, wrong, obvious, supplied, inferred, or unresolved so product learning can be evaluated separately from persuasive prose.

## Stage 4 — Guided semantic commissioning

ABIL begins explicit human-in-the-loop reconstruction of machine meaning.

The technician may identify known devices/functions, confirm or correct proposed relationships, and describe the purpose of signals, commands, sensors, actuators, and sequence states.

ABIL must preserve provenance between:

- discovered topology/configuration evidence;
- behavior learned from telemetry;
- technician-supplied semantics;
- hypotheses not yet confirmed.

The key validation question is:

> Can targeted technician interaction ground enough semantics to make ABIL useful without turning commissioning into full manual re-engineering?

Evidence should include:

- number/count of signals/devices discovered automatically;
- number/count of manual semantic declarations required;
- time spent in technician commissioning;
- relationships learned before and after semantic grounding;
- corrections/retractions after incorrect inferred meanings;
- machine-specific learned structure that survives label ablation.

## Stage 5 — Constrained manual-control gateway

Where safe, technically supported, and explicitly authorized, ABIL may present bounded manual-control requests for commissioning and diagnostic use.

The technician remains the initiator/approver of the action. The action path must be independently constrained and must not give the learning plane unrestricted write authority.

Promotion evidence includes:

- exact target hardware/protocol/deployment identity;
- exact allowed command set;
- state prerequisites and ordinary permissives;
- external safety authority/interlocks;
- request logging and freshness/replay protection;
- representative negative tests for disallowed commands;
- rollback/disable path;
- confirmation that learner/plugin code cannot access write credentials/handles directly.

## Stage 6 — Machine-model reconstruction

ABIL constructs an inspectable behavioral/control model from accumulated evidence.

The model should represent, as appropriate:

- machine states and modes;
- transitions;
- commands/actions;
- expected consequences;
- timing relationships;
- prerequisites/permissives;
- ordinary non-safety interlocks;
- alarm/fault conditions;
- recovery paths;
- unresolved or competing explanations;
- provenance and uncertainty.

The objective is not to reproduce ladder syntax. It is to reconstruct the machine's ordinary control behavior in a representation that can be reviewed, tested, and compiled/translated to multiple execution targets.

Evidence should include reconstruction fidelity against held-out observed behavior and technician review of incorrect/missing relationships.

## Stage 7 — Candidate control synthesis

ABIL may generate a candidate automation artifact from an approved machine model.

Possible targets may include:

- a conventional vendor PLC program/project where technically appropriate;
- a narrow high-level PLC execution-proxy interface;
- the ABIL deterministic control runtime;
- another supported industrial controller.

Generation itself confers no machine authority.

Every candidate must bind:

- source machine-model/evidence version;
- target runtime/controller profile;
- exact protocol/I/O configuration assumptions;
- unresolved assumptions and uncertainty;
- generated artifact/version identity.

Generated control must be inspectable and testable. A black-box artifact that cannot be reviewed or falsified does not qualify.

## Stage 8 — Replay, simulation, and shadow validation

Candidate automation is tested before cutover.

Validation should include as applicable:

- recorded replay;
- synthetic/digital-process simulation;
- shadow comparison against the surviving controller;
- expected-state/transition coverage;
- timing windows;
- fault/alarm paths;
- manual/recovery modes;
- restart/restore behavior;
- deterministic resource/cycle/jitter measurements for the target runtime;
- negative tests for disallowed transitions/commands;
- regression evidence across repeated runs.

The candidate remains non-authoritative until required acceptance criteria pass.

## Stage 9 — Existing-PLC execution proxy

When the existing PLC remains viable, ABIL may use it as the deterministic execution target while ABIL owns more of the reconstructed machine model and supervisory intent.

The interface should be narrow and semantic where possible: ABIL requests bounded operations while the PLC retains scan-timed I/O, established fieldbus behavior, local deterministic sequencing, and ordinary interlocks.

This stage may be transitional or permanent.

Required evidence includes:

- exact PLC/project/runtime identity;
- documented proxy interface and command semantics;
- bounded command set;
- deterministic PLC behavior under ABIL requests;
- rollback to legacy/local control where practical;
- comparison of ABIL-requested outcomes with actual machine responses;
- preserved independent safety authority.

## Stage 10 — Supervised cutover

A validated control artifact may be promoted into limited real machine authority under explicit installation-specific authorization.

The cutover package should include:

- exact hardware/network/protocol/deployment identity;
- active control artifact/version;
- acceptance evidence from prior validation stages;
- commissioning signoff;
- rollback/recovery procedure;
- watchdog/fail-closed behavior;
- alarm/fault handling evidence;
- declared operating envelope;
- independent safety boundary;
- exact authority/promotion receipt.

No generic ABIL release automatically authorizes a specific machine cutover.

## Stage 11 — Direct remote-I/O control where needed

When coexistence with the legacy PLC/control system is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, the ABIL deterministic runtime may replace the ordinary controller function and communicate directly with qualified remote I/O and field devices.

This is not simply Stage 9 with the PLC removed. It requires protocol-specific deterministic control qualification.

Evidence must include:

- qualified fieldbus/driver stack and interface hardware;
- exact I/O ownership/configuration;
- deterministic input/output update timing;
- cycle/jitter/load measurements under worst relevant conditions;
- watchdog and communication-loss behavior;
- restart/resynchronization behavior;
- drive/actuator command handling;
- alarm/fault paths;
- rollback/recovery plan;
- target-specific negative testing;
- proof that independent safety systems remain effective.

## Stage 12 — Permanent ABIL control runtime and support lifecycle

The ABIL appliance becomes the supported permanent control computer for the installation.

Long-run qualification should cover:

- stable deterministic execution over extended operation;
- persistence and restoration of machine/deployment state;
- versioned control-artifact upgrades;
- separation between ongoing learning/diagnostics and active control authority;
- update/rollback tooling;
- hardware replacement/recovery procedure;
- backup/export of machine model, configuration, evidence, and active control artifact;
- service diagnostics and auditability;
- supportable field replacement of appliance hardware;
- clear ownership of protocol adapters and vendor-specific dependencies.

A permanent installation should be maintainable as a product, not only understandable by the engineer who commissioned it.

## Coexistence versus replacement decision evidence

ABIL should explicitly record why an installation remains with an existing PLC execution target or advances to direct ABIL control.

Relevant considerations include:

- controller/project accessibility;
- supportability and vendor lifecycle;
- hardware condition/obsolescence;
- fieldbus and protocol support;
- deterministic timing performance;
- maintainability;
- availability of qualified ABIL adapters/runtime;
- licensing/proprietary-tool burden;
- rollback/recovery risk;
- commissioning labor;
- customer lifecycle/support requirements.

The product should not replace a still-useful PLC merely because ABIL can. It should also not make a legacy PLC mandatory when that controller is the failed or unsupportable component.

## Core evaluation metrics

ABIL should be scored on more than anomaly detection.

Important measures include:

- next-state and multi-horizon prediction;
- calibration/uncertainty quality;
- change/regime detection delay and false-positive rate;
- retention of older recurring regimes;
- adaptation speed after change;
- held-out condition transfer;
- topology/device discovery coverage;
- semantic-grounding efficiency;
- amount of manual semantic onboarding required;
- commissioning labor/time;
- usefulness of suggested discriminating observations/tests;
- machine-specific learned-structure quality;
- reconstructed control-model fidelity;
- generated-control validation pass/fail evidence;
- deterministic cycle/jitter/resource metrics when direct control is tested;
- restart/checkpoint equivalence;
- recovery/rollback time;
- protocol-adapter portability across fixtures/installations;
- compute, memory, storage, and network cost;
- operator usefulness ratings tied to specific outputs;
- permanent supportability;
- ability to say "insufficient evidence" when appropriate.

## Kill or material-revision conditions

The ABIL thesis should be materially revised if realistic testing shows that:

- useful performance requires exhaustive hand-labeling of every signal and relationship;
- reconstruction requires essentially full conventional manual re-engineering before ABIL contributes meaningful structure;
- simple established baselines match ABIL at substantially lower complexity/cost;
- online adaptation creates unacceptable forgetting or false normalization of faults;
- the model cannot remain stable during long-running streaming operation;
- discovered relationships are mostly persuasive restatements of tag names or operator annotations;
- generated control cannot be made inspectable, testable, and attributable to evidence;
- direct control cannot meet target deterministic timing/reliability requirements;
- protocol/vendor diversity makes each deployment a bespoke rewrite with little reusable product infrastructure;
- deployment/commissioning labor dominates the economic value;
- uncertainty is too poorly calibrated to support trustworthy diagnostics or control reconstruction;
- coexistence with surviving PLCs consistently delivers the same customer value at substantially lower risk/cost, in which case ABIL's product emphasis should shift toward reconstruction/commissioning and PLC-targeted execution rather than forcing direct takeover.

Failure of direct takeover as a universal strategy does not automatically invalidate ABIL if coexistence-first reconstruction remains commercially valuable. The product claim should narrow to what evidence actually supports.
