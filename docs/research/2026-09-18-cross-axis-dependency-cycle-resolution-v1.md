# Cross-Axis Dependency Cycle Resolution V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related research subjects:
- Draft PR #7 — deployment commissioning currentness
- Draft PR #8 — support/recovery currentness
- Draft PR #9 — cross-axis state consistency

## Purpose

A composition audit across PR #7, PR #8, and PR #9 exposed a real dependency-cycle seam.

Deployment commissioning can depend on support/recovery evidence.

Support/recovery can depend on deployment commissioning evidence.

Those dependencies are individually reasonable, but together they create a dangerous possibility:

> Axis A is treated as current because Axis B is current, while Axis B is treated as current because Axis A is current.

No pair or group of state axes may bootstrap itself into currentness through mutual references.

This research defines cycle-safe evaluation principles for cross-axis currentness.

## 1. Dependency graph

Model currentness dependencies as a directed graph:

`CurrentnessDependencyGraph = (subjects, dependency_edges)`

Each node is an immutable evidence/currentness subject.

Each edge means:

> This subject's currentness/admissibility depends on that exact subject or predicate.

Edges should bind:

- source subject ID/digest;
- target subject ID/digest;
- dependency type;
- requested operation/capability scope;
- required predicate;
- currentness generation/version;
- provenance;
- optionality;
- invalidation behavior.

A human-readable label such as `RECOVERY_READY` is not enough.

## 2. No circular proof

A dependency cycle cannot prove itself.

Invalid pattern:

`DeploymentCurrent <- RecoveryCurrent <- DeploymentCurrent`

If no independently established evidence enters that cycle, the cycle is unsupported.

Expected outcome:

`DENIED_CYCLIC_CURRENTNESS`

or equivalent.

## 3. Leaf evidence

A currentness decision should ultimately ground required predicates in evidence that does not depend on the conclusion being established.

Examples of leaf evidence:

- immutable hardware identity readback;
- independently verified firmware/configuration digest;
- technician maintenance record;
- direct I/O mapping verification;
- qualified product evidence;
- separately rooted authority grant;
- independently verified promotion receipt;
- recovery exercise result;
- controlled commissioning replay;
- preserved safety-classification record.

Leaf evidence may itself have freshness requirements.

## 4. Operation-specific dependency slicing

Not every operation requires every axis or every predicate.

Examples:

### Read-only diagnostics

May require:
- current product capability for read-only adapter;
- target/deployment identity;
- no write authority;
- no recovery predicate.

### Manual recovery action

May require:
- current product capability;
- current deployment semantic mapping for affected I/O;
- current manual-recovery capability;
- current authority/ownership where the action writes;
- no unresolved blocking safety/ambiguity condition.

It does not automatically require direct-control artifact currentness.

### Production direct control

May require:
- current product qualification;
- current deployment commissioning;
- current authority;
- current promoted artifact;
- required recovery/fallback readiness;
- current ownership/fencing;
- applicable safety/noninterference state.

Dependency evaluation should therefore slice the graph for the exact requested operation.

## 5. Strongly connected components

A future checker should detect strongly connected components (SCCs) in the required dependency graph.

An SCC with more than one node, or a self-loop, requires explicit treatment.

Allowed outcomes:

### `SCC_GROUNDED`

The cycle is acceptable because one or more independent leaf-evidence predicates establish the shared invariant without assuming any member's currentness.

### `SCC_JOINTLY_QUALIFIED`

The members were qualified together as one immutable bundle under a test/procedure that established the joint invariant directly.

### `SCC_UNGROUNDED`

The cycle depends only on mutual references.

Expected:
deny currentness/admissibility.

A cycle is not safe merely because every node says `CURRENT`.

## 6. Joint qualification bundle

Some dependencies are inherently mutual.

Example:
- deployment fallback policy and recovery procedure may need to be validated together.

A future joint subject could bind:

- exact deployment subject;
- exact recovery subject;
- exact product/runtime subject;
- exact artifact subject where applicable;
- test procedure;
- evidence set;
- independent preconditions;
- resulting operating envelope;
- resulting fallback/recovery envelope;
- currentness generation;
- invalidation dependencies.

The bundle must establish the combined invariant directly.

It must not just wrap mutually self-asserted statuses.

## 7. Independent generations

Each currentness-bearing subject should have an immutable identity and preferably a monotonic generation/version within its domain.

Examples:
- deployment evidence generation;
- recovery evidence generation;
- product qualification generation;
- artifact lifecycle generation;
- authority epoch.

Cross-axis evaluation should bind exact generations, not only latest labels.

A later generation on one axis does not automatically refresh dependent older generations.

## 8. Freshness and generation are different

A subject can be:
- latest generation but stale;
- older generation but still historically valid;
- current within a declared envelope;
- superseded but retained for audit.

Generation establishes ordering/identity.

Freshness establishes whether the evidence may still be relied upon now.

Do not collapse them.

## 9. Coherent currentness cut

A currentness cut must include mutually compatible subject generations.

Example:

- product P3;
- deployment D7;
- authority A12;
- artifact C5;
- recovery R4.

The cut is valid only if every required dependency edge among these exact subjects is satisfied.

Mixing:
- D7 that depends on R5,
with
- R4 because it was "last known good"

is inconsistent even if both individually report current.

## 10. Historical-cut mismatch

A common failure is mixing facts from different historical moments.

Example:

- deployment D5 was current with recovery R3;
- recovery later advanced to R4 after hardware replacement;
- deployment was not recommissioned after that replacement.

Using D5 + R4 as one "current" pair is not justified merely because both subjects were individually valid at different times.

Expected:
`DENIED_AXIS_MISMATCH` or `DENIED_INCOHERENT_CURRENTNESS_CUT`.

## 11. Dependency invalidation propagation

When subject X changes:

1. create new immutable subject X';
2. identify direct dependents;
3. invalidate/review only affected dependency edges;
4. recompute affected SCCs;
5. recompute admissibility for requested operations;
6. preserve unaffected subjects;
7. preserve historical cuts.

Do not mutate historical evidence in place.

## 12. Partial recommission and recovery

PR #7 and PR #8 both allow partial re-establishment.

Cycle-safe rule:

A partial update may preserve unaffected predicates only when:

- dependency edges identify them;
- the retained predicates do not depend on the changed subject;
- no SCC becomes ungrounded;
- the requested operation's exact slice remains complete.

"Partial passed" must not become "whole axis current."

## 13. Recovery/deployment cycle example

Suppose:

- deployment D7 requires fallback policy F2 and manual recovery mapping M3;
- recovery R4 requires deployment semantic mapping S8 and commissioning envelope E5.

Safe evaluation may ground:

- S8 from direct channel verification;
- E5 from independent commissioning constraints;
- F2 from target fallback test;
- M3 from manual recovery exercise.

Then D7 and R4 may be jointly consistent.

Unsafe evaluation:

- D7 says recovery R4 is current;
- R4 says deployment D7 is current;
- no independent evidence is checked.

That is circular proof.

## 14. Authority must remain externally rooted

Authority is special.

No cross-axis SCC may include an edge that allows deployment, artifact, recovery, or product state to manufacture authority currentness.

Authority remains separately rooted in current authority/admission evidence.

A cycle involving authority can depend on authority, but it cannot prove authority.

## 15. Safety must remain externally scoped

Likewise, ordinary ABIL state cannot self-prove safety ownership/classification.

Safety-classification evidence may be a leaf dependency for ordinary operation.

It must not be generated merely because the operational state vector is otherwise coherent.

## 16. Ambiguous transaction constraints

An unresolved ambiguous transaction is not an axis that can be made current.

It is a blocking condition/predicate.

A dependency graph should carry:

`NO_BLOCKING_AMBIGUOUS_TRANSACTION`

or an operation-specific equivalent where required.

No SCC or currentness cut can erase unresolved physical ambiguity.

## 17. Time-of-check / time-of-use

Cycle-safe evaluation also needs freshness at dispatch.

A graph that was coherent at decision time can become invalid if:

- authority revokes;
- deployment generation changes;
- recovery generation changes;
- ownership transfers;
- artifact supersedes;
- safety classification changes.

A decision receipt should not be indefinitely reusable.

## 18. Hostile research cases

A future checker should fail closed on at least:

1. deployment current only because recovery current, recovery current only because deployment current;
2. a wrapper "joint receipt" merely restates two mutual CURRENT flags without independent evidence;
3. currentness cut mixes deployment generation D7 with recovery generation R4 when D7 depends on R5;
4. newer recovery generation silently refreshes older deployment evidence;
5. partial recommission marks full deployment axis current;
6. partial recovery retest marks all recovery capabilities current;
7. SCC includes authority and treats mutual consistency as authority proof;
8. ordinary state vector is used to prove safety classification;
9. unresolved ambiguous physical action omitted from dependency slice;
10. dependency edge exists but exact subject generation is not bound;
11. timestamps match but subject generations are incompatible;
12. newest generation is assumed fresh without freshness evidence;
13. cached currentness cut reused after one SCC member changes;
14. one cycle member is revoked/superseded but other members remain green;
15. a historical jointly qualified bundle is reused after one member's identity changes.

## 19. Review / denial semantics

Suggested research denial reasons:

- `DENIED_CYCLIC_CURRENTNESS`
- `DENIED_UNGROUNDED_SCC`
- `DENIED_INCOHERENT_CURRENTNESS_CUT`
- `DENIED_DEPENDENCY_GENERATION_MISMATCH`
- `DENIED_STALE_DEPENDENCY`
- `DENIED_UNKNOWN_DEPENDENCY`

A denial should identify the exact missing or circular predicate.

## 20. Research disposition

The practical rule is:

> Mutual dependency is allowed; mutual self-justification is not.

Cross-axis currentness should be derived from an exact operation-specific dependency graph whose cycles are either independently grounded or jointly qualified under direct evidence.

No dependency-checker implementation, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
