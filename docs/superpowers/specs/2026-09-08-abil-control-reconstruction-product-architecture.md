# ABIL Control Reconstruction Product Architecture

Status: **reviewer-ready proposed successor architecture; implementation remains staged, review-gated, and falsifiable**

Date: 2026-09-08

Normative companion: `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`

The companion contract is part of this proposed architecture and supplies the detailed authority, lifecycle, commissioning, command-transaction, identity, restore/anti-rollback, and safety-noninterference invariants summarized here.

## 1. Purpose

ABIL — Adaptive Brownfield Intelligence Layer — is intended to recover, reconstruct, modernize, and where necessary replace unsupported brownfield machine-control systems while preserving useful existing industrial hardware whenever practical.

The long-term product is not merely an analytics appliance. Its target form is a field-deployable industrial mini-PC that can enter an unfamiliar or partially failed automation environment, preserve useful surviving evidence, discover the control network, help a technician recover bounded manual operability, learn machine-specific behavior and semantics through observation and guided commissioning, synthesize an inspectable control model, validate candidate automation, and either cooperate with surviving controls or become the permanent ordinary-control runtime when replacement is justified.

The product principle remains:

> Learn the machine that actually exists.

The architectural strategy is **replacement-capable, coexistence-first**.

## 2. Default strategy: coexist first, replace when necessary

ABIL should not default to deleting, overwriting, or bypassing an existing PLC program merely because it is old.

The preferred order is:

1. **Preserve and observe what still exists.** Treat surviving PLCs, HMIs, drives, remote I/O, fieldbus devices, traffic, configuration, and technician knowledge as separately attributed evidence.
2. **Work with existing PLC logic when practical.** Existing ladder/function-block/structured-text logic may remain the deterministic executor while ABIL reconstructs machine behavior.
3. **Use the PLC as an execution proxy or permanent target when useful.** ABIL may issue bounded semantic requests while the PLC retains scan-time I/O, local sequencing, and established fieldbus behavior.
4. **Replace ordinary PLC/control logic only when coexistence is impossible, undesirable, uneconomic, unsupported, locked, unreliable, or itself the failed component.** ABIL's separately qualified deterministic runtime may then become the ordinary controller against qualified remote I/O and field devices.

ABIL aims to replace the *function* of an unsupported control system, not assume that modifying proprietary vendor internals is always the safest or easiest route.

## 3. Recovery workflow and evidence preservation

A representative recovery workflow is:

1. A machine remains mechanically useful but its HMI/control PC, PLC project, supervisory software, controller family, or vendor support becomes unavailable or impractical to recover.
2. If a predecessor control component is still partially alive or observable, preserve useful legacy evidence before isolation/removal whenever safe and practical. Record whether the reference is `AVAILABLE`, `CAPTURED`, `PARTIAL`, or `UNAVAILABLE`.
3. Connect the ABIL appliance through capability-qualified industrial interfaces.
4. Classify where ordinary and safety-related control authority actually lives before deciding what can be preserved or replaced.
5. Inventory reachable devices and relationships without treating addresses, names, tags, or metadata as proven stable identity or functional semantics.
6. If existing PLC logic still works, use it as evidence and, where useful, as the deterministic execution target rather than immediately replacing it.
7. Where separately authorized and capability-qualified, provide technician-facing commissioning controls only inside an independently established commissioning envelope.
8. Keep operator commands, gateway decisions, execution attempts/receipts, subsequent telemetry, technician-supplied semantics, and later causal hypotheses distinct.
9. Build a machine-specific behavioral/control model with explicit uncertainty, provenance, unknowns, and a control-coverage ledger.
10. Generate candidate automation and validate it through replay, simulation, shadow comparison where available, held-out/negative transitions, fault/recovery tests, deterministic runtime tests, and technician review.
11. Promote a candidate only through a trust domain separate from candidate generation.
12. Choose the least disruptive supportable terminal mode: read-only/advisory, deterministic manual-recovery, permanent PLC proxy/target, or direct ABIL ordinary control.
13. Any authority transfer must preserve exactly-one-writer ownership and independently authoritative safety systems.

A dead or inaccessible predecessor creates a genuine evidence gap. ABIL must preserve that provenance ceiling rather than pretending all recovery cases have equivalent evidence.

