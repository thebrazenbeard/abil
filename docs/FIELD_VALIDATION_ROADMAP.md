# ABIL Field Validation Roadmap

Status: **working validation graph; no deployment authorization implied**

The early roadmap is ordered so each capability can fail cheaply before ABIL earns access to a harder environment or stronger capability. After the common reconstruction/validation work, deployment paths branch; the numbers below are evidence/qualification milestones, not one universal per-installation ordinal state machine.

Product capability qualification, deployment commissioning state, execution authority, control-artifact lifecycle, and support/recovery state are separate axes. Passing a product qualification stage never grants a particular machine deployment authority.

`docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md` is the normative proposed companion for authority, commissioning, transaction, identity, restore, and permanent-mode lifecycle rules.

## Cross-stage invariants

Every stage inherits these rules:

- control-substrate qualification and learner-efficacy qualification are separate;
- passive observation, bounded reads, active discovery, commissioning writes, proxy control, and direct deterministic control are distinct capability levels;
- useful predecessor evidence should be captured before isolation when it remains safely available; unavailable predecessor evidence lowers the reconstruction evidence ceiling rather than being silently ignored;
- mutable addresses/locators are not stable device identity;
- unknown or unobserved control behavior is not silently promoted;
- unknown protective/interlock semantics are safety-relevant until independently classified;
- ordinary ABIL capability is negatively scoped away from safety ownership/configuration/effect absent a separate safety-engineering authority;
- each physical output/control namespace has exactly one authoritative ordinary-control writer at a time;
- generated control remains a candidate until separately authenticated promotion, protected active-artifact selection, and independent runtime verification succeed;
- authority-bearing state has monotonic anti-rollback semantics and is not recreated by ordinary learner/model restore;
- physical command ambiguity is preserved: timeout/reconnect does not prove non-execution and never licenses blind retry of an ambiguous non-idempotent action;
- independent safety systems remain authoritative unless a separate safety-engineering project explicitly changes that contract;
- physical safe-state/fallback behavior is target-specific rather than one universal `fail-closed` response;
- promoted deterministic/manual recovery capability must not depend on the adaptive-learning plane remaining healthy.

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

Before any isolation/removal of a partially functioning predecessor, capture safe/relevant predecessor evidence where practical: controller/HMI configuration, project state where accessible, observed traffic, I/O/tag mappings, protocol/mastership state, command/response timing, and rollback/fallback information. Record whether legacy reference evidence is captured, partial, unavailable, or unsafe to acquire.

The first live objective is deliberately narrow:

> Can ABIL observe an unfamiliar real system long enough to learn machine-specific predictive relationships that are useful to an experienced human without exhaustive manual mapping?

Before connection, the deployment must declare its discovery profile:

- passive observation only;
- bounded authenticated/configuration reads;
- active enumeration/browse/scan;
- no write/commissioning capability.

If active discovery is used, evidence must include target allowlists, scan/query budgets, rate limits, timeout/retry behavior, and known side effects. `Read-only` is not evidence that the network interaction is operationally harmless.

Expected evidence includes exact deployment/topology/adapter/protocol identity, observed signal/schema inventory, acquisition/drop statistics, checkpoint/model identity, preregistered baseline comparison, opaque-label results where feasible, operator usefulness assessment, resource/stability evidence, and external proof that machine writes are unavailable.

## Stage 3 — Operator-facing advisory mode

ABIL remains unable to directly change machine state but may surface predictions, changes, ranked hypotheses, evidence, uncertainty, topology/device relationships, candidate semantic groupings, proposed observations/tests, and explicit unknowns.

The interface should let the operator mark findings as useful, wrong, obvious, supplied, inferred, unresolved, or safety-classification-required.

## Stage 4 — Guided semantic commissioning

ABIL begins explicit human-in-the-loop reconstruction of machine meaning.

Before any action capability is introduced, the deployment should classify the observed legacy control-authority locus as supervisory HMI, SCADA, soft PLC/control PC, ordinary PLC/PAC logic, motion/drive control, safety control, mixed, or unknown.

The technician may identify known devices/functions, confirm/correct proposed relationships, and describe signals, commands, sensors, actuators, and sequence states.

ABIL must keep operator command, gateway decision, execution attempt/receipt, subsequent telemetry, and later causal attribution distinct. A subsequent observation is not automatically a proven `ACTION_CONSEQUENCE`.

