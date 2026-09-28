# ABIL Protected Head Witness Semantic Primitive V1

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR PROVIDER AUTHORITY**

Date: 2026-09-19

Architecture base:
`712d5b30b45ba9299dcfce0599878cb81db70e8f`

Purpose:

> Define one reusable protected-currentness primitive for replay, evidence, trust, governance-root, and other high-consequence state domains so every subsystem uses the same uniqueness, anti-rollback, authority, and multi-head composition semantics.

This research does not select a database, consensus system, hardware root, quorum technology, provider, or deployment mechanism.

## 1. ProtectedHeadWitness

Conceptual subject:

`ProtectedHeadWitness`

Required fields/semantics include at least:

- domain type;
- domain ID;
- exact scope;
- current successor subject/cut digest;
- predecessor witness digest;
- predecessor witness sequence/generation;
- successor subject generation where the domain uses one;
- writer/ownership generation or equivalent writer-fencing identity where material;
- witness authority/profile identity;
- witness-authority currentness receipt;
- unique-advancement commit receipt;
- commit sequence/generation;
- immutable witness digest.

The witness is not the judged payload itself.

Its rollback/failure domain must be sufficiently independent from the state store it judges that restoring the judged store cannot silently restore currentness.

## 2. Current means uniquely committed head

For a protected domain:

`CURRENT(scope) := candidate_subject_digest == unique_current_witness(scope).successor_subject_digest`

plus all required integrity, authority, scope, conflict, and operation-specific predicates.

No other local property creates currentness.

In particular, currentness is not proven by:
- highest local generation;
- longest local chain;
- newest local timestamp;
- local application pointer;
- successful local write;
- local replica majority without qualified commit semantics;
- valid descendant lineage alone.

## 3. Atomic predecessor-bound unique advancement

A witness advancement MUST bind at least:

`(domain, scope, predecessor_witness_digest, predecessor_witness_sequence, successor_subject_digest, writer_generation, commit_authority_profile)`

and satisfy one semantic property:

> Two incompatible successors from the same exact predecessor cannot both receive the status `CURRENT_COMMITTED` for the same scope.

This may be implemented by:
- atomic compare-and-swap;
- linearizable compare-and-advance;
- quorum/consensus single-head commit;
- another independently qualified mechanism with equivalent semantics.

Technology is open.
The uniqueness property is not optional.

## 4. ProtectedHeadCommitReceipt

A successful witness advancement produces a `ProtectedHeadCommitReceipt` or mechanically equivalent subject binding:

- domain/scope;
- predecessor witness digest/sequence;
- predecessor subject digest;
- successor subject/cut digest;
- successor generation where applicable;
- writer/ownership generation;
- exact commit authority identity/profile;
- required approvals/quorum;
- actual approvals/attestations;
- conflict/predecessor-current check result;
- authority/root/currentness cut used;
- atomic/consensus commit result;
- resulting witness digest/sequence;
- readback verification;
- immutable receipt digest.

A receipt cannot create the commit authority it claims.

## 5. Commit authority is distinct from subject-transition authority

Where the domain also has semantic transition authorization, keep separate:

- authority to approve the semantic successor;
- authority to commit that successor as the unique current head.

A principal may hold one without the other.

Examples:
- trust-state transition authorization vs trust witness commit;
- evidence ingestion/qualification vs evidence-ledger witness commit;
- replay record creation vs replay-head commit.

## 6. Witness authority currentness

The authority/profile permitted to advance a witness must itself be current and independently rooted.

A `WitnessAuthorityReadReceipt` or equivalent should bind:

- authority subject ID/digest;
- authority generation/currentness;
- exact domain/scope permitted;
- allowed commit classes;
- quorum/role policy;
- expiry/currentness constraints;
- root/governance dependency where applicable;
- verifier identity/profile;
- immutable receipt digest.

If witness authority is unknown, stale, revoked, scope-mismatched, or conflicting:
witness advancement fails closed.

## 7. No circular witness authority

