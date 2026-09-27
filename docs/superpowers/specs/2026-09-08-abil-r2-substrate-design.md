# ABIL R2 Non-Actuating Substrate Design

Status: **proposed successor design for review; implementation not yet authorized**

Date: 2026-09-08

Normative correction companion: `docs/superpowers/specs/2026-09-08-abil-r2-review-corrections-r1.md`

The correction companion is cumulative with this design and controls where the two conflict. Reviewers must evaluate the exact PR #3 head as the composition of both documents.

## 1. Purpose and provenance

R2 is the corrected successor to the frozen F0 learning-substrate design. It exists because the frozen F0 subject failed qualification and must not be repaired or relabeled in place.

Historical frozen subject:

- repository: `thebrazenbeard/abil`;
- frozen source: `main@b4c0fb4599cd2e15feb9f4ac8a3389afd64d8b25`;
- frozen verdict: `FAIL / NOT_IMPLEMENTATION_READY`;
- frozen source remains historical evidence.

This R2 design is based on the approved **package-first, CLI-driven experimental runtime** direction. It is intentionally non-actuating. It defines an honest substrate for synthetic, replay, checkpoint, and learner evaluation work without introducing industrial write capability, a long-running appliance daemon, production networking, or machine control.

The design also assumes the broader coexistence-first/replacement-capable product architecture proposed in ABIL Draft PR #2. This R2 branch was cut from exact PR #2 head `22187ea9d8fdc22b0e47a42f7877dbe35f11247f`. If that architecture changes materially, R2 must be reconciled against the new exact source before promotion.

## 2. Decision

R2 will be a local Python 3.12 development/runtime substrate composed of two installable distributions in one repository:

1. **`abil-core`** — learner-facing contracts, deterministic feature assembly, learner interfaces/baselines, bounded learner-state codecs, learner worker process, and learner-side CLI utilities.
2. **`abil-eval`** — evaluator records, synthetic/replay adapters, learner projection, outer checkpoint binding, qualification orchestration, scoring, negative controls, qualification receipts, and the developer qualification CLI.

The evaluator runs the learner by fresh process execution. The qualification child environment contains `abil-core` but not `abil-eval`, receives only declared learner-visible bytes/state, and has no object/API path back into evaluator truth.

This is deliberately stronger than putting a simulator object and learner object in the same Python process and relying on discipline not to traverse hidden state.

## 3. Why package-first rather than service-first

R2 is an experimental substrate, not yet the field appliance runtime.

A package-first design is preferred because it:

- keeps the first proof small enough to inspect and falsify;
- makes deterministic local tests and replay easy;
- avoids inventing deployment/service lifecycle before the learner/evidence contracts are trustworthy;
- lets the same core wheel later run inside a service or appliance without making daemon behavior part of the first qualification problem;
- keeps R2 free of live machine connections and write-capable dependencies.

A service-first daemon is deferred because persistence supervision, networking, update policy, and appliance lifecycle would add failure modes that are not needed to close the frozen F0 information-boundary defects.

A same-process monolith is rejected because evaluator/learner object sharing would recreate the capability-leakage class that failed frozen F0 review.

## 4. Scope

R2 includes:

- rich evaluator-side records;
- one closed typed learner projection;
- source-scoped opaque learner identity;
- deterministic asynchronous feature assembly;
- prequential prediction/evidence ordering;
- synthetic and recorded replay through the same learner projection;
- established online baselines before novel learner credit;
- safe outer checkpoint binding plus bounded learner-state serialization;
- deterministic replay/restart equivalence testing;
- timing-oracle controls;
- opaque-label and hidden-truth negative controls;
- machine-readable qualification receipts;
- CPU, memory, disk, throughput, queue, checkpoint, restore, and overload measurement;
- a separate learner-efficacy gate after substrate qualification.

R2 does **not** include:

- industrial write clients or handles;
- PLC/HMI/drive/remote-I/O commissioning;
- active industrial discovery;
- live fieldbus ownership;
- a safety/action gateway;
- control-artifact generation or promotion;
- deterministic machine control;
- a production daemon/service;
- a GUI/HMI;
- cloud services;
- remote fleet management;
- a custom Linux image;
- write-capable Stage-5+ architecture.

