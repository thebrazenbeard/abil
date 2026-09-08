# ABIL Field Validation Roadmap

Status: **working validation sequence; no deployment authorization implied**

The roadmap is ordered so each stage can fail cheaply before ABIL earns access to a harder environment or stronger capability.

Passing one stage does not imply authority for the next.

## Cross-stage invariants

Every stage inherits these rules:

- control-substrate qualification and learner-efficacy qualification are separate;
- passive observation, bounded reads, active discovery, commissioning writes, proxy control, and direct deterministic control are distinct capability levels;
- unknown or unobserved control behavior is not silently promoted;
- unknown protective/interlock semantics are safety-relevant until independently classified;
- each physical output/control namespace has exactly one authoritative ordinary-control writer at a time;
- generated control remains an artifact until validation and explicit promotion;
- independent safety systems remain authoritative unless a separate safety-engineering project explicitly changes that contract.

## Stage 0 — Synthetic headless process

Build a small non-rendered industrial process simulator with hidden state, noisy sensors, controllable actuators, delays, recurring regimes, faults, drift, and confounding relationships.

ABIL should receive only declared learner-visible signals.

### Stage 0A — substrate qualification

Goals:

- verify a closed typed learner-event model;
- keep evaluator truth structurally inaccessible to learner/plugin code;
- test asynchronous event identity/currentness, missing/late/duplicate/reordered events, and deterministic feature assembly;
- compare uninterrupted execution with checkpoint/restore execution;
- verify replay/corpus/config/schema/code/seed identity;
- preserve fair paired baselines and machine-readable recomputable evidence;
- measure CPU, memory, disk, throughput, checkpoint, and restart cost;
- exercise opaque-label/semantic-ablation controls;
- permit the result `simple baseline wins` or `no useful learner advantage` without failing the substrate itself.

### Stage 0B — learner efficacy

Only after the substrate qualifies, test whether a particular learner earns stronger claims such as nontrivial machine-specific learned structure, improved prediction/adaptation versus agreed baselines, recurring-regime retention, useful uncertainty/change behavior, and semantic-efficiency advantages.

The first learner does not need to win in order for the experimental substrate to be honest and implementation-ready.

## Stage 1 — Recorded telemetry replay

Feed recorded industrial-style telemetry through the same declared learner-facing event boundary used by the simulator.

Replay must support original and accelerated pacing where allowed without changing analytical identity that should be pacing-independent.

Goals include missing values, jitter, asynchronous signals, resets, duplicates, late events, schema drift, deterministic evidence, restart/checkpoint behavior, opaque-label tests, and fair comparison with established baselines.

No live equipment connection is required.

## Stage 2 — Live isolated shadow mode

Deploy ABIL on a separate PC connected to a real isolated machine/process environment in an externally enforced read-only profile.

The first live objective is deliberately narrow:

> Can ABIL observe an unfamiliar real system long enough to learn machine-specific predictive relationships that are useful to an experienced human without exhaustive manual mapping?

Before connection, the deployment must declare its discovery profile:

- passive observation only;
- bounded authenticated/configuration reads;
- active enumeration/browse/scan;
- no write/commissioning capability.

If active discovery is used, evidence must include target allowlists, scan/query budgets, rate limits, timeout/retry behavior, and known side effects. `Read-only` is not evidence that the network interaction is operationally harmless.

Expected evidence includes exact adapter/protocol/deployment identity, observed signal/schema inventory, acquisition/drop statistics, checkpoint/model identity, preregistered baseline comparison, opaque-label results where feasible, operator usefulness assessment, resource/stability evidence, and external proof that machine writes are unavailable.

## Stage 3 — Operator-facing advisory mode

ABIL remains unable to directly change machine state but may surface predictions, changes, ranked hypotheses, evidence, uncertainty, topology/device relationships, candidate semantic groupings, proposed observations/tests, and explicit unknowns.

The interface should let the operator mark findings as useful, wrong, obvious, supplied, inferred, unresolved, or safety-classification-required.

## Stage 4 — Guided semantic commissioning

ABIL begins explicit human-in-the-loop reconstruction of machine meaning.

Before any action capability is introduced, the deployment should classify the observed legacy control-authority locus as supervisory HMI, SCADA, soft PLC/control PC, ordinary PLC/PAC logic, motion/drive control, safety control, mixed, or unknown.

