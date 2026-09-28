# Evidence Ledger Protected-Head Primitive Binding V3

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR STORAGE AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #18 predecessor exact head `13d0a5c6712ca38fed6887913c49366647bf623e`.

Required shared semantic dependency:
- Draft PR #25 head: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`
- artifact: `docs/research/2026-09-19-protected-head-witness-semantic-primitive-v1.md`
- blob: `fa5a883551d92fd35b73f0ad6bd5456caf81ffd0`

This binding supersedes any reading of PR #18 V2 where independent witness storage can still fork and let two incompatible evidence cuts each appear current before conflict discovery.

## 1. EvidenceLedgerHeadWitness specializes ProtectedHeadWitness

Evidence CURRENT_COMPLETE requires:
- exact cut equality to the unique current protected head;
- PR #25 predecessor-bound unique advancement;
- valid ProtectedHeadCommitReceipt;
- current witness authority;
- no unresolved fork/split brain;
- required-partition closure;
- evidence-domain continuity/completeness predicates.

Two incompatible evidence cuts from the same protected predecessor MUST NOT both receive CURRENT_COMMITTED.

## 2. Evidence witness commit tuple

At minimum, evidence-head advancement binds:

`(evidence_domain, scope, predecessor_witness_digest, predecessor_sequence, successor_evidence_cut_digest, writer_generation, commit_authority_profile)`.

If the predecessor is no longer the unique current head:
commit fails.

## 3. Partition closure happens inside the successor cut

The successor evidence cut binds:
- RequiredEvidencePartitionProfile digest;
- exact partition checkpoint set;
- EvidencePartitionClosureReceipt digest;
- gap/corruption/conflict disposition;
- aggregate evidence-cut digest.

The protected witness commits that exact aggregate evidence cut.

A caller cannot advance a head over one partition set and later substitute another equivalent-looking set without a new protected successor.

## 4. Witness authority currentness

Evidence witness commit authority is not derived from:
- checkpoint signer;
- evidence producer;
- ledger database role;
- local storage admin;
- the evidence cut itself.

It binds the independently current authority/root profile permitted to advance the exact evidence domain/scope.

If authority is unresolved, protected advancement fails closed.

## 5. Concurrent evidence cuts

If E31A and E31B both descend from E30:

- each may be internally valid;
- each may have complete partition closure;
- both may preserve authentic evidence.

But at most one incompatible successor may become CURRENT_COMMITTED for the same scope under the protected witness primitive.

The other remains historical/pending/conflicting.

Do not union the cuts automatically.

## 6. Failover / replica promotion

A replica cannot become the current evidence source because it:
- has the longest chain;
- has the largest local sequence;
- has all required partitions locally;
- is the only reachable replica.

It must reconcile to the unique protected evidence head.

If single-head resolution is unavailable:
current completeness is unresolved for protected operations that require it.

## 7. Evidence authenticity remains separate

The protected head proves which aggregate evidence cut is uniquely current.

It does not prove:
- each record's origin;
- evaluator independence;
- target receipt semantics;
- transformation correctness.

PR #20 producer-authenticity/provenance requirements remain separately required.

## 8. Historical cuts

A cut may have been historically protected-committed and later superseded.

That remains historical truth.

It does not remain current after witness advancement.

Currentness always resolves from the current unique head.

## 9. Hostile checks

Future implementation/review SHOULD include:

1. concurrent complete evidence cuts E31A/E31B from E30; only one can be CURRENT_COMMITTED.
2. partitioned witness services each return success but no qualified single-head property; current completeness fails.
3. same witness sequence with different aggregate evidence-cut digest; conflict.
4. evidence DB role self-authorizes witness commit; reject.
5. stale replica has complete partitions but protected head is newer; stale cut not current.
6. checkpoint signer valid but witness authority stale; no new current evidence cut.
7. partition closure changes after witness commit without new successor cut; reject substitution.
8. historically committed old cut restored; remains historical.

## 10. Practical rule

> Evidence currentness requires both claim-specific partition completeness and PR #25-compliant unique protected-head commitment. A complete local ledger or independent witness store without non-forking predecessor-bound advancement is insufficient.

No evidence storage/witness implementation, retention action, machine authority, merge, or deployment is authorized.
