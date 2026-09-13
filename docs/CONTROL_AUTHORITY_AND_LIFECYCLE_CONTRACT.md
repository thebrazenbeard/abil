# ABIL Control Authority and Lifecycle Contract

Status: **reviewer-ready proposed successor contract; no implementation or deployment authority implied**

Date: 2026-09-08

This document is a normative companion to the proposed control-reconstruction successor architecture in Draft PR #2. It closes trust, lifecycle, commissioning, and ambiguous-effect gaps identified during architecture review without expanding the immediate R2 early substrate into a write-capable controller.

The historical frozen F0/R1 subject remains unchanged and failed. This contract applies to the proposed successor architecture only.

## 1. Orthogonal state domains

ABIL must not use one ordinal `stage` value as a substitute for several different kinds of state.

At minimum the architecture distinguishes:

1. **ProductCapabilityQualification** — capabilities a particular ABIL build/release has qualified to provide for a declared hardware/protocol profile.
2. **DeploymentCommissioningState** — what has been established for one installation: evidence capture, discovery, semantic grounding, manual commissioning, model validation, cutover preparation, and support state.
3. **ExecutionAuthorityState** — which principal/runtime currently owns each ordinary-control output namespace, including explicit `NO_ACTIVE_AUTHORITY`, `AUTHORITY_OUTCOME_UNKNOWN`, and `DUAL_AUTHORITY_CONFLICT` states.
4. **ControlArtifactLifecycle** — candidate-generation, validation, promotion, activation, supersession, revocation, rollback-candidate, and active-current state for a particular artifact.
5. **SupportRecoveryState** — known-good recovery/manual capability, degraded operation, rollback readiness, hardware replacement, and restoration state.

A stronger product capability does not grant an installation stronger authority. A deployment may remain read-only, advisory, manual-only, or PLC-proxy even when the installed build is globally qualified for later capabilities.

After common discovery/reconstruction/validation work, the product path branches. A permanent PLC-proxy installation is a valid terminal operating mode and does not need to pass through direct remote-I/O takeover merely to qualify for permanent support. Direct takeover is a separate branch used only when evidence and customer constraints justify it.

## 2. Legacy evidence capture before isolation

When the predecessor control system is partially alive or still observable, ABIL should preserve useful predecessor evidence before isolation or removal whenever doing so is safe and practical.

The deployment record should explicitly classify predecessor evidence as at least:

- `LEGACY_REFERENCE_AVAILABLE`;
- `LEGACY_REFERENCE_CAPTURED`;
- `LEGACY_REFERENCE_PARTIAL`;
- `LEGACY_REFERENCE_UNAVAILABLE`.

Potential evidence includes network traffic, project/configuration state, tag/I/O mappings, controller/HMI relationships, command/response timing, protocol/mastership state, and rollback/fallback information.

If the predecessor is already dead, inaccessible, corrupt, or unsafe to interrogate, record that evidence gap. Do not pretend the resulting reconstruction has the same provenance or coverage ceiling as a case with captured predecessor evidence.

## 3. Identity hierarchy

Addresses and names are observations, not universal identity.

Keep distinct at least:

- `DeploymentIdentity` — the machine/installation subject;
- `TopologyGeneration` — immutable observed topology snapshot/generation;
- `NodeIdentity` — ABIL-stable logical device identity;
- `EndpointObservation` — time-bound IP address, fieldbus node number, slot, port, assembly/register, tag path, or other locator;
- `SignalChannelIdentity` — source-scoped signal/channel identity;
- `AdapterIdentity` — adapter implementation/configuration/profile identity.

Address equality must not silently imply device identity. Device replacement may preserve an address while changing hardware identity; network changes may alter addresses while preserving the device.

The immediate non-actuating R2 substrate must preserve source-scoped event identity and avoid making mutable transport locators the permanent machine identity key.

## 4. Typed intervention and evidence records

Action intent, authorization, execution, observation, and causal interpretation are separate records.

Use logically distinct objects equivalent to:

- `OperatorCommand` — technician/human requested action;
- `ActionProposal` — learner or diagnostic proposal only;
- `GatewayDecision` — independent permit/deny decision plus policy/envelope evidence;
- `ActionExecutionAttempt` — exact action issued to the target interface;
- `ExecutionReceipt` — acknowledgement/readback/result/ambiguity for that attempt;
- `TelemetryObservation` — subsequent sensed/observed machine evidence;
- `CausalHypothesis` / `Attribution` — later inference about whether an observation was caused by the action.

The architecture must not encode an answer-bearing learner-visible label such as `ACTION_CONSEQUENCE` merely because an observation occurred after a command. Temporal succession is evidence, not automatically proven causation.

## 5. Candidate, promotion, and runtime authority separation

