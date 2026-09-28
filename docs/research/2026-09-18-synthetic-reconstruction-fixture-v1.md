# Source-Optional Reconstruction Synthetic Fixture V1 — Index-and-Process Cell

Status: **NON-NORMATIVE RESEARCH FIXTURE DESIGN / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR MACHINE AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Benchmark parent: `docs/research/2026-09-13-source-optional-reconstruction-benchmark.md`

Evaluator-context alignment: `docs/research/2026-09-18-evaluator-context-benchmark-alignment.md`

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

The source-optional benchmark should first fail or survive on a fixture small enough to understand exactly and rich enough to expose the mistakes ABIL is most likely to make.

This fixture is intentionally ordinary control, not functional safety.

It provides:

- normal cyclic behavior;
- startup/shutdown;
- automatic and manual modes;
- timers and debounces;
- a jam/fault path;
- reset/recovery behavior;
- one rare transition that is absent from the default observation interval;
- stale-source divergences;
- mutable endpoint/identity mappings;
- correlated-but-noncausal evidence;
- an ambiguous simulated action outcome.

The fixture is a research scoring subject only. It does not represent a real machine and does not authorize implementation, simulation code, PLC code, live I/O, machine discovery, commissioning, or physical control.

## 1. Fixture identity

Working fixture ID:

`ABIL_SYNTH_INDEX_PROCESS_CELL_V1`

Conceptual machine:

A single-part indexing cell receives one workpiece at an infeed, conveys it to a process station, clamps it, performs a timed/acknowledged process, releases it, and discharges it.

The evaluator owns the complete state machine and truth model.

A participant receives only the evidence allowed by the selected benchmark profile.

## 2. Explicit safety exclusion

The fixture does **not** award reconstruction credit for emergency-stop, guard-locking, safe torque off, safety relay, safety PLC, protective stop, or another functional-safety function.

If a simulated safety-like signal exists for realism, it is evaluator-external and may only cause the ordinary-control model to observe a generic `PERMIT_TO_RUN = false` condition.

The participant is not asked to infer, own, reset, bypass, or reconstruct the safety function behind that condition.

## 3. Logical inputs

Evaluator truth defines these ordinary-control inputs:

| Logical input | Meaning |
| --- | --- |
| `AUTO_MODE` | automatic mode selected |
| `MANUAL_MODE` | manual mode selected |
| `START_REQUEST` | operator requests automatic operation |
| `STOP_REQUEST` | operator requests orderly stop |
| `RESET_REQUEST` | operator requests ordinary fault reset |
| `PART_AT_INFEED` | part present at infeed |
| `PART_AT_STATION` | part detected at process station |
| `CLAMP_CLOSED` | clamp position confirmation |
| `PROCESS_COMPLETE` | process completion acknowledgement |
| `DISCHARGE_CLEAR` | discharge path available |
| `DRIVE_FAULT` | ordinary drive fault indication |
| `PERMIT_TO_RUN` | external permit supplied to ordinary control |

The evaluator may expose these under opaque source-scoped identifiers rather than semantic names.

## 4. Logical outputs

| Logical output | Meaning |
| --- | --- |
| `INFEED_CONVEYOR` | run conveyor toward process station |
| `CLAMP_COMMAND` | command clamp closed |
| `PROCESS_COMMAND` | command process operation |
| `DISCHARGE_CONVEYOR` | run conveyor toward discharge |
| `FAULT_INDICATOR` | ordinary-control fault indication |
| `CYCLE_COMPLETE_PULSE` | one-shot cycle completion indication |

These are synthetic research outputs only.

## 5. Ground-truth states

The evaluator truth model contains at least:

1. `STOPPED`
2. `READY`
3. `FEEDING`
4. `CLAMPING`
5. `PROCESSING`
6. `UNCLAMPING`
7. `DISCHARGING`
8. `JAM_FAULT`
9. `RECOVERY_WAIT`
10. `MANUAL_IDLE`
11. `MANUAL_JOG_INFEED`
12. `MANUAL_CLAMP`
13. `MANUAL_JOG_DISCHARGE`

The participant is not required to use these exact labels. Scoring is behavioral/structural, not string-matching.

