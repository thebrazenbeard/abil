# Evidence Producer Authenticity V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #18 — evidence ledger integrity / continuity
- Draft PR #16 — execution evidence / causal attribution
- Draft PR #17 — transaction reconciliation
- Draft PR #11 — non-authority currentness proof
- PR #6 — write-capability admission design

## Purpose

Ledger continuity can prove that retained records were not silently truncated or reordered.

That does not prove the claimed producer actually created the record.

The question is:

> How should ABIL distinguish an authentic gateway/evaluator/technician/safety/currentness record from a forged record that merely has the correct schema and fields?

This research defines producer-authenticity semantics without choosing a cryptographic provider or mutating credentials.

## 1. Claimed identity versus authenticated identity

Every evidence record should distinguish:

- `claimed_producer_identity`;
- `authenticated_producer_identity`;
- `producer_role`;
- `trust_domain`;
- `verifier_profile`;
- `authenticity_disposition`.

A schema field reading `producer=evaluator` is not authentication.

## 2. Producer authenticity dispositions

Suggested research states:

- `AUTHENTICATED_CURRENT`
- `AUTHENTICATED_HISTORICAL`
- `AUTHENTICATED_BUT_SCOPE_MISMATCH`
- `AUTHENTICATED_BUT_SUPERSEDED`
- `AUTHENTICATED_BUT_REVOKED_FOR_NEW_EFFECTS`
- `UNVERIFIED_PRODUCER`
- `VERIFIER_UNKNOWN`
- `SIGNATURE_OR_ATTESTATION_INVALID`
- `PRODUCER_CONFLICT`
- `TRUST_DOMAIN_MISMATCH`

These are evidence-authenticity states, not authority states.

## 3. Verifier identity

A future verifier should bind:

- verifier implementation/profile identity;
- accepted producer trust roots or keys;
- accepted algorithm/profile identity where applicable;
- canonicalization profile;
- expected producer role;
- scope/profile the producer is allowed to attest;
- current validity/revocation material;
- evaluation time/currentness;
- exact evidence record digest.

The record claimant must not select its own permissive verifier profile.

## 4. Role/scope binding

An authenticated producer may still be out of scope.

Examples:

- telemetry collector authenticates a sensor sample but cannot issue safety classification;
- learner authenticates its own hypothesis but cannot authenticate independent evaluator truth;
- gateway authenticates an execution attempt but cannot self-issue technician signoff;
- commissioning engineer may attest semantic grounding but not independent safety ownership unless separately authorized;
- target adapter may authenticate target receipt semantics but not causal attribution.

Authentication is necessary but not sufficient for role authority.

## 5. Trust-domain separation

Evidence roles should remain distinct:

- learner/candidate plane;
- deterministic runtime;
- gateway;
- telemetry collector;
- target/device;
- operator/technician;
- evaluator/reviewer;
- currentness evaluator;
- promotion/authority plane;
- independent safety project.

A producer credential from one domain must not automatically satisfy another domain's evidence role.

## 6. Self-attestation limits

The plane benefiting from a stronger claim must not be able to create the independent evidence that upgrades that claim unless the design explicitly allows it.

Examples to reject:

- learner signs `CAUSAL_ATTRIBUTION_SUPPORTED` as if it were evaluator evidence;
- candidate generator signs `CONTROL_COVERAGE_CURRENT`;
- runtime signs `SAFETY_CLASSIFICATION_CURRENT`;
- gateway signs technician approval;
- benchmark participant signs evaluator score.

Self-authenticated evidence should remain labeled self-originated.

## 7. Historical authenticity versus current producer validity

A producer credential may later expire, rotate, or be revoked.

Historical evidence can remain authentic if:

- it was valid at creation/attestation time;
- required timestamp/order evidence is supportable;
- the signature/attestation verifies against the historical trust state;
- revocation semantics do not require retroactive invalidation.

Distinguish:

> historical authenticity

from:

> current eligibility to produce new evidence.

## 8. Revocation semantics

A future trust profile should define whether revocation is:

- prospective only;
- retroactive for compromised credentials;
- scoped to certain evidence classes;
- scoped to a producer role;
- scoped to one deployment or time interval.

A blanket "key revoked => all historical records invalid" may destroy truthful history.

A blanket "historical signatures always valid" may preserve forged records after key compromise.

