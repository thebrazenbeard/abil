# Evidence Ledger Protected Head Witness and Completeness Currentness V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR STORAGE AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #18 predecessor exact head `8d7ffe6650136b7a2037206da75a665235324a16`.

This companion closes a restore/currentness seam in Evidence Ledger Integrity and Continuity V1.

V1 correctly distinguishes record integrity, ledger continuity, completeness and availability, and requires stale prefixes/selective restores to be detectable.

The missing structural predicate is:

> What independently proves which evidence-ledger cut is the current protected cut after restore, failover, replica divergence, or selective storage rollback?

A locally highest sequence/generation/checkpoint is not sufficient because the local store itself may be the stale restored object.

## 1. Evidence record truth and ledger currentness are separate

An immutable evidence record may remain historically valid even when:
- the local ledger is stale;
- a newer ledger cut exists elsewhere;
- a required partition is missing;
- the current checkpoint witness cannot be resolved.

Therefore distinguish:

- record integrity;
- historical ledger continuity;
- current ledger-head identity;
- required-partition completeness;
- availability.

A valid historical prefix is not automatically current complete evidence.

## 2. EvidenceLedgerHeadWitness

A future high-consequence evidence ledger should bind a separately protected current-head subject:

`EvidenceLedgerHeadWitness`

or mechanically equivalent qualified anti-rollback commit record.

It binds at least:
- evidence-ledger domain ID;
- deployment/scope;
- ledger generation/cut identity;
- current checkpoint/root digest;
- previous checkpoint/root or lineage accumulator;
- required-partition-profile digest;
- per-partition current checkpoint IDs/digests where applicable;
- witness sequence/generation;
- witness authority/profile;
- commit/verification evidence;
- immutable witness digest.

The witness rollback domain MUST be sufficiently independent from the ledger storage it judges that restoring the ledger cannot silently restore the witness to the same stale cut.

## 3. Local maximum is not currentness

Do not infer current evidence cut from:
- highest local sequence;
- highest local ledger generation;
- latest local filename;
- newest local wall-clock timestamp;
- longest local hash chain;
- most complete-looking replica;
- replica with the most favorable evidence.

These may be evidence about a candidate cut.

They are not sufficient proof that the cut is current.

## 4. Current evidence-cut predicate

A current evidence cut for a claim/operation is established only when all required predicates hold:

- checkpoint/segment integrity valid;
- lineage/continuity valid;
- protected ledger-head witness resolves;
- exact witnessed cut is available or its required data is verifiably retrievable;
- required-partition profile resolves;
- every required partition cut is present and identity-matched;
- no unresolved fork/replica conflict affects the required scope;
- producer-authenticity requirements are satisfied where required;
- currentness/time requirements are satisfied where material.

If one required predicate is unknown, the result cannot silently remain CURRENT_COMPLETE.

## 5. Missing witness fails closed

If the protected evidence-ledger witness is:
- unavailable;
- unverifiable;
- stale;
- scope-mismatched;
- conflicting;
- unable to identify a unique current cut;

then high-consequence claims requiring current complete evidence become:
`EVIDENCE_LEDGER_CURRENTNESS_UNRESOLVED`
or a stronger fail-closed disposition.

Historical reads MAY continue under explicitly historical/incomplete semantics where safe.

## 6. EvidenceLedgerCheckpoint V2

A checkpoint should bind at least:

- ledger domain ID;
- deployment/scope;
- checkpoint generation;
- start/end sequence or equivalent range;
- predecessor checkpoint digest;
- segment/root digest;
- required-partition-profile digest;
- per-partition cut identities/digests;
- gap/corruption dispositions;
- producer/authenticity subject for the checkpoint itself;
- canonicalization profile;
- temporal/order metadata where material;
- checkpoint digest.

A checkpoint's existence does not make it current.

## 7. Required partition profile is independently bound

The required partition set cannot be inferred from whichever partitions happen to be present.

A `RequiredEvidencePartitionProfile` or equivalent should bind:
- claim/operation class;
- required partition IDs/classes;
- optional partitions;
- minimum continuity cut for each;
- acceptable replica/source classes;
- cross-partition dependency rules;
- retention requirements;
- currentness rules;
- profile version/digest.

The caller cannot omit an inconvenient partition to obtain a cleaner evidence result.

## 8. EvidencePartitionClosureReceipt

For each current evidence evaluation, bind:

- required-partition-profile digest;
- exact resolved partition set;
- exact checkpoint/root for each partition;
- partition continuity result;
- partition availability result;
- producer-authenticity result where required;
- unresolved/missing/conflicting partitions;
- closure result;
- exact partition-cut-set digest.

