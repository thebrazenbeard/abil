# Source-Optional Reconstruction Benchmark

Status: **NON-NORMATIVE RESEARCH DESIGN / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-13

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Competitive-scan parent: `research/control-reconstruction-competitive-scan-20260913@417d003ef47944259b192bbd4c4f12b2ee716d76`

## Purpose

The competitive scan narrows ABIL's plausible moat to **source-optional, evidence-driven reconstruction of the installed machine itself** rather than generic AI PLC programming, source migration, soft-PLC execution, or brownfield analytics.

That claim needs a benchmark that can fail it.

The benchmark question is:

> Can ABIL reconstruct useful ordinary machine-control structure from declared machine-visible evidence and bounded technician interaction, preserve uncertainty where evidence is insufficient, and reduce engineering archaeology relative to conventional and AI-augmented controls workflows?

The benchmark is intentionally separated from substrate qualification. A trustworthy R2 substrate can pass even if every ABIL learner loses this benchmark. Conversely, a good reconstruction score cannot excuse leakage, non-reproducibility, hidden evaluator truth, or another substrate defect.

This document defines a research target only. It does not authorize implementation, machine connection, industrial discovery, commissioning writes, control generation for a real machine, deployment, procurement, merge, or canonical acceptance criteria.

## 1. Core comparison

ABIL should not be compared only against anomaly detectors. The relevant reconstruction baselines are:

1. **Conventional manual controls reconstruction** — an engineer receives the evidence normally available for the declared profile and reconstructs the control behavior with ordinary tools.
2. **AI-augmented controls engineering** — an engineer may use current source/project analysis, PLC-code explanation/generation, RAG/copilot, and migration tooling, but receives no evaluator-only truth.
3. **Direct source transformation** — when an intact trustworthy source project exists, use a realistic source-to-target migration path rather than forcing behavioral reconstruction.
4. **Simple data-driven baselines** — established forecasting/system-identification/change-detection methods for the portions of the task they can legitimately address.
5. **ABIL reconstruction** — the candidate ABIL workflow under exactly the same declared evidence and technician-interaction budget.

A strong ABIL result must beat the appropriate baseline for the evidence regime. It does not earn credit by choosing a harder workflow when a trustworthy intact project already makes conventional migration cheaper and safer.

## 2. Evaluator-versus-participant boundary

The benchmark evaluator may know more than any reconstruction participant.

Evaluator-only truth may include:

- exact synthetic controller/state-machine definition;
- intact legacy source/project artifact;
- deliberately stale or divergent source variants;
- hidden state, transition, timer, fault, reset, startup, shutdown, recovery, and manual-mode truth;
- exact physical/logical source identities and remaps;
- injected field-modification truth;
- ground-truth provenance of every change;
- withheld transition/fault schedule;
- scoring joins and coverage labels.

None of that becomes learner-visible merely because the evaluator possesses it.

The benchmark must reuse the R2 information-boundary principle: participant-visible inputs are an explicit closed projection; evaluator truth is a separate scoring subject. Any future implementation of this benchmark must preserve R2's prequential/no-hindsight and independent-recomputation requirements rather than inventing a looser research path.

## 3. Evidence profiles

The same underlying machine family should be exercised under multiple evidence profiles.

### Profile A — intact trustworthy source

Participant receives the current source/project/configuration artifact plus the declared observable machine evidence.

Purpose:

- establish the strongest conventional/source-migration baseline;
- measure whether ABIL adds material evidence/coverage value beyond modern source transformation;
- prevent ABIL from claiming advantage on a problem already solved cheaply by intact-source migration.

Expected result: direct source transformation may win. That is not an ABIL failure outside this job class; it is evidence about where reconstruction adds value.

### Profile B — source withheld

Evaluator retains the intact source/project as hidden scoring truth. Participant receives only declared machine-visible evidence and the same bounded technician channel available to ABIL.

Purpose:

