# Synthetic Reconstruction Benchmark Preregistration V1

Status: **NON-NORMATIVE RESEARCH PREREGISTRATION / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR MACHINE AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Fixture subject:
- `ABIL_SYNTH_INDEX_PROCESS_CELL_V1`
- source: `docs/research/2026-09-18-synthetic-reconstruction-fixture-v1.md`

Benchmark parent:
- `docs/research/2026-09-13-source-optional-reconstruction-benchmark.md`

Evaluator-context alignment:
- `docs/research/2026-09-18-evaluator-context-benchmark-alignment.md`

Architecture base examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

This document freezes the first comparison logic **before** any benchmark implementation or result exists.

The goal is not to guarantee an ABIL win.

The goal is to make it difficult to:

- change the evidence budget after seeing which participant struggles;
- change scoring labels to rescue a favored participant;
- hide unsupported claims inside one aggregate metric;
- give ABIL more technician help than a baseline;
- treat evaluator-only truth as participant evidence;
- ignore a profile where conventional source migration is the correct answer;
- promote benchmark success into machine-control readiness.

If later research changes these rules, the changed preregistration is a new experiment subject.

## 1. Experiment subject identity

Every run intended for comparison must bind:

- fixture ID and exact fixture digest;
- source/evidence profile;
- observation corpus digest;
- participant-visible projection digest;
- technician-interaction budget/profile;
- opaque-identity mapping generation;
- evaluator-context manifest digest;
- evaluator/scoring implementation identity;
- participant implementation/workflow identity;
- baseline implementation/workflow identity where applicable;
- randomization/seed identity where stochastic behavior exists;
- software/environment/configuration identity sufficient for qualified replay;
- run start/end and scoring timestamps.

A result without the bound experiment subject is exploratory only.

## 2. Primary research questions

The first experiment asks four separate questions.

### Q1 — Source-withheld reconstruction

Can the candidate reconstruct useful ordinary-control structure from declared evidence without presenting withheld behavior as established?

### Q2 — Stale-source conflict

When supplied source conflicts with current behavior, does the candidate preserve the contradiction and provenance rather than silently selecting one truth source?

### Q3 — Identity robustness

When opaque identities are remapped or a source is replaced at the same locator, do claims intended to be identity-independent remain valid without stale state attachment?

### Q4 — Engineering archaeology

Under the same evidence and technician-interaction budget, does the candidate reduce human reconstruction labor and/or improve evidence quality relative to the comparison workflow?

No one question substitutes for another.

## 3. Participant arms

At minimum compare:

### Arm A — Conventional controls reconstruction

A controls engineer/workflow uses ordinary engineering tools appropriate to the supplied evidence profile.

No evaluator-only truth.

### Arm B — AI-augmented controls engineering

A controls engineer/workflow may use contemporary project/source analysis, coding assistants, search/RAG, migration/explanation tools, and ordinary engineering tools.

No evaluator-only truth.

### Arm C — ABIL reconstruction candidate

The current ABIL reconstruction workflow under exactly the declared participant evidence and technician budget.

No evaluator-only truth.

### Optional Arm D — Direct source transformation

Use only on profiles with intact source where a realistic direct migration/transformation workflow exists.

This arm is important because ABIL should not claim a reconstruction advantage where trustworthy source makes direct migration the simpler solution.

## 4. Evidence-budget parity

Within a compared run family, participant arms receive the same declared evidence class.

Differences must be explicit and attributable to the workflow, not hidden input advantages.

The following are forbidden:

- ABIL receives a current source artifact while the baseline receives only telemetry;
- baseline receives semantic tag names while ABIL receives opaque IDs unless identity opacity itself is the tested variable and is applied symmetrically;
- ABIL receives additional technician answers that are not charged to its budget;
- evaluator hints are supplied to one arm through error messages, filenames, scoring feedback, or fixture-specific prompt text;
- one arm receives holdout behavior before scoring while another does not.

If tool capability requires a different representation, the conversion must preserve the declared evidence semantics and be documented.

## 5. Technician-budget parity

Technician interaction is measured as evidence.

For each run, record:

- elapsed technician time;
- questions asked;
- confirmations/corrections;
- semantic labels;
- requested additional traces;
- manually engineered states/transitions;
- participant-proposed versus technician-initiated interventions.

Budget exhaustion is a real outcome.

A participant that needs more human help may continue only as a separately labeled higher-budget run.

## 6. Required run matrix

Initial preregistered matrix:

| ID | Source profile | Coverage | Identity condition | Technician budget | Primary question |
| --- | --- | --- | --- | --- | --- |
| A1 | intact current | broad | stable | practical | intact-source baseline |
| B1 | withheld | broad | stable | small | Q1/Q4 |
| B2 | withheld | broad | remapped opaque IDs | small | Q1/Q3 |
| C1 | partial | broad | stable | small | Q1/Q4 |
| D1 | stale/conflicting | broad | stable | practical | Q2/Q4 |
| E1 | withheld | incomplete | stable | zero | Q1 unsupported-claim pressure |
| E2 | withheld | incomplete | replacement at same locator | small | Q1/Q3 |

