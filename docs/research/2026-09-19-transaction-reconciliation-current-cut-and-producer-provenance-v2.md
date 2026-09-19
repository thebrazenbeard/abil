# Transaction Reconciliation Current-Cut and Producer-Provenance Composition V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #17 predecessor exact head `1837c6b6c47225fd02674ea7e735caef0f83e97b`.

This companion reconciles Transaction Reconciliation and Late Evidence V1 with:
- PR #14 replay-ledger protected currentness;
- PR #15 protected dispatch-reservation barrier;
- PR #18 evidence-ledger protected current cut;
- PR #20 producer-chain authenticity;
- PR #24 time-source currentness/order.

The central question is:

> How does a system select the current historical reconciliation disposition without letting stale restores, forged reviewers, selectively missing evidence, or convenient timestamps rewrite the transaction story?

## 1. Reconciliation is an append-only interpretation chain

A transaction's historical reconciliation should form an immutable chain:

`R0 -> R1 -> R2 -> ...`

Each resolution generation binds:
- original transaction identity;
- predecessor resolution digest;
- newly considered evidence digests;
- reviewer/evaluator identity;
- physical-effect disposition;
- causal disposition;
- uncertainty/conflict;
- evidence ceiling;
- exact evidence-ledger cut;
- time/order evidence where material;
- resulting resolution digest.

A later resolution supersedes interpretation.
It does not erase predecessors.

## 2. Current reconciliation must derive from current evidence cut

If reconciliation records live inside the PR #18 evidence ledger, do not create a separate mutable "current resolution" pointer as the sole authority.

The active historical disposition should be derived from:
- current `EvidenceLedgerHeadWitness`;
- exact required-partition profile;
- complete current evidence cut;
- immutable resolution lineage for the transaction;
- exact selection/supersession profile.

A locally highest resolution generation is not enough if the evidence ledger itself may be stale.

## 3. Separate store rule

If reconciliation state is physically/administratively stored outside the protected evidence ledger, that separate store MUST have an equivalent independently protected anti-rollback current-head mechanism.

Do not rely on:
- local max resolution number;
- newest timestamp;
- database row marked current;
- cache pointer;
- restored application state.

The design should prefer reuse of PR #18 evidence-ledger currentness where the reconciliation history is already part of that ledger.

## 4. Reconciliation selection receipt

A future `TransactionReconciliationSelectionReceipt` may bind:

- transaction identity;
- exact current EvidenceLedgerHeadWitness digest;
- exact evidence-cut/partition-closure digest;
- complete resolution-chain digest;
- selected current resolution digest;
- superseded resolution set;
- producer-authenticity receipts for newly relied-on evidence;
- reviewer/evaluator authenticity receipt;
- time/order cut where material;
- unresolved conflicts;
- final historical disposition;
- verifier identity/profile;
- immutable receipt digest.

This receipt does not grant current write authority.

## 5. Evidence completeness precedes stronger reconciliation

A later conclusion cannot become stronger merely because inconvenient evidence is absent from the restored/current view.

Before selecting:
- `KNOWN_NO_EFFECT`;
- `KNOWN_EFFECT_OCCURRED`;
- a stronger causal conclusion;

the required evidence profile must prove the relevant partitions/cuts are complete enough for that claim.

An `EVIDENCE_GAP_UNKNOWN` or incomplete partition closure caps the reconciliation result.

## 6. Producer authenticity is claim-specific

Late evidence may come from:
- target/device;
- gateway;
- sensor;
- technician;
- evaluator;
- recovery log;
- target-side transaction store.

Each item keeps its PR #20 producer-chain ceiling.

Examples:
- authenticated gateway envelope does not automatically prove device origin;
- technician identity does not prove independent causal analysis;
- target receipt authenticity does not automatically prove physical effect;
- authenticated evaluator does not automatically prove evaluator independence.

Reconciliation cannot upgrade producer evidence beyond its established class.

## 7. Reviewer authenticity and reviewer authority are distinct

A reconciliation reviewer may be authentically identified yet still lack authority for a given resolution class.

Bind separately:
- reviewer identity/authenticity;
- reviewer role;
- deployment/scope;
- evidence class allowed;
- independence profile where required;
- current governance/trust cut.

An authenticated learner/candidate still cannot become an independent reconciliation authority.

## 8. Late receipt exact-subject binding

A delayed receipt must bind the exact historical:
- request ID;
- effect-intent digest;
- dispatch reservation/commit receipt;
- attempt/correlation ID;
- target identity/session;
- authority/ownership generation;
- relevant protocol semantics.

If any required identity dimension mismatches or is unresolved:
do not attach it to the transaction by convenience.

## 9. Cross-generation evidence isolation

Late evidence may arrive after:
- authority epoch change;
- ownership transfer;
- artifact change;
- deployment recommission;
- target replacement;
- trust rotation.

It may refine the old transaction only if identity linkage remains exact.

It MUST NOT:
- satisfy a current request;
- grant current authority;
- reactivate old ownership;
- validate the new target merely because address is unchanged.

## 10. Reconciliation and replay state

A transaction that crossed the protected dispatch-reservation barrier does not return to `UNUSED`.

Even after `KNOWN_NO_EFFECT`:
- historical transaction remains consumed/reserved history;
- any new physical attempt needs a current decision/request unless the exact qualified recovery contract explicitly reuses the same logical transaction.

PR #14 current replay witness remains independently required.

## 11. KNOWN_NO_EFFECT ceiling

`KNOWN_NO_EFFECT` requires evidence appropriate to the exact target/transport semantics.

Potential proof classes:
- target durable transaction state proves no commit/effect;
- protected gateway/transport evidence proves effect boundary never crossed;
- independently qualified physical/process evidence proves no effect possible;
- qualified target prepare cancellation proves no commit.

