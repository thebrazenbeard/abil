# ABIL Component Evidence Restoration Authority and Dependency Closure V1

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #4 component-conformance/evidence research at predecessor exact head `cd4f811ec9318231a3864fcedf4cd67befab07a7`.

This addendum responds to the exact-head hostile review finding that an evidence state can only be trustworthy if:
- upward restoration cannot launder claim ownership;
- the required dependency set is complete and provenance-bound;
- support envelopes cannot be broadened by an integrator without qualifying evidence;
- current-vs-historical evaluation has explicit temporal/currentness semantics.

It is research only. It does not implement an evidence engine or authorize certification, product selection, procurement, machine connection/write, commissioning, deployment, merge, or another protected effect.

## 1. Immutable evidence facts; derived claim state

The preferred model is:

1. preserve immutable evidence assertions and evidence subjects;
2. preserve immutable claim-definition subjects;
3. preserve immutable dependency-definition subjects;
4. preserve immutable envelope subjects;
5. compute claim disposition from those bound inputs under a versioned derivation profile;
6. persist the derivation receipt, not an independently authoritative mutable `green` badge.

A persisted prior result is historical evidence about a prior derivation cut. It is never current merely because the stored label was once green.

A current derived claim MUST be recomputable from:
- exact claim-definition digest;
- exact complete dependency-definition digest;
- exact evidence-subject set;
- exact envelope subjects;
- exact as-of/currentness cut;
- exact derivation-profile identity/version;
- exact derivation result.

## 2. Claim owner and evidence owner remain distinct

The existing claim-owner classes remain:
- `THIRD_PARTY_DIRECT`;
- `THIRD_PARTY_COMPOSITION_DEPENDENT`;
- `ABIL_OWNED`;
- `MACHINE_APPLICATION`.

Evidence ingestion does not transfer claim ownership.

ABIL MAY:
- store third-party evidence;
- content-address it;
- verify byte identity/signature/provenance;
- evaluate whether it applies to a declared ABIL composition;
- conservatively narrow an inherited scope.

ABIL MUST NOT, solely by ingestion or an ABIL-authored assertion:
- become the qualification owner of `THIRD_PARTY_DIRECT`;
- broaden a third-party qualification envelope;
- manufacture a replacement third-party certificate/conformance claim;
- restore a composition-dependent third-party claim outside the evidence class/source that owns it.

## 3. Upward evidence restoration requires an EvidenceRestorationReceipt

Any state transition from a weaker disposition to a stronger disposition requires an immutable `EvidenceRestorationReceipt` or mechanically equivalent subject.

It binds at least:
- claim ID and claim-definition digest;
- claim-owner class;
- old claim-state receipt digest;
- old evidence-subject set digest;
- new evidence-subject set digest;
- exact complete dependency-definition digest;
- exact dependency-resolution receipt digest;
- prior disposition;
- proposed disposition;
- restoring artifact identity/digest;
- restoring artifact evidence class;
- artifact issuer identity;
- issuer authority class;
- issuer scope/domain;
- evidence acquisition/verification procedure identity;
- verification result and evidence digest;
- exact envelope identity/digest, if any;
- exact effective/as-of/currentness cut;
- derivation-profile identity/version;
- independent verifier identity/profile where required;
- restoration result.

The restoration receipt cannot itself create the authority it claims.

## 4. Restoration authority matrix

### 4.1 THIRD_PARTY_DIRECT

A `THIRD_PARTY_DIRECT` claim can be restored only by:
- new/current evidence from the same qualification owner or an explicitly authorized successor authority; or
- a properly scoped independent test body whose evidence class is explicitly permitted by the claim definition as substitutable evidence.

ABIL-authored evidence MAY verify authenticity/applicability but cannot, by itself, restore the underlying third-party qualification owner claim.

### 4.2 THIRD_PARTY_COMPOSITION_DEPENDENT

Restoration requires:
- current applicable third-party component evidence for every component-level dependency the claim schema requires;
- current composition-specific evidence from the party/evidence class that owns the composition claim;
- exact composition identity and envelope;
- complete dependency closure.

An ABIL integration test may satisfy an ABIL-owned integration predicate but cannot silently relabel itself as the vendor's composition qualification.

### 4.3 ABIL_OWNED

ABIL-owned claims may be restored by ABIL-owned qualification evidence only when:
- the claim definition explicitly assigns ABIL as owner;
- the evidence procedure is accepted by the exact claim schema/profile;
- every non-ABIL dependency resolves to current/scope-compatible evidence;
- required independent verification is satisfied.

### 4.4 MACHINE_APPLICATION

