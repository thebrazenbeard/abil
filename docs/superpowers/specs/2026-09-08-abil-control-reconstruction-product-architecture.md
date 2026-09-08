# ABIL Control Reconstruction Product Architecture

Status: **approved product direction; implementation remains staged, review-gated, and falsifiable**

Date: 2026-09-08

## 1. Purpose

ABIL — Adaptive Brownfield Intelligence Layer — is ultimately intended to recover, reconstruct, modernize, and where necessary replace unsupported brownfield machine-control systems while preserving useful existing industrial hardware whenever practical.

The long-term product is not merely an analytics appliance. Its target end state is a field-deployable industrial mini-PC that can enter an unfamiliar or partially failed automation environment, discover the surviving control network, help a technician recover manual operability, learn machine-specific behavior and semantics through observation and guided commissioning, synthesize a replacement control model, validate that model, and eventually operate as the permanent control runtime when the original supervisory/control software or ordinary PLC logic can no longer be relied upon.

The product principle remains:

> Learn the machine that actually exists.

This successor architecture expands the meaning of that principle from observation and diagnosis into controlled reconstruction of ordinary automation behavior.

## 2. Default strategy: coexist first, replace when necessary

ABIL should not default to deleting, overwriting, or bypassing an existing PLC program merely because it is old.

The preferred order is:

1. **Discover and observe the existing system.** Treat the surviving PLC, HMI, drives, remote I/O, fieldbus devices, and network traffic as evidence.
2. **Work with the existing PLC logic when practical.** Existing ladder/function-block/structured-text logic may remain the deterministic executor while ABIL learns and reconstructs machine behavior.
3. **Use the existing PLC as an execution proxy when useful.** ABIL may issue bounded high-level requests through a narrow interface while the PLC continues to own scan-time I/O, local interlocks, and established fieldbus behavior.
4. **Replace ordinary PLC control logic when coexistence is impossible, undesirable, uneconomic, unsupported, locked, unreliable, or itself the failed component.** In that case ABIL's deterministic control runtime may become the actual machine controller against remote I/O and field devices.

The architectural goal is therefore **replacement-capable, coexistence-first**.

ABIL should replace the *function* of the legacy control system, not assume that modifying proprietary vendor internals is always the safest or easiest path.

## 3. Product recovery scenario

A representative target workflow is:

1. A machine's unsupported HMI/control PC or control stack fails or becomes practically unrecoverable.
2. A technician disconnects the failed PC or otherwise isolates the failed control component.
3. An ABIL appliance is connected to the surviving industrial network and appropriate fieldbus interfaces.
4. ABIL inventories reachable nodes, adapters, I/O devices, drives, sensors, valve manifolds, controllers, and communication relationships without assuming semantic meaning from identifiers alone.
5. Where safe and authorized, ABIL presents manual commissioning controls through an independently constrained action path.
6. The technician operates known machine functions, identifies devices and purposes, and confirms or corrects ABIL's inferred relationships.
7. ABIL records topology, I/O identity, timing, observed consequences, operator-supplied semantics, uncertainty, and provenance as distinct evidence classes.
8. ABIL builds and continuously revises a machine-specific behavioral model.
9. ABIL synthesizes a candidate automation model representing states, transitions, commands, permissives, timings, alarms, and non-safety interlocks.
10. The candidate control model is replayed, simulated, shadowed, and compared against recorded/observed behavior before gaining machine authority.
11. If the existing PLC remains useful, ABIL may continue to use it as the execution target or proxy.
12. If the ordinary PLC/control software must be replaced, the validated ABIL deterministic control runtime assumes direct control of the appropriate remote I/O and field devices.
13. The ABIL appliance becomes the permanent supported replacement control computer while retaining the reconstructed machine model, configuration, evidence, and versioned control runtime.

## 4. Three control deployment modes

### 4.1 Mode A — coexistence / discovery

The existing controller remains authoritative for ordinary automation.

ABIL:

- passively observes available traffic and telemetry;
- imports reachable device and controller metadata;
- builds a topology and signal inventory;
- learns timing and behavioral relationships;
- accepts targeted human semantic labeling;
- detects discrepancies between documented, named, and observed behavior;
- proposes candidate relationships and commissioning tests.

This is the lowest-risk mode and the preferred starting point whenever the old control system still operates.

### 4.2 Mode B — PLC execution proxy

ABIL owns more of the reconstructed machine model, but the existing PLC remains the deterministic I/O executor.

The interface should be narrow and explicit. For example, ABIL may request semantic operations such as `clamp_extend`, `conveyor_run`, or `index_station`, while the PLC continues to execute the actual fieldbus writes, scan-timed sequencing, and local permissives.

This mode provides several benefits:

- ABIL can validate reconstructed behavior without immediately replacing vendor fieldbus/controller infrastructure;
- existing PLC scan determinism and hardware integration remain useful;
- rollback is easier;
- ABIL can compare requested outcomes with actual PLC/machine responses;
- the product can deliver value before direct protocol replacement exists for every vendor/network.

Mode B may be transitional or permanent depending on the machine and customer constraints.

