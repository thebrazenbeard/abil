# Trust-State Transition Authorization V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #20 — evidence producer authenticity
- Draft PR #21 — trust-state currentness / anti-rollback
- PR #6 — write-capability admission design

## Purpose

PR #21 defines a monotonic current trust state.

Monotonicity alone does not establish legitimacy.

An attacker or misconfigured component could publish a higher generation that trusts a malicious producer.

The question is:

> What makes a transition from trust state T(n) to T(n+1) authorized, scoped, reviewable, and non-self-authorizing?

This research defines transition-authorization properties only.

It does not authorize any actual credential, trust-root, verifier, provider, or policy mutation.

## 1. Transition subject

A future trust-state change should be represented as an immutable transition subject.

Conceptually:

`EvidenceTrustStateTransition`

Potential fields:
- prior trust-state subject/digest;
- prior generation;
- proposed successor generation;
- proposed successor trust-state digest;
- transition class;
- deployment/organization/trust-domain scope;
- exact additions/removals;
- exact revocations;
- exact rotations/supersessions;
- verifier-profile changes;
- delegation changes;
- effective time;
- emergency/ordinary classification;
- proposer identity;
- required authorizer policy/profile;
- approvals/attestations;
- transition evidence digest.

## 2. Transition classes

Distinguish at minimum:

### `INITIAL_BOOTSTRAP`

Creates the first trust-state subject.

### `ADD_PRODUCER`

Adds new current producer eligibility.

### `REMOVE_PRODUCER`

Removes eligibility without necessarily marking compromise.

### `ROTATE_PRODUCER`

Moves current producer identity/material from predecessor to successor.

### `REVOKE_PRODUCER`

Marks producer/trust material invalid according to declared prospective/retroactive policy.

### `HARDEN_VERIFIER_PROFILE`

Makes acceptance policy stricter.

### `RELAX_VERIFIER_PROFILE`

Makes acceptance policy more permissive.

### `ADD_DELEGATION`

Allows one authorized principal/domain to delegate scoped evidence production.

### `REVOKE_DELEGATION`

Removes that delegation.

### `EMERGENCY_REVOKE`

Fast fail-closed removal for suspected compromise.

### `TRUST_DOMAIN_RESTRUCTURE`

Changes trust-domain or scope relationships.

Different classes may require different authorization policy.

## 3. Higher generation is not self-authenticating

Reject:

`generation(Tx) > generation(Tcurrent)`

as sufficient evidence of legitimacy.

The successor must also satisfy the current transition-authorization policy.

Otherwise:
`UNAUTHORIZED_HIGHER_GENERATION`.

## 4. Authorization policy binding

The current trust state or separately protected governance subject should bind the policy for its own successor transitions.

A future transition evaluator should know:
- allowed transition classes;
- allowed proposers;
- required authorizer roles;
- required threshold/quorum;
- scope restrictions;
- emergency override rules;
- prohibited self-approval cases;
- effective-time constraints;
- transition-specific evidence requirements.

The proposed successor must not choose the policy that validates itself.

## 5. Self-authorization prohibition

A producer being added to trust must not be able to authorize its own admission merely by presenting a valid credential.

Likewise:
- a producer being revoked must not be the sole authority preventing revocation;
- a verifier profile being relaxed must not self-validate under the relaxed rules;
- a new trust root must not authenticate its own bootstrap unless the governing bootstrap contract explicitly requires a separately rooted ceremony.

Self-signed is not the same as self-authorized.

## 6. Separation of proposer and authorizer

Potential model:

- proposer prepares exact transition subject;
- one or more authorized principals approve;
- deterministic evaluator verifies policy;
- successor trust state is derived from exact approved transition.

A single actor may fill multiple roles only if the policy explicitly allows it.

High-consequence transitions may require role separation.

## 7. Quorum / threshold semantics

If quorum is required, bind:
- exact eligible authorizer set/profile;
- threshold;
- distinct principal identities;
- role requirements;
- whether duplicate identities count once;
- whether delegated approvals are allowed;
- approval validity/freshness;
- scope.

Examples:
- 2 of 3 trust administrators;
- one commissioning authority + one security authority;
- one emergency security revoker for emergency revoke only.