A candidate-generating or adaptive/intelligence principal must be unable, by itself, to cause an unapproved artifact to become the artifact executed by the deterministic control runtime.

The write-capable architecture therefore separates at least these authority domains:

### 5.1 Candidate plane

The intelligence/commissioning plane may generate candidate machine models, control artifacts, and evidence packages. It may write candidate storage only. Candidate existence, model confidence, validation output, or an internal `approved=true` field grants no execution authority.

### 5.2 Validation/evidence plane

Validation systems may produce replay, simulation, shadow, coverage, timing, resource, fault-path, and commissioning evidence. They do not grant promotion authority merely because tests pass.

### 5.3 Promotion-authority plane

A separately authorized principal/process reviews an exact candidate package and, when authorized, emits an authenticated/integrity-protected promotion manifest or receipt.

A process name, role label, or self-asserted `authorized=true` is not an authority root. Before any write-capable implementation, the architecture requires a separate current authority grant/admission record (equivalent to `AuthorityGrant`) that is independently rooted and verifiable. The grant binds at least:

- authority-root/issuer identity and verifier/trust-material identity;
- authorized subject principal/process;
- exact deployment/machine identity and authority domain/output scope;
- permitted capability, mode, and action scope;
- validity/currentness and monotonic grant generation;
- revocation/supersession state; and
- independence constraints preventing candidate, learner, evaluator, plugin, or runtime-subject code from creating or mutating the grant.

Candidate/evaluator/learner/plugin principals cannot create, widen, refresh, revoke, or supersede that grant. Promotion/activation requires a current grant in addition to a valid promotion manifest. Deployment authority and artifact-promotion authority remain separate scopes/receipts even when one qualified organization or person may hold both roles for a particular installation; the two facts must remain independently evidenced.

The promotion manifest binds, directly or by stable digest/reference:

- exact deployment/machine identity;
- control-authority locus and ownership domain(s);
- topology generation;
- source machine-model/evidence version;
- semantic mapping/provenance cut where material;
- control-coverage ledger version;
- generated control artifact digest/version;
- target hardware/network/protocol/configuration identity;
- compiler/generator/runtime version/configuration where material;
- preserved safety-interface/handshake inventory;
- validation evidence set and acceptance result;
- declared operating envelope;
- installation-specific safe-state/fallback policy identity;
- predecessor active artifact/authority state;
- known-good rollback artifact/configuration;
- current authority grant/admission identity and verifier/trust-root identity;
- promotion authority/signoff identity;
- monotonic authority generation/epoch.

The architecture does not yet choose one cryptographic mechanism, but mutable unauthenticated metadata in the candidate/intelligence trust domain is insufficient for production authority.

### 5.4 Active artifact store and loader selection

Active/promoted artifact storage, loader selection, next-boot target, trust material, and authority ledger are protected from candidate-generation/learner/LLM/plugin write access.

Candidate storage and active/promoted storage are distinct trust domains.

### 5.5 Runtime-authority plane

The deterministic loader/runtime independently verifies the authenticated promotion manifest, exact artifact digest, deployment binding, authority generation, and ownership state before activation and again on restart.

It does not trust learner-generated claims of approval.

Activation must be atomic or transactionally equivalent from the runtime's perspective. Missing, partial, corrupt, mismatched, unauthenticated, unpromoted, wrong-deployment, or stale authority material cannot become active. The prior known-good artifact remains selected where allowed or the installation enters its validated non-operating/fallback state.

Execution evidence must expose the exact verified active artifact and promotion identity.

## 6. Authority epoch, revocation, and anti-rollback

Control authority is not ordinary checkpoint state.

Authority-bearing state must have a monotonic, separately authenticated generation such as `authority_epoch` or an equivalent durable ordering.

Required invariants:

- restoring learner/model/configuration backups cannot grant, downgrade, or resurrect control authority;
- the current accepted authority generation is checked independently of ordinary learner checkpoints;
- revocation and supersession survive ordinary backup restoration, restart, and appliance replacement;
- an old but cryptographically valid promotion cannot silently reactivate after a newer promotion, revocation, ownership transfer, safety/configuration change, or authority epoch;
- rollback to an older known-good artifact requires a **new** separately authorized rollback/promotion receipt with a newer authority generation;
- rollback means selecting older known-good artifact bytes under new current authority, not restoring an obsolete authority epoch;
- ownership/fencing generation is bound to current promotion/runtime authority so a stale restored writer cannot regain control.

If the authority ledger is missing, corrupt, divergent, or untrusted, the system gains no new write authority by inference.

## 7. Independent commissioning envelope

Write-capable semantic discovery must be bounded by an installation-specific commissioning envelope whose admissibility rules do not depend solely on the not-yet-qualified machine model being investigated.

Independent certified/hardwired safety protection remains necessary where applicable, but it does not necessarily prevent machine, tooling, product, or process damage from an unsafe ordinary output combination, order, timing, or state transition.