A later live read-only adapter remains a separate reviewed capability. R2 synthetic/replay qualification does not authorize a machine connection.

## 5. Trust and process boundaries

### 5.1 Evaluator process

The evaluator process owns information that may include:

- fixture hidden state;
- regime/fault truth;
- rich source/deployment identity;
- rich provenance;
- simulator seed and schedule;
- hidden scoring labels not otherwise part of learner evidence;
- semantic mapping used only for evaluator analysis;
- corpus and fixture control metadata;
- raw adapter/device quality and transport diagnostics;
- learner projection configuration.

An observed target measurement used for online prediction is different from hidden evaluator truth: it becomes learner-visible only through the normal event stream and only **after** the prediction point when prequential learning requires it.

Evaluator records may be rich because they are not learner input.

### 5.2 Projection boundary

All learner ingress crosses one projection function that converts an evaluator-side source record into a closed learner-visible record.

The projection contract must:

- use a typed schema with unknown fields rejected;
- contain no unrestricted metadata dictionary;
- emit only fields declared by the run's projection profile;
- convert rich source/device identity to opaque source-scoped learner identity;
- exclude evaluator-only labels, hidden truth, regime IDs, fixture seeds, semantic tag names, plant addresses, deployment names, and answer-bearing causal labels;
- apply the same logic to synthetic input and recorded replay;
- produce deterministic canonical bytes for the same declared input/profile.

A field's existence in `EvaluatorRecord` never implies learner visibility.

### 5.3 Learner process

The learner process is started by fresh process execution, not by fork inheritance of evaluator memory.

Qualification execution uses:

- an environment containing `abil-core` only;
- a scratch working directory rather than the repository/evaluator working directory;
- a sanitized environment-variable allowlist;
- no evaluator truth path supplied by argument, environment, checkpoint, or protocol;
- only declared standard streams/control descriptors;
- serialized `LearnerEvent` input and declared learner-side state;
- a bounded output channel for predictions/evidence.

It does not receive:

- the `abil-eval` package as an import dependency;
- evaluator objects;
- evaluator truth records/files/paths;
- fixture seed/schedule;
- hidden scoring labels;
- semantic mapping files;
- raw rich source metadata;
- a handle back into the evaluator process.

The evaluator must not import learner plugins into its hidden-truth object graph and then hand those objects to plugin code.

### 5.4 R2 learner-code threat model

R2 qualifies architectural/capability separation for **reviewed learner code**, not an arbitrary hostile third-party code-execution sandbox.

The R2 claim is that the declared learner interface, process launch, state, and data paths provide no evaluator/world object or hidden-truth capability. R2 does not claim that malicious code running as the same operating-system user could never inspect unrelated files or exploit the host.

If ABIL later accepts untrusted third-party learner plugins, that requires a separate sandbox/isolation design and qualification. That future requirement must not be inferred as already satisfied by R2 process separation.

### 5.5 Scoring join

Scoring is a separate evaluator-side operation.

`EvaluationJoin` associates learner outputs with evaluator evidence only after the learner output exists. Learner/plugin code cannot traverse the join back to hidden truth.

## 6. Run-control versus learner-task manifests

R2 separates the rich run-control manifest from the learner task configuration.

### 6.1 `RunManifest` — evaluator/control side

May bind:

- rich fixture/corpus/deployment identity;
- adapter/parser identity;
- source digests;
- evaluator seed/schedule;
- projection profile;
- timing profile;
- learner wheel/config identity;
- feature-assembly profile;
- checkpoint compatibility identity;
- scoring/negative-control configuration;
- resource qualification profile.

It is not learner input.

### 6.2 `LearnerTaskManifest` — learner side

Contains only what the learner needs to execute the declared task, such as:

- learner implementation/config;
- opaque target stream/channel identity;
- learner-event schema ID;
- timing visibility profile;
- feature-assembly configuration;
- opaque stream-set/frontier information required for state continuity.

It contains no rich deployment/device identity, semantic mapping, fixture truth, or scoring labels.

## 7. Core record model

### 7.1 `EvaluatorRecord`

Evaluator-side source records may include rich fields such as:

- deployment identity;
- topology/source/device identity;
- raw endpoint/address observations;
- source and acquisition timestamps;
- source quality/status;
- raw scalar value;
- hidden fixture/regime/fault state;
- operator/vendor annotations;
- raw provenance;
- scoring labels.