This research does not mandate a specific threshold.

## 8. Transition scope

A transition should not exceed its authorized scope.

Examples:
- deployment-specific admin cannot alter organization-wide trust;
- evaluator-domain admin cannot change safety trust;
- ordinary ABIL trust cannot modify independent safety trust;
- one evidence-class administrator cannot authorize another class unless policy says so.

Scope widening must be explicit.

## 9. Permissive versus restrictive transitions

More permissive transitions often deserve stricter authorization than restrictive ones.

Examples:

### Restrictive
- revoke compromised producer;
- remove algorithm;
- disable delegation.

### Permissive
- add trust root;
- add producer;
- relax verifier profile;
- widen deployment scope;
- create delegation.

A future policy may allow faster restrictive fail-closed transitions while requiring stronger approval for permissive expansion.

## 10. Emergency revocation

Emergency revocation may need:
- lower-latency authorization;
- narrower transition class;
- immediate effective time;
- later review/ratification;
- immutable incident reference;
- exact scope;
- no ability to add new trust or relax verifier policy.

Emergency power should fail closed, not become a general-purpose trust mutation channel.

## 11. Emergency recovery

If emergency revocation later proves mistaken:
- do not delete the revocation event;
- create a new authorized transition restoring eligibility if appropriate;
- preserve historical interruption;
- preserve affected evidence/claim review.

History is append/supersede, not rewrite.

## 12. Rotation authorization

Rotation should bind:
- retiring identity/material;
- successor identity/material;
- overlap/grace policy;
- effective time;
- historical verification treatment;
- deployment/evidence scope;
- authorizer approvals.

A new producer key cannot become current merely because the old producer says it is its successor unless policy allows that delegation/rotation model.

## 13. Verifier-profile changes

Verifier policy transitions can be more important than key rotation.

Examples:
- algorithm set;
- required trust root;
- canonicalization profile;
- deployment binding;
- producer-role constraints;
- revocation semantics.

A profile relaxation should be explicit and strongly authorized.

Silent policy downgrade is prohibited.

## 14. Delegation transitions

Delegation should bind:
- delegator;
- delegate;
- evidence role;
- scope;
- duration;
- onward-delegation permission;
- revocation policy.

A delegate cannot widen its own delegation.

Onward delegation is denied unless explicitly permitted.

## 15. Transition currentness

An approved transition may still become stale before application.

Potential reasons:
- prior trust state advanced;
- authorizer lost authority;
- emergency revocation superseded it;
- deployment scope changed;
- proposal expired.

A future evaluator should bind exact prior generation and reject applying a transition against a different parent unless explicitly rebased/reapproved.

## 16. Concurrent transitions

Two valid proposals may race from T20:

- TxA -> T21A
- TxB -> T21B

Both cannot silently become one current state.

Possible outcomes:
- one wins and the other becomes superseded;
- transitions are mechanically commutative and recomposed under a new approved subject;
- conflict requires explicit reconciliation.

Do not union trust changes automatically.

## 17. Transition replay

An old authorized transition must not be replayed after later generations.

Example:
- T20 -> T21 adds producer K2;
- T22 later revokes K2;
- replay old T20->T21 transition against current state.

Expected:
reject parent-generation mismatch.

## 18. Transition provenance

Retain:
- exact proposal;
- exact approvals;
- exact authorization policy;
- evaluator result;
- predecessor subject;
- successor subject;
- application time;
- supersession/conflict history;
- incident/change-ticket reference where applicable.

A bare “admin changed trust store” log line is insufficient.

## 19. Transition authenticity

Approvals themselves need authenticated producer identities under the appropriate governance trust domain.

Evidence producer trust and trust-transition authorization may use separate roots/domains.

A producer credential accepted for telemetry does not automatically authorize trust-state transitions.

## 20. Bootstrapping / first trust state

The first generation cannot rely on a predecessor trust state.

Therefore bootstrap should be a separately governed protected procedure with an immutable bootstrap manifest/record.

Potential inputs:
- initial trust roots;
- initial verifier profile;
- initial administrator/authorizer policy;
- scope;
- creation provenance;
- external/manual ceremony evidence.

This research does not authorize performing that bootstrap.

