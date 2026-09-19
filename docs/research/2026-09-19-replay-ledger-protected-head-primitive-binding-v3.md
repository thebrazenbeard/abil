# Replay Ledger Protected-Head Primitive Binding V3

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #14 predecessor exact head `ec6dc0c1bc9f88bd9e93525e51876c3919df7f1e`.

Required shared semantic dependency:
- Draft PR #25 head: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`
- artifact: `docs/research/2026-09-19-protected-head-witness-semantic-primitive-v1.md`
- blob: `fa5a883551d92fd35b73f0ad6bd5456caf81ffd0`

This binding supersedes any reading of PR #14 V2 in which witness independence alone is sufficient.

## 1. Replay currentness uses the shared uniqueness primitive

`ReplayLedgerHeadWitness` is a domain specialization of the PR #25 `ProtectedHeadWitness`.

Therefore replay CURRENT requires:
- exact subject equality to the unique current protected head;
- predecessor-bound unique advancement;
- valid ProtectedHeadCommitReceipt;
- current WitnessAuthorityReadReceipt;
- no unresolved split-brain/fork;
- replay-domain closure predicates.

Two incompatible replay successors from the same predecessor MUST NOT both receive CURRENT_COMMITTED.

## 2. Replay witness commit tuple

At minimum, replay advancement binds:

`(replay_domain, scope, predecessor_witness_digest, predecessor_sequence, successor_replay_cut_digest, writer_or_ownership_generation, commit_authority_profile)`.

The commit succeeds only if the predecessor remains the unique current replay head.

A stale predecessor commit attempt fails.

## 3. Historically committed candidate versus uniquely current head

If a replay candidate:
- is valid;
- was locally or historically persisted;
- may even have a historical commit receipt under a weaker/non-current mechanism;

but is not the unique current PR #25-compliant protected head, it is not current replay authority.

Use:
- `AUTHORIZED_NOT_COMMITTED`;
- `HISTORICAL`;
- `CONFLICTING`;
- `CURRENTNESS_UNRESOLVED`
as applicable.

## 4. Replay witness authority currentness

Replay witness advancement authority MUST bind an independently current authority/root cut appropriate to the deployment/domain.

The replay ledger itself cannot decide who may advance its witness.

If witness authority becomes stale/revoked/conflicting:
- no new replay-head advancement;
- current replay read semantics follow the last uniquely committed head plus operation policy;
- protected writes block if current witness-authority resolution is required and unresolved.

## 5. Failover

A standby may not promote its replay cut based on local replication status.

It must:
- resolve the unique current protected replay head;
- prove its local/reconciled cut equals that head;
- resolve current writer/ownership generation;
- resolve target-dedup state where relied upon.

If partition prevents unique replay-head resolution:
protected replay-dependent writes block.

## 6. Target dedup remains a separate specialization dependency

Target-dedup currentness does not replace protected-head uniqueness unless the exact operation profile explicitly accepts a target-side barrier as the replay substitute.

Where accepted, the target-dedup proof must itself establish:
- exact target identity;
- current session/configuration;
- persistence/restart/replacement semantics;
- request namespace;
- retention/currentness;
- qualified authority/provenance.

No local replay fork is made harmless merely by assuming target dedup.

## 7. Hostile checks

Future implementation/review SHOULD include:

1. W19 -> R20A/R20B concurrent replay successors; only one may become CURRENT_COMMITTED.
2. partitioned witnesses both return local success but no single-head guarantee; currentness fails.
3. stale writer attempts replay-head advance after ownership generation changed; reject.
4. replay candidate higher generation but no ProtectedHeadCommitReceipt; non-current.
5. replay witness authority derived only from replay store row; reject circular authority.
6. failover replica behind unique protected head; no dispatch.
7. restored replay store includes locally committed branch not selected by unique witness; historical/non-current.
8. same witness sequence with different replay cut digest; conflict.

## 8. Practical rule

> Replay state is current only when the exact replay cut is the uniquely committed PR #25 protected head for the exact scope under current commit authority. Witness independence without unique predecessor-bound advancement is insufficient.

No replay implementation, witness service, target mutation, write action, merge, or deployment is authorized.
