# Synthetic Reconstruction Baseline Workflows V1

Status: **NON-NORMATIVE RESEARCH BASELINE CONTRACT / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR MACHINE AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Fixture:
- `ABIL_SYNTH_INDEX_PROCESS_CELL_V1`

Preregistration:
- `docs/research/2026-09-18-synthetic-reconstruction-preregistration-v1.md`

Evidence package:
- `docs/research/2026-09-18-synthetic-reconstruction-evidence-package-v1.md`

Architecture base examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

The benchmark already requires conventional, AI-augmented, and ABIL comparison arms.

This document fixes what those baseline arms are allowed to do before any result exists.

The purpose is to prevent a false comparison where ABIL receives a competent engineering workflow while a baseline is reduced to an artificial straw man.

A baseline is valid only when it is permitted to solve the reconstruction problem in a realistic way for its own workflow class.

## 1. Baseline fairness principle

The benchmark compares supportable engineering outcomes under materially equal evidence and technician budgets.

It does **not** require every arm to use the same reasoning process, tool architecture, intermediate representation, or internal workflow.

A baseline may:
- refuse unsupported conclusions;
- ask budgeted technician questions;
- preserve contradictions;
- construct state tables manually;
- use ordinary engineering calculations;
- use permitted source/project analysis tools;
- use AI assistance when the arm is AI-augmented;
- exploit intact source when the run profile explicitly supplies it.

A baseline may not:
- receive evaluator-only truth;
- receive more technician help than the compared ABIL arm;
- receive an easier evidence representation without documenting the semantic transformation;
- see holdout behavior before scoring;
- receive hidden scoring feedback;
- inherit truth from earlier runs unless cross-run state is explicitly part of the subject.

## 2. Arm A — Conventional Controls Reconstruction

Arm ID:
`CONVENTIONAL_CONTROLS_RECONSTRUCTION`

This arm represents competent manual controls-engineering archaeology without generative-AI reconstruction assistance.

### 2.1 Allowed tools

Examples:
- text editor;
- spreadsheet;
- timing calculations;
- signal/event tables;
- state-transition tables;
- manual note-taking;
- source/project viewers;
- diff tools;
- ordinary log viewers;
- plotting/graphing tools;
- protocol/documentation references already included in the evidence profile;
- calculators and deterministic local analysis utilities.

The benchmark should not artificially prohibit tools a competent controls engineer would normally use merely because ABIL automates similar work.

### 2.2 Prohibited assistance

Arm A must not use:
- generative AI;
- LLM-based semantic reconstruction;
- AI coding assistants;
- AI RAG over the project/evidence set;
- evaluator truth;
- hidden fixture documentation.

If a tool contains embedded AI features, either disable them or move the run to Arm B.

### 2.3 Expected workflow

A competent Arm A participant may:

1. inventory supplied evidence;
2. identify signal classes and ambiguities;
3. construct timeline/event tables;
4. infer candidate operating phases;
5. compare repeated cycles;
6. estimate timers/debounces from observations;
7. identify contradictions and missing regions;
8. use budgeted technician questions to resolve high-value ambiguity;
9. produce a state/transition model;
10. explicitly mark unsupported behavior unknown/outside envelope;
11. provide provenance for manual conclusions.

This is not a mandatory sequence. It is the minimum competence envelope the baseline must be allowed.

### 2.4 Human-labor accounting

Arm A must charge:
- all controls-engineer analysis time;
- all technician time;
- manual labeling;
- manual state-table construction;
- manual conflict resolution;
- manual source comparison;
- rework after contradictory evidence.

The benchmark should not treat unrecorded analyst labor as free.

## 3. Arm B — AI-Augmented Controls Engineering

Arm ID:
`AI_AUGMENTED_CONTROLS_ENGINEERING`

This arm represents a competent controls engineer using currently available general AI/project-analysis assistance, without ABIL-specific reconstruction mechanisms.

### 3.1 Allowed tools

Arm B may use:
- LLM chat;
- coding assistants;
- project-aware source analysis;
- RAG/search over supplied participant-visible artifacts;
- scripts generated interactively;
- log summarization;
- code/source explanation;
- migration/explanation tooling;
- data-analysis tools;
- ordinary controls-engineering tools allowed to Arm A.

Tool identity/version/configuration must be retained where materially relevant.

### 3.2 Equal evidence rule

AI tools may receive only participant-visible evidence permitted by the run profile.

