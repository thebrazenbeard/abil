# Synthetic Reconstruction Evidence Package V1

Status: **NON-NORMATIVE RESEARCH EVIDENCE CONTRACT / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR MACHINE AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Fixture:
- `ABIL_SYNTH_INDEX_PROCESS_CELL_V1`
- `docs/research/2026-09-18-synthetic-reconstruction-fixture-v1.md`

Preregistration:
- `docs/research/2026-09-18-synthetic-reconstruction-preregistration-v1.md`

Evaluator-context alignment:
- `docs/research/2026-09-18-evaluator-context-benchmark-alignment.md`

Architecture base examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

The preregistration fixes what the first benchmark is supposed to test.

This document fixes what evidence must exist afterward for a run to be auditable.

The goal is to prevent a later narrative from standing in for the experiment itself.

A benchmark result is not considered reproducibly inspectable unless the retained package lets an independent reviewer answer:

- what exact experiment subject ran;
- what the participant was allowed to see;
- what the evaluator knew but the participant did not;
- what technician help occurred;
- what outputs the participant actually produced;
- how every scored behavior was joined to evaluator truth;
- which claims were established, unknown, partial, incorrect, omitted, or misattributed;
- what comparison baseline received;
- which post-run exclusions or invalidations occurred;
- what claim tier, if any, the evidence can support.

## 1. Evidence package root

Every run package should have one immutable root identity:

`SyntheticReconstructionRunEvidence`

Required root fields:

- `evidence_version`
- `run_id`
- `experiment_subject_id`
- `fixture_subject`
- `participant_arm`
- `participant_subject`
- `participant_visible_projection`
- `evaluator_context_subject`
- `technician_interaction_ledger`
- `observation_corpus_subject`
- `participant_output_subject`
- `scoring_subject`
- `baseline_subjects`
- `resource_accounting_subject`
- `invalidation_subject`
- `claim_disposition_subject`
- `created_at`
- `completed_at`
- `package_digest`

Every nested subject should carry an immutable digest or equivalent content-addressed identity.

A filename, branch name, timestamp, or human label alone is not sufficient identity.

## 2. Experiment subject

`experiment_subject_id` must bind the preregistered tuple.

At minimum:

- exact fixture identity/digest;
- source/evidence profile;
- behavior-coverage profile;
- identity/remap condition;
- technician-budget profile;
- observation-corpus digest;
- participant-visible projection digest;
- evaluator-context manifest digest;
- evaluator/scoring identity;
- participant workflow identity;
- randomization/seed identity where applicable;
- replay-relevant environment/configuration identity.

If any field that can materially change evaluation semantics changes, the run is a different experiment subject.

## 3. Fixture subject

Required:

- fixture ID;
- fixture artifact path/reference;
- immutable fixture digest;
- truth-model generation/version;
- source-variant identities;
- holdout-set identity;
- seeded-conflict identity;
- identity-remap generation;
- evaluator-only truth digest.

The package may reveal evaluator-only truth only in the retained evaluator package, never in the participant-visible projection.

## 4. Participant arm

Allowed preregistered values:

- `CONVENTIONAL_CONTROLS_RECONSTRUCTION`
- `AI_AUGMENTED_CONTROLS_ENGINEERING`
- `ABIL_RECONSTRUCTION_CANDIDATE`
- `DIRECT_SOURCE_TRANSFORMATION` when the run profile allows it.

Required participant metadata:

- workflow/tool description;
- exact workflow version/configuration where reproducible;
- model/tool identities where materially relevant;
- prompt/instruction subject where applicable;
- source/project/tool inputs actually supplied;
- human operator identity class, not unnecessary personal data;
- start/end timestamps;
- whether the workflow had persistent state from earlier runs.

Cross-run hidden carryover must be recorded.

## 5. Participant-visible projection

This is the exact evidence boundary presented to the participant.

Required:

- projection digest;
- source artifacts supplied;
- telemetry/observation artifacts supplied;
- semantic labels supplied;
- opaque IDs supplied;
- technician-interaction policy supplied;
- allowed diagnostic-query policy;
- participant-facing task instructions;
- withheld categories;
- any representation conversion applied for tool compatibility.

