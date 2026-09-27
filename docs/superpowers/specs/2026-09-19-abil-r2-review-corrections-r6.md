# ABIL R2 Review Corrections R6 — Evaluator Equivalence, Resolver Authority, and Coherent Context Cuts

Status: **IP_CONFIDENTIAL / NORMATIVE CORRECTION COMPANION / DESIGN ONLY / NO IMPLEMENTATION AUTHORITY**

Date: 2026-09-19

Applies to the cumulative R2 written-design subject rooted at architecture base `712d5b30b45ba9299dcfce0599878cb81db70e8f` and predecessor PR #3 head `c2e363d4c1b8c67e032c22d9cad6451342b04e7b`.

R6 preserves R5 as historical review provenance and supersedes only the R5 wording addressed below.

## 1. Purpose

R5 correctly made consulted evaluator-only context part of the reproducible experiment subject.

Hostile review identified three residual defects:

1. an evaluator could self-assert that changed hidden context was irrelevant and thereby preserve an equivalence claim;
2. an "independently recomputable" evidence package could expose resolvable evaluator-only objects without an explicit read-authorization boundary;
3. per-object effective-time/currentness metadata did not by itself define one coherent run-level evaluation cut.

R6 closes those defects.

## 2. Experiment identity is strict; equivalence is a separate derived relation

If any consulted evaluator-context manifest digest changes, the resulting run is a **different experiment identity**.

No irrelevance claim may preserve the old experiment identity.

A later system MAY establish a separate relation:

`EvaluatorContextEquivalence(old_run, new_run, claim_scope)`

but that relation is evidence about two distinct experiment subjects. It never rewrites them into one identity.

The equivalence relation MUST bind at least:

- old evaluator-context manifest digest;
- new evaluator-context manifest digest;
- old and new run-manifest digests;
- exact evaluator implementation identity, build/version, and configuration digest;
- exact scoring/fixture/admissibility/negative-control/claim-ceiling profile identities;
- an explicit machine-readable enumeration of every changed evaluator-context field;
- the declared claim scope for which equivalence is being asserted;
- exact proof method;
- verifier identity and verifier-profile/version;
- verification result and evidence digest.

## 3. Irrelevance is not evaluator self-assertion

A changed evaluator-only field is irrelevant to a declared claim only if irrelevance is **mechanically derived** under an independently bound verifier profile.

The evaluator whose result benefits from an equivalence finding MUST NOT establish that finding merely by emitting `irrelevant=true`.

At least one of these proof classes is required:

### 3.1 Dependency/noninterference proof

The verifier establishes that every changed field is outside the complete dependency closure of:

- fixture/corpus selection;
- admissibility/exclusion;
- target construction;
- scoring;
- negative-control interpretation;
- limitation/claim-ceiling derivation;

for the exact evaluator implementation/configuration and claim scope.

The proof binds:
- complete dependency schema/profile identity;
- changed-field set;
- reachable-dependency result;
- verifier identity/profile;
- exact evaluated code/config subjects.

Unknown, dynamic, or unresolved dependency edges fail equivalence.

### 3.2 Deterministic paired replay

The verifier replays both context subjects through the exact same independently bound evaluator implementation/configuration and proves invariant, as applicable:

- selected fixture/corpus identities;
- admissibility/exclusion decisions;
- target construction;
- score inputs;
- scores and tolerances;
- negative-control classifications;
- limitations;
- claim ceiling;
- other claim-relevant evaluator decisions.

The paired-replay evidence binds both complete context manifests and both resulting decision traces.

A changed field that cannot be proven irrelevant by dependency closure or paired replay yields:

`EVALUATOR_CONTEXT_EQUIVALENCE_NOT_ESTABLISHED`

and the runs remain distinct without an equivalence relation.

## 4. No widening through partial equivalence

Equivalence is claim-scoped.

Proof that a changed field cannot affect one metric does not establish equivalence for:
- a different metric;
- fixture selection;
- admissibility;
- a different negative control;
- a broader claim ceiling;
- another evaluator build/configuration.

The equivalence claim cannot be broader than the exact mechanically verified decision surface.

## 5. Evaluator-only object resolution is authorization-scoped

Content addressing proves object identity/integrity. It does **not** grant read authority.

Every evaluator-only context object or content-addressed reference MUST carry or resolve under a classification/access profile that distinguishes at least:

- learner-visible;
- evaluator-only resolvable;
- evaluator-only commitment-only;
- prohibited to the requesting principal.

A learner-visible evidence package MAY contain opaque commitments/digests proving that evaluator-only evidence was bound, but MUST NOT make the protected payload resolvable to the learner merely because the learner possesses the digest or URI.

Resolution of evaluator-only payloads is permitted only inside an authorized evaluator/verifier domain whose identity and access profile are independently bound.

The resolver MUST fail closed when:
- caller/principal identity is missing or unverified where required;
- classification is unknown;
- requested scope exceeds authorization;
- content-addressed object exists but caller lacks read authority;
- resolver/currentness profile is unknown or mismatched.

Digest possession, object existence, or successful hash verification never implies read authorization.

## 6. Independently recomputable evidence has two surfaces

A qualification package claiming `INDEPENDENTLY_RECOMPUTABLE` distinguishes:

### 6.1 Public/learner-safe commitment surface

