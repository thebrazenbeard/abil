# Governance Root Protected Currentness Witness V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #23 predecessor exact head `590f472114aeb665ceb1086439e79cd2e2725b8d`.

This companion closes the anti-rollback recursion exposed after PR #21 was strengthened with a separately protected trust-state head witness.

PR #23 V1 correctly terminates *authorization* recursion at an externally established `GovernanceRootAnchor`.

That is necessary but not sufficient for *currentness*.

A restored host can possess an authentic historical root and still be unable to prove that it is the current root.

This companion therefore adds an explicit protected currentness witness for the governance-root layer.

## 1. Root identity and root currentness are separate

An authentic `GovernanceRootAnchor` answers:

> What exact root subject is this?

It does not by itself answer:

> Is this exact root the current root for this exact scope now?

Root currentness therefore requires a separately protected subject.

## 2. GovernanceRootHeadWitness

Conceptual subject:

`GovernanceRootHeadWitness`

It binds at least:
- governance-root domain ID;
- exact scope/environment;
- current root generation;
- current root subject digest;
- predecessor/root-lineage digest or accumulator;
- witness sequence/generation;
- witness authority/profile;
- external commit/verification evidence;
- root-transition receipt digest when non-bootstrap;
- currentness/effective semantics;
- immutable witness digest.

The witness rollback domain MUST be sufficiently independent from ordinary ABIL/local root storage that restoring that storage cannot silently restore the witness to the same stale point.

## 3. Bootstrap binds both root and witness

Initial bootstrap is not complete merely because root bytes exist.

The external protected bootstrap procedure must establish:
- exact initial GovernanceRootAnchor;
- exact initial GovernanceRootHeadWitness;
- exact scope;
- immutable bootstrap provenance;
- external authority evidence;
- any required custody/quorum evidence.

ABIL may verify the resulting subjects.

ABIL cannot self-create their authority.

## 4. Root anti-rollback predicate

A root is current for subordinate trust-transition authorization only if:

- root subject integrity is valid;
- exact scope/environment matches;
- root lineage is valid;
- root transition authorization is valid for non-bootstrap roots;
- protected root-head witness resolves;
- root is the exact uniquely witnessed head;
- no unresolved root fork/conflict exists;
- required currentness/time policy is satisfied;
- resolver/witness profile is valid.

Local maximum root generation is never sufficient.

## 5. Restored historical root cannot self-current

Hostile restore:

1. G3 removed compromised administrator A;
2. a backup contains authentic G1 with A;
3. host restores G1;
4. local files/configuration all agree with G1.

If the protected external witness proves G3 current, G1 is:
`GOVERNANCE_ROOT_HISTORICAL`
or
`GOVERNANCE_ROOT_ROLLBACK_DETECTED`,
not current.

If the witness cannot be resolved, current subordinate trust mutation fails closed rather than choosing local G1.

## 6. Missing or conflicting root witness

If the witness is:
- unavailable;
- unverifiable;
- stale;
- scope-mismatched;
- forked;
- conflicting with another qualified witness;

then current root status is not established.

At minimum:
`GOVERNANCE_ROOT_CURRENTNESS_UNRESOLVED`.

New subordinate trust-state transitions MUST block for the affected scope.

Historical verification MAY continue only under an explicitly historical profile.

## 7. Same-generation different-root conflict

Two root subjects with:
- same domain;
- same scope;
- same generation;
- different digest/content

are not resolved by generation equality.

Without a qualified external resolution/commit record:
`GOVERNANCE_ROOT_CONFLICTING`.

Do not:
- union authorizers;
- choose the more permissive root;
- choose local root;
- choose newer wall-clock timestamp;
- choose whichever root validates a desired action.

## 8. Root transition authorization

A non-bootstrap root successor requires a separately protected `GovernanceRootTransitionAuthorizationReceipt` or equivalent external authority subject.

It binds at least:
- exact predecessor root + predecessor witness;
- exact proposed successor root;
- root-transition class;
- exact changed governance predicates;
- scope;
- exact external authority evidence;
- required approvals/quorum;
- actual approvals;
- emergency/ordinary class;
- effective-time policy;
- verification result;
- immutable receipt digest.

A new root cannot authorize the transition that creates itself.

## 9. Root node creation versus root commit

Creating a successor root subject does not make it current.

Conceptual sequence:

1. resolve current root + root witness;
2. validate external root-transition authority;
3. create/verify successor root subject;
4. establish no competing committed successor;
5. advance GovernanceRootHeadWitness coherently;
6. issue current-root read/currentness receipt.

If witness advancement fails:
`GOVERNANCE_ROOT_AUTHORIZED_NOT_COMMITTED`.

