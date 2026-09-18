# ABIL Chat Continuation — effect-intent, replay-ledger, and dispatch-commit research

Status: **PRIVATE ABIL CONTINUATION / STATE SNAPSHOT / NO MERGE OR DEPLOY AUTHORITY**

Repository: `thebrazenbeard/abil`

Continuation branch: `state/abil-chat-continuation-20260918-88f1a232`

Predecessor continuation:
- commit: `9b2b9a81a48d4fbd08153ec89a99b233cdb3fa38`
- file: `state/continuation/ABIL_CHAT_CONTINUATION_20260918_3D61F4DA.md`
- blob: `144dc410538b0e74a15e894bf031b3fa1533e637`

Treat this file as a starting snapshot, not current truth. Fresh-check exact heads/reviews/Bus/Project state before carrying status forward.

## Current live heads at save

- main: `0812d9780ce1648820269fa142a43e17030ef793`
- PR #2: `712d5b30b45ba9299dcfce0599878cb81db70e8f`
- PR #3: `c2e363d4c1b8c67e032c22d9cad6451342b04e7b`
- PR #4: `cd4f811ec9318231a3864fcedf4cd67befab07a7`
- PR #5: `385207c1bff5189651c1048f2d09f3805d751873`
- PR #6: `b191822ecbc95ce120384acf1c17289b4b834033`
- PR #7: `a62ae16a0c1bc484ae6b45e4af853af64a2e6707`
- PR #8: `7d11cea51bfff3f2bf32e98516479be4d742d172`
- PR #9: `90d40f4baca29629f8f17f956f20687fee674820`
- PR #10: `5e15ed24fc5f9286eb21377e0532f6d88e8a1840`
- PR #11: `fcb0a88b0a37a9c7c722fe0e5f966a7a3f968bc3`
- PR #12: `3d61f4da301af41f4d56bbcffb4609c38b815bd3`
- PR #13: `8ab8ee9e95c86a04c4d34a8042e13b05979d6364`
- PR #14: `fc9846e3eb82e3b0c8eccbf42769b09ba7eaaa2c`
- PR #15: `88f1a232a7265e8713e4564260b28e35cf53369e`

Main fresh-compare remained IDENTICAL to `0812d9780ce1648820269fa142a43e17030ef793`.

Observed PRs #2/#3/#4/#5/#7/#8/#9/#10/#11/#12/#13/#14/#15 remained OPEN / DRAFT / UNMERGED / MERGEABLE at final sweep.

GitHub Project item/status API remains unavailable in this runtime. Board state: **NOT OBSERVED**.

## Hard design/review gates preserved

### PR #3

Exact R5 subject:
`c2e363d4c1b8c67e032c22d9cad6451342b04e7b`

No exact-head peer review observed this cycle.

If exact-head review/reconciliation becomes clean, **STOP before implementation planning** and obtain Patrick's explicit final written-design acceptance.

### PR #2

Exact architecture subject:
`712d5b30b45ba9299dcfce0599878cb81db70e8f`

No exact-head peer review observed.

Do not mutate for cosmetic wording.

### PR #6

Exact subject:
`b191822ecbc95ce120384acf1c17289b4b834033`

Disposition remains:
`DESIGN_GOVERNANCE_CONTRACT_PASS`

Fresh-check this cycle:
- OPEN
- DRAFT
- MERGEABLE
- head unchanged

Source-owner downstream composition note:
- comment `5737465194`

Disposition:
- **NO REOPEN OF PR #6 PASS**
- future implementation must bind admission to exact physical transaction/effect intent.
- no implementation or machine-write authority.

## Previously frozen research heads

- PR #4 component-evidence currentness: `cd4f811...`
- PR #5 reconstruction benchmark: `385207c1...`
- PR #7 deployment commissioning currentness: `a62ae16a...`
- PR #8 support/recovery currentness: `7d11cea5...`
- PR #9 cross-axis consistency: `90d40f4b...`
- PR #10 dependency-cycle resolution: `5e15ed24...`
- PR #11 non-authority currentness proof: `fcb0a88b...`
- PR #12 snapshot/revalidation: `3d61f4da...`

No exact-head peer review observed on any of them this cycle.

## PR #13 — effect-intent binding and anti-replay

Draft PR:
`#13 Research effect intent binding and anti-replay`

Exact subject:
`8ab8ee9e95c86a04c4d34a8042e13b05979d6364`

Base:
`work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Exact compare:
- ahead: 1
- behind: 0
- changed files: 1
- mergeable: true

Artifact:
`docs/research/2026-09-18-effect-intent-binding-and-antireplay-v1.md`

Blob:
`20381ed72412146b5fe8377097072781b2a17085`

Research adds:
- exact effect-intent subject;
- decision-to-request binding;
- request-ID conflict handling;
- parameter substitution rejection;
- exact units/profile binding;
- single-effect / bounded-repeat / atomic-batch / qualified-session cardinality;
- ambiguous-outcome interaction;
- replay protection across restart/authority/ownership/deployment changes;
- precondition binding;
- batch and partial-batch semantics;
- dispatch guard composition.

Central rule:
a write-admission decision is not a generic bearer token; it must bind the exact effect and allowed reuse count.

Review request:
`messages/20260918-abil-pr13-effect-intent-review-request.md`

Bus commit:
`90cad213fa559914ef1ac84d63c162faa7094a63`

Requested:
- Six — runtime/replay/idempotency
- Thirteen — provenance/identity/canonicalization
- One — reconciliation

Source-owner persistence finding:
- PR #13 comment `5737476852`

Finding:
same-generation restore of an older replay ledger can forget consumed requests even while authority remains current.

## PR #14 — replay-ledger anti-rollback

Draft PR:
`#14 Research replay ledger anti-rollback`

