# ABIL Research Integration / Claim Lattice V2

Status: **IP_CONFIDENTIAL / NON-NORMATIVE RESEARCH INTEGRATION MAP / PRIVATE ABIL SOURCE / NO IMPLEMENTATION PLAN / NO MERGE OR DEPLOY AUTHORITY**

Date: 2026-09-19

Architecture base:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Purpose:

> Make the current ABIL research portfolio reviewable as a dependency lattice of bounded claims through PR #24 without turning research dependencies into implementation authority, merge order, or a readiness score.

This V2 companion supersedes V1 only as the newer integration map.
It does not rewrite or absorb the underlying PR subjects.

## 1. Authority and design anchors

### PR #2 — successor architecture

Exact subject:
`712d5b30b45ba9299dcfce0599878cb81db70e8f`

Role:
- architecture separation;
- lifecycle/authority contract;
- typed intervention/evidence boundaries;
- orthogonal product/deployment/authority/artifact/recovery state;
- deny-by-default authority and safety-classification separation.

Current status:
- exact-head independent architecture review/reconciliation still pending.

### PR #3 — R2 written design / R6

Exact subject:
`1da5bc57b0228178300f6ba966d97d1dce807dc1`

R6 companion:
`docs/superpowers/specs/2026-09-19-abil-r2-review-corrections-r6.md`

Role:
- final written-design subject for the non-actuating R2 substrate/reconstruction path;
- evaluator-context identity/equivalence;
- authorization-scoped evaluator evidence;
- coherent evaluator-context cuts;
- generation/lineage-over-wall-clock currentness.

Hard governance gate:

> If exact-head peer review and One reconciliation become clean, STOP before implementation planning and obtain Patrick's explicit final written-design acceptance.

No research subject in this lattice bypasses that gate.

### PR #6 — write-capability admission design

Exact subject:
`b191822ecbc95ce120384acf1c17289b4b834033`

Disposition:
`DESIGN_GOVERNANCE_CONTRACT_PASS`

Role:
- exact write-admission subject;
- independently resolved authority/currentness surfaces;
- freshness/canonicalization/profile binding;
- multi-surface reconciliation;
- fail-closed write-admission semantics.

Ceiling:
written contract only.
No executable validator, current-authority reader, commissioning, or write authority follows from this PASS.

## 2. Evidence and qualification layer

### PR #4 — component/runtime evidence research

Exact subject:
`1fd7767a6516dd9efab8eb6b74fdd8f97cf23407`

New V2 repair:
`docs/research/2026-09-19-component-evidence-restoration-authority-and-dependency-closure-v1.md`

Role:
- third-party direct vs composition-dependent vs ABIL-owned vs machine-application evidence;
- evidence invalidation;
- owner/evidence-class constrained restoration;
- complete RequiredDependencySpecification;
- DependencyClosureReceipt;
- provenance-bound support envelopes;
- current vs historical evidence cuts.

Feeds:
- product capability/currentness;
- PR #9 cross-axis consistency;
- PR #11 currentness proof;
- PR #19 portfolio claim ceilings.

### PR #5 — source-optional reconstruction benchmark

Exact subject:
`385207c1bff5189651c1048f2d09f3805d751873`

Role:
- falsifiable source-optional reconstruction research;
- synthetic fixture/preregistration;
- evidence package;
- competent baselines;
- hostile benchmark validation.

Ceiling:
research only.
`REPLACEMENT_CONTROL_READY` is non-awardable.

## 3. Operational currentness chain

### PR #7 — deployment commissioning currentness

Exact subject:
`a62ae16a0c1bc484ae6b45e4af853af64a2e6707`

Role:
- topology/semantic/commissioning/control-coverage/target-behavior/cutover/support evidence;
- partial/full recommission;
- machine/deployment-specific currentness.

### PR #8 — support/recovery currentness

Exact subject:
`7d11cea51bfff3f2bf32e98516479be4d742d172`

Role:
- manual recovery;
- rollback/restore;
- hardware replacement;
- degraded operation;
- non-operating fallback.

