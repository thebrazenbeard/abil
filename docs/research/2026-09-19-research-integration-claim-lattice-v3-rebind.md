# ABIL Research Integration / Claim Lattice V3 Rebind

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH INTEGRATION REBIND / NO IMPLEMENTATION OR MERGE AUTHORITY**

Date: 2026-09-19

Predecessor integration map:
- PR #19 head: `107e426e4c4ccf2ecf2ed2b438193ae5f79dae25`
- V2 artifact: `docs/research/2026-09-19-research-integration-claim-lattice-v2.md`

Purpose:

> Preserve the V2 dependency/invalidation map while rebinding every subject that moved during the 2026-09-19 hostile-repair pass.

This file supersedes only the exact-head bindings and companion references listed below. All unchanged V2 integration rules remain in force.

## Current exact bindings

- PR #2 architecture: `712d5b30b45ba9299dcfce0599878cb81db70e8f`
- PR #3 R6 written design: `1da5bc57b0228178300f6ba966d97d1dce807dc1`
- PR #4 component evidence/policy: `e60bc866ad6893214c14b7dd25e312752dc4c791`
- PR #6 write-admission design: `b191822ecbc95ce120384acf1c17289b4b834033`
- PR #14 replay-ledger currentness: `ec6dc0c1bc9f88bd9e93525e51876c3919df7f1e`
- PR #15 dispatch protected commit barrier: `78b62ccb5c3c6f669a50185c2080eb5cf607848b`
- PR #17 transaction reconciliation current-cut: `30cccddc0eb2ec476d97c3c6166cc71d2b31b7fb`
- PR #18 evidence-ledger currentness: `13d0a5c6712ca38fed6887913c49366647bf623e`
- PR #20 producer authenticity/provenance: `dfb66be6b39ee66a270f1f29fd25de24790affb1`
- PR #21 trust-state currentness V3: `abeaf69774eefe96701e7db73cd54e24dc5294b6`
- PR #22 transition authorization: `a6377627f73fed5a396ea9606e02b17dbdd92392`
- PR #23 governance-root currentness: `705e0a9c2aa0143091761a2eb875213e1c24832e`
- PR #24 time-source currentness: `57039cecbc8aa8bbf41ae2bf56a037d50a03db5b`

Unlisted PR heads retain the bindings from the V2 integration map until they move or a material finding changes their subject.

## New/updated companion subjects

### PR #4
- `docs/research/2026-09-19-component-evidence-restoration-authority-and-dependency-closure-v1.md`
- `docs/research/2026-09-19-component-evidence-definition-authority-and-restoration-independence-v2.md`

Current rule:
dependency closure is valid only under an authorized, provenance-bound claim/dependency/envelope/restoration policy subject. Unauthorized policy weakening cannot create a fresh green derivation.

### PR #14
- `docs/research/2026-09-19-replay-ledger-protected-head-witness-and-dedup-currentness-v2.md`

Current rule:
local maximum replay generation is not currentness proof; a separately protected replay-head witness or independently qualified target-dedup barrier is required.

### PR #15
- `docs/research/2026-09-19-dispatch-reservation-protected-commit-barrier-v2.md`

Current rule:
before non-idempotent physical effect can become possible, the exact reservation must cross the protected no-blind-replay commit barrier.

### PR #17
- `docs/research/2026-09-19-transaction-reconciliation-current-cut-and-producer-provenance-v2.md`

Current rule:
the active historical reconciliation disposition derives from the complete current witnessed evidence cut plus immutable resolution lineage and authenticated producer/reviewer evidence.

### PR #18
- `docs/research/2026-09-19-evidence-ledger-protected-head-witness-and-completeness-currentness-v2.md`

Current rule:
current complete evidence is the uniquely witnessed current ledger cut plus claim-specific required-partition closure.

### PR #20
- `docs/research/2026-09-19-evidence-producer-chain-provenance-and-trust-cut-v2.md`

Current rule:
authenticated envelope/transport/intermediary identity is not automatically authenticated evidence origin; producer-chain and transformation provenance remain explicit.

### PR #21
- `docs/research/2026-09-19-trust-state-protected-head-witness-and-transition-authority-v2.md`
- `docs/research/2026-09-19-trust-state-exact-witness-equality-and-commit-authority-v3.md`

Current rule:
protected currentness requires exact equality to the uniquely resolved witnessed head. Authorized descendants not committed by the protected witness are pending, not current. Transition authority and witness-commit authority are distinct.

### PR #22
- `docs/research/2026-09-19-trust-state-transition-authorization-composition-v2.md`

Current rule:
transition authorization binds the exact current witnessed predecessor and current governance root; protected witness advancement is separately authorized.

### PR #23
- `docs/research/2026-09-19-governance-root-protected-currentness-witness-v2.md`

Current rule:
authentic historical governance-root bytes do not prove current governance after restore/failover; a separately protected root-head witness is required.

### PR #24
- `docs/research/2026-09-19-time-source-currentness-and-trust-ordering-composition-v2.md`

Current rule:
structural identity/authority/lineage/currentness is established before temporal admissibility. Time may narrow but cannot create structural authority/currentness.

## Thirteen exact-head review state incorporated

### PR #3
Thirteen facet:
`NO DEFECT FOUND` on exact head `1da5bc57...`.

This is one peer facet only. The hard gate is not reached until all required exact-head peer review and One reconciliation are clean.

### PR #4
Thirteen predecessor review:
`CHANGES_REQUIRED`.

Source-owner successor:
`e60bc866...`.

Fresh independent rereview required.

### PR #21
Thirteen predecessor review:
`CHANGES_REQUIRED`.

Source-owner successor:
`abeaf697...`.

Fresh independent rereview required.

## No-PASS-inheritance reminders

- PR #4 evidence-policy authority does not certify any component.
- PR #14 replay currentness does not grant write authority.
- PR #15 protected reservation does not prove exactly-once physical execution.
- PR #17 reconciliation does not make a historical request reusable.
- PR #18 evidence completeness does not prove producer authenticity.
- PR #20 producer authenticity does not prove trust-state currentness.
- PR #21 trust-state currentness does not authorize a transition.
- PR #22 transition authorization does not establish root authority or witness commit.
- PR #23 root currentness does not establish subordinate trust-state currentness.
- PR #24 valid time does not create authority/currentness.

## Hard gate

Unchanged:

1. PR #3 exact-head independent peer review;
2. One reconciliation;
3. if clean, Patrick's explicit final written-design acceptance;
4. only then may implementation planning be considered.

## Authority boundary

This rebind:
- creates no implementation plan;
- authorizes no merge/canonical promotion;
- authorizes no machine connection/write;
- authorizes no commissioning/deployment;
- authorizes no credential/root/provider/time-source mutation;
- authorizes no product selection/procurement/license acceptance;
- authorizes no safety ownership.

Patrick remains sole authority for protected effects.
