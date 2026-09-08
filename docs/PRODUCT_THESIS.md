# ABIL Product Thesis

Status: **working product thesis; not a validated commercial claim**

## Problem

A large installed base of industrial equipment remains mechanically useful while its software, controls ecosystem, documentation, vendor support, or human knowledge ages out.

The operational problem is not merely that these machines are old. Each installation becomes increasingly individual over time:

- PLC logic is modified;
- HMI or supervisory software becomes unsupported;
- controller projects become locked, unavailable, corrupted, or dependent on obsolete engineering tools;
- drives, sensors, remote-I/O modules, and fieldbus components are replaced;
- process conditions drift;
- operators develop workarounds;
- tooling changes;
- maintenance changes behavior;
- documentation becomes stale;
- the people who know the machine best eventually leave.

A mechanically healthy machine can therefore become economically stranded because the control system is no longer supportable.

Replacing the entire asset merely to modernize its intelligence/control layer can be economically irrational.

## Product proposition

ABIL — **Adaptive Brownfield Intelligence Layer** — is intended to learn and reconstruct the machine/control system that actually exists, then preserve or replace the surviving control stack using the least disruptive supportable path.

The product has two broad phases.

### 1. Learn and reconstruct

ABIL should:

1. inventory reachable controllers, remote I/O, drives, sensors, fieldbus nodes, HMIs, and other surviving control components;
2. ingest telemetry and configuration evidence with minimal disruption;
3. learn recurring operating regimes, timing relationships, dependencies, and change relative to the machine's own history;
4. keep human-supplied semantics separate from relationships inferred from behavior;
5. support guided commissioning so a technician can confirm or correct the purpose of devices, commands, sensors, sequence states, and observed consequences;
6. maintain uncertainty instead of presenting guesses as facts;
7. build an inspectable machine-specific behavioral/control model.

### 2. Preserve or replace control

After reconstruction, ABIL should prefer coexistence when practical:

- continue using the existing PLC as an evidence/configuration source;
- use the existing PLC as a deterministic execution proxy;
- generate or target conventional controller logic where that is the safer maintainable path;
- leave a still-viable PLC as the permanent execution target when appropriate.

When coexistence is impossible, undesirable, unsupported, locked, unreliable, failed, or uneconomic, ABIL may replace the ordinary control function with a separately qualified deterministic control runtime that directly interfaces with remote I/O and field devices.

The strategic rule is **replacement-capable, coexistence-first**.

## Primary customer and recovery scenario

The first likely customer is a manufacturer with valuable brownfield automated equipment where replacement is expensive and machine knowledge or controls support is incomplete, concentrated, or disappearing.

A high-value recovery case may involve:

- an unsupported or failed HMI/control PC;
- obsolete SCADA/supervisory software;
- an inaccessible or undocumented PLC project;
- a PLC/controller family whose engineering environment is no longer practical to maintain;
- legacy remote-I/O or fieldbus networks that still physically function;
- chronic intermittent faults and unclear machine behavior;
- substantial downtime cost;
- dependence on one or two experienced technicians for diagnosis;
- a machine whose real behavior differs materially from nominal OEM documentation.

The commercial objective is not necessarily to replace all automation hardware. It is to restore a supportable control system around the mechanically useful machine while preserving valuable surviving components wherever practical.

## What ABIL is not

ABIL is not:

- an automatic replacement for safety PLCs, safety relays, E-stops, guard circuits, hardwired protective interlocks, or certified safety functions;
- an unrestricted learning policy or LLM directly driving production outputs;
- a promise that ABIL can safely overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other proprietary PLC projects;
- a claim that network discovery, device names, tag names, or vendor metadata alone reveal reliable functional semantics;
- a generic chatbot for maintenance manuals;
- a guarantee of causal understanding from passive data alone;
- a requirement to use Noema or any single AI architecture.

Ordinary control reconstruction and safety-system replacement are separate engineering problems. The default ABIL path preserves independent safety authority.

## Differentiation target

Existing industrial analytics can already monitor tags, detect anomalies, estimate remaining useful life, classify faults, predict process variables, and generate dashboards or explanations.

Conventional controls integrators can already replace PLCs and HMIs through manual engineering.

PC-based controller products can already execute deterministic control logic on industrial computers.

Those capabilities alone are not sufficient differentiation.

ABIL's stronger target is **machine-specific control reconstruction**:

> Build and continuously revise an operational model of this particular installation strongly enough to discover useful structure, ground semantics through targeted technician interaction, reconstruct an inspectable control model, validate candidate automation, and either cooperate with or replace the surviving ordinary controller with a supportable runtime.

