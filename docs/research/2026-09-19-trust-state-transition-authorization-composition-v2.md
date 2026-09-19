# Trust-State Transition Authorization Composition V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #22 predecessor exact head `b9fbe482e37811053c1f3b1f0faf628ad4b5b188`.

This companion reconciles PR #22 with:
- PR #21 successor trust-currentness research at `abeaf69774eefe96701e7db73cd54e24dc5294b6` (exact witnessed-head equality + distinct witness-commit authority);
- PR #23 governance-root/bootstrap research;
- PR #24 time-source currentness research.

It preserves PR #22 V1 as historical/source provenance and tightens only the composition seams below.

## 1. Transition authorization and transition currentness are different predicates

A transition may be correctly authorized yet not become current.

A future transition evaluation therefore separates:

- `TRANSITION_AUTHORIZATION_VALID`
- `TRANSITION_COMMIT_CURRENT`

Authorization answers whether the exact proposed T(n)->T(n+1) change was permitted.

Commit-currentness answers whether that exact authorized successor became the uniquely committed current trust-state head.

Neither implies the other.

## 2. Exact predecessor must be the protected witnessed head

The transition subject MUST bind:
- exact predecessor trust-state node digest;
- predecessor generation;
- exact predecessor protected-head-witness digest;
- trust domain and scope;
- currentness/read-cut receipt.

A transition cannot be authorized against "whatever state is currently local."

Before transition application, the evaluator MUST prove that the predecessor is the exact current witnessed head for the affected scope.

If the protected witness has advanced, the proposal is stale even when its predecessor remains historically valid.

Disposition:
`TRANSITION_PARENT_SUPERSEDED`.

## 3. Governance policy must resolve from the current external root chain

The authorization policy that decides whether a transition is permitted MUST bind:
- exact `GovernanceRootAnchor` subject;
- exact root generation/digest;
- exact current root-head witness or equivalent protected external currentness subject;
- exact subordinate transition-policy profile digest;
- exact scope;
- exact authorizer-set/profile digest.

The proposed successor trust state cannot select or relax the governance policy that validates its creation.

A local configuration file, database row, environment variable, or successor payload is not sufficient governance authority.

## 4. TransitionAuthorizationReceipt

A stronger future receipt should bind at least:

- transition subject digest;
- predecessor trust-state node/generation;
- predecessor head-witness digest;
- proposed successor node digest/generation;
- transition class;
- exact changed trust predicates/material;
- scope;
- governance-root subject/generation/digest;
- governance-root currentness/witness receipt;
- transition-policy profile digest;
- proposer identity;
- required authorizer roles/quorum;
- actual approval identities and approval-evidence digests;
- approval/currentness result;
- time-source/cut reference where temporal policy is material;
- authorization result;
- verifier identity/profile;
- immutable receipt digest.

The receipt is evidence of authorization. It is not itself proof that the successor became current.

## 5. Commit step and protected witness advancement

After authorization, the successor node enters a pending state until the protected trust-state head witness advances coherently to that exact successor under the separately authorized witness-commit policy.

Conceptual sequence:

1. resolve current governance root;
2. resolve current predecessor trust-state witness;
3. verify transition authorization;
4. construct/verify exact successor trust-state node;
5. prove no conflicting commit has won since the predecessor cut;
6. advance protected trust-state head witness by an authorized compare-and-commit mechanism;
7. issue currentness receipt for the successor.

If step 6 fails, the successor remains:
`TRANSITION_AUTHORIZED_NOT_COMMITTED`.

It MUST NOT accept new protected producer evidence as current.

## 6. Concurrent authorized transitions

If TxA and TxB are both authorized from the same exact predecessor:

- authorization of both may remain historically true;
- only a uniquely committed successor may become current under the protected witness;
- a losing transition is not silently rebased;
- a second successor with the same predecessor creates conflict/pending reconciliation unless a new authorized composition transition is created.

Do not auto-union, pick by generation, pick by timestamp, or pick the more permissive result.

## 7. Commutative changes still require a new authorized subject

Even when two transitions appear mathematically commutative, a merged successor MUST be a separately identified transition subject whose:
- exact predecessor/current cut;
- combined change set;
- governance policy;
- approvals;
- successor digest;
- witness advancement

are independently validated.

"Would have produced the same set" is not sufficient currentness provenance.

## 8. Approval freshness and time are subordinate to structural authority