The package must make it possible to prove that evaluator-only truth was absent from the participant projection.

## 6. Evaluator context

Bind the existing evaluator-context rules.

Required:

- evaluator-context manifest digest;
- exact evaluator-only sources/objects consulted;
- identity/version/generation of each;
- immutable reference/digest;
- role = `EVALUATOR_ONLY`;
- as-of/currentness semantics;
- provenance;
- effect flags for:
  - fixture selection;
  - admissibility;
  - scoring;
  - negative-control interpretation;
  - claim ceiling;
- replay disposition for changed evaluator-only context.

A changed evaluator-only object that affects evaluation semantics creates a new experiment subject unless a mechanically justified irrelevance disposition exists.

## 7. Technician interaction ledger

Every technician interaction must be retained as evidence.

Each entry should bind:

- interaction ID;
- timestamp/order;
- participant request or technician-initiated event;
- question/request;
- answer/correction/label;
- elapsed technician time charged;
- budget category;
- linked behavior/hypothesis if known;
- whether the information was already present elsewhere;
- participant output(s) modified afterward.

Summary fields:

- total technician minutes;
- question count;
- confirmation/correction count;
- semantic-label count;
- additional-trace requests;
- manual engineering actions;
- budget remaining/exhausted.

Technician-supplied knowledge cannot later be labeled autonomous reconstruction.

## 8. Observation corpus

Required:

- corpus ID/digest;
- source generation;
- ordering/timing model;
- included trace segments;
- omitted/withheld trace segments;
- perturbation or simulated-intervention segments;
- known missing data;
- timestamp semantics;
- data transformations;
- opaque-identity mapping generation.

The package should permit exact replay of the participant-visible observation sequence when practical.

## 9. Participant output subject

Retain the output as produced before evaluator correction.

Required:

- immutable output digest;
- proposed states/modes;
- proposed transitions;
- prerequisites/permissives;
- commands/actions;
- timing values;
- fault/recovery model;
- manual behavior;
- unknown regions;
- alternative hypotheses;
- provenance assertions;
- requested discriminating evidence;
- claimed support/confidence/envelope.

If the workflow emits executable-looking structure, retention does not confer execution authority.

## 10. Behavior scoring join

The scoring artifact must be item-level.

Each `BehaviorScoreRecord` should bind:

- behavior ID;
- evaluator truth proposition identity;
- truth proposition digest;
- participant proposition(s) mapped to it;
- participant support/provenance claim;
- primary disposition;
- secondary defect tags;
- evaluator rationale;
- evaluator evidence reference;
- participant evidence reference;
- technician-led knowledge reference if applicable;
- unresolved ambiguity;
- scorer identity/version;
- scoring timestamp.

Primary dispositions remain:

- `CORRECT_ESTABLISHED`
- `CORRECTLY_QUARANTINED_UNKNOWN`
- `PARTIALLY_SUPPORTED`
- `INCORRECT_ESTABLISHED`
- `OMITTED_WITHOUT_ACKNOWLEDGEMENT`
- `PROVENANCE_MISATTRIBUTED`

The package must not contain only an aggregate score.

## 11. Seeded hostile-case register

For the synthetic fixture, retain one explicit register for each intentionally seeded falsifier.

At minimum:

- withheld clamped-part recovery;
- stale station debounce;
- stale clamp timeout;
- stale process timeout;
- stale stop-during-processing behavior;
- stale clamped-part recovery behavior;
- stale endpoint locator;
- correlated `UPSTREAM_PHOTOEYE` proxy;
- replacement source at stable locator;
- incomplete fault/manual/stop evidence;
- ambiguous synthetic action acknowledgement;
- evaluator-context change case.

Each hostile case records:

- whether participant evidence exposed it;
- whether participant detected it;
- whether it was preserved as conflict/unknown;
- whether it was incorrectly promoted;
- linked behavior-score records;
- effect on claim disposition.

## 12. Baseline symmetry record

For each compared baseline:

- baseline arm identity;
- exact evidence projection digest;
- technician budget;
- tool/workflow identity;
- observation corpus digest;
- scoring subject identity;
- resource accounting;
- deviations from participant parity.

Any asymmetry must have a written reason.

