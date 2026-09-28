# ABIL Research Integration / Claim Lattice V4 Rebind

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH INTEGRATION REBIND / NO IMPLEMENTATION OR MERGE AUTHORITY**

Date: 2026-09-19

Predecessor integration subject:
- PR #19 head: `08a9ac657975d772310da63c81ad164773f6711c`
- V3 rebind: `docs/research/2026-09-19-research-integration-claim-lattice-v3-rebind.md`

Purpose:

> Rebind the transaction/evidence anti-rollback chain to the shared ProtectedHeadWitness semantic primitive created in response to Thirteen's exact-head hostile review.

This file supersedes only the moved exact-head bindings and adds PR #25 as the common protected-currentness semantic dependency.

## Current moved bindings

- PR #4 component-evidence policy authority: `e60bc866ad6893214c14b7dd25e312752dc4c791`
- PR #14 replay-ledger currentness: `e9fb2751e75379ae901de5dcf539cc64cc2f109d`
- PR #15 dispatch protected/multi-head cut: `c79a13b3d6995cfccfc2f6c80b89c7dca367e0a0`
- PR #17 reconciliation current-cut: `30cccddc0eb2ec476d97c3c6166cc71d2b31b7fb`
- PR #18 evidence-ledger currentness: `0c7a764486e7bb758915e8bbe767fc5ea6f9416a`
- PR #20 producer-chain authenticity: `dfb66be6b39ee66a270f1f29fd25de24790affb1`
- PR #21 trust-state currentness V3: `abeaf69774eefe96701e7db73cd54e24dc5294b6`
- PR #22 transition authorization: `a6377627f73fed5a396ea9606e02b17dbdd92392`
- PR #23 governance-root currentness: `705e0a9c2aa0143091761a2eb875213e1c24832e`
- PR #24 time-source currentness: `57039cecbc8aa8bbf41ae2bf56a037d50a03db5b`
- PR #25 shared ProtectedHeadWitness primitive: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`

Unlisted exact-head bindings remain as recorded by V2/V3 unless moved by a later exact rebind.

## PR #25 — shared protected-head semantic primitive

Artifact:
`docs/research/2026-09-19-protected-head-witness-semantic-primitive-v1.md`

Blob:
`fa5a883551d92fd35b73f0ad6bd5456caf81ffd0`

Role:
- reusable unique protected-currentness semantics;
- predecessor-bound atomic/consensus-equivalent advancement;
- incompatible siblings cannot both receive CURRENT_COMMITTED;
- commit authority/currentness is separately bound;
- split-brain currentness fails closed;
- multi-head operations require aggregate cut or explicit ordered revalidation.

This is a shared semantic primitive, not an implementation/provider choice.

## PR #14 binding

New companion:
`docs/research/2026-09-19-replay-ledger-protected-head-primitive-binding-v3.md`

Blob:
`95081ef0418e871853e25220065d13cd38f8e219`

ReplayLedgerHeadWitness specializes PR #25.

Current replay requires:
- exact unique protected head;
- ProtectedHeadCommitReceipt;
- current witness authority;
- replay-domain closure;
- no unresolved fork.

## PR #18 binding

New companion:
`docs/research/2026-09-19-evidence-ledger-protected-head-primitive-binding-v3.md`

Blob:
`eed2febf81fb11ccf956435d7d22d2819ccecf77`

EvidenceLedgerHeadWitness specializes PR #25.

Current complete evidence requires:
- exact unique protected head;
- required-partition closure;
- current witness authority;
- no unresolved fork/replica conflict.

## PR #15 binding

New companion:
`docs/research/2026-09-19-dispatch-multi-head-operation-cut-binding-v3.md`

Blob:
`ac70aec499b87fb46ae440ad5aa30c49178b3283`

Protected dispatch now requires:
- every required head uniquely current under PR #25;
- exact operation profile selects either aggregate ProtectedOperationCutCommit or explicit independent-head ordering/revalidation;
- mandatory replay/evidence coherent binding when both axes are required;
- final dispatch fence immediately before effect-possible boundary.

The predecessor V2 `SHOULD cross-bind` language is superseded where the operation profile requires the axis.

## Thirteen transaction/evidence finding disposition

Predecessor exact review:
`CHANGES_REQUIRED`.

Blocking finding:
witness independence did not guarantee unique/non-forking advancement before dispatch consumed witness advancement as a safety barrier.

Successor closure:
- shared PR #25 unique predecessor-bound advancement;
- PR #14/#18 domain specializations;
- PR #15 operation-cut coherence.

Material finding:
replay/evidence cross-binding was advisory.

Successor closure:
PR #15 V3 makes the operation profile's selected coherent-cut rule mandatory whenever both axes are required.

Question:
witness authority/root currentness.

Successor direction:
PR #25 makes witness authority currentness explicit and non-circular; domain bindings rely on that shared predicate.

Fresh independent rereview is required. Source-owner repair is not peer credit.

## Dependency relation

Conceptually:

```text
                   PR25 ProtectedHeadWitness
                    /       |       \
                   v        v        v
              PR14 replay  PR18 evidence  PR21/PR23 compatible protected-head domains
                   \        /
                    \      /
                     v    v
                      PR15 protected dispatch operation cut
                         |
                         v
                      PR17 reconciliation / downstream historical interpretation
```

PR #20 producer authenticity remains separate from evidence-ledger currentness.
PR #24 temporal validity remains subordinate to structural unique currentness.

## No-PASS inheritance

- PR #25 source/research review cannot qualify a concrete CAS/consensus service.
- PR #14 protected replay head does not grant write authority.
- PR #18 protected evidence head does not prove record origins.
- PR #15 coherent operation cut does not prove physical execution or exactly-once semantics.
- PR #21 trust currentness does not authorize semantic transition.
- PR #23 root currentness does not establish subordinate trust state.
- PR #24 valid time does not establish structural currentness.

## Hard gate

Unchanged:

1. PR #3 exact-head independent peer review;
2. One reconciliation;
3. if clean, Patrick explicit final written-design acceptance;
4. only then may implementation planning be considered.

## Authority boundary

This rebind authorizes no:
- implementation planning;
- merge/canonical promotion;
- witness/provider deployment;
- machine connection/write;
- commissioning;
- credential/root/provider/time-source mutation;
- safety authority.

Patrick remains sole authority for protected effects.
