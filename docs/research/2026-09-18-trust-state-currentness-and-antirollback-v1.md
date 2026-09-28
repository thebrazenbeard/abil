# Trust-State Currentness and Anti-Rollback V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #20 — evidence producer authenticity
- Draft PR #18 — evidence-ledger integrity / continuity
- PR #6 — write-capability admission design
- Draft PR #8 — support/recovery currentness

## Purpose

PR #20 distinguishes historical verification material from current producer-acceptance material.

A state-management question remains:

> How should verifier/trust configuration remain current and non-regressive across backup, restore, failover, rotation, revocation, and supersession?

Authority anti-rollback does not automatically protect evidence-verifier trust state.

A restore may leave authority unchanged while silently reviving an old producer trust root or revoked credential.

## 1. Trust state is a separately governed subject

A future trust state should have an immutable subject identity.

Conceptually:

`EvidenceTrustStateSubject`

Potential fields:
- deployment or organization scope;
- trust-domain profile;
- current trust-state generation;
- accepted producer identities;
- accepted trust roots/keys;
- accepted verifier profiles;
- accepted algorithms/profiles where applicable;
- revocation set;
- supersession/rotation lineage;
- delegation set;
- historical-verification material references;
- current producer-acceptance material references;
- effective time/currentness;
- protected configuration identity;
- immutable digest.

This research does not mandate a schema.

## 2. Monotonic trust-state generation

Current producer-acceptance state should advance monotonically.

Examples:
- T17 -> T18 after credential rotation;
- T18 -> T19 after producer revocation;
- T19 -> T20 after verifier-profile hardening.

Restore to T17 must not silently become current when T20 already exists.

Historical T17 may remain readable for historical verification.

## 3. Current trust versus historical verification

Keep separate:

### `CURRENT_ACCEPTANCE_TRUST`

Material permitted to authenticate **new** evidence now.

### `HISTORICAL_VERIFICATION_TRUST`

Retired material retained so old evidence can be verified against the trust state applicable when it was created.

Historical verification material does not grant current producer eligibility.

## 4. Trust-state dispositions

Suggested states:

- `TRUST_STATE_CURRENT`
- `TRUST_STATE_SUPERSEDED`
- `TRUST_STATE_REVOKED`
- `TRUST_STATE_STALE`
- `TRUST_STATE_UNKNOWN`
- `TRUST_STATE_CONFLICTING`
- `TRUST_STATE_PARTIAL`
- `TRUST_STATE_ROLLBACK_DETECTED`

A record verified under a stale trust state may need a lower claim ceiling or explicit historical-only interpretation.

## 5. Restore anti-rollback

On restore:

- compare restored trust generation to protected/current trust generation;
- reject silent downgrade;
- preserve historical trust material separately;
- do not reactivate retired producer acceptance;
- preserve revocation/supersession state;
- preserve delegation revocation state;
- preserve verifier-profile hardening.

A byte-valid backup may contain stale trust state.

## 6. Same-authority-generation case

Critical case:

1. authority epoch A12 remains current;
2. trust state T20 revokes evaluator key K1;
3. backup from T17 still trusts K1;
4. appliance restore loads backup;
5. authority still legitimately remains A12;
6. K1 becomes accepted again unless trust state is independently protected.

Expected:
`TRUST_STATE_ROLLBACK_DETECTED`
or fail-closed equivalent.

Authority currentness cannot repair stale verifier trust state.

## 7. Failover / replication

In HA/replicated deployments:

- trust-state generation must replicate to the qualified commit point;
- standby nodes must not accept older trust material after failover;
- conflicting trust states must be explicit;
- producer acceptance should fail closed when current trust generation cannot be established.

A stale replica must not be selected because it accepts more producers.

## 8. Rotation lineage

Rotation should preserve:

- predecessor trust state;
- successor trust state;
- old producer credential;
- new producer credential;
- effective transition;
- whether old material remains historical-only;
- overlap/grace rules if any;
- exact scope.

Ambiguous overlap must not create two silently current producer identities unless policy explicitly allows it.

## 9. Revocation lineage

Revocation should bind:

- revoked producer/trust material;
- reason/classification;
- effective generation/time;
- scope;
- prospective versus retroactive semantics;
- affected evidence classes;
- affected deployments;
- downstream claim-review requirement if applicable.

Restoring a pre-revocation snapshot must not erase the revocation.

## 10. Verifier-profile hardening

Trust state includes verifier policy, not only keys.

Examples:
- old profile allowed SHA-1;
- new profile requires stronger profile;
- old profile accepted self-signed evaluator evidence;
- new profile requires independent trust root;
- old profile omitted deployment scope.

Restoring old verifier policy can be as dangerous as restoring old keys.

## 11. Algorithm/profile supersession

Historical evidence may need old algorithm support for verification.

That does not imply the old profile remains acceptable for new evidence.

A verifier should know whether a profile is:

- current for new production;
- historical-verification-only;
- prohibited entirely.

## 12. Delegation anti-rollback

If producer A once delegated to B but later revoked delegation:

- old backup must not restore B's current eligibility;
- historical records produced during valid delegation may remain authentic;
- future B records must fail current producer acceptance.

Delegation state therefore participates in trust-state generation.

## 13. Cross-deployment scope

Trust state may be:
- global;
- organization-wide;
- deployment-specific;
- evidence-class-specific.

Generation/currentness must bind the intended scope.

T20 for Deployment A does not automatically supersede T7 for unrelated Deployment B unless the trust hierarchy says so.