Key rule:
restoring bytes does not restore authority/currentness.

### PR #9 — cross-axis state consistency

Exact subject:
`90d40f4baca29629f8f17f956f20687fee674820`

Role:
`OperationalStateVector = (product, deployment, authority, artifact, recovery)`

Adds:
- no cross-axis implication;
- requested-operation predicate;
- ownership/fencing overlay;
- ambiguity overlay;
- safety-classification overlay;
- coherent currentness cuts.

### PR #10 — dependency-cycle resolution

Exact subject:
`5e15ed24fc5f9286eb21377e0532f6d88e8a1840`

Role:
- exact currentness dependency graph;
- SCC/cycle detection;
- independent leaf evidence;
- jointly qualified bundles;
- no mutual self-justification.

### PR #11 — non-authority currentness proof

Exact subject:
`fcb0a88b0a37a9c7c722fe0e5f966a7a3f968bc3`

Role:
- machine-checkable currentness receipts for deployment/coverage/recovery/safety/product dependencies;
- identity vs currentness separation;
- independent invalidation/freshness resolution;
- self-attestation boundary.

### PR #12 — snapshot / dispatch revalidation

Exact subject:
`3d61f4da301af41f4d56bbcffb4609c38b815bd3`

Role:
- decision-time vs dispatch-time TOCTOU;
- required-subject read sets/version vectors;
- dispatch-time revalidation;
- atomic/optimistic/target-guard mechanisms;
- operation-specific currentness cut.

Key rule:
admissibility applies only to the exact checked state vector while it remains current.

## 4. Physical transaction-safety chain

### PR #13 — effect-intent binding / anti-replay

Exact subject:
`8ab8ee9e95c86a04c4d34a8042e13b05979d6364`

Role:
- exact transaction/request/target/semantic operation/parameters/precondition binding;
- execution cardinality;
- replay protection;
- batch/session semantics.

### PR #14 — replay-ledger anti-rollback

Exact subject:
`fc9846e3eb82e3b0c8eccbf42769b09ba7eaaa2c`

Role:
- consumed requests cannot become unused after restore;
- same-authority-generation replay rollback;
- failover/dedup/session/batch replay state.

### PR #15 — dispatch commit ordering

Exact subject:
`88f1a232a7265e8713e4564260b28e35cf53369e`

Role:
- durable pre-dispatch reservation;
- conservative effect-may-occur boundary;
- crash-window classification;
- known-no-effect proof;
- HA/storage ordering.

### PR #16 — execution evidence / causal attribution

Exact subject:
`ac36991d6c54dfa870aca7c64d05a980a034c10c`

Role:
dispatch -> delivery -> acceptance -> target report -> readback -> physical observation -> causal attribution.

Key rule:
execution, observation, and causation remain separate evidence layers.

### PR #17 — transaction reconciliation / late evidence

Exact subject:
`1837c6b6c47225fd02674ea7e735caef0f83e97b`

Role:
- append-only reconciliation of delayed receipts/observations;
- no return to UNUSED;
- retry eligibility separate from historical execution conclusion;
- partial/conflicting effect preservation.

### PR #18 — evidence-ledger integrity / continuity

Exact subject:
`8d7ffe6650136b7a2037206da75a665235324a16`

Role:
- record integrity vs ledger completeness;
- gap/truncation/selective-restore detection;
- negative/conflicting evidence preservation;
- replica/restore/retention/compaction boundaries;
- exact evidence-cut binding.

## 5. Producer, trust, governance and time chain

### PR #20 — evidence producer authenticity

Exact subject:
`dfb66be6b39ee66a270f1f29fd25de24790affb1`

V2 companion:
`docs/research/2026-09-19-evidence-producer-chain-provenance-and-trust-cut-v2.md`

Role:
- claimed origin vs authenticated origin vs intermediary/transport/transformer identity;
- producer role/scope;
- trust-domain separation;
- historical authenticity vs current producer eligibility;
- verifier identity/profile;
- envelope authenticity vs origin authenticity;
- producer-chain/transformation provenance;
- shared-credential/quorum boundaries;
- compromise/rotation/revocation semantics.