## 21. Transition read/validation receipt

A future `TrustStateTransitionValidationReceipt` could bind:
- transition digest;
- predecessor trust subject;
- expected predecessor generation;
- proposed successor digest;
- transition class;
- governing authorization policy/profile;
- authenticated approvals;
- threshold result;
- scope result;
- currentness result;
- conflict/supersession result;
- final disposition;
- immutable receipt digest.

Research shape only.

## 22. Dispositions

Suggested outcomes:
- `TRANSITION_AUTHORIZED`
- `TRANSITION_UNAUTHORIZED`
- `TRANSITION_SCOPE_MISMATCH`
- `TRANSITION_THRESHOLD_NOT_MET`
- `TRANSITION_SELF_AUTHORIZATION_REJECTED`
- `TRANSITION_PARENT_SUPERSEDED`
- `TRANSITION_CONFLICTING`
- `TRANSITION_EXPIRED`
- `TRANSITION_APPROVER_REVOKED`
- `TRANSITION_POLICY_UNKNOWN`

## 23. Safety trust separation

Independent safety trust should have its own transition policy.

Ordinary ABIL trust administrators must not:
- add safety signers;
- relax safety verifier policy;
- revoke safety authorities;
- alter safety trust scope

unless a separate explicitly authorized safety-governance process grants that authority.

## 24. Restore / anti-rollback

PR #21 protects current trust state from rollback.

This research adds:
- the current trust state must also have an authorized transition lineage.

A restored T19 cannot claim legitimacy over T20 merely because T19 has valid historical transition evidence.

Currentness and authorization lineage are both required.

## 25. Evidence-ledger linkage

Trust transitions should be preserved in the evidence ledger or equivalent protected governance history.

Selective deletion of:
- revocations;
- approvals;
- denied transitions;
- conflicts

must not make a later trust state appear cleaner or more legitimate.

## 26. Unauthorized mutation handling

If current trust configuration differs from the last authorized trust-state subject:
- mark `TRUST_CONFIGURATION_DIVERGENCE`;
- do not silently bless the ambient configuration as a new generation;
- block affected high-consequence evidence acceptance if required;
- investigate/reconcile under authorized procedure.

Ambient configuration is not automatically canonical trust state.

## 27. Hostile research cases

A future implementation should reject or fail closed on at least:

1. attacker creates T99 that trusts itself;
2. new producer authorizes its own addition;
3. relaxed verifier profile validates the transition that relaxed it;
4. one required approver signs twice under two aliases;
5. revoked approver's old approval is reused;
6. deployment admin modifies global trust;
7. ordinary ABIL admin modifies safety trust;
8. emergency revoker adds a new trust root;
9. emergency revoke is silently deleted after incident;
10. concurrent T20 transitions are automatically unioned;
11. old authorized add transition replays after producer later revoked;
12. transition applies to wrong parent generation;
13. delegation widens itself;
14. delegate creates onward delegation despite prohibition;
15. rotation introduces new key outside approved evidence scope;
16. trust-store configuration changes with no transition subject;
17. transition history omits denied/conflicting proposals;
18. bootstrap exists with no immutable governance record;
19. current trust state is monotonic but lineage contains unauthorized transition;
20. transition verifier trusts approvals under the same permissive successor policy being proposed.

## 28. Relationship to PR #20/#21

PR #20:
- authenticates evidence producers.

PR #21:
- establishes which trust state is current/non-regressive.

This research:
- establishes whether movement from one trust state to the next was authorized.

All three are distinct.

## 29. Evidence ceiling

This research does not:
- create credentials;
- add/remove trust roots;
- rotate/revoke producers;
- select PKI/provider/algorithms;
- mutate verifier policy;
- approve any actual trust transition;
- authorize safety governance;
- authorize machine writes.

It defines transition-authorization properties and failure semantics only.

## 30. Research disposition

The practical rule is:

> A newer trust-state generation is current only if it is both non-regressive and descended through an authorized, scope-correct transition lineage.

No trust-transition implementation, credential/provider mutation, trust-root provisioning, verifier mutation, machine access/write, commissioning, deployment, promotion, merge/canonical promotion, or other protected effect is authorized by this research.