`EvaluatorRecord` is not a learner schema.

### 7.2 `LearnerEvent`

The default R2 learner schema is intentionally narrow.

Conceptual fields:

```text
schema_id
learner_stream_id
stream_incarnation_id
channel_id
event_id
event_seq
value
observation_status?   # only if projection profile explicitly allows it
relative_time_delta?  # only if timing profile explicitly allows it
```

Rules:

- `learner_stream_id` is opaque and source-scoped;
- `stream_incarnation_id` is opaque and identifies one continuity-established incarnation of that stream;
- `channel_id` is scoped within `learner_stream_id` and its active incarnation;
- bare short channel names are never assumed globally unique;
- `event_id` is an opaque stable identity for duplicate/replay detection and contains no readable plant semantics;
- `event_seq` is allocated from a monotonic sequence domain within one stream incarnation, but physical/recorded arrival may be out of order relative to that sequence;
- `value` in the first R2 slice is a finite scalar numeric/boolean value; arbitrary strings and object payloads are out of scope;
- unknown fields fail closed;
- no arbitrary metadata bag exists;
- no `deployment_id`, device name, network address, tag name, hidden regime, fixture seed, or `ACTION_CONSEQUENCE` label crosses by default;
- optional observation/transport status is supplied evidence and remains conceptually distinct from learner/model uncertainty.

If two records claim the same `(learner_stream_id, stream_incarnation_id, event_seq)` with different `event_id` or different canonical value bytes, the substrate treats that as a source conflict rather than silently replacing one record.

### 7.3 Opaque identifier construction

Learner-visible IDs must not be a direct unsalted hash of readable device/tag/address strings that could be dictionary-reversed.

The evaluator creates corpus/run-local opaque namespaces and mappings. Stable replay identity may be deterministically derived from already-opaque namespace/stream/incarnation/sequence subjects, while the rich-to-opaque mapping remains evaluator-side.

The exact construction is part of the projection profile and qualification evidence.

### 7.4 Human semantics and future action evidence

Human semantic annotations are excluded from the default R2 learner projection.

A future experiment may add a separately typed, explicitly preregistered supplied-annotation channel, but that would be a new evidence profile whose claims must distinguish supplied semantics from learned structure.

R2 has no machine action path. Synthetic exogenous controls may be represented as ordinary opaque input channels when the experiment requires them. They are not labeled `ACTION_CONSEQUENCE`, and temporal observations after an input are not promoted to causal truth by schema.

## 8. Identity model

R2 preserves a strict separation between evaluator/runtime identity and learner-visible identity.

Evaluator/runtime state may bind:

- exact deployment or fixture identity;
- source adapter identity/configuration;
- corpus identity;
- rich physical/source provenance;
- time-bound endpoint/locator observations;
- evidence-backed source-incarnation continuity.

Learner-visible state uses only opaque identities needed for collision-safe learning and replay:

```text
learner_stream_id
  -> stream_incarnation_id
      -> channel_id
          -> event_seq / event_id
```

The mapping from rich evaluator source identity to learner-visible IDs is evaluator-side and part of the projection profile/configuration digest.

IP address, PLC slot, node number, assembly/register, tag path, source filename, device serial, or other rich provenance never becomes the learner primary key merely because it exists.

Evaluator/control-side identity continuity is represented by an `IdentityBinding` (or equivalent) that records endpoint observations, evidence/provenance, and a continuity state equivalent to `ESTABLISHED`, `UNRESOLVED`, or `BROKEN_NEW_INCARNATION`.

Same-locator replacement does not imply continuity. Same-source locator change retains continuity only when independently established. Unresolved continuity blocks ordinary state attachment/restore or starts a fresh incarnation under an explicit rule.

## 9. Timing and schedule-oracle control

Frozen F0 used fixed timing/origin and a deterministic regime split that could become an unintended oracle. R2 makes timing visibility an explicit experiment capability.

Each run declares one `TimeVisibilityProfile`:

