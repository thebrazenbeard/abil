# ABIL Foundation Design

Status: **approved foundation direction; implementation remains staged and falsifiable**

Date: 2026-09-06

## 1. Purpose

ABIL — Adaptive Brownfield Intelligence Layer — is a commercial engineering project for adding adaptive machine-specific intelligence to existing industrial equipment without requiring replacement of the existing control system.

The first technical objective is not autonomous control. It is to prove that ABIL can observe an unfamiliar system, learn useful predictive structure over time, detect meaningful regime changes, preserve uncertainty, and remain useful as the system changes.

## 2. Product principle

ABIL should learn the machine that actually exists.

The system may receive raw or normalized telemetry, timing, quality, and explicitly supplied operator semantics, but it must distinguish those supplied facts from relationships inferred from behavior.

The product is successful only if its adaptive layer produces useful machine-specific knowledge beyond what simple existing analytics provide.

## 3. Architecture

ABIL is divided into four major subsystems.

### 3.1 Adapter layer

Adapters acquire data from equipment-specific interfaces and emit a common telemetry/event contract.

The first implementation should not attempt broad protocol coverage. It should support:

- a synthetic-process adapter;
- a recorded-telemetry replay adapter;
- one future live read-only adapter selected for the first field environment.

The common event schema should carry:

- deployment identity;
- source/device identity;
- signal identity;
- source timestamp where available;
- acquisition timestamp;
- value;
- quality/status;
- adapter/provenance metadata;
- optional human-supplied semantic annotation kept distinct from learned structure.

### 3.2 Adaptive learning core

The learning core consumes the normalized event stream and owns persistent machine-specific learned state.

The first implementation must include simple baselines before any novel adaptive architecture is promoted.

Required baseline capabilities:

- persistence/last-value prediction;
- exponentially weighted or equivalent streaming prediction;
- at least one multivariate online predictor;
- explicit residual/error tracking;
- at least one regime/change detector;
- checkpoint and restore;
- long-run replay without hidden retraining resets.

The first proprietary/novel learner should be introduced only behind the same interface and must beat the baselines on preregistered tasks to earn complexity.

### 3.3 Evidence and operator layer

The initial operator surface is headless/report-oriented rather than a polished GUI.

Every reported finding should distinguish:

- observed telemetry;
- prediction;
- error/residual;
- detected change;
- hypothesis/inference;
- uncertainty or unresolved ambiguity;
- operator-supplied context.

Natural-language generation is optional and must not become the sole representation of evidence.

### 3.4 Safety/action layer

The first implementation exposes **no machine write path**.

The action gateway is an architectural boundary that will be implemented only when read-only and advisory evidence justifies it.

Future action support must be independently allowlisted and constrained. The adaptive learner never gains control authority merely by emitting a desired action.

## 4. Persistence model

ABIL is machine-specific and deployment-specific.

Persistent state must be versioned and attributable to a deployment identity.

A checkpoint should include or bind:

- schema/config version;
- adapter identity/config digest;
- deployment identity;
- learner type/version;
- learner parameters/state;
- learned normalization/calibration state;
- regime/change-detector state;
- evidence frontier / last ingested event position;
- software version;
- creation time.

Restoring a checkpoint against a different deployment identity should fail unless an explicit transfer operation is requested later by a design that defines what transfer means.

## 5. Validation environments

### 5.1 Synthetic process

A headless simulator should produce:

- multiple interacting continuous/discrete signals;
- hidden operating regimes;
- control inputs;
- delayed effects;
- noisy sensors;
- correlated but noncausal signals;
- gradual drift;
- abrupt faults;
- previously seen regimes that later recur.

Exact simulator truth remains evaluator-side and is not embedded in learner-visible signal names or values.

### 5.2 Replay

Recorded telemetry replay should exercise the exact same normalized event interface as live adapters.

Replay must support deterministic ordering and configurable acceleration without changing source timestamps.

### 5.3 Live shadow mode

The first live field adapter is read-only.

The goal is not broad hardware support. It is to prove usefulness on one real isolated brownfield system while preserving enough adapter abstraction to avoid hard-coding the product to that machine.

## 6. First success criteria

The first ABIL slice is successful if it can demonstrate, with reproducible evidence:

1. sustained streaming ingestion and restart-safe persistence;
2. prediction better than persistence/naive baselines on at least one nontrivial synthetic/replay task;
3. detection and adaptation after a regime change;
4. recovery of performance when an earlier regime returns;
5. no hidden full retraining step required for ordinary adaptation;
6. explicit reporting of prediction error and uncertainty/ambiguity rather than only labels;
7. exact separation between learner-visible signals and evaluator-only truth;
8. resource accounting for CPU, memory, disk, and event throughput.

## 7. First kill conditions

The design should be challenged or simplified if:

- simple baselines perform equivalently at materially lower complexity;
- continual adaptation causes unacceptable forgetting;
- the learner treats persistent degradation as harmless normality with no useful change signal;
- useful results require exhaustive semantic tag mapping;
- checkpoint/restore changes predictions in unexplained ways;
- long-running operation requires periodic hidden resets;
- the evidence surface cannot distinguish observed facts from generated explanations.

## 8. Technology stance for the first slice

The first implementation should optimize for inspectability and experimental speed, not production-scale throughput.

Recommended first stack:

- Python 3.12;
- `uv` for project/dependency management;
- `pydantic` for event/config/checkpoint schemas;
- `numpy` for numerical operations;
- `river` for established online-learning/drift-detection baselines;
- `pytest` for tests;
- newline-delimited JSON for small deterministic fixtures and replay tests;
- a later storage benchmark before selecting a production telemetry store.

No GPU is required for the foundation slice.

The learning interface must not couple ABIL permanently to `river` or any one model family.

## 9. Repository structure target

```text
README.md
docs/
  PRODUCT_THESIS.md
  ARCHITECTURE_BOUNDARIES.md
  FIELD_VALIDATION_ROADMAP.md
  COMPETITIVE_REALITY_CHECK.md
  superpowers/
    specs/
    plans/
src/abil/
  events.py
  adapters/
  learners/
  persistence/
  evaluation/
  cli.py
tests/
  unit/
  integration/
  fixtures/
```

Only the documentation exists in the foundation PR. Source code begins in a later implementation PR after review of this spec and plan.

## 10. Explicitly deferred

This design does not yet choose:

- the first real industrial protocol/PLC adapter;
- a proprietary learning architecture;
- camera/vision ingestion;
- an operator GUI;
- cloud deployment;
- remote fleet management;
- write-capable machine control;
- pricing/licensing;
- legal entity/IP strategy;
- production telemetry storage;
- a relationship between ABIL and any specific Noema runtime.

Those decisions should be made when a concrete experiment or customer requirement forces them.
