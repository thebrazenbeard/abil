# ABIL Control Reconstruction Product Architecture

Status: **reviewer-ready proposed successor architecture; implementation remains staged, review-gated, and falsifiable**

Date: 2026-09-08

## 1. Purpose

ABIL — Adaptive Brownfield Intelligence Layer — is intended to recover, reconstruct, modernize, and where necessary replace unsupported brownfield machine-control systems while preserving useful existing industrial hardware whenever practical.

The long-term product is not merely an analytics appliance. Its target end state is a field-deployable industrial mini-PC that can enter an unfamiliar or partially failed automation environment, discover the surviving control network, help a technician recover manual operability, learn machine-specific behavior and semantics through observation and guided commissioning, synthesize a replacement control model, validate that model, and eventually operate as the permanent ordinary-control runtime when the original supervisory/control software or PLC logic can no longer be relied upon.

The product principle remains:

> Learn the machine that actually exists.

This successor architecture expands that principle from observation and diagnosis into controlled reconstruction of ordinary automation behavior.

## 2. Default strategy: coexist first, replace when necessary

ABIL should not default to deleting, overwriting, or bypassing an existing PLC program merely because it is old.

The preferred order is:

1. **Discover and observe the existing system.** Treat surviving PLCs, HMIs, drives, remote I/O, fieldbus devices, network traffic, configuration, and technician knowledge as separately attributed evidence.
2. **Work with the existing PLC logic when practical.** Existing ladder/function-block/structured-text logic may remain the deterministic executor while ABIL learns and reconstructs machine behavior.
3. **Use the existing PLC as an execution proxy when useful.** ABIL may issue bounded high-level requests through a narrow interface while the PLC continues to own scan-time I/O, local interlocks, and established fieldbus behavior.
4. **Replace ordinary PLC control logic when coexistence is impossible, undesirable, uneconomic, unsupported, locked, unreliable, or itself the failed component.** ABIL's separately qualified deterministic control runtime may then become the ordinary controller against remote I/O and field devices.

The architectural goal is therefore **replacement-capable, coexistence-first**.

ABIL should replace the *function* of the legacy control system, not assume that modifying proprietary vendor internals is always the safest or easiest path.

## 3. Product recovery scenario

A representative target workflow is:

1. A machine's unsupported HMI/control PC or control stack fails or becomes practically unrecoverable.
2. A technician disconnects, isolates, or otherwise bounds the failed component.
3. An ABIL appliance is connected to the surviving industrial network through capability-qualified interfaces.
4. ABIL classifies the observed legacy control-authority locus before deciding what role can be replaced.
5. ABIL inventories reachable devices and relationships without treating connectivity, tag names, or metadata as proven functional meaning.
6. Where safe, separately authorized, and capability-qualified, ABIL presents manual commissioning controls through an independently constrained action path.
7. The technician operates known machine functions, identifies devices and purposes, and confirms or corrects ABIL's inferred relationships.
8. ABIL records topology, I/O identity, timing, observed consequences, operator-supplied semantics, uncertainty, and provenance as distinct evidence classes.
9. ABIL builds and continuously revises a machine-specific behavioral model.
10. ABIL synthesizes a candidate automation model representing states, transitions, commands, permissives, timings, alarms, recovery paths, and ordinary interlocks within a declared coverage envelope.
11. The candidate control model is replayed, simulated, shadowed, and compared against recorded/observed behavior before gaining machine authority.
12. If the existing PLC remains useful, ABIL may continue to use it as the execution target or proxy.
13. If ordinary PLC/control software must be replaced, the validated ABIL deterministic control runtime assumes direct control only over explicitly transferred control-ownership domains.
14. The ABIL appliance becomes the permanent supported replacement control computer while retaining the reconstructed machine model, configuration, evidence, and versioned control runtime.

### 3.1 Control-authority locus classification

`HMI/control system` is not one machine role. Before replacement planning, ABIL must classify the observed authority locus at least as one or more of:

- `SUPERVISORY_HMI_ONLY`;
- `SCADA_SUPERVISORY`;
- `SOFT_PLC_OR_CONTROL_PC`;
- `PLC_PAC_LOGIC`;
- `MOTION_OR_DRIVE_CONTROL`;
- `SAFETY_CONTROL`;
- `MIXED`;
- `UNKNOWN`.

Unknown authority locus fails closed at the claim/authority level for takeover. A failed supervisory HMI is a different replacement problem from a failed soft PLC, motion controller, ordinary PLC, or safety controller.

## 4. Three control deployment modes