Subordinate trust transitions continue to use the previously committed root or fail closed according to policy.

## 10. Root fork handling

If G3 has two externally well-formed successors G4A and G4B and no protected commit establishes a unique head, both may remain historical candidate evidence but neither is silently selected as current.

Disposition:
`GOVERNANCE_ROOT_CONFLICTING`.

External governance reconciliation must produce:
- exact resolution;
- exact surviving/new root subject;
- exact transition provenance;
- exact witness advancement.

## 11. Root witness authority cannot be the root it witnesses

To avoid circularity, the currentness authority for `GovernanceRootHeadWitness` cannot be established solely by the same mutable governance root being witnessed.

The external protection mechanism may be:
- a separately governed append-only service;
- hardware/organizational monotonic state;
- externally controlled quorum/commit log;
- another independently qualified protected mechanism.

This research intentionally does not select one.

The key requirement is rollback/currentness separation, not a specific technology.

## 12. Root failover

A failover node with local root G2 may not authorize subordinate transitions until it reconciles against the protected root witness.

If witness proves G3:
- fetch/reconcile G3 as permitted;
- validate lineage/transition evidence;
- only then use G3.

Availability does not outrank governance currentness.

## 13. Ambient configuration divergence

If:
- local root subject says G3;
- environment/database/UI config authorizer set differs;
- protected witness still says G3;

the ambient configuration is not a new root.

Report:
`GOVERNANCE_ROOT_CONFIGURATION_DIVERGENCE`.

Protected root/witness subjects remain the reference.

## 14. Time is subordinate to root lineage/currentness

Effective-time evidence may:
- delay activation;
- expire temporary authority;
- annotate historical applicability.

Time cannot:
- make an unwitnessed root current;
- revive a superseded root;
- resolve a root fork;
- create external authority.

When time is material, bind the qualified time subject/receipt from the PR #24 model.

If time is unavailable but root currentness can be established structurally and the operation does not require temporal validity, policy may permit bounded operation.

Time is not a universal root-currentness prerequisite.

## 15. Root and trust-state witness separation

Do not collapse:
- `GovernanceRootHeadWitness`;
- `TrustStateHeadWitness`.

The root witness establishes current governance authority.

The trust-state witness establishes current producer/verifier acceptance state under that governance authority.

A current trust-state witness cannot repair a stale root witness.

A current root witness does not itself establish current trust-state content.

## 16. Safety-governance witness separation

If safety governance has an independent root, it needs its own separately protected currentness lineage/witness.

Ordinary ABIL governance-root currentness does not imply safety-governance currentness or authority.

## 17. Root currentness receipt

A future `GovernanceRootReadReceipt` should bind:
- root subject ID/digest;
- root generation;
- scope/environment;
- protected root-head-witness digest;
- root lineage result;
- root transition authorization result;
- conflict/fork result;
- time/currentness result where material;
- resolver identity/profile;
- final disposition;
- immutable receipt digest.

A field saying `CURRENT` without protected-witness evidence is only an assertion.

## 18. Historical verification

Historical root records remain valuable to verify:
- old transition approvals;
- old evidence authenticity decisions;
- incident chronology.

Historical verification MUST bind an explicit historical root cut.

It MUST NOT:
- update the current root witness;
- authorize new subordinate transitions;
- revive historical administrators;
- reopen historical grace windows as current.

## 19. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. restore authentic G1 while external root witness proves G3; G1 cannot become current.
2. restore both local root store and local resolver from G1 backup; absence of independent witness blocks current root claim.
3. G4A and G4B share G3 predecessor; no unique external commit => conflict.
4. same root generation with different digest => conflict.
5. new root signs/validates its own creation with no external authority => reject.
6. valid external transition subject exists but root witness never advances => successor not current.
7. stale failover node tries to authorize subordinate transition before witness reconciliation => reject.
8. ambient database authorizer differs from current root subject => configuration divergence.
9. wall clock rollback makes G1 effective interval appear active; protected witness still proves G3 => G1 remains historical.
10. current trust-state witness exists under stale root witness; subordinate mutation authority remains unresolved.
11. root witness is available but wrong environment/customer scope; reject.
12. ordinary governance root is substituted for safety-governance root; reject.

## 20. Practical rule

> The ultimate governance chain terminates at an externally established root **and** a separately protected external currentness witness for that root. Authentic historical root bytes are not sufficient to prove current governance after restore/failover.

## 21. Authority boundary

This document does not:
- create/change governance roots;
- create a live root-witness service;
- provision credentials;
- assign administrators;
- mutate trust policy;
- select cryptographic/provider mechanisms;
- authorize safety governance;
- authorize machine writes;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