Key rule:
ledger integrity does not prove producer authenticity.

### PR #21 — trust-state currentness / anti-rollback V2

Exact subject:
`2b4d5da33d9ce7dfe4d13c44a07bcd2f1c469120`

V2 companion:
`docs/research/2026-09-19-trust-state-protected-head-witness-and-transition-authority-v2.md`

Role:
- immutable trust-state nodes;
- separately protected `TrustStateHeadWitness`;
- fork/conflict handling;
- restore/failover anti-rollback;
- transition-authority requirement;
- multi-scope coherent cuts;
- current vs historical trust separation.

Key rule:
local maximum generation is not currentness proof.

### PR #22 — trust-state transition authorization V2

Exact subject:
`4933e0fdbee0c472faf9ba49b9659ae04efedc35`

V2 companion:
`docs/research/2026-09-19-trust-state-transition-authorization-composition-v2.md`

Role:
- exact predecessor authorization;
- current GovernanceRootAnchor/policy binding;
- proposer/authorizer/quorum/scope rules;
- authorization vs commit-currentness separation;
- protected trust-head witness advancement;
- competing-successor behavior.

Key rule:
an authorized successor is not current until the protected trust-state witness uniquely commits it.

### PR #23 — governance root/bootstrap boundary V2

Exact subject:
`705e0a9c2aa0143091761a2eb875213e1c24832e`

V2 companion:
`docs/research/2026-09-19-governance-root-protected-currentness-witness-v2.md`

Role:
- external `GovernanceRootAnchor`;
- bootstrap authority boundary;
- separately protected `GovernanceRootHeadWitness`;
- root restore/failover anti-rollback;
- root fork/conflict;
- external root-transition authorization;
- ordinary trust vs governance-root vs safety-governance separation.

Key rule:
authentic historical root bytes do not prove current governance.

### PR #24 — time-source currentness / ordering V2

Exact subject:
`57039cecbc8aa8bbf41ae2bf56a037d50a03db5b`

V2 companion:
`docs/research/2026-09-19-time-source-currentness-and-trust-ordering-composition-v2.md`

Role:
- wall vs monotonic separation;
- source/session/currentness/uncertainty;
- rollback/jump/reboot/holdover;
- structural-first trust/time evaluation;
- trust↔time cycle rejection;
- uncertainty-aware temporal boundaries;
- `TemporalEvaluationCut`.

Key rule:
protected lineage/witness currentness is structural; time may only narrow temporal admissibility for claims that require it.

## 6. Integrated dependency graph

Conceptual high-level graph:

```text
PR2 architecture
 |-------------------------------|
 |                               |
 v                               v
PR4 product/component evidence   PR5 reconstruction research
 |
 +--> PR7 deployment currentness -----------+
 |                                          |
 +--> PR8 recovery currentness -------------+--> PR9 cross-axis state
                                                |
                                                v
                                             PR10 cycle-safe dependencies
                                                |
PR6 write admission -------------------------->PR11 currentness proof
                                                |
                                                v
                                             PR12 dispatch revalidation
                                                |
                                                v
                                             PR13 effect intent
                                                |
PR8 recovery -------------------------------->PR14 replay anti-rollback
                                                |
                                                v
                                             PR15 dispatch ordering
                                                |
                                                v
                                             PR16 execution/causal evidence
                                                |
                                                v
                                             PR17 late reconciliation

PR18 evidence-ledger integrity cross-cuts PR5/11/12/14/16/17.

PR18 --> PR20 producer authenticity
             |
             v
          PR21 trust-state currentness / protected witness
             |
             v
          PR22 transition authorization / exact witnessed predecessor
             |
             v
          PR23 external governance root + protected root witness

PR24 time-source currentness cross-cuts PR6/12/16/20/21/22/23
but MUST NOT become the structural authority for PR21/22/23.

PR19 (this integration map) describes dependency/claim composition only.
```

This graph is not:
- merge order;
- implementation order;
- deployment order;
- readiness score.

