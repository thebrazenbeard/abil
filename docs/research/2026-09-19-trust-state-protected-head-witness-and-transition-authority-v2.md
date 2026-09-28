# ABIL Trust-State Protected Head Witness and Transition Authority V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #21 predecessor exact head `1e2d16913bd9014a38306c0a2d53314ad98491e2`.

This addendum responds to hostile review findings that:
- monotonic generation alone cannot establish currentness across restore/failover;
- a locally restored trust store cannot be its own anti-rollback witness;
- currentness-resolver provenance must be non-circular;
- effective-time semantics must not defeat lineage/currentness;
- multi-scope changes need coherent-cut semantics;
- generation advancement itself needs transition authority.

This remains research only. It does not create, rotate, revoke, provision, or install credentials/trust roots; choose a PKI/provider/algorithm; mutate verifier configuration; or authorize machine writes.

## 1. Immutable trust-state nodes

The preferred strong model is an append-only content-addressed trust-state lineage.

Each `EvidenceTrustStateNode` binds at least:
- trust-domain ID;
- exact scope;
- generation;
- predecessor node digest, except bootstrap;
- trust-state payload digest;
- accepted-current material-set digest;
- historical-only material-set digest;
- revocation-set digest;
- delegation-set digest;
- verifier-policy/profile digest;
- effective-time policy subject;
- transition-authorization receipt digest;
- node digest.

Trust-state nodes are immutable historical facts.

A node's existence does not by itself make it current.

## 2. Separately protected head witness

Currentness for protected new-evidence acceptance requires a separately protected anti-rollback subject:

`TrustStateHeadWitness`

or mechanically equivalent qualified commit record.

It binds at least:
- trust-domain ID;
- exact scope;
- current trust-state generation;
- current trust-state node digest;
- predecessor/lineage digest or lineage accumulator;
- witness generation/sequence;
- witness authority/profile identity;
- commit/verification evidence;
- effective/currentness semantics;
- immutable witness digest.

The witness rollback domain MUST be sufficiently independent from the trust store it judges that restoring the trust store cannot silently restore the witness to the same stale point.

A restored T17 trust store cannot become current if a qualified witness proves T20 is the unique current descendant.

## 3. Anti-rollback currentness predicate

For new protected evidence acceptance, trust state is current only if all required predicates hold:

- node integrity valid;
- scope matches;
- node generation/lineage valid;
- transition authorization valid;
- protected head witness resolves;
- node is the exact witnessed head or an explicitly admissible descendant/equivalent under the bound profile;
- no unresolved fork/conflict;
- effective-time policy permits current use;
- required verifier/currentness profile matches.

Local maximum generation is never sufficient currentness evidence.

## 4. Missing witness fails closed

If the protected head witness:
- is unavailable;
- is stale;
- is unverifiable;
- has unknown scope;
- cannot prove a unique current descendant;
- conflicts with another qualified witness;

then current producer acceptance for the affected protected scope fails closed or downgrades to an explicitly non-authoritative state.

Historical verification MAY continue under an explicitly historical profile where safe.

The system MUST NOT silently fall back to:
- local maximum generation;
- last-known permissive state;
- most recent wall-clock timestamp;
- state accepting the broadest key set;
- state available on the restored appliance.

## 5. Fork handling

Suppose T19 has two incompatible successors:
- T20A;
- T20B.

If both are validly formed descendants of T19 but no qualified commit/witness establishes one as the unique current branch, status is:

`TRUST_STATE_CONFLICTING`.

The system MUST NOT resolve the fork by:
- generation number;
- lexical digest order;
- local recency;
- wall-clock timestamp;
- permissiveness;
- producer preference;
- restored-node preference.

Current protected evidence acceptance remains blocked for the affected scope until the conflict is resolved by the authorized governance/commit mechanism.

## 6. Currentness resolver provenance

An `EvidenceTrustStateReadReceipt` or equivalent currentness receipt MUST bind:
- trust-state node digest;
- generation;
- trust-domain/scope;
- protected head witness digest;
- witness authority/profile;
- resolver identity;
- resolver profile/version;
- resolution procedure;
- lineage/fork result;
- effective-time/time-source result;
- final currentness disposition;
- receipt digest.

"Independent resolver" means authority/failure-domain separation sufficient to falsify rollback.

A separate process restored from the same stale backup domain is not automatically independent.

## 7. Trust-state transitions need explicit authority

Higher generation does not imply legitimate generation.

Every successor node after bootstrap requires a `TrustStateTransitionAuthorizationReceipt` or mechanically equivalent protected transition subject.

It binds at least:
- trust-domain ID;
- exact scope;
- predecessor node digest/generation;
- proposed successor payload digest;
- successor generation;
- transition class;
- transition reason;
- exact changed trust predicates/material;
- requested effective semantics;
- transition-authority identity/profile;
- required approvals/quorum roles;
- actual approval identities/receipts;
- emergency/ordinary classification;
- verification result;
- immutable receipt digest.