1. **`ORDER_ONLY`** — default. Learner receives event ordering but no absolute timestamps or wall-clock origin.
2. **`RELATIVE_DELTA`** — learner may receive bounded relative time deltas needed for irregularly sampled dynamics.
3. **`SOURCE_TIME_DECLARED`** — absolute/source timing is learner-visible because the experiment explicitly needs it; claims must acknowledge this supplied evidence.

The chosen profile is part of run, projection, feature-assembly, and checkpoint identity.

Synthetic fixtures must not use one publicly fixed regime transition such as `step_count // 2` as the sole evaluation schedule. Qualification uses randomized or held-out change schedules and randomized time origins that are evaluator-side and withheld from the learner.

Required timing controls include:

- time-origin shift runs;
- alternate/held-out regime schedules;
- original versus accelerated replay;
- hostile wall-clock pauses/jitter for pacing-independent profiles;
- identical learner-visible event bytes under evaluator-only timestamp-origin mutation for `ORDER_ONLY` runs.

If a timing field is supplied to the learner, the result is credited only to the declared timing profile rather than generalized to timing-blind performance.

## 10. Asynchronous event and feature assembly contract

R2 does not assume all channels form a clean synchronous row at one timestamp.

Raw learner events remain an ordered ingress stream. Feature construction is a separately versioned deterministic contract.

### 10.1 Default assembler behavior

The first R2 assembler maintains last-known learner-visible channel state and processes events in accepted ingress order.

For a configured target channel:

1. receive the next accepted event;
2. if the event is a target observation, build a feature frame **before** incorporating that target value;
3. request prediction;
4. durably associate the prediction with the exact evidence frontier used;
5. reveal the target value to the learner only after prediction for online learning/update;
6. update assembler state;
7. continue.

This enforces prequential ordering and prevents current-target leakage.

Events from other channels update available feature state when they are accepted.

A committed historical prediction/frame may not be rewritten using later or out-of-order evidence. Backward fill, centered windows, future-anchored interpolation, future-dependent normalization, or later evaluator labels/status are incompatible with a prequential profile unless the run is explicitly reclassified as an acausal/offline profile.

### 10.2 Duplicate, late, reordered, and missing events

The assembler/ingress contract must define and test:

- exact duplicate detection by stable event identity;
- source-sequence conflict detection;
- bounded handling of out-of-order arrivals where a profile explicitly enables reorder buffering;
- deterministic watermark/late-event disposition when buffering is enabled;
- no silent interpolation or fabricated values;
- explicit missingness in feature frames;
- deterministic frame output for the same canonical event sequence and config;
- no silent rewrite of already-committed historical predictions when late evidence arrives.

The default R2 replay path uses the corpus's declared canonical ingress sequence. If the original source lacks trustworthy arrival ordering and an adapter derives a total order, that ordering policy is part of the adapter/corpus manifest and claim ceiling.

### 10.3 `FeatureFrame`

A feature frame binds:

- feature-assembly schema/version;
- assembly config digest;
- target opaque stream/incarnation/channel;
- prediction index;
- exact input event frontier used;
- feature values and missingness mask;
- timing-derived features only if the active timing profile permits them.

The learner never receives a feature derived from an event that occurs after the prediction frontier.

### 10.4 Incarnation transition barrier

A source-incarnation transition is an atomic causal boundary across event/frontier state, reorder buffers, open windows, feature state, normalization/calibration, rolling state, change detectors, learner/model state that depends on the transitioned stream, and checkpoint material.

Old/new incarnations may not silently coexist in one feature frame/window. Late old-incarnation events cannot advance new-incarnation state. Open buffers/windows must be deterministically closed, flushed, quarantined, or recomputed before new-incarnation learning proceeds. State migration requires an explicit compatible rule.

If a replacement boundary is discovered late, exact boundaries are recomputed or invalidated from a valid cut where practical; ambiguous boundaries produce explicit contaminated/claim-limited state rather than silently preserving clean history.

## 11. Replay and corpus identity

Recorded replay uses the same evaluator-to-learner projection as synthetic runs.

A replay corpus has a manifest that binds at least:

- corpus ID;
- source file digests;
- adapter/parser version/config digest;
- projection profile/schema digest;
- canonical learner-event sequence digest;
- declared canonical ordering policy;
- timing visibility profile;
- stream-incarnation transition records and continuity-profile digest where present;
- fixture/scoring metadata digest retained evaluator-side;
- opaque-label transform identity when used.