## 7. Distinct axes that must not collapse

### Product capability
PR #4 / future product qualification.

### Deployment commissioning
PR #7.

### Execution/write authority
PR #6 / architecture authority contracts.

### Artifact lifecycle
PR #2 architecture.

### Support/recovery
PR #8.

### Cross-axis currentness
PR #9/#10/#11/#12.

### Transaction identity and replay
PR #13/#14/#15/#17.

### Execution/causal evidence
PR #16.

### Evidence-history integrity
PR #18.

### Producer authenticity
PR #20.

### Trust-state currentness
PR #21.

### Trust-transition authorization
PR #22.

### Governance-root authority/currentness
PR #23.

### Time-source currentness
PR #24.

A green state in one axis does not manufacture another.

## 8. No PASS inheritance

Examples:

- PR #6 design PASS does not qualify a PR #11 currentness implementation.
- PR #4 evidence PASS cannot grant machine-application support when a required dependency is unknown.
- PR #21 trust currentness cannot authorize a trust transition; PR #22 must also pass.
- PR #22 authorization cannot make an uncommitted successor current; PR #21 witness commit must establish it.
- PR #23 current governance root does not prove current subordinate trust state.
- PR #24 valid time cannot revive stale/revoked/root-conflicting state.
- PR #18 complete ledger does not prove the producer was authentic; PR #20 addresses that.
- PR #20 authentic producer does not prove the trust state accepting that producer is current; PR #21 addresses that.
- PR #15 durable dispatch ordering does not prove physical effect or causation; PR #16 addresses that.
- PR #5 benchmark validity does not prove ABIL wins.

## 9. Anti-circularity rules

### Currentness cycles
PR #10:
mutual dependency is allowed; mutual self-justification is not.

### Trust transition
PR #22:
successor cannot supply the policy/authority that validates its own creation.

### Governance root
PR #23:
the root chain terminates at externally established protected governance plus separately protected currentness witness.

### Time/trust
PR #24:
do not use temporal validity to bootstrap the structural trust required to authenticate the same time source.

### Recovery
PR #8/#14/#21/#23:
restored local bytes do not self-prove current authority, replay state, trust, or governance.

## 10. Currentness and commit layers

For high-consequence state, distinguish:

1. subject identity;
2. subject integrity;
3. authorization/qualification;
4. currentness;
5. unique protected commit/head witness where required;
6. operation-specific admissibility;
7. temporal admissibility where required.

Skipping from "valid object" to "current/admissible" is not allowed.

## 11. Invalidation propagation examples

### PR #4 restoration/dependency closure fails

Affected:
- product/component support claims relying on incomplete/over-broad evidence;
- PR #9/#11 product-currentness predicates.

Not automatically affected:
- transaction identity mechanics in PR #13.

### PR #10 cycle grounding fails

Affected:
- PR #11/12 claims depending on cyclic currentness closure;
- partial recovery/commissioning compositions.

Not automatically affected:
- PR #6 written authority schema.

### PR #14 replay anti-rollback fails

Affected:
- restored/failover write safety;
- PR #15 durable dispatch assumptions;
- PR #17 no-return-to-unused semantics.

Not automatically affected:
- PR #13 exact effect-intent identity itself.

### PR #18 ledger continuity fails

Affected:
- any stronger claim requiring complete historical evidence;
- replay/currentness/reconciliation/benchmark claims that depend on complete history.

Does not prove:
- individual record bytes are false.

### PR #20 producer authenticity fails

Affected:
- claims requiring authenticated producer identity;
- trust-state evidence about that producer.

Does not prove:
- ledger continuity is broken.

### PR #21 trust-currentness fails

Affected:
- current producer/verifier acceptance;
- transition application against supposed current predecessor;
- time-source authentication when that source depends on affected trust.

Historical verification may remain possible under explicit historical cuts.

### PR #22 transition authorization fails

Affected:
- legitimacy of the successor trust-state lineage.

A valid protected witness cannot make an unauthorized transition legitimate.

### PR #23 root-currentness fails