The technician may identify known devices/functions, confirm/correct proposed relationships, and describe signals, commands, sensors, actuators, sequence states, and observed consequences.

ABIL must preserve provenance between discovered topology/configuration, behavior learned from telemetry, technician-supplied semantics, vendor-supplied semantics, and unresolved hypotheses.

The key question is whether targeted technician interaction grounds enough semantics to make ABIL useful without turning commissioning into full manual re-engineering.

Evidence should include discovery coverage, manual semantic declarations, commissioning time, inferred relationships before/after grounding, corrections/retractions, and learner-efficacy evidence that survives semantic ablation where the claim requires it.

## Stage 5 — Constrained manual-control gateway

Where safe, technically supported, and explicitly authorized, ABIL may present bounded manual-control requests for commissioning and diagnostic use.

The technician remains the initiator/approver. The learning plane receives no unrestricted write capability.

Promotion evidence includes exact target hardware/protocol/deployment identity, exact allowed command set, independent protective/safety prerequisites, request freshness/replay protection, negative tests for disallowed commands, rollback/disable path, and proof that learner/plugin code cannot directly access write credentials or handles.

Unknown protective/interlock semantics remain out of autonomous reconstruction and must not be bypassed.

## Stage 6 — Machine-model reconstruction

ABIL constructs an inspectable behavioral/control model from accumulated evidence.

The model should represent states/modes, transitions, commands/actions, expected consequences, timing, prerequisites/permissives, ordinary interlocks independently classified as non-safety, alarm/fault conditions, recovery paths, manual modes, provenance, uncertainty, and unresolved explanations.

The objective is not to reproduce ladder syntax. It is to reconstruct ordinary machine-control behavior in a representation that can be reviewed, tested, and translated to multiple execution targets.

Every reconstructed behavior must begin accumulating a **control-coverage ledger** stating whether it was observed, technician-specified, vendor-specified, inferred, simulated, or tested.

`Not observed` is not equivalent to `safe to omit`.

## Stage 7 — Candidate control synthesis

ABIL may generate a candidate automation artifact from an approved machine model.

Possible targets include a conventional vendor PLC program/project, a narrow PLC execution-proxy interface, the ABIL deterministic control runtime, or another supported industrial controller.

Generation confers no machine authority.

Every candidate must bind source machine-model/evidence version, target runtime/controller profile, exact protocol/I/O assumptions, control-authority locus, preserved safety interfaces/handshakes, unresolved assumptions, control-coverage ledger, and generated artifact identity.

Any state, transition, permissive, timeout, recovery path, or ordinary interlock lacking sufficient support remains excluded, fail-closed, or technician-engineered rather than guessed into the executable envelope.

## Stage 8 — Replay, simulation, and shadow validation

Candidate automation is tested before cutover.

Validation should include recorded replay, synthetic/digital-process simulation, shadow comparison where a surviving controller exists, expected-state/transition coverage, held-out and negative transitions, timing windows, fault/alarm paths, manual/recovery modes, restart/restore behavior, deterministic resource/cycle/jitter measurements, and negative tests for disallowed transitions/commands.

A candidate can match all recorded traces and still fail if important unobserved behavior remains outside a safe declared operating envelope.

The candidate remains non-authoritative until required acceptance criteria pass.

## Stage 9 — Existing-PLC execution proxy

When the existing PLC remains viable, ABIL may use it as the deterministic execution target while ABIL owns more of the reconstructed machine model and supervisory intent.

The interface should be narrow and semantic where practical: ABIL requests bounded operations while the PLC retains scan-timed I/O, established fieldbus behavior, local deterministic sequencing, and ordinary interlocks.

This stage may be transitional or permanent.

Before activation, define explicit control-ownership domains. For each physical output/control namespace, exactly one ordinary-control writer must be authoritative. ABIL proxy operation must not create a second writer alongside legacy HMI/PLC paths.

Required evidence includes exact PLC/project/runtime identity, documented proxy interface, command semantics, bounded command set, deterministic behavior, single-writer/fencing evidence, rollback path, outcome comparison, and preserved independent safety authority.

## Stage 10 — Supervised cutover

A validated control artifact may be promoted into limited real machine authority under explicit installation-specific authorization.