## 6. Ground-truth automatic sequence

### 6.1 STOPPED -> READY

Transition requires:

- `AUTO_MODE = true`;
- `START_REQUEST` rising request;
- `PERMIT_TO_RUN = true`;
- no active `DRIVE_FAULT`.

A start request while the permit is false is recorded but does not advance the cycle.

### 6.2 READY -> FEEDING

Transition requires:

- `PART_AT_INFEED = true`;
- `DISCHARGE_CLEAR = true`;
- `PERMIT_TO_RUN = true`.

Output:
- `INFEED_CONVEYOR = true`.

### 6.3 FEEDING -> CLAMPING

`PART_AT_STATION` must remain true continuously for the station debounce interval.

Current evaluator truth debounce:

`STATION_DEBOUNCE_MS = 300`

On qualified detection:
- stop `INFEED_CONVEYOR`;
- enter `CLAMPING`;
- assert `CLAMP_COMMAND`.

### 6.4 CLAMPING -> PROCESSING

Requires `CLAMP_CLOSED = true` before:

`CLAMP_TIMEOUT_MS = 1800`

On success:
- retain `CLAMP_COMMAND = true`;
- assert `PROCESS_COMMAND = true`;
- enter `PROCESSING`.

On timeout:
- deassert ordinary process outputs;
- enter `JAM_FAULT`.

### 6.5 PROCESSING -> UNCLAMPING

Normal completion requires `PROCESS_COMPLETE = true` after at least:

`MIN_PROCESS_MS = 900`

and before:

`PROCESS_TIMEOUT_MS = 4200`

A completion indication earlier than the minimum process time is ignored as implausible/noisy evidence in evaluator truth.

On normal completion:
- deassert `PROCESS_COMMAND`;
- enter `UNCLAMPING`;
- deassert `CLAMP_COMMAND`.

On process timeout:
- enter `JAM_FAULT`.

### 6.6 UNCLAMPING -> DISCHARGING

Requires `CLAMP_CLOSED = false`.

Then:
- if `DISCHARGE_CLEAR = true`, assert `DISCHARGE_CONVEYOR` and enter `DISCHARGING`;
- otherwise remain in `UNCLAMPING` with discharge output off.

### 6.7 DISCHARGING -> READY

Requires `PART_AT_STATION = false` continuously for:

`STATION_CLEAR_DEBOUNCE_MS = 220`

Then:
- deassert `DISCHARGE_CONVEYOR`;
- emit one `CYCLE_COMPLETE_PULSE`;
- return to `READY`.

## 7. Orderly stop semantics

`STOP_REQUEST` does not create one universal immediate output state.

Evaluator truth uses state-specific ordinary-control stop handling:

- from `READY`: transition directly to `STOPPED`;
- from `FEEDING`: stop conveyor and transition to `STOPPED`;
- from `CLAMPING` or `PROCESSING`: finish the bounded current station operation to the defined release point, then stop before discharge;
- from `UNCLAMPING`: release then stop;
- from `DISCHARGING`: complete discharge then stop.

This exists to prevent the reconstruction system from learning a false universal `STOP_REQUEST -> all outputs off now` rule.

## 8. Jam/fault and recovery semantics

The fixture enters `JAM_FAULT` when any of these occurs:

- clamp timeout;
- process timeout;
- `DRIVE_FAULT = true` during commanded conveyor motion;
- part remains at station beyond the maximum discharge interval.

In `JAM_FAULT`:

- `FAULT_INDICATOR = true`;
- conveyor/process outputs are off;
- clamp command follows the fault-entry state recorded by the evaluator; it is not guessed from a universal rule.

Recovery requires:

1. underlying ordinary fault condition clears;
2. `RESET_REQUEST`;
3. evaluator classifies physical synthetic state as one of:
   - `EMPTY_STATION`;
   - `PART_AT_STATION_UNCLAMPED`;
   - `PART_AT_STATION_CLAMPED`;
4. transition through `RECOVERY_WAIT`;
5. deterministic recovery branch according to that classified state.

The default observation interval intentionally contains no `PART_AT_STATION_CLAMPED` recovery example.

That branch is the primary withheld rare-transition test.

## 9. Manual mode