Before a commissioning write is allowed, the envelope must include, as applicable:

- deny-by-default writable I/O/capability scope;
- explicit technician/operator-authorized action class;
- independently established preconditions;
- prohibited output combinations, sequences, states, or rates;
- bounded action duration/extent and automatic cessation/reversion behavior;
- independent physical/operator stop or disable path;
- supervision requirements;
- jog/hold-to-run/reduced-speed/reduced-energy/reduced-force semantics where appropriate and independently established;
- gateway enforcement of state/combination/order/rate constraints, not merely scalar ranges;
- no implicit privilege expansion from one successful action to related commands;
- separate provenance for technician/engineer-supplied commissioning constraints versus relationships later learned by ABIL;
- explicit `UNKNOWN` handling when a required machine-protection condition is unresolved.

A required independently established precondition in `UNKNOWN` blocks that action. The learner may propose a command, but it does not get to define the sole rules that make its own experiment admissible.

## 8. Transactional command semantics

A timeout or reconnect must never be treated as proof that a physical command did not execute.

Future Stage-5 manual commissioning and Mode-B PLC-proxy actions must use a command transaction envelope containing, as applicable:

- unique `request_id` / operation identity;
- deployment/machine identity;
- authority domain and current ownership generation;
- current authenticated authority epoch/promotion identity;
- exact semantic operation and parameters;
- expected state/precondition version or snapshot when required;
- expiry/freshness/replay protection;
- acknowledgement lifecycle distinguishing at least accepted/rejected and, where supported, started/completed/failed/unknown-or-ambiguous;
- duplicate-request/idempotency policy;
- timeout and reconnect semantics;
- bounded queue depth/backpressure;
- target/protocol correlation identity where available;
- durable linkage among request, gateway decision, execution attempt, receipt, and subsequent observation.

