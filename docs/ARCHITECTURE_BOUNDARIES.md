# ABIL Architecture Boundaries

Status: **living successor boundary contract under review; implementation choices remain open**

This document is read together with `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`, which is a normative proposed companion for promotion trust, anti-rollback, commissioning, transactional-command, identity, lifecycle, and safety-noninterference rules.

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
               Candidate control artifact
                         |
                         v
             Separate promotion authority
                         |
                         v
       Protected promoted artifact / loader state
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
- discovery, learning, semantic grounding, control synthesis, promotion authority, deterministic execution, control ownership, and safety authority are distinct responsibilities;
- a learning component does not receive production output authority merely because it can propose a command or generate control logic;
- candidate generation is not promotion authority, and the learner/LLM/plugin plane cannot write/select the active artifact or promotion trust material;
- a new control revision becomes executable only through explicit validation, authenticated promotion, protected active-artifact selection, and independent loader verification;
- authority-bearing state is monotonic and anti-rollback; ordinary restore cannot resurrect stale control authority;
- unknown or unobserved control behavior is not silently promoted;
- each physical output/control namespace has exactly one authoritative ordinary-control writer at a time;
- physical command ambiguity is preserved; timeout/reconnect never proves non-execution and does not authorize blind retry;
- once a deterministic/manual recovery capability is promoted, failure of adaptive-learning services must not automatically remove that qualified capability;
- product capability, installation commissioning, execution authority, artifact lifecycle, and support/recovery state are orthogonal.

## 1. Discovery and industrial adapters

Adapters translate equipment-specific interfaces into explicit internal evidence and capability contracts.

Potential interfaces include PLC/PAC tags and vendor configuration, OPC UA/DA, EtherNet/IP, PROFINET, Modbus TCP/RTU, DeviceNet, PROFIBUS, CAN/CANopen, historian data, drive/motion diagnostics, remote I/O, alarms/HMI events, cameras, vendor APIs/files, and serial or gateway-connected legacy devices.

Adapter capability classes are distinct:

1. **Passive observation** — observe traffic/telemetry without introducing active query traffic.
2. **Low-impact read/configuration access** — bounded authenticated reads with declared request rates and retry behavior.
3. **Active discovery/enumeration** — browse, scan, broadcast, connection, or vendor-specific enumeration that can be operationally disruptive even without writes.
4. **Commissioning/manual action capability** — issue explicitly bounded technician-authorized requests under an independently established commissioning envelope.
5. **Deterministic control capability** — participate in qualified scan/update scheduling and command ordinary field I/O as part of an approved runtime.

Qualification for one capability does not imply qualification for another. `Read-only` does not mean `operationally harmless`.

Active discovery adapters must declare target allowlists, scan/query budgets, rate limits, timeout/retry policy, known side effects, and failure behavior.

All adapters must declare deployment/source identity, protocol/interface identity, timing/update semantics, quality/status semantics, capability level, supplied semantic mappings, configuration digest/version where applicable, and failure behavior.

An adapter must not silently convert evaluator, vendor, or engineer knowledge into learned machine relationships and then credit ABIL for discovering them.

## 2. Legacy evidence, control-authority locus, and identity

When a predecessor controller/HMI/control PC is still partially alive or observable, preserve useful predecessor evidence before isolation/removal where safe and practical. Record whether legacy evidence is `AVAILABLE`, `CAPTURED`, `PARTIAL`, or `UNAVAILABLE`; an already-dead predecessor creates a real evidence/coverage gap.

Before ABIL plans replacement, it must distinguish what role the legacy component actually owns. At minimum the deployment model should represent:

- `SUPERVISORY_HMI_ONLY`;
- `SCADA_SUPERVISORY`;
- `SOFT_PLC_OR_CONTROL_PC`;
- `PLC_PAC_LOGIC`;
- `MOTION_OR_DRIVE_CONTROL`;
- `SAFETY_CONTROL`;
- `MIXED`;
- `UNKNOWN`.

