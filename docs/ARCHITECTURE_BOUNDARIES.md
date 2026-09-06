# ABIL Architecture Boundaries

Status: **foundation boundary contract; implementation choices remain open**

## Core separation

ABIL should be designed as a layered system rather than a monolithic controller.

```text
Existing machine / process
        |
        v
Industrial adapters
        |
        v
Adaptive learning core
        |
        +------> Operator interface / diagnostics
        |
        v
Safety and action gateway
        |
        v
Existing machine / process
```

The important architectural rule is that observation, learning, operator presentation, and action authorization are distinct responsibilities.

## 1. Industrial adapters

Adapters translate available equipment interfaces into a stable internal event/telemetry model.

Potential sources include:

- PLC/PAC tags;
- OPC UA/DA;
- EtherNet/IP;
- Modbus TCP/RTU;
- historian data;
- drive and motion-controller diagnostics;
- remote I/O;
- alarms and HMI events;
- maintenance records;
- cameras or other vision sources;
- vendor APIs or files;
- serial or gateway-connected legacy devices.

An adapter may perform necessary transport decoding and normalization. It should not silently convert evaluator or engineer knowledge into learned machine relationships and then credit ABIL for discovering them.

Adapter capabilities, polling behavior, write capability, and semantic mappings must be explicit.

## 2. Adaptive learning core

The learning core owns machine-specific learned state.

The first implementation should support at least:

- streaming observations;
- persistent learned state;
- action-conditioned prediction where action information exists;
- calibrated or otherwise explicit uncertainty;
- regime-change detection;
- online adaptation;
- comparison against simple baselines;
- retention of older recurring regimes;
- provenance sufficient to explain what evidence changed a prediction or model standing.

The architecture should not assume that one model family will solve every installation.

A practical ABIL system may combine multiple methods, including conventional system identification, probabilistic forecasting, representation learning, change-point detection, causal discovery, rules, and learned models.

## 3. Operator interface

The operator interface should answer useful maintenance and process questions without pretending that the model knows more than it does.

Outputs should distinguish:

- observation;
- prediction;
- anomaly/change evidence;
- hypothesis;
- uncertainty;
- recommended additional observation or test;
- requested action.

A language model may be used to translate structured machine state into natural-language explanations, but it must not become an untracked source of machine truth.

The underlying evidence should remain inspectable independently of generated prose.

## 4. Safety and action gateway

Any future write-capable ABIL deployment must place an independent gateway between learned policy/recommendation and plant control.

The gateway, not the learner, determines what actions are permitted.

Expected controls may include:

- explicit allowlists;
- hard ranges and rate limits;
- operating-state prerequisites;
- independent interlocks;
- human approval requirements;
- action logging;
- timeout/reversion behavior;
- simulation or dry-run checks where useful;
- immediate disable/bypass.

The safety gateway must not depend on the learning model behaving correctly.

Existing PLC logic, safety PLCs, E-stops, hardwired safety circuits, and machine protection remain authoritative unless a later explicitly engineered project changes that contract.

## Read-only first

The first live field deployment should have no control authority.

Read-only shadow mode is not merely a safety concession; it is a useful product stage. ABIL must first prove that it can learn something valuable from a real system before write access is commercially or technically justified.

## Persistent state

ABIL should preserve machine-specific learned state across process restarts and software upgrades using explicit versioned checkpoints.

A checkpoint should distinguish at least:

- model parameters;
- model/runtime state;
- learned normalization/calibration;
- regime or context memory;
- telemetry schema/adapter configuration;
- operator-supplied annotations;
- software/config version;
- source-system identity and deployment identity.

Copying or restoring a checkpoint must not silently attach learned state from one machine to another without an explicit transfer operation.

## Evidence and causation

ABIL must not equate correlation with causation.

Passive data may support prediction while leaving causal direction unresolved. The system should be allowed to say that multiple explanations remain viable.

When distinguishing explanations would require intervention, ABIL should surface the proposed discriminating observation or bounded test rather than fabricate certainty.

## Brownfield onboarding principle

Custom integration labor is a commercial risk.

ABIL should aim to minimize manual semantic mapping while remaining honest about what cannot be inferred.

The desired progression is:

1. discover or import available signals;
2. normalize and timestamp them;
3. learn statistical and temporal relationships without requiring names for everything;
4. surface candidate groupings/relationships;
5. invite targeted human labeling only where it materially improves usefulness;
6. retain provenance for human-supplied semantics separately from learned structure.

## No hidden product coupling to Noema

Noema is not a runtime dependency of ABIL.

If a Noema-derived mechanism outperforms simpler industrial methods under fair evaluation, ABIL may adopt it. If a conventional algorithm works better, ABIL should use the conventional algorithm.

The product is judged by usefulness, reliability, deployment cost, and evidence—not architectural elegance.