ABIL must preserve provenance between discovered topology/configuration, behavior learned from telemetry, technician-supplied semantics, vendor-supplied semantics, and unresolved hypotheses.

The key question is whether targeted technician interaction grounds enough semantics to make ABIL useful without turning commissioning into full manual re-engineering.

Evidence should include discovery coverage, manual semantic declarations, commissioning time, inferred relationships before/after grounding, corrections/retractions, and learner-efficacy evidence that survives semantic ablation where the claim requires it.

## Stage 5 — Constrained manual-control gateway

Where technically supported and separately authorized, ABIL may present bounded manual-control requests for commissioning and diagnostic use.

The technician remains the initiator/approver. The learning plane receives no unrestricted write capability.

Before any write, the installation must have an **independent commissioning envelope** whose admissibility constraints do not rely solely on the not-yet-qualified model. As applicable, it includes deny-by-default writable scope, independently established prerequisites, prohibited output/state combinations and sequences, duration/extent/rate limits, supervision, independent stop/disable path, jog/hold-to-run/reduced-energy semantics, and explicit `UNKNOWN` handling. A required independent prerequisite in `UNKNOWN` blocks the action.

Every physical action must use a transaction envelope with stable request identity, deployment/authority domain, current authority/ownership generation, exact operation/parameters, relevant state/precondition version, freshness/expiry, declared acknowledgement lifecycle, duplicate/idempotency policy, timeout/reconnect semantics, bounded queue/backpressure, and durable request→decision→attempt→receipt linkage.

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` is first-class. A lost acknowledgement or reconnect does not prove a command failed or never executed. Non-idempotent/ambiguous actions are not automatically retried unless the target-specific contract proves retry safe.

Promotion evidence includes exact target hardware/protocol/deployment identity, exact allowed command set, independent commissioning envelope, external protective/safety prerequisites, request replay protection, ambiguity/idempotency behavior, negative tests for disallowed combinations/order/state, rollback/disable path, and proof that learner/plugin code cannot directly access write credentials or handles.

Unknown protective/interlock semantics remain out of autonomous reconstruction and must not be bypassed.

The manual/recovery surface should be architected so a later qualified version can remain usable even when adaptive-learning services are unavailable.

## Stage 6 — Machine-model reconstruction

ABIL constructs an inspectable behavioral/control model from accumulated evidence.

The model should represent states/modes, transitions, commands/actions, expected observations and claimed consequences with provenance, timing, prerequisites/permissives, ordinary interlocks independently classified as non-safety, alarm/fault conditions, recovery paths, manual modes, provenance, uncertainty, and unresolved explanations.

The objective is not to reproduce ladder syntax. It is to reconstruct ordinary machine-control behavior in a representation that can be reviewed, tested, and translated to multiple execution targets.

Every reconstructed behavior must begin accumulating a **control-coverage ledger** stating whether it was observed, technician-specified, vendor-specified, inferred, simulated, or tested.

`Not observed` is not equivalent to `safe to omit`.

## Stage 7 — Candidate control synthesis

ABIL may generate a candidate automation artifact from an approved machine model.

Possible targets include a conventional vendor PLC program/project, a narrow PLC execution-proxy interface, the ABIL deterministic control runtime, or another supported industrial controller.

Generation confers no machine authority.

Every candidate must bind source machine-model/evidence version, semantic/provenance cut where material, target runtime/controller profile, exact protocol/I/O assumptions, control-authority locus, topology generation, preserved safety interfaces/handshakes, unresolved assumptions, control-coverage ledger, and generated artifact identity.

Any state, transition, permissive, timeout, recovery path, or ordinary interlock lacking sufficient support remains excluded, outside authority, or technician-engineered rather than guessed into the executable envelope.

## Stage 8 — Replay, simulation, and shadow validation

Candidate automation is tested before any promotion.

Validation should include recorded replay, synthetic/digital-process simulation, shadow comparison where a surviving controller exists, expected-state/transition coverage, held-out and negative transitions, timing windows, fault/alarm paths, manual/recovery modes, restart/restore behavior, deterministic resource/cycle/jitter measurements, and negative tests for disallowed transitions/commands.

A candidate can match all recorded traces and still fail if important unobserved behavior remains outside a safe declared operating envelope.

Validation produces evidence; it does not itself promote the candidate.

## Post-validation branch A — permanent read-only/advisory or manual-recovery support

Some installations may remain permanently read-only/advisory, or may use a separately qualified deterministic manual-recovery surface without transferring normal automatic control to ABIL.

These are valid supportable end states when they satisfy customer needs and the relevant capability/commissioning contract. They are not failed attempts to reach direct takeover.

## Post-validation branch B — existing-PLC execution proxy / permanent PLC target

When the existing PLC remains viable, ABIL may use it as the deterministic execution target while ABIL owns more of the reconstructed machine model and supervisory intent.

The interface should be narrow and semantic where practical: ABIL requests bounded operations while the PLC retains scan-timed I/O, established fieldbus behavior, local deterministic sequencing, and ordinary interlocks.

This branch may be transitional **or permanent**.

Before activation, define explicit control-ownership domains. For each physical output/control namespace, exactly one ordinary-control writer must be authoritative. ABIL proxy operation must not create a second writer alongside legacy HMI/PLC paths.

Proxy commands inherit the Stage-5 transaction/ambiguity/idempotency contract. Reconnect must not silently replay unknown physical operations.

Required evidence includes exact PLC/project/runtime identity, documented proxy interface, command semantics, bounded command set, deterministic behavior, single-writer/fencing evidence, transaction/ambiguity behavior, rollback path, outcome comparison, and preserved independent safety authority.

A permanent PLC-proxy deployment then enters the same support-lifecycle discipline described below; it does not need direct I/O takeover merely to count as a permanent ABIL installation.

## Post-validation branch C — supervised direct-control cutover

A validated control artifact may be promoted into real ordinary machine authority only under explicit installation-specific authorization and after write-capable product/runtime qualification for the exact target profile.

Promotion must occur through a trust boundary separate from candidate generation. The promotion authority emits authenticated/integrity-protected material that binds:

- exact hardware/network/protocol/deployment identity;
- topology generation and ownership domain;
- active control artifact digest/version;
- source machine-model/evidence version;
- semantic/provenance cut where material;
- control-coverage ledger version;
- prior validation evidence set and acceptance result;
- preserved safety-interface/handshake inventory;
- target-specific validated safe-state/fallback policy;
- commissioning/authority signoff;
- known-good rollback artifact/configuration;
- monotonic authority generation/epoch.

The deterministic loader/runtime independently verifies the exact promotion and artifact before activation and on restart. Candidate/learner/LLM/plugin principals cannot write active artifact storage, promotion trust material, loader selection, or the current authority ledger.

Activation must be atomic or transactionally equivalent. Missing, partial, corrupt, mismatched, unauthenticated, unpromoted, wrong-deployment, or stale authority material does not become active.

Cutover uses explicit authority-transfer state and mechanically enforced fencing. It is incomplete until the previous writer is mechanically unable to continue authoritatively writing the transferred domain and the new writer's ownership is verified.

No generic ABIL release automatically authorizes a specific machine cutover.

## Direct remote-I/O control qualification

When coexistence with the legacy PLC/control system is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, the ABIL deterministic runtime may replace the ordinary controller function and communicate directly with qualified remote I/O and field devices.

This is not simply PLC proxy with the PLC removed.

Evidence must include qualified fieldbus/driver stack and interface hardware, exact I/O ownership/configuration, deterministic I/O update timing, cycle/jitter/load measurements under worst relevant conditions, watchdog/communication-loss behavior, restart/resynchronization behavior, drive/actuator handling, alarm/fault paths, rollback/recovery, target-specific negative testing, complete control-coverage evidence for the promoted operating envelope, preserved safety interfaces, safety-noninterference tests, proof of single-writer fencing, authenticated promotion/authority-epoch verification, and target-specific safe-state/fallback qualification.

Ordinary ABIL must be technically unable to claim ownership of, reconfigure, reset, bypass, or otherwise mutate independent safety systems absent a separately engineered safety project. Qualification must show the preserved safety path remains effective under applicable startup/restart, intelligence-plane failure, runtime failure, communication loss, adapter failure, cutover, rollback, and shared-infrastructure fault cases.

The deterministic runtime must also be tested with adaptive-learning/LLM/diagnostic services intentionally stopped or faulted to demonstrate that promoted control/manual recovery capability degrades according to the qualified design rather than collapsing with the intelligence plane.

## Permanent support lifecycle — applies to every supported terminal mode

Permanent support is not synonymous with direct ABIL control. Read-only/advisory, manual-recovery, PLC-proxy, and direct-control deployments may each enter an appropriate permanent support lifecycle.

Long-run qualification should cover, as applicable, stable operation, versioned artifact/config upgrades, separation between ongoing learning and active control authority, update/rollback tooling, hardware replacement/recovery, backup/export of machine model/configuration/evidence/control coverage, service diagnostics, auditability, protocol/vendor dependencies, ownership/fencing recovery, and target-specific fallback behavior.

For authority-bearing deployments, active promotion/authority state is restored under separate monotonic anti-rollback rules. Ordinary backup restoration cannot grant, downgrade, or resurrect authority. A cryptographically valid historical artifact can be rolled back only through a new authorized rollback/promotion receipt at a newer authority generation; an old authority epoch is never revived simply because old bytes were restored.

The appliance must have learner-independent degraded modes. Failure, restart, upgrade, or intentional shutdown of adaptive-learning services must not by itself remove an already-qualified deterministic/manual recovery capability. Resource reservation and process isolation must prevent the intelligence plane from starving the deterministic runtime.

A permanent installation should be maintainable as a product, not only understandable by the engineer who commissioned it.

## Coexistence versus replacement decision evidence

ABIL should explicitly record why an installation remains read-only/manual, stays with an existing PLC execution target, or advances to direct ABIL control.

Relevant considerations include controller/project accessibility, predecessor evidence quality, supportability/vendor lifecycle, hardware condition/obsolescence, fieldbus/protocol support, deterministic timing, maintainability, qualified ABIL adapter/runtime availability, licensing/proprietary-tool burden, rollback/recovery risk, commissioning labor, control-coverage completeness, safety-interface certainty, learner-independent degraded-operation capability, and customer lifecycle requirements.

The product should not replace a still-useful PLC merely because ABIL can. It should also not make a legacy PLC mandatory when that controller is the failed or unsupportable component.

## Core evaluation metrics

ABIL should be scored on more than anomaly detection.

Important measures include prediction, calibration/uncertainty, change/regime detection, retention/adaptation, topology/device discovery coverage, semantic-grounding efficiency, manual onboarding/commissioning labor, predecessor-evidence coverage, machine-specific learned structure, reconstructed control-model fidelity, control-coverage completeness, unknown-state count/quarantine, generated-control validation, held-out/negative transition performance, deterministic cycle/jitter/resource metrics, restart/checkpoint equivalence, recovery/rollback time, protocol portability, split-brain/fencing tests, promotion trust-root isolation, authority-epoch/anti-rollback tests, commissioning-envelope falsifiers, command ambiguity/idempotency tests, safety-noninterference tests, learner-independent degraded-operation tests, operator usefulness, permanent supportability, and the ability to say `insufficient evidence`.

## Kill or material-revision conditions

The ABIL thesis should be materially revised if realistic testing shows that:

- useful performance requires exhaustive hand-labeling of every signal and relationship;
- reconstruction requires essentially full conventional manual re-engineering before ABIL contributes meaningful structure;
- simple baselines match learner value at materially lower complexity/cost;
- online adaptation creates unacceptable forgetting or fault normalization;
- the model cannot remain stable during long-running operation;
- discovered relationships are mostly restatements of supplied semantics;
- generated control cannot be made inspectable, testable, and attributable to evidence;
- unobserved behavior cannot be bounded into a supportable operating envelope;
- direct control cannot meet target deterministic timing/reliability;
- control ownership cannot be fenced against split-brain writers;
- candidate generation cannot be mechanically separated from promotion/active-artifact authority;
- restore/restart can resurrect stale control authority or a revoked writer;
- commissioning cannot be safely bounded without relying on the model being investigated;
- physical-command ambiguity cannot be represented/reconciled without unsafe retries;
- ordinary ABIL operation cannot preserve independent safety-system ownership/effect;
- deterministic/manual recovery capability cannot survive learner-service failure according to a qualified degraded-mode design;
- protocol/vendor diversity makes each deployment a bespoke rewrite;
- deployment/commissioning labor dominates the economic value;
- uncertainty or safety-function classification remains too weak for trustworthy reconstruction;
- coexistence with surviving PLCs consistently delivers equivalent customer value at substantially lower risk/cost, in which case ABIL should emphasize reconstruction/commissioning and PLC-targeted execution rather than forcing direct takeover.

Failure of direct takeover as a universal strategy does not automatically invalidate ABIL if coexistence-first reconstruction remains commercially valuable. The product claim should narrow to what evidence supports.