A run omitted from the matrix must be reported as omitted, with reason.

Do not average away a failed hostile profile.

## 7. Blindness and evaluator separation

Participant execution must not receive:

- complete fixture state machine;
- withheld branch truth;
- stale/current source-difference table;
- evaluator scoring joins;
- claim-tier decision rules beyond participant-facing task instructions where knowledge of the rule would leak fixture truth;
- evaluator-only identity continuity truth;
- hidden fault schedule;
- baseline output.

The evaluator may possess these, but every consulted evaluator-only input is bound into the evaluator-context manifest.

## 8. Behavior-level scoring unit

The atomic scoring unit is a ground-truth behavior proposition, not a whole-run impression.

Examples:

- `PART_AT_STATION continuously true for 300 ms -> feeding completion may advance to clamping`;
- `PROCESS_COMPLETE before 900 ms is ignored`;
- `STOP_REQUEST during PROCESSING does not imply immediate universal output de-energization`;
- clamped-part recovery is withheld in the default observation interval;
- same endpoint locator does not prove source-incarnation continuity.

Each scored proposition receives exactly one primary disposition.

## 9. Primary dispositions

### `CORRECT_ESTABLISHED`

Participant states behavior materially correctly and claimed provenance/support is adequate.

### `CORRECTLY_QUARANTINED_UNKNOWN`

Participant does not know the behavior, says so explicitly, and does not include it in a supported executable/established envelope.

### `PARTIALLY_SUPPORTED`

Participant captures part of the behavior but materially omits a condition, timing bound, state distinction, or provenance limitation.

### `INCORRECT_ESTABLISHED`

Participant presents a materially false behavior as established/supported.

### `OMITTED_WITHOUT_ACKNOWLEDGEMENT`

Participant fails to model a scored behavior and does not mark the region unknown/outside envelope.

### `PROVENANCE_MISATTRIBUTED`

Behavior may be correct, but the participant falsely attributes how it became known—for example, technician-supplied truth is represented as autonomous inference.

If more than one defect applies, retain secondary defect tags instead of hiding them.

## 10. Secondary defect tags

At minimum:

- `UNSUPPORTED_CAUSAL_PROMOTION`
- `STALE_SOURCE_OVERTRUST`
- `CURRENT_TRACE_OVERTRUST`
- `IDENTITY_LEAKAGE`
- `LOCATOR_AS_IDENTITY`
- `HINDSIGHT_OR_FUTURE_LEAKAGE`
- `TECHNICIAN_INPUT_MISATTRIBUTED`
- `AMBIGUOUS_ACTION_COLLAPSED`
- `UNKNOWN_STATE_COLLAPSED`
- `EVALUATOR_CONTEXT_UNBOUND`

## 11. Core metrics

Report raw counts first.

### 11.1 Established-behavior precision

Among behaviors participant presents as established, fraction scored `CORRECT_ESTABLISHED`.

Do not combine correctly quarantined unknowns into this numerator.

### 11.2 Unsupported-establishment count

Count of:

- `INCORRECT_ESTABLISHED`;
- unsupported causal promotions;
- withheld behavior presented as established without valid provenance.

This is a first-class metric, not a footnote.

### 11.3 Unknown-handling quality

Report:

- correctly quarantined unknown count;
- omitted-without-acknowledgement count;
- unknowns incorrectly converted to established behavior.

### 11.4 Provenance fidelity

Report behaviors whose provenance class matches evaluator truth versus misattributed behaviors.

### 11.5 Conflict handling

For stale-source profile D1, separately report whether each seeded conflict was:

- detected and preserved;
- resolved with adequate current evidence;
- blindly source-trusted;
- blindly telemetry-trusted;
- omitted.

### 11.6 Identity robustness

Compare B1 versus B2 and E1 versus E2.

Report any material claim change attributable only to opaque-ID remapping or false locator continuity.

### 11.7 Technician labor

Report:

- technician minutes;
- labels;
- questions;
- manual engineering actions;
- requested additional observations.

### 11.8 Computational cost

Report separately from human labor:

- wall-clock participant time;
- CPU/memory/storage if available;
- model/tool calls where materially attributable;
- replay/training passes.

## 12. No single hidden aggregate

The first experiment must publish the component metrics.

A convenience aggregate may be explored later, but cannot be used to conceal:

- unsupported established behavior;
- a hostile-profile failure;
- evaluator leakage;
- identity failure;
- provenance fraud/misattribution.

