# Trust-State Exact Witness Equality and Commit Authority V3

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #21 predecessor exact head `2b4d5da33d9ce7dfe4d13c44a07bcd2f1c469120`.

This companion responds to Thirteen's exact-head hostile review of the predecessor.

The predecessor substantially closed:
- local-generation rollback;
- stale restore/failover;
- fork handling;
- transition-authorization separation;
- root/currentness separation;
- multi-scope/currentness/time semantics.

Two corrections remain:

1. protected currentness must require exact witnessed-head equality, not generic "admissible descendant/equivalent";
2. advancing the protected witness requires its own explicit commit authority/receipt distinct from node-transition authorization.

## 1. Exact currentness equality

For protected new-evidence acceptance:

`CURRENT(scope) := candidate_node_digest == resolved_ProtectedHead(scope).node_digest`

plus all required integrity, authorization, scope, conflict and temporal predicates.

A valid authorized descendant that is not yet the exact protected witnessed head is:

`TRUST_STATE_PENDING_NOT_CURRENT`.

It MUST NOT:
- accept new protected producer evidence as current;
- satisfy current trust-state dependency;
- be used as a current trust cut merely because lineage is valid.

## 2. Remove generic descendant/equivalent currentness

The predecessor phrase:

> exact witnessed head or an explicitly admissible descendant/equivalent under the bound profile

is superseded for protected currentness.

Generic descendant/equivalent status is insufficient.

Lineage validity may establish:
- candidate legitimacy;
- recovery path;
- historical relationship;
- eligibility for commit.

It is not an alternate currentness path.

## 3. Equivalence/alias is current only when itself protected-committed

If a system needs equivalent/alias node identities, equivalence must be represented by an explicit protected subject:

`TrustStateWitnessEquivalenceRecord`

or equivalent.

It binds:
- exact protected head witness digest;
- canonical current node digest;
- alias/equivalent node digest;
- equivalence class/profile;
- proof/evidence;
- exact scope;
- authorization;
- commit authority;
- immutable digest.

The protected witness mechanism itself must commit that equivalence.

An application-local profile cannot declare a locally visible descendant "equivalent enough" to bypass witness advancement.

## 4. Node transition authority and witness commit authority are distinct

Separate powers:

### TrustStateTransitionAuthorization
Answers:
> Is this proposed T(n)->T(n+1) semantic change authorized?

### TrustStateWitnessCommitAuthorization
Answers:
> Is this exact successor allowed to become the protected current head now?

A principal may hold one power without the other.

Compromise of transition authorizer MUST NOT automatically grant witness-commit authority.

## 5. TrustStateWitnessCommitAuthorizationReceipt

Every protected witness advancement SHOULD bind a receipt or mechanically equivalent protected commit subject containing at least:

- trust-domain ID;
- exact scope;
- predecessor witness digest;
- predecessor witness sequence/generation;
- exact predecessor node digest;
- successor node digest;
- successor node generation;
- TrustStateTransitionAuthorizationReceipt digest;
- commit authority identity/profile;
- required commit roles/quorum;
- actual commit approvals/attestations;
- conflict/fork check result;
- current governance-root cut;
- time/effective policy cut where material;
- compare-and-commit result;
- resulting witness digest/sequence;
- immutable receipt digest.

The receipt cannot create the commit authority it claims.

## 6. Commit authority is separately rooted

Witness-commit authority must derive from:
- current GovernanceRootAnchor/currentness;
- explicitly delegated witness-commit policy;
- exact trust-domain/scope.

It MUST NOT be inferred solely from:
- successor trust-state payload;
- transition authorizer identity;
- local administrator role;
- local possession of witness storage;
- candidate node generation.

## 7. Compare-and-commit semantics

Witness advancement should conceptually require:

1. resolve exact current GovernanceRootHeadWitness;
2. resolve exact current TrustStateHeadWitness;
3. verify transition authorization against that predecessor;
4. verify exact successor node;
5. verify commit authority/quorum;
6. prove no conflicting witness advancement already won;
7. compare predecessor witness digest/sequence atomically or coherently;
8. commit new witness binding exact successor;
9. read back exact witness;
10. issue currentness receipt.

If the predecessor witness changed before step 8:
- commit fails;
- successor remains pending/historical candidate;
- no currentness inferred.

## 8. Authorized-but-uncommitted state

Explicit disposition:

`TRUST_STATE_AUTHORIZED_NOT_COMMITTED`

This state may mean:
- transition authorization passed;
- successor node is valid;
- commit attempt has not happened or did not succeed.

It is not:
- current;
- eligible for current producer acceptance;
- a fallback if witness service is unavailable.

## 9. Commit conflict

If two valid authorized successors attempt to advance the same predecessor witness:

- both authorizations may remain historically valid;
- at most one exact successor may become the current witnessed head under the commit policy;
- losing candidate becomes superseded/pending/conflicting as policy defines;
- no automatic union or timestamp/generation winner.

If commit state cannot establish one unique current result:
`TRUST_STATE_CONFLICTING`.

## 10. Multi-scope commit authority

For atomic multi-scope transition:
- commit receipt binds all predecessor witnesses;
- all exact successors;
- one coherent commit/cut identity;
- required cross-scope commit authority/quorum;
- resulting witnesses.

Partial commit under an atomic profile does not produce current combined state.

For independent-cut policy:
- each scope has its own exact witness commit;
- admissible intermediate combinations are explicitly defined;
- a later combination receipt binds the exact witnessed heads.

## 11. Restore/failover read path

On restore/failover:

1. local trust store loads as candidate/historical data;
2. current TrustStateHeadWitness resolves independently;
3. candidate currentness requires exact digest equality to the witnessed node;
4. missing newer node is fetched/reconciled if permitted;
5. authorized-but-uncommitted local descendants remain non-current;
6. current producer acceptance remains blocked until exact equality is established.

No descendant shortcut is permitted.

## 12. Currentness receipt

A future `EvidenceTrustStateReadReceipt` for current acceptance MUST bind:

- exact candidate node digest;
- exact TrustStateHeadWitness digest;
- equality result;
- trust-domain/scope;
- transition authorization result;
- witness commit authorization receipt;
- fork/conflict result;
- governance-root cut;
- temporal result where required;
- resolver identity/profile;
- final currentness disposition;
- immutable receipt digest.

If equality fails:
the receipt cannot say CURRENT.

## 13. Witness alias migration

If implementation migration changes storage representation while preserving logical trust state, do not use informal equivalence.

Use a protected migration/equivalence subject that:
- binds old exact witnessed node;
- binds new representation;
- proves semantic equivalence under an exact profile;
- has explicit authorization;
- is committed by the witness mechanism.

Only after that protected commit may the new representation serve as current.

## 14. Historical validity

A node may be:
- historically valid;
- transition-authorized;
- never committed current.

Preserve that distinction.

Historical audit should be able to answer:
- proposed?
- authorized?
- committed?
- superseded?
- current at what cut?

Do not rewrite authorized-but-uncommitted candidates as if they never existed.

## 15. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. witness at T20; local authorized T21 exists but witness not advanced -> T21 is NOT current.
2. profile says T21 is "equivalent descendant" but no protected equivalence record -> reject currentness.
3. protected equivalence record commits exact alias -> alias may be current under that exact record.
4. transition authorizer also tries to advance witness but lacks commit authority -> reject commit.
5. witness storage admin advances head without valid transition/commit receipts -> reject currentness.
6. two authorized successors race; exact compare-and-commit permits one unique winner only.
7. predecessor witness changed before commit; stale commit attempt fails.
8. valid successor node with higher generation but commit service unavailable -> pending, not current.
9. restore contains T21 but external witness says T20 because T21 was never committed -> T20 remains current.
10. restore contains T20 but witness says T21 -> T20 historical/stale.
11. atomic multi-scope transition commits only one scope -> combined currentness fails.
12. local app creates alias mapping between T20/T21 -> no currentness without protected alias commit.
13. transition authorization valid under current root but witness-commit authority is revoked -> commit fails.
14. currentness receipt omits witness-commit receipt/equality result -> insufficient.
15. same witness sequence appears with different node digest -> conflict.

## 16. Practical rule

> For protected currentness, lineage does not substitute for commitment. The current trust state is the exact node uniquely committed by the separately protected witness, and advancing that witness requires authority distinct from authorizing the semantic transition itself.

## 17. Authority boundary

This document does not:
- create/advance a real witness;
- grant transition or commit authority;
- create/rotate/revoke credentials;
- mutate trust roots/provider state;
- implement trust-state currentness;
- authorize safety evidence;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
