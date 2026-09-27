# ABIL R2 Review Corrections R4 — Successor-Architecture Base Reconciliation

Classification: **IP_CONFIDENTIAL**

Status: **normative narrow reconciliation for Draft PR #3; implementation not authorized**

Date: 2026-09-13

## 1. Purpose and exact reconciliation subject

The primary R2 design records that the R2 branch was cut from ABIL successor-architecture head `22187ea9d8fdc22b0e47a42f7877dbe35f11247f` and requires reconciliation if that architecture changes materially before promotion.

The successor-architecture branch has since advanced by one documentation commit to:

`712d5b30b45ba9299dcfce0599878cb81db70e8f`

The exact architecture delta is commit `712d5b30b45ba9299dcfce0599878cb81db70e8f`, `docs: close authority-root and safety-classification review gaps`. It changes only successor architecture documentation and adds or clarifies:

- an independently rooted `AuthorityGrant` requirement before future write-capable deployment/promotion;
- separation of deployment authority from artifact-promotion authority;
- runtime verification of the current authority grant for a future write-capable path;
- independent, current `SafetyClassificationRecord` evidence before unknown protective/interlock semantics can be downgraded from safety-relevant treatment;
- deny-by-default promotion/authority wording for unresolved behavior, while preserving installation-specific physical safe-state/fallback policy.

This R4 document records the required R2 reconciliation against that exact architecture delta.

## 2. Compatibility disposition

The architecture delta does **not** conflict with or weaken the current R2 non-actuating substrate contract.

R2 remains intentionally outside the future write-capable authority plane. It contains no industrial write client, commissioning gateway, machine-control artifact promotion, active-artifact loader, physical-output ownership transfer, safety-system mutation, or deterministic machine-control path.

Therefore:

1. R2 does not need an `AuthorityGrant` in order to execute its synthetic/replay qualification scope because it has no write-capable deployment authority to grant.
2. R2 must not treat the absence of an `AuthorityGrant` as permission to introduce write capability; write capability remains out of scope.
3. `AuthorityGrant`, promotion-authority state, active-artifact state, commissioning authority, and `SafetyClassificationRecord` are evaluator/control/deployment concepts for later capability stages and are **not learner-visible evidence by default**.
4. No authority-root, safety-classification, or rich deployment identity introduced by the broader architecture may be added to `LearnerEvent`, `LearnerTaskManifest`, learner checkpoint state, feature frames, or another learner-visible R2 channel merely because it exists in the broader product model.
5. A future R2 successor that introduces live machine access, commissioning, physical writes, artifact promotion, control ownership, or safety-classification consumption becomes a new reviewed capability subject and may not inherit this non-actuating reconciliation as authorization.

## 3. Safety and claim boundary

R2's evaluator may retain rich fixture truth needed for synthetic/replay scoring, but that is not an industrial safety-classification authority.

Nothing in R2 may claim that observed behavior, learned correlation, replay success, hidden fixture truth, or learner confidence is sufficient to create or downgrade an industrial `SafetyClassificationRecord`.

Likewise, successful R2 substrate qualification or learner efficacy does not grant deployment, commissioning, promotion, machine-write, control-owner, or safety authority.

## 4. Normative composition and precedence

For the current R2 written-design subject, the normative source composition is cumulative:

1. `docs/superpowers/specs/2026-09-08-abil-r2-substrate-design.md`
2. `docs/superpowers/specs/2026-09-08-abil-r2-review-corrections-r1.md`
3. `docs/superpowers/specs/2026-09-08-abil-r2-review-corrections-r2.md`
4. `docs/superpowers/specs/2026-09-09-abil-r2-review-corrections-r3.md`
5. this R4 reconciliation.

R3's cumulative-source and precedence rule remains in force: later corrections control only genuine conflicts, and unchanged earlier obligations remain cumulative.

For broader-product compatibility, this five-document R2 subject is reviewed against successor-architecture base `712d5b30b45ba9299dcfce0599878cb81db70e8f`.

## 5. Review and authority boundary

The required next review subject is the exact PR #3 head containing this R4 file together with successor-architecture base `712d5b30b45ba9299dcfce0599878cb81db70e8f`.

Reviewers should verify that the base reconciliation:

- preserves R2's zero-write/non-actuating boundary;
- does not leak future authority/safety metadata into learner evidence;
- does not weaken the cumulative R2 qualification obligations;
- does not infer any implementation, Hephaestus, merge, machine, deployment, publication, licensing, or safety authority.

This document authorizes none of those effects. Patrick remains the final authority for protected promotion and implementation gates.