## 14. Trust-state read receipt concept

A future `EvidenceTrustStateReadReceipt` could bind:

- trust-state subject;
- generation;
- digest;
- deployment/scope;
- accepted verifier profile;
- accepted trust-root set digest;
- revocation-set digest;
- delegation-set digest;
- historical-material-set digest;
- read/evaluation time;
- reader/verifier identity;
- currentness disposition;
- immutable receipt digest.

This is a research shape, not a required schema.

## 15. Independent currentness resolution

The claimant whose record is being verified must not decide which trust-state generation applies.

A verifier should resolve the expected current trust state independently.

Otherwise a producer could present an older trust state that still accepts it.

## 16. Split-brain trust state

If two replicas claim different current generations:

Potential status:
`TRUST_STATE_CONFLICTING`.

Do not:
- select the more permissive state;
- union the accepted key sets;
- accept both as current automatically.

Protected evidence issuance/verification may need to fail closed for affected scope.

## 17. Trust-state availability failure

If current trust state is unavailable:

- historical verification may continue where safe;
- new high-consequence evidence acceptance may be blocked;
- unauthenticated/low-trust evidence can remain explicitly labeled;
- do not silently fall back to last-known permissive state.

## 18. Trust-state evidence in currentness cuts

PR #11-style currentness receipts may need the trust-state generation used to authenticate their producers.

A currentness receipt authenticated under stale T17 should not be treated as equivalent to one authenticated under required T20 if producer eligibility changed.

## 19. Evidence-ledger linkage

PR #18 checkpoints should bind the trust-state generation used to authenticate producers where material.

If ledger L40 contains records accepted under T18 and later T20 revokes a producer retroactively for a compromise interval, downstream claim review may be required.

Do not rewrite ledger history; annotate/reconcile trust interpretation.

## 20. Reconciliation linkage

PR #17 reconciliation receipts can change historical conclusions.

The reconciliation producer should be authenticated against the trust state current for reconciliation issuance.

A stale restored trust state must not make a revoked reconciler current again.

## 21. Safety evidence linkage

Independent safety evidence may have a separate, stronger trust state.

Ordinary ABIL evidence-trust state must not override it.

If safety trust state is unavailable/conflicting:
- ordinary ABIL cannot infer safety authority from general evidence trust.

## 22. Credential compromise

If a trust root or verifier credential is compromised:

- advance trust-state generation;
- mark affected producer/trust material;
- retain historical evidence;
- apply retroactive-compromise policy where defined;
- identify downstream claims requiring review;
- block new evidence from compromised material.

The exact incident-response process remains future implementation/governance.

## 23. Backup metadata

A backup containing trust configuration should bind:

- trust-state generation;
- trust-state digest;
- accepted-current material set digest;
- historical-only material set digest;
- revocation/supersession digest;
- verifier-profile digest.

Restore compares these against protected/current trust state.

## 24. Garbage collection

Historical trust material may eventually be removed only when policy proves it is no longer required to verify retained evidence or audits.

Deleting old verification material can make truthful historical evidence unverifiable.

Retaining old material must not make it current for new acceptance.

## 25. Trust bootstrap and first generation

The initial trust-state generation remains a protected bootstrap decision.

This research does not authorize:
- choosing trust roots;
- installing keys;
- configuring a PKI;
- creating credentials.

It only requires that bootstrap become an explicit immutable trust-state subject rather than untracked ambient configuration.

## 26. Hostile research cases

A future implementation should fail closed or downgrade for at least:

1. restore pre-revocation trust state after producer key revoked;
2. restore old verifier profile that accepts weaker evidence;
3. standby failover uses stale trust generation;
4. two replicas disagree on current producer set;
5. old delegated producer becomes current again after restore;
6. producer supplies an older trust state that still accepts it;
7. historical verification key is treated as current producer key;
8. algorithm deprecated for new evidence is silently re-enabled;
9. trust-store backup omits revocation set;
10. trust-state generation matches but digest differs;
11. current authority remains valid and incorrectly masks stale trust state;
12. safety evidence is verified under ordinary evidence trust instead of safety trust;
13. compromised root remains accepted for new evidence after rotation;
14. current trust unavailable causes fallback to permissive historical state;
15. garbage collection deletes trust material needed to verify retained evidence;
16. trust state for Deployment A is incorrectly reused for Deployment B;
17. currentness receipt omits trust-state generation;
18. reconciliation receipt is issued by producer revoked in current trust state;
19. rollback restores old delegation chain;
20. bootstrap configuration exists with no immutable generation/subject.

## 27. Relationship to PR #20

PR #20 asks:

> Who actually produced this evidence, under what role/scope/trust?

This research asks:

> Which verifier/trust state is current, and can restore/failover make that acceptance state regress?

Producer authenticity and trust-state currentness are separate.

## 28. Evidence ceiling

This research does not:

- create credentials;
- rotate/revoke credentials;
- select a PKI/provider;
- select cryptographic algorithms;
- install trust roots;
- change verifier configuration;
- authorize safety evidence;
- authorize machine writes.

It defines trust-state currentness and anti-rollback properties only.

## 29. Research disposition

The practical rule is:

> Historical trust may remain readable, but current evidence-acceptance trust must be monotonic, scope-bound, and non-regressive across restore and failover.

No trust-state implementation, credential/provider mutation, trust-root provisioning, machine access/write, commissioning, deployment, promotion, merge/canonical promotion, or other protected effect is authorized by this research.
