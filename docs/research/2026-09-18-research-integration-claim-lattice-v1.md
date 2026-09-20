# ABIL Research Integration / Claim Lattice V1

Status: **NON-NORMATIVE RESEARCH INTEGRATION MAP / PRIVATE ABIL SOURCE / NO IMPLEMENTATION PLAN / NO MERGE OR DEPLOY AUTHORITY**

Date: 2026-09-18

Architecture base:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Purpose:

> Make the growing ABIL research chain reviewable as one evidence/claim system without turning research dependencies into implementation authority or merge order.

This file does not replace any source PR.
It records how their claims compose.

## 1. Authority / design anchors

### PR #2 — successor architecture

Exact subject:
`712d5b30b45ba9299dcfce0599878cb81db70e8f`

Role:
- architectural separation;
- lifecycle/authority contract;
- typed intervention/evidence records;
- field validation roadmap;
- orthogonal state axes.

Status:
- frozen exact-head architecture review pending.

### PR #3 — R2 written design / R5 correction

Exact subject:
`c2e363d4c1b8c67e032c22d9cad6451342b04e7b`

Role:
- written-design gate for R2 substrate/reconstruction path.

Critical governance rule:

> If exact-head peer review/reconciliation becomes clean, stop before implementation planning and obtain Patrick's explicit final written-design acceptance.

### PR #6 — write-capability admission design

Exact subject:
`b191822ecbc95ce120384acf1c17289b4b834033`

Disposition:
`DESIGN_GOVERNANCE_CONTRACT_PASS`

Role:
- exact write-admission subject;
- current authority receipt semantics;
- freshness/canonicalization/profile binding;
- multi-surface reconciliation;
- exact current safety/commissioning/coverage/artifact/fence requirements.

Important:
PR #6 PASS does not imply executable validator, deployment authority, commissioning authority, or machine write authority.

## 2. Evidence / qualification research layer

### PR #4 — component evidence scope/currentness

Exact subject:
`cd4f811ec9318231a3864fcedf4cd67befab07a7`

Role:
- direct third-party versus composition-dependent versus ABIL-owned versus machine-application evidence;
- component evidence invalidation;
- derived claim cannot outrank weakest required dependency.

Feeds:
- product/currentness dimension;
- PR #9 cross-axis consistency;
- PR #11 non-authority currentness proof.

### PR #5 — source-optional reconstruction benchmark

Exact subject:
`385207c1bff5189651c1048f2d09f3805d751873`

Role:
- falsifiable source-optional reconstruction research;
- synthetic fixture/preregistration;
- evidence package;
- competent baselines;
- hostile benchmark validation.

Evidence ceiling:
- reconstruction research only;
- `REPLACEMENT_CONTROL_READY` is non-awardable.

Feeds:
- research validity/falsifiability;
- future evidence claims, not write authority.

## 3. State-currentness research layer

### PR #7 — deployment commissioning currentness

Exact subject:
`a62ae16a0c1bc484ae6b45e4af853af64a2e6707`

Role:
- machine/deployment-specific commissioning currentness;
- semantic mapping, commissioning envelope, control coverage, target behavior, cutover, recovery evidence;
- partial/full recommission.

Key rule:
same topology does not prove same commissioned behavior.

### PR #8 — support/recovery currentness

Exact subject:
`7d11cea51bfff3f2bf32e98516479be4d742d172`

Role:
- manual recovery;
- artifact rollback;
- appliance restore;
- hardware replacement;
- degraded operation;
- non-operating fallback currentness.

Key rule:
restoring bytes must not restore authority.

### PR #9 — cross-axis consistency

Exact subject:
`90d40f4baca29629f8f17f956f20687fee674820`

Role:
- evaluates:
  `OperationalStateVector = (product, deployment, authority, artifact, recovery)`;
- no cross-axis implication by default;
- operation-specific predicates;
- ownership/fencing, ambiguous-transaction, safety overlays;
- coherent currentness cut.

Depends conceptually on:
- PR #4;
- PR #6;
- PR #7;
- PR #8;
- PR #2 lifecycle/artifact contracts.

### PR #10 — dependency-cycle resolution

Exact subject:
`5e15ed24fc5f9286eb21377e0532f6d88e8a1840`

Role:
- prevents deployment/recovery or other state axes from mutually self-justifying currentness;
- exact dependency graph;
- SCC detection;
- independent leaf evidence;
- directly qualified joint bundles;
- exact subject generations.

Key rule:
mutual dependency is allowed; mutual self-justification is not.

Strengthens:
- PR #9;
- PR #7/#8 composition.

### PR #11 — non-authority currentness proof

