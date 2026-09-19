# Time-Source Currentness and Trust-Ordering Composition V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR PROVIDER AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #24 predecessor exact head `0eca969ae67d641c4d81e56be524aa5336659122`.

This companion reconciles PR #24 with the strengthened trust/governance chain:
- PR #21 protected trust-state head witness;
- PR #22 transition authorization composition;
- PR #23 protected governance-root currentness witness.

It preserves PR #24 V1 as research provenance and tightens the composition rules below.

## 1. Time does not establish structural currentness

Time and structural lineage answer different questions.

Structural currentness is established by:
- exact identity;
- authorized lineage;
- protected head witness/currentness mechanism;
- scope;
- conflict/fork status.

Temporal evidence may then determine:
- not-before activation;
- expiry;
- grace/overlap;
- approval freshness;
- causal-window membership;
- retention eligibility.

Therefore replace any shorthand such as "generation remains primary anti-rollback evidence" with the stronger rule:

> Protected lineage/witness currentness is the anti-rollback authority; generation is one bound lineage attribute. Time may narrow temporal admissibility but cannot establish or restore structural currentness.

## 2. Avoid time↔trust circularity

A trust decision may depend on time:
- certificate expiry;
- delegation expiry;
- transition approval freshness.

A time source may itself depend on authenticated provenance.

This can form a cycle:

`trust -> authenticated time -> temporal trust validity -> trust`.

A future evaluator MUST NOT treat that cycle as mutual self-justification.

## 3. Structural-first evaluation cut

For claims requiring trusted time, use a two-stage or equivalently grounded evaluation:

### Stage A — structural trust/currentness
Establish, without relying on the temporal predicate currently being evaluated:
- current GovernanceRootAnchor + protected root witness;
- current trust-state node + protected trust witness;
- exact time-source identity/provenance subject;
- required signer/provider role and scope;
- no unresolved structural fork/rollback.

### Stage B — temporal admissibility
Using the structurally admitted time source and its current session/uncertainty evidence, evaluate:
- not-before;
- expiry;
- grace;
- approval freshness;
- causal/retention windows.

If Stage A cannot be established without the same Stage B predicate in a cycle, the dependency is unresolved and MUST fail closed or use an explicitly qualified external bootstrap profile.

## 4. Time source identity is not time-source currentness

A valid signed or configured time source does not prove:
- its current session is live;
- its synchronization is fresh;
- its clock has not rolled back;
- its uncertainty is within the required bound;
- the host did not restore an older time-source state.

Bind a `TimeSourceCurrentnessReceipt` or mechanically equivalent subject.

## 5. TimeSourceCurrentnessReceipt

Potential fields:
- time-source subject ID/digest;
- source implementation/provider identity;
- exact host/deployment scope;
- boot/session ID;
- time-source generation/config generation;
- wall-clock estimate;
- monotonic reading where applicable;
- synchronization source/profile;
- last qualified sync evidence;
- offset/drift estimate;
- uncertainty bound;
- rollback/forward-jump counters/evidence;
- holdover state;
- structural trust/currentness cut digest;
- reader/verifier identity/profile;
- final time-source disposition;
- immutable receipt digest.

This is a research shape, not an implementation authorization.

## 6. Time-source rollback evidence must not depend solely on wall time

A clock cannot prove its own non-rollback merely by reporting a later timestamp.

Useful non-wall-clock evidence may include:
- boot/session identity;
- monotonic counters within a boot;
- protected configuration generation;
- append-only synchronization sequence;
- externally witnessed sequence;
- trusted hardware monotonic evidence;
- another independently qualified ordering source.

The exact mechanism is profile-specific.

## 7. Boot/session reset semantics

Monotonic readings are only comparable within their bound session unless a qualified bridge exists.

After reboot:
- old monotonic deadlines do not silently transfer;
- cached freshness receipts bound to prior session are stale unless the exact policy provides a safe bridge;
- wall-clock continuity does not prove monotonic continuity.

A future receipt MUST include boot/session identity where monotonic time is material.

## 8. Uncertainty-aware interval comparison

Treat a time estimate as an interval when uncertainty is nonzero.

Conceptually:
`now ∈ [estimate - uncertainty, estimate + uncertainty]`.

For a fail-closed expiry boundary:
- if the entire interval is before expiry, temporal-validity MAY be established;
- if the interval crosses expiry, exact freshness is not established;
- if the entire interval is after expiry, expired.

For not-before activation:
- if interval crosses activation boundary, activation is unresolved;
- do not select the convenient endpoint.

Operation-specific policy may be more conservative.

## 9. Time cannot widen authority

If a structural state is:
- revoked;
- superseded;
- conflicting;
- not uniquely witnessed;
- unauthorized;

no timestamp can upgrade it to current.

Time may only preserve or narrow an already structurally admissible state.

## 10. Historical time and current time are separate cuts

Historical verification may use:
- historical event time;
- historical qualified time-source evidence;
- historical trust/root cuts.

Current acceptance must use:
- current structural trust/root cuts;
- current admissible time-source session/cut where temporal conditions matter.

A historical time receipt cannot become current by restore.

## 11. Trust transition integration

For PR #22 transitions:
- predecessor/root currentness is structurally established first;
- authorizer role/scope is established structurally;
- temporal approval freshness/effective time is evaluated afterward;
- uncertainty crossing the temporal policy boundary blocks precise authorization/application;
- protected witness advancement remains required independently of time.