Machine-application evidence requires the exact deployment/machine/application subject and its required commissioning/application evidence. Component or generic ABIL evidence cannot restore a machine-specific claim without the machine-application dependencies.

## 5. Stronger-state restoration is never label-driven

A receipt field such as:
- `RESTORED`;
- `PASS`;
- `CURRENT`;
- `SUPPORTED`;
- `VERIFIED`;

has no independent authority.

The stronger disposition is valid only if mechanically derived from admissible evidence under the exact owner/evidence-class/dependency/envelope/currentness rules.

An issuer may assert an evidence fact within its authority. The derivation profile determines whether that fact supports the target claim.

## 6. Closed required-dependency specification

Every derived claim that may be `UNCHANGED_SUPPORTED` or `SUPPORTED_WITHIN_DECLARED_ENVELOPE` MUST bind a versioned `RequiredDependencySpecification`.

The specification binds:
- claim ID;
- claim-definition version/digest;
- dependency-schema version;
- complete required dependency keys/classes;
- cardinality rules;
- optional versus required status;
- scope-compatibility rules;
- allowed evidence classes/owners for each dependency;
- envelope relationship rules;
- currentness rule for each dependency;
- conflict-resolution rule;
- derivation-profile version.

The system MUST NOT infer dependency completeness from whichever edges happen to be present in a graph.

Completeness is a separately evidenced predicate.

## 7. DependencyClosureReceipt

For each current derived-claim evaluation, a `DependencyClosureReceipt` binds:
- required-dependency specification digest;
- exact resolved dependency edge set;
- exact evidence subject for each required edge;
- edge owner/evidence class;
- edge scope and envelope;
- edge currentness result;
- unresolved/missing/conflicting edges;
- closure-completeness result;
- exact dependency-set digest.

Possible closure results:
- `COMPLETE_CURRENT_COMPATIBLE`;
- `COMPLETE_WITH_REVIEW_REQUIRED_EDGE`;
- `INCOMPLETE_REQUIRED_EDGE`;
- `CONFLICTING_REQUIRED_EDGE`;
- `SCOPE_INCOMPATIBLE_EDGE`;
- `CURRENTNESS_UNRESOLVED`.

A derived claim MUST NOT be `UNCHANGED_SUPPORTED` or `SUPPORTED_WITHIN_DECLARED_ENVELOPE` unless closure result is exactly `COMPLETE_CURRENT_COMPATIBLE` under the claim's derivation profile.

## 8. Missing or omitted required dependency

If a required dependency:
- is absent;
- is unknown;
- is unresolved;
- has no admissible evidence subject;
- has incompatible scope;
- has unresolved currentness;

then the dependency cannot disappear from the graph and cease to matter.

Minimum result:
- `REVIEW_REQUIRED` when the missing edge is a review-policy condition that does not determine truth.

Required result:
- `UNSUPPORTED_UNKNOWN` when the missing dependency is necessary to establish the truth/support of the target claim.

For high-consequence claims, unknown whether a dependency is necessary is itself `REVIEW_REQUIRED` or stronger fail-closed state until the claim definition resolves that uncertainty.

## 9. Dependency definition changes invalidate prior derived support

Adding, removing, reclassifying, changing cardinality, changing allowed evidence class, or changing currentness/envelope semantics for a dependency is a claim-definition/dependency-definition change.

A prior derived-state receipt bound to the predecessor dependency definition becomes historical-only.

It cannot be carried forward until the claim is re-derived under the new exact dependency definition.

This blocks laundering by deleting an inconvenient edge from a later graph.

## 10. Provenance-bound support envelopes

Every `SUPPORTED_WITHIN_DECLARED_ENVELOPE` result binds an immutable `EvidenceEnvelopeSubject`.

The envelope binds at least:
- envelope ID/version/digest;
- claim ID/owner class;
- evidence source/owner;
- issuer identity/authority;
- source artifact/evidence digest;
- exact dimensions/parameters/ranges;
- exclusions/prohibited combinations;
- interpretation/profile identity;
- temporal/currentness scope;
- any composition/device/firmware/OS/protocol/topology identity constraints.

A support state cannot cite an ambient or mutable envelope name.

## 11. Envelope narrowing versus widening

ABIL MAY conservatively narrow an inherited third-party envelope.

Such narrowing:
- creates an ABIL interpretation/narrowing subject;
- binds the original third-party envelope;
- cannot increase any range, add a supported dimension, remove an exclusion, or weaken a prohibited combination.

Widening third-party scope requires new qualifying evidence from the owner/evidence class permitted to establish that wider scope.