Unknown authority locus blocks takeover authority. Network presence or device identity is not proof of control authority.

Identity must keep deployment, topology generation, logical node identity, mutable endpoint/address observations, source-scoped signal/channel identity, and adapter instance/configuration distinct. IP addresses, fieldbus node numbers, slots, tag names, assemblies/registers, and similar locators are evidence, not globally stable device identity.

## 3. Machine-model / intelligence plane

The intelligence plane owns machine-specific learned structure and evidence-oriented inference.

It may support streaming observations, persistent learned state, action-conditioned prediction where action evidence exists, explicit uncertainty, regime/change detection, online adaptation, fair baseline comparison, recurring-regime retention, competing hypotheses, learned topology/temporal/behavioral relationships, and candidate control-model synthesis.

The architecture should not assume one model family solves every installation. ABIL may combine conventional system identification, forecasting, representation learning, change-point detection, causal discovery, rules, symbolic state models, learned models, and Noema-derived mechanisms where justified.

The intelligence plane may keep learning while deployed. That does **not** mean it may continuously rewrite production control logic or mutate authority-bearing state.

## 4. Semantic grounding and guided commissioning

Network discovery can identify nodes, addresses, types, tags, assemblies/registers, timing, and traffic patterns. It cannot be assumed to prove functional meaning such as `infeed_clamp_extend`, `station_complete`, or `index_ready`.

Guided commissioning is therefore first-class:

`observe -> propose candidate relationship -> constrained technician action -> record subsequent observations -> technician confirm/correct semantics -> derive/update hypotheses -> retain provenance -> update machine model`

Operator command, learner proposal, gateway decision, action execution attempt, execution receipt, subsequent telemetry, and causal attribution must remain separately represented. Human-supplied labels stay attributable and must not be credited as autonomous discovery. A subsequent observation is not automatically encoded as an `ACTION_CONSEQUENCE` causal fact.

Before any write-capable commissioning action, an installation-specific **independent commissioning envelope** must be established without relying solely on the not-yet-qualified model. The envelope is deny-by-default and defines the writable capability scope, independently established preconditions, prohibited state/output combinations or sequences, duration/extent/rate limits, supervision and stop/disable requirements, any jog/hold-to-run/reduced-energy semantics, and explicit `UNKNOWN` handling. Unknown required preconditions block the action.

The target is **targeted semantic grounding**, not exhaustive hand-programming of every signal and relationship.

## 5. Operator commissioning and diagnostics

The operator surface should distinguish observed telemetry, vendor/configuration evidence, operator-supplied semantics, learned relationships, prediction, residual/error, anomaly/change evidence, hypothesis, uncertainty, proposed observations/tests, requested actions, generated candidate control revisions, control-coverage state, promoted/active control artifacts, current control-ownership state, authority epoch, and ambiguous execution outcomes.

A language model may translate structured evidence into natural-language explanations, but the underlying evidence must remain independently inspectable. Generated prose is not machine truth.

## 6. Control-model synthesis and coverage

ABIL should not equate `generate automation` with unconstrained source-code generation.

The preferred intermediate artifact is an inspectable machine-control model containing, as applicable:

- machine states and modes;
- transitions;
- commands/actions;
- expected observations/claimed consequences with provenance;
- prerequisites/permissives;
- ordinary interlocks independently classified as non-safety;
- timers/timing windows;
- alarm/fault conditions;
- recovery paths;
- manual/operator modes;
- unresolved relationships/uncertainty.

Every candidate control artifact must also carry a **control-coverage ledger**. Each promoted state, transition, command, permissive, timeout, recovery path, and ordinary interlock must identify the evidence/requirements that support it and whether it was observed, technician-specified, vendor-specified, inferred, simulated, or tested.

`Not observed` means `not authorized by inference alone`. Unknown or insufficiently covered behavior must be excluded from authority, remain technician-engineered, or be explicitly outside the promoted operating envelope.