The revocation model must be explicit.

## 9. Rotation / supersession

When producer credentials rotate:

- new records use the new current credential/profile;
- old records retain historical producer identity;
- trust lineage should preserve old -> new succession where relevant;
- old credentials must not silently regain current producer authority after restore;
- evidence verification should know which credential/profile was current at record creation.

Rotation is not evidence-history rewrite.

## 10. Compromise handling

If a producer credential is believed compromised:

- preserve affected historical records;
- mark authenticity/currentness uncertainty according to policy;
- identify affected time/scope;
- identify downstream claims that relied on those records;
- reverify/recollect evidence where possible;
- do not silently delete the records;
- do not automatically trust a new credential as proof the old history was clean.

Potential disposition:
`PRODUCER_COMPROMISE_REVIEW_REQUIRED`.

## 11. Timestamp / creation-time evidence

Historical authenticity may depend on knowing when a record was created.

Potential supporting evidence:

- trusted timestamp/profile;
- ledger sequence/checkpoint;
- external checkpoint anchor;
- device monotonic counter;
- database/WAL sequence;
- signed batch checkpoint.

Wall-clock timestamp alone may be insufficient.

## 12. Canonicalization binding

Any signature/attestation must bind deterministic canonicalization.

A verifier should know:

- schema version;
- field order;
- null/omitted semantics;
- numeric representation;
- units;
- string/binary encoding;
- nested references;
- collection ordering;
- timestamp representation.

Otherwise producer identity may verify over different logical content than the consumer interprets.

## 13. Record versus envelope authenticity

Some systems may authenticate:

- each record individually;
- a signed evidence segment;
- a signed checkpoint root;
- an authenticated transport envelope.

These provide different guarantees.

A signed segment proves inclusion only if:
- record-to-segment inclusion is verifiable;
- segment identity is current/valid;
- no required partitions are omitted;
- ledger continuity/completeness requirements from PR #18 are met.

## 14. Target/device evidence

Target/device receipts may be:

- natively authenticated;
- authenticated through a trusted gateway/session;
- unauthenticated protocol data;
- authenticated only at transport layer.

The evidence claim should reflect the actual level.

Do not promote unauthenticated target data to `AUTHENTICATED_TARGET_RECEIPT`.

## 15. Human evidence

Technician/operator evidence may use different authentication methods than machine records.

Potential provenance may include:

- authenticated user identity;
- session identity;
- role;
- deployment scope;
- signoff action;
- device/workstation identity where material;
- timestamp;
- exact evidence object reviewed.

A display name is not sufficient identity for high-consequence signoff.

## 16. Evaluator evidence

Independent evaluator records should bind:

- evaluator identity;
- evaluation profile/version;
- subject under review;
- exact evidence cut;
- result;
- limitations/evidence ceiling.

The learner/candidate plane must not be able to mint evaluator identity.

## 17. Safety evidence

Safety-classification evidence has stronger independence requirements.

A future verifier should bind:

- independent safety-project identity;
- classifier/signoff identity;
- exact deployment/topology subject;
- exact safety scope;
- verifier/trust-root identity;
- currentness/revocation state.

Ordinary ABIL producer credentials cannot satisfy this by role substitution.

## 18. Currentness receipts

PR #11 currentness receipts should bind authenticated evaluator/reader identity.

A currentness receipt should be rejected or downgraded if:

- producer identity is unverified;
- verifier profile is caller-selected incorrectly;
- producer is outside allowed role;
- trust material is stale/revoked for new evidence;
- evidence cut does not match authenticated subject.

## 19. Reconciliation receipts

PR #17 reconciliation records may change historical interpretation.

Therefore their producer/reviewer authenticity should be independently verifiable.

A learner-generated "resolution" should not become authoritative reconciliation merely because it is appended to the ledger.

## 20. Evidence-ledger checkpoints

PR #18 ledger checkpoints may themselves require producer authenticity.

A perfect hash chain generated by an untrusted claimant proves internal consistency of that claimant's history, not independent authenticity.

Checkpoint authenticity and ledger continuity are separate properties.

## 21. Multi-signature / quorum concepts

Some high-consequence evidence may require more than one producer.

Possible research patterns:

- technician + commissioning engineer;
- runtime + gateway;
- evaluator + independent reviewer;
- safety engineer + safety authority.

This research does not mandate quorum/multisignature.

It establishes that if quorum is required, the exact participants/roles and threshold must be machine-checkable.

## 22. Trust-root bootstrap

A future implementation must define how initial producer/verifier trust is established.

Possible sources:

- installation trust manifest;
- protected configuration;
- external PKI;
- hardware identity;
- manually provisioned trust roots.

This research does not choose one.

The bootstrap itself is a protected-effect/configuration concern and is outside current authority.

## 23. Restore / rollback

Restoring old verifier/trust configuration must not silently re-enable revoked producer credentials for current evidence production.

Historical verification may still need access to retired trust material.

Therefore distinguish:

- historical verification material;
- current producer-acceptance material.

Restore semantics should not collapse them.

## 24. Cross-deployment evidence

A producer may be authenticated globally but still out of scope for a specific deployment.

Evidence should bind deployment or allowed deployment scope where material.

An authenticated receipt from Deployment A must not be accepted as evidence for Deployment B solely because producer identity is valid.

## 25. Delegation

If one producer delegates evidence authority to another:

- delegation identity;
- scope;
- validity;
- chain;
- revocation;
- exact evidence classes;
- deployment scope

should be explicit.

Implicit delegation by shared credentials is dangerous.

## 26. Anonymous / unauthenticated evidence

Unauthenticated evidence may still be useful as low-confidence observation.

It should be labeled accordingly.

Examples:
- unauthenticated broadcast;
- legacy protocol readback;
- manually imported log with uncertain provenance.

The system should not discard it automatically.

But stronger claims must not treat it as authenticated producer evidence.

## 27. Authenticity receipt concept

A future `EvidenceAuthenticityReceipt` could bind:

- evidence record/checkpoint digest;
- claimed producer;
- authenticated producer;
- producer role;
- trust domain;
- verifier profile;
- trust material identity;
- creation/as-of evidence;
- revocation/rotation status;
- scope;
- disposition;
- limitations;
- immutable receipt digest.

This is a research shape, not a mandated schema.

## 28. Hostile research cases

A future implementation should fail closed or downgrade evidence for at least:

1. learner emits evaluator-shaped record;
2. gateway emits technician-signoff record;
3. valid producer signs evidence outside its deployment scope;
4. revoked producer continues issuing new records;
5. historical record is rejected solely because current credential rotated, despite valid historical trust evidence;
6. compromised credential's old records remain blindly trusted despite retroactive-compromise policy;
7. record signature verifies under caller-selected permissive verifier profile;
8. canonicalization mismatch changes logical content after verification;
9. signed checkpoint omits negative-evidence partition;
10. trust store restore re-enables revoked credential;
11. target receipt is unauthenticated but labeled authenticated;
12. human display name treated as signoff identity;
13. evaluator record omits exact evidence cut;
14. safety classification accepted from ordinary ABIL credential;
15. currentness receipt self-issued by candidate plane;
16. cross-deployment authenticated evidence is reused incorrectly;
17. implicit delegation occurs through shared key;
18. multi-party threshold is bypassed by one role;
19. old compromised key and new rotated key both appear current;
20. verifier cannot identify which trust state applied at record creation.

## 29. Relationship to PR #18

PR #18 asks:

> Is the required evidence history internally intact and complete enough?

This research asks:

> Did the claimed producer/trust domain actually originate the evidence under the expected role/scope?

Both are required for stronger evidence claims.

A signed forged-history root from the wrong producer is not enough.
A perfectly authenticated individual receipt inside a truncated ledger is also not enough.

## 30. Evidence ceiling

This research does not:

- choose a signature algorithm;
- choose a PKI/provider;
- create or rotate credentials;
- define certificate lifetimes;
- provision trust roots;
- authorize safety signoff;
- authorize write authority.

It defines producer-authenticity properties and failure semantics only.

## 31. Research disposition

The practical rule is:

> Evidence provenance is not just a producer label; stronger claims require independently verifiable producer identity, role, scope, trust state, and historical validity.

No producer-authentication implementation, credential creation/rotation/revocation, trust-root provisioning, evidence-ledger implementation, machine access/write, commissioning, deployment, promotion, merge/canonical promotion, or other protected effect is authorized by this research.