## 4. Identity and authority-locus model

`HMI/control system` is not one machine role. Before replacement planning, ABIL must classify the observed authority locus at least as one or more of:

- `SUPERVISORY_HMI_ONLY`;
- `SCADA_SUPERVISORY`;
- `SOFT_PLC_OR_CONTROL_PC`;
- `PLC_PAC_LOGIC`;
- `MOTION_OR_DRIVE_CONTROL`;
- `SAFETY_CONTROL`;
- `MIXED`;
- `UNKNOWN`.

Unknown authority locus blocks takeover authority.

Identity also has layers. Keep deployment/machine identity, immutable topology generation, logical node/device identity, time-bound endpoint/address observations, source-scoped signal/channel identity, and adapter instance/configuration identity distinct. An IP address, DeviceNet node number, PROFIBUS address, PLC slot, tag name, assembly/register, or similar locator is evidence about where a device was observed, not globally stable device identity.

The immediate non-actuating R2 substrate must preserve collision-safe source-scoped learner identity without exposing privileged physical provenance as a learner oracle.

## 5. Control deployment modes

### 5.1 Mode A — coexistence / discovery

The existing controller remains authoritative for ordinary automation.

Discovery capability is graded:

1. **Passive observation** — no active query traffic introduced by ABIL.
2. **Low-impact reads** — bounded authenticated/configuration reads with declared rates and timeout/retry behavior.
3. **Active enumeration** — browse, scan, broadcast, connection, or vendor-specific discovery that may be disruptive even without writes.
4. **Commissioning/write capability** — separately qualified, authorized, and constrained.
5. **Deterministic control capability** — separately qualified real-time ordinary-control capability.

Qualification for one level does not imply qualification for another. `Read-only` does not mean `operationally harmless`.

### 5.2 Mode B — PLC execution proxy / target

ABIL owns more of the reconstructed semantic/control model while an existing PLC remains the deterministic I/O executor.

The interface should be narrow and explicit. ABIL may request semantic operations such as `clamp_extend`, `conveyor_run`, or `index_station`, while the PLC continues to execute the actual fieldbus writes, scan-timed sequencing, and local deterministic behavior.

Mode B may be **transitional or permanent**. It is a legitimate supported end state, not a failed attempt to reach direct control.

### 5.3 Mode C — direct ABIL ordinary-control runtime

When the legacy ordinary controller cannot or should not remain, ABIL may replace its function with a separately engineered deterministic runtime that:

- scans/receives qualified remote I/O;
- executes an approved machine state/sequence model;
- runs deterministic timers and ordinary interlocks;
- handles protocol-specific I/O update semantics;
- commands drives, valves, actuators, and other ordinary-control outputs through qualified adapters;
- exposes alarms, operator state, and manual controls;
- records execution evidence and faults;
- enters the installation's validated safe-state/fallback behavior on relevant faults rather than assuming one universal physical `fail-closed` state.

Direct takeover is a capability and authority promotion, not a configuration convenience.

## 6. Intelligence, candidate, promotion, and deterministic-runtime separation

ABIL must not make a general-purpose learner, LLM, Python process, or continuously changing ML policy the real-time machine controller.

### 6.1 Intelligence / commissioning plane

Responsible for discovery, telemetry normalization, semantic grounding, behavioral learning, regime/change discovery, causal-hypothesis management, operator-guided commissioning, control-model synthesis, simulation/replay/shadow comparison, and diagnostics/evidence presentation.

It may generate candidate artifacts and candidate evidence. It cannot activate them.

### 6.2 Validation/evidence plane

Produces evidence about a candidate: replay, simulation, shadow, coverage, timing, resource, fault-path, and commissioning results. Passing tests does not itself grant authority.

### 6.3 Promotion-authority plane

A separately authorized principal/process reviews an exact candidate package and, when authorized, emits authenticated/integrity-protected promotion material bound to the deployment, authority domain, topology generation, source model/evidence, semantic/provenance cut where material, control coverage, generated artifact, target runtime/hardware/network/protocol/configuration, generator/compiler/translator identity and configuration where material, safety-interface inventory, validation set, operating envelope, fallback policy, rollback target, current authority-grant identity, signoff, and monotonic authority generation.

