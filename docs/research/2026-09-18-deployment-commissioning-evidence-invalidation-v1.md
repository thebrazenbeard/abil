# Deployment Commissioning Evidence Invalidation V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Relevant architecture contracts:
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`
- `docs/FIELD_VALIDATION_ROADMAP.md`
- `docs/ARCHITECTURE_BOUNDARIES.md`

Related component-evidence research:
- Draft PR #4 component-conformance and invalidation work

## Purpose

The successor architecture already treats these as orthogonal state domains:

- `ProductCapabilityQualification`
- `DeploymentCommissioningState`
- `ExecutionAuthorityState`
- `ControlArtifactLifecycle`
- `SupportRecoveryState`

Product capability qualification and component evidence can therefore remain valid while one particular machine installation has changed enough that its prior commissioning evidence is stale.

This research asks:

> What machine/deployment changes should invalidate or narrow deployment-specific commissioning evidence before ABIL is allowed to rely on it again?

This is deliberately separate from:

- product/runtime qualification;
- component certification/conformance;
- current execution authority;
- artifact promotion authority;
- functional-safety qualification.

A globally qualified ABIL build does not make stale commissioning evidence current.

## 1. Deployment commissioning subject

A deployment commissioning subject should bind, at minimum:

- `DeploymentIdentity`;
- exact `TopologyGeneration`;
- control-authority locus classification;
- node/source identity set;
- mutable endpoint/address observations;
- signal/channel identity set;
- I/O ownership/configuration;
- semantic mapping/provenance cut;
- commissioning envelope identity;
- independently established preconditions;
- prohibited combinations/sequences/rates;
- operating envelope;
- machine-model/evidence version;
- control-coverage ledger version;
- target hardware/network/protocol configuration;
- preserved safety-interface/handshake inventory;
- target-specific fallback/safe-state policy identity;
- known-good rollback/manual-recovery subject;
- commissioning evidence set;
- timestamp/currentness boundary;
- technician/engineer signoff identity where applicable.

A human-readable machine name is not sufficient deployment identity.

## 2. Commissioning evidence classes

Deployment-specific evidence should distinguish at least:

### `TOPOLOGY_EVIDENCE`

What devices, relationships, interfaces, and ownership paths were observed for a topology generation.

### `SEMANTIC_GROUNDING_EVIDENCE`

Which signal/device/function meanings were technician-supplied, vendor-supplied, inferred, tested, or otherwise established.

### `COMMISSIONING_ENVELOPE_EVIDENCE`

Which manual/write-capable actions were independently bounded by deny-by-default scope, preconditions, prohibited combinations, duration/rate limits, supervision, stop/disable paths, and explicit unknown handling.

### `CONTROL_COVERAGE_EVIDENCE`

Which promoted states, transitions, commands, permissives, timers, fault/recovery paths, and ordinary interlocks are supported within the declared operating envelope.

### `TARGET_BEHAVIOR_EVIDENCE`

Timing, protocol, restart, reconnect, fault, degraded-mode, and fallback behavior demonstrated on this installation subject.

### `CUTOVER_OWNERSHIP_EVIDENCE`

Single-writer/fencing, predecessor quiescence, ownership-generation transfer, and post-transfer readback evidence.

### `SUPPORT_RECOVERY_EVIDENCE`

Known-good rollback/manual recovery, appliance replacement, restart, and restoration evidence for the installation.

These classes may invalidate independently.

## 3. Deployment change classes

At minimum track:

- device replacement;
- I/O module replacement;
- drive/VFD/servo replacement;
- firmware change;
- PLC/PAC project/configuration change;
- HMI/SCADA/control-PC change;
- adapter/driver change;
- fieldbus/protocol configuration change;
- node/address remap;
- topology/gateway/switch change;
- wiring/I/O remap;
- sensor/actuator replacement;
- machine tooling change;
- mechanical modification;
- sequence/recipe logic change;
- operating envelope change;
- production material/process change;
- safety-interface/handshake change;
- commissioning-envelope change;
- authority-locus change;
- fallback/safe-state policy change;
- rollback/manual-recovery subject change.

A change report should identify both the observed changed value and the previous bound subject.

## 4. Deployment evidence outcomes

A changed deployment evidence subject should result in one of:

### `CURRENT_SUPPORTED`

No relevant deployment dependency changed.

### `SUPPORTED_WITHIN_DECLARED_ENVELOPE`

A value changed but remains inside a previously qualified deployment range explicitly covered by retained evidence.

### `PARTIAL_RECOMMISSION_REQUIRED`

Only identified commissioning evidence classes must be re-established before dependent actions/claims can be relied upon.

### `FULL_RECOMMISSION_REQUIRED`

The deployment subject changed broadly enough that the prior commissioning cut cannot safely be reused as current evidence.

### `UNKNOWN_CURRENTNESS`

Change/currentness cannot be established well enough to rely on prior deployment evidence.

### `PROHIBITED_CARRYOVER`

Prior evidence belongs to a different deployment/identity/authority subject and must not be inherited.

No state above grants execution authority.

## 5. Invalidation is dependency-specific

A machine change should not force unnecessary full requalification when the affected dependency can be bounded.

Examples:

### Sensor replacement, same qualified interface

May reopen:
- node/source identity;
- calibration/scale;
- semantic grounding if behavior differs;
- relevant control-coverage evidence;
- related fault detection.

May not automatically reopen:
- unrelated deterministic runtime qualification;
- unrelated protocol-component conformance.

### Drive firmware update

May reopen:
- drive behavior/timing;
- fault/reset semantics;
- motion/command handling;
- target-specific commissioning envelope;
- restart/recovery;
- control coverage using those semantics.

It does not automatically invalidate every machine-model fact unrelated to the drive.

### Mechanical tooling change

May leave network topology unchanged while reopening:
- state-transition timing;
- actuator/sensor causal relationships;
- process permissives;
- operating envelope;
- fault/recovery paths.

A topology-only currentness check is therefore insufficient.

## 6. Topology generation is necessary but not sufficient

The architecture already binds `TopologyGeneration`.

This research adds an important limit:

> Same topology generation does not prove same commissioned machine behavior.

Examples:
- tooling changed with identical control nodes;
- sensor replaced at same address;
- firmware behavior changed without endpoint change;
- recipe/sequence behavior changed in surviving PLC;
- mechanical stops/travel changed;
- process material changes alter timing or permissible ranges.

Deployment currentness therefore needs both structural identity and behavior/commissioning dependencies.

## 7. Identity and replacement rules

Address equality is not device continuity.

If a replacement device occupies the same:
- IP address;
- node number;
- slot;
- tag path;
- assembly/register;
- port;

prior source-specific commissioning evidence must not silently attach to the replacement device.

Where exact identity continuity cannot be established:
`UNKNOWN_CURRENTNESS` or `PROHIBITED_CARRYOVER` applies to dependent evidence.

## 8. Semantic mapping invalidation

Human-supplied semantics can become stale.

Examples:
- physical output rewired;
- valve manifold channel reassigned;
- PLC tag retains name but meaning changes;
- technician label reflected old tooling;
- same drive command selects a different configured mode.

A semantic label should bind:
- source/channel identity;
- deployment/topology subject;
- provenance;
- as-of/currentness;
- evidence or technician confirmation;
- dependencies that can invalidate it.

Correct historical semantics are not automatically current semantics.

## 9. Commissioning-envelope invalidation

A previously valid write-capable commissioning envelope can become stale when:

- actuator behavior changes;
- tooling changes;
- preconditions change;
- operating range changes;
- stop/disable path changes;
- supervisory ownership changes;
- independent protective assumptions change;
- prohibited combinations/sequences change;
- safe bounded duration/rate changes.

If an independently established required precondition is no longer current, that action returns to deny-by-default.

`UNKNOWN` remains blocking.

## 10. Control-coverage invalidation

Control coverage should be dependency-bearing.

A promoted behavior may depend on:
- specific node/source identity;
- exact semantic mappings;
- observed timing range;
- operating regime;
- technician-specified requirement;
- vendor configuration;
- fault/recovery evidence;
- topology/ownership state.

When one dependency becomes stale, the affected behavior should downgrade rather than the ledger remaining globally green.

Potential statuses:

- `COVERED_CURRENT`
- `COVERED_WITHIN_ENVELOPE`
- `COVERAGE_REVIEW_REQUIRED`
- `COVERAGE_RETEST_REQUIRED`
- `COVERAGE_UNKNOWN`
- `OUTSIDE_CURRENT_ENVELOPE`

## 11. Promotion/currentness consequence

A prior promoted artifact can remain historically valid evidence while becoming inadmissible for current activation.

If a deployment dependency bound by the promotion manifest changes materially:

- the old promotion receipt remains historical provenance;
- current activation must not treat it as current merely because signature/digest remains valid;
- affected deployment evidence must be re-established;
- any later activation/promotion uses a new current authority/evidence subject.

Cryptographic validity is not deployment-currentness.

## 12. Execution authority remains separate

A change that invalidates commissioning evidence does not itself decide current writer ownership.

Likewise, a currently fenced/authorized writer does not prove its commissioning evidence is current.

If current execution authority exists but a required deployment evidence dependency becomes stale, the target-specific contract must determine whether the installation:

- continues within a smaller already-supported envelope;
- transitions to degraded/manual mode;
- enters fallback/non-operating state;
- requires re-commissioning before stronger actions resume.

The intelligence plane must not silently widen the envelope to preserve uptime.

## 13. Ambiguous change/currentness

Some deployment changes will be discovered after the fact.

Examples:
- maintenance replaced a sensor without recording exact model;
- PLC logic was modified by a vendor;
- wiring changed during repair;
- firmware auto-updated;
- tooling changed between shifts.

The system should preserve:

`DEPLOYMENT_CHANGE_OUTCOME_UNKNOWN`

or equivalent until evidence establishes what changed.

Absence of a recorded change is not proof that no change occurred.

## 14. Currentness evidence sources

Potential currentness evidence may include:

- immutable device identity/serial where available;
- firmware/configuration digests;
- topology snapshots;
- controller project/configuration hashes;
- I/O configuration readback;
- adapter/driver version;
- technician maintenance record;
- physical inspection;
- controlled readback;
- behavior/timing comparison;
- calibration record;
- commissioning replay;
- negative/held-out validation.

No single evidence source is universally sufficient.

## 15. Deployment heartbeat is not enough

A runtime heartbeat can establish liveness.

It cannot by itself prove:
- unchanged physical machine;
- unchanged wiring;
- unchanged device identity;
- unchanged semantics;
- unchanged commissioning envelope;
- unchanged control coverage.

Currentness and liveness are separate.

## 16. Hostile research cases

A future deployment-currentness contract should fail closed on at least:

1. replacement sensor at same address inherits old semantic mapping automatically;
2. PLC project changes while topology remains identical;
3. mechanical tooling changes while all network identities remain unchanged;
4. drive firmware update silently retains old timing/fault/recovery evidence;
5. valve output is rewired but the tag name remains unchanged;
6. same machine deployment ID is reused after major control-cabinet rebuild;
7. safety-interface handshake changes while ordinary control commissioning remains green;
8. commissioning stop/disable path is altered without invalidating write envelope;
9. promoted artifact remains cryptographically valid and is reactivated despite stale deployment evidence;
10. current execution-authority receipt is treated as proof of current commissioning evidence;
11. unrecorded maintenance change is assumed not to have happened;
12. only topological currentness is checked despite known process/mechanical dependency changes;
13. fallback/manual recovery hardware changes but support-recovery evidence remains current;
14. a stale technician label is treated as permanent machine truth;
15. a partial recommission result is incorrectly promoted to full deployment-currentness.

## 17. Partial recommissioning

A useful future product should avoid two bad extremes:

- trust all old commissioning evidence forever;
- force total recommissioning after every minor change.

Partial recommissioning should be possible when dependency edges prove the affected surface.

A partial recommission receipt should bind:

- exact changed deployment subject;
- detected change(s);
- affected evidence classes;
- evidence retained as current;
- evidence re-established;
- unresolved dependencies;
- resulting operating envelope;
- resulting control-coverage state;
- resulting support/recovery state;
- exact timestamp/as-of;
- responsible signoff where required.

Missing dependency information should bias toward broader review, not optimistic carryover.

## 18. Historical truth preservation

Recommissioning does not rewrite history.

The system should retain:

- what was commissioned previously;
- what changed;
- which prior evidence became stale;
- which evidence remained valid;
- what was re-established;
- which promoted artifacts were valid for which deployment cuts.

This supports audit, rollback analysis, and root-cause reconstruction without pretending historical evidence is current.

## 19. Relationship to product/component qualification

Product qualification answers:

> Is this ABIL build/component stack qualified to provide capability X for a declared product profile?

Deployment commissioning answers:

> Has this particular installation established the machine-specific evidence required to use capability X here, now, within this operating envelope?

Both must be current where the action requires both.

A current product qualification cannot repair stale deployment evidence.

Current deployment evidence cannot extend a product beyond its qualified capability.

## 20. Research disposition

The practical rule is:

> Deployment commissioning must be treated as dependency-bearing evidence with explicit currentness and invalidation semantics, not as a permanent "commissioned=true" flag.

That preserves the successor architecture's orthogonal state model and prevents machine changes from silently inheriting stale semantic, control-coverage, or commissioning authority assumptions.

No commissioning action, evidence-engine implementation, machine access/write, product selection, procurement, license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