If policy says an approval expires or a transition has a scheduled effective time, PR #24-style time evidence MAY narrow whether the transition is usable.

Time MUST NOT establish:
- governance-root authority;
- predecessor currentness;
- authorizer identity;
- trust-state lineage;
- protected-witness currentness.

These structural predicates are established independently first.

A convenient wall-clock value cannot repair a stale predecessor or unauthorized authorizer.

## 9. Temporal uncertainty fails closed at policy boundaries

When approval freshness or effective-time activation is material, bind:
- exact time-source subject;
- source/session generation;
- time-read receipt;
- uncertainty bound;
- comparison semantics.

If the uncertainty interval crosses a required freshness/activation boundary, the transition cannot claim precise temporal admissibility.

The operation-specific policy may:
- reject;
- defer;
- downgrade to pending.

It may not choose the time value that makes the transition valid.

## 10. Root transition and subordinate transition remain separate

PR #23 governs the external/root layer.

A subordinate trust-state transition cannot:
- mutate the governance root;
- advance the root witness;
- redefine root-transition authority;
- use subordinate approval to bootstrap a new governance root.

If a single organizational event changes both root and subordinate trust, it requires distinct protected subjects and a coherent externally authorized cut linking them.

## 11. Historical transition verification

Historical verification may prove:
- proposal authenticity;
- approvals were valid under the historical root/policy;
- transition authorization was valid;
- whether the transition was ever committed current.

Historical truth is append-only.

A historically authorized but never committed transition MUST remain distinguishable from one that became current.

A historically committed transition MUST not become current again merely because old state is restored.

## 12. Transition replay rejection

Replay checks bind both:
- predecessor node identity/generation;
- predecessor protected-head-witness subject.

Even if the same predecessor bytes are restored, the current witness may prove the system has advanced beyond them.

Therefore restoring T20 does not make an old T20->T21 authorization replayable after T22 was committed.

## 13. Authorizer currentness

An approval is admissible only if the authorizer's governance authority is valid for:
- exact role;
- exact scope;
- exact transition class;
- required temporal/currentness profile.

A historical approval from an authorizer later revoked may still prove historical authorization if valid under the historical cut.

It cannot authorize a new current transition after revocation.

## 14. Emergency path

Emergency revoke/freeze may use a distinct protected policy, but the policy itself MUST be rooted in the current governance root.

Emergency authority MAY:
- narrow trust;
- revoke/freeze within exact scope;
- block new acceptance.

It MUST NOT automatically:
- add producers;
- add roots;
- relax verifier policy;
- widen scope;
- replace the governance root.

An emergency transition still requires protected witness advancement to become current.

## 15. Cross-scope transition cuts

A transition that changes multiple trust scopes binds either:

### atomic multi-scope commit
one authorized cut and coherent witness advancement for all affected scopes;

or

### explicit partial-order commit
a policy specifying:
- which scope may commit first;
- admissible intermediate combinations;
- which protected operations are blocked during partial advancement;
- final combination receipt.

Individually authorized transitions do not prove that an arbitrary combination of their successor states is admissible.

## 16. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. authorization valid but trust-head witness never advances; successor MUST remain non-current.
2. proposal binds local T20 while protected witness already records T21; reject stale parent.
3. successor payload supplies the policy that validates itself; reject.
4. local config supplies an authorizer absent from current GovernanceRootAnchor; reject.
5. two authorized successors race from T20; do not auto-union or select by timestamp/generation.
6. losing successor is replayed after winner committed; reject parent/witness mismatch.
7. approval expiry falls inside time uncertainty interval; no precise PASS.
8. wall clock is rolled backward to revive expired approval; structural witness/currentness still rejects.
9. emergency revoker attempts to add producer/root; reject scope/class.
10. historical authorized-but-uncommitted transition is restored; remain historical/pending, not current.
11. subordinate transition attempts governance-root mutation; reject domain boundary.
12. multi-scope transition partially commits under an atomic policy; combined currentness fails.

## 17. Practical composition rule

The stronger composed rule is:

> A trust-state successor is current only when the exact transition is authorized under the independently current governance root, applies to the exact current witnessed predecessor, and the separately protected trust-state head witness commits that exact successor.

Authorization, node creation, and current commit are three distinct evidence stages.

## 18. Authority boundary

This document does not:
- approve a real transition;
- provision credentials;
- add/remove roots;
- mutate verifier policy;
- create a live governance/witness service;
- authorize safety governance;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
