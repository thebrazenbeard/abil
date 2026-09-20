# ABIL Research Integration / Claim Lattice V5 Rebind

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH INTEGRATION REBIND / NO IMPLEMENTATION OR MERGE AUTHORITY**

Date: 2026-09-19

Predecessor integration subject:
- PR #19 head: `ef017dba6d04da33275ead7d316d70782474a947`
- V4 rebind: `docs/research/2026-09-19-research-integration-claim-lattice-v4-rebind.md`

Purpose:

> Rebind the integration tuple after PR #15 closes the dispatch-fence TOCTOU gap with an explicit effect-admission linearization contract.

This file changes only the PR #15 exact binding and the interpretation of its final dispatch barrier. Every other V4 binding remains unchanged unless separately moved by a later exact rebind.

## Current exact bindings

- PR #4 component-evidence policy authority: `e60bc866ad6893214c14b7dd25e312752dc4c791`
- PR #14 replay-ledger currentness: `e9fb2751e75379ae901de5dcf539cc64cc2f109d`
- PR #15 dispatch protected/multi-head cut: `7e92fc4dcef6bf5e658ddf80119a8a26f02a5037`
- PR #17 reconciliation current-cut: `30cccddc0eb2ec476d97c3c6166cc71d2b31b7fb`
- PR #18 evidence-ledger currentness: `0c7a764486e7bb758915e8bbe767fc5ea6f9416a`
- PR #20 producer-chain authenticity: `dfb66be6b39ee66a270f1f29fd25de24790affb1`
- PR #21 trust-state currentness V3: `abeaf69774eefe96701e7db73cd54e24dc5294b6`
- PR #22 transition authorization: `a6377627f73fed5a396ea9606e02b17dbdd92392`
- PR #23 governance-root currentness: `705e0a9c2aa0143091761a2eb875213e1c24832e`
- PR #24 time-source currentness: `57039cecbc8aa8bbf41ae2bf56a037d50a03db5b`
- PR #25 shared ProtectedHeadWitness primitive: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`

## PR #15 successor binding

Artifact:
`docs/research/2026-09-19-dispatch-multi-head-operation-cut-binding-v3.md`

Successor blob:
`eb93199982c2b19e0271d2749e0c4f0df6536d4f`

The predecessor exact subject `c79a13b3d6995cfccfc2f6c80b89c7dca367e0a0` remains historical review provenance and carried the coordinator finding `DISPATCH_FENCE_TOCTOU_UNCLOSED`.

The successor requires an explicit effect-admission linearization point after final Model A/B cut verification and before physical effect can become possible.

Every operation profile must choose one of two semantics:

1. **SERIALIZED_INVALIDATION_FENCE**
   - admission commit is serialized against every required protected-head transition declared invalidating;
   - the exact operation cut, invalidation profile, effect intent, and admission generation/token are bound;
   - an invalidating transition cannot leave an older stale admission usable across the effect boundary.

2. **POINT_IN_TIME_COMMIT**
   - one exact admission commit is the currentness/authorization linearization point;
   - all required cut verification must complete before that commit;
   - protected-head movement after the commit is explicitly non-retroactive for the already-admitted effect;
   - every later attempt observes the newer heads;
   - silence never implies point-in-time semantics.

Therefore `successful final reread -> unconstrained send` is no longer a permitted interpretation.

## Integration effect

The integration lattice now distinguishes:

```text
protected-head unique currentness
        |
        v
coherent multi-head operation cut
        |
        v
final revalidation
        |
        v
explicit effect-admission linearization
        |
        v
effect-possible boundary
```

PR #25 establishes unique protected-head advancement semantics. It does not itself serialize an operation's effect admission against concurrent movements across several heads.

PR #15 now owns that missing operation-level semantic boundary.

## Review consequence

The prior coordinator TOCTOU finding is **SOURCE-OWNER REPAIRED / INDEPENDENT REREVIEW REQUIRED**.

No prior independent disposition transfers to:
- PR #15 head `7e92fc4dcef6bf5e658ddf80119a8a26f02a5037`; or
- this PR #19 successor head after publication.

One reconciliation remains blocked until the required independent exact-head review facets are fresh on the current tuple.

## Hard gate

Unchanged:

1. PR #3 exact-head independent peer review;
2. required exact-head peer facets on the current tuple;
3. One exact-tuple reconciliation;
4. if clean, STOP for Patrick's explicit final written-design acceptance;
5. implementation planning only after that authority.

## Authority boundary

This rebind grants no:
- implementation planning;
- merge/canonical promotion;
- machine connection/write;
- physical dispatch/effect;
- witness/provider deployment;
- commissioning;
- credential/root/provider/time-source mutation.

Patrick remains sole authority for protected effects.