Not sufficient by itself:
- missing acknowledgement;
- missing telemetry;
- stale restored logs;
- operator expectation;
- timeout.

## 12. KNOWN_EFFECT_OCCURRED ceiling

`KNOWN_EFFECT_OCCURRED` requires evidence that supports actual physical effect under the exact operation profile.

Target `SUCCESS` may remain:
`TARGET_REPORTS_EFFECT`
if target semantics do not independently prove physical effect.

A later state consistent with the requested effect may remain:
`PHYSICAL_OBSERVATION_CONSISTENT`
when competing causes are unresolved.

## 13. Causal resolution stays separate

Physical effect disposition and downstream causal attribution remain distinct.

A reconciliation record binds both separately.

Examples:
- valve opening may be known;
- pressure change may be observed;
- causal link may remain uncertain due to other active pathways.

A stronger physical-effect result does not automatically strengthen causal attribution.

## 14. Time/order evidence cannot repair identity gaps

Late-evidence ordering may use:
- qualified source event time;
- receive time;
- target sequence;
- gateway sequence;
- monotonic session order;
- ledger order.

A convenient timestamp cannot:
- bind receipt to wrong request;
- resolve producer identity;
- prove current trust;
- prove causation.

PR #24 time-source uncertainty rules apply when temporal boundaries matter.

## 15. Intervening-event closure

Before attributing late physical state to an old transaction, the claim profile should account for material intervening events.

If the current evidence cut does not establish whether intervening commands/effects occurred, causal attribution is capped.

Do not infer:
"state matches old command, therefore old command caused it."

## 16. Resolution conflict

If two admissible evidence sets support incompatible reconciliation conclusions:

`RECONCILIATION_CONFLICTING`

Do not:
- choose newest by timestamp alone;
- choose higher resolution generation alone;
- choose the conclusion that permits retry;
- discard inconvenient reviewer/evidence source.

Conflict remains append-only evidence until resolved by a stronger qualified process.

## 17. Resolution rollback detection

Restore/failover must not silently select R1 if the current witnessed evidence cut contains R3.

If:
- current evidence witness proves later resolution chain;
- local application state points to older resolution;

then local selection is stale.

The old resolution remains historical provenance, not current historical disposition.

## 18. Partial-effect representation

For partial effects bind:
- requested extent;
- observed/established extent;
- unknown extent;
- evidence class;
- target/physical/cause distinctions;
- affected batch/session counters.

Do not collapse partial effect into:
- no effect;
- full completion;
- generic failure.

## 19. Batch/session reconciliation

For batches/sessions preserve:
- exact member/sequence identity;
- per-member resolution;
- reserved/dispatched/known/ambiguous counts;
- remaining budget;
- evidence cut used;
- cross-member dependency.

Final machine state does not prove every member succeeded.

## 20. Coverage/model updates are downstream claims

Reconciliation may feed:
- control coverage;
- machine model;
- fault model;
- commissioning evidence.

Those downstream updates must bind:
- exact reconciliation selection receipt;
- evidence class/ceiling;
- scope;
- invalidation dependencies.

A reconciliation result does not automatically widen executable authority.

## 21. Garbage collection

Reconciliation history remains required while it can affect:
- replay safety;
- unresolved ambiguity;
- causal attribution;
- coverage/model claims;
- delayed receipt correlation;
- audit/root cause.

GC must bind a current witnessed evidence cut and a qualified irrelevance/retention rule.

Wall-clock age alone is not enough where ambiguity remains operationally relevant.

## 22. Historical versus current authority

A reconciliation result may become historically better supported over time.

That never creates:
- current write authority;
- current ownership;
- current commissioning;
- current artifact selection;
- current safety authority.

Historical truth and current operational authority remain separate axes.

## 23. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. restore evidence ledger before R3 and local pointer selects R1; current witness proves R3 => R1 cannot become current disposition.
2. forged learner record shaped like evaluator reconciliation; producer/role check rejects stronger authority.
3. authenticated gateway late receipt is treated as device-signed origin; origin ceiling blocks.
4. target success upgrades directly to physical effect without target-semantics proof; reject stronger disposition.
5. missing conflicting partition after selective restore makes KNOWN_NO_EFFECT look clean; completeness gap blocks.
6. old receipt attaches to newer same-address target after replacement; identity mismatch blocks.
7. transaction becomes UNUSED after KNOWN_NO_EFFECT; replay semantics reject.
8. wall-clock timestamp makes old receipt seem temporally convenient but correlation ID mismatches; identity wins.
9. two valid reviewers disagree; do not choose by newest timestamp/generation.
10. physical state matches old command after intervening actions are unknown; causal conclusion remains capped.
11. historical resolution arrives after ownership transfer and mutates current authority; reject cross-axis promotion.
12. final batch state causes all members to be labeled completed; preserve per-member evidence.
13. garbage collection removes prior conflicting resolution while claim still depends on it; reject completeness/currentness.
14. authenticated reviewer lacks scope/role for safety reconciliation; reject role substitution.
15. current evidence witness advances with new contradiction; old selection receipt cannot silently remain current.
16. separate reconciliation store rolls back while evidence ledger is current; separate store needs protected currentness or derivation from ledger.

## 24. Practical rule

> The current historical reconciliation disposition is the strongest claim supportable from the complete, currently witnessed evidence cut and authenticated producer/reviewer chain for that exact transaction. Reconciliation may refine history, but it cannot erase prior uncertainty, revive request reuse, or create current operational authority.

## 25. Authority boundary

This document does not:
- implement reconciliation;
- select reviewer identities;
- configure trust;
- modify replay/evidence storage;
- retry machine actions;
- authorize writes;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
