# ABIL Chat Continuation — post PR6 exact-head remediation

Status: **PRIVATE ABIL CONTINUATION / STATE SNAPSHOT / NO MERGE OR DEPLOY AUTHORITY**

Repository: `thebrazenbeard/abil`

Continuation branch: `state/abil-chat-continuation-20260918-b191822e`

Predecessor checkpoint:
- branch: `state/abil-chat-continuation-20260918-1443`
- commit: `eba35f9b3456493a71790b3b51f4678364259f05`
- file blob: `f3966faa03cf8b13ea547210110264b5cd2f9d06`

This checkpoint is coordination/state only. Treat it as a starting snapshot, not current truth. It grants no merge/canonical promotion, deployment, live-machine connection/write, credential/provider/permission mutation, repository visibility/publication change, procurement/license acceptance, safety authority, or other protected effect.

## Native project execution rule

Continue under native `.` semantics:

> orient to live state → identify highest-value actionable frontier → do work → verify → persist/route → reassess → continue until Patrick's decision/authority/credentials/physical intervention or an unavailable capability is genuinely required.

Do not carry old PASS/FAIL status across head changes.

## GitHub Project surface

The GitHub connector in this runtime exposes no GitHub Project item/status API.

Project board state: **NOT OBSERVED**.

Do not infer board contents from PRs or Bus messages.

## Main

Fresh compare against the predecessor checkpoint showed no main movement.

`main@0812d9780ce1648820269fa142a43e17030ef793`

## Draft PR #6 — write-capability admission boundary

Title: `Add fail-closed write-capability admission boundary`

Base: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Current exact head:

`b191822ecbc95ce120384acf1c17289b4b834033`

State: **OPEN / DRAFT / UNMERGED / MERGEABLE / DESIGN-GOVERNANCE ONLY**

The Runner review on predecessor `fff52af32089f1bf32c4abbbc572b25d89127d5b` was **CHANGES REQUIRED** for three supported gaps:

1. freshness self-declarable/under-specified;
2. revoked/superseded epoch rejection not computable from declared inputs;
3. multi-surface completeness not mechanically bound.

Those findings were verified against source rather than accepted by assertion.

Current remediation at `b191822e...`:
- requires independently resolved freshness-profile identity/digest;
- requires per-surface freshness deadlines to be independently derived from the freshness profile and aggregate deadline to be derived from required surfaces;
- binds independently resolved canonicalization-profile identity/digest before epoch/surface-set digests are accepted;
- materializes current/revoked/superseded epoch state, rejects conflicting/ambiguous epoch state, recomputes `max_observed_authority_epoch`, and requires candidate epoch to exceed it;
- binds independently resolved deployment authority-surface profile/required set;
- carries per-surface reads plus required/reconciled set digests and rejects duplicate/missing/mismatched surfaces;
- keeps `SCHEMA_VALID` distinct from stateful `WRITE_ADMISSION_VALID`;
- hostile design contract contains 36 cases.

Verification performed:
- both JSON documents parse successfully;
- exact receipt schema contains bound freshness/canonicalization/surface/epoch inputs;
- validation prose contains derivation/recomputation rules;
- compare `fff52af...` → `b191822e...` is 8 commits ahead / 0 behind and changes only four expected PR #6 files:
  - `docs/AUTHORITY_STATE_READ_RECEIPT_V1.schema.json`
  - `docs/WRITE_CAPABILITY_ADMISSION_V1.md`
  - `docs/WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.hostile-vectors.json`
  - `docs/WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.md`
- PR base remains exactly `712d5b30...`;
- no combined-status contexts are reported for the head.

The earlier exact-head rereview request for `8180e3e8cd90e65629634a728302456cb275f8ff` is stale provenance. A superseding rereview request is posted on PR #6 for `b191822e...`.

No executable validator/current-authority reader is claimed to exist or be qualified.

**Next PR #6 frontier:** exact-head hostile/Runner rereview of `b191822e...`. Process only findings actually supported by that exact source.

## Draft PR #3 — R2 non-actuating substrate design

Current exact head:

`c2e363d4c1b8c67e032c22d9cad6451342b04e7b`

Architecture base:

`712d5b30b45ba9299dcfce0599878cb81db70e8f`

State: **OPEN / DRAFT / UNMERGED / MERGEABLE / DESIGN ONLY**

R5 file:
`docs/superpowers/specs/2026-09-18-abil-r2-review-corrections-r5.md`

R5 blob:
`6cd17677b485bef48f81b91cc4b06dac646d8447`

R5 binds evaluator-only context actually consulted by fixture selection, admissibility, scoring/target construction, negative controls, or claim ceiling into the reproducible experiment subject while preserving the learner information firewall.

A source-owner exact-head audit was posted:
`SOURCE_OWNER_R5_DELTA_AUDIT_CLEAN / NO_PEER_CREDIT / NO_IMPLEMENTATION_AUTHORITY`.

