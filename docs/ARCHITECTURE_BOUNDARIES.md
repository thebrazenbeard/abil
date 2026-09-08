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
- discovery, learning, semantic grounding, control synthesis, deterministic execution, control ownership, and safety authority are distinct responsibilities;
- a learning component does not receive production output authority merely because it can propose a command or generate control logic;
- a new control revision becomes executable only through an explicit validation and promotion path;
- unknown or unobserved control behavior is not silently promoted;
- each physical output/control namespace has exactly one authoritative ordinary-control writer at a time.

## 1. Discovery and industrial adapters

Adapters translate equipment-specific interfaces into explicit internal evidence and capability contracts.

Potential interfaces include PLC/PAC tags and vendor configuration, OPC UA/DA, EtherNet/IP, PROFINET, Modbus TCP/RTU, DeviceNet, PROFIBUS, CAN/CANopen, historian data, drive/motion diagnostics, remote I/O, alarms/HMI events, cameras, vendor APIs/files, and serial or gateway-connected legacy devices.

Adapter capability classes are distinct:

1. **Passive observation** — observe traffic/telemetry without introducing active query traffic.
2. **Low-impact read/configuration access** — bounded authenticated reads with declared request rates and retry behavior.
3. **Active discovery/enumeration** — browse, scan, broadcast, connection, or vendor-specific enumeration that can be operationally disruptive even without writes.
4. **Commissioning/manual action capability** — issue explicitly bounded technician-authorized requests.
5. **Deterministic control capability** — participate in qualified scan/update scheduling and command ordinary field I/O as part of an approved runtime.

Qualification for one capability does not imply qualification for another. `Read-only` does not mean `operationally harmless`.

Active discovery adapters must declare target allowlists, scan/query budgets, rate limits, timeout/retry policy, known side effects, and failure behavior.

All adapters must declare deployment/source identity, protocol/interface identity, timing/update semantics, quality/status semantics, capability level, supplied semantic mappings, configuration digest/version where applicable, and failure behavior.

An adapter must not silently convert evaluator, vendor, or engineer knowledge into learned machine relationships and then credit ABIL for discovering them.

## 2. Control-authority locus

Before ABIL plans replacement, it must distinguish what role the legacy component actually owns. At minimum the deployment model should represent:

- `SUPERVISORY_HMI_ONLY`;
- `SCADA_SUPERVISORY`;
- `SOFT_PLC_OR_CONTROL_PC`;
- `PLC_PAC_LOGIC`;
- `MOTION_OR_DRIVE_CONTROL`;
- `SAFETY_CONTROL`;
- `MIXED`;
- `UNKNOWN`.

Unknown authority locus fails closed for takeover. Network presence or device identity is not proof of control authority.

## 3. Machine-model / intelligence plane

The intelligence plane owns machine-specific learned structure and evidence-oriented inference.

It may support streaming observations, persistent learned state, action-conditioned prediction where action evidence exists, explicit uncertainty, regime/change detection, online adaptation, fair baseline comparison, recurring-regime retention, competing hypotheses, learned topology/temporal/behavioral relationships, and candidate control-model synthesis.

The architecture should not assume one model family solves every installation. ABIL may combine conventional system identification, forecasting, representation learning, change-point detection, causal discovery, rules, symbolic state models, learned models, and Noema-derived mechanisms where justified.

The intelligence plane may keep learning while deployed. That does **not** mean it may continuously rewrite production control logic.

## 4. Semantic grounding and guided commissioning

Network discovery can identify nodes, addresses, types, tags, assemblies/registers, timing, and traffic patterns. It cannot be assumed to prove functional meaning such as `infeed_clamp_extend`, `station_complete`, or `index_ready`.

Guided commissioning is therefore first-class:

`observe -> propose candidate relationship -> constrained technician action -> measure consequences -> technician confirm/correct semantics -> retain provenance -> update machine model`

Operator command, learner proposal, gateway decision, action execution, execution receipt, and subsequent telemetry must remain separately represented. Human-supplied labels stay attributable and must not be credited as autonomous discovery.