Cutover must use an explicit authority-transfer state machine and mechanically enforced fencing. The package should include exact hardware/network/protocol/deployment identity, active control artifact/version, prior validation evidence, commissioning signoff, rollback/recovery procedure, watchdog/fail-closed behavior, alarm/fault evidence, declared operating envelope, reviewed safety-interface list, control-coverage ledger, and exact authority/promotion receipt.

Cutover is incomplete until the previous writer is mechanically unable to continue authoritatively writing the transferred output/control domain and the new writer's ownership is verified.

No generic ABIL release automatically authorizes a specific machine cutover.

## Stage 11 — Direct remote-I/O control where needed

When coexistence with the legacy PLC/control system is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, the ABIL deterministic runtime may replace the ordinary controller function and communicate directly with qualified remote I/O and field devices.

This is not simply Stage 9 with the PLC removed.

Evidence must include qualified fieldbus/driver stack and interface hardware, exact I/O ownership/configuration, deterministic I/O update timing, cycle/jitter/load measurements under worst relevant conditions, watchdog/communication-loss behavior, restart/resynchronization behavior, drive/actuator handling, alarm/fault paths, rollback/recovery, target-specific negative testing, complete control-coverage evidence for the promoted operating envelope, preserved safety interfaces, and proof of single-writer fencing.

## Stage 12 — Permanent ABIL control runtime and support lifecycle

The ABIL appliance becomes the supported permanent ordinary-control computer for the installation.

Long-run qualification should cover stable deterministic execution, versioned artifact upgrades, separation between ongoing learning and active control authority, update/rollback tooling, hardware replacement/recovery, backup/export of machine model/configuration/evidence/control-coverage/active artifact, service diagnostics, auditability, protocol/vendor dependencies, and ownership/fencing restoration after restart or appliance replacement.

A permanent installation should be maintainable as a product, not only understandable by the engineer who commissioned it.

## Coexistence versus replacement decision evidence

ABIL should explicitly record why an installation remains with an existing PLC execution target or advances to direct ABIL control.

Relevant considerations include controller/project accessibility, supportability/vendor lifecycle, hardware condition/obsolescence, fieldbus/protocol support, deterministic timing, maintainability, qualified ABIL adapter/runtime availability, licensing/proprietary-tool burden, rollback/recovery risk, commissioning labor, control-coverage completeness, safety-interface certainty, and customer lifecycle requirements.

The product should not replace a still-useful PLC merely because ABIL can. It should also not make a legacy PLC mandatory when that controller is the failed or unsupportable component.

## Core evaluation metrics

ABIL should be scored on more than anomaly detection.

Important measures include prediction, calibration/uncertainty, change/regime detection, retention/adaptation, topology discovery coverage, semantic-grounding efficiency, manual onboarding/commissioning labor, machine-specific learned structure, reconstructed control-model fidelity, control-coverage completeness, unknown-state count/quarantine, generated-control validation, held-out/negative transition performance, deterministic cycle/jitter/resource metrics, restart/checkpoint equivalence, recovery/rollback time, protocol portability, split-brain/fencing tests, operator usefulness, permanent supportability, and the ability to say `insufficient evidence`.

## Kill or material-revision conditions

The ABIL thesis should be materially revised if realistic testing shows that:

- useful performance requires exhaustive hand-labeling of every signal and relationship;
- reconstruction requires essentially full conventional manual re-engineering before ABIL contributes meaningful structure;
- simple baselines match learner value at materially lower complexity/cost;
- online adaptation creates unacceptable forgetting or fault normalization;
- the model cannot remain stable during long-running operation;
- discovered relationships are mostly restatements of supplied semantics;
- generated control cannot be made inspectable, testable, and attributable to evidence;
- unobserved behavior cannot be bounded into a safe operating envelope;
- direct control cannot meet target deterministic timing/reliability;
- control ownership cannot be fenced against split-brain writers;
- protocol/vendor diversity makes each deployment a bespoke rewrite;
- deployment/commissioning labor dominates the economic value;
- uncertainty or safety-function classification remains too weak for trustworthy reconstruction;
- coexistence with surviving PLCs consistently delivers equivalent customer value at substantially lower risk/cost, in which case ABIL should emphasize reconstruction/commissioning and PLC-targeted execution rather than forcing direct takeover.

Failure of direct takeover as a universal strategy does not automatically invalidate ABIL if coexistence-first reconstruction remains commercially valuable. The product claim should narrow to what evidence supports.