Original-speed and accelerated replay must produce identical analytical learner-event bytes, feature frames, predictions, and scores for a pacing-independent profile.

If a learner is intentionally allowed wall-clock pacing evidence, that experiment is a distinct profile and cannot claim pacing invariance.

## 12. Baseline and learner interface

R2 requires established baselines before a novel learner can earn complexity.

The first baseline set should include:

- persistence/last-value;
- exponentially weighted streaming prediction or equivalent;
- at least one multivariate online predictor;
- one established change/regime detector where applicable.

Every learner runs behind the same interface and consumes the same declared `FeatureFrame` sequence for a given task.

The evaluation harness uses prequential ordering: prediction first, then target reveal/learning.

Learner-specific preprocessing is allowed only when it is part of that learner's declared configuration and cannot alter the shared source/event/target ordering.

No learner receives a better evaluator projection than its competitors unless the experiment explicitly compares evidence profiles as the independent variable.

## 13. Substrate qualification versus learner efficacy

R2 has two separate gates.

### 13.1 `R2-SUBSTRATE-QUALIFIED`

This gate asks whether the experimental/runtime substrate is honest, deterministic, restart-safe, bounded, and implementation-ready.

It may pass even when:

- the persistence baseline wins;
- a simple model beats a more complex learner;
- no learner earns product differentiation;
- machine-specific structure remains weak.

A substrate result must never be upgraded to learner efficacy merely because the plumbing passed.

### 13.2 `R2-LEARNER-EFFICACY`

This separate gate asks whether a particular learner earns stronger product/learning claims.

Stronger efficacy claims require, as applicable:

- fair improvement over agreed baselines;
- recurring-regime retention and adaptation evidence;
- no hidden retraining reset;
- calibrated or otherwise defensible uncertainty/change behavior;
- performance under opaque-label/semantic-ablation controls when the claim is semantic independence;
- at least one inspectable nontrivial machine-specific learned-structure artifact rather than only a scalar score;
- a second fixture/corpus onboarding run using the generic substrate without core-code changes, with configuration/semantic setup burden recorded;
- evidence that supplied names/annotations are not being credited as autonomous discovery.

Failure of learner efficacy does not retroactively fail a structurally honest substrate.

## 14. Opaque-label, identity-remap, and semantic-ablation controls

The qualification tooling must be able to transform an evaluator fixture/corpus so that learner-visible stream/channel/incarnation IDs are deterministically remapped to opaque labels while preserving event/value/order structure.

For substrate qualification, the transform must prove that:

- the schema and runtime continue to function;
- no hidden rich identity is required by the learner interface;
- checkpoint/restore and replay still work under the transformed identity profile;
- evaluator scoring can still join correctly without exposing the mapping to the learner.

For claims where identity itself is not intended to carry predictive information, qualification must include consistent opaque-ID remapping and/or held-out new stream/incarnation identities. If stable identity is intentionally predictive evidence, the claim ceiling must say so.

For learner-efficacy claims, the performance requirement is claim-specific. A learner that collapses when tag semantics disappear cannot be credited with semantics-independent machine-structure learning.

## 15. Evaluator noninterference qualification

R2 must include a deterministic whole-path noninterference test.

Construct paired evaluator runs in which:

- learner-visible canonical event bytes are identical;
- evaluator-only hidden regime/fault labels or other withheld truth differ;
- the learner process starts from the same code/config/checkpoint state.

Required result:

- learner ingress bytes are identical;
- learner predictions/evidence outputs are identical;
- learner checkpoint bytes/digests are identical except for explicitly non-semantic creation metadata that is normalized out of the comparison;
- only evaluator scoring/interpretation may differ.

Any learner-output difference caused solely by evaluator-only truth mutation is a qualification failure.

This noninterference test is distinct from source-continuity testing: actual source replacement/remap is not an evaluator-only metadata mutation and must exercise the source-incarnation rules instead.

## 16. Checkpoint and restore contract

Checkpoint authority is compatibility/state continuity only. It carries no machine-control authority.

### 16.1 Two-layer checkpoint subject

The checkpoint system has two distinct layers:

1. **Outer evaluator/control binding** — rich compatibility/provenance identity not visible to the learner.
2. **Learner state envelope** — bounded opaque learner continuity state.