- test the central source-optional reconstruction claim;
- compare reconstructed behavior against both hidden source and actual machine behavior;
- quantify how much technician archaeology remains necessary.

This profile is especially valuable on a machine whose current source can be retained by the evaluator while being withheld from the reconstruction system.

### Profile C — partial source

Participant receives an incomplete backup, partial project, I/O export, tag list, HMI artifact, old printout, or another realistically incomplete source package.

Purpose:

- test whether ABIL can combine source evidence with observed behavior without pretending the partial artifact is complete;
- measure the value of retaining source provenance separately from learned structure.

### Profile D — stale/conflicting source

Participant receives a plausible legacy project that disagrees with installed behavior in evaluator-known ways.

Example controlled divergences may include:

- changed I/O mapping or replacement device;
- field-added debounce/filter logic;
- changed timeout;
- swapped normal/recovery sequence;
- modified manual-mode behavior;
- added or removed permissive;
- altered startup/restart handling;
- operator workaround reflected in real behavior but absent from the backup.

Purpose:

- test whether the system preserves contradiction instead of blindly privileging source or telemetry;
- require explicit provenance and uncertainty around the disagreement;
- measure ability to identify which evidence would resolve the conflict.

### Profile E — no source and incomplete behavioral coverage

Participant receives only machine-visible evidence from an observation interval that intentionally excludes one or more rare but ordinary-control behaviors.

Purpose:

- test unknown-state quarantine;
- ensure unobserved startup/shutdown/fault/recovery/manual behavior is not guessed into an authorized model;
- distinguish useful reconstruction from overconfident trace imitation.

## 4. Technician-interaction budget

Human interaction must be measured, not treated as free hidden supervision.

Each benchmark run records at least:

- technician minutes;
- number of explicit labels/semantic declarations;
- number of confirmations/corrections;
- number of requested additional observations;
- number and type of bounded diagnostic/commissioning actions in profiles where such actions are simulated or otherwise separately authorized;
- amount of source/project interpretation performed manually;
- number of manually engineered states/transitions/permissives/recovery paths;
- interventions proposed by the system versus initiated independently by the technician.

A benchmark may define multiple budgets, for example `ZERO_SEMANTIC_LABELS`, `SMALL_TARGETED_BUDGET`, and `PRACTICAL_ENGINEERING_BUDGET`.

The product claim is not that humans are unnecessary. It is that **targeted** human grounding should beat exhaustive manual reconstruction on the machine classes ABIL targets.

## 5. Reconstruction subject

The scored reconstruction is not ladder syntax.

The benchmark should score an inspectable ordinary-control model containing, where present in evaluator truth:

- operating states/modes;
- transitions;
- commands/actions;
- expected observations and timing relationships;
- prerequisites/permissives;
- ordinary non-safety interlocks;
- timers/timeouts;
- alarms/fault states;
- startup and shutdown behavior;
- reset/restart behavior;
- jam/fault recovery;
- manual/operator modes;
- unresolved alternatives and explicit unknowns;
- provenance/coverage for every claimed behavior.

Independent safety functions are outside this benchmark's reconstruction target. Synthetic fixtures should use ordinary-control semantics and keep any safety-like evaluator truth explicitly out of autonomous reconstruction credit.

## 6. Scoring dimensions

No single aggregate score should hide an unsafe failure mode.

### 6.1 Behavioral coverage

Measure the fraction of evaluator-known ordinary-control behaviors represented correctly in the reconstruction, separated by class:

- normal cycle;
- startup/shutdown;
- manual mode;
- fault/alarm;
- reset/restart;
- recovery;
- timing/timeout;
- rare transition.

Coverage must distinguish `correctly reconstructed`, `correctly left unknown/outside envelope`, `incorrectly reconstructed`, and `omitted without acknowledgement`.

### 6.2 False-authority / unsupported-claim rate

Count behaviors the reconstruction presents as established/automatable without adequate evidence.

This metric is more important than raw recall for a replacement-control thesis. A system that fills every gap with a plausible guess can score superficially well while being unusable.

