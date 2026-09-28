# Governance Root / Bootstrap Boundary V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #20 — evidence producer authenticity
- Draft PR #21 — trust-state currentness / anti-rollback
- Draft PR #22 — trust-state transition authorization

## Purpose

PR #22 requires trust-state transitions to be authorized by identities rooted in an appropriate governance trust domain.

That raises a recursion question:

> What authorizes the governance trust domain itself?

This research defines the termination boundary.

ABIL must not recursively self-prove the ultimate governance root that authorizes changes to ABIL's own trust system.

The ultimate governance/bootstrap anchor is an external protected authority subject.

## 1. Root boundary

Define a conceptual boundary:

`GovernanceRootAnchor`

The root anchor is:
- externally established;
- immutable for the duration of its active generation;
- protected from ordinary ABIL mutation;
- independently identifiable;
- explicit about scope;
- explicit about who/what may authorize subordinate trust-state transitions.

ABIL may verify and consume the anchor.

ABIL does not self-create or self-justify it.

## 2. Bootstrap is a protected effect

Creating the first governance root is not an ordinary runtime operation.

It may require:
- explicit human authority;
- external security/governance process;
- protected installation procedure;
- hardware or organizational identity;
- manual ceremony;
- immutable bootstrap manifest.

This research does not authorize performing that bootstrap.

## 3. Root anchor subject

A future root anchor may bind:

- root-anchor ID;
- generation;
- organization/project scope;
- trust-domain scope;
- allowed subordinate domains;
- governance authorizer identities or profiles;
- transition-policy profile;
- emergency-governance profile;
- effective time;
- predecessor anchor if any;
- bootstrap provenance;
- external authority reference;
- immutable digest.

Exact representation is open.

## 4. Root generation

If root anchors can change, root generation should be monotonic.

Examples:
- G1 initial anchor;
- G2 authority-set rotation;
- G3 governance-policy hardening.

A restored older root must not silently become current.

Historical roots may remain available for historical verification.

## 5. Root transition is not an ordinary subordinate transition

A subordinate trust state may be changed under the current governance root.

Changing the governance root itself requires a different protected process.

Do not allow:
- evidence trust admins;
- trust-transition admins;
- learner/candidate plane;
- ordinary runtime;
- deployment-local admin

to rewrite the governance root merely because they are authorized below it.

## 6. External authority requirement

A root transition should require exact external authority.

Within this ABIL project, Patrick remains the sole merge/protected-effect authority unless a fresher exact authority record supersedes that boundary.

Research can model root-transition requirements.

Research cannot exercise that authority.

## 7. No self-bootstrap

Reject any pattern where:
- new governance root authenticates its own creation;
- new governance policy validates the transition that installs it;
- subordinate trust state promotes itself to governance root;
- learner-generated evidence creates governance authority.

The root must be anchored externally.

## 8. Root currentness

A future verifier should know whether the root anchor is:

- `GOVERNANCE_ROOT_CURRENT`
- `GOVERNANCE_ROOT_HISTORICAL`
- `GOVERNANCE_ROOT_SUPERSEDED`
- `GOVERNANCE_ROOT_REVOKED`
- `GOVERNANCE_ROOT_UNKNOWN`
- `GOVERNANCE_ROOT_CONFLICTING`
- `GOVERNANCE_ROOT_ROLLBACK_DETECTED`

Unknown/conflicting current root should fail closed for trust-state transitions.

## 9. Root anti-rollback

Restore/failover must not revive an older governance root.

Critical case:

1. current root G3 removes compromised administrator A;
2. backup from G1 still includes A;
3. restore loads G1;
4. subordinate trust state remains otherwise current.

Expected:
- detect root rollback;
- do not accept A as current governance authority;
- block affected trust-state transitions.

## 10. Historical verification

Historical root material may be needed to verify:
- old trust-state transitions;
- old approvals;
- old evidence-authenticity decisions;
- incident history.

Historical root material must remain clearly historical-only.

It cannot authorize new transitions.

## 11. Governance-root transition record

A root change should retain:

- prior root subject;
- proposed successor root;
- exact change;
- external authority evidence;
- approval/signoff provenance;
- effective time;
- emergency/ordinary classification;
- resulting successor root;
- supersession record.

This research does not define the exact signature/provider mechanism.

## 12. Root versus trust-state transition

Keep separate:

### governance root transition
changes who governs subordinate trust.

### trust-state transition
changes producer/verifier acceptance under the current governance root.

A valid subordinate transition cannot modify the governance root unless the root policy explicitly delegates a protected root-transition power—which itself must be externally anchored.

## 13. Emergency governance

