# Evidence Producer Chain Provenance and Trust-Cut Composition V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH / NO IMPLEMENTATION OR CREDENTIAL AUTHORITY**

Date: 2026-09-19

Applies to Draft PR #20 predecessor exact head `6ee8a9d252cd1c4d1243e861c650b0e6629fb872`.

This companion reconciles producer authenticity with:
- PR #18 evidence-ledger integrity;
- PR #21 protected trust-state currentness;
- PR #22 transition authorization;
- PR #23 governance-root currentness;
- PR #24 time-source currentness.

It also closes a producer-chain seam:

> Authentication of a transport/session/envelope signer does not automatically authenticate the originator of the evidence payload carried inside that envelope.

## 1. Distinguish provenance roles in the producer chain

A future evidence object may involve several different principals:

- `claimed_origin_producer`;
- `authenticated_origin_producer`;
- `observer_or_collector`;
- `transformer_or_normalizer`;
- `gateway_or_transport_signer`;
- `checkpoint_or_batch_signer`;
- `verifier`.

These roles MUST NOT be collapsed into one generic `producer` identity.

A gateway that signs a record it received proves, at most, what the gateway can truthfully attest under its role and evidence profile.

It does not automatically prove the device, technician, evaluator, or other claimed originator created the underlying content.

## 2. Origin-authentication dispositions

Suggested origin-specific dispositions:

- `ORIGIN_AUTHENTICATED_CURRENT`;
- `ORIGIN_AUTHENTICATED_HISTORICAL`;
- `ORIGIN_ATTESTED_BY_TRUSTED_INTERMEDIARY`;
- `TRANSPORT_AUTHENTICATED_ORIGIN_UNVERIFIED`;
- `ORIGIN_SCOPE_MISMATCH`;
- `ORIGIN_CONFLICTING`;
- `ORIGIN_UNVERIFIED`.

A stronger origin claim MUST NOT be inferred from a weaker transport/envelope claim.

## 3. Envelope authenticity is a different predicate

A signed transport/session/envelope may establish:

- sender/session identity;
- message integrity after signing;
- replay/session properties;
- delivery path identity.

It does not by itself establish:

- who originally measured/observed the evidence;
- whether the payload was transformed before signing;
- whether an imported legacy record is authentic;
- whether the signer had authority to attest the claimed origin;
- whether the signer preserved the complete original evidence.

Therefore keep separate:

- `ENVELOPE_AUTHENTICITY`;
- `PAYLOAD_INTEGRITY`;
- `ORIGIN_AUTHENTICITY`;
- `ROLE_SCOPE_AUTHORITY`.

## 4. Intermediary-attested origin

Some protocols cannot authenticate the endpoint/device directly.

A trusted gateway may be permitted to attest:

> I observed bytes/state X from endpoint Y over protocol/session Z under profile P.

That is not identical to:

> Endpoint Y cryptographically signed X.

An `IntermediaryOriginAttestation` or equivalent should bind at least:

- intermediary identity;
- intermediary role/scope;
- endpoint/claimed-origin identity;
- protocol/session identity;
- exact raw observed bytes or canonical observation digest;
- collection timestamp/order evidence;
- transformation status;
- source-address/identity-resolution evidence;
- verifier/trust cut;
- attestation limitations.

The resulting evidence ceiling must reflect the attestation class actually established.

## 5. Transformation provenance

If evidence is:
- decoded;
- normalized;
- unit-converted;
- aggregated;
- filtered;
- summarized;
- translated;
- mapped to semantic tags;
- corrected;

then the authenticity chain should bind the transformation.

A future `EvidenceTransformationRecord` may bind:

- exact input digest(s);
- exact output digest;
- transformer identity;
- transformer role;
- transformation profile/version;
- parameters/units;
- lossiness/reversibility classification;
- timestamp/order evidence where material;
- verifier result.

The output may be authentic as a transformation produced by the transformer while remaining weaker evidence of the original real-world event.

## 6. Raw evidence and interpreted evidence remain distinct

For high-consequence claims, retain separable subjects where feasible:

- raw observation/evidence;
- parsed/decoded form;
- semantic interpretation;
- causal interpretation;
- currentness/qualification decision.

An authenticated parser/evaluator cannot retroactively make the raw source authenticated if the raw source origin was unverified.

Likewise, an authenticated raw device receipt does not prove a later semantic interpretation is correct.

## 7. Exact record-subject binding

Producer authenticity MUST bind the exact evidence subject being verified.

The authenticity receipt should include:

- exact record/checkpoint digest;
- schema/canonicalization profile;
- referenced raw/source object digests;
- transformation-chain digest where applicable;
- producer-chain digest;
- exact claim/evidence class;
- exact scope/deployment.

This blocks a valid signature over one representation from being reused as proof for a materially different normalized/derived object.

## 8. Current trust-state cut is mandatory for new evidence acceptance

For current producer evidence, bind the exact PR #21-style trust currentness subject:

- trust-state node digest;
- `TrustStateHeadWitness` digest;
- verifier profile;
- producer key/material identity;
- role/scope/delegation state;
- revocation/supersession state;
- trust-currentness receipt.

Local trust-store state alone is not sufficient.

A credential accepted under restored stale trust MUST NOT produce `AUTHENTICATED_CURRENT`.

## 9. Governance root is a separate dependency

Where producer trust depends on governed trust-state transitions, bind the exact PR #23-style governance-root currentness evidence:

- GovernanceRootAnchor;
- GovernanceRootHeadWitness;
- root scope;
- relevant transition-policy profile.

A current trust-state node whose governance lineage cannot be grounded in the current root cannot silently establish current producer eligibility.

## 10. Historical authenticity requires a historical trust cut

Historical authenticity SHOULD bind:

- evidence record digest;
- producer identity/material;
- historical trust-state node;
- historical transition/governance lineage;
- creation/order evidence;
- revocation/compromise semantics;
- verifier profile used for historical evaluation;
- explicit `HISTORICAL` disposition.

Historical authenticity does not update current trust heads or producer eligibility.

## 11. Creation time is not self-proved by the producer

A producer's own timestamp cannot be the sole evidence that its record predates revocation/expiry/compromise.

Historical creation/as-of support may come from:

- qualified time-source receipt;
- protected ledger/checkpoint sequence;
- trusted gateway receive sequence;
- device monotonic counter;
- externally witnessed batch;
- other independently qualified ordering evidence.

If historical timing is material and cannot be grounded, the historical claim ceiling must downgrade.

## 12. Trust↔time circularity is prohibited

If producer trust validity depends on time, and the time source is authenticated using that producer trust domain, do not allow the cycle to self-justify.

Use the PR #24 structural-first rule:

1. establish structural trust/root/currentness without relying on the temporal predicate currently under evaluation;
2. establish admissible time-source identity/currentness;
3. then evaluate expiry/not-before/compromise windows.

If the cycle cannot be broken by an independent structural/bootstrap path, fail closed or downgrade.

## 13. Delegation chain currentness

When producer P is accepted through delegation:

- bind every delegation edge;
- bind each delegator/delegate identity;
- bind evidence role/class;
- bind deployment/scope;
- bind onward-delegation permission;
- bind validity/currentness;
- bind revocation state;
- bind the current trust/root cut.

A valid leaf credential cannot widen a parent delegation.

A restored historical delegation cannot re-enable current evidence production.

## 14. Shared credentials do not prove distinct producers

If multiple nominal producers share one authentication key/session identity, cryptographic authentication may prove possession of the shared credential but not which human/device/role created the record.

The evidence ceiling must reflect this ambiguity.

Do not use shared credential possession to satisfy:
- independent reviewer quorum;
- distinct-role threshold;
- dual-control requirement;
- producer separation required by a claim.

## 15. Quorum counts authenticated principals, not labels

Where multiple independent producers/reviewers are required:

- distinct logical labels are insufficient;
- distinct authenticated principals must satisfy the policy;
- common-control/common-key restrictions must be evaluated;
- one principal cannot count twice unless the policy explicitly allows role multiplexing.

The quorum receipt binds exact identities, roles, and independence profile.

## 16. Checkpoint/batch signatures do not prove omitted records

A signed batch/checkpoint may authenticate:
- checkpoint signer;
- exact included root/manifest;
- included records if inclusion is mechanically proven.

It does not prove:
- no required partition was omitted;
- completeness across required evidence classes;
- authenticity of individual origins when only the checkpoint signer is authenticated.

PR #18 ledger-completeness predicates remain independently required.

## 17. Target/device identity resolution

For device-origin claims, separate:

- protocol address;
- configured logical ID;
- physical device identity;
- authenticated endpoint/session identity;
- hardware/key identity where available.

Same address after replacement does not prove same producer.

An authenticity receipt must bind the identity domain actually established.

## 18. Human evidence binding

High-consequence human evidence should distinguish:

- account identity;
- authenticated session;
- person/organizational principal;
- assigned role;
- deployment scope;
- workstation/device where material;
- exact reviewed evidence object;
- exact action/signoff intent.

A session account or display name alone may be insufficient for person-level or independent-role claims.