Examples:
- if the participant sees opaque IDs, the AI sees opaque IDs;
- if source is withheld, the AI does not receive the hidden source project;
- if only two extra traces may be requested, AI-generated requests consume the same budget;
- if technician labels are capped, AI prompts cannot indirectly request extra labels outside the ledger.

### 3.3 Expected workflow

A competent Arm B participant may:

1. ingest supplied evidence into allowed project/search context;
2. ask AI to summarize signals, source, and traces;
3. ask AI to propose candidate states/transitions;
4. use scripts or analysis notebooks to test timing hypotheses;
5. compare source and observed behavior;
6. ask the AI to identify contradictions and unknowns;
7. generate candidate technician questions;
8. have the human participant accept/reject/refine AI hypotheses;
9. produce an inspectable reconstruction;
10. preserve provenance distinguishing:
   - supplied evidence;
   - technician statements;
   - AI inference;
   - human engineering judgment.

### 3.4 No AI privilege through hidden context

The benchmark must not preload Arm B with:
- fixture truth;
- evaluator scoring rules containing behavior truth;
- previous participant outputs;
- hidden stale/current divergence tables;
- hidden identity-continuity state.

General model pretraining is not treated as fixture-specific evaluator evidence, but any benchmark-specific context supplied at run time must be recorded.

### 3.5 Human/compute accounting

Arm B must record separately:
- engineer time;
- technician time;
- model/tool calls;
- generated scripts;
- manual verification/rework;
- wall-clock workflow time;
- material compute/tool costs if measurable.

## 4. Arm C — ABIL Reconstruction Candidate

Arm ID:
`ABIL_RECONSTRUCTION_CANDIDATE`

Arm C is the ABIL workflow under test.

This baseline document does not define ABIL internals.

It does impose fairness constraints:
- same participant-visible evidence class;
- same technician budget;
- same holdout boundary;
- same scoring unit;
- same resource-accounting categories;
- no evaluator truth;
- no special-case fixture knowledge.

If ABIL uses persistent learned state, that state must be part of the run subject and must obey the identity/remap rules of the fixture.

## 5. Arm D — Direct Source Transformation

Arm ID:
`DIRECT_SOURCE_TRANSFORMATION`

This arm is optional and only valid where the evidence profile contains sufficiently intact source to make direct transformation/migration realistic.

Its purpose is to prevent ABIL from claiming value where reconstruction is unnecessary.

### 5.1 Allowed workflow

Arm D may:
- inspect the intact supplied source;
- build a manual or tool-assisted migration map;
- transform source representations;
- preserve existing logic/timing semantics;
- identify unsupported hardware/runtime assumptions;
- decline to reconstruct behavior already explicitly represented in trustworthy current source.

### 5.2 Claim interpretation

If Arm D is faster and equally evidence-supported on A1, that is useful evidence that intact-source work may be a direct-migration problem rather than an ABIL reconstruction problem.

This does not invalidate source-optional research on other profiles.

## 6. Evidence presentation normalization

Different workflows may require different file formats, but transformations must preserve semantics.

Allowed examples:
- CSV to spreadsheet;
- structured JSON to a table;
- source tree to read-only project index;
- event stream to plotted timeline.

Every transformation must record:
- source artifact;
- transformation method;
- output digest;
- whether names/labels/order/timing changed;
- whether any semantic enrichment was added.

Semantic enrichment not available to other compared arms is an evidence advantage and must be disclosed or removed.

## 7. Common participant task

Every compared arm should receive a participant-facing objective equivalent to:

> Produce the most supportable reconstruction of the supplied ordinary-control behavior that the evidence permits. Distinguish established behavior, unresolved alternatives, unknown/outside-envelope regions, timing constraints, fault/recovery behavior, manual behavior, identity assumptions, and provenance. Do not invent missing behavior. Request additional evidence only within the supplied interaction budget.

Wording may be adapted for tool ergonomics without leaking fixture truth.

## 8. Common output requirements

Every arm must return enough structure to score the same behavior propositions.

At minimum:
- states/modes;
- transitions;
- commands/actions;
- prerequisites/permissives;
- timers/debounces/timeouts where supported;
- fault/recovery behavior;
- manual behavior;
- unresolved alternatives;
- explicit unknown/outside-envelope regions;
- provenance/support;
- requested discriminating evidence;
- claimed confidence/support envelope.

Free-form narrative is permitted only if the evaluator can deterministically map it to behavior propositions.