A successor lacking admissible transition authority is not current merely because its generation is larger.

## 8. Transition classes

At minimum distinguish:

- `BOOTSTRAP`;
- `ORDINARY_ROTATION`;
- `REVOCATION`;
- `DELEGATION_GRANT`;
- `DELEGATION_REVOCATION`;
- `VERIFIER_POLICY_HARDENING`;
- `ALGORITHM_PROFILE_CHANGE`;
- `EMERGENCY_REVOCATION`;
- `INCIDENT_CONTAINMENT`;
- `SCOPE_RESTRUCTURE`.

Each class may require a different approval/authority profile.

Emergency revocation MAY have a narrower/faster authority path than ordinary trust expansion, but that path must be explicitly governed. "Emergency" is not a generic bypass.

## 9. Authority cannot self-bootstrap through evidence trust

Evidence-trust state cannot define its own authority to create a successor unless that authority is rooted in a separately governed authorization subject.

Examples of prohibited circularity:
- T20 payload says signer K is authorized, and K signs T20, with no prior authority root;
- restored trust store says its local admin is transition authority, and that local admin declares the restored state current;
- a new verifier profile validates the transition that installs that same verifier profile with no independently rooted authorization.

Transition authority must be derivable from an authority root/governance subject whose validity is not created solely by the successor trust state being authorized.

## 10. Scope-bound transition authority

Transition authority is scope-bound.

Authority to rotate trust for Deployment A does not imply authority for:
- Deployment B;
- organization-global roots;
- safety evidence trust;
- unrelated evidence classes;
- provider-wide verifier policy.

The transition authorization receipt binds exact scope and rejects scope widening beyond the authority grant.

## 11. Quorum and multi-role approval

Some transition classes SHOULD require multiple independently rooted roles.

Examples:
- global root replacement;
- safety-evidence trust change;
- verifier-policy weakening;
- algorithm-profile expansion;
- trust-domain merge/split.

The research does not prescribe a fixed quorum.

The policy must bind:
- required roles;
- cardinality/quorum;
- independence constraints;
- approval expiry/currentness;
- conflict-of-interest rules where applicable.

A single signer cannot satisfy multiple required independent roles merely by carrying multiple labels unless the policy explicitly permits it.

## 12. Protected head witness advancement

A transition is not fully current for protected acceptance merely because the successor node was authored.

The protected head witness must advance to bind the authorized successor.

Conceptually:

1. validate predecessor/current witness;
2. validate transition authorization;
3. validate successor node;
4. establish no conflicting successor under the commit policy;
5. atomically or coherently advance the protected witness;
6. issue currentness receipt.

If witness advancement fails after node creation, the node may exist historically/pending but is not current.

## 13. Witness anti-rollback properties

The witness mechanism itself needs a qualification profile.

It SHOULD provide enough evidence to reject:
- restoring an older witness snapshot;
- deleting a later witnessed head;
- same-sequence conflicting witness values;
- unauthorized witness advancement;
- scope substitution;
- local self-currentness after network partition;
- unproven failover to a stale witness replica.

The exact implementation could be:
- monotonic hardware-backed state;
- separately protected append-only service;
- quorum/consensus commit log;
- another independently qualified anti-rollback mechanism.

This research intentionally does not choose one.

## 14. Multi-scope trust-state advancement

A trust change may affect multiple scopes.

Two valid models are permitted.

### 14.1 Atomic parent cut

A `TrustStateMultiScopeCut` binds:
- all affected scope IDs;
- exact predecessor node/witness for each;
- exact successor node for each;
- one transition-authorization subject;
- one commit/cut identity;
- final per-scope witness updates;
- cut digest.

Currentness requires the whole declared cut to commit coherently.

### 14.2 Explicit independent-cut semantics

If scopes advance independently, the policy MUST define:
- which combinations are admissible during partial advancement;
- ordering/dependency edges between scope changes;
- which scopes block protected evidence acceptance until peers advance;
- reconciliation behavior;
- exact combination receipt.

A set of individually current scope nodes is not automatically a valid combined trust state if the combination never formed an authorized coherent cut.

## 15. Cross-scope combination receipt

When a verification decision depends on multiple trust scopes, bind a `TrustStateCombinationReceipt` that records:
- every scope;
- each current node/witness digest;
- cross-scope dependency policy;
- admissibility result;
- unresolved partial advancement/conflict;
- combination digest.

This prevents verifier decisions from silently mixing mutually incompatible but individually valid scoped states.

## 16. Effective time is subordinate to lineage/currentness

Generation/lineage plus protected witness order is the primary anti-rollback signal.

Wall-clock/effective-time data may:
- delay activation;
- expire a grace window;
- constrain historical applicability;
- annotate compromise intervals.

Time MUST NOT:
- revive a superseded/revoked node;
- make an unwitnessed fork current;
- turn a stale local maximum into current state;
- widen acceptance under uncertainty.