### 4.1 Mode A — coexistence / discovery

The existing controller remains authoritative for ordinary automation.

ABIL may:

- passively observe traffic and telemetry;
- perform separately qualified configuration reads;
- perform separately qualified active discovery/enumeration;
- build topology and signal inventories;
- learn timing and behavioral relationships;
- accept targeted human semantic labeling;
- detect discrepancies between documented, named, and observed behavior;
- propose candidate relationships and commissioning tests.

Discovery capability is graded rather than binary:

1. **Passive observation** — no active query traffic introduced by ABIL.
2. **Low-impact reads** — bounded authenticated/configuration reads with declared request rates and timeout behavior.
3. **Active enumeration** — browse, scan, broadcast, connection, or vendor-specific discovery that may affect fragile networks even without writes.
4. **Commissioning/write capability** — separately authorized and constrained.

Every active discovery adapter must declare target allowlists, scan/query budgets, rate limits, retry/timeout policy, known side effects, and failure behavior. `Read-only` must not be treated as synonymous with `operationally non-disruptive`.

### 4.2 Mode B — PLC execution proxy

ABIL owns more of the reconstructed machine model, but the existing PLC remains the deterministic I/O executor.

The interface should be narrow and explicit. ABIL may request semantic operations such as `clamp_extend`, `conveyor_run`, or `index_station`, while the PLC continues to execute actual fieldbus writes, scan-timed sequencing, and local permissives.

Mode B may be transitional or permanent. It does not authorize a second writer to the same output namespace; control ownership remains exclusive as defined in Section 12.

### 4.3 Mode C — direct ABIL control runtime

When the legacy PLC/control logic cannot or should not remain the ordinary controller, ABIL may replace its function.

The ABIL appliance then owns an independently engineered deterministic control runtime that:

- scans/receives remote I/O;
- executes an approved machine state/sequence model;
- runs deterministic timers and ordinary interlocks;
- handles protocol-specific I/O update semantics;
- commands drives, valves, actuators, and ordinary control outputs through qualified adapters;
- exposes alarms, operator state, and manual controls;
- records execution evidence and faults;
- enters a **target-specific validated safe-state/fallback policy** on relevant faults rather than assuming one universal physical `fail-closed` behavior.

Direct takeover is a capability promotion, not a configuration convenience. It requires protocol-specific qualification, hardware compatibility evidence, timing/resource evidence, control-coverage evidence, fenced ownership transfer, target-specific safe-state/fallback evidence, and explicit authorization for the target installation.

## 5. Intelligence plane versus deterministic control plane

ABIL must not make a general-purpose learner, LLM, Python notebook, or continuously changing ML policy the real-time machine controller.

### 5.1 Intelligence / commissioning plane

Responsible for topology discovery, telemetry normalization, semantic grounding, behavioral learning, change/regime discovery, causal-hypothesis management, operator-guided commissioning, control-model synthesis, simulation/replay/shadow comparison, and diagnostics/evidence presentation.

This plane may use Python, ML libraries, causal/system-identification tools, rules, LLMs, vision, or Noema-derived mechanisms where justified.

### 5.2 Deterministic control runtime

Responsible for approved machine state/sequence execution, bounded command handling, I/O scheduling, deterministic timers, ordinary process permissives/interlocks, watchdog behavior, protocol runtime integration, and alarm/execution-state reporting.

The deterministic runtime executes a promoted control artifact. It does not continuously rewrite itself merely because the intelligence plane has learned something new. A newly synthesized control revision must pass defined validation and promotion gates before becoming executable authority.

### 5.3 Learner-independent degraded/manual operation

Once deterministic control or a known-good manual/recovery surface has been promoted, the intelligence/adaptive-learning plane must not become a single point of failure for that already-qualified capability.

The appliance architecture must support declared degraded states in which adaptive learning, LLM services, diagnostics synthesis, or model-update processes can crash, stall, be disabled, or be upgraded while:

- the promoted deterministic control runtime continues according to its qualified operating envelope; or
- the system enters its target-specific validated safe-state/fallback policy; and
- qualified manual/recovery controls remain available where the installation design requires them.

Resource allocation, process isolation, startup ordering, watchdogs, and recovery behavior must preserve this separation.

## 6. Control synthesis model

ABIL should not treat control generation as unconstrained source-code generation.

The preferred intermediate product is an inspectable machine control model with explicit semantics such as:

- machine states and modes;
- transitions;
- prerequisites/permissives;
- requested actions;
- expected consequences;
- timing windows;
- ordinary interlocks independently classified as non-safety;
- alarm conditions;
- recovery paths;
- operator/manual modes;
- unresolved or uncertain relationships;
- evidence/coverage status for every promoted behavior.

That model can then be compiled or translated to an existing vendor PLC program when technically and legally practical, a narrow PLC proxy interface, the ABIL deterministic control runtime, or another supported industrial controller.

The learned machine model and generated execution artifact are separate. A generated PLC or ABIL-runtime program is one implementation of the approved machine model, not the sole representation of machine truth.

## 7. Control-coverage ledger and unknown-state quarantine

Brownfield control behavior is underdetermined by ordinary production traces. Rare startup/shutdown paths, jam recovery, maintenance/manual modes, latent permissives, fault reactions, timing races, and one-shot interlocks may never appear in observed evidence.

Therefore every candidate control artifact must carry a **control-coverage ledger**. At minimum, each promoted state, transition, command, permissive, timeout, recovery path, and ordinary interlock must identify:

- evidence source(s);
- whether behavior was observed, technician-specified, vendor-specified, inferred, simulated, or tested;
- confidence/uncertainty and unresolved assumptions;
- held-out/negative-transition test coverage where applicable;
- authorization status within the declared operating envelope.

`Not observed` means **not authorized by inference alone**. Unknown or insufficiently covered behavior must be excluded from authority, remain technician-engineered, or be explicitly outside the promoted operating envelope. The resulting physical response to an unknown/fault condition is governed by the target-specific validated safe-state/fallback policy, not a universal default.

Matching recorded traces is necessary but not sufficient for promotion.

## 8. Vendor PLC treatment

Existing PLCs should be treated as one or more of:

- evidence sources;
- topology/configuration sources;
- deterministic execution proxies;
- permanent execution targets;
- replaceable legacy components.

ABIL should not assume it can safely overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other vendor projects.

Hardware configuration, I/O ownership, produced/consumed data, fieldbus master configuration, firmware compatibility, licensing, password/protection state, motion configuration, safety signatures, engineering-tool requirements, and proprietary project formats may make vendor-project mutation inappropriate or impractical.

Direct rewrite of an installed PLC is a target-specific migration path, not ABIL's universal onboarding mechanism.

## 9. Fieldbus and remote-I/O strategy

ABIL's direct-control capability should be protocol- and interface-specific rather than pretending all brownfield networks are generic Ethernet.

Potential targets include EtherNet/IP, PROFINET, Modbus TCP/RTU, DeviceNet, PROFIBUS, CAN/CANopen, vendor-specific drive/motion networks, and serial/gateway-connected I/O.

Some networks can run through ordinary industrial Ethernet hardware; others require dedicated adapters, gateways, or fieldbus interfaces.

A protocol adapter qualified for passive discovery or read-only telemetry is not automatically qualified for active enumeration, commissioning, or deterministic control authority.

## 10. Manual commissioning and semantic grounding

Network discovery can reveal device identities, addresses, classes, assemblies/registers, traffic, timing, status, and relationships. It cannot be assumed to reveal reliable functional semantics such as `infeed_clamp_extend` or `station_complete`.

Guided commissioning is therefore a first-class product workflow:

`observe -> propose candidate relationship -> constrained technician action -> measure consequences -> technician confirm/correct semantics -> retain provenance -> update machine model`

The operator teaches targeted semantics; ABIL should learn as much surrounding temporal and causal structure as it can instead of requiring exhaustive hand-programming.

Operator command, learner proposal, authorization decision, action execution, execution receipt, and subsequent telemetry must remain separately typed/attributed records. An answer-bearing label such as `ACTION_CONSEQUENCE` must not silently become learner-visible causal truth.

## 11. Safety boundary and protective-function classification

This architecture expands ABIL's long-term scope to ordinary machine-control replacement. It does **not** silently expand ABIL into automatic replacement of safety functions.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

On an undocumented machine, ABIL may not initially know whether a permissive, relay contact, reset handshake, drive-enable path, gate condition, safe-speed input, or PLC-to-safety handshake is merely process logic or part of a protective function.

Therefore the default classification rule is:

> **Unknown protective/interlock semantics are safety-relevant and out of scope for autonomous reconstruction until independently classified by qualified engineering evidence.**

ABIL may observe such signals and preserve them as prerequisites, but it may not downgrade them to ordinary control based on successful production traces or their location in standard PLC logic.

Direct takeover and generated-control promotion must bind a reviewed list of preserved safety interfaces/handshakes and demonstrate that ordinary-controller replacement cannot bypass or defeat them.