The judged store/witness MUST NOT be the sole source of authority that says who may advance that same witness.

Examples to reject:
- replay ledger contains "writer X may advance replay witness," and X uses that row as sole authority;
- trust successor names its own witness-commit authority;
- evidence ledger checkpoint authorizes its own checkpoint head commit;
- governance root being installed is the sole authority validating the commit that makes it current.

The authority chain must terminate in a separately governed/current root appropriate to the domain.

## 8. Authorized candidate versus uniquely current head

Explicit states:

- `CANDIDATE_VALID`;
- `AUTHORIZED_NOT_COMMITTED`;
- `CURRENT_COMMITTED`;
- `SUPERSEDED`;
- `HISTORICAL`;
- `CONFLICTING`;
- `CURRENTNESS_UNRESOLVED`.

A valid or authorized candidate is not current until the protected commit succeeds.

## 9. Concurrent successors

If two actors start from the same predecessor W19:

- candidate A -> successor S20A;
- candidate B -> successor S20B.

Both may be:
- well formed;
- independently authorized.

But both MUST NOT become `CURRENT_COMMITTED`.

At most one can win the predecessor-bound protected commit.

The losing candidate remains:
- historical/authorized-not-committed;
- superseded;
- or conflicting/pending reconciliation according to domain policy.

Do not select the winner by:
- timestamp;
- local arrival order;
- larger successor generation;
- more permissive content;
- whichever replica is currently reachable.

## 10. Split-brain / partition behavior

If the protected witness mechanism cannot guarantee unique advancement during partition:

- affected protected currentness MUST NOT be claimed;
- protected operations depending on currentness block or downgrade;
- historical candidate creation may continue only where policy permits;
- post-partition reconciliation must not retroactively claim both branches were current.

Availability does not outrank unique currentness.

## 11. Readback is part of commit evidence

After successful advancement, a caller relying on the new current head should verify:

- protected witness now binds exact successor;
- predecessor/sequence changed as expected;
- scope/domain unchanged;
- commit receipt matches;
- no known conflict is unresolved.

A local "update succeeded" return without qualified readback is weaker evidence.

## 12. Restore / failover

On restore/failover:

1. local state loads as candidate/historical bytes;
2. protected witness resolves independently;
3. exact subject digest equality to witnessed successor is checked;
4. missing newer state is reconciled/fetched as permitted;
5. candidate descendants not committed by the witness remain non-current;
6. protected operations resume only after exact currentness is re-established.

A backup's embedded witness copy is not sufficient unless the profile proves it is the qualified protected witness itself.

## 13. Same-sequence/different-digest conflict

If the same protected witness sequence/generation appears with incompatible successor digests:

`PROTECTED_HEAD_CONFLICTING`.

Do not resolve by:
- local preference;
- wall time;
- lexical digest order;
- subject generation.

This indicates witness-integrity/currentness failure requiring explicit reconciliation.

## 14. Domain specialization

This primitive supplies common semantics only.

Each domain adds its own closure rules.

### Replay domain
Adds:
- request consumption state;
- target-dedup currentness;
- writer/ownership generation;
- no-blind-replay semantics.

### Evidence domain
Adds:
- required-partition closure;
- ledger continuity/completeness;
- producer authenticity.

### Trust-state domain
Adds:
- transition authorization;
- producer/verifier acceptance semantics;
- governance-root dependency.

### Governance-root domain
Adds:
- external bootstrap/root-transition authority;
- environment/scope separation.

Other domains may reuse the primitive only if their claim semantics fit.

## 15. Multi-head protected operation cuts

Some operations require multiple protected heads simultaneously.

Example:
a physical dispatch may depend on:
- replay head R20;
- evidence head E31;
- trust head T9;
- authority head A12.

The operation profile MUST choose one of two models.

### A. Aggregate protected operation cut

A `ProtectedOperationCutCommit` binds:
- exact required domain/scope set;
- exact ProtectedHeadWitness digest for each;
- operation/claim type;
- currentness/freshness rules;
- one aggregate cut digest;
- commit/currentness semantics.