The product only earns a differentiated position if it can demonstrate that this reconstruction process materially reduces the manual archaeology and re-engineering normally required to recover a brownfield control system.

## Product wedge versus end product

The first technical and commercial wedge remains **read-only shadow mode**.

ABIL must first prove that, after observing an unfamiliar real system, it can produce predictions and machine-specific discovered structure that are useful to someone who understands the machine without exhaustive semantic hand-mapping.

That wedge should answer questions such as:

- Can ABIL learn normal operating regimes and temporal relationships?
- Can it predict near-future state better than simple baselines?
- Can it detect a genuinely new regime or changed relationship?
- Can it adapt without permanently forgetting older recurring regimes?
- Can it distinguish stable predictive structure from transient noise?
- Can it rank plausible explanations without pretending correlation proves causation?
- Can it remain useful when signal names and human semantic annotations are withheld?
- Can it reduce the amount of manual tag-by-tag mapping required before useful structure emerges?

Read-only shadow mode is **not the final product boundary**. It is the evidence gate before commissioning, control-model reconstruction, and eventually qualified write-capable control.

## Coexistence-first migration value

A surviving PLC is not automatically an obstacle. Depending on the installation, it may be:

- an evidence source;
- a configuration/topology source;
- a deterministic execution proxy;
- a permanent execution target;
- a replaceable legacy component.

This flexibility matters commercially. ABIL should not force replacement of hardware that is still reliable merely to prove that it can replace it.

A successful migration may end with ABIL learning and commissioning around the existing PLC, with ABIL generating a narrow high-level request interface or a conventional vendor program. Another migration may end with the PLC removed and the ABIL appliance directly controlling remote I/O through a qualified deterministic runtime.

The decision should be based on supportability, access, timing, protocol capability, maintainability, cost, rollback risk, and target-specific evidence.

## Control synthesis principle

ABIL should not treat automation generation as unconstrained source-code generation.

The primary generated artifact should be an inspectable machine-control model containing, as applicable:

- states and operating modes;
- transitions;
- commands/actions;
- expected consequences;
- prerequisites/permissives;
- ordinary non-safety interlocks;
- timing windows and delays;
- alarms/fault conditions;
- recovery paths;
- operator/manual behavior;
- unresolved relationships and uncertainty.

That model can then be translated to an existing vendor PLC, a narrow PLC-proxy interface, an ABIL deterministic runtime, or another supported industrial controller.

The learned machine model and the executable control artifact must remain distinct. A learner may propose a revision; it does not silently mutate production control authority.

## Long-term product success conditions

The stronger ABIL thesis requires evidence that the system can:

1. enter a real brownfield environment with incomplete documentation;
2. discover useful surviving topology and device identity without assuming names equal semantics;
3. reconstruct useful machine semantics with targeted rather than exhaustive technician labeling;
4. learn nontrivial machine-specific relationships from behavior;
5. produce an inspectable machine/control model whose evidence and uncertainty can be reviewed;
6. generate candidate automation from that approved model;
7. validate generated automation through replay, simulation, shadow comparison, and commissioning evidence;
8. work with existing PLC logic when that is the safer/easier/more maintainable route;
9. replace ordinary PLC control behavior when the legacy controller cannot remain viable;
10. meet deterministic timing/reliability requirements for the target hardware and fieldbus before direct takeover;
11. preserve independent safety authority unless a separate safety-engineering project explicitly changes that contract;
12. remain supportable as a permanent installed system rather than a one-off engineering demo.

## Commercial hypothesis

ABIL may support a high-value B2B model because industrial downtime is expensive, brownfield equipment is widespread, and controls obsolescence can strand otherwise valuable assets.

That hypothesis is not yet validated for ABIL specifically. Revenue potential depends on proving at least:

1. useful learning and reconstruction on real equipment;
2. deployability without excessive custom integration labor;
3. a commissioning workflow that reduces manual controls archaeology rather than merely moving it into a new tool;
4. operator trust through inspectable evidence, provenance, uncertainty, and deterministic execution boundaries;
5. repeatable coexistence and migration patterns across more than one installation/vendor/protocol profile;
6. economic value large enough to justify deployment, qualification, and lifecycle support costs.

## Relationship to Noema

ABIL and Noema are separate projects.

Noema investigates persistent learned intelligence under strict developmental and epistemic constraints. ABIL is a commercial engineering product and may use conventional ML, system identification, causal methods, rules, LLMs, vision models, databases, deterministic control runtimes, or Noema-derived mechanisms as appropriate.

Noema may contribute ideas to ABIL. ABIL may provide real-world pressure that improves Noema. Neither project should be forced to inherit the other's constraints.