Physical fault response, stop behavior, de-energization, holding behavior, rollback, and recovery policy are target-specific and must be validated with independent safety/hazard authority appropriate to the installation. This architecture does not define one universal machine-safe state.

Safety replacement, validation, certification, and regulatory obligations remain outside the default ABIL control-reconstruction path.

## 12. Single-writer control ownership and authority transfer

For every physical output or control namespace, **exactly one authoritative ordinary-control writer may exist at a time**, with mechanically enforced ownership/fencing.

A surviving PLC, HMI, commissioning gateway, ABIL proxy, and ABIL direct runtime must never rely on convention alone to avoid competing writes.

The control-ownership contract must define:

- ownership domains down to the relevant output/control namespace;
- current authoritative writer identity;
- acquisition and release conditions;
- protocol, configuration, credential, or physical fencing used to prevent stale writers;
- restart behavior;
- stale-command rejection;
- partial-failure behavior;
- rollback/fallback semantics;
- transfer-of-authority receipts and exact active artifact/controller identity.

Cutover is complete only when the previous writer is mechanically unable to continue authoritatively writing the transferred domain and the new writer's ownership is verified.

### 12.1 Immutable promotion/deployment binding

Generated control is always a **candidate** until a promotion binding exists.

Promotion must bind, directly or by stable digest/reference:

- exact target deployment/machine identity;
- control-authority locus and ownership domain(s) being transferred;
- machine-model/evidence version;
- control-coverage ledger version;
- generated control artifact digest/version;
- target hardware/network/protocol/configuration identity;
- preserved safety-interface/handshake inventory;
- validation evidence set and acceptance result;
- target-specific safe-state/fallback policy identity;
- human/authority signoff and promotion receipt;
- known-good rollback artifact/configuration identity.

A control artifact lacking this binding has no production authority.

## 13. Validation and promotion ladder

The existing read-only F0 work remains useful but is a development/qualification stage, not the final product definition.

The long-term capability ladder is:

1. synthetic/headless learning substrate;
2. recorded telemetry replay;
3. live passive discovery/read-only shadow mode;
4. operator-guided semantic commissioning;
5. bounded manual-control tooling through an independent gateway;
6. machine-model reconstruction;
7. generated candidate control model plus control-coverage ledger;
8. replay/simulation validation including held-out/negative transition coverage;
9. shadow comparison against the surviving controller where available;
10. PLC execution-proxy mode with explicit single-writer ownership;
11. supervised cutover to a validated control artifact with immutable promotion binding and fenced authority transfer;
12. direct remote-I/O takeover where needed;
13. permanent ABIL runtime with learner-independent deterministic/manual degraded behavior and ongoing diagnostics/learning outside execution authority.

Each promotion must be separately evidenced. Passing an earlier stage does not imply authority for a later one.

## 14. Product packaging direction

The likely physical product is an industrial edge appliance rather than an APK or ordinary desktop application.

A plausible package is a rugged/fanless mini-PC, appropriate industrial Ethernet and fieldbus interfaces, bootable installer/recovery media, a small Linux-based appliance OS, ABIL intelligence/commissioning services, deterministic control runtime, persistent deployment/machine-model/configuration/evidence storage, a local operator/service interface, and export/backup/restore tooling.

Tiny Core/CorePure64, a stripped Debian-family appliance, or another compact Linux base may be evaluated later. The product architecture does not yet bind ABIL to one distribution.

The appliance architecture must permit deterministic/manual recovery services to be isolated from and survive failure or intentional shutdown of adaptive-learning services.

## 15. Persistent machine/deployment state

The valuable ABIL state is created during discovery, learning, commissioning, synthesis, validation, and operation. It does not pre-exist before ABIL arrives.

Persistent records may include discovered topology; source/device/signal identities; control-authority-locus classification; adapter/protocol configuration; operator semantics with provenance; learned machine model; evidence/history; control-coverage ledger; candidate control models; validation receipts; promoted control artifact/version; immutable promotion binding; ownership/fencing state; target-specific safe-state/fallback policy reference; runtime configuration; deployment identity; and software/schema/config versions.

Ordinary restore must fail closed at the compatibility/authority level on incompatible identity/binding. Cross-machine/schema/config/software reuse is a separate explicit migration/transfer operation.

## 16. Relationship to frozen F0 R1 review

The 2026-09-06 foundation/F0 subject and its R1 review remain historical evidence of the earlier, narrower architecture. Do not rewrite that reviewed source to pretend the broader control-reconstruction direction was already present.