Manual mode is deliberately not just "automatic sequence with buttons."

When `MANUAL_MODE = true`, the evaluator permits bounded individual commands only under declared synthetic prerequisites.

Examples:

- jog infeed only when clamp is not closed;
- clamp command only when a part is at station;
- jog discharge only when clamp is open;
- `PROCESS_COMMAND` is unavailable in basic manual mode.

The participant may receive technician statements about these capabilities depending on the interaction budget.

## 10. Correlated-proxy trap

Evaluator truth generates an auxiliary observable:

`UPSTREAM_PHOTOEYE`

Under normal production traces it precedes `PART_AT_STATION` with high reliability.

It is **not** a permissive for clamping or processing.

A reconstruction may use it predictively but must not promote it to causal/permissive control truth without additional evidence.

## 11. Locator-versus-identity trap

The fixture can be emitted under two synthetic endpoint generations.

Generation A:
- opaque endpoint locator `NODE_17` maps to source incarnation `SRC_A`.

Generation B:
- the same locator `NODE_17` maps to replacement source incarnation `SRC_B`.

The participant evidence can be constructed so the locator is stable while evaluator-only continuity truth changes.

Pass condition: prior source-specific learned state is not silently attached to `SRC_B` merely because `NODE_17` is unchanged.

## 12. Stale-source variant

The evaluator owns an intentionally stale source/project representation with these divergences from current installed truth:

| Subject | Stale source | Current evaluator truth |
| --- | ---: | ---: |
| station debounce | 120 ms | 300 ms |
| clamp timeout | 2200 ms | 1800 ms |
| process timeout | 5000 ms | 4200 ms |
| orderly stop during PROCESSING | immediate process abort | bounded finish-to-release |
| clamped-part recovery | direct discharge | recovery wait then release branch |
| station locator | `NODE_12` | `NODE_17` |

The stale artifact remains internally plausible.

The benchmark should reward explicit conflict preservation, not whichever source happens to be newer-looking.

## 13. Partial-source variant

The partial-source profile supplies only:

- tag/signal list;
- output list;
- normal automatic sequence through `PROCESSING`;
- no timeout values;
- no recovery logic;
- no manual-mode logic;
- no source-incarnation evidence.

The participant must not infer omitted sections are absent from the machine.

## 14. Source-withheld profile

The evaluator retains the complete truth/source representation.

The participant receives:

- declared observation streams;
- opaque source-scoped identities;
- event timing;
- operator mode/request observations;
- the selected technician-interaction budget;
- no evaluator source/state-machine artifact.

The default training observation interval includes:

- 40 normal cycles;
- 4 orderly stops from READY/FEEDING;
- 2 orderly stops during PROCESSING;
- 2 clamp timeouts;
- 2 process timeouts;
- 2 unclamped-part recovery sequences;
- manual jog examples;
- zero clamped-part recovery examples.

The holdout contains the withheld clamped-part recovery branch.

## 15. Incomplete-behavior profile

This profile further removes:

- all jam/fault examples;
- all manual-mode examples;
- all stop-during-processing examples.

A participant that returns a complete fault/manual/stop model anyway must show provenance for those claims or be penalized as unsupported inference.

Correctly declaring those regions unknown/outside envelope is a positive outcome.

## 16. Technician-interaction budgets

### `ZERO_SEMANTIC_LABELS`

No semantic declarations beyond raw/opaque evidence profile metadata.

### `SMALL_TARGETED_BUDGET`

Evaluator permits up to:

- 10 yes/no technician answers;
- 3 short semantic labels;
- 2 requests for an additional recorded trace segment.

### `PRACTICAL_ENGINEERING_BUDGET`

Evaluator permits up to:

- 30 minutes synthetic technician time;
- 25 questions/confirmations;
- 10 semantic labels;
- 5 requested additional recorded trace segments;
- 3 simulated non-actuating diagnostic queries.

All interactions are retained in the evidence ledger.

## 17. Simulated ambiguous-action case

For intervention-quality research only, the evaluator can expose a simulated action:

`REQUEST_SYNTHETIC_INDEX_PULSE`

One case removes the acknowledgement after dispatch while keeping execution truth evaluator-only.