Time cannot decide which competing authorized successor won.

## 12. Governance-root integration

For PR #23:
- GovernanceRootHeadWitness determines root structural currentness;
- time may govern scheduled activation or temporary authority only under that witnessed lineage;
- clock rollback cannot revive old root;
- time conflict cannot be resolved by choosing whichever clock validates the preferred root.

## 13. Trust-state integration

For PR #21:
- TrustStateHeadWitness determines structural trust-state currentness;
- generation is a bound lineage property, not standalone anti-rollback proof;
- time may constrain overlap/grace/certificate/delegation validity;
- stale/unwitnessed trust remains non-current regardless of time.

## 14. Write-admission integration

For PR #6:
- authority/currentness predicates remain independently established;
- freshness deadline computation binds exact time profile/source/session;
- caller-provided timestamps cannot extend validity;
- cached deadline evaluated under a different time-source session/profile is not reusable by default;
- uncertainty at an admission expiry boundary fails closed under the operation profile.

## 15. Snapshot/revalidation integration

For PR #12:
- dispatch-time revalidation binds a fresh structural state cut;
- if time-based freshness is required, it also binds a current time-source receipt;
- the dispatch receipt records both;
- neither a stale structural cut nor a stale time cut can be repaired by the other.

## 16. Causal-attribution integration

For PR #16:
- source event time, receive time, monotonic local sequence and transaction ordering remain separate;
- causal window width must be compared against clock uncertainty/skew;
- if the uncertainty/ordering ambiguity is larger than the causal distinction, causal attribution downgrades;
- sequence/happens-before evidence may be stronger than synchronized wall-clock ordering.

## 17. Evidence-retention integration

Retention/deletion requires:
- qualified current time if time-based;
- uncertainty margin;
- evidence-ledger dependency state;
- no unresolved transaction/ambiguity retention hold.

A forward clock jump cannot alone authorize irreversible deletion.

When time is uncertain, retain longer rather than deleting earlier where feasible.

## 18. Multiple time sources

A decision using multiple clocks MUST bind:
- each source identity/session;
- each uncertainty bound;
- known offsets/relationships;
- synchronization evidence;
- comparison profile.

If required clocks conflict beyond allowed bounds:
`TIME_SOURCE_CONFLICTING`.

Do not average or choose a convenient source unless the exact profile explicitly defines a safe algorithm.

## 19. Time-source failover

A failover node cannot assume its local clock is equivalent to the primary merely because both report similar wall time.

It should establish:
- its own time-source identity/session/currentness;
- required synchronization/uncertainty evidence;
- relation to protected structural currentness cut.

If time-dependent operations cannot establish those predicates, they block or narrow.

## 20. Time provider/config transition

Changing:
- synchronization provider;
- trust root used for authenticated time;
- clock service;
- leap handling;
- oscillator source;
- holdover profile

creates a new time-source/configuration generation where material.

Old time-read/currentness receipts do not silently transfer across that generation.

## 21. TemporalEvaluationCut

A future `TemporalEvaluationCut` may bind:
- structural currentness cut digest;
- exact time-source currentness receipt(s);
- operation/claim type;
- temporal policy/profile;
- evaluated boundaries;
- uncertainty treatment;
- result;
- cut digest.

This keeps structural and temporal evidence distinct while producing one reproducible decision input.

## 22. No universal time dependency

Not every operation requires qualified wall-clock time.

If a claim can be established using:
- protected lineage/witness currentness;
- monotonic local ordering;
- exact transaction sequence;
- no temporal expiry/effective predicate;

then unavailable wall-clock time need not create a false universal blocker.

The operation profile declares what time evidence is actually required.

## 23. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. expired approval is revived by rolling wall clock backward; reject.
2. structurally stale trust state has apparently valid time window; remain stale.
3. root witness says G3 but clock makes G1 effective interval appear current; G1 remains historical.
4. time source signed by current trust but trust's temporal validity depends on that same time source with no structural bootstrap; detect unresolved cycle.
5. post-reboot monotonic value is compared with prior boot; reject without bridge.
6. uncertainty interval crosses expiry; no exact fresh PASS.
7. two clocks disagree and permissive one is selected; reject/profile conflict.
8. failover node uses similar-looking local clock with no session/currentness proof; block time-dependent operation.
9. forward jump would permit retention deletion; require qualified temporal cut and uncertainty handling.
10. time provider changes but old currentness receipt is reused; reject generation/session mismatch.
11. cached PR #6 deadline from old clock session is reused after reboot; reject.
12. temporal approval is valid but transition predecessor witness is stale; transition still rejects.
13. structural transition/witness current, but not-before interval unresolved; remain pending temporally.
14. causal ordering is claimed from wall-clock difference smaller than combined uncertainty; downgrade.
15. operation has no time dependency and structural predicates are current; do not invent a wall-clock requirement.

## 24. Practical rule

> First establish structural identity, authority, lineage and protected currentness without circular reliance on the temporal predicate being tested. Then apply qualified time-source/session/uncertainty evidence only to the temporal boundaries the exact claim actually requires.

## 25. Authority boundary

This document does not:
- select/configure NTP/PTP/GPS;
- change host clocks;
- install synchronization software;
- choose a time provider;
- mutate credentials/trust roots;
- create a live time-currentness service;
- authorize machine writes;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