The outer binding includes or content-addresses at least:

- checkpoint schema/version and checkpoint ID;
- exact learner implementation/version/config digest;
- learner state codec/version;
- learner-event schema ID;
- projection profile digest;
- timing profile;
- feature-assembly version/config digest;
- adapter/source profile digest;
- corpus/fixture identity where relevant;
- exact active stream-incarnation set;
- continuity/`IdentityBinding` profile digest;
- source-scoped frontier for every active stream incarnation;
- software/build identity;
- payload length/shape bounds;
- payload digest/integrity value;
- creation metadata retained outside learner features.

The learner state envelope contains only learner-required opaque state and no rich deployment/device/source identity.

### 16.2 Safe serialization

Generic Python `pickle`, `marshal`, or arbitrary executable object deserialization is not an accepted R2 checkpoint codec.

Each learner must expose a typed bounded state codec. Acceptable first-slice techniques include canonical JSON for scalar/map state and bounded numerical arrays loaded with object deserialization disabled.

Checkpoint decoding must enforce declared size, type, array-shape, and version bounds before constructing learner state.

### 16.3 Restore rules

Restore mechanically rejects, absent a separately designed migration operation:

- wrong deployment/fixture/source binding where that binding is required;
- wrong source incarnation or unresolved continuity state;
- wrong learner implementation/config;
- wrong projection/timing/assembly profile;
- wrong event schema;
- wrong adapter/source profile;
- unknown codec/version;
- corrupt or tampered payload;
- stale frontier that would silently duplicate already-consumed events;
- frontier ahead of available replay/source evidence;
- stream/incarnation-set mismatch;
- incompatible software/schema identity.

R2 does not define cross-machine model transfer. A transfer/migration capability is a separate future design and must be mechanically distinct from ordinary restore.

### 16.4 Restart equivalence

For a deterministic learner and run profile, uninterrupted execution and execution interrupted by checkpoint/restore at declared cut points must produce equivalent subsequent predictions, learner state digest, evaluation results, and source-incarnation frontier.

Qualification uses multiple cut points, including around regime changes, duplicates, late events, and source-incarnation transitions/unresolved continuity.

## 17. Runtime, queue, resource, and overload contract

R2 must measure resource behavior and must not convert overload into silent evidence loss.

The learner worker and evaluator orchestrator use bounded queues/buffers.

On overload, the runtime must produce an explicit machine-readable disposition such as:

- `BACKPRESSURE_APPLIED`;
- `EVENT_REJECTED_OVER_CAPACITY`;
- `RUN_INVALID_RESOURCE_ENVELOPE`;
- controlled shutdown/failure.

It may not silently drop, reorder, duplicate, or fabricate events and still report a valid qualification run.

Each qualification run records resource evidence separately for:

1. learner child/process tree;
2. evaluator/orchestrator;
3. end-to-end substrate.

For each applicable scope record:

- input event count and rate;
- accepted/duplicate/conflict/late/rejected counts;
- prediction count;
- queue high-water marks;
- CPU time and wall time;
- peak resident memory;
- output/checkpoint/corpus disk bytes;
- checkpoint duration;
- restore duration;
- child-process startup duration;
- any overload/failure disposition.

Where the platform cannot perfectly attribute a metric, the limitation is recorded rather than represented as exact attribution.

The implementation plan must preregister concrete numeric resource profiles before performance qualification is run. Those numbers are engineering test targets, not product performance claims. Until measured on an identified reference environment, resource status remains `PROPOSED / UNMEASURED`.

## 18. Qualification receipts, evidence packages, and reproducibility

Every substrate or learner-efficacy run emits a machine-readable `QualificationReceipt` plus a content-addressed `QualificationEvidencePackage` or equivalent retained evidence set.

The receipt binds at least:

- qualification gate and exact test profile;
- repository/source commit;
- source tree/build/wheel digest;
- Python/runtime/dependency-lock identity;
- evaluator package identity;
- learner package identity;
- learner config digest;
- fixture/corpus manifest digest;
- projection/timing/assembly config digests;
- baseline set identity;
- random seeds retained evaluator-side where needed;
- checkpoint identity/cut points where used;
- environment/hardware summary;
- measured metrics;
- every acceptance criterion with `PASS`, `FAIL`, or `NOT_RUN`;
- limitations/claim ceiling;
- evidence-package manifest digest and output artifact digests.