A process label, role name, or self-asserted approval is not an authority root. Before write-capable implementation, admission requires a current, independently rooted `AuthorityGrant` (or equivalent) binding issuer/trust material, authorized subject, exact deployment and authority domain/output scope, permitted capability/action scope, validity/currentness, monotonic generation, revocation/supersession, and verifier identity. Candidate, learner, evaluator, plugin, and runtime-subject principals cannot create or widen that grant. Deployment authority and artifact-promotion authority remain separate scopes/receipts even if one qualified organization or person holds both.

### 6.4 Protected active-artifact / loader state

Candidate-generation, learner, LLM, and plugin principals cannot write the active artifact store, promotion trust material, loader selection, next-boot target, or current authority ledger.

### 6.5 Deterministic loader/runtime

The loader/runtime independently verifies the authenticated promotion, exact artifact identity, deployment binding, authority generation, and ownership state before activation and again on restart.

Activation must be atomic or transactionally equivalent. Missing, partial, corrupt, mismatched, unauthenticated, unpromoted, wrong-deployment, or stale material does not become active.

## 7. Learner-independent degraded/manual operation

Once deterministic control or a known-good manual/recovery surface is promoted, adaptive-learning, LLM, and diagnostic-synthesis services must not become a single point of failure for that capability.

Process isolation, resource reservation, startup ordering, watchdogs, and recovery behavior must support declared degraded states in which intelligence services can crash, stall, be disabled, or be upgraded while the already-qualified deterministic/manual capability either continues inside its operating envelope or transitions according to the installation-specific validated fallback policy.

## 8. Control synthesis and coverage

ABIL should not equate `generate automation` with unconstrained source-code generation.

The preferred intermediate artifact is an inspectable machine-control model containing, as applicable:

- states and modes;
- transitions;
- prerequisites/permissives;
- requested actions;
- expected observations and claimed consequences with provenance;
- timing windows;
- ordinary interlocks independently classified as non-safety;
- alarm/fault conditions;
- recovery paths;
- operator/manual modes;
- unresolved relationships and uncertainty.

That model can be translated to an existing vendor PLC, a PLC-proxy interface, the ABIL deterministic runtime, or another supported controller.

Every candidate artifact also carries a **control-coverage ledger**. Each state, transition, command, permissive, timeout, recovery path, and ordinary interlock within the proposed operating envelope must identify the evidence/requirements supporting it and whether it was observed, technician-specified, vendor-specified, inferred, simulated, or tested.

`Not observed` means **not authorized by inference alone**. Unknown or insufficiently covered behavior must be excluded, remain technician-engineered, or be explicitly outside the promoted operating envelope. Matching recorded traces is necessary but not sufficient.

## 9. Vendor PLC and fieldbus treatment

Existing PLCs may be evidence/configuration sources, observed-behavior sources, deterministic execution proxies, permanent execution targets, or replaceable legacy components.

ABIL should not assume it can safely overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other proprietary projects. Hardware configuration, I/O ownership, produced/consumed data, fieldbus master configuration, firmware, licensing, protection/password state, motion configuration, safety signatures, engineering-tool requirements, and project formats can make vendor-project mutation inappropriate or impractical.

Direct rewrite is a target-specific migration path, not the universal onboarding mechanism.

Direct-control capability is protocol/interface-specific. Potential targets include EtherNet/IP, PROFINET, Modbus TCP/RTU, DeviceNet, PROFIBUS, CAN/CANopen, vendor-specific drive/motion networks, and serial/gateway-connected I/O. A read/discovery adapter is not automatically a deterministic-control adapter.

## 10. Guided commissioning and transactional physical action

Discovery cannot be assumed to reveal reliable functional semantics such as `infeed_clamp_extend` or `station_complete`.

The commissioning loop is conceptually:

`observe -> propose candidate relationship -> technician-authorized bounded action -> record execution evidence and subsequent observations -> technician confirm/correct semantics -> derive/update hypotheses -> retain provenance -> update machine model`

Do not collapse `OperatorCommand`, `ActionProposal`, `GatewayDecision`, `ActionExecutionAttempt`, `ExecutionReceipt`, `TelemetryObservation`, and `CausalHypothesis/Attribution` into one answer-bearing record. An observation following an action is not automatically a proven `ACTION_CONSEQUENCE`.

