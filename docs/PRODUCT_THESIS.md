# ABIL Product Thesis

Status: **working product thesis; not a validated commercial claim**

## Problem

A large installed base of industrial equipment remains mechanically useful while its software, controls ecosystem, documentation, vendor support, or human knowledge ages out.

Each installation becomes increasingly individual over time:

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

A mechanically healthy machine can therefore become economically stranded because the control system is no longer supportable. Replacing the entire asset merely to modernize its intelligence/control layer can be economically irrational.

## Product proposition

ABIL — **Adaptive Brownfield Intelligence Layer** — is intended to learn and reconstruct the machine/control system that actually exists, then preserve or replace the surviving ordinary-control stack using the least disruptive supportable path.

The product has two broad phases.

### 1. Learn and reconstruct

ABIL should:

1. determine where control authority currently lives rather than assuming every HMI/PLC/network node owns the same role;
2. inventory reachable controllers, remote I/O, drives, sensors, fieldbus nodes, HMIs, and surviving control components through explicitly bounded discovery capabilities;
3. ingest telemetry and configuration evidence with minimal disruption;
4. learn recurring operating regimes, timing relationships, dependencies, and change relative to the machine's own history;
5. keep human/vendor-supplied semantics separate from relationships inferred from behavior;
6. support guided commissioning so a technician can confirm/correct the purpose of devices, commands, sensors, sequence states, and observed consequences;
7. maintain uncertainty and explicit unknowns instead of presenting guesses as facts;
8. build an inspectable machine-specific behavioral/control model with evidence coverage for every behavior proposed for automation.

### 2. Preserve or replace control

After reconstruction, ABIL should prefer coexistence when practical:

- continue using the existing PLC as evidence/configuration source;
- use the existing PLC as a deterministic execution proxy;
- generate or target conventional controller logic when that is the safer maintainable path;
- leave a still-viable PLC as the permanent execution target when appropriate.

When coexistence is impossible, undesirable, unsupported, locked, unreliable, failed, or uneconomic, ABIL may replace the ordinary control function with a separately qualified deterministic runtime that directly interfaces with remote I/O and field devices.

The strategic rule is **replacement-capable, coexistence-first**.

## Primary customer and recovery scenario

The first likely customer is a manufacturer with valuable brownfield automated equipment where replacement is expensive and machine knowledge or controls support is incomplete, concentrated, or disappearing.

A high-value recovery case may involve an unsupported or failed HMI/control PC, obsolete SCADA/supervisory software, inaccessible or undocumented PLC project, controller family whose engineering environment is no longer practical to maintain, functioning legacy remote-I/O/fieldbus hardware, chronic intermittent faults, substantial downtime cost, or dependence on a few experienced technicians.

The commercial objective is not necessarily to replace all automation hardware. It is to restore a supportable control system around the mechanically useful machine while preserving valuable surviving components wherever practical.

## What ABIL is not

ABIL is not:

- an automatic replacement for safety PLCs, safety relays, E-stops, guard circuits, hardwired protective interlocks, or certified safety functions;
- an unrestricted learning policy or LLM directly driving production outputs;
- a promise that ABIL can safely overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other proprietary PLC projects;
- a claim that network discovery, device names, tag names, or vendor metadata alone reveal reliable functional semantics;
- a claim that ordinary production traces completely determine rare startup, shutdown, recovery, maintenance, fault, or one-shot control behavior;
- a generic chatbot for maintenance manuals;
- a guarantee of causal understanding from passive data alone;
- a requirement to use Noema or any single AI architecture.

Ordinary control reconstruction and safety-system replacement are separate engineering problems. Unknown protective/interlock semantics are treated as safety-relevant until independently classified.

## Differentiation target

Existing industrial analytics can already monitor tags, detect anomalies, estimate remaining useful life, classify faults, predict process variables, and generate dashboards or explanations.

Conventional controls integrators can already replace PLCs and HMIs through manual engineering. PC-based controller products can already execute deterministic logic on industrial computers.

Those capabilities alone are not sufficient differentiation.

ABIL's stronger target is **machine-specific control reconstruction**:

> Build and continuously revise an operational model of this particular installation strongly enough to discover useful structure, ground semantics through targeted technician interaction, reconstruct an inspectable control model, explicitly quarantine unknown behavior, validate candidate automation, and either cooperate with or replace the surviving ordinary controller with a supportable runtime.

The product only earns a differentiated position if this reconstruction materially reduces the manual archaeology and re-engineering normally required to recover a brownfield control system.

## Product wedge versus end product

The first technical and commercial wedge remains **read-only shadow mode**.

ABIL must first prove that, after observing an unfamiliar real system, it can produce predictions and machine-specific discovered structure useful to someone who understands the machine without exhaustive semantic hand-mapping.