Emergency governance may need a narrowly scoped path to:
- revoke compromised governance identity;
- freeze subordinate trust changes;
- force fail-closed operation.

Emergency governance should not automatically allow:
- adding new roots;
- relaxing trust policy;
- widening subordinate scopes.

Emergency recovery should later create a new explicit root-transition record.

## 14. Root conflict

If two competing roots both claim current status:

Potential disposition:
`GOVERNANCE_ROOT_CONFLICTING`.

Do not:
- union authorizers;
- choose the more permissive root;
- use whichever root validates the desired transition.

Affected trust mutation should fail closed until external governance reconciliation occurs.

## 15. Root availability failure

If current root cannot be established:
- historical evidence verification may continue where independently safe;
- new subordinate trust-state transitions should block;
- evidence acceptance may continue only where current trust state does not require root re-evaluation and policy explicitly permits it;
- do not infer a root from ambient configuration.

## 16. Ambient configuration is not root authority

Files, environment variables, database rows, or UI settings that resemble root configuration are not automatically authoritative.

The current root must be tied to the protected root subject.

Untracked ambient changes should produce:
`GOVERNANCE_ROOT_CONFIGURATION_DIVERGENCE`.

## 17. Root lineage

A valid current root should have either:

- an initial externally established bootstrap record; or
- an authorized root-transition lineage from such a bootstrap.

A higher generation with no valid lineage is not current merely because it is newer.

## 18. Cross-environment scope

Development/test/simulation root authority must not automatically transfer to:
- production;
- another customer;
- another deployment;
- independent safety governance.

Root scope is explicit.

## 19. Safety governance

Independent safety governance may have its own root anchor.

Ordinary ABIL governance root must not silently subsume safety governance.

If a future project explicitly unifies them, that would require separate protected authority and safety engineering.

## 20. Root trust and evidence trust

Relationship:

- root governance says who may authorize subordinate trust transitions;
- trust-state transition authorization says whether T(n)->T(n+1) is legitimate;
- trust-state currentness says which T is current;
- producer authenticity says whether evidence came from the claimed producer;
- evidence-ledger integrity says whether evidence history is complete/intact.

No layer substitutes for another.

## 21. Root read receipt concept

A future `GovernanceRootReadReceipt` could bind:

- root subject ID;
- generation;
- digest;
- scope;
- governance-policy profile;
- authorizer-set/profile digest;
- predecessor identity;
- effective time;
- read/evaluation time;
- currentness disposition;
- verifier identity;
- immutable receipt digest.

Research shape only.

## 22. Root transition receipt concept

A future `GovernanceRootTransitionReceipt` could bind:

- prior root;
- successor root;
- transition class;
- external authority evidence reference;
- approvals/signoffs;
- exact changed fields;
- scope;
- currentness;
- conflict/supersession status;
- immutable receipt digest.

Research shape only.

## 23. Hostile research cases

A future implementation should reject/fail closed on at least:

1. new root validates its own creation;
2. subordinate trust admin installs itself as root;
3. learner/candidate emits root record;
4. restored old root revives compromised admin;
5. two roots are unioned;
6. more permissive root is selected because it validates desired transition;
7. test-environment root used in production;
8. ordinary ABIL root used as safety-governance root;
9. root config changed in database with no protected root-transition record;
10. higher root generation has no authorized lineage;
11. current root unavailable causes fallback to stale local config;
12. historical root authorizes new transition;
13. emergency freeze path adds new root;
14. root-transition evidence is deleted from history;
15. root transition has valid signatures but wrong scope;
16. root generation matches but digest differs;
17. subordinate transition policy rewrites root-transition policy;
18. root transition occurs without exact external authority;
19. bootstrap root exists without immutable provenance;
20. failover node uses stale root while primary used newer root.

## 24. Relationship to PR #22

PR #22 asks:

> Is the trust-state transition authorized under the governance policy?

This research asks:

> What externally anchors that governance policy so the authorization chain terminates rather than recurses?

The answer is an explicit protected governance root/bootstrap boundary.

## 25. Evidence ceiling

This research does not:
- create or change governance roots;
- provision credentials;
- select cryptographic providers/algorithms;
- assign real administrators;
- modify trust policy;
- authorize safety governance;
- authorize implementation;
- authorize machine writes.

It defines where ABIL's self-verification ends and external protected governance begins.

## 26. Research disposition

The practical rule is:

> The trust chain terminates at an externally established protected governance root; ABIL may verify that root, but cannot self-create or self-justify it.

No governance-root implementation, root transition, credential/provider mutation, trust-root provisioning, verifier mutation, machine access/write, commissioning, deployment, promotion, merge/canonical promotion, or other protected effect is authorized by this research.
