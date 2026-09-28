# Support / Recovery State Currentness V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Relevant architecture contract:
- `docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md`

Related research:
- Draft PR #7 deployment commissioning evidence invalidation
- Draft PR #4 component evidence invalidation

## Purpose

The successor architecture defines `SupportRecoveryState` as an orthogonal state domain covering:

- known-good recovery/manual capability;
- degraded operation;
- rollback readiness;
- hardware replacement;
- restoration state.

Authority anti-rollback is already explicit: restoring backups cannot resurrect stale authority, and selecting older artifact bytes requires new current authority.

A different unresolved question remains:

> When is a recovery/manual/rollback capability itself still current and trustworthy after software, hardware, topology, configuration, or deployment evidence changes?

The phrase "known good" must not become permanent merely because a recovery path worked once.

## 1. Support / recovery subject

A support/recovery evidence subject should bind, where applicable:

- deployment identity;
- topology generation;
- recovery capability type;
- exact recovery artifact/configuration digest;
- deterministic runtime/loader version;
- target hardware identity;
- storage/media identity where material;
- adapter/driver/protocol configuration;
- required deployment commissioning evidence cut;
- required product/component qualification cut;
- preserved safety-interface inventory;
- fallback/safe-state policy identity;
- manual control surface identity;
- authority-neutral restore procedure;
- current authority/admission prerequisites;
- backup/snapshot subject and creation time;
- restore-test subject;
- rollback-test subject;
- hardware-replacement procedure subject;
- required external dependencies;
- technician/operator prerequisites;
- last successful qualification/readback time;
- known exclusions and unsupported conditions.

A file called `known_good.img` is not evidence by itself.

## 2. Recovery capability classes

At minimum distinguish:

### `MANUAL_RECOVERY_CAPABILITY`

A bounded manual/operator surface that can restore or maintain limited useful operation without the adaptive intelligence plane.

### `ARTIFACT_ROLLBACK_CAPABILITY`

Ability to select older known-good artifact bytes under **new current authority**, not restore their historical authority epoch.

### `APPLIANCE_RESTORE_CAPABILITY`

Ability to rebuild/restore the appliance software/state while preserving authority anti-rollback and deployment identity boundaries.

### `HARDWARE_REPLACEMENT_CAPABILITY`

Ability to replace failed computing/interface hardware and re-establish the required product/deployment evidence without inheriting stale identity or authority.

### `DEGRADED_OPERATION_CAPABILITY`

Ability to continue within an explicitly smaller validated envelope when intelligence or noncritical services fail.

### `NON_OPERATING_FALLBACK_CAPABILITY`

Ability to transition reproducibly to the target-specific validated non-operating/fallback state.

These are separate capabilities; one passing does not prove another.

## 3. Recovery evidence states

Suggested research states:

### `RECOVERY_CURRENT`

Exact support/recovery subject remains supported by current evidence.

### `RECOVERY_CURRENT_WITHIN_ENVELOPE`

Recovery remains supported only within a declared reduced/current envelope.

### `RECOVERY_REVIEW_REQUIRED`

A dependency changed and current evidence does not mechanically establish that recovery remains valid.

### `RECOVERY_RETEST_REQUIRED`

The changed dependency directly affects recovery behavior and the relevant path must be re-exercised/requalified.

### `RECOVERY_UNKNOWN`

Recovery currentness cannot be established.

### `RECOVERY_PROHIBITED_CARRYOVER`

Evidence belongs to a different deployment/hardware/configuration subject and must not be inherited.

None of these states grants execution authority.

## 4. Dependencies that can stale recovery evidence

At minimum:

- hardware replacement;
- storage-device replacement;
- BIOS/firmware change;
- OS/kernel change;
- deterministic runtime/loader change;
- driver/adapter change;
- fieldbus/protocol configuration change;
- network/topology change;
- I/O ownership/configuration change;
- machine/deployment commissioning change;
- safety-interface change;
- manual-control surface change;
- fallback/safe-state policy change;
- artifact format/compiler/generator change;
- backup format/version change;
- credential/trust-material rotation;
- external service/dependency change;
- support procedure/tooling change.

A dependency change may reopen only part of recovery evidence, but that effect must be explicit.

## 5. Backup validity is not recovery validity

A backup can be:

- intact;
- decryptable/readable;
- content-addressed correctly;
- restorable in a lab;

and still be unsafe or inadmissible for the current deployment.

Reasons include:

- stale authority state;
- stale deployment commissioning evidence;
- old topology;
- incompatible runtime/driver;
- removed hardware;
- changed safety/fallback policy;
- outdated device identity;
- unresolved command transactions;
- obsolete ownership/fencing generation.

Therefore:

> Backup integrity proves preserved bytes, not current recoverability or current authority.

## 6. Restore must not restore authority

The architecture already requires authority anti-rollback.

Support/recovery research should preserve this stronger separation:

A restore operation may recover:
- learner/model state;
- non-authority configuration;
- candidate artifacts;
- logs/evidence;
- approved historical artifact bytes;
- recovery tooling;

but must not by itself recover:
- obsolete authority epoch;
- revoked grant;
- stale ownership generation;
- historical active-artifact selection as current authority;
- old queued command authority;
- old unresolved command treated as safely replayable.

Authority must be re-established from the current protected authority subject.

## 7. Historical artifact rollback

"Rollback" must distinguish:

### Bytes rollback

Select older known-good artifact bytes.

### Authority rollback

Restore old authority state.

Bytes rollback can be legitimate under a new authorized promotion/rollback receipt.

Authority rollback is prohibited.

Recovery evidence should prove the mechanism preserves this distinction across restart and appliance replacement.

## 8. Unresolved command state across recovery

A recovery path must preserve ambiguous physical outcomes.