Replay similarity alone is insufficient. Validation should include held-out and negative-transition coverage where applicable, technician review, fault/alarm paths, restart/restore behavior, deterministic timing/resource qualification, and rollback/recovery testing.

Validation produces evidence; it does not itself grant promotion authority.

## 7. Existing PLC coexistence roles

An existing PLC may be an evidence/configuration source, source of observed control behavior, deterministic execution proxy, permanent execution target, or replaceable legacy controller.

Default behavior is to preserve and work with surviving PLC logic when practical.

A useful architecture is **PLC execution proxy mode**: ABIL owns more of the reconstructed semantic/control model and issues narrow high-level requests while the PLC continues to own scan-timed I/O, local deterministic sequencing, and established fieldbus behavior.

PLC proxy may be transitional **or permanent**. Permanent support is not reserved for direct takeover.

Direct rewriting of an installed vendor project is target-specific, not ABIL's universal onboarding method. Hardware configuration, I/O ownership, produced/consumed data, motion, fieldbus master configuration, firmware, passwords/protection, safety signatures, licenses, and proprietary project formats can all make vendor-project mutation inappropriate or impractical.

## 8. Deterministic control runtime and degraded operation

When coexistence is impossible, undesirable, unsupported, unreliable, failed, locked, or uneconomic, ABIL may replace the ordinary control function with a separately engineered deterministic runtime.

The deterministic runtime is responsible for approved machine state/sequence execution, deterministic timers, bounded command handling, ordinary process permissives/interlocks, I/O scan/update scheduling, protocol-specific I/O semantics, watchdog behavior, target-specific validated safe-state/fallback behavior, alarm/fault reporting, execution evidence, restart/recovery behavior, and exact active artifact/promotion identity.

The runtime executes only an independently verified promoted control artifact. It must not contain a general-purpose learner or LLM that can freely change control behavior during execution.

Direct remote-I/O takeover requires exact hardware/protocol/deployment identity, timing/resource evidence, qualified drivers/adapters, control-coverage evidence, rollback/recovery evidence, fenced control ownership, target-specific safe-state/fallback evidence, safety noninterference evidence, and explicit target-specific authorization.

Once deterministic control or a known-good manual/recovery surface is promoted, adaptive-learning/LLM/diagnostic-synthesis services must not become a single point of failure for it. Process isolation, resource reservation, startup ordering, watchdogs, and recovery behavior must support declared degraded modes in which the intelligence plane can crash, stall, be disabled, or be upgraded while the already-qualified deterministic/manual capability either continues inside its operating envelope or transitions according to the target-specific validated safe-state/fallback policy.

## 9. Promotion trust root, authority state, and anti-rollback

Generated control is always a **candidate** until a separately authorized promotion exists.

The architecture distinguishes candidate generation, validation/evidence production, promotion authority, protected active-artifact/loader state, and deterministic runtime verification.

A process label, role name, or self-asserted approval is not an authority root. Before write-capable implementation, admission requires a current, independently rooted `AuthorityGrant` (or equivalent) binding the issuer/trust material, authorized subject, exact deployment and authority domain/output scope, permitted capability/action scope, validity/currentness, monotonic generation, revocation/supersession, and verifier identity. Candidate, learner, evaluator, plugin, and runtime-subject principals cannot create or widen that grant. Deployment authority and artifact-promotion authority remain distinct scopes/receipts even if one qualified organization or person holds both.

The intelligence/commissioning/learner/LLM/plugin plane may write candidates, but it cannot write promotion trust material, active artifact storage, loader selection, next-boot target, the current authority ledger, or the authority grant.

A separately authorized promotion principal/process emits an authenticated/integrity-protected promotion manifest binding the exact deployment, topology/ownership domain, machine-model/evidence version, control-coverage ledger, artifact digest, target runtime/hardware/network/protocol/configuration, preserved safety interfaces, validation evidence, operating envelope, target-specific fallback policy, rollback identity, current authority-grant identity, signoff, and a monotonic authority generation/epoch.

