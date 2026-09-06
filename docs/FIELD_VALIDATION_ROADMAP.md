# ABIL Field Validation Roadmap

Status: **working validation sequence; no deployment authorization implied**

The roadmap is intentionally ordered so each stage can fail cheaply before ABIL earns access to a harder environment.

## Stage 0 — Synthetic headless process

Build a small non-rendered industrial process simulator with hidden state, noisy sensors, controllable actuators, delays, recurring regimes, faults, drift, and confounding relationships.

ABIL should receive only declared learner-visible signals.

Goals:

- verify the telemetry/event model;
- compare candidate learners against simple baselines;
- test online adaptation and persistent state;
- prove that late regime changes can still be learned;
- test recurring old regimes after newer learning;
- measure compute and memory cost;
- keep exact simulator truth evaluator-side.

The simulator should be fast enough to generate long histories without GPU-expensive visual rendering.

## Stage 1 — Recorded telemetry replay

Feed ABIL recorded industrial-style telemetry through the same adapter/event boundary used by the simulator.

Replay must support original timing and accelerated timing where the model permits it.

Goals:

- test missing values, jitter, asynchronous signals, resets, and real-world noise;
- test schema drift and tag additions/removals;
- measure whether the learner finds stable predictive structure;
- compare performance with conventional forecasting/change-detection baselines;
- evaluate restart/checkpoint behavior.

No live equipment connection is required at this stage.

## Stage 2 — Live isolated shadow mode

Deploy ABIL on a separate PC connected to a real isolated machine/process environment in read-only mode.

The first live objective is deliberately narrow:

> Can ABIL observe an unfamiliar real system long enough to learn machine-specific predictive relationships that are useful to an experienced human without exhaustive manual mapping?

Expected evidence package:

- exact adapter configuration;
- list/schema of observed signals;
- acquisition timing and drop statistics;
- model/checkpoint version;
- prediction accuracy against preregistered baselines;
- regime/change detections;
- examples of correct and incorrect inferred relationships;
- operator assessment of whether surfaced findings are useful, obvious, wrong, or novel;
- resource consumption and stability over long runs.

## Stage 3 — Operator-facing advisory mode

ABIL remains unable to directly change machine state but may surface:

- near-term predictions;
- detected changes;
- ranked hypotheses;
- evidence supporting or weakening each hypothesis;
- unresolved uncertainty;
- suggested additional observations;
- proposed discriminating tests.

The operator interface should make it easy to mark findings as useful, wrong, obvious, or unresolved so product learning can be evaluated separately from persuasive prose.

## Stage 4 — Human-supervised test requests

ABIL may propose bounded tests intended to reduce uncertainty.

A human decides whether and how the test is executed using existing plant procedures and controls.

ABIL observes the resulting evidence and updates its model.

The key validation question is whether active evidence gathering resolves ambiguity better than passive monitoring alone.

## Stage 5 — Constrained action gateway

Only after advisory and supervised-test evidence is strong enough should ABIL be allowed to submit machine-action requests to an independent safety gateway.

The gateway enforces explicit constraints and may require human approval.

ABIL still does not own safety authority.

## Stage 6 — Bounded autonomy

Autonomous action is a later product stage, not an initial requirement.

Any bounded-autonomy claim must be specific about:

- allowed actions;
- operating envelope;
- independent interlocks;
- confidence/uncertainty conditions;
- rollback/recovery behavior;
- response to sensor failure or model disagreement;
- human override;
- evidence that autonomy materially outperforms advisory-only operation.

## Core evaluation metrics

ABIL should be scored on more than anomaly detection.

Important measures include:

- next-state and multi-horizon prediction;
- calibration/uncertainty quality;
- change/regime detection delay and false-positive rate;
- retention of older recurring regimes;
- adaptation speed after change;
- held-out condition transfer;
- usefulness of suggested discriminating observations/tests;
- amount of manual semantic onboarding required;
- compute, memory, storage, and network cost;
- operator usefulness ratings tied to specific outputs;
- ability to say "insufficient evidence" when appropriate.

## Kill conditions for the first field thesis

The initial ABIL thesis should be materially revised if realistic testing shows that:

- useful performance requires exhaustive hand-labeling of every signal and relationship;
- simple established baselines match ABIL at substantially lower complexity/cost;
- online adaptation creates unacceptable forgetting or false normalization of faults;
- the model cannot remain stable during long-running streaming operation;
- discovered relationships are mostly persuasive restatements of tag names or operator annotations;
- deployment/integration labor dominates the economic value;
- uncertainty is too poorly calibrated to support trustworthy diagnostics.