A protected operation uses the exact aggregate cut.

### B. Explicit independent-head ordering

If heads cannot be atomically aggregated, the profile MUST define:
- required read order;
- which head movements invalidate prior reads;
- required revalidation point;
- admissible partial advancement;
- final dispatch/decision fence;
- resulting multi-head cut receipt.

No arbitrary pair of individually current heads is assumed to form a valid operation cut.

## 16. MultiHeadOperationCutReceipt

A future receipt may bind:

- operation/claim type;
- exact required domain/scope set;
- each ProtectedHeadWitness digest/sequence;
- read/commit order;
- invalidation dependencies;
- freshness/time predicates where required;
- final revalidation result;
- aggregate cut digest;
- verifier identity/profile;
- immutable receipt digest.

This receipt does not grant authority not already present in the bound heads/policies.

## 17. Cross-head invalidation

The operation profile declares whether movement of one protected head invalidates cached reads of another.

Examples:
- replay head movement may invalidate dispatch reservation eligibility;
- evidence head movement may invalidate reconciliation/coverage claims;
- trust head movement may invalidate producer-authenticity evaluation;
- governance-root movement may invalidate witness-authority resolution.

No subsystem invents its own permissive reuse rule.

## 18. Time is subordinate to structural unique currentness

Qualified time may govern:
- expiry;
- freshness;
- scheduled activation;
- holdover.

Time MUST NOT:
- make an uncommitted candidate current;
- choose between two protected-head forks;
- revive a superseded witness;
- replace predecessor-bound unique advancement.

Where temporal validity is required, bind a qualified time cut after structural currentness is established.

## 19. Historical commit versus current commit

A commit receipt may prove that a candidate was committed at a historical cut.

It does not prove the candidate remains current after later witness advancement.

Historical commit truth is preserved.

Currentness always resolves from the current protected head for the exact scope.

## 20. Operation barriers

A downstream protected action may treat witness advancement as a barrier only if:

- the witness mechanism satisfies unique predecessor-bound advancement;
- exact authority/currentness is valid;
- required domain closure passes;
- the action binds the resulting witness/cut receipt;
- any other required heads are coherently bound.

If these are not proven:
the barrier is not qualified for protected effect.

## 21. Hostile acceptance cases

Future implementations/reviews SHOULD cover at least:

1. two authorized writers race from W19; only one incompatible successor can become CURRENT_COMMITTED.
2. both partitions report local success but no qualified single-head commit exists; protected currentness fails.
3. candidate node is valid and higher generation but witness never advances; remains non-current.
4. stale predecessor compare-and-advance attempt after W20 already committed; fails.
5. witness commit authority is stale/revoked; advancement fails.
6. witness store admin lacks semantic commit authority; cannot self-promote state.
7. same witness sequence with different digest; conflict.
8. restore includes S21 but protected witness says S20 because S21 was never committed; S20 remains current.
9. restore includes S20 but witness says S21; S20 historical/stale.
10. local "write succeeded" but readback does not show successor; no CURRENT claim.
11. replay and evidence heads are individually current but operation profile requires aggregate cut that was never committed; dispatch blocked.
12. independent-head profile reads R20/E31; E advances to E32 and profile says replay decision invalidates; revalidation required.
13. wall clock chooses convenient branch after fork; rejected.
14. alias/equivalent subject is locally declared without protected commit; not current.
15. historical commit receipt is replayed as proof of present currentness; rejected.

## 22. Practical rule

> A protected state is current only when its exact subject is the uniquely committed head under a predecessor-bound protected advancement rule whose authority is itself current and independently rooted. Multi-head operations must bind one coherent operation cut rather than assembling convenient individually current states.

## 23. Authority boundary

This research does not:
- implement a consensus/CAS service;
- create or advance a real protected witness;
- mutate credentials/roots/providers;
- authorize machine writes;
- perform failover/recovery;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