The target is **targeted semantic grounding**, not exhaustive hand-programming of every signal and relationship.

## 5. Operator commissioning and diagnostics

The operator surface should distinguish observed telemetry, vendor/configuration evidence, operator-supplied semantics, learned relationships, prediction, residual/error, anomaly/change evidence, hypothesis, uncertainty, proposed observations/tests, requested actions, generated candidate control revisions, control-coverage state, and promoted/active control artifacts.

A language model may translate structured evidence into natural-language explanations, but the underlying evidence must remain independently inspectable. Generated prose is not machine truth.

## 6. Control-model synthesis and coverage

ABIL should not equate `generate automation` with unconstrained source-code generation.

The preferred intermediate artifact is an inspectable machine-control model containing, as applicable:

- machine states and modes;
- transitions;
- commands/actions;
- expected consequences;
- prerequisites/permissives;
- ordinary interlocks independently classified as non-safety;
- timers/timing windows;
- alarm/fault conditions;
- recovery paths;
- manual/operator modes;
- unresolved relationships/uncertainty.

Every candidate control artifact must also carry a **control-coverage ledger**. Each promoted state, transition, command, permissive, timeout, recovery path, and ordinary interlock must identify the evidence/requirements that support it and whether it was observed, technician-specified, vendor-specified, inferred, simulated, or tested.

`Not observed` means `not authorized by inference alone`. Unknown or insufficiently covered behavior must fail closed, remain technician-engineered, or be explicitly excluded from the promoted operating envelope.

Replay similarity alone is insufficient. Validation should include held-out and negative-transition coverage where applicable, technician review, fault/alarm paths, restart/restore behavior, deterministic timing/resource qualification, and rollback/recovery testing.

Only a validated, explicitly promoted control artifact may enter deterministic execution.

## 7. Existing PLC coexistence roles

An existing PLC may be an evidence/configuration source, source of observed control behavior, deterministic execution proxy, permanent execution target, or replaceable legacy controller.

Default behavior is to preserve and work with surviving PLC logic when practical.

A useful transitional architecture is **PLC execution proxy mode**: ABIL owns more of the reconstructed semantic/control model and issues narrow high-level requests while the PLC continues to own scan-timed I/O, local deterministic sequencing, and established fieldbus behavior.

Direct rewriting of an installed vendor project is target-specific, not ABIL's universal onboarding method. Hardware configuration, I/O ownership, produced/consumed data, motion, fieldbus master configuration, firmware, passwords/protection, safety signatures, licenses, and proprietary project formats can all make vendor-project mutation inappropriate or impractical.

## 8. Deterministic control runtime

When coexistence is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, ABIL may replace the ordinary control function with a separately engineered deterministic runtime.

The deterministic runtime is responsible for approved machine state/sequence execution, deterministic timers, bounded command handling, ordinary process permissives/interlocks, I/O scan/update scheduling, protocol-specific I/O semantics, watchdog behavior, timeout/fail-closed or declared fallback behavior, alarm/fault reporting, execution evidence, restart/recovery behavior, and exact active artifact identity.

The runtime executes a promoted control artifact. It must not contain a general-purpose learner or LLM that can freely change control behavior during execution.

Direct remote-I/O takeover requires exact hardware/protocol/deployment identity, timing/resource evidence, qualified drivers/adapters, control-coverage evidence, rollback/recovery evidence, fenced control ownership, and explicit target-specific authorization.

## 9. Single-writer control ownership

For every physical output/control namespace, exactly one authoritative ordinary-control writer may exist at a time.

A surviving PLC, HMI, ABIL commissioning gateway, PLC proxy, and ABIL direct runtime must not rely on convention alone to avoid split-brain writes.

The ownership contract must define:

- ownership domains;
- current authoritative writer identity;
- acquisition/release conditions;
- physical, protocol, configuration, or credential fencing;
- stale-command/writer rejection;
- restart and partial-failure behavior;
- rollback/fallback semantics;
- exact transfer-of-authority receipts.