Suggested closure results:
- `PARTITION_CLOSURE_COMPLETE_CURRENT`;
- `PARTITION_CLOSURE_INCOMPLETE_REQUIRED`;
- `PARTITION_CLOSURE_CONFLICTING`;
- `PARTITION_CLOSURE_STALE`;
- `PARTITION_CLOSURE_UNKNOWN`.

No stronger evidence-completeness claim may be issued unless the required closure result passes the exact claim profile.

## 9. Multi-partition current cut

A set of individually valid partition checkpoints does not automatically form a valid combined evidence cut.

Two valid models are allowed:

### 9.1 Atomic partition cut
One parent cut binds all required partition checkpoints and the protected ledger witness advances to that exact aggregate cut.

### 9.2 Explicit independent-partition semantics
The profile defines:
- permitted partial advancement;
- cross-partition dependency ordering;
- admissible combinations;
- which claims block during partial advancement;
- reconciliation requirements;
- exact combination receipt.

A combination that never existed as an admissible cut cannot be assembled after the fact merely because each component is individually valid.

## 10. Selective restore detection

Restoring:
- positive receipts;
- old clean checkpoint;
- one replica;
- one evidence class;

while omitting:
- conflicts;
- corrections;
- ambiguity;
- denied operations;
- negative controls;
- other required partitions

must not produce a new current cut.

The protected witness plus required-partition closure must expose the regression/incompleteness.

## 11. Restore procedure

A future restore flow should conceptually:

1. load restored ledger bytes/checkpoints as candidate historical state;
2. independently resolve the protected EvidenceLedgerHeadWitness;
3. identify the exact current required partition profile;
4. compare restored cuts with the witnessed cut;
5. retrieve/reconcile missing newer partitions/checkpoints as permitted;
6. detect forks, gaps, corruption and selective restore;
7. verify checkpoint producer authenticity where required;
8. issue a current evidence-cut receipt only after closure passes.

A backup's embedded generation/checkpoint is evidence of backup contents, not authority that those contents are current.

## 12. Failover procedure

A standby/replica MUST NOT become authoritative current evidence merely because:
- it is reachable;
- it has a valid chain;
- it reports the highest local generation.

It should reconcile against:
- protected ledger-head witness;
- exact partition profile;
- required current checkpoint set.

If it cannot prove current closure, current evidence-dependent protected operations block or downgrade according to the operation profile.

## 13. Replica conflict

If two replicas present incompatible successors from the same witnessed predecessor and no qualified commit establishes a unique current cut:

`EVIDENCE_LEDGER_CONFLICTING`.

Do not:
- union records automatically;
- choose the cleaner replica;
- choose the longer chain;
- choose the newer wall-clock timestamp;
- choose whichever result allows the requested action.

Conflict resolution must be explicit and append-only.

## 14. Checkpoint signer is not evidence-origin authority

A checkpoint may be authentically signed by an aggregator while containing records from many origins.

Checkpoint authenticity proves only the bounded claim established by the checkpoint-signing profile.

It does not automatically prove:
- every record origin;
- every transformation;
- every human/evaluator identity.

PR #20 producer-chain authenticity remains a separate dependency.

## 15. Evidence-ledger witness authority cannot be self-issued by the ledger

A ledger cannot establish its own anti-rollback witness solely by appending:
`I am current`.

The witness authority/failure domain must be sufficiently independent to falsify storage rollback.

Possible implementation classes include:
- independently protected append-only commit service;
- hardware monotonic state;
- separately governed quorum/consensus log;
- another qualified anti-rollback mechanism.

This research intentionally does not select one.

## 16. Historical cut versus current cut

Historical verification binds:
- exact historical checkpoint/cut;
- continuity evidence available for that cut;
- historical producer/trust state where required;
- explicit historical disposition.

Historical verification MUST NOT:
- advance the current ledger witness;
- reactivate stale replay/currentness conclusions;
- manufacture present completeness.

A historically complete cut may be useful and true without being current.

## 17. Currentness receipts bind exact evidence cuts

PR #11/PR #12-style currentness/admission decisions that rely on evidence completeness should bind:

- EvidenceLedgerHeadWitness digest;
- RequiredEvidencePartitionProfile digest;
- EvidencePartitionClosureReceipt digest;
- exact aggregate evidence-cut digest;
- relevant producer-authenticity/trust-cut receipts;
- operation-specific currentness result.

If the ledger witness later advances or a required partition becomes invalid, the old decision cannot be reused as if it were evaluated on the new cut.

