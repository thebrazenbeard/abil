# Component Evidence Invalidation Matrix V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NOT LEGAL OR CERTIFICATION ADVICE / NO PRODUCT-SELECTION AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #4

Parent evidence boundary:
- `docs/research/2026-09-18-component-conformance-evidence-boundary.md`

Architecture base examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

The component-evidence boundary says third-party qualification evidence is scoped, provenance-bearing, and invalidatable.

This document makes that principle more operational.

The core research question is:

> When one part of the deployed component subject changes, which evidence may remain valid, which evidence becomes conditional, and which claims must fall back to unknown or requalification-required?

The goal is not to define a certification program. It is to prevent unsupported inheritance before a future product-qualification contract exists.

## 1. Evidence subject model

A component evidence subject should be treated as a tuple, not a product name.

Minimum dimensions:

- manufacturer/vendor identity;
- product/model identity;
- hardware revision;
- firmware version;
- software/runtime/stack version;
- driver version;
- host OS distribution/version;
- kernel/configuration;
- protocol technology;
- protocol role/profile;
- vendor/device/profile identity where applicable;
- topology/integration role;
- electrical/power environment;
- environmental assumptions;
- certificate/declaration/test-report identity;
- standard/specification/test-suite edition;
- enabled options/features;
- licensing/branding representation where material;
- ABIL deployment subject that consumes the component.

Any qualification claim must identify which tuple dimensions it actually depends on.

## 2. Claim-owner classes

Every retained claim belongs to one qualification owner:

### `THIRD_PARTY_DIRECT`

Claim is supported directly by vendor/test-body evidence for the exact qualified component subject.

### `THIRD_PARTY_COMPOSITION_DEPENDENT`

Claim is useful only while stated host/integration assumptions remain true.

### `ABIL_OWNED`

Claim depends on ABIL behavior, configuration, orchestration, timing, authority, recovery, generated artifacts, or integration logic.

### `MACHINE_APPLICATION`

Claim depends on installation-specific semantics, commissioning, I/O mapping, process behavior, environmental conditions, safety validation, or machine-specific limits.

Claims do not migrate between owners merely because the underlying component is commercially qualified.

## 3. Invalidation outcomes

A future evidence graph should be able to place every affected claim into one of these states:

### `UNCHANGED_SUPPORTED`

The changed dimension is outside the claim's declared dependency envelope.

### `SUPPORTED_WITHIN_DECLARED_ENVELOPE`

The changed value differs but remains inside an explicitly documented qualified range/compatibility envelope.

### `REVIEW_REQUIRED`

The claim may remain valid, but existing evidence does not mechanically establish that the change is immaterial.

### `REQUALIFICATION_REQUIRED`

The change affects a bound qualification dependency and supporting evidence must be rerun/re-established.

### `UNSUPPORTED_UNKNOWN`

Evidence no longer supports the claim and no valid replacement evidence exists.

### `PROHIBITED_INHERITANCE`

The claim was never transferable to this owner/scope in the first place.

No state above implies authorization to deploy.

## 4. Change-to-evidence matrix

### Hardware revision changes

Possible effect:
- direct component evidence may remain valid only if the certificate/test report explicitly covers the revision;
- driver/runtime timing evidence may reopen;
- ABIL-owned integration tests may reopen if electrical/resource behavior changes;
- machine application evidence may reopen if I/O/power/environmental behavior changes.

Default when coverage is unclear:
`REVIEW_REQUIRED`, not silent inheritance.

### Firmware changes

Possible effect:
- protocol conformance may reopen;
- vendor/device/profile behavior may reopen;
- host API compatibility may reopen;
- timing/interoperability assumptions may reopen;
- ABIL orchestration/recovery tests may need rerun.

If exact firmware is part of the certificate subject and new firmware is not covered:
`REQUALIFICATION_REQUIRED`.

### Driver changes

Possible effect:
- host timing;
- error semantics;
- retry behavior;
- queueing;
- device discovery;
- reset/recovery behavior.

Direct product certification may remain untouched while composition-dependent and ABIL-owned evidence reopens.

### Host OS or kernel changes

Possible effect:
- vendor supportability;
- deterministic timing;
- driver compatibility;
- scheduler/resource behavior;
- update/recovery semantics.

A "supported OS family" statement is not equivalent to timing qualification.

### Protocol role/profile changes

Possible effect:
- conformance scope changes even when the same physical device remains;
- vendor/device/profile identity may differ;
- host orchestration assumptions change.

Default:
new qualification subject unless the evidence explicitly covers both roles/profiles.

### Topology changes

Examples:
- moving a protocol component behind a bridge/gateway;
- changing failure domains;
- moving deterministic runtime into a VM/container;
- adding external I/O aggregation;
- changing redundant path behavior.

Direct component evidence may survive while composition-dependent evidence reopens.

### Electrical/power changes

Possible effect:
- component environmental/electrical certification;
- external I/O behavior;
- restart/brownout recovery;
- machine-level fault response.

A component certificate does not automatically cover an assembled power architecture.

### Licensing/branding/vendor-ID changes

Possible effect:
- represented product identity;
- legal/conformance usage conditions;
- device/profile identifiers;
- certificate applicability.