Before any commissioning write, an installation-specific **independent commissioning envelope** must exist. It is deny-by-default and does not rely solely on the model being investigated. As applicable it defines independently established prerequisites, prohibited output/state combinations and sequences, action duration/extent/rate limits, supervision and stop/disable requirements, target-appropriate jog/hold-to-run/reduced-energy semantics, and explicit `UNKNOWN` handling. An unresolved required prerequisite blocks the action.

Write-capable manual/proxy actions also require a transaction envelope bound to the exact deployment, authority domain, current authority epoch, current ownership/fencing generation, and unique request identity. It records operation/parameters, relevant precondition version, freshness/expiry, acknowledgement lifecycle, idempotency/duplicate policy, timeout/reconnect behavior, queue/backpressure rules, target correlation where available, and durable request→decision→attempt→receipt linkage.

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` is durable. A lost acknowledgement or reconnect does not prove non-execution and never authorizes blind retry of an ambiguous non-idempotent action. Unresolved old-generation commands remain quarantined across restart, cutover, rollback, or ownership transfer; stale receipts cannot complete new-generation requests.

## 11. Safety boundary, classification, and noninterference

This architecture expands ABIL's long-term scope to ordinary machine-control replacement. It does **not** silently expand ABIL into automatic replacement of safety functions.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

The default classification rule is:

> **Unknown protective/interlock semantics are safety-relevant and out of scope for autonomous reconstruction until a current, independently authorized safety-classification record establishes otherwise.**

Any later classification or downgrade to ordinary control requires a current `SafetyClassificationRecord` (or equivalent safety-project record) independent of the ordinary ABIL candidate/learner/evaluator planes. It binds the classifier/signoff authority, exact deployment and topology generation, hazard/safety context, evidence digest/set, classification scope and affected asset/semantics, validity/currentness, and revocation/supersession. Ordinary ABIL cannot create, refresh, or approve it. Until a current record exists, the conservative safety-relevant classification remains authoritative.

Ordinary ABIL discovery, commissioning, proxy, and direct-control authority is negatively scoped away from safety ownership/configuration/effect absent separate safety-project authority. Ordinary ABIL must not claim safety-device ownership, download/reset/reconfigure safety projects or signatures, change drive safety/network ownership, bypass/mask/spoof protective paths, or alter shared infrastructure in a way that silently disables independent safety.

Direct-control qualification must test safety noninterference under applicable startup/restart, ABIL runtime failure, intelligence-plane failure, communication loss, adapter/driver failure, cutover, rollback, and shared-infrastructure fault/recovery conditions.

Physical safe-state/fallback behavior remains installation-specific and must be independently qualified for the actual hazard context.

## 12. Single-writer control ownership and authority transfer

For every physical output/control namespace, exactly one authoritative ordinary-control writer may exist at a time, or the namespace is explicitly in a non-authoritative/unknown/conflicted state.

The ownership contract defines control domains, current writer, authority/ownership generation, acquisition/release, protocol/configuration/credential/physical fencing, stale-command rejection, restart/partial-failure behavior, rollback/fallback semantics, and transfer receipts.

Representative authority-transfer states include:

- `LEGACY_AUTHORITY_ACTIVE`;
- `TRANSFER_PREPARED`;
- `LEGACY_QUIESCED_VERIFIED`;
- `ABIL_PROXY_AUTHORITY_ACTIVE`;
- `ABIL_DIRECT_AUTHORITY_ACTIVE`;
- `ROLLBACK_PREPARED`;
- `ROLLBACK_ACTIVE`;
- `NO_ACTIVE_AUTHORITY`;
- `DUAL_AUTHORITY_CONFLICT`;
- `AUTHORITY_OUTCOME_UNKNOWN`.

Cutover is complete only when the previous writer is mechanically unable to continue authoritatively writing the transferred domain and the new writer's ownership is verified.

If transfer occurs while a physical command outcome remains ambiguous, that command remains quarantined under its prior authority/ownership generation. Neither the new writer nor a restored old writer may silently reissue it.

## 13. Authority epoch, restore, revocation, and rollback

Control authority is not ordinary checkpoint state.

Authority-bearing state uses a monotonic separately authenticated `authority_epoch` or equivalent durable generation. Ordinary learner/model/configuration backup restoration cannot grant, downgrade, or resurrect authority.

Revocation and supersession survive restart, restore, and appliance replacement. An old but cryptographically valid promotion cannot silently reactivate after a newer promotion, revocation, ownership transfer, safety/configuration change, or authority epoch.

Rollback to older known-good artifact bytes requires a **new** separately authorized rollback/promotion receipt at a newer authority generation. Rollback does not restore the historical authority epoch or historical command/receipt state.

If the current authority ledger is missing, corrupt, divergent, or untrusted, no new write authority is inferred.

## 14. Orthogonal state domains and branching deployment graph

ABIL must not use one ordinal `stage` as a substitute for several different state dimensions.

Keep at least these subjects distinct:

1. **ProductCapabilityQualification** — what an ABIL build/release is globally qualified to do for a declared profile.
2. **DeploymentCommissioningState** — what this installation has actually established.
3. **ExecutionAuthorityState** — who currently owns each ordinary-control namespace.
4. **ControlArtifactLifecycle** — generated, validated, promoted, active, superseded, revoked, rollback-candidate, retired.
5. **SupportRecoveryState** — permanent support, degraded/manual state, recovery readiness, hardware replacement/restoration.

The common evidence path may include substrate qualification, learner efficacy, replay, live read-only discovery, advisory/semantic grounding, bounded commissioning, machine-model reconstruction, candidate synthesis, and offline/shadow validation.

After that common work, the deployment **branches**. Valid supported terminal modes include:

- **READ_ONLY / ADVISORY** — no write authority;
- **MANUAL_RECOVERY** — deterministic technician controls inside an approved envelope;
- **PLC_PROXY** — surviving PLC remains deterministic executor, potentially permanently;
- **DIRECT_ABIL_CONTROL** — separately qualified ABIL deterministic runtime owns ordinary I/O domains.

A globally qualified capability never grants a particular deployment authority, and direct-control capability never forces a deployment to abandon a safer permanent PLC-proxy route.

## 15. Product packaging direction

The likely physical product is an industrial edge appliance rather than an APK or ordinary desktop application.

A plausible package is a rugged/fanless mini-PC, appropriate industrial Ethernet and fieldbus interfaces, bootable installer/recovery media, a small Linux-based appliance OS, ABIL intelligence/commissioning services, deterministic control runtime, persistent deployment/machine-model/configuration/evidence storage, local operator/service interface, and export/backup/restore tooling.

Tiny Core/CorePure64, a stripped Debian-family appliance, or another compact Linux base may be evaluated later. The architecture does not yet bind ABIL to one distribution.

## 16. Persistent machine/deployment state

The valuable ABIL state is created during discovery, learning, commissioning, synthesis, validation, and operation. It does not pre-exist before ABIL arrives.

Keep at least these state classes distinct:

- learner state;
- evidence/machine-model state;
- candidate-artifact state;
- deterministic runtime operational state;
- authority state.

Persistent records may include discovered topology, identity observations, control-authority-locus classification, adapter/protocol configuration, operator semantics with provenance, learned machine model, evidence/history, control-coverage ledger, candidates, validation receipts, promoted artifact/version, authenticated promotion binding, ownership/fencing state, fallback policy reference, runtime configuration, deployment identity, and software/schema/config versions.

Ordinary learner/evidence backup is insufficient to recreate authority state. Cross-machine/schema/config/software reuse is a separate explicit migration/transfer operation.

## 17. Relationship to frozen F0 R1 review

The 2026-09-06 foundation/F0 subject and its R1 review remain historical evidence of the earlier, narrower architecture. Do not rewrite that reviewed source to pretend this broader direction was already present.

The broader product direction adds future capability stages; it does not weaken admitted R1 requirements.

## 18. Corrected early-substrate evidence model

The immediate successor substrate preserves a strict three-plane evidence model:

- **EvaluatorRecord** — may contain hidden fixture/regime/fault truth, rich provenance, scoring labels, and other evidence not necessarily learner-visible.
- **LearnerEvent** — a closed, typed, allowlisted projection containing only preregistered learner evidence. Unknown/unregistered fields fail closed; no arbitrary metadata bag crosses into the learner plane.
- **EvaluationJoin** — scoring-only association between learner outputs/evidence positions and evaluator truth. Learner/plugin code has no object/API/capability path back to evaluator/world hidden state.

Raw learner events remain asynchronous. Grouping, resampling, interpolation, windowing, and vector construction belong to a separately versioned feature-assembly contract with deterministic replay semantics.

Learner-visible identity must be collision-safe without exposing privileged physical provenance as an oracle. Transport/device status, externally supplied confidence/annotation, and learner/model uncertainty remain separate evidence classes.

Checkpoint compatibility must bind source/deployment/adapter/event-schema/feature-assembly/learner/codec/software/frontier identities and integrity, with restart-equivalence and stale/ahead/corrupt/wrong-identity rejection tests.

## 19. Immediate R2 gate split

The next R2 subject must not conflate substrate honesty with learner/product efficacy.

### 19.1 `R2-SUBSTRATE-QUALIFIED`

Asks whether the corrected early substrate is implementation-ready as an honest non-actuating experimental/runtime foundation. It includes evaluator/learner separation and noninterference, event identity/currentness, prequential evidence ordering, asynchronous assembly, deterministic replay/corpus identity, checkpoint trust binding and restart equivalence, fair paired baselines, recomputable evidence, resource bounds, opaque-label controls, and the ability to report that a simple baseline wins or no useful learner advantage exists.

This gate does **not** require the first learner to discover nontrivial structure or outperform baselines.

### 19.2 `R2-LEARNER-EFFICACY`

Separately asks whether a particular learner earns product/learning claims. It may require preregistered evidence such as useful nontrivial machine-specific learned structure, agreed baseline comparison, recurrence/forgetting/adaptation behavior, uncertainty/change quality, opaque-label performance, and onboarding/semantic-efficiency evidence.

### 19.3 Long-term compatibility question

A corrected early substrate must avoid commitments that block later coexistence-first control reconstruction. It must preserve extensibility for later topology/device/capability/semantic/coverage/authority subjects without importing later control privileges or privileged plant provenance into learner state.

The immediate R2 remains zero-industrial-write by scope.

## 20. Long-term product success criteria

ABIL earns the stronger product claim only if it can demonstrate that it can:

1. enter a real brownfield environment with incomplete documentation;
2. preserve useful predecessor evidence where available and honestly represent missing evidence;
3. inventory useful surviving components without conflating addresses/names with stable identity or functional semantics;
4. classify the control-authority locus before replacement planning;
5. become useful without exhaustive manual semantic programming;
6. support independently bounded technician commissioning without trusting the unknown model to define its own admissibility;
7. reconstruct an inspectable machine-control model with explicit unknown-state coverage;
8. validate generated automation against recorded, simulated, shadow, held-out, negative-transition, fault/recovery, and operator evidence;
9. work with an existing PLC when that is the safer/easier route, including permanent PLC-proxy support;
10. replace ordinary PLC control when the legacy controller cannot remain viable;
11. preserve independent safety authority and prove ordinary-ABIL noninterference;
12. mechanically prevent split-brain ordinary-control writers;
13. keep physical-command ambiguity durable across restart and authority transfer without unsafe retries;
14. make promotion authority mechanically separate from candidate generation and loader selection;
15. prevent backup/restore from resurrecting stale promotions, revocations, writers, or commands;
16. keep already-promoted deterministic/manual recovery capability available independently of learner-service failure according to the qualified operating design;
17. run promoted ordinary control deterministically and stably for the target hardware/network;
18. provide a supportable permanent product rather than a one-off engineering demo.

## 21. Explicit non-goals for the current successor design

This document does not yet choose a specific appliance Linux distribution, first write-capable fieldbus, first vendor PLC migration target, deterministic-controller language/runtime, RTOS/real-time kernel strategy, HMI framework, safety PLC replacement strategy, automatic rewriting of arbitrary proprietary PLC projects, cloud dependence, remote fleet management, or pricing/licensing/legal structure.

Those choices should be forced by qualification evidence and the first concrete field target rather than prematurely frozen.