May include:
- evaluator-context manifest digest;
- opaque evaluator-only object commitments;
- evaluator/verifier implementation and profile identities;
- decision-trace digest;
- equivalence-proof digest;
- result/claim receipt;
- evidence classification metadata.

It MUST NOT expose evaluator-only payloads beyond the requesting principal's authorization.

### 6.2 Authorized evaluator/verifier resolution surface

Contains or resolves:
- exact consulted evaluator-only inputs;
- exact decision traces;
- exact equivalence proof inputs;
- other protected evaluator evidence required for recomputation.

Independent recomputation of protected evaluator semantics therefore requires an authorized verifier principal, not merely possession of the learner-safe package.

"Independently recomputable" describes reproducibility for an authorized verifier under the bound access profile. It does not abolish the learner information firewall.

## 7. Coherent run-level evaluator-context cut

Every run whose evaluator consults current/effective evaluator-only state MUST bind one `EvaluatorContextCut` (or mechanically equivalent subject).

The cut binds:
- run ID / run-manifest digest;
- exact set of required evaluator-context subjects;
- each subject identity, generation/version, digest, and source;
- each subject's effective/currentness interval or ordered state position where defined;
- one declared evaluation as-of semantics;
- exact currentness/verifier profile;
- cut construction method;
- cut digest.

The run MUST NOT construct its semantics from ambient "latest now" reads performed at unrelated times with no join rule.

## 8. Single-cut and deterministic multi-cut semantics

A profile may use either:

### 8.1 Single coherent cut

All required evaluator-context subjects are resolved as of one qualified evaluation cut.

### 8.2 Deterministic multi-cut join

If the system cannot provide one atomic/snapshot cut, the profile MUST define a deterministic join protocol that binds:
- every individual read/cut;
- ordering/version evidence;
- admissible skew/uncertainty where applicable;
- retry/reconciliation rule;
- conflict rule;
- exact final joined-cut digest.

If two required subjects cannot be shown to coexist under the declared join semantics, the run fails currentness/reproducibility for claims depending on them.

No "pick whichever current value is convenient" behavior is permitted.

## 9. Effective-time semantics never repair generation inconsistency

Wall-clock/effective-time information and generation/lineage information solve different problems.

If a newer generation supersedes an older subject, moving a clock backward or choosing an earlier as-of timestamp MUST NOT silently reactivate the older subject unless the exact replay profile explicitly requests historical replay and binds that historical cut.

For live/current evaluation:
- generation/lineage/currentness rules dominate rollback;
- time windows can narrow validity;
- time uncertainty cannot widen validity.

## 10. Revised replay-equivalence rule

R5 Section 4 is superseded by this rule:

Replay/restart equivalence requires:
1. the exact same evaluator-context manifest digest; **or**
2. a separately identified `EvaluatorContextEquivalence` relation established under Sections 2–4.

Even in case (2), old and new runs remain distinct experiment identities.

A missing, stale, self-issued, unverifiable, or over-broad equivalence relation is treated as non-equivalence.

## 11. Revised evidence-package obligation

R5 Section 6 is superseded to require:

- exact run and evaluator-context manifest digests;
- exact `EvaluatorContextCut` digest;
- learner-safe commitment surface;
- authorization-scoped evaluator resolution surface;
- evaluator implementation/build/configuration identities;
- exact scoring/selection/admissibility/negative-control/claim profiles;
- decision-trace digest and authorized trace resolution;
- any `EvaluatorContextEquivalence` relation plus its verifier evidence;
- classification/access-policy identity for every protected resolvable object.

The package MUST demonstrate both:
- **integrity/provenance** of protected evaluator evidence; and
- **authorization scope** for resolving it.

These are independent predicates.

## 12. Hostile acceptance cases

The cumulative R2 qualification suite adds at least:

1. change a consulted evaluator-only field and self-assert `irrelevant=true`; equivalence MUST fail;
2. change a field outside a complete statically/deterministically proven dependency closure; equivalence MAY pass only for the exact verified claim scope;
3. paired-replay old/new contexts and mutate a decision result; equivalence MUST fail;
4. prove metric-only equivalence and attempt to reuse it for a broader claim ceiling; MUST fail;
5. give learner a valid digest/URI for evaluator-only payload with no read authority; resolution MUST fail while commitment verification MAY succeed;
6. give authorized evaluator the same reference under the correct access profile; exact payload resolution and digest verification MUST succeed;
7. assemble context from mutually incompatible subject generations that were never coherent under the declared cut/join; run MUST fail currentness/reproducibility;
8. move wall clock backward after supersession and attempt to revive old live evaluator context; MUST fail;
9. replay an explicitly historical cut under a historical-replay profile; historical result MAY reproduce but MUST remain historical and non-current;
10. mutate verifier profile/build while retaining old equivalence receipt; receipt MUST fail exact-profile binding.

## 13. Composition and authority

R6 is cumulative with the primary R2 design and R1–R5. R6 supersedes R5 only where the wording above directly conflicts.

R6 does not authorize implementation planning, package scaffolding, Hephaestus handoff, live machine access, industrial writes, commissioning, deterministic control, safety classification, product selection, procurement, deployment, merge/canonical promotion, publication/visibility change, licensing change, credential/provider mutation, or another protected effect.

Patrick remains the final authority for protected effects and for the explicit written-design acceptance gate after clean exact-head peer review/reconciliation.