Affected:
- new subordinate trust-transition authorization;
- any governance decision requiring the disputed root.

Current subordinate operational state may continue only where policy explicitly permits and does not require root reevaluation.

### PR #24 time-currentness fails

Affected only where the exact claim requires temporal predicates:
- expiry/freshness;
- scheduled activation;
- grace/overlap;
- causal windows;
- time-based retention.

Structural lineage/currentness does not automatically fail merely because wall-clock evidence is unavailable, unless the operation profile requires it.

## 12. Historical truth versus current authority

Across PR #4/#8/#14/#17/#18/#20/#21/#23/#24:

- historical valid evidence remains historical evidence;
- later invalidation does not rewrite old facts;
- historical evidence does not become current by restore;
- current authority/currentness requires a current exact cut;
- late evidence may refine historical disposition without manufacturing present authority.

## 13. Exact-head review discipline

Every verdict binds the exact reviewed head.

Material head movement:
- invalidates current review credit on the moved subject;
- preserves the old review as provenance only;
- requires fresh exact-head review.

Composition reviews MUST name every exact head in the tuple they evaluate.

PR number alone is not a review subject.

## 14. Review-role separation

### Source-owner audit
May identify, repair and reconcile internal composition issues.
Does not count as independent peer credit.

### Independent peer review
Exact-head hostile/review assessment.

### Coordinator reconciliation
One may reconcile only after exact-head peer returns.

### Patrick authority
Required for protected effects and for final PR #3 written-design acceptance before implementation planning.

These roles do not substitute for one another.

## 15. Current exact-head review queue

Highest-priority active subjects:

- PR #3 `1da5bc57...` — R6 exact-head peer review and One reconciliation.
- PR #4 `1fd7767a...` — hostile rereview of restoration/dependency-closure repair.
- PR #21 `2b4d5da3...`
- PR #22 `4933e0fd...`
- PR #23 `705e0a9c...`
- PR #24 `57039cec...`
  — linked trust/governance/time hostile composition review.

Also pending as applicable:
- PR #2 architecture;
- PR #5 benchmark;
- PR #7–#18 individual research review.

PR #6 remains written-contract PASS unless its exact head moves or a materially new finding reopens it.

## 16. Highest-value decision frontier

The gating chain before implementation planning remains unchanged:

1. exact-head PR #3 independent review;
2. One reconciliation;
3. if clean, Patrick's explicit final written-design acceptance;
4. only after that acceptance may implementation planning be considered.

The broader research lattice may continue to improve evidence/safety/currentness design in parallel, but cannot consume or bypass Patrick's acceptance gate.

## 17. Evidence ceilings

### Architecture
PR #2:
architecture only.

### Written design
PR #3:
final written-design gate; implementation planning held.

### Design/governance contract
PR #6:
written contract PASS only.

### Research
PR #4/#5/#7–#24:
non-normative research;
no executable proof;
no product certification;
no commissioning qualification;
no machine authority;
no runtime qualification.

### Integration map
PR #19:
dependency/claim reasoning only.

## 18. Protected-effect boundary

Nothing in PR #2–#24 authorizes:

- merge/canonical promotion;
- implementation planning past the PR #3 clean-review gate without Patrick acceptance;
- production deployment;
- machine connection/write;
- commissioning;
- product selection/procurement/license acceptance;
- trust-root/credential/provider/time-source mutation;
- ruleset/permission mutation;
- publication/visibility change;
- safety ownership.

## 19. Practical integration rule

> Treat ABIL as a dependency lattice of independently bounded claims. Stronger operational claims require the exact required axes to be simultaneously valid on one coherent current cut; no local PASS, timestamp, generation, receipt, certificate, restore, or valid historical artifact may manufacture a missing axis.

## 20. Research disposition

This V2 map adds no mechanism and authorizes no implementation.

It exists to prevent:
- stale-head review transfer;
- cross-axis implication;
- authority/currentness conflation;
- trust/time circularity;
- review-role conflation;
- research-to-readiness promotion.

Patrick remains sole authority for protected effects.