The durable logical command identity is scoped by the authority state that made it admissible, conceptually equivalent to `(deployment, authority_domain, authority_epoch, ownership_generation, request_id)`. A request identifier does not float across authority transfers.

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME` is a first-class **durable** state. If acknowledgement is lost after possible physical execution, the unresolved transaction must survive process restart/reconnect long enough to prevent blind reissue and preserve later reconciliation. Durable state must retain the evidence actually available, the retry/idempotency disposition, and the eventual resolution if one is established.

A non-idempotent or physically ambiguous action must not be blindly retried after timeout/reconnect. Retry is allowed only when the operation is mechanically idempotent under the exact target contract or an installation-specific recovery rule explicitly establishes that retry is safe.

Reconnect must not implicitly replay unknown physical operations. Queue/backpressure behavior must not silently reorder or duplicate commands.

When promotion, rollback, cutover, ownership transfer, or revocation advances the authority or ownership generation:

- outstanding prior-generation commands do **not** migrate automatically into the new generation;
- unresolved prior-generation outcomes remain quarantined and auditable;
- reconnect/restart does not replay those historical operations merely because the new writer is healthy;
- a semantically equivalent later action requires a new request under the new authority generation unless an exact target-specific recovery contract proves otherwise;
- delayed or stale receipts from an old generation cannot satisfy or complete a new-generation request;
- queued-but-not-executed commands from a revoked generation lose authority and cannot be dispatched;
- restoring an old gateway queue or transaction store cannot resurrect command authority from an obsolete generation.

Rollback of artifact bytes does not roll command time backward. Selecting an older known-good artifact under a new rollback/promotion receipt creates a new authority generation; request/receipt state from the artifact's historical generation remains historical evidence.

## 9. Single-writer transfer and split-brain prevention

For every physical output/control namespace, exactly one authoritative ordinary-control writer exists at a time, or the namespace is explicitly in `NO_ACTIVE_AUTHORITY`, `AUTHORITY_OUTCOME_UNKNOWN`, or `DUAL_AUTHORITY_CONFLICT`.

An authority-transfer state machine should be able to represent, at minimum:

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

Transfer evidence binds exact deployment/topology generation, predecessor/current writer, output/I/O scope, protocol/master/session ownership where relevant, authority epoch/ownership generation, quiescence evidence, transfer operation identity, post-transfer readback, and rollback/fallback target.

If predecessor quiescence or new ownership cannot be established, do not continue merely because the new runtime is otherwise qualified.

If an authority transfer occurs while a physical command outcome is unresolved, that transaction remains explicitly quarantined across the transfer. Neither the new writer nor a restored old writer may silently reissue it; reconciliation must preserve the exact old authority/ownership generation and any later evidence about its physical effect.

## 10. Independent-safety noninterference

Ordinary ABIL discovery, commissioning, proxy, and direct-control capability is negatively scoped away from independent safety/protective ownership and configuration unless a separate explicitly engineered and authorized safety project grants exact scope.

Unknown protective/interlock semantics remain safety-relevant and out of scope for autonomous reconstruction until a current, independently authorized safety-classification record establishes otherwise. Any later classification or downgrade to ordinary control requires a current `SafetyClassificationRecord` (or equivalent safety-project record) independent of the ordinary ABIL candidate/learner/evaluator planes. It binds at least the classifier/signoff authority, exact deployment and topology generation, hazard/safety context, evidence digest/set, classification scope and affected asset/semantics, validity/currentness, and revocation/supersession state. Ordinary ABIL cannot create, refresh, or approve this record. Until a current record exists, the conservative safety-relevant classification remains authoritative.

Absent that separate safety authority, ordinary ABIL must not:

- claim ownership of safety PLCs, safety relays/controllers, or safety output namespaces;
- download, reset, or reconfigure safety projects/signatures;
- change drive safety configuration or safety-network ownership;
- bypass, mask, bridge around, spoof, or programmatically defeat guards, E-stops, or protective paths;
- alter shared adapter/network configuration in a way that silently disables the independent safety path;
- treat successful ordinary-controller replacement as proof that the safety path remains effective.

The deployment model binds the preserved safety-interface/handshake inventory and identifies ordinary-control dependencies required for the safety system to remain effective after replacement.

Later direct-control qualification must test safety-path noninterference across applicable startup, restart, ABIL runtime failure, intelligence-plane failure, communications loss, adapter/driver failure, controller replacement/cutover, rollback, and shared-infrastructure loss/recovery cases.

The exact physical safe-state/fallback response remains installation-specific.

## 11. Branching validation and permanent support

The early qualification sequence remains intentionally conservative, but the post-validation product path is a graph rather than one mandatory per-installation ladder.

Common evidence work may include substrate qualification, learner efficacy, replay, read-only discovery, advisory/semantic grounding, bounded commissioning, reconstruction, candidate synthesis, and offline/shadow validation.

After that common evidence base, an installation may remain in or promote to one of several terminal/supportable modes:

- **READ_ONLY / ADVISORY permanent support** — no write authority;
- **MANUAL_RECOVERY permanent support** — deterministic technician controls only within an approved commissioning/recovery envelope;
- **PLC_PROXY permanent support** — surviving PLC remains deterministic executor;
- **DIRECT_ABIL_CONTROL permanent support** — separately qualified ABIL deterministic runtime owns ordinary I/O domains.

A direct-control-capable product release does not force a deployment into direct control. A permanent PLC-proxy installation may receive the same lifecycle support, backup/recovery, diagnostics, and upgrade discipline without ever transferring I/O mastership to ABIL.

## 12. Minimum hostile-test obligations for future write-capable implementation

Future implementation contracts should be able to demonstrate at least:

1. learner/intelligence compromise cannot write/select/promote active artifacts or trust material;
2. candidate storage edits cannot alter active execution;
3. unapproved, wrong-deployment, wrong-config, stale, corrupt, partial, or unauthenticated promotion material is rejected;
4. restart verifies the exact current promotion/authority epoch before resuming writes;
5. restoring an old backup cannot resurrect a stale promotion, revocation, or ownership epoch;
6. rollback to older known-good artifact bytes requires a new authorized receipt at a newer authority epoch;
7. individually allowlisted commissioning commands unsafe in combination/order/state are rejected independently of learner permissives;
8. an action whose independent prerequisite is `UNKNOWN` is rejected;
9. acknowledgement loss after an executed physical command does not cause blind duplicate actuation;
10. duplicate request IDs obey the declared idempotency contract within the exact authority/ownership generation;
11. duplicate request IDs or delayed receipts from old authority generations cannot be mistaken for current-generation transactions;
12. reconnect/restart does not replay ambiguous commands and preserves unresolved ambiguity state;
13. queue/backpressure failure cannot silently reorder/duplicate physical operations;
14. restoring an old gateway queue/transaction store cannot resurrect old command authority;
15. an in-flight ambiguous command remains quarantined across writer ownership transfer or rollback;
16. stale writer generations are rejected after authority transfer;
17. safety/protective assets remain outside ordinary ABIL mutation/ownership and the independent safety path remains effective under declared failure/restart cases;
18. adaptive-learning services can be stopped/faulted without violating the already-qualified deterministic/manual degraded-operation contract.

## 13. Immediate R2 boundary

Nothing in this document authorizes or requires write-capable commissioning, PLC proxy execution, direct remote-I/O control, deterministic controller implementation, machine connection, deployment, or cutover in the immediate R2 substrate.

The immediate R2 subject remains non-actuating and should focus on an honest learner/evaluator/event/replay/checkpoint/resource substrate plus a separate learner-efficacy gate. It must remain forward-compatible with the identity/provenance distinctions above without importing later control authority into learner state.
