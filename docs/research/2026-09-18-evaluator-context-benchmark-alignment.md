# Source-Optional Benchmark — Evaluator-Context Reproducibility Addendum

Status: **NON-NORMATIVE RESEARCH DESIGN / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related design candidate under separate review: PR #3 R5 at `c2e363d4c1b8c67e032c22d9cad6451342b04e7b`

## Research question

The source-optional reconstruction benchmark already separates participant-visible evidence from evaluator-only truth.

That separation prevents leakage, but it does not by itself make evaluator behavior reproducible.

If hidden evaluator context changes fixture selection, admissibility, scoring targets, negative-control interpretation, or claim ceilings, then two runs with byte-identical participant-visible evidence can receive different evaluation semantics while appearing to share the same benchmark subject.

This addendum asks:

> What must the benchmark bind so evaluator-only context is reproducible without becoming participant-visible?

## Finding

A benchmark run needs two independent evidence identities:

1. the exact **participant-visible projection** supplied to the reconstruction workflow; and
2. the exact **evaluator-context subject** actually consulted to interpret and score that run.

Keeping hidden truth out of participant input is necessary. Treating hidden evaluator context as ambient is not.

## Proposed benchmark evaluator-context manifest

Any benchmark run whose evaluator consults non-participant-visible context should emit or content-address a `BenchmarkEvaluatorContextManifest` or mechanically equivalent subject.

For each consulted evaluator-only input, bind at least:

- source/object class;
- exact identity and generation/version where defined;
- immutable digest or content-addressed reference;
- provenance/source location;
- effective-time or as-of semantics where currentness matters;
- whether it affected fixture/corpus selection;
- whether it affected admissibility/exclusion;
- whether it affected target construction or scoring;
- whether it affected negative-control interpretation;
- whether it affected a limitation or claim ceiling.

Examples include:

- intact or stale source/project variants retained only by the evaluator;
- hidden field-modification truth;
- withheld transition/fault schedules;
- evaluator-only device/source remap truth;
- scoring joins and behavior-class labels;
- benchmark claim-tier rules;
- any later control/deployment context deliberately used to select or interpret a fixture.

The manifest itself remains evaluator-only unless a field is separately declared participant-visible.

## Run identity

For independently recomputable claims, the benchmark run identity should bind at least:

- fixture family/version/digest;
- evidence-profile identity;
- participant-visible projection digest;
- technician-interaction budget/profile;
- evaluator-context manifest digest;
- evaluator/scoring implementation and configuration;
- baseline implementation/configuration identities;
- benchmark schema/version;
- participant/reconstruction implementation identity;
- software/environment identity needed for deterministic or qualified replay.

Two runs with the same participant-visible bytes but materially different consulted evaluator context are different experiment subjects unless the changed context is proven irrelevant to every evaluator decision used by the declared result.

## Replay and irrelevance

Replay equivalence should require either:

1. the same evaluator-context manifest subject; or
2. a machine-readable irrelevance disposition showing that every changed evaluator-only field could not affect fixture selection, admissibility, target/scoring logic, negative controls, or the claim ceiling for that replay profile.

`Not participant-visible` is not evidence of irrelevance.

A changed hidden source version, scoring table, fault schedule, or claim rule must not silently reuse the old run identity merely because the reconstruction input bytes stayed constant.

## Evidence-package consequence

The benchmark artifact package should additionally retain or content-address:

- the exact evaluator-context manifest;
- every consulted evaluator-only input or an immutable resolvable reference;
- the evaluator decision trace or mechanically equivalent dependency evidence;
- irrelevance dispositions used to permit replay across changed context;
- the participant-visible projection as a separate bound subject.

This keeps leakage analysis and evaluator reproducibility auditable as two different questions.

## Hostile research cases

Add at least these research cases before treating the benchmark harness as trustworthy:

1. **Hidden stale-source swap** — keep participant-visible bytes constant, change the evaluator-retained source variant used for scoring, and require a different evaluator-context subject.
2. **Hidden fault-schedule swap** — change withheld transition/fault truth while holding participant evidence constant; run identity and scoring provenance must change.
3. **Scoring-rubric drift** — change a behavior-class weighting/claim rule; the benchmark must not present the result as the same evaluation subject.
4. **Missing consulted context** — omit a hidden input that affected scoring; independently recomputable status must fail.
5. **Irrelevant hidden change** — mutate an evaluator-only field proven not to affect this profile; require a checked irrelevance disposition and unchanged result.
6. **Leakage guard** — mutate evaluator-only context and verify participant-visible projection bytes/digests remain unchanged unless the profile explicitly declares otherwise.
7. **Replay with exact context** — replay the same fixture/projection/evaluator-context tuple and require identical scoring joins/results under deterministic profiles.

## Relationship to PR #3 R5

PR #3 R5 currently proposes the same general boundary for the R2 qualification design, but it remains an unaccepted exact-head review subject.

This research addendum does not treat R5 as canonical, does not carry a PASS forward, and does not change PR #3. If the accepted R2 design changes, any future benchmark implementation should reconcile this research note to the accepted design before use.

The independent research conclusion survives that uncertainty:

> evaluator-only information can remain hidden from the participant while still needing explicit provenance and run-identity binding when it changes evaluation semantics.

## Research disposition

This closes a reproducibility hole in the benchmark design without changing ABIL's moat hypothesis or promoting any architecture claim.

It does not authorize benchmark implementation, package scaffolding, Hephaestus handoff, machine connection, live discovery, commissioning, industrial writes, product selection, procurement, deployment, merge/canonical promotion, publication/visibility change, licensing change, credential/provider mutation, or any other protected effect.
