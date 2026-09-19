# Component Evidence Definition Authority and Restoration Independence V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CERTIFICATION AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #4 predecessor exact head `1fd7767a6516dd9efab8eb6b74fdd8f97cf23407`.

This companion responds to Thirteen's exact-head hostile review of the predecessor.

The predecessor already closed:
- evidence-owner separation;
- dependency-closure completeness;
- envelope provenance;
- current-vs-historical evidence cuts;
- stale-state recomputation.

The remaining authority question is one level higher:

> Who is allowed to define or change the claim schema, dependency specification, envelope semantics, and restoration policy that determine what counts as a valid derived claim?

Without that authority boundary, an integrator could remove an inconvenient dependency from a new definition and then legitimately re-derive a green result under the weakened definition.

## 1. Claim-policy subject

Treat the following as one versioned governed policy subject:

`EvidenceClaimPolicySubject`

It binds at least:
- claim ID;
- claim-owner class;
- claim-definition version/digest;
- RequiredDependencySpecification digest;
- EvidenceEnvelope semantic/profile digest;
- restoration-authority matrix/profile digest;
- evidence-class admissibility rules;
- currentness rules;
- independence-verification policy;
- scope;
- predecessor policy digest;
- policy authority class;
- immutable policy digest.

Derived evidence state depends on both:
- admissible evidence;
- exact authorized policy subject.

A valid evidence set cannot compensate for an unauthorized policy definition.

## 2. Definition authority is separate from evidence authority

Distinguish:
- authority to issue evidence;
- authority to define what evidence a claim requires;
- authority to change that definition;
- authority to verify the resulting derivation.

These may be held by different principals.

A producer that can supply evidence does not automatically own the claim schema.

An integrator that can evaluate a claim does not automatically own the external claim definition.

## 3. ClaimDefinitionAuthorityReceipt

Every new or changed `EvidenceClaimPolicySubject` requires a `ClaimDefinitionAuthorityReceipt` or mechanically equivalent protected subject.

It binds at least:
- policy/claim ID;
- exact predecessor policy digest;
- proposed successor policy digest;
- claim-owner class;
- policy-authority identity;
- policy-authority class;
- exact semantic delta;
- changed dependency keys/cardinality;
- changed evidence-class rules;
- changed envelope rules;
- changed currentness rules;
- changed restoration/independence rules;
- scope;
- weakening/widening classification;
- required approvals/independent review;
- actual approval evidence;
- effective/currentness cut;
- verification result;
- immutable receipt digest.

A new definition is not legitimate merely because it has a new version number or schema digest.

## 4. Unauthorized definition changes fail closed

If the policy change:
- lacks a valid predecessor binding;
- lacks admissible authority;
- has unresolved owner provenance;
- exceeds authority scope;
- changes required semantics without required approvals;
- cannot classify whether it weakens/widens the claim;

then:
`DEFINITION_AUTHORITY_UNRESOLVED`.

A claim evaluated under such a policy cannot receive a stronger/current supported disposition.

Historical evidence and historical policy records remain preserved.

## 5. THIRD_PARTY_DIRECT definition authority

For `THIRD_PARTY_DIRECT` claims:

ABIL MUST NOT redefine the external owner's claim by:
- deleting owner-required predicates;
- changing owner-required evidence classes;
- widening supported ranges;
- removing owner exclusions;
- changing conformance meaning;
- changing certificate applicability semantics.

ABIL MAY:
- preserve the exact owner definition;
- create a local narrower interpretation;
- add extra ABIL requirements;
- mark owner semantics unknown/unavailable.

Any local narrower interpretation is a separate ABIL interpretation subject and MUST retain the original owner policy reference.

It cannot be presented as the external owner's redefined claim.

## 6. THIRD_PARTY_COMPOSITION_DEPENDENT definition authority

For composition-dependent external claims:

ABIL MAY bind the exact external composition requirements into a local evaluation profile.

ABIL MUST NOT:
- remove owner-required components/dependencies;
- change required compatibility conditions;
- relabel ABIL integration evidence as owner composition qualification;
- widen owner composition scope.

An external owner update creates a new external policy subject.

A local policy must either:
- bind that new owner policy;
- remain explicitly historical;
- or enter review/unsupported state.

## 7. ABIL_OWNED claim definition authority

For `ABIL_OWNED` claims, ABIL may define and change the claim policy only through the separately governed ABIL policy-authority process.

Policy change authority SHOULD bind:
- role;
- scope;
- predecessor;
- semantic delta;
- required review;
- currentness.

A learner/candidate/evaluator that benefits from a weaker claim MUST NOT unilaterally weaken the policy.

## 8. MACHINE_APPLICATION claim definition authority

Machine/deployment-specific claim definitions may require:
- ABIL policy authority;
- commissioning/deployment authority;
- customer/site-specific authority;
- independent safety governance where applicable.

A generic ABIL policy author cannot silently remove machine-specific commissioning, safety, or control-coverage predicates.

## 9. Semantic weakening and widening classification

Every policy delta should classify whether it:

- adds a requirement;
- removes a requirement;
- narrows scope;
- widens scope;
- relaxes evidence quality;
- strengthens evidence quality;
- changes owner class;
- changes currentness semantics;
- changes independence requirements;
- changes restoration authority.

Unknown classification:
`POLICY_DELTA_SEMANTICS_UNKNOWN`.

Unknown semantic impact blocks stronger/current derivation until reviewed.

## 10. Dependency removal is a high-risk semantic change

Removing a required dependency is never treated as a cosmetic schema edit.

