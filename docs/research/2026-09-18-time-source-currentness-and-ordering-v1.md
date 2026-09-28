# Time-Source Currentness and Ordering V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR PROVIDER AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- PR #6 — write-capability admission design
- Draft PR #12 — snapshot/revalidation
- Draft PR #16 — execution evidence / causal attribution
- Draft PR #20 — evidence producer authenticity
- Draft PR #21 — trust-state currentness / anti-rollback
- Draft PR #22 — trust-state transition authorization

## Purpose

ABIL now uses time for several bounded claims:

- admission expiry/freshness;
- dispatch revalidation;
- causal attribution windows;
- delayed receipt interpretation;
- historical producer validity;
- credential/trust overlap windows;
- transition effective times;
- approval freshness;
- retention and garbage-collection policy.

The open question is:

> What makes a timestamp or time comparison trustworthy enough for the exact claim being made?

A declared clock/profile is necessary but not sufficient.

## 1. Time-source subject

A future time source should be an explicit subject.

Conceptually:

`TimeSourceSubject`

Potential fields:
- time-source profile ID;
- implementation/source identity;
- deployment/host scope;
- monotonic-clock identity if applicable;
- wall-clock identity if applicable;
- synchronization source/profile;
- current time estimate;
- uncertainty/error bound;
- last synchronization evidence;
- source generation/boot/session identity;
- rollback/jump counters;
- health/currentness disposition;
- immutable digest.

This research does not mandate a schema.

## 2. Wall clock and monotonic time are different

Wall-clock time is useful for:
- UTC timestamps;
- certificate/effective-time interpretation;
- cross-system correlation.

Monotonic time is useful for:
- elapsed duration;
- expiry relative to a trusted start;
- timeout;
- local ordering within one boot/session.

Do not substitute one for the other implicitly.

A wall clock may jump.
A monotonic clock may reset on reboot.

## 3. Time-source dispositions

Suggested states:

- `TIME_CURRENT_WITHIN_BOUND`
- `TIME_CURRENT_BUT_UNCERTAIN`
- `TIME_STALE`
- `TIME_SOURCE_UNKNOWN`
- `TIME_SOURCE_CONFLICTING`
- `TIME_ROLLBACK_DETECTED`
- `TIME_FORWARD_JUMP_DETECTED`
- `TIME_UNCERTAINTY_EXCEEDED`
- `TIME_SESSION_RESET`

These are evidence/currentness states, not authority states.

## 4. Uncertainty is part of the comparison

If an expiry deadline is near the current time, uncertainty matters.

Example:

- current estimate: 12:00:00
- uncertainty: ±5 s
- expiry: 12:00:03

A future validator should not claim precise freshness if the deadline lies inside the uncertainty interval.

Possible conservative rule:
- if uncertainty overlaps a fail-closed boundary, reject or downgrade.

Exact policy depends on operation class.

## 5. Time rollback

Hostile case:

1. credential/evidence expires at 12:00;
2. system clock is restored to 11:30;
3. stale object appears valid again.

Expected:
- detect rollback or fail currentness comparison;
- do not reactivate expired authority/trust/evidence.

Generation/epoch checks remain independently required.

## 6. Forward jumps

Large forward jumps can also be dangerous.

Effects may include:
- premature expiry;
- retention/garbage collection too early;
- invalid causal windows;
- skipped grace periods;
- immediate transition activation.

A jump should be explicit evidence, not silently accepted as ordinary elapsed time.

## 7. Reboot / monotonic reset

Monotonic counters often reset on reboot.

Therefore a monotonic timestamp should bind:
- boot/session identity;
- source generation;
- elapsed-time origin.

A post-reboot monotonic value must not be compared directly with pre-reboot value without a qualified bridge.

## 8. Multi-source time

Distributed components may use different clocks.

Potential sources:
- host clock;
- PLC/device clock;
- gateway clock;
- telemetry collector;
- database timestamp;
- external synchronized time.

A future causal/currentness decision should know which clock produced each timestamp and how their uncertainty/order relates.

## 9. Partial ordering

When exact clock synchronization is weak, retain stronger ordering evidence where available:

- request sequence;
- transaction sequence;
- ledger sequence;
- target correlation sequence;
- monotonic local order;
- causal happens-before relation.

Do not infer total chronology from wall-clock timestamps alone.

## 10. Synchronization evidence

A future time profile may record:
- synchronization protocol/profile;
- last successful sync;
- offset estimate;
- drift estimate;
- uncertainty bound;
- source identity;
- holdover state.

This research does not select NTP/PTP/GPS/provider.

## 11. Holdover

If external synchronization is lost, local clocks may remain usable within a bounded holdover envelope.

A future policy may define:
- maximum holdover duration;
- drift bound;
- operation classes allowed;
- when uncertainty becomes too large.

Do not silently treat unsynchronized holdover as fully current time.

## 12. Time-source currentness generation

Time source/profile/configuration may change.

Examples:
- synchronization source changes;
- host clock service changes;
- firmware changes;
- oscillator/clock hardware changes;
- leap-handling policy changes.

A future time-source generation can make such changes explicit.

## 13. Admission / PR #6 integration

Write-admission expiry/freshness should bind:
- evaluation clock/profile identity;
- time-source currentness disposition;
- uncertainty bound;
- evaluation timestamp;
- exact comparison semantics.

A caller-supplied timestamp cannot extend authority.

## 14. Snapshot / PR #12 integration