## 18. Replay-ledger cross-binding

PR #14 replay state and PR #18 evidence ledger may remain separate domains.

For protected physical effects, the current cut should expose enough cross-binding to detect:
- replay says consumed while evidence history lacks the request/dispatch subject;
- evidence records ambiguous execution while replay restored to UNUSED;
- one store advanced beyond the other;
- selective restore of one store.

Neither store may silently bless the other's stale state.

## 19. Reconciliation cross-binding

PR #17 late reconciliation may append new evidence conclusions.

A new reconciliation generation should:
- bind the prior reconciliation subject;
- bind the exact evidence-ledger witnessed cut;
- append rather than rewrite;
- preserve conflicts/negative evidence;
- never mutate an old transaction back to UNUSED.

If reconciliation evidence exists only on a stale/unwitnessed ledger fork, it cannot become the current authoritative reconciliation by local preference.

## 20. Time and ordering

Time may support:
- event correlation;
- retention;
- historical interpretation.

But protected ledger witness/lineage determines structural evidence-cut currentness.

Wall-clock time MUST NOT:
- revive stale checkpoint;
- resolve ledger fork;
- make a restored prefix current;
- choose a favorable replica.

Where time is material, bind PR #24-style time-source/session/uncertainty evidence.

## 21. Retention/compaction commit

Retention or compaction that changes the evidence representation MUST produce a new protected evidence subject/cut preserving required proof obligations.

A compaction result should bind:
- source cut;
- retained proof roots/summaries;
- deleted/tombstoned identities;
- governing retention profile;
- authorizer;
- claim dependencies retained;
- resulting checkpoint/cut.

Irreversible deletion MUST NOT be authorized merely by a local wall-clock jump.

## 22. Claim-specific completeness

Not every claim requires every partition.

Completeness is claim/operation-specific.

Examples:
- replay decision may require transaction/replay/ambiguity partitions;
- benchmark claim may require failed-run/hostile-profile/resource partitions;
- causal claim may require dispatch/telemetry/physical-observation partitions;
- support-currentness claim may require recovery-test/fallback partitions.

The required profile determines the closure.

A complete cut for one claim does not imply complete evidence for another.

## 23. Evidence cut receipt

A future `EvidenceLedgerCurrentCutReceipt` may bind:

- ledger domain/scope;
- protected head witness;
- exact aggregate checkpoint/cut;
- required-partition profile;
- partition-closure receipt;
- continuity/gap/corruption result;
- replica conflict result;
- producer-authenticity dependencies;
- time/order evidence where material;
- verifier identity/profile;
- final disposition;
- immutable receipt digest.

A `CURRENT_COMPLETE` label without these bound predicates is not sufficient evidence.

## 24. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. restore valid old prefix L16 while protected witness proves L20; L16 cannot become current.
2. restore both ledger and local resolver from L16 backup; absence of independent witness blocks current claim.
3. same local max generation on two different ledger roots; conflict.
4. longer chain omits required negative-evidence partition; closure incomplete.
5. replica with favorable evidence is chosen over conflicting witnessed state; reject.
6. atomic multi-partition profile has only some partitions advanced; combined currentness fails.
7. caller omits inconvenient required partition; required-profile comparison rejects.
8. checkpoint signer authentic but record origins unverified; checkpoint authenticity cannot upgrade origin authenticity.
9. replay ledger restored to UNUSED while evidence witness proves consumed/ambiguous transaction exists; cross-store inconsistency blocks write reuse.
10. historical clean checkpoint is restored after later conflict; remains historical.
11. wall clock rollback makes old retention/cut appear current; witness order dominates.
12. failover replica cannot reconcile to witnessed head; current evidence-dependent protected actions block.
13. compaction drops unresolved ambiguity without qualified tombstone/proof; completeness fails.
14. valid currentness receipt binds L20; ledger advances to L21; old receipt cannot silently claim L21.
15. two individually current partitions are combined even though no admissible cross-partition cut existed; reject combination.
16. learner writes `current_checkpoint=L99` inside the same ledger; self-witness does not establish currentness.

## 25. Practical rule

> Evidence-ledger currentness is the exact uniquely witnessed current cut plus claim-specific required-partition closure. A locally valid chain, maximum generation, readable replica, signed checkpoint, or restored backup cannot by itself prove current complete evidence.

## 26. Authority boundary

This document does not:
- choose a database/storage system;
- create a live witness service;
- configure retention;
- delete or compact evidence;
- implement replication;
- select cryptography;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