It requires:
- exact predecessor dependency definition;
- reason;
- owner/authority basis;
- proof the dependency is no longer required for the claim;
- required independent review according to policy;
- invalidation/re-derivation of dependent claims.

A policy author cannot delete an edge simply to make closure pass.

## 11. Envelope change authority

Evidence envelopes are also policy.

A wider envelope, weaker exclusion, removed prohibited combination, or changed identity applicability must be authorized under the same policy authority.

Local ABIL interpretation MAY narrow an inherited third-party envelope without changing the external owner's policy.

Any widening requires qualifying evidence + authority allowed to define the wider claim.

## 12. Restoration authority matrix is policy

The restoration-authority matrix itself cannot be modified by the actor performing a restoration in order to validate that restoration.

A change to:
- who may restore;
- which evidence class is substitutable;
- required verifier independence;
- currentness rules;

is a policy change requiring a ClaimDefinitionAuthorityReceipt.

## 13. High-consequence independence policy is explicit and fail-closed

Replace open-ended `SHOULD` semantics with:

For any claim class designated `HIGH_CONSEQUENCE`, the claim policy MUST bind an explicit `RestorationIndependencePolicy`.

It defines at least:
- which upward transitions require independent verification;
- required independence dimension(s);
- prohibited shared failure domains;
- allowed deterministic same-implementation proof classes;
- verifier role/profile;
- evidence required to establish independence;
- exceptions, if any, and their authority basis.

If the policy is missing, unknown, stale, or unauthorized:
`RESTORATION_INDEPENDENCE_POLICY_UNRESOLVED`.

No high-consequence upward restoration may proceed.

## 14. Independence means more than a second process name

Potential independence dimensions include:
- separate implementation;
- separate operator/principal;
- separate trust domain;
- separate data path;
- separate evidence source;
- separate runtime/failure domain;
- separately verifiable proof object.

The exact claim policy specifies which are required.

A differently named process that shares the same defective implementation/data source does not automatically satisfy independence.

## 15. Deterministic independently checkable proofs

A same-implementation verifier MAY be acceptable only when the proof class itself is independently checkable and the claim policy explicitly permits it.

Examples might include:
- deterministic cryptographic inclusion proof;
- recomputable canonical digest proof;
- formally specified dependency-closure proof;
- deterministic paired replay with exact frozen evaluator/profile.

This is policy-scoped, not a generic shortcut.

## 16. Derived claim receipt V2

A derived claim result should bind:
- exact EvidenceClaimPolicySubject digest;
- ClaimDefinitionAuthorityReceipt digest;
- exact evidence-subject set;
- DependencyClosureReceipt;
- envelope subject;
- currentness/evaluation cut;
- restoration receipt if upward transition;
- RestorationIndependencePolicy digest;
- independent verification receipt where required;
- derivation profile;
- final disposition;
- immutable receipt digest.

A stored green label lacking the exact authorized policy binding is non-authoritative.

## 17. Policy currentness

Policy subjects themselves may be:
- CURRENT;
- HISTORICAL;
- SUPERSEDED;
- REVOKED;
- CONFLICTING;
- AUTHORITY_UNRESOLVED.

Current derivation MUST bind the current applicable policy cut.

Restoring an old policy must not reactivate a weaker definition after a stricter successor was authorized.

The currentness mechanism is a future implementation subject; this research defines the required semantics only.

## 18. Policy fork/conflict

If two incompatible policy successors claim the same predecessor/scope and no authorized reconciliation resolves them:

`CLAIM_POLICY_CONFLICTING`.

Do not:
- union requirements selectively;
- choose the weaker policy;
- choose the policy that makes the claim green;
- choose by timestamp/version number alone.

Affected stronger claims fail closed until policy currentness is resolved.

## 19. Historical policy verification

Historical evidence may be re-evaluated under:
- the policy that was current at the historical cut;
- a newer policy for retrospective analysis.

These are distinct results.

A newer stricter policy does not rewrite what was historically believed.

An old weaker policy does not authorize current claims after supersession.

## 20. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. integrator deletes a failing required dependency and publishes v2 schema; no authority receipt => `DEFINITION_AUTHORITY_UNRESOLVED`.
2. third-party direct claim is locally redefined with fewer owner predicates; external claim inheritance rejected.
3. ABIL narrows a vendor envelope while retaining owner policy reference; allowed if all other predicates pass.
4. ABIL widens vendor envelope without qualifying owner/allowed authority; reject.
5. restoration actor modifies restoration matrix to authorize itself; reject circular policy change.
6. high-consequence claim lacks independence policy; restoration fails closed.
7. independence policy says separate implementation required but verifier is same code under different process name; reject.
8. policy explicitly permits deterministic same-implementation proof with independently checkable proof object; may pass if proof validates.
9. old weaker policy restored after stricter successor; old policy remains historical.
10. two conflicting policy successors exist; do not pick convenient one.
11. dependency removed with no semantic proof/approval; stronger claim rejects.
12. machine-specific safety predicate removed by ordinary ABIL policy author; reject scope/authority.
13. evidence is valid but policy authority unresolved; claim cannot be CURRENT_SUPPORTED.
14. policy version/digest changes but semantic delta omitted; policy change unresolved.
15. historical result under old policy remains historical while current derivation uses current policy.

## 21. Practical rule

> Dependency closure is trustworthy only when the dependency/claim policy itself is an authorized, provenance-bound subject. Evidence cannot rescue an unauthorized definition, and a new definition cannot launder away an inconvenient predicate.

## 22. Authority boundary

This document does not:
- authorize any real claim-definition change;
- certify a component;
- select products;
- implement an evidence/policy engine;
- mutate vendor policy;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