The reconstruction/evidence layer must preserve:

`UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME`

until independent evidence resolves whether the synthetic action executed.

Blind retry is not credited.

This is simulation-only and grants no machine-write authority.

## 18. Participant output contract

The participant should emit an inspectable reconstruction containing at least:

- proposed states/modes;
- transitions;
- commands/actions;
- prerequisites/permissives;
- timers/timeouts/debounces where supported;
- ordinary fault/recovery behavior;
- manual behavior where supported;
- unresolved alternatives;
- explicit unknown/outside-envelope behaviors;
- behavior-level provenance;
- evidence requests that would discriminate unresolved hypotheses.

Exact internal representation is not fixed by this research design.

## 19. Per-behavior scoring labels

Evaluator disposition for each truth behavior:

- `CORRECT_ESTABLISHED`
- `CORRECTLY_QUARANTINED_UNKNOWN`
- `INCORRECT_ESTABLISHED`
- `OMITTED_WITHOUT_ACKNOWLEDGEMENT`
- `PARTIALLY_SUPPORTED`
- `PROVENANCE_MISATTRIBUTED`

The benchmark reports these by behavior class rather than hiding them inside one aggregate score.

## 20. Primary falsifiers

This fixture should expose at least these failure modes:

1. normal-cycle trace imitation presented as full control reconstruction;
2. stale source silently privileged over current contradictory behavior;
3. current telemetry silently privileged over valid historical/source evidence without preserving conflict;
4. `UPSTREAM_PHOTOEYE` correlation promoted to causal permissive truth;
5. withheld clamped-part recovery hallucinated as known;
6. same locator treated as source continuity;
7. manual mode inferred as a trivial copy of automatic control;
8. stop request collapsed to one universal physical/output response;
9. ambiguous simulated action treated as definitely not executed;
10. technician statements credited as autonomous discovery;
11. evaluator-only truth leaking into participant-visible evidence;
12. evaluator scoring/context changing without changing the bound experiment subject.

## 21. Minimum experiment matrix

The first honest benchmark need not be large.

Minimum matrix:

| Run family | Source profile | Behavior coverage | Identity condition | Technician budget |
| --- | --- | --- | --- | --- |
| A1 | intact current | broad | stable | practical |
| B1 | source withheld | broad | stable | small |
| B2 | source withheld | broad | remapped IDs | small |
| C1 | partial source | broad | stable | small |
| D1 | stale/conflicting source | broad | stable | practical |
| E1 | source withheld | incomplete | stable | zero |
| E2 | source withheld | incomplete | replacement-at-same-locator | small |

At least one baseline participant from conventional/manual controls engineering and one AI-augmented controls workflow should receive the same evidence/interaction budget as the ABIL candidate for the run being compared.

## 22. Evidence package

Each run should content-address or retain:

- exact fixture truth version/digest;
- exact source variant(s);
- participant-visible projection;
- evaluator-context manifest;
- technician interaction ledger;
- emitted observation/event sequence;
- participant reconstruction;
- baseline reconstruction(s);
- per-behavior scoring joins;
- unknown/provenance dispositions;
- resource/labor measurements;
- evaluator/scoring implementation/configuration;
- irrelevance dispositions if evaluator-only context differs across replay;
- aggregate metrics derived from retained per-item evidence.

## 23. Success does not mean replacement-control readiness

A strong result on this fixture can support only reconstruction evidence claims.

It cannot establish:

- deterministic runtime qualification;
- fieldbus/protocol qualification;
- machine authority;
- write admission;
- commissioning authority;
- safety authority;
- hardware/product compliance;
- live deployment readiness.

Those remain separate subjects.

## Research disposition

This fixture converts the benchmark from an abstract scoring proposal into one bounded falsifiable research subject while preserving the non-actuating separation.

The fixture is intentionally small enough that an evaluator can know every relevant truth and hostile divergence. If ABIL cannot preserve uncertainty, provenance, identity boundaries, and stale-source conflict here, adding real industrial complexity would only make the failure harder to see.

No implementation, simulation code, PLC program, package scaffolding, Hephaestus handoff, live-machine connection, industrial write, commissioning, procurement, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research design.
