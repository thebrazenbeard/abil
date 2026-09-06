# ABIL Product Thesis

Status: **working product thesis; not a validated commercial claim**

## Problem

A large installed base of industrial equipment remains mechanically useful while its software, controls ecosystem, documentation, vendor support, or human knowledge ages out.

The operational problem is not merely that these machines are old. It is that each installation becomes increasingly individual over time:

- PLC logic is modified;
- drives and sensors are replaced;
- process conditions drift;
- operators develop workarounds;
- tooling changes;
- maintenance changes behavior;
- documentation becomes stale;
- the people who know the machine best eventually leave.

Replacing a functioning asset merely to modernize its intelligence layer can be economically irrational.

## Product proposition

ABIL — **Adaptive Brownfield Intelligence Layer** — is intended to sit alongside an existing machine or process and learn the system that actually exists.

The initial product should:

1. ingest available telemetry with minimal disruption;
2. learn recurring operating regimes and predictive relationships;
3. detect meaningful change relative to the machine's own history;
4. maintain uncertainty instead of presenting guesses as facts;
5. surface machine-specific predictions and diagnostic evidence to a human operator or maintenance technician;
6. continue adapting after deployment rather than remaining a frozen model;
7. require progressively stronger evidence before moving from observation to recommendation to bounded action.

## Initial customer

The first likely customer profile is a manufacturer operating valuable brownfield equipment where replacement is expensive and machine knowledge is incomplete, concentrated, or declining.

High-value conditions include:

- unsupported or obsolete HMI/SCADA/software components;
- legacy PLC/PAC systems that still perform useful production work;
- limited historical instrumentation but meaningful live telemetry;
- chronic intermittent faults;
- substantial downtime cost;
- machine behavior that differs materially from nominal OEM assumptions;
- dependence on one or two experienced technicians for diagnosis.

## What ABIL is not

ABIL is not initially:

- a replacement PLC;
- a safety controller;
- an unrestricted autonomous operator;
- a generic chatbot for maintenance manuals;
- a claim that arbitrary network traffic can be understood with no adapter or context;
- a guarantee of causal understanding from passive data alone;
- a requirement to use Noema or any single AI architecture.

## Differentiation target

Existing industrial analytics can already monitor tags, detect anomalies, estimate remaining useful life, classify faults, and predict process variables.

Those capabilities are not sufficient differentiation.

ABIL's stronger target is **continual machine-specific system learning**:

> Build and continuously revise an operational model of this particular installation strongly enough to predict, detect regime changes, compare explanations, expose uncertainty, and identify what additional evidence would be useful.

The product only earns a differentiated position if it can demonstrate useful behavior beyond generic anomaly detection on realistic brownfield data.

## Product wedge

The first commercially useful wedge is read-only shadow mode.

A successful early deployment does not need to control equipment. It needs to show that, after observing a real system, ABIL can produce predictions or discovered relationships that are useful to someone who understands the machine.

The initial proof should answer questions such as:

- Can ABIL learn the normal operating regimes of an unfamiliar system?
- Can it predict near-future state better than simple baselines?
- Can it detect when the system has entered a genuinely new regime?
- Can it adapt without permanently forgetting older recurring regimes?
- Can it distinguish stable predictive structure from transient noise?
- Can it rank plausible explanations without pretending correlation proves causation?
- Can it reduce the amount of manual tag-by-tag semantic mapping required to become useful?

## Commercial hypothesis

ABIL may support a high-value B2B model because industrial downtime is expensive and the installed base of brownfield equipment is large.

That hypothesis is not yet validated for ABIL specifically. Revenue potential depends on proving four things:

1. useful learning on real equipment;
2. deployability without excessive custom integration labor;
3. operator trust through evidence and uncertainty rather than opaque scoring;
4. economic value large enough to justify deployment and support costs.

## Relationship to Noema

ABIL and Noema are separate projects.

Noema investigates persistent learned intelligence under strict developmental and epistemic constraints. ABIL is a commercial engineering product and may use conventional ML, system identification, causal methods, rules, LLMs, vision models, databases, or Noema-derived mechanisms as appropriate.

Noema may contribute ideas to ABIL. ABIL may provide real-world pressure that improves Noema. Neither project should be forced to inherit the other's constraints.