Stronger claims should require zero or near-zero unsupported promotion candidates for the declared operating envelope.

### 6.3 Unknown-state quality

Measure whether withheld/ambiguous behaviors are explicitly surfaced as unknown and whether the system proposes useful evidence to resolve them.

Useful outcomes include:

- correct quarantine;
- correct competing hypotheses;
- discriminating observation/action proposal;
- correct refusal to collapse uncertainty.

### 6.4 Source-conflict handling

For stale-source profiles, score whether the participant:

- detects the conflict;
- preserves source versus observed-behavior provenance;
- avoids silently rewriting history;
- avoids blindly trusting the source artifact;
- identifies evidence capable of resolving or bounding the discrepancy.

### 6.5 Semantic-grounding efficiency

Measure useful reconstruction gained per technician minute / label / correction.

Report both absolute labor and marginal value of each additional human interaction budget.

### 6.6 Archaeology labor

Measure total human engineering effort required to reach the declared supportable reconstruction envelope.

The relevant comparison is:

`manual controls engineer` versus `AI-augmented controls engineer` versus `ABIL-assisted workflow`.

If ABIL does not materially reduce labor or improve evidence quality/supportability enough to justify its additional machinery, the commercial thesis narrows.

### 6.7 Provenance fidelity

For every scored behavior, check whether its asserted provenance matches the actual path by which it entered the model:

- observed;
- source/vendor supplied;
- technician supplied;
- inferred;
- simulated/tested;
- unresolved.

A correct behavior with falsely claimed autonomous discovery does not earn the same credit as a correctly attributed supplied fact.

### 6.8 Evidence-request quality

When evidence is insufficient, score proposed next observations/tests by expected discrimination among competing hypotheses and by unnecessary intervention cost.

This can initially be evaluator-scored in simulation without granting real-machine write authority.

### 6.9 Time/resources to useful result

Report wall-clock/computational resources separately from human labor:

- time to first useful structure;
- time to declared reconstruction envelope;
- CPU/memory/storage where relevant;
- replay/training passes;
- number of intervention opportunities consumed.

## 7. Hostile benchmark cases

The benchmark should contain adversarial cases that specifically attack ABIL's story.

### H1 — normal-cycle trap

Normal production traces make one control model appear complete, but startup/recovery behavior requires an additional state/transition.

Pass condition: missing behavior remains explicit unknown/outside envelope until evidence supports it.

### H2 — correlated-proxy trap

A sensor reliably precedes an actuator in observed data but is not the actual permissive/causal control relationship.

Pass condition: prediction may use the correlation; control reconstruction does not promote it to causal/permissive truth without additional evidence.

### H3 — stale-project trap

Legacy source contains a valid historical mapping that no longer matches installed I/O/behavior.

Pass condition: conflict is surfaced and provenance retained; source is not silently treated as current truth.

### H4 — opaque-identity/remap trap

Equivalent machine evidence is presented under remapped opaque learner identifiers.

Pass condition: claims intended to be identity-independent remain materially stable or are narrowed transparently.

### H5 — replacement-at-same-locator trap

A logical endpoint/address remains the same while the underlying source/device incarnation changes.

Pass condition: continuity is not inferred from locator equality and prior learned state does not silently attach to the replacement source.

### H6 — missing acknowledgement / ambiguous action trap

In simulation-only intervention profiles, an action may or may not have executed before acknowledgement disappears.

Pass condition: the evidence model preserves ambiguity and does not manufacture a causal label or blind retry assumption.

### H7 — withheld rare transition

A rare recovery/manual/fault transition is absent from the training/observation interval.

Pass condition: the reconstructed executable envelope excludes or explicitly engineers it; it is not hallucinated from nearby traces.

## 8. Benchmark artifact package

A run intended to support an independently recomputable research claim should content-address or retain at least:

- benchmark/fixture version and digest;
- evaluator ground-truth machine/control model;
- all source/project variants and their provenance;
- exact participant-visible evidence profile;
- canonical event/replay sequence;
- technician-interaction transcript/ledger;
- intervention proposals and simulated outcomes where applicable;
- participant reconstruction output;
- reconstruction provenance/coverage ledger;
- baseline outputs;
- evaluator scoring joins;
- per-behavior dispositions;
- labor/resource measurements;
- configuration/software/schema identities;
- aggregate results derived from the retained per-item evidence.

Evaluator truth remains outside the learner/runtime capability boundary even though it is retained in the evidence package for independent scoring.

## 9. Proposed claim tiers

These are research labels, not current canonical gates.

### `RECONSTRUCTION_EVIDENCE_ONLY`

Participant recovers useful machine-specific structure but has substantial unknown behavior or no evidence of labor advantage.

### `SOURCE_OPTIONAL_RECONSTRUCTION_SUPPORTED`

Across at least one source-withheld/partial-source fixture, the participant reconstructs substantial ordinary-control behavior with explicit unknown handling and without evaluator leakage.

### `ARCHAEOLOGY_REDUCTION_SUPPORTED`

Against a preregistered human/AI-augmented baseline on the same evidence profile, ABIL materially reduces engineering labor and/or improves evidence/coverage quality at acceptable computational cost.

### `STALE_SOURCE_RESILIENCE_SUPPORTED`

On controlled stale-source cases, ABIL reliably detects/preserves conflicts and does not silently privilege the obsolete artifact.

### `REPLACEMENT_CONTROL_READY`

**Not awardable by this benchmark.** Replacement-control readiness additionally requires separately reviewed deterministic-runtime, authority, ownership/fencing, commissioning, safety-noninterference, protocol/hardware, and deployment qualification. This benchmark can inform reconstruction evidence only.

## 10. Kill / narrowing conditions

The ABIL reconstruction thesis should narrow if repeated controlled tests show that:

- source-withheld reconstruction requires effectively complete manual semantic mapping;
- AI-augmented conventional engineering reaches the same supportable model with materially less labor/cost;
- stale source is routinely trusted over contradictory current evidence;
- normal-cycle performance hides unsupported startup/recovery/fault assumptions;
- unknown states are converted into plausible but unsupported transitions;
- useful structure disappears under opaque-ID remapping or label ablation when the claim excludes identity/semantics;
- intervention proposals do not reduce uncertainty better than experienced-engineer heuristics;
- generated reconstruction cannot retain auditable behavior-level provenance;
- per-installation custom work does not decline as reusable ABIL capability grows.

A narrowed result can still support a useful product. For example, ABIL may prove strongest as an evidence/commissioning assistant around partial source rather than as a source-free reconstruction system. The benchmark should discover that outcome rather than force the broad thesis to pass.

## 11. Recommended progression

If this research direction is later adopted, the cheapest progression is:

1. build one synthetic ordinary-control fixture whose exact controller model is evaluator-only;
2. generate intact, partial, stale, and withheld source profiles from the same underlying machine;
3. preregister baseline evidence budgets and scoring;
4. run source-withheld and stale-source reconstruction entirely offline through the qualified non-actuating substrate;
5. add a human technician interaction budget in simulation;
6. only after the benchmark behaves honestly, apply the same evidence discipline to recorded real-machine data;
7. live read-only validation remains a separate capability gate;
8. any write-capable commissioning or control validation remains separately authorized and reviewed.

This sequence keeps the novel reconstruction claim separable from fieldbus/control-runtime complexity and from protected machine effects.

## Research disposition

The benchmark design is compatible with the current PR #2 product architecture and PR #3 R2 separation: it strengthens the field-evidence thesis without changing either active review subject.

The most valuable property is not a particular metric. It is that ABIL can lose honestly. If intact-source migration wins, if source-free reconstruction collapses into manual engineering, or if the system cannot quarantine unobserved behavior, the benchmark should make that visible early.