The deterministic loader/runtime independently verifies the current authority grant and promotion material before activation and restart. Activation is atomic or transactionally equivalent. Missing, partial, corrupt, mismatched, unauthenticated, unpromoted, wrong-deployment, or stale material does not become active.

Authority-bearing state is not ordinary checkpoint state. Learner/model/config backups cannot grant, downgrade, or resurrect control authority. Revocation/supersession survives restart/restore. Rollback to older known-good artifact bytes requires a **new** authorized rollback/promotion receipt at a newer authority generation rather than restoring an old authority epoch.

If the authority ledger is missing, corrupt, divergent, or untrusted, no new write authority is inferred.

## 10. Single-writer control ownership and transaction semantics

For every physical output/control namespace, exactly one authoritative ordinary-control writer may exist at a time, or the namespace is explicitly non-authoritative/unknown/conflicted.

A surviving PLC, HMI, ABIL commissioning gateway, PLC proxy, and ABIL direct runtime must not rely on convention alone to avoid split-brain writes.

The ownership contract must define ownership domains, current writer identity, authority epoch/ownership generation, acquisition/release conditions, physical/protocol/configuration/credential fencing, stale-command rejection, restart/partial-failure behavior, rollback/fallback semantics, and transfer-of-authority receipts.

Cutover is not complete until the previous writer is mechanically unable to continue authoritatively writing the transferred domain and the new writer's ownership is verified.

Future commissioning/manual and PLC-proxy commands must use a transaction envelope with unique request identity, deployment/authority domain, current authority generation, exact operation/parameters, relevant precondition state, freshness/expiry, acknowledgement lifecycle, duplicate/idempotency policy, timeout/reconnect semantics, bounded queue/backpressure, and durable linkage among gateway decision, execution attempt/receipt, and subsequent observations.

A timeout or reconnect does **not** prove that a physical action did not execute. `UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` is first-class. Non-idempotent or ambiguous physical actions are not blindly retried unless the exact target contract or installation-specific recovery rule proves retry safe.

## 11. Safety and action authority

Ordinary control reconstruction does **not** silently authorize safety-system reconstruction.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, drive safety functions, machine-protection circuits, and other independent protective systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

On an undocumented machine, a permissive, relay contact, reset handshake, drive-enable path, gate condition, safe-speed input, or PLC-to-safety handshake may have unknown protective meaning.

The default classification rule is:

> **Unknown protective/interlock semantics are safety-relevant and out of scope for autonomous reconstruction until a current, independently authorized safety-classification record establishes otherwise.**

Any later classification or downgrade to ordinary control requires a current `SafetyClassificationRecord` (or equivalent safety-project record) independent of the ordinary ABIL candidate/learner/evaluator planes. It binds the classifier/signoff authority, exact deployment and topology generation, hazard/safety context, evidence digest/set, classification scope and affected asset/semantics, validity/currentness, and revocation/supersession. Ordinary ABIL cannot create, refresh, or approve it. Until a current record exists, the conservative safety-relevant classification remains authoritative.

ABIL may observe such state and preserve it as a prerequisite, but it may not downgrade it to ordinary control merely because the machine operated successfully or because the signal appears inside standard PLC logic.

Ordinary ABIL discovery, commissioning, proxy, and direct-control capability is negatively scoped away from independent safety ownership/configuration/effect. Without a separate explicitly authorized safety-engineering project, ordinary ABIL must not claim safety-device ownership, download/reset/reconfigure safety projects/signatures, change drive safety/network ownership, bypass/mask/spoof protective paths, or alter shared infrastructure in a way that silently disables them.

Direct takeover and generated-control promotion must bind a reviewed list of preserved safety interfaces/handshakes. Later qualification must test safety noninterference across applicable startup/restart, ABIL runtime failure, intelligence-plane failure, communications loss, adapter/driver failure, cutover, rollback, and shared-infrastructure failure/recovery cases.