The broader product direction adds future capability stages; it does not weaken admitted R1 requirements.

## 17. Corrected early-substrate evidence model

The immediate successor substrate should preserve a strict three-plane evidence model:

- **EvaluatorRecord** — may contain hidden fixture/regime/fault truth, rich provenance, scoring labels, and other evidence not necessarily learner-visible.
- **LearnerEvent** — a closed, typed, allowlisted projection containing only preregistered learner evidence. Unknown/unregistered fields fail closed; no arbitrary metadata bag crosses into the learner plane.
- **EvaluationJoin** — scoring-only association between learner outputs/evidence positions and evaluator truth. Learner/plugin code has no object/API/capability path back to evaluator/world hidden state.

Raw learner events remain asynchronous. Grouping, resampling, interpolation, windowing, and vector construction belong to a separately versioned feature-assembly contract with deterministic replay semantics.

Learner-visible identity must be collision-safe without exposing privileged physical provenance as an oracle. Transport/device status, externally supplied confidence/annotation, and learner/model uncertainty remain separate evidence classes.

Checkpoint compatibility must bind source/deployment/adapter/event-schema/feature-assembly/learner/codec/software/frontier identities and integrity, with restart-equivalence and stale/ahead/corrupt/wrong-identity rejection tests.

## 18. Immediate R2 gate split

The next R2 subject must not conflate substrate honesty with learner/product efficacy.

### 18.1 `R2-SUBSTRATE-QUALIFIED`

Asks whether the corrected early substrate is implementation-ready as an honest experimental/runtime foundation. It includes evaluator/learner separation and noninterference; event identity/currentness; prequential/causal evidence ordering; asynchronous assembly; deterministic replay/corpus identity; checkpoint trust binding and restart equivalence; fair paired baselines; recomputable evidence; resource bounds; opaque-label controls; and the ability to report that a simple baseline wins or no useful learner advantage exists.

This gate must **not** require the first learner to discover nontrivial structure or outperform baselines.

### 18.2 `R2-LEARNER-EFFICACY`

Separately asks whether a particular learner earns product/learning claims. It may require preregistered evidence such as useful nontrivial machine-specific learned structure, improvement over agreed baselines where appropriate, recurrence/forgetting/adaptation behavior, uncertainty/change quality, opaque-label performance, and onboarding/semantic-efficiency evidence.

### 18.3 Long-term compatibility question

A corrected early substrate must also avoid architectural commitments that block later coexistence-first control reconstruction. In particular it must not collapse PLC/vendor identity, capability levels, human-supplied semantics, control-coverage state, safety classification, ownership/fencing, promotion binding, or future deterministic control artifacts into one irreversible schema or runtime assumption.

Write-capable commissioning, PLC proxy execution, vendor-project generation, direct remote-I/O control, deterministic runtime implementation, and production cutover remain later separately qualified capability stages.

## 19. Long-term product success criteria

ABIL earns the stronger product claim only if it can demonstrate that it can:

1. enter a real brownfield control environment with incomplete documentation;
2. inventory useful surviving components without conflating discovery with functional semantics;
3. classify the control-authority locus before replacement planning;
4. become useful without exhaustive manual semantic programming;
5. recover enough machine semantics and behavior to support guided commissioning;
6. reconstruct an inspectable machine-control model with explicit unknown-state coverage;
7. validate generated automation against recorded, simulated, shadow, held-out, negative-transition, and operator evidence;
8. work with an existing PLC when that is the safer/easier route;
9. replace ordinary PLC control behavior when the legacy controller cannot remain viable;
10. preserve or independently classify protective/safety functions rather than infer them away;
11. mechanically prevent split-brain ordinary-control writers during proxy, cutover, rollback, and restart;
12. bind promoted control immutably to exact deployment/evidence/artifact/validation/rollback identities;
13. keep already-promoted deterministic/manual recovery capability available independently of learner-service failure according to the qualified operating design;
14. run the promoted control artifact deterministically and stably for the target hardware/network;
15. provide a supportable permanent replacement system rather than a one-off engineering demo.

## 20. Explicit non-goals for the current successor design

This document does not yet choose a specific appliance Linux distribution, first write-capable fieldbus, first vendor PLC migration target, deterministic-controller language/runtime, RTOS/real-time kernel strategy, HMI framework, safety PLC replacement strategy, automatic rewriting of arbitrary proprietary PLC projects, cloud dependence, remote fleet management, or pricing/licensing/legal structure.

Those choices should be forced by qualification evidence and the first concrete field target rather than prematurely frozen.