An ABIL-owned test can create an ABIL-owned claim about behavior outside the third-party envelope if properly qualified, but it cannot rewrite the third-party claim as broader.

## 12. Envelope comparison must be semantic

Envelope change is not determined by text or version number alone.

A comparison receipt SHOULD classify changes by dimension:
- narrower;
- equal;
- wider;
- incomparable;
- unknown.

`UNKNOWN` or `INCOMPARABLE` never authorizes inherited support without review/requalification according to the claim profile.

## 13. Current and historical evidence cuts are distinct

Every derived-claim evaluation binds an `EvidenceEvaluationCut`.

It identifies:
- evaluation mode: `CURRENT` or `HISTORICAL_REPLAY`;
- declared as-of/effective semantics;
- exact evidence subjects;
- exact dependency closure;
- exact envelope subjects;
- exact revocation/supersession information used;
- exact currentness resolver/profile;
- cut digest.

A later-discovered certificate or incompatibility does not rewrite what evidence existed at an earlier historical cut.

A historical cut does not become current merely because its evidence remains cryptographically valid.

## 14. Currentness and effective-time ordering

For current evaluation:
- lineage/supersession/revocation rules dominate stale persisted status;
- effective-time windows can narrow admissibility;
- unknown time/currentness cannot widen support;
- a newer applicable revocation/supersession subject prevents current support even if an older certificate remains within its printed date window;
- newly ingested evidence cannot retroactively prove that an old deployment was qualified at an earlier commissioning cut unless that evidence itself validly establishes such historical applicability.

For historical replay:
- use the explicitly bound historical cut;
- preserve later-discovered corrections separately;
- report the result as historical, not current.

## 15. Independent verification of upward transitions

A restoration that crosses a high-consequence boundary SHOULD require a verifier independent enough to detect issuer/ingestion error under the exact policy.

The verifier receipt binds:
- restoration receipt digest;
- evidence subject digests;
- dependency closure digest;
- envelope digest;
- currentness cut;
- verifier identity/profile/version;
- verification outcome.

"Independent" must be defined by the relevant claim profile. A different process name alone is not sufficient where both rely on the same unauthenticated source.

## 16. Derived claim state ceiling

Let:
- `C` = claim-definition admissibility;
- `D` = dependency-closure result;
- `E` = evidence-subject dispositions;
- `V` = envelope compatibility;
- `T` = temporal/currentness disposition;
- `A` = issuer/restoration authority admissibility;
- `R` = required independent verification result.

The derived claim disposition is bounded by the weakest required predicate.

No later stage may upgrade a weaker required predicate by local assertion.

## 17. Hostile acceptance cases

Future evidence-engine design/qualification SHOULD include at least:

1. ABIL writes an artifact labeled as restoring a vendor certificate; `THIRD_PARTY_DIRECT` restoration MUST fail.
2. Valid new vendor certificate, correct owner/scope, all dependencies current; restoration MAY succeed.
3. Delete an inconvenient required dependency edge from the observed graph while leaving claim schema unchanged; closure MUST be `INCOMPLETE_REQUIRED_EDGE`.
4. Change claim schema to remove that dependency; prior derived state becomes historical and MUST be re-derived.
5. Broaden a vendor envelope in an ABIL interpretation document; inherited vendor support MUST fail for the broadened region.
6. Narrow a vendor envelope conservatively; narrowed interpretation MAY remain supportable where all other predicates pass.
7. Use a valid but revoked/superseded evidence subject for current evaluation; current support MUST fail or downgrade per profile.
8. Reconstruct the old historical cut; historical result MAY reproduce without becoming current.
9. Present all evidence facts but omit a required independent verification receipt; stronger state MUST not be awarded when verification is required.
10. Persist a prior `SUPPORTED` label while changing a dependency/evidence subject; current derivation MUST ignore the stale label and recompute.

## 18. Relationship to existing PR #4 research

This addendum preserves the existing useful distinctions:
- evidence owner separation;
- direct versus composition-dependent versus ABIL-owned versus machine-application evidence;
- historical truth preservation;
- downgrade propagation;
- no certification inheritance by component presence alone.

It tightens upward movement and closure semantics. Where this addendum conflicts with earlier research wording about upward restoration or missing dependency metadata, this addendum is the proposed stronger research rule.

## 19. Authority boundary

This document does not:
- certify a component;
- accept a vendor claim;
- select a controller/runtime/OS/protocol stack;
- implement a qualification/evidence engine;
- purchase or license anything;
- connect to or write to a machine;
- perform commissioning;
- merge/canonically promote a branch;
- deploy anything.

Patrick remains sole authority for protected effects.