## 19. Evaluator/reviewer evidence

Evaluator/reviewer authenticity should bind:

- exact evaluator/reviewer principal;
- evaluator profile/build;
- subject head/digest;
- evidence cut;
- result;
- evidence ceiling;
- independence profile where required.

Authentic evaluator identity does not by itself prove evaluator independence.

Independence is a separate claim.

## 20. Safety evidence remains independently governed

Ordinary ABIL trust/root/currentness cannot be reused to authenticate safety evidence unless the safety project explicitly defines that trust relationship.

A safety receipt should bind:
- safety governance root/currentness;
- exact safety producer role;
- exact deployment/scope;
- independent safety policy.

No ordinary producer-chain shortcut may promote non-safety evidence into safety authority.

## 21. EvidenceAuthenticityReceipt V2

A future receipt SHOULD bind at least:

- exact evidence subject digest;
- evidence class;
- claimed origin producer;
- authenticated origin producer, if established;
- intermediary/collector/gateway signer identities;
- transformation-chain digest;
- producer role/scope;
- delegation-chain digest, if any;
- trust-state node + TrustStateHeadWitness;
- governance-root/root-witness evidence where required;
- verifier identity/profile;
- canonicalization profile;
- historical/current mode;
- time/order evidence where material;
- compromise/revocation result;
- origin-authenticity disposition;
- transport/envelope-authenticity disposition;
- limitations/evidence ceiling;
- immutable receipt digest.

The receipt cannot upgrade a missing predicate by label.

## 22. Current versus historical claim matrix

### Current new-evidence acceptance
Requires:
- current structural trust/root state;
- current role/scope/delegation;
- exact record binding;
- required time predicates if any.

### Historical authenticity
Requires:
- historical trust/governance cut;
- creation/order support appropriate to revocation semantics;
- explicit historical-only result.

### Transport-only authenticity
May remain useful evidence but cannot become authenticated origin.

### Unverified origin
May remain low-ceiling evidence if policy permits, with limitations preserved.

## 23. Hostile acceptance cases

Future implementation/review SHOULD include at least:

1. trusted gateway signs a forged payload claiming device D originated it; transport authentic, origin unverified.
2. gateway truthfully attests raw bytes from D but D has no native auth; result is intermediary-attested origin, not device-signed origin.
3. parser normalizes signed raw bytes into materially different semantic value without transformation binding; stronger claim rejects.
4. valid producer credential is accepted from a restored stale trust store; current authenticity rejects.
5. historical record predates revocation only according to producer's own untrusted clock; historical timing unresolved.
6. time source is authenticated by the same temporal trust predicate it is used to validate; circularity rejects.
7. shared key is used by two nominal reviewers to satisfy 2-of-2 quorum; reject independence.
8. signed checkpoint omits required negative-evidence partition; authenticity does not repair completeness.
9. device at same protocol address is replaced; old identity must not transfer automatically.
10. current trust state valid but governance-root witness stale/conflicting; new producer eligibility unresolved.
11. historical trust material verifies old record; record stays historical and cannot mint current producer authority.
12. delegation chain contains one expired/revoked/wrong-scope edge; leaf producer current eligibility rejects.
13. authenticated evaluator review exists but reviewer independence is unproven; authenticity PASS does not imply independent review PASS.
14. safety-shaped record is signed under ordinary ABIL producer trust; safety role rejects.
15. envelope is signed after payload alteration; exact payload/canonical record binding detects mismatch.
16. transformation output is authentic as transformer output but original source origin remains unverified; claim ceiling remains bounded.

## 24. Relationship to the trust chain

PR #18:
- proves ledger integrity/completeness properties.

PR #20:
- proves origin/intermediary/transport producer authenticity at bounded claim ceilings.

PR #21:
- establishes current evidence-trust state via protected witness.

PR #22:
- establishes whether trust-state transitions were authorized.

PR #23:
- externally anchors and currentness-protects the governance root.

PR #24:
- supplies qualified temporal evidence where exact claims require it.

No layer substitutes for another.

## 25. Practical rule

> Strong producer-authenticity claims must bind the exact evidence subject to an authenticated origin or explicitly bounded intermediary attestation, through the exact current or historical trust/governance cut. A trusted envelope signer, collector, transformer, timestamp, or checkpoint cannot silently become proof of a different producer or stronger provenance class.

## 26. Authority boundary

This document does not:
- select cryptography/PKI/provider;
- create/rotate/revoke credentials;
- provision roots;
- implement authentication;
- authorize safety evidence;
- authorize machine connection/write;
- merge or deploy anything.

Patrick remains sole authority for protected effects.