### 4.3 Mode C — direct ABIL control runtime

When the legacy PLC/control logic cannot or should not remain the ordinary controller, ABIL may replace its function.

The ABIL appliance then owns an independently engineered deterministic control runtime that:

- scans/receives remote I/O;
- executes an approved machine state/sequence model;
- runs deterministic timers and interlocks;
- handles protocol-specific I/O update semantics;
- commands drives, valves, actuators, and ordinary control outputs through qualified adapters;
- exposes alarms, operator state, and manual controls;
- records execution evidence and faults;
- fails closed or falls back according to a declared runtime policy.

Direct takeover is a capability promotion, not a configuration convenience. It requires protocol-specific qualification, hardware compatibility evidence, timing/resource evidence, and explicit authorization for the target installation.

## 5. Intelligence plane versus deterministic control plane

ABIL must not make a general-purpose learner, LLM, Python notebook, or continuously changing ML policy the real-time machine controller.

The appliance should separate two major planes.

### 5.1 Intelligence / commissioning plane

Responsible for:

- topology discovery;
- telemetry/event normalization;
- semantic grounding;
- behavioral learning;
- change/regime discovery;
- causal-hypothesis management;
- operator-guided commissioning;
- control-model synthesis;
- simulation/replay/shadow comparison;
- diagnostics and evidence presentation.

This plane may use Python, ML libraries, causal/system-identification tools, rules, LLMs, vision, or Noema-derived mechanisms where justified.

### 5.2 Deterministic control runtime

Responsible for:

- approved machine state/sequence execution;
- bounded command handling;
- I/O scan/update scheduling;
- deterministic timers;
- ordinary process permissives and interlocks;
- watchdog behavior;
- protocol runtime integration;
- alarm and execution-state reporting.

The deterministic runtime executes a promoted control artifact. It does not continuously rewrite itself merely because the intelligence plane has learned something new.

A newly synthesized control revision must pass defined validation and promotion gates before becoming executable authority.

## 6. Control synthesis model

ABIL should not treat control generation as unconstrained source-code generation.

The preferred intermediate product is a machine control model with explicit, inspectable semantics such as:

- machine states;
- transitions;
- prerequisites/permissives;
- requested actions;
- expected consequences;
- timing windows;
- ordinary non-safety interlocks;
- alarm conditions;
- recovery paths;
- operator/manual modes;
- unresolved or uncertain relationships.

That model can then be compiled or translated to one of several execution targets:

- an existing vendor PLC program when technically and legally practical;
- a narrow PLC proxy interface;
- the ABIL deterministic control runtime;
- another supported industrial controller.

The learned machine model and the generated execution artifact are separate. A generated PLC or ABIL-runtime program is one implementation of the approved machine model, not the sole representation of machine truth.

## 7. Vendor PLC treatment

Existing PLCs should be treated as one or more of:

- evidence sources;
- topology/configuration sources;
- deterministic execution proxies;
- permanent execution targets;
- replaceable legacy components.

ABIL should not assume it can safely overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other vendor projects.

Vendor-specific issues may include:

- hardware configuration;
- I/O ownership;
- produced/consumed data;
- fieldbus master configuration;
- firmware compatibility;
- licensing;
- password/protection state;
- motion configuration;
- safety signatures;
- engineering-tool requirements;
- proprietary file/project formats.

Therefore, direct rewrite of an installed PLC is a target-specific migration path, not ABIL's universal onboarding mechanism.

## 8. Fieldbus and remote-I/O strategy

ABIL's direct-control capability should be protocol- and interface-specific rather than pretending that all brownfield networks are generic Ethernet.

Potential targets include, among others:

- EtherNet/IP;
- PROFINET;
- Modbus TCP/RTU;
- DeviceNet;
- PROFIBUS;
- CAN/CANopen;
- vendor-specific drive/motion networks;
- serial/gateway-connected I/O.

Some networks can run through ordinary industrial Ethernet hardware; others require dedicated adapters, gateways, or fieldbus interfaces.

A protocol adapter used for discovery or read-only telemetry does not automatically qualify the same adapter for deterministic control authority.

## 9. Manual commissioning and semantic grounding

Network discovery can reveal device identities, addresses, classes, assemblies/registers, traffic, timing, status, and relationships. It cannot be assumed to reveal reliable functional semantics such as "infeed clamp extend" or "station complete".

ABIL should therefore make guided commissioning a first-class product workflow.

The system should support:

1. passive observation before actuation;
2. candidate grouping and relationship discovery;
3. constrained manual actuation when safe and authorized;
4. recording which outputs were requested;
5. measuring which signals/states changed afterward;
6. technician confirmation/correction of functional meaning;
7. provenance separating human-supplied labels from relationships inferred from behavior;
8. repeated evidence accumulation until a relationship is sufficiently understood for control synthesis.

The operator teaches targeted semantics; ABIL should learn as much of the surrounding temporal and causal structure as it can instead of requiring exhaustive hand-programming.

## 10. Safety boundary