Substrate qualification and learner efficacy are separate gates. The early substrate must be honest, deterministic/reproducible enough, leakage-resistant, restart-safe, and fair to baselines even if the first learner does not outperform those baselines. Learner/product claims are earned separately.

Read-only shadow mode is **not the final product boundary**. It is the evidence gate before commissioning, control-model reconstruction, and eventually qualified write-capable control.

## Coexistence-first migration value

A surviving PLC may be an evidence source, configuration/topology source, deterministic execution proxy, permanent execution target, or replaceable legacy component.

This flexibility matters commercially. ABIL should not force replacement of hardware that is still reliable merely to prove that it can replace it.

A successful migration may end with ABIL learning and commissioning around the existing PLC, with ABIL generating a narrow high-level request interface or conventional vendor program. Another may end with the PLC removed and the ABIL appliance directly controlling remote I/O through a qualified deterministic runtime.

The decision should be based on supportability, access, timing, protocol capability, maintainability, cost, rollback risk, control-coverage completeness, safety-interface certainty, and target-specific evidence.

## Control synthesis principle

ABIL should not treat automation generation as unconstrained source-code generation.

The primary generated artifact should be an inspectable machine-control model containing, as applicable:

- states and operating modes;
- transitions;
- commands/actions;
- expected consequences;
- prerequisites/permissives;
- ordinary interlocks independently classified as non-safety;
- timing windows and delays;
- alarms/fault conditions;
- recovery paths;
- operator/manual behavior;
- unresolved relationships and uncertainty;
- a control-coverage ledger describing what evidence or engineering requirement supports each promoted behavior.

`Not observed` does not mean `safe to omit`. Unresolved behavior must be denied promotion/authority by default, remain technician-engineered, or be excluded from the promoted operating envelope. Physical safe-state/fallback behavior remains installation-specific.

The model can then be translated to an existing vendor PLC, a narrow PLC-proxy interface, an ABIL deterministic runtime, or another supported industrial controller.

The learned machine model and executable control artifact remain distinct. A learner may propose a revision; it does not silently mutate production control authority.

## Control ownership and cutover principle

For each physical output/control namespace, exactly one authoritative ordinary-control writer may exist at a time.

Coexistence, proxy mode, commissioning, direct takeover, restart, and rollback must use mechanically enforced ownership/fencing so a surviving PLC, HMI, ABIL commissioning gateway, and ABIL runtime cannot become competing writers.

Cutover is a transfer of authority, not simply starting a second controller.

## Long-term product success conditions

The stronger ABIL thesis requires evidence that the system can:

1. enter a real brownfield environment with incomplete documentation;
2. discover useful surviving topology without assuming names equal semantics;
3. identify the legacy control-authority locus before replacement planning;
4. reconstruct useful machine semantics with targeted rather than exhaustive technician labeling;
5. learn nontrivial machine-specific relationships from behavior when making learner-efficacy claims;
6. produce an inspectable machine/control model whose evidence, uncertainty, and unknown coverage can be reviewed;
7. generate candidate automation from that approved model;
8. validate generated automation through replay, simulation, shadow comparison, held-out/negative transition tests, and commissioning evidence;
9. work with existing PLC logic when that is the safer/easier/more maintainable route;
10. replace ordinary PLC control behavior when the legacy controller cannot remain viable;
11. meet deterministic timing/reliability requirements for the target hardware/fieldbus before direct takeover;
12. preserve independently classified safety authority and protective handshakes;
13. prevent split-brain ordinary-control writers during cutover, rollback, and restart;
14. remain supportable as a permanent installed system rather than a one-off engineering demo.

## Commercial hypothesis

ABIL may support a high-value B2B model because industrial downtime is expensive, brownfield equipment is widespread, and controls obsolescence can strand otherwise valuable assets.

That hypothesis is not yet validated for ABIL specifically. Revenue potential depends on proving useful learning/reconstruction on real equipment, deployability without excessive custom labor, commissioning that reduces manual controls archaeology, operator trust through inspectable evidence and deterministic boundaries, repeatable migration patterns across multiple installations, and economic value large enough to justify deployment/qualification/lifecycle support costs.

## Relationship to Noema

ABIL and Noema are separate projects.

Noema investigates persistent learned intelligence under strict developmental and epistemic constraints. ABIL is a commercial engineering product and may use conventional ML, system identification, causal methods, rules, LLMs, vision models, databases, deterministic control runtimes, or Noema-derived mechanisms as appropriate.

Noema may contribute ideas to ABIL. ABIL may provide real-world pressure that improves Noema. Neither project should be forced to inherit the other's constraints.