An unexplained evidence advantage invalidates a direct fairness claim.

## 13. Resource accounting

Separate human and compute cost.

Human:

- technician minutes;
- controls-engineer minutes;
- evaluator minutes;
- manual labeling;
- manual model/state-machine construction;
- correction/rework time.

Compute/tooling:

- wall-clock workflow time;
- model calls;
- external tool invocations;
- CPU/memory/storage where material;
- replay/training/analysis passes;
- tool/license assumptions relevant to reproducibility.

Do not collapse labor reduction and computational cost into one number.

## 14. Invalidation and exclusion record

Every run package has an explicit invalidation section, even when empty.

Allowed statuses:

- `VALID_AS_RUN`
- `EXPLORATORY_ONLY`
- `INVALID_FIXTURE_DEFECT`
- `INVALID_EVIDENCE_LEAK`
- `INVALID_BUDGET_ASYMMETRY`
- `INVALID_EVALUATOR_DRIFT`
- `INVALID_PARTICIPANT_CONTAMINATION`
- `INVALID_OTHER`

Required for invalidated/excluded material:

- discovery time;
- defect description;
- affected run/behavior IDs;
- whether all arms are affected;
- corrective subject, if any;
- whether rerun is required.

A failed participant result is not itself an invalidation reason.

## 15. Claim disposition

The package must end with an evidence-bounded claim record.

Allowed research claim tiers from the preregistration:

- `RECONSTRUCTION_EVIDENCE_ONLY`
- `SOURCE_OPTIONAL_RECONSTRUCTION_SUPPORTED`
- `STALE_SOURCE_RESILIENCE_SUPPORTED`
- `ARCHAEOLOGY_REDUCTION_SUPPORTED`

Explicitly non-awardable:

- `REPLACEMENT_CONTROL_READY`

Each awarded tier must list:

- supporting run IDs;
- blocking/contrary run IDs;
- hostile profiles passed;
- hostile profiles failed;
- residual unknowns;
- scope limitations;
- evaluator leakage disposition;
- identity-robustness disposition;
- provenance-fidelity disposition.

A tier with unreported contrary evidence is invalid.

## 16. Package-level hostile checks

Before calling a benchmark result inspectable, verify at least:

1. every required nested subject has immutable identity;
2. participant-visible projection is distinguishable from evaluator-only truth;
3. evaluator-context inputs that affect semantics are bound;
4. technician interactions are fully charged and attributable;
5. participant output is retained before evaluator correction;
6. behavior scoring is item-level;
7. seeded hostile cases are individually accounted for;
8. compared baselines have parity evidence;
9. invalidation record exists even when empty;
10. failed hostile profiles are not removed from summaries;
11. aggregate metrics are reproducible from retained item-level records;
12. claim tier cites both supporting and contrary evidence;
13. `REPLACEMENT_CONTROL_READY` is never awarded by this benchmark.

## 17. Minimum auditable directory concept

A future implementation may choose a different storage structure, but an auditable package should be able to express the equivalent of:

```
run/
  manifest
  fixture-subject
  participant-visible/
  evaluator-only/
  interactions/
  observations/
  participant-output/
  scoring/
  hostile-cases/
  baselines/
  resources/
  invalidation/
  claim-disposition/
```

This is an evidence organization concept, not implementation authority or a mandated filesystem/API layout.

## 18. Reproducibility boundary

A replay is qualified as the same experiment subject only when replay-relevant identities match or changed fields have a justified, retained irrelevance disposition.

A replay that changes:

- fixture truth;
- holdout;
- participant projection;
- evaluator semantics;
- technician budget;
- scoring rules;
- baseline evidence;
- identity-remap condition;

is not silently pooled with the original run.

## 19. Research disposition

This evidence contract turns the benchmark preregistration into an auditable evidence shape without implementing the benchmark.

The intended failure mode is explicit:

> If the package cannot prove what each participant saw, what the evaluator knew, what the technician supplied, how each behavior was scored, and why the resulting claim ceiling follows, the benchmark result is not strong enough to support the claim.

No benchmark runner, scoring engine, simulation code, PLC program, package scaffolding, Hephaestus handoff, live-machine connection, industrial write, commissioning, procurement, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research evidence contract.