A run may claim `INDEPENDENTLY_RECOMPUTABLE` only when the evidence package contains or content-addresses enough material to independently recompute the declared result, including learner-visible event sequence, feature inputs/profile, scored outputs/frontiers, evaluator joins/targets/profile, paired baselines, negative-control outputs, per-test detail, checkpoint artifacts where relevant, and raw resource measurements.

Aggregate-only receipts are insufficient for independent recomputability.

A human-readable summary may be generated from the receipt, but the summary is not the qualification authority.

## 19. Minimum `R2-SUBSTRATE-QUALIFIED` acceptance set

The substrate gate requires fresh evidence for **every** item in this section and every cumulative added obligation in the normative correction companion.

1. unknown learner-event fields fail closed;
2. no unrestricted evaluator metadata crosses the projection;
3. synthetic and replay paths use the same learner projection contract;
4. hidden-truth mutation with identical learner-visible bytes leaves learner outputs/state unchanged;
5. learner/plugin code receives no evaluator/world object or hidden-truth capability path;
6. source-scoped IDs tolerate duplicate short channel names across streams without collision;
7. rich physical/source identity can change while an explicitly unchanged learner projection remains unchanged only when source continuity remains independently established;
8. transport/device status remains separately attributed from learner/model uncertainty;
9. `ORDER_ONLY` timing tests survive absolute-origin changes and held-out regime schedules without hidden timing fields appearing;
10. raw asynchronous events do not require timestamp-row synchrony;
11. prequential tests prove target value is unavailable before prediction;
12. duplicate, sequence-conflict, missing, late, and reordered-event cases have deterministic declared outcomes;
13. replay corpus identity and canonical learner-event digest are stable;
14. original and accelerated replay are equivalent for pacing-independent profiles;
15. wrong-identity, corrupt, stale, ahead, mismatched, and incompatible checkpoints are mechanically rejected;
16. uninterrupted and checkpoint/restored runs are equivalent at multiple cut points;
17. checkpoint decoding uses bounded non-executable state codecs;
18. every baseline and learner receives the same declared event/frame sequence for paired comparison;
19. the harness can validly report `simple baseline wins` without treating that as substrate failure;
20. opaque-label transformation runs without learner access to the mapping;
21. a second replay fixture can be configured/onboarded through generic substrate/configuration paths without modifying `abil-core` logic, and the setup burden is recorded;
22. queues/buffers are bounded and overload cannot silently produce a valid run;
23. CPU/memory/disk/throughput/checkpoint/restore evidence is emitted under a preregistered resource profile with learner/evaluator/end-to-end attribution;
24. the implementation contains no industrial machine-write client/path and no live-machine capability is implied by the result;
25. one complete `QualificationReceipt` and referenced evidence package are recomputable from retained run artifacts and digests;
26. a deliberately broken harness/comparator/fixture negative control fails as expected; unexpected pass invalidates the affected harness/gate;
27. a source-incarnation transition is mechanically isolated across buffers/features/frontiers/derived learner state and replay;
28. future evidence cannot rewrite a committed prequential prediction/frame;
29. opaque-ID remap and/or held-out-identity controls are exercised for claims that exclude identity as predictive evidence;
30. an old-incarnation checkpoint cannot attach to a replacement source merely because a locator or stable stream handle is reused;
31. unresolved source continuity cannot silently resume as clean ordinary state.

The correction companion adds more detailed hostile cases under these same obligations. A missing or `NOT_RUN` required case means the substrate is not yet `R2-SUBSTRATE-QUALIFIED`.

## 20. Learner-efficacy evidence contract

After substrate qualification, a learner may be evaluated under a separate exact source/config/corpus subject.

A learner receives no efficacy credit merely because:

- the substrate runs;
- it emits an anomaly score;
- it reproduces supplied tag names;
- human annotations disclose the relationship;
- evaluator timing leaks the regime schedule;
- it improves only after a hidden reset/full retrain;
- one fixture is hand-tailored in code;
- it memorizes stable fixture/stream/incarnation IDs where identity is not part of the declared predictive evidence.

