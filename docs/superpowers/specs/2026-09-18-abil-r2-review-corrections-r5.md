# ABIL R2 Review Corrections R5 — Evaluator-Context Reproducibility

Status: **IP_CONFIDENTIAL / NORMATIVE CORRECTION COMPANION / DESIGN ONLY / NO IMPLEMENTATION AUTHORITY**

Date: 2026-09-18

Applies to the cumulative R2 written-design subject rooted at architecture base `712d5b30b45ba9299dcfce0599878cb81db70e8f` and predecessor PR #3 head `c31d760a711dfd36c00ef9f40a7036b2b1701f45`.

## 1. Purpose

R4 correctly excludes future authority, safety-classification, commissioning, promotion, and active-artifact state from learner-visible R2 evidence by default.

That information firewall is necessary but not sufficient for reproducible evaluation.

If evaluator-side fixture selection, admissibility, scoring, negative-control interpretation, or claim ceilings consult non-learner-visible control context, then that consulted context is part of the experiment subject even though it must remain hidden from the learner.

R2 therefore adds an explicit evaluator-context binding requirement.

## 2. Evaluator-context manifest

Every qualification or efficacy run whose evaluator consults non-learner-visible control/deployment context MUST emit or content-address an `EvaluatorContextManifest` (or mechanically equivalent receipt subject).

For every consulted evaluator-only input, the manifest binds at least:

- exact source/object class;
- exact identity and generation/version where defined;
- immutable digest or content-addressed reference;
- role classification equivalent to `EVALUATOR_ONLY`;
- currentness / effective-time / as-of semantics;
- provenance sufficient to determine where the value came from;
- whether the value affected fixture/corpus selection;
- whether the value affected admissibility or exclusion;
- whether the value affected scoring or target construction;
- whether the value affected a negative-control interpretation;
- whether the value affected the run's limitation or claim ceiling.

Examples MAY include later-stage concepts such as `AuthorityGrant`, `SafetyClassificationRecord`, commissioning-envelope state, promotion state, or active-artifact state when a synthetic/replay evaluator deliberately uses those concepts to define a fixture or claim profile.

Their inclusion in the evaluator-context manifest grants no machine or deployment authority and does not make them learner-visible.

## 3. Run and receipt identity

The evaluator-side `RunManifest`, `QualificationReceipt`, and independently recomputable evidence package MUST bind the exact evaluator-context manifest digest whenever such context is consulted.

Two runs with identical learner-visible bytes but materially different consulted evaluator context are different experiment subjects unless the changed context is explicitly proven irrelevant to every evaluator decision that affects the declared result.

A missing, unresolved, stale, or digest-mismatched required evaluator-context subject fails reproducibility/currentness for the affected claim. It does not silently reuse the prior run identity.

## 4. Replay equivalence

Replay/restart equivalence requires either:

1. the same evaluator-context manifest subject; or
2. a machine-readable irrelevance disposition proving that each changed evaluator-only field could not affect fixture selection, admissibility, scoring, negative controls, or claim ceiling for that replay profile.

"Not learner-visible" is not an irrelevance proof.

A replay whose evaluator semantics changed must not claim equivalence merely because the learner-visible event stream remained byte-identical.

## 5. Separation from learner noninterference

Evaluator-context reproducibility and learner noninterference are distinct requirements.

R4/Three/Seven hidden-state noninterference remains cumulative:

- hold declared learner-visible inputs constant;
- mutate evaluator-only authority/safety/promotion/commissioning/active-artifact state;
- require learner-visible events, task manifests, projection/profile identifiers, feature frames, checkpoint material, opaque identities, and learner-visible digests to remain unchanged unless the declared learner evidence profile explicitly says otherwise.

R5 adds the complementary evaluator-side rule:

- when evaluator behavior legitimately changes because hidden context changed, the experiment identity/receipt must record that context change rather than making the evaluator semantics ambient.

A correct implementation may therefore produce:
- identical learner-visible bytes;
- a different evaluator-context manifest digest;
- and a different evaluation/claim result,
without violating the learner firewall, provided the dependency is explicit and reproducible.

## 6. Evidence-package obligation

A run claiming `INDEPENDENTLY_RECOMPUTABLE` MUST include or content-address:

- the exact evaluator-context manifest;
- every consulted evaluator-only input or an immutable resolvable reference to it;
- the evaluator decision trace or mechanically equivalent evidence showing which inputs affected fixture selection, admissibility, scoring, negative controls, or claim ceiling;
- any irrelevance dispositions used to permit replay across changed evaluator context.

Aggregate metrics alone cannot reconstruct this dependency.

## 7. Hostile acceptance cases

The cumulative R2 qualification suite adds at least these hostile cases:

1. mutate a consulted evaluator-only context value while keeping learner-visible bytes constant; require a distinct evaluator-context subject and reproducible resulting evaluation semantics;
2. omit a required consulted evaluator-context binding; the affected run must fail reproducibility/currentness rather than silently qualify;
3. mutate an evaluator-only field declared irrelevant; require the irrelevance disposition to be mechanically checked and the evaluation result to remain unchanged;
4. mutate hidden authority/safety/promotion/commissioning state and verify learner-visible bytes/identities/digests remain unchanged under the R2 profile;
5. replay a retained run with the exact evaluator-context subject and require the same evaluator joins/scoring/claim-ceiling result under deterministic profiles;
6. attempt replay with a stale or mismatched evaluator-context generation and require rejection or explicit non-equivalence classification.

## 8. Composition and authority

R5 is cumulative with the primary R2 design and R1–R4. Later correction text controls only where it directly conflicts with earlier wording; unchanged obligations remain in force.

R5 does not authorize implementation planning, package scaffolding, Hephaestus handoff, live machine access, industrial writes, commissioning, deterministic control, safety classification, product selection, procurement, deployment, merge/canonical promotion, publication/visibility change, licensing change, credential/provider mutation, or any other protected effect.

Patrick remains the final authority for protected-effect and implementation-gate transitions.