Fresh check found **no exact-head R5 peer submission yet**. Three/Seven/Nine/Two/Six and One were routed an exact-head rereview request through Bus.

**Next PR #3 frontier:** process exact-head peer returns and One reconciliation. If the exact design state becomes clean, STOP BEFORE implementation planning and obtain Patrick's explicit final written-design acceptance. Package scaffolding and Hephaestus handoff remain held.

## Draft PR #2 — successor architecture

Current exact head:

`712d5b30b45ba9299dcfce0599878cb81db70e8f`

Base:

`main@0812d9780ce1648820269fa142a43e17030ef793`

State: **OPEN / DRAFT / UNMERGED / MERGEABLE**

Fresh review read found no independent peer review bound to this exact head. Older peer results at `22187ea...` remain stale provenance.

Exact-head review was routed to:
- Nine — architecture delta/regression;
- Four — minimality/coherence;
- Thirteen — authority/premise/provenance;
- Seven — security/safety-noninterference regression;
- One — coordinator reconciliation after peer returns.

Two source-owner seams remain explicitly nonblocking hypotheses pending peer challenge:
- field-validation roadmap does not repeat the exact `AuthorityGrant` name/trust-root wording from the normative control contract;
- future third-party component certification/conformance scope needs a dedicated product-qualification evidence contract.

Do not move the head for cosmetic wording unless a real blocker is established.

## Draft PR #4 — deterministic runtime / fieldbus / appliance research

Current exact research head:

`68195ee0a5743fa9be164dcd43c1c8c6e34ba6c0`

New research artifact:
`docs/research/2026-09-18-component-conformance-evidence-boundary.md`

Blob:
`4bf1d5aaf125c64f8a97ec2d00129c96f5f73753`

The research now explicitly separates:
- `DIRECT_COMPONENT_EVIDENCE`;
- `COMPOSITION_DEPENDENT_EVIDENCE`;
- `ABIL_OWNED_EVIDENCE`;
- `MACHINE_APPLICATION_EVIDENCE`.

Purpose: qualified commercial components may shrink ABIL-owned qualification surface without allowing unsupported certificate/conformance inheritance into the assembled controller or machine application.

Research only; no certification/product/procurement/license/implementation authority.

## Draft PR #5 — competitive boundary / reconstruction benchmark research

Current exact research head:

`d12b65545d20f6f267c0ccacc8d55e5ec5ebed1f`

New research artifact:
`docs/research/2026-09-18-evaluator-context-benchmark-alignment.md`

Blob:
`f28b1b98e549d683fea313ce185d27b9d43fa553`

The source-optional benchmark now explicitly separates participant-visible projection identity from hidden evaluator-context identity and requires evaluator-only context that materially changes scoring semantics to be bound into reproducible run/evidence identity.

This is non-normative research and does not promote PR #3 R5.

## Current combined-status observation

GitHub combined-status queries returned no reported status contexts for current PR #2/#3/#4/#5/#6 exact heads. This means **NO STATUS CONTEXT OBSERVED**, not that tests or CI passed.

## Chat Bus

Hub: `thebrazenbeard/chat-communication-bus`

Vera lane: `bus/vera-v2`

Current HEAD.json blob observed while saving this checkpoint:

`71290d7199b04d6f976403af5a69174a5a18d12a`

Current HEAD pointer:
- latest_message_id: `vera-v2-20260918-abil-pr6-superseding-rereview`
- latest_path: `messages/20260918T1555-abil-pr6-superseding-rereview.md`
- latest_message_commit: `7d5637566c7f0331b2a55c057f8ee1f526a1c6c5`
- status: `action-required-superseding-exact-head`

Current work-bearing messages routed during this continuation include:
- PR #6 rereview / PR #3 R5 gate routing;
- PR #3 exact-head R5 peer rereview;
- PR #2 exact-head architecture peer rereview;
- PR #6 superseding exact-head rereview at `b191822e...`.

Fresh compare found worker lanes One/Two/Three/Four/Six/Seven/Nine/Thirteen unchanged from the predecessor checkpoint at the final review sweep; no worker reply had landed yet.

On restore, fresh-check every lane before relying on that statement.

## Current stop reason / next execution frontier

The source/research work currently reachable without protected authority has been advanced and verified.

The next highest-value frontiers are review-return dependent:

1. PR #6 exact-head hostile rereview of `b191822e...`.
2. PR #3 exact-head R5 peer returns + One reconciliation.
3. PR #2 exact-head architecture peer returns + One reconciliation.
4. If PR #3 becomes clean, Patrick's explicit final written-design acceptance is required before implementation planning.
5. GitHub Project item/status state remains unavailable in this runtime and must stay `NOT OBSERVED`.

Do not wait on stale hashes, do not invent worker replies, and do not interpret this checkpoint as merge/deploy/machine authority.

## Resume directive

`ABIL::RESTORE::ABIL_CHAT_CONTINUATION_20260918_B191822E`

# END CONTINUATION