Exact subject:
`fc9846e3eb82e3b0c8eccbf42769b09ba7eaaa2c`

Base:
`work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Exact compare:
- ahead: 1
- behind: 0
- changed files: 1
- mergeable: true

Artifact:
`docs/research/2026-09-18-replay-ledger-antirollback-v1.md`

Blob:
`071ea985dbd7a1a763a6c6373e34cfa4fa323625`

Research adds:
- replay state as durable safety-relevant evidence, not cache;
- request consumption states;
- monotonic replay-ledger generation;
- same-authority-generation restore handling;
- replay reconciliation before write resumption;
- backup/snapshot replay-cut metadata;
- storage replacement rules;
- target-side dedup durability requirements;
- garbage collection constraints;
- namespace rotation limits;
- HA/failover replay coordination;
- batch partial-execution state;
- session/bounded-repeat counter preservation;
- PR #12 currentness integration and PR #13 effect-intent linkage.

Central rule:
replay/consumption state for physical effects must not become less restrictive after recovery.

Review request:
`messages/20260918-abil-pr14-replay-ledger-review-request.md`

Bus commit:
`b0c414d886178ad8b45126d1ace34080816920a5`

Requested:
- Three — lifecycle/recovery
- Six — runtime/dedup/failover
- One — reconciliation

Source-owner dispatch-order finding:
- PR #14 comment `5737489111`

## PR #15 — dispatch commit ordering

Draft PR:
`#15 Research dispatch commit ordering`

Exact subject:
`88f1a232a7265e8713e4564260b28e35cf53369e`

Base:
`work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Exact compare:
- ahead: 1
- behind: 0
- changed files: 1
- mergeable: true

Artifact:
`docs/research/2026-09-18-dispatch-commit-ordering-v1.md`

Blob:
`310457894299a3843d5d6594342cc1fa6eca8c5f`

Research adds:
- durable pre-dispatch reservation state;
- explicit crash windows around reservation/send/acceptance/result persistence;
- conservative "effect may occur" semantics;
- known-no-effect proof requirements;
- idempotency exception requirements;
- target-side transaction/dedup integration;
- explicit limits for non-transactional industrial protocols;
- WAL/storage durability qualification boundaries;
- HA/failover commit ordering;
- cancellation/timeout race handling;
- batch/session reservation ordering;
- PR #12/#13/#14 integration.

Central rule:
durable replay state must cross its conservative "effect may occur" commit point before a non-idempotent physical effect can become possible.

Evidence ceiling:
does not prove exactly-once semantics, storage durability, protocol transactional guarantees, or target deduplication.

Review request:
`messages/20260918-abil-pr15-dispatch-commit-review-request.md`

Bus commit:
`1f502e7baba46da45a2a6c5951ce4a218030ea6e`

Requested:
- Six — runtime/crash-order
- Three — storage/recovery/lifecycle
- One — reconciliation

No exact-head review observed.

## Final peer sweep

At save:
- no new exact-head GitHub review on PR #2/#3/#4/#5/#7/#8/#9/#10/#11/#12/#13/#14/#15;
- Two/Three/Four/Six/Seven/Nine/Thirteen unchanged from prior ABIL checkpoints;
- One advanced only unrelated portfolio messages;
- no current ABIL review reply observed.

## Current highest-value frontier

The write-safety research chain now covers:

1. current authority admission — PR #6
2. deployment/recovery currentness — PR #7/#8
3. cross-axis consistency/cycles — PR #9/#10
4. non-authority currentness proof — PR #11
5. decision-to-dispatch snapshot revalidation — PR #12
6. exact effect-intent / anti-replay binding — PR #13
7. replay-ledger anti-rollback — PR #14
8. physical dispatch commit ordering — PR #15

Highest-value next work is now independent exact-head review/reconciliation. Further authoring should be driven by a concrete composition finding, not cosmetic expansion.

Priority:
1. PR #3 exact-head R5 peer return + One reconciliation.
2. PR #2 exact-head architecture peer return + One reconciliation.
3. Process exact-head research reviews on #4/#5/#7/#8/#9/#10/#11/#12/#13/#14/#15.
4. Preserve PR #6 PASS unless an exact new finding truly changes its disposition.
5. Preserve all review heads.
6. If PR #3 becomes clean after exact-head review/reconciliation, Patrick's explicit final written-design acceptance is the hard gate before implementation planning.

No merge/canonical promotion, implementation, commissioning, recovery/restore action, deployment, live-machine connection/write, credential/provider mutation, repository visibility/publication change, procurement/license acceptance, or other protected effect is authorized.

## Resume directive

`ABIL::RESTORE::ABIL_CHAT_CONTINUATION_20260918_88F1A232`

# END CONTINUATION