This architecture expands ABIL's long-term scope to ordinary machine-control replacement. It does **not** silently expand ABIL into automatic replacement of safety functions.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

ABIL may observe safety state and use it as a prerequisite for ordinary machine behavior, but it must not claim that observed operation is sufficient evidence to reconstruct certified safety requirements.

Safety replacement, validation, certification, and regulatory obligations are outside the default ABIL control-reconstruction path.

## 11. Validation and promotion ladder

The existing read-only F0 work remains useful but is a development/qualification stage, not the final product definition.

The long-term capability ladder is:

1. synthetic/headless learning substrate;
2. recorded telemetry replay;
3. live passive discovery/read-only shadow mode;
4. operator-guided semantic commissioning;
5. bounded manual-control tooling through an independent gateway;
6. machine-model reconstruction;
7. generated candidate control model;
8. replay/simulation validation;
9. shadow comparison against the surviving controller where available;
10. PLC execution-proxy mode;
11. supervised cutover to a validated control artifact;
12. direct remote-I/O takeover where needed;
13. permanent ABIL runtime with ongoing diagnostics and learning outside the deterministic execution authority.

Each promotion must be separately evidenced. Passing an earlier stage does not imply authority for a later one.

## 12. Product packaging direction

The likely physical product is an industrial edge appliance rather than an APK or ordinary desktop application.

A plausible product package is:

- rugged/fanless mini-PC;
- appropriate industrial Ethernet and fieldbus interfaces;
- bootable installer/recovery media;
- small Linux-based appliance OS;
- ABIL intelligence/commissioning services;
- deterministic control runtime;
- persistent deployment/machine-model/configuration/evidence storage;
- local operator/service interface;
- export/backup/restore tooling.

Tiny Core/CorePure64, a stripped Debian-family appliance, or another compact Linux base may be evaluated later. The product architecture should not yet bind ABIL to one distribution.

The same bootable media may eventually serve installation, recovery, diagnostics, and controlled restoration of a known-good runtime image.

## 13. Relationship to frozen F0 R1 review

The 2026-09-06 foundation/F0 subject and its R1 review remain historical evidence of the earlier, narrower architecture.

Do not rewrite that reviewed source to pretend the broader control-reconstruction direction was already present.

The successor architecture must preserve the admitted R1 requirements, including:

- closed learner/evaluator information boundaries;
- source-scoped identity;
- deterministic replay/currentness rules;
- checkpoint identity/integrity binding;
- runtime/resource qualification;
- opaque-label/semantic-ablation testing;
- onboarding-cost evidence;
- nontrivial machine-specific learned-structure evidence.

The broader product direction adds new future capability stages; it does not weaken those requirements.

## 14. Success criteria for the long-term product thesis

ABIL earns the stronger product claim only if it can demonstrate that it can:

1. enter a real brownfield control environment with incomplete documentation;
2. inventory and identify useful surviving control/network components;
3. become useful without exhaustive manual semantic programming;
4. recover enough machine semantics and behavior to support safe guided manual commissioning;
5. reconstruct a machine-control model whose behavior is inspectable and evidence-backed;
6. validate generated automation against recorded, simulated, shadow, and operator evidence;
7. work with an existing PLC when that is the safer/easier route;
8. replace ordinary PLC control behavior when the legacy controller cannot remain viable;
9. run the promoted control artifact deterministically and stably for the target hardware/network;
10. preserve independent safety authority unless a separate safety project explicitly replaces it;
11. provide a supportable permanent replacement system rather than a one-off engineering demo.

## 15. Explicit non-goals for the current successor design

This document does not yet choose:

- a specific appliance Linux distribution;
- the first write-capable fieldbus;
- the first vendor PLC migration target;
- a programming language/runtime for the deterministic controller;
- a hard real-time kernel or scheduler;
- a specific HMI framework;
- a safety PLC replacement strategy;
- automatic rewriting of arbitrary proprietary PLC projects;
- cloud dependence;
- remote fleet management;
- pricing/licensing/legal structure.

Those choices should be forced by qualification evidence and the first concrete field target rather than prematurely frozen.

## 16. Immediate successor review boundary

This broader product architecture does **not** turn the next R2 source subject into a write-capable controller build.

The immediate successor review should remain focused on repairing the frozen F0 learning/telemetry substrate contract against the admitted R1 failures while preserving alignment with the long-term product direction.

The R2 review board should therefore ask two separate questions:

1. **Is the corrected early substrate implementation-ready on its own terms?** This includes learner/evaluator separation, event identity/currentness, replay determinism, checkpoint trust binding, runtime/resource qualification, opaque-label testing, onboarding-cost evidence, and machine-specific learned-structure evidence.
2. **Does the corrected early substrate avoid architectural commitments that would block the later coexistence-first control-reconstruction path?** In particular it should not collapse PLC/vendor identity, protocol capability levels, human-supplied semantics, or future deterministic control artifacts into one irreversible schema or runtime assumption.

Write-capable commissioning, PLC proxy execution, vendor-project generation, direct remote-I/O control, deterministic runtime implementation, and production cutover remain later separately qualified capability stages.