An efficacy result should retain at least:

- paired baseline comparison;
- prediction/change/adaptation metrics appropriate to the task;
- recurrence/forgetting evidence where applicable;
- opaque-label/identity-remap result where applicable;
- second-fixture onboarding evidence;
- inspectable learned-structure artifact;
- explicit uncertainty/insufficient-evidence behavior;
- exact claim ceiling.

The first R2 learner is allowed to fail this gate without invalidating the substrate.

## 21. Proposed repository structure

```text
pyproject.toml                  # uv workspace / root tooling
uv.lock
packages/
  abil-core/
    pyproject.toml
    src/abil/
      __init__.py
      contracts/
        events.py
        features.py
        predictions.py
        checkpoints.py
        receipts.py
      assembly/
        base.py
        prequential.py
      learners/
        base.py
        baselines.py
      persistence/
        codec.py
        checkpoint.py
      worker.py
      cli.py
  abil-eval/
    pyproject.toml
    src/abil_eval/
      __init__.py
      evaluator_records.py
      projection.py
      identity.py
      corpora.py
      replay.py
      fixtures/
        synthetic.py
      scoring.py
      controls/
        opaque_labels.py
        hidden_truth.py
        timing.py
        broken_harness.py
      qualification.py
      cli.py
tests/
  unit/
  integration/
  qualification/
  fixtures/
```

The learner child environment installs `abil-core` only. The evaluator/orchestrator environment installs both distributions.

## 22. CLI shape

The first operator is the developer/reviewer, not a plant operator.

Representative commands:

```text
abil checkpoint inspect <path>
abil worker --learner-config <file>

abil-eval corpus verify <manifest>
abil-eval replay --manifest <run-manifest>
abil-eval qualify-substrate --manifest <qualification-manifest>
abil-eval evaluate-learner --manifest <efficacy-manifest>
abil-eval receipt verify <receipt>
```

The exact flags may change during implementation planning, but the semantic separation remains:

- `abil` is learner/core-side;
- `abil-eval` owns evaluator truth, projection, identity continuity, scoring, and qualification orchestration.

No CLI command in R2 opens a machine write path.

## 23. Technology choices

Initial stack:

- Python 3.12;
- `uv` workspace and lockfile;
- Pydantic 2.x for closed typed contracts and manifests;
- NumPy for bounded numerical state/fixtures;
- River for established online baselines where its behavior fits the declared interface;
- `pytest` for unit/integration/qualification tests;
- newline-delimited JSON or canonical JSON for small retained event/receipt fixtures;
- SHA-256 digests for content identity/integrity within the local R2 trust model.

R2 does not claim cryptographic authenticity from a SHA-256 digest alone. If artifacts cross an untrusted boundary, authenticated signing/verification is a separate security capability and must not be implied by local integrity checks.

## 24. Failure behavior

The substrate fails closed at the claim/evidence boundary.

Examples:

- unknown learner schema field -> reject input/run;
- projection mismatch -> reject run;
- duplicate event with identical identity/content -> deterministic duplicate disposition;
- same source sequence with conflicting identity/content -> invalidate/quarantine run;
- corrupt checkpoint -> reject restore;
- wrong profile/source/incarnation/frontier checkpoint -> reject restore;
- unresolved source continuity -> block ordinary state attachment/restore or start an explicit fresh incarnation;
- evaluator/learner noninterference test fails -> substrate gate fails;
- resource envelope exceeded with data loss risk -> run invalid, not a degraded pass;
- baseline wins -> valid substrate result, learner efficacy not earned;
- hidden truth or semantic mapping reaches learner -> qualification failure;
- broken-harness negative control unexpectedly passes -> affected qualification harness/gate untrusted;
- evidence package missing/incomplete/digest-mismatched -> no independent-recomputability claim;
- unavailable test evidence -> `NOT_RUN`, never inferred pass.

## 25. Review boundaries and next gate

This document and its normative correction companion are design artifacts only.

They do not authorize:

- implementation;
- source package scaffolding;
- Hephaestus implementation handoff;
- industrial machine connection;
- live adapter work;
- write capability;
- deployment;
- merge.

The next process gate is exact-head peer review of the corrected PR #3 design composition. Implementation planning may begin only after that design source is approved under the current gate.
