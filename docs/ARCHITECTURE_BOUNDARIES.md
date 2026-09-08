# ABIL Architecture Boundaries

Status: **living successor boundary contract; implementation choices remain open**

## Core separation

ABIL should be designed as a layered control-reconstruction system rather than a monolithic learner or monolithic controller.

```text
Existing machine / surviving controls
        |
        v
Discovery + industrial adapters
        |
        v
Machine-model / intelligence plane
        |
        +----> Operator commissioning + diagnostics
        |
        +----> Control-model synthesis + validation
                         |
                         v
              Approved control artifact
                         |
                +--------+--------+
                |                 |
                v                 v
       Existing PLC proxy   ABIL deterministic
          / target           control runtime
                |                 |
                +--------+--------+
                         |
                         v
               Ordinary machine I/O

Independent safety systems remain authoritative across all modes.
```

The key architectural rules are:

- **replacement-capable, coexistence-first**;
- discovery, learning, semantic grounding, control synthesis, deterministic execution, and safety authority are distinct responsibilities;
- a learning component does not receive production output authority merely because it can propose a command or generate control logic;
- a new control revision becomes executable only through an explicit validation and promotion path.

## 1. Discovery and industrial adapters

Adapters translate equipment-specific interfaces into explicit internal evidence and capability contracts.

Potential interfaces include:

- PLC/PAC tags and vendor configuration;
- OPC UA/DA;
- EtherNet/IP;
- PROFINET;
- Modbus TCP/RTU;
- DeviceNet;
- PROFIBUS;
- CAN/CANopen;
- historian data;
- drive and motion-controller diagnostics;
- remote I/O;
- alarms and HMI events;
- maintenance records;
- cameras or other vision sources;
- vendor APIs or files;
- serial or gateway-connected legacy devices.

An adapter may support one or more distinct capability classes:

1. **Passive/read-only acquisition** — observe telemetry, status, traffic, or configuration without machine writes.
2. **Topology/configuration discovery** — enumerate reachable devices, identities, assemblies/registers, relationships, or vendor configuration evidence.
3. **Commissioning/manual action capability** — issue explicitly bounded technician-authorized requests for diagnostic or semantic-grounding purposes.
4. **Deterministic control capability** — participate in scan/update scheduling and command ordinary field I/O as part of an approved control runtime.

Qualification for one capability does not imply qualification for another. A read-only EtherNet/IP adapter, for example, is not automatically a qualified deterministic control adapter.

Adapters must declare:

- deployment/source identity;
- protocol and interface identity;
- timing/update semantics;
- quality/status semantics;
- read/write capability;
- supplied semantic mappings;
- configuration digest/version where applicable;
- failure behavior.

An adapter must not silently convert evaluator, vendor, or engineer knowledge into learned machine relationships and then credit ABIL for discovering them.

## 2. Machine-model / intelligence plane

The intelligence plane owns machine-specific learned structure and evidence-oriented inference.

It may support:

- streaming observations;
- persistent learned state;
- action-conditioned prediction where action evidence exists;
- explicit uncertainty;
- regime/change detection;
- online adaptation;
- comparison against simple baselines;
- retention of older recurring regimes;
- competing hypotheses;
- provenance sufficient to explain what evidence changed a model or hypothesis;
- learned topology/temporal/behavioral relationships;
- candidate control-model synthesis.

The architecture should not assume one model family solves every installation. ABIL may combine conventional system identification, forecasting, representation learning, change-point detection, causal discovery, rules, symbolic state models, learned models, and Noema-derived mechanisms where justified.

The intelligence plane may keep learning while the system is deployed. That does **not** mean it may continuously rewrite production control logic.

## 3. Semantic grounding and guided commissioning

Network discovery can identify nodes, addresses, types, tags, assemblies/registers, timing, and traffic patterns. It cannot be assumed to prove functional meaning such as `infeed_clamp_extend`, `station_complete`, or `index_ready`.

Guided commissioning is therefore a first-class boundary.

The preferred loop is:

`observe -> propose candidate relationship -> constrained technician action -> measure consequences -> technician confirm/correct semantics -> retain provenance -> update machine model`

ABIL should support:

- passive observation before actuation;
- candidate signal/device grouping;
- proposed relationships and discriminating tests;
- bounded technician-authorized actuation where permitted;
- recording the exact requested action and observed consequences;
- explicit technician confirmation/correction;
- provenance separating human-supplied labels from learned structure;
- repeated evidence accumulation rather than one-shot semantic assignment.

The target is **targeted semantic grounding**, not exhaustive hand-programming of every signal and relationship.

## 4. Operator commissioning and diagnostics

The operator surface should expose useful machine state without pretending the model knows more than it does.

Outputs should distinguish:

- observed telemetry;
- vendor/configuration evidence;
- operator-supplied semantics;
- learned relationships;
- prediction;
- residual/error;
- anomaly/change evidence;
- hypothesis;
- uncertainty;
- proposed additional observation/test;
- requested action;
- generated candidate control revision;
- promoted/active control artifact.

A language model may translate structured evidence into natural-language explanations, but the underlying evidence must remain independently inspectable. Generated prose is not machine truth.

## 5. Control-model synthesis and validation

ABIL should not equate "generate automation" with unconstrained source-code generation.

The preferred intermediate artifact is an inspectable machine-control model containing, as applicable:

- machine states and modes;
- transitions;
- requested actions;
- expected consequences;
- prerequisites/permissives;
- ordinary non-safety interlocks;
- timers and timing windows;
- alarm/fault conditions;
- recovery paths;
- manual/operator modes;
- unresolved relationships and uncertainty.

A candidate control model must be attributable to the machine model/evidence version that produced it.

Validation may include:

- recorded replay;
- simulator/digital-process comparison;
- shadow comparison against a surviving controller;
- technician review;
- deterministic timing/resource qualification;
- fault/alarm-path testing;
- rollback/recovery testing.

Only a validated, explicitly promoted control artifact may enter deterministic execution.

The learned machine model and executable control artifact remain separate. A learned insight may propose a new control revision; it does not silently mutate the active runtime.

## 6. Existing PLC coexistence roles

An existing PLC may be treated as one or more of:

- evidence/configuration source;
- source of observed ordinary control behavior;
- deterministic execution proxy;
- permanent execution target;
- replaceable legacy controller.

Default behavior is to preserve and work with surviving PLC logic when practical.

A useful transitional architecture is **PLC execution proxy mode**: ABIL owns more of the reconstructed semantic/control model and issues narrow high-level requests while the PLC continues to own scan-timed I/O, local deterministic sequencing, and established fieldbus behavior.

Direct rewriting of an installed vendor project is target-specific, not ABIL's universal onboarding method. Hardware configuration, I/O ownership, produced/consumed data, motion, fieldbus master configuration, firmware, passwords/protection, safety signatures, licenses, and proprietary project formats can all make vendor-project mutation inappropriate or impractical.

ABIL's universal goal is to reconstruct and support the machine's ordinary control function, not to depend on overwriting proprietary internals.

## 7. Deterministic control runtime

When coexistence is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, ABIL may replace the ordinary control function with a separately engineered deterministic runtime.

The deterministic runtime is responsible for:

- approved machine state/sequence execution;
- deterministic timers;
- bounded command handling;
- ordinary process permissives/interlocks;
- I/O scan/update scheduling;
- protocol-specific input/output semantics;
- watchdog behavior;
- timeout/fail-closed or declared fallback behavior;
- alarm/fault reporting;
- execution-state/evidence logging;
- restart/recovery behavior;
- exact active artifact/version identity.

The deterministic runtime executes a promoted control artifact. It should not contain a general-purpose learner or LLM that can freely change control behavior during execution.

Direct remote-I/O takeover is a capability promotion requiring exact hardware/protocol/deployment identity, timing/resource evidence, qualified drivers/adapters, rollback/recovery evidence, and explicit authorization for the target installation.

This document does not yet select the runtime language, scheduler, RTOS, real-time kernel strategy, fieldbus stack, or HMI framework.

## 8. Safety and action authority

Ordinary control reconstruction does **not** silently authorize safety-system reconstruction.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, machine-protection circuits, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

ABIL may observe safety state and require it as a prerequisite for ordinary control behavior. It must not infer certified safety requirements merely from observed operation and then claim equivalent protection.

Any write-capable commissioning or control path must be independently constrained according to its capability level. Controls may include:

- explicit allowlists;
- hard ranges/rate limits;
- state prerequisites;
- independent interlocks;
- human approval requirements;
- action logging;
- request freshness/replay protection;
- timeout/reversion behavior;
- immediate disable/bypass;
- external read-only or write-denial enforcement where applicable.

The safety/action boundary must not depend on the learning model behaving correctly.

## 9. Read-only first

The first live field deployment should have no control authority.

Read-only shadow mode remains an important evidence stage because ABIL must first prove that it can learn something useful from a real system before write-capable commissioning or direct control is justified.

Read-only is a qualification stage and product wedge, not the final product boundary.

## 10. Persistent machine/deployment state

The valuable ABIL state is created during discovery, learning, commissioning, synthesis, and operation. It should not be assumed to pre-exist before ABIL arrives at a machine.

Persistent state may include distinct versioned records for:

- discovered topology;
- device/source/signal identities;
- adapter/protocol configuration;
- operator-supplied semantics and corrections with provenance;
- learned machine model and uncertainty;
- regime/context history;
- evidence/history frontier;
- candidate control models;
- validation receipts/results;
- promoted control artifact/version;
- deterministic runtime configuration;
- deployment/source identity;
- software/schema/config versions.

A checkpoint or machine package must bind enough identity and compatibility information to prevent silent attachment of learned/control state to the wrong machine or incompatible runtime.

Copying/restoring state from one installation to another requires an explicit transfer/migration operation with defined semantics.

## 11. Evidence, causation, and claim ceilings

ABIL must not equate correlation with causation.

Passive data may support prediction while leaving causal direction unresolved. ABIL should be able to maintain multiple explanations and say that evidence is insufficient.

Technician-guided interventions can strengthen causal evidence, but human actions, annotations, tag names, vendor metadata, and action-origin labels must remain separately attributed. ABIL must not claim to have discovered structure that was supplied directly through privileged semantics.

Where a claim depends on supplied timing, quality, identity, labels, or annotations, the claim scope should say so.

## 12. Brownfield onboarding principle

Custom integration labor is a commercial risk.

The desired progression is:

1. discover/import available devices and signals;
2. normalize identity/timing/provenance;
3. learn statistical and temporal structure without requiring names for everything;
4. surface candidate groupings/relationships;
5. invite targeted human labeling and bounded commissioning actions where useful;
6. retain human semantics separately from learned structure;
7. synthesize an inspectable machine/control model;
8. preserve the existing controller when it is the best execution path;
9. replace ordinary control only when evidence supports that migration.

If every deployment requires essentially full conventional reverse engineering before ABIL contributes useful structure, the product thesis has failed or narrowed into a controls-integration consultancy.

## 13. No hidden product coupling to Noema

Noema is not a runtime dependency of ABIL.

If a Noema-derived mechanism outperforms simpler industrial methods under fair evaluation, ABIL may adopt it. If a conventional algorithm or deterministic technique works better, ABIL should use the conventional method.

The product is judged by usefulness, reliability, supportability, deployment cost, and evidence—not architectural elegance.