Do not treat "same binary" as sufficient if represented identity is part of the evidence scope.

## 5. Invalidation lattice

A useful future rule is monotonic downgrade unless new evidence is added.

Example progression:

`UNCHANGED_SUPPORTED`
→ `SUPPORTED_WITHIN_DECLARED_ENVELOPE`
→ `REVIEW_REQUIRED`
→ `REQUALIFICATION_REQUIRED`
→ `UNSUPPORTED_UNKNOWN`

`PROHIBITED_INHERITANCE` is not a downgrade state. It means the claim never belonged to the target subject.

Evidence may move upward only when an explicit artifact justifies the move.

A human assertion such as "probably fine" does not move evidence upward.

## 6. Dependency-edge requirements

A future evidence graph should bind each claim to dependency edges such as:

- `DEPENDS_ON_HARDWARE_REVISION`
- `DEPENDS_ON_FIRMWARE`
- `DEPENDS_ON_DRIVER`
- `DEPENDS_ON_HOST_OS`
- `DEPENDS_ON_KERNEL_CONFIG`
- `DEPENDS_ON_PROTOCOL_ROLE`
- `DEPENDS_ON_TOPOLOGY`
- `DEPENDS_ON_ELECTRICAL_ENVIRONMENT`
- `DEPENDS_ON_CONFIGURATION`
- `DEPENDS_ON_LICENSE_OR_BRANDING_ROLE`
- `DEPENDS_ON_MACHINE_APPLICATION`

The absence of a declared edge must not automatically mean independence.

For high-consequence claims, missing dependency metadata should default to `REVIEW_REQUIRED`.

## 7. Derived-claim rules

A higher-level claim may depend on several lower-level evidence subjects.

Example:

`CYCLIC_PROTOCOL_PATH_QUALIFIED`

could require:
- certified protocol component subject;
- supported driver subject;
- supported OS/kernel subject;
- ABIL cyclic scheduler qualification;
- ABIL error/retry/recovery qualification;
- deployment topology qualification.

If any required dependency falls to `REQUALIFICATION_REQUIRED` or `UNSUPPORTED_UNKNOWN`, the derived claim cannot remain fully supported.

A derived claim cannot outrank its weakest required dependency.

## 8. Anti-laundering hostile cases

A future evidence engine should reject at least:

1. same model number, new hardware revision, old certificate retained with no revision coverage;
2. certified firmware upgraded in place and certificate carried forward by product name alone;
3. protocol card stays certified while host driver changes retry/queue semantics and ABIL retains end-to-end protocol qualification unchanged;
4. runtime moves from a tested Debian kernel to a different kernel and deterministic timing claim remains unchanged because the runtime still launches;
5. same card changes from one protocol role/profile to another while retaining old conformance evidence;
6. external I/O/power hardware is added to a certified industrial PC and the complete assembly is described as certified by association;
7. topology moves a component behind a gateway and end-to-end timing/interoperability claim is retained without requalification;
8. component vendor ID/profile representation changes while old interoperability/conformance claim remains;
9. machine-specific commissioning is treated as unaffected because all component certificates remain valid;
10. one component becomes stale, but a derived "controller qualified" claim remains green because the evidence graph tracks only top-level labels.

## 9. Evidence replacement

When old evidence becomes invalid or conditional, replacement evidence should identify:

- superseded evidence subject;
- new evidence subject;
- reason for replacement;
- affected claim IDs;
- whether scope is broader, narrower, or equivalent;
- whether historical deployed subjects remain under old evidence;
- whether existing deployments require review/requalification.

Replacing evidence for new builds must not silently rewrite the historical evidence state of already-deployed subjects.

## 10. Historical truth preservation

A future qualification system should answer both:

- "What evidence supports the current candidate?"
- "What evidence supported deployed subject X at the time it was commissioned?"

Evidence invalidation for a new version does not erase historical provenance.

Likewise, a newly obtained certificate does not retroactively prove that an older deployment was qualified if the historical subject did not match its scope.

## 11. Release/update consequence

A future product/update pipeline should not ask only:

`Did tests pass?`

It should also ask:

- did any qualification dependency change?
- which claims depend on that changed dimension?
- did those claims remain inside declared evidence envelope?
- which claim owners must act?
- which deployments are affected?
- what claim state should be downgraded until evidence is restored?

This is especially important for routine-looking firmware, driver, kernel, or configuration updates.

## 12. Separation from machine authority

An evidence state of `UNCHANGED_SUPPORTED` or `SUPPORTED_WITHIN_DECLARED_ENVELOPE` does not authorize:

- machine connection;
- write access;
- commissioning;
- promotion;
- activation;
- safety ownership;
- deployment.

Qualification evidence and operational authority remain separate subjects.

## 13. Research disposition

The practical productization rule is:

> Component qualification should be represented as a dependency graph with explicit invalidation semantics, not as a durable badge attached to a product name.

That allows ABIL to benefit from qualified commercial components while preventing certification/conformance claims from surviving changes that actually alter the evidence subject.

No certification claim, evidence-engine implementation, product selection, procurement, license acceptance, implementation plan, machine connection/write, commissioning, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