If a command from the pre-failure generation has:

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME`

then:

- restoring the gateway/runtime must not replay it automatically;
- selecting older artifact bytes must not erase it;
- replacing hardware must not turn it into `NOT_EXECUTED`;
- the new authority generation must not accept a delayed old receipt as completion of a new request;
- later reconciliation remains linked to the historical authority/ownership generation.

Recovery success that loses ambiguity evidence is not qualified recovery.

## 9. Hardware replacement currentness

A replacement appliance or interface may be operationally equivalent while still requiring new evidence.

Bind at least:

- new hardware identity;
- trusted boot/runtime subject where applicable;
- driver/interface identity;
- restored deployment identity;
- current authority verifier/trust root;
- topology/interface readback;
- commissioning dependencies affected by the replacement;
- storage/backup restoration subject;
- recovery test evidence;
- single-writer/fencing state.

Same model number does not prove same support/recovery subject.

## 10. Manual recovery surface currentness

A manual fallback surface can become stale when:

- I/O mappings change;
- device identity changes;
- actuator semantics change;
- operating envelope changes;
- commissioning prerequisites change;
- safety/fallback interfaces change;
- control authority locus changes;
- operator procedure changes.

A manual control page that still renders is not evidence that its actions remain admissible.

Required preconditions in `UNKNOWN` remain blocking.

## 11. Degraded operation

A degraded mode must bind:

- services/components allowed to fail;
- capability that remains available;
- reduced operating envelope;
- resource assumptions;
- watchdog/failure detection;
- transition into degraded mode;
- transition out of degraded mode;
- state reconciliation on return;
- current commissioning/support evidence required;
- fallback if degraded assumptions fail.

"System stayed running" is not enough to prove declared degraded capability.

## 12. Recovery after adaptive-plane failure

Once a deterministic/manual capability is promoted, adaptive intelligence failure should not automatically remove that qualified capability.

However, restart of the intelligence plane must not:

- overwrite active runtime state;
- widen operating envelope;
- promote a new candidate;
- rewrite authority state;
- erase ambiguous transactions;
- attach stale learned state to replaced devices;
- claim deployment currentness without evidence.

Recovery of learning services is separate from recovery of control authority.

## 13. Recovery after authority loss/corruption

If authority ledger/current grant state is:

- missing;
- corrupt;
- divergent;
- untrusted;

support/recovery may restore non-authority evidence and tooling, but it gains no new write authority by inference.

Allowed outcome may be:
- read-only diagnostics;
- non-operating fallback;
- separately qualified manual surface that does not require the missing authority domain;
- explicit authority-recovery process.

The exact permitted behavior must be target-specific and prequalified.

## 14. Support-recovery currentness versus deployment currentness

PR #7 research asks whether machine-specific commissioning evidence is still current.

This research asks whether the declared recovery mechanism remains current.

They intersect but are not identical.

Examples:

- machine commissioning remains current, but backup format is no longer restorable on the updated appliance;
- product/runtime remains qualified, but manual recovery mapping is stale after wiring changes;
- rollback artifact bytes remain valid, but the fallback policy changed;
- new hardware is product-qualified, but deployment restoration has not been re-established.

A support/recovery claim cannot substitute for deployment commissioning evidence.

## 15. Support-recovery currentness versus product/component qualification

A replacement industrial PC may have current product/component qualification.

That does not prove:

- the deployment backup restores correctly;
- interface mappings match;
- current authority can be re-established;
- manual recovery works;
- fallback behavior matches the machine;
- ambiguous transactions survive correctly.

Likewise, a successful restore does not qualify the hardware/product generally.

## 16. Recovery receipt concept

A future `RecoveryQualificationReceipt` could bind:

- exact recovery capability class;
- deployment identity;
- recovery subject digest;
- source backup/artifact identity;
- target hardware/runtime subject;
- required product/deployment evidence references;
- procedure identity;
- preconditions;
- test/exercise evidence;
- readback/result;
- exclusions;
- currentness/as-of;
- invalidation dependencies;
- resulting support/recovery state.

This research does not mandate that representation.

## 17. Invalidation / partial retest

A change should trigger the smallest justified recovery retest only when dependency edges prove the unaffected surfaces.

Examples:

### HMI-only change

May not reopen deterministic artifact rollback, but could reopen operator/manual recovery UI evidence.

### Storage-device replacement

May reopen backup/restore, persistence, ambiguous-transaction durability, and boot recovery without reopening unrelated machine semantics.

### Driver update

May reopen hardware-replacement and deterministic/manual I/O recovery paths.

### Tooling change

May leave appliance restore intact while reopening manual recovery and fallback envelope evidence.

Missing dependency data should bias toward broader review.

## 18. Hostile research cases

A future support/recovery contract should fail closed on at least:

1. old backup restores an obsolete authority epoch;
2. older artifact bytes reactivate without a new current rollback/promotion receipt;
3. appliance replacement inherits prior writer ownership solely from restored disk state;
4. ambiguous pre-failure command disappears after restore;
5. delayed receipt from old generation satisfies a new-generation command;
6. manual recovery UI retains stale I/O mapping after rewiring;
7. replacement device at same address inherits old manual semantics;
8. degraded mode remains labeled qualified after required watchdog/resource assumptions changed;
9. fallback policy changed but old recovery test remains green;
10. storage migration preserves files but loses durable ambiguity journal;
11. runtime/driver update breaks restore but backup integrity check still passes;
12. current product qualification is treated as proof of deployment recovery;
13. successful lab restore is treated as proof of current machine rollback;
14. support procedure depends on an unavailable external tool/service;
15. recovery evidence from one deployment is copied to another identical-looking machine;
16. restore returns learner/model state whose source identities no longer match current devices;
17. hardware replacement uses same model but different firmware/adapter behavior and old receipt remains current;
18. a failed recovery exercise is omitted while the support state stays `KNOWN_GOOD`.

## 19. Periodic exercise / aging

Some recovery claims age even without explicit known changes.

Potential reasons:
- backups become unreadable;
- dependencies disappear;
- credentials/trust material rotate;
- procedures/tool versions drift;
- spare hardware becomes unavailable;
- operators lose access/knowledge;
- firmware/runtime support ends.

A future product may therefore need freshness/exercise policy for recovery evidence.

This is not a recommendation for one universal interval. The interval should depend on consequence and change rate.

## 20. Historical truth preservation

When recovery evidence becomes stale:

- do not erase that it once passed;
- record the exact historical subject and evidence;
- mark why it is no longer current;
- bind any replacement/retest evidence;
- preserve which deployed versions were covered at the time.

A new successful recovery test must not retroactively prove an older unsupported deployment.

## 21. Research disposition

The practical rule is:

> `SupportRecoveryState` should be evidence-backed and invalidatable, not a permanent label such as `KNOWN_GOOD` or `ROLLBACK_READY`.

Recovery must preserve authority anti-rollback, single-writer ownership, ambiguous physical-outcome evidence, deployment identity, and the exact reduced envelope actually proven.

No recovery action, restore operation, machine access/write, evidence-engine implementation, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
