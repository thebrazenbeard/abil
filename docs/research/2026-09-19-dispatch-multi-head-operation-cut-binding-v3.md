# Dispatch Multi-Head Operation Cut Binding V3

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #15 predecessor exact head `78b62ccb5c3c6f669a50185c2080eb5cf607848b`.

Required shared semantic dependency:
- Draft PR #25 head: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`
- artifact: `docs/research/2026-09-19-protected-head-witness-semantic-primitive-v1.md`
- blob: `fa5a883551d92fd35b73f0ad6bd5456caf81ffd0`

This binding responds to Thirteen's exact-head transaction/evidence review.

Two corrections are made:
1. the replay-head barrier is qualified only when it satisfies PR #25 unique predecessor-bound advancement;
2. when a protected operation consumes both replay and evidence currentness, the operation profile MUST define one coherent multi-head cut rule. `SHOULD cross-bind` is superseded.

## 1. Qualified replay barrier

The dispatch barrier may rely on `ReplayLedgerHeadWitness` only if that witness satisfies the PR #25 `ProtectedHeadWitness` semantic primitive.

Therefore physical dispatch MUST NOT rely on witness advancement that:
- can fork during partition;
- allows two incompatible successors to receive CURRENT_COMMITTED;
- lacks predecessor-bound compare-and-advance/consensus semantics;
- lacks current commit authority;
- lacks exact readback.

If unique advancement cannot be established:
dispatch remains blocked.

## 2. Protected operation cut profile

Every protected operation class declares its required protected-head set.

Example:
- replay head;
- evidence head;
- trust head;
- authority/currentness head.

For any operation consuming more than one protected head, the profile MUST select exactly one model:

### Model A — aggregate protected operation cut

A `ProtectedOperationCutCommit` binds exact current head-witness digests for every required domain into one aggregate cut before dispatch.

### Model B — explicit independent-head ordering

The profile defines:
- exact read order;
- dependency/invalidation edges;
- which head movements invalidate earlier reads;
- required rereads/revalidation;
- final dispatch fence;
- exact MultiHeadOperationCutReceipt.

No implicit third model is allowed.

## 3. Replay + evidence coherence

If dispatch eligibility depends on both:
- replay currentness;
- evidence completeness/currentness;

then the operation profile MUST bind the exact replay and evidence protected-head witnesses.

It may not:
- read R20;
- later read E19;
- independently advance one axis;
- then claim the pair was a coherent current cut without the selected Model A/B proof.

A pair of individually current heads is not automatically an admissible operation cut.

## 4. Final dispatch fence

Immediately before the effect-possible boundary, the writer verifies the final operation cut.

For Model A:
- aggregate cut is current;
- all bound head digests still match.

For Model B:
- required final rereads/revalidation pass;
- invalidation rules show no disqualifying head movement;
- MultiHeadOperationCutReceipt is current.

Only then may physical effect become possible.

## 5. Head movement after reservation

A reservation may already be protected-committed in replay state.

If another required protected head moves after reservation but before send:

- apply the operation profile invalidation rule;
- if invalidating, do not send;
- preserve replay reservation;
- append cancellation/no-send/ambiguity evidence as supported;
- require fresh currentness/decision for later attempt.

Replay durability does not rescue stale evidence/trust/authority state.

## 6. Witness-authority movement

If the authority/root cut governing one required protected head becomes unresolved or changes in a way the profile marks invalidating:

- the corresponding head currentness cannot be assumed reusable;
- operation cut is invalidated;
- dispatch blocks pending re-resolution.

## 7. Cross-domain split brain

If:
- replay head is uniquely current in one partition;
- evidence head cannot establish unique currentness;
or vice versa:

the operation cut fails if the profile requires both.

Do not downgrade a required axis to "best available" for availability.

## 8. Operation cut receipt

A future `DispatchOperationCutReceipt` may specialize PR #25's `MultiHeadOperationCutReceipt` with:

- request ID;
- effect-intent digest;
- deployment/target/output scope;
- exact admission/currentness decision;
- replay-head witness digest;
- evidence-head witness digest when required;
- trust/authority head digests when required;
- read/commit order;
- invalidation policy;
- final revalidation result;
- reservation commit receipt;
- target dedup/prepare receipt where relied upon;
- final dispatch eligibility;
- immutable digest.

This receipt does not prove physical execution.

## 9. No optional cross-binding for required axes

The predecessor V2 phrase that replay reservation commit `SHOULD cross-bind` the evidence cut where completeness is required is superseded.

If the operation profile says evidence completeness is required, coherent binding is mandatory.

If the operation profile says it is not required, evidence head need not be invented into the dispatch cut.

Requirements are explicit, operation-specific, and fail closed.

## 10. Hostile checks

Future implementation/review SHOULD include:

1. replay and evidence witnesses both fork-capable; local success on each does not qualify dispatch.
2. replay R20 current, evidence E19 read, evidence advances E20 before send; profile says invalidating => block/revalidate.
3. aggregate cut binds R20/E19; E20 later becomes current; aggregate cut stale => no dispatch if freshness/currentness requires latest.
4. independent-order profile omits invalidation rule for evidence movement; profile invalid.
5. replay reservation committed but trust head revokes producer before send; operation cut invalidates.
6. evidence head unavailable while profile requires evidence completeness; availability does not permit replay-only dispatch.
7. pair R20/E20 individually current but never passed selected Model A/B coherence rule; reject operation cut.
8. final dispatch fence readback fails; no effect-possible transition.
9. profile does not require evidence head for a genuinely replay-only idempotent internal operation; do not invent unnecessary axis.
10. target dedup used as replay substitute but evidence/trust required heads still need coherent operation cut.

## 11. Practical rule

> A protected dispatch may cross the effect-possible boundary only after every required protected-head dependency is both uniquely current under PR #25 and coherently bound into the exact operation cut by an explicit aggregate or ordered-revalidation profile.

No dispatch implementation, machine action, witness service, provider mutation, merge, or deployment is authorized.