Cutover is not complete until the previous writer is mechanically unable to continue authoritatively writing the transferred domain and the new writer's ownership is verified.

## 10. Safety and action authority

Ordinary control reconstruction does **not** silently authorize safety-system reconstruction.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, machine-protection circuits, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

On an undocumented machine, a permissive, relay contact, reset handshake, drive-enable path, gate condition, safe-speed input, or PLC-to-safety handshake may have unknown protective meaning.

The default classification rule is:

> **Unknown protective/interlock semantics are safety-relevant and out of scope for autonomous reconstruction until independently classified by qualified engineering evidence.**

ABIL may observe such state and preserve it as a prerequisite, but it may not downgrade it to ordinary control merely because the machine operated successfully or because the signal appears inside standard PLC logic.

Direct takeover and generated-control promotion must bind a reviewed list of preserved safety interfaces/handshakes and show that ordinary-controller replacement cannot bypass or defeat them.

Any write-capable path must be independently constrained with capability-appropriate allowlists, ranges/rate limits, state prerequisites, freshness/replay protection, logging, timeout/reversion behavior, and immediate disable/bypass.

## 11. Read-only first

The first live field deployment should have no control authority.

Read-only shadow mode remains an important evidence stage because ABIL must first prove that it can learn something useful from a real system before write-capable commissioning or direct control is justified.

Read-only is a qualification stage and product wedge, not the final product boundary.

## 12. Persistent machine/deployment state

The valuable ABIL state is created during discovery, learning, commissioning, synthesis, validation, and operation. It should not be assumed to pre-exist before ABIL arrives.

Persistent state may include versioned records for discovered topology, control-authority locus, device/source/signal identities, adapter/protocol configuration, operator semantics with provenance, learned machine model and uncertainty, evidence/history, control-coverage ledger, candidate control models, validation receipts, promoted control artifact/version, control-ownership/fencing state, deterministic runtime configuration, deployment identity, and software/schema/config versions.

Copying/restoring state across machines requires an explicit compatibility/migration operation. Ordinary restore must fail closed on incompatible identity/binding.

## 13. Evidence, causation, and early-substrate boundaries

ABIL must not equate correlation with causation. Passive data may support prediction while leaving causal direction unresolved.

Technician-guided interventions can strengthen evidence, but human actions, annotations, tag names, vendor metadata, timing, quality, and action-origin labels must remain separately attributed.

The corrected early substrate should preserve separate evaluator records, a closed typed learner projection, and scoring-only evaluation joins. Learner/plugin code must have no hidden object/API/capability path to evaluator truth.

Transport/device status, externally supplied confidence/annotation, and learner/model uncertainty are distinct evidence classes.

Raw learner events remain asynchronous; feature assembly is separately versioned and deterministic under replay.

Substrate qualification and learner efficacy are separate gates. A valid substrate must be able to report that a simple baseline wins.

## 14. Brownfield onboarding principle

Custom integration labor is a commercial risk.

The desired progression is:

1. passively observe where possible;
2. use bounded active discovery only under a declared capability profile;
3. discover/import available devices and signals;
4. normalize identity/timing/provenance;
5. learn statistical and temporal structure without requiring names for everything;
6. invite targeted human labeling and bounded commissioning actions where useful;
7. retain human semantics separately from learned structure;
8. synthesize an inspectable machine/control model with explicit coverage and unknowns;
9. preserve the existing controller when it is the best execution path;
10. replace ordinary control only when evidence supports that migration.

If every deployment requires essentially full conventional reverse engineering before ABIL contributes useful structure, the product thesis has failed or narrowed into a controls-integration consultancy.

## 15. No hidden product coupling to Noema

Noema is not a runtime dependency of ABIL.

If a Noema-derived mechanism outperforms simpler industrial methods under fair evaluation, ABIL may adopt it. If a conventional algorithm or deterministic technique works better, ABIL should use the conventional method.

The product is judged by usefulness, reliability, supportability, deployment cost, and evidence—not architectural elegance.