Dispatch revalidation should not use a stale decision solely because:
- wall clock moved backward;
- cached freshness deadline appears future again;
- reboot reset monotonic time.

Dispatch-time comparison should bind the current time-source/session subject.

## 15. Causal-attribution / PR #16 integration

Causal windows should retain:
- timestamp source;
- uncertainty;
- sequence/order evidence;
- expected latency interval.

If clock uncertainty exceeds the causal window:
- attribution should downgrade;
- temporal succession alone is insufficient.

## 16. Producer-authenticity / PR #20 integration

Historical producer validity may depend on whether evidence was created:
- before expiry;
- before compromise/revocation effective time;
- during valid delegation.

Historical timestamp claims therefore need:
- qualified time source or ordering evidence;
- trust-state generation;
- creation-time evidence.

Do not use an untrusted producer's own clock as sole proof of historical validity.

## 17. Trust-state / PR #21 integration

Trust-state effective-time windows should not override monotonic generation/anti-rollback.

Generation remains primary anti-rollback evidence.

Time may govern:
- overlap;
- grace;
- scheduled activation;
- historical interpretation.

A backward clock must not revive superseded trust generation.

## 18. Transition / PR #22 integration

Approval freshness and transition effective time should bind:
- exact time-source profile;
- currentness;
- uncertainty;
- parent generation.

A transition whose approval freshness is ambiguous due to clock uncertainty should fail closed if policy requires fresh approval.

## 19. Governance-root integration

If governance-root transitions use effective times:
- root generation/lineage remains authoritative;
- time controls activation only within the protected transition contract.

Time cannot create governance authority.

## 20. Evidence-ledger integration

Evidence records should bind their timestamp source/profile where time is material.

Ledger sequence can remain valid even if wall-clock time later proves wrong.

Correction should:
- preserve original timestamp;
- append corrected/qualified time interpretation;
- avoid rewriting history.

## 21. Delayed evidence

A delayed receipt/observation should not be classified only by arrival wall-clock time.

Retain:
- source event time;
- receive time;
- sequence/correlation identity;
- uncertainty;
- intervening events.

Arrival time and occurrence time are separate.

## 22. Retention / garbage collection

Time-based deletion is dangerous if clock state is uncertain.

A future retention policy should use:
- qualified time source;
- uncertainty margin;
- ledger/currentness dependencies;
- unresolved ambiguity constraints.

Clock jump must not delete still-relevant evidence.

## 23. Clock source authenticity

A time source may itself need authenticated provenance.

Examples:
- signed time source;
- trusted local platform clock;
- authenticated synchronization server;
- device clock under a trusted gateway.

This research does not require one method.

The claim ceiling should reflect actual source authenticity.

## 24. Conflicting clocks

If two required sources disagree beyond permitted bound:

`TIME_SOURCE_CONFLICTING`

Do not:
- average blindly;
- select the time that makes a credential valid;
- select the time that makes an evidence window convenient.

Use operation-specific fail-closed policy.

## 25. Leap / calendar semantics

A future profile should define:
- UTC interpretation;
- leap-second handling;
- timezone use;
- daylight-saving irrelevance for protocol time;
- serialization format.

Local civil time should not be used for security/currentness boundaries without explicit conversion semantics.

## 26. Time-read receipt concept

A future `TimeSourceReadReceipt` could bind:
- time-source subject ID;
- source generation/session;
- wall-clock estimate;
- monotonic reading;
- uncertainty bound;
- synchronization evidence;
- rollback/jump disposition;
- read time/order;
- reader identity;
- profile digest;
- immutable receipt digest.

Research shape only.

## 27. Hostile research cases

A future implementation should fail closed or downgrade for at least:

1. wall clock rolls back and expired evidence appears current;
2. forward jump prematurely expires authority;
3. reboot resets monotonic time and old timeout is reused;
4. caller supplies convenient timestamp;
5. two clocks disagree and system chooses permissive one;
6. uncertainty overlaps expiry but validator returns exact PASS;
7. stale sync source remains trusted indefinitely;
8. holdover exceeds qualified drift bound;
9. causal window narrower than clock uncertainty;
10. delayed observation is ordered by arrival time only;
11. old device clock attaches stale telemetry to new request;
12. trust rotation grace window reopens after rollback;
13. transition approval freshness is evaluated under stale clock;
14. retention job deletes evidence after forward jump;
15. local timezone/DST changes alter expiry interpretation;
16. device and gateway clocks are compared without offset/uncertainty;
17. historical producer uses its own untrusted clock to prove pre-revocation creation;
18. monotonic reading from prior boot is compared to new boot;
19. synchronization source changes without new time-source generation;
20. clock profile changes but old currentness receipt remains reused.

## 28. Relationship to generations

Time and generations solve different problems.

Generations prove:
- supersession;
- anti-rollback;
- state lineage.

Time proves:
- duration;
- expiry;
- effective windows;
- causal timing.

Neither substitutes for the other.

## 29. Evidence ceiling

This research does not:
- select or configure NTP/PTP/GPS;
- change host clocks;
- install synchronization software;
- choose a cloud time provider;
- mutate credentials;
- authorize machine writes.

It defines time-source identity/currentness/uncertainty properties only.

## 30. Research disposition

The practical rule is:

> A timestamp is usable only to the extent that its source, session, currentness, uncertainty, and ordering semantics support the exact claim being made.

No time-source implementation, time-provider mutation, host-clock configuration, credential/provider mutation, machine access/write, commissioning, deployment, promotion, merge/canonical promotion, or other protected effect is authorized by this research.