Exact subject:
`fcb0a88b0a37a9c7c722fe0e5f966a7a3f968bc3`

Role:
- machine-checkable currentness for deployment/coverage/recovery/safety/product evidence;
- digest identity != currentness;
- currentness receipts;
- independent invalidation/freshness profiles;
- self-attestation boundary.

Important:
does not reopen PR #6 PASS.

Feeds:
- future machine-checkable realization of PR #6's already-required currentness predicates.

### PR #12 — snapshot / dispatch revalidation

Exact subject:
`3d61f4da301af41f4d56bbcffb4609c38b815bd3`

Role:
- decision-time versus dispatch-time TOCTOU;
- required-subject read set/version vector;
- authority/deployment/artifact/ownership/recovery/safety/ambiguity races;
- dispatch-time revalidation.

Key rule:
an admissibility decision is valid only for the exact checked vector while that vector remains current.

Depends conceptually on:
- PR #6;
- PR #9;
- PR #10;
- PR #11.

## 4. Physical transaction-safety research layer

### PR #13 — effect-intent binding / anti-replay

Exact subject:
`8ab8ee9e95c86a04c4d34a8042e13b05979d6364`

Role:
- exact request/effect intent;
- parameters/units;
- request-ID uniqueness;
- execution cardinality;
- batch/session semantics;
- replay protection.

Key rule:
write admission is not a generic reusable bearer token.

Depends conceptually on:
- PR #6;
- PR #12;
- PR #2 transaction semantics.

### PR #14 — replay-ledger anti-rollback

Exact subject:
`fc9846e3eb82e3b0c8eccbf42769b09ba7eaaa2c`

Role:
- consumed requests cannot become unused after restore;
- replay ledger generation;
- same-authority-generation restore;
- target dedup requirements;
- HA/failover/session/batch replay state.

Key rule:
replay/consumption state must not become less restrictive after recovery.

Depends conceptually on:
- PR #8;
- PR #12;
- PR #13.

### PR #15 — dispatch commit ordering

Exact subject:
`88f1a232a7265e8713e4564260b28e35cf53369e`

Role:
- durable pre-dispatch reservation;
- crash windows around send/accept/receipt persistence;
- conservative "effect may occur" state;
- known-no-effect proof;
- transactional/non-transactional target limits;
- WAL/HA/storage durability boundary.

Key rule:
durable replay state crosses its conservative commit point before non-idempotent physical effect can become possible.

Depends conceptually on:
- PR #12;
- PR #13;
- PR #14.

### PR #16 — execution evidence / causal attribution

Exact subject:
`ac36991d6c54dfa870aca7c64d05a980a034c10c`

Role:
- evidence ladder:
  dispatch -> delivery -> acceptance -> target report -> readback -> physical observation -> causal attribution;
- target receipt semantics;
- competing causes;
- learner/evaluator label separation;
- control-coverage evidence classes.

Key rule:
execution, observation, and causation are separate evidence layers.

Depends conceptually on:
- PR #13/#15 exact transaction identity;
- PR #2 typed evidence architecture.

### PR #17 — transaction reconciliation / late evidence

Exact subject:
`1837c6b6c47225fd02674ea7e735caef0f83e97b`

Role:
- later evidence may narrow historical ambiguity;
- immutable historical transaction identity;
- no return to `UNUSED`;
- retry eligibility remains separate;
- conflict/partial-effect preservation;
- cross-generation late evidence isolation.

Key rule:
reconciliation refines historical knowledge; it does not rewrite transaction identity or manufacture current authority.

Depends conceptually on:
- PR #14;
- PR #15;
- PR #16.

### PR #18 — evidence-ledger integrity / continuity

Exact subject:
`8d7ffe6650136b7a2037206da75a665235324a16`

Role:
- record integrity != ledger completeness;
- detectable truncation/gaps/selective restore;
- negative/conflicting evidence preservation;
- replicas/restore/compaction/tombstones;
- producer identity;
- claim binding to exact ledger cuts.

Key rule:
valid individual records are insufficient if the required surrounding history can be silently omitted.

Cross-cuts:
- PR #11 currentness proof;
- PR #12 snapshot decisions;
- PR #14 replay state;
- PR #16 execution evidence;
- PR #17 reconciliation;
- PR #5 benchmark integrity.

## 5. Dependency graph

Conceptual high-level graph:

```text
PR2 architecture
 |------------------------------|
 |                              |
 v                              v
PR4 product evidence           PR5 reconstruction research
 |
 v
PR7 deployment ----                    PR8 recovery --------> PR9 cross-axis consistency
                            |
PR6 write admission --      v
                       -> PR10 cycle-safe dependencies
                               |
                               v
                            PR11 currentness proof
                               |
                               v
                            PR12 snapshot/revalidation
                               |
                               v
                            PR13 exact effect intent
                               |
                    PR8 ------>PR14 replay anti-rollback
                               |
                               v
                            PR15 dispatch commit ordering
                               |
                               v
                            PR16 execution/causal evidence
                               |
                               v
                            PR17 late reconciliation

PR18 evidence-ledger integrity cross-cuts PR5/11/12/14/16/17.
```

This is not a merge order.

It is a claim-dependency map.

## 6. No PASS inheritance

A PASS or clean review on one subject does not automatically transfer.

Examples:

- PR #6 PASS does not imply PR #11 currentness-proof design is correct.
- PR #13 review does not imply PR #14 replay persistence is correct.
- PR #15 review does not imply exactly-once physical execution.
- PR #16 review does not imply causal attribution is always resolvable.
- PR #18 review does not prove a future storage implementation preserves ledger integrity.
- PR #5 benchmark quality does not prove ABIL wins the benchmark.

## 7. Exact-head rule

Every review disposition binds the exact reviewed head.

If a head moves:
- old review becomes provenance;
- new exact head requires fresh review for current credit.

Do not carry PASS/FAIL forward by PR number alone.

## 8. Review types are distinct

Keep separate:

### source-owner audit

Can identify/reconcile internal composition findings.

Does not count as independent peer review.

### independent peer review

Exact-head external/peer assessment.

### reconciliation

Disposition after exact-head peer returns.

### Patrick authority

Required for protected effects and the PR #3 written-design acceptance gate.

These are not interchangeable.

## 9. Invalidation propagation

Examples:

### If PR #10 fails

Affected:
- cross-axis currentness compositions involving cycles;
- PR #11/12 claims that rely on cycle-safe dependency closure.

Unaffected automatically:
- PR #6 authority receipt design;
- PR #13 effect-intent identity mechanics that do not depend on cyclic currentness.

### If PR #14 fails

Affected:
- replay safety across restore/failover;
- PR #15 assumptions about durable replay state;
- PR #17 no-return-to-unused historical semantics.

Does not automatically refute:
- PR #13 exact effect-intent binding.

### If PR #16 fails

Affected:
- physical-effect/causal claim grading;
- PR #17 reconciliation evidence ceilings;
- control-coverage upgrades based on interventions.

Does not automatically invalidate:
- dispatch anti-replay mechanics.

### If PR #18 fails

Affected:
- any stronger claim requiring complete historical evidence;
- currentness/reconciliation/replay claims that assume ledger continuity.

Does not prove individual record bytes are invalid.

## 10. Evidence ceilings

### Design/governance
PR #6:
- written contract only.

### Research
PR #4/#5/#7–#18:
- non-normative research subjects;
- no executable proof;
- no current implementation qualification.

### Architecture
PR #2:
- architecture subject;
- no merge/deploy authority.

### Written design
PR #3:
- subject to explicit Patrick acceptance after clean peer/reconciliation.

## 11. Protected-effect boundary

None of PR #2–#18 authorizes:

- merge/canonical promotion;
- implementation planning after the PR #3 clean-review hard gate without Patrick acceptance;
- production deployment;
- machine connection/write;
- commissioning authority;
- product selection/procurement/license acceptance;
- credential/provider mutation;
- visibility/publication change;
- safety ownership.

## 12. Review queue at this integration cut

Pending exact-head peer/reconciliation subjects:

- PR #2 — architecture;
- PR #3 — R5 written design;
- PR #4 — component evidence;
- PR #5 — benchmark research;
- PR #7 — deployment currentness;
- PR #8 — recovery currentness;
- PR #9 — cross-axis;
- PR #10 — cycle resolution;
- PR #11 — non-authority currentness proof;
- PR #12 — snapshot/revalidation;
- PR #13 — effect intent;
- PR #14 — replay anti-rollback;
- PR #15 — dispatch ordering;
- PR #16 — execution evidence;
- PR #17 — late reconciliation;
- PR #18 — evidence-ledger integrity.

PR #6 remains design-contract PASS unless exact head or a materially new finding changes its disposition.

## 13. Highest-value decision frontier

Before implementation planning, the highest-value gating chain remains:

1. independent exact-head review of PR #3;
2. One reconciliation;
3. if clean: Patrick explicit final written-design acceptance;
4. only then may implementation planning be considered.

Research PRs can continue to inform risk/evidence design without bypassing that gate.

## 14. Research disposition

The practical integration rule is:

> Treat ABIL's current research as a dependency lattice of bounded claims, not as one accumulating "ready" score.

This integration map creates no implementation authority, merge authority, machine authority, deployment authority, or acceptance decision.