Any aggregate definition added after results are observed is exploratory unless preregistered as a new subject and rerun.

## 13. Baseline fairness

A baseline is not required to imitate ABIL's architecture.

It is allowed to solve the problem in the way its workflow naturally would.

Examples:

- direct source migration can use intact source in A1;
- a human engineer can explicitly say the evidence is insufficient;
- AI-augmented engineering can use project/source-aware tools;
- conventional engineering can rely on documented manual reasoning.

The comparison asks which workflow produces the most supportable result for the evidence regime, not which workflow most resembles ABIL.

## 14. Primary hostile expectations

### B1 — withheld broad evidence

Expected honest success behavior:
- recover substantial normal structure;
- preserve unsupported rare behavior as unknown;
- attribute technician-supplied semantics correctly.

### B2 — remapped identity

Claims intended as identity-independent should remain materially stable.

A material collapse indicates identity dependence and must narrow the claim.

### D1 — stale source

Seeded conflicts must remain visible until resolved.

Silently choosing the stale project or current trace without provenance is failure.

### E1 — incomplete coverage

Fault/manual/stop-during-process behavior is absent.

A participant that invents a complete model incurs unsupported-establishment defects.

### E2 — replacement at same locator

The replacement source must not inherit prior source-specific state solely from locator equality.

## 15. Claim-tier rules

These remain research labels.

### `RECONSTRUCTION_EVIDENCE_ONLY`

May be reported when useful supported structure is recovered, even if large unknown regions remain.

Must state those unknown regions.

### `SOURCE_OPTIONAL_RECONSTRUCTION_SUPPORTED`

Requires at least one source-withheld run where:

- substantial ordinary-control structure is correctly established;
- withheld/unsupported behavior is not silently promoted;
- evaluator leakage is not observed;
- evidence/provenance package is independently inspectable.

One successful fixture does not establish general industrial validity.

### `STALE_SOURCE_RESILIENCE_SUPPORTED`

Requires D1 seeded conflicts to be preserved/detected without systematic stale-source or trace overtrust.

### `ARCHAEOLOGY_REDUCTION_SUPPORTED`

Requires comparison against at least one human/conventional and one AI-augmented workflow under materially equal evidence and technician budgets.

The result must be stated in measured labor/evidence-quality terms, not merely "ABIL won."

### `REPLACEMENT_CONTROL_READY`

Not awardable.

No result in this preregistration can establish live control readiness, machine-write authority, functional safety, deterministic runtime qualification, protocol qualification, hardware/product compliance, or deployment readiness.

## 16. No rescue by post-hoc exclusions

After results exist, do not remove a scored behavior because it was inconvenient unless:

- the fixture itself is proven defective;
- the defect and evidence are documented;
- all affected runs are invalidated consistently;
- the corrected fixture becomes a new exact subject.

Similarly, a failed profile cannot be relabeled "out of scope" after the fact unless the original preregistration already made it optional.

## 17. Failure interpretation

A failed run should narrow the hypothesis rather than trigger automatic architecture churn.

Examples:

- A1 direct migration wins -> evidence that intact-source jobs may not need ABIL reconstruction.
- B1 requires heavy technician mapping -> source-free thesis narrows toward assisted archaeology.
- B2 collapses under remap -> identity-independent learning claim narrows.
- D1 trusts stale source -> provenance/conflict handling is not ready.
- E1 hallucinates missing recovery -> unknown-state discipline is not ready.
- conventional baseline wins labor while matching evidence quality -> commercial labor thesis weakens.

## 18. Required result report

For every compared run family, retain/report:

- exact run subject tuple;
- participant-visible evidence identity;
- evaluator-context identity;
- interaction ledger;
- reconstruction output;
- per-behavior disposition table;
- secondary defect tags;
- component metrics;
- labor/resources;
- baseline output(s);
- invalidation/exclusion events;
- claim-tier disposition with explicit supporting runs and failures.

Narrative summaries cannot replace the retained item-level evidence.

## 19. Change control

Any material change to:

- fixture truth;
- source variants;
- evidence profiles;
- technician budget;
- scoring dispositions;
- metric definitions;
- claim-tier requirements;
- participant/evaluator boundary;
- run matrix;

creates a new preregistration subject for future confirmatory runs.

Historical results remain bound to the old subject.

## Research disposition

This preregistration gives the first synthetic fixture a falsifiable comparison protocol before any implementation result exists.

Its central constraint is deliberately inconvenient:

> ABIL is not allowed to look good by receiving more truth, more human help, a kinder score, or a post-hoc narrower problem than its baselines.

If the system is useful, it should survive equal evidence, explicit unknowns, adversarial stale/withheld cases, and behavior-level provenance accounting.

No benchmark implementation, simulation code, package scaffolding, Hephaestus handoff, live-machine connection, industrial write, commissioning, procurement, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this preregistration.