## 17. Qualified time authority

When time affects an acceptance decision, the receipt binds:
- time-source identity;
- time-source qualification/profile;
- observed time;
- uncertainty bound;
- monotonic/rollback evidence where applicable;
- effective-window interpretation.

If qualified time is unavailable or uncertainty crosses a policy boundary, the result fails closed or narrows.

Clock uncertainty never silently widens producer acceptance.

## 18. Historical replay versus current acceptance

Historical verification explicitly binds:
- historical trust-state node;
- historical witness/cut evidence if retained;
- historical effective-time semantics;
- historical verifier profile;
- `HISTORICAL_VERIFICATION_ONLY` disposition.

Historical replay may reproduce a prior verification result.

It MUST NOT:
- reactivate historical producer eligibility;
- update the protected current head;
- treat old grace windows as currently active;
- override later revocation/supersession.

## 19. Restore procedure

A future restore flow should conceptually:

1. load restored trust-state bytes as untrusted candidate state;
2. resolve protected head witness independently;
3. reconstruct/validate lineage from candidate/restored nodes to the witnessed head;
4. fetch/reconcile missing newer nodes as permitted;
5. detect forks/conflicts;
6. validate transition authorizations;
7. validate effective-time/currentness policy;
8. only then allow current protected evidence acceptance.

A backup's embedded generation/digest is evidence about backup contents, not authority that those contents are current.

## 20. Failover procedure

A standby MAY become operational only after reconciling to the qualified head witness/currentness cut for every required scope.

A stale standby that cannot prove reconciliation:
- may support bounded historical verification where safe;
- MUST NOT accept new protected evidence as if current.

Failover availability does not outrank currentness.

## 21. Currentness receipt cannot self-authorize

A currentness receipt signed by a resolver is admissible only if:
- resolver authority/profile is independently rooted;
- witness evidence is bound;
- trust-state node/lineage is bound;
- scope is exact;
- resolver is not merely reporting its own restored local state.

A receipt that says `CURRENT` without the protected witness/provenance evidence is an assertion, not anti-rollback proof.

## 22. Relationship to authority-state anti-rollback

Execution/write authority and evidence-trust currentness remain separate state axes.

A current authority epoch does not prove current trust state.

A current trust witness does not grant machine/write authority.

Both may appear in a higher-level operational cut, but neither may be inferred from the other.

## 23. Relationship to safety evidence

Safety-evidence trust may use a distinct stronger witness/transition-authority profile.

Ordinary evidence-trust governance cannot:
- install a safety trust root;
- widen safety verification policy;
- override a safety trust conflict;
- treat ordinary trust currentness as safety authority.

## 24. Hostile acceptance cases

Future trust-state implementation/qualification SHOULD include at least:

1. restore T17 while protected witness proves T20; current acceptance MUST reject T17.
2. restore both trust store and stale local resolver from same backup; absence of independent witness MUST fail currentness.
3. create T20A and T20B from T19; no unique witnessed successor => `TRUST_STATE_CONFLICTING`.
4. give T21 a larger generation but invalid transition authority; it MUST NOT become current.
5. let successor payload self-declare its own transition signer authority; MUST fail circular-authority check.
6. ordinary rotation signed only by an emergency-revocation authority where policy does not permit it; MUST fail.
7. emergency revocation follows explicitly authorized emergency path; MAY advance if all emergency predicates pass.
8. valid node creation occurs but witness advancement fails; node remains pending/historical, not current.
9. restore old witness snapshot while newer witness commit exists; witness rollback MUST be detected.
10. Deployment A transition authority attempts Deployment B change; scope check MUST fail.
11. multi-scope policy requires atomic cut but only one scope advances; combined currentness MUST fail.
12. independent-cut policy permits temporary partial state under exact restrictions; only permitted operations MAY continue.
13. wall clock is moved backward into an old grace window after witness has advanced beyond old state; old trust MUST remain non-current.
14. time uncertainty spans an expiry/revocation boundary; current acceptance MUST fail closed/narrow.
15. historical replay of pre-revocation evidence reproduces historical result but cannot accept a new producer record.
16. current authority A12 remains valid while trust witness detects restored T17 < T20; trust acceptance MUST fail independently.

## 25. Research disposition

The stronger practical rule is:

> Current evidence-acceptance trust is not "the highest generation visible locally." It is the uniquely authorized trust-state lineage committed by a separately protected anti-rollback witness for the exact scope, with admissible transition authority and coherent currentness/time semantics.

Historical trust may remain readable for verification, but it cannot become current by restore, failover, timestamp manipulation, local generation ordering, or self-issued currentness receipts.

## 26. Authority boundary

This document does not:
- create/rotate/revoke credentials;
- install trust roots;
- create a PKI;
- select a provider or cryptographic algorithm;
- change verifier configuration;
- create a live witness service;
- mutate a trust store;
- authorize safety evidence;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