## 9. Technician interaction equality

Technician interaction is a scarce shared resource.

For all compared arms:
- technician answers are charged;
- clarifications are charged;
- semantic labels are charged;
- additional traces are charged;
- manual correction is charged;
- participant-generated questions do not create extra budget.

If one workflow consumes less technician budget, that is a result.

If one workflow exceeds the budget, its continued run must be separately labeled.

## 10. Time accounting

The benchmark should report at least:
- participant active engineering time;
- participant waiting time attributable to tools;
- technician time;
- evaluator time separately;
- wall-clock completion time.

A workflow that hides human cleanup after the nominal run is not faster.

## 11. Starting-condition parity

Each arm should begin from a clean run state unless persistent state is explicitly the tested subject.

Required controls:
- no previous output from another arm;
- no previous fixture answer;
- no scored holdout behavior;
- no evaluator annotations;
- no hidden correction history.

For stochastic AI workflows, seed/configuration identity should be retained when available.

## 12. Cross-arm contamination

The following invalidate direct comparison unless explicitly designed into the experiment:
- Arm B sees Arm A's finished reconstruction;
- Arm C sees baseline outputs before producing its own;
- technician answers are reused across arms without charging them as supplied evidence;
- an operator unconsciously supplies knowledge learned while running another arm.

Preferred mitigation:
- independent operators or reset/separation protocol;
- fixed technician-answer oracle;
- immutable participant-visible interaction transcript generated from each charged query;
- randomized arm order where practical.

## 13. Competence floor

A baseline participant/workflow must meet a minimal competence floor.

Evidence should show:
- familiarity with basic control sequencing;
- ability to reason about timers/debounces;
- ability to distinguish command from feedback;
- ability to represent unknown behavior;
- ability to preserve contradictory evidence.

A failed baseline caused by obvious operator incompetence is not evidence of ABIL advantage.

## 14. Baseline pilot rule

Before confirmatory comparison, each baseline workflow should complete a non-scored pilot on a separate simple fixture.

Pilot purpose:
- verify tool access;
- verify evidence presentation;
- verify output format;
- verify technician ledger;
- verify resource accounting.

The pilot must not expose truth from `ABIL_SYNTH_INDEX_PROCESS_CELL_V1`.

A baseline may be repaired after pilot mechanics fail, but the repaired workflow identity must be frozen before confirmatory runs.

## 15. Baseline invalidation conditions

A baseline run is invalid for direct comparison if:
- participant received evaluator-only truth;
- evidence budget differs materially without declared reason;
- technician budget is exceeded without relabeling;
- cross-arm contamination occurs;
- required resource accounting is absent;
- output is evaluator-corrected before retention;
- baseline tooling fails for unrelated infrastructure reasons and the failure is counted as reconstruction weakness;
- participant competence floor is not met.

Poor reconstruction quality by a valid baseline is not an invalidation condition.

## 16. Comparison interpretation

The benchmark should never report only:
`ABIL > baseline`

Instead report:
- behavior precision;
- unsupported-establishment count;
- unknown handling;
- provenance fidelity;
- stale-source conflict handling;
- identity robustness;
- technician labor;
- engineer labor;
- compute/tool usage;
- hostile-case outcomes.

Examples of legitimate conclusions:
- ABIL recovered more supportable source-withheld structure with less technician time;
- AI-augmented engineering matched ABIL accuracy but required more manual provenance cleanup;
- conventional engineering was slower but made fewer unsupported claims;
- direct source transformation was superior on intact-source A1;
- no arm had enough evidence to establish withheld recovery behavior.

## 17. No architecture favoritism

The evaluator must not reward:
- ABIL-specific vocabulary;
- ABIL-specific internal data structures;
- a particular state-machine serialization;
- automated output merely because it is automated.

Only scored behavioral/provenance outcomes and preregistered resources count.

## 18. Research disposition

This baseline contract prevents a favorable ABIL result from depending on deliberately weak comparison workflows.

A meaningful archaeology-reduction claim requires ABIL to outperform or complement competent conventional and AI-augmented workflows under equal evidence and technician budgets, while preserving uncertainty and provenance at least as well.

If a competent baseline wins, the benchmark should say so and narrow ABIL's claim.

No benchmark runner, baseline implementation, AI-tool procurement, account connection, paid service use, package scaffolding, machine connection/write, commissioning, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research baseline contract.