Physical safe-state/fallback behavior is target-specific. Depending on the machine and hazard analysis, de-energize, hold, controlled stop, rollback, or another response may be appropriate. ABIL must not encode one universal physical `fail-closed` behavior; the applicable policy must come from independently qualified installation-specific safety/hazard evidence.

## 12. Persistent machine/deployment state

The valuable ABIL state is created during discovery, learning, commissioning, synthesis, validation, and operation. It should not be assumed to pre-exist before ABIL arrives.

Persistent state may include versioned records for discovered topology, control-authority locus, device/source/signal identities, adapter/protocol configuration, operator semantics with provenance, learned machine model and uncertainty, evidence/history, control-coverage ledger, candidate control models, validation receipts, promoted control artifact/version, authenticated promotion binding, control-ownership/fencing state, target-specific safe-state/fallback policy reference, deterministic runtime configuration, deployment identity, and software/schema/config versions.

State classes remain distinct: learner state, evidence/model state, candidate artifact state, runtime operational state, and authority state. Ordinary learner/evidence backups are insufficient to recreate authority state.

Copying/restoring state across machines requires an explicit compatibility/migration operation. Ordinary restore must reject incompatible identity/binding and must not bypass the separately authenticated current authority generation.

## 13. Evidence, causation, and early-substrate boundaries

ABIL must not equate correlation with causation. Passive data may support prediction while leaving causal direction unresolved.

Technician-guided interventions can strengthen evidence, but human actions, annotations, tag names, vendor metadata, timing, quality, and action-origin labels must remain separately attributed.

The corrected early substrate should preserve separate evaluator records, a closed typed learner projection, and scoring-only evaluation joins. Learner/plugin code must have no hidden object/API/capability path to evaluator truth.

Transport/device status, externally supplied confidence/annotation, and learner/model uncertainty are distinct evidence classes.

Raw learner events remain asynchronous; feature assembly is separately versioned and deterministic under replay.

Substrate qualification and learner efficacy are separate gates. A valid substrate must be able to report that a simple baseline wins.

The early substrate remains non-actuating. Later promotion, commissioning, command, and authority semantics must not leak into learner state as hidden privileges or answer-bearing semantics.

## 14. Capability graph and permanent support

The early evidence sequence is ordered, but later per-installation deployment is not one universal ordinal ladder.

Product capability qualification, deployment commissioning state, execution-authority state, control-artifact lifecycle, and support/recovery state are separate axes.

After common discovery/reconstruction/validation work, an installation may remain permanently in read-only/advisory mode, a qualified deterministic manual-recovery mode, a permanent PLC-proxy/PLC-target mode, or a separately qualified direct-ABIL-control mode.

A direct-control-capable ABIL build does not force a deployment into direct control. A permanent PLC-proxy deployment receives support lifecycle, backup/recovery, diagnostics, and upgrade discipline without requiring direct I/O takeover.

## 15. Brownfield onboarding principle

Custom integration labor is a commercial risk.

The desired progression is:

1. preserve useful predecessor evidence where available and safe;
2. passively observe where possible;
3. use bounded active discovery only under a declared capability profile;
4. discover/import available devices and signals;
5. normalize identity/timing/provenance without confusing address with identity;
6. learn statistical and temporal structure without requiring names for everything;
7. invite targeted human labeling and independently bounded commissioning actions where useful;
8. retain human semantics separately from learned structure;
9. synthesize an inspectable machine/control model with explicit coverage and unknowns;
10. preserve the existing controller when it is the best execution path;
11. replace ordinary control only when evidence supports that migration.

If every deployment requires essentially full conventional reverse engineering before ABIL contributes useful structure, the product thesis has failed or narrowed into a controls-integration consultancy.

## 16. No hidden product coupling to Noema

Noema is not a runtime dependency of ABIL.

If a Noema-derived mechanism outperforms simpler industrial methods under fair evaluation, ABIL may adopt it. If a conventional algorithm or deterministic technique works better, ABIL should use the conventional method.

The product is judged by usefulness, reliability, supportability, deployment cost, and evidence—not architectural elegance.
