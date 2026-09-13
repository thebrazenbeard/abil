# ABIL Control Reconstruction Product Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update ABIL's living product documentation so the repository clearly defines a coexistence-first, replacement-capable brownfield control-system reconstruction appliance while preserving the frozen 2026-09-06 F0/R1 evidence as historical provenance.

**Architecture:** The living docs distinguish the long-term product from the current F0 learning substrate. ABIL defaults to observing and working with surviving PLC logic, may use the PLC as a deterministic execution proxy, and replaces ordinary PLC control logic with a separate ABIL deterministic control runtime only when necessary. Safety authority remains independently bounded.

**Tech Stack:** Markdown documentation; Git/GitHub; no production code change in this plan.

**Spec:** `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md`

## Global Constraints

- Preserve the exact historical meaning of the 2026-09-06 foundation/F0 design and its frozen R1 review; do not rewrite history.
- Default product strategy is **replacement-capable, coexistence-first**.
- Existing ordinary PLC logic is preferred as an execution partner when practical.
- Direct ABIL takeover of ordinary PLC control is a separately qualified capability promotion.
- Safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, and other independent safety functions remain authoritative unless a separate explicitly engineered safety project changes that contract.
- The intelligence/commissioning plane remains distinct from the deterministic control runtime.
- Read-only F0 remains a development/qualification stage, not the final product definition.
- No production code, machine connection, deployment, credential/provider mutation, or merge is part of this documentation update.

## Completed documentation tasks

- [x] Reframed `README.md` around the actual end product and preserved the recovery scenario in durable product language.
- [x] Expanded `docs/PRODUCT_THESIS.md` from analytics wedge to control-system reconstruction and coexistence-first migration.
- [x] Rebuilt `docs/ARCHITECTURE_BOUNDARIES.md` around discovery, semantic commissioning, control synthesis, PLC coexistence, deterministic execution, and independent safety authority.
- [x] Extended `docs/FIELD_VALIDATION_ROADMAP.md` from synthetic/read-only evidence through guided commissioning, PLC proxy, supervised cutover, direct remote-I/O control, and permanent runtime support.
- [x] Updated `docs/COMPETITIVE_REALITY_CHECK.md` to distinguish ABIL from analytics-only tools, soft-PLC runtimes, and conventional one-off controls integration.
- [x] Preserved the 2026-09-06 foundation design and F0 shadow-pilot plan unchanged as frozen historical provenance.
- [x] Verified living docs no longer define read-only shadow mode or bounded autonomy as the terminal product boundary.
- [x] Verified living docs do not claim automatic safety replacement, arbitrary vendor-PLC overwrite, metadata-as-semantics, or direct learner self-modification of production control.
- [x] Added an explicit immediate R2 review boundary so the broader end-product architecture does not accidentally authorize premature write-capable implementation.
- [x] Marked the successor documentation as ready for independent review while keeping PR #2 unmerged.

## Verification record

PR #2 changed-file inventory after execution contains only living successor documentation plus the new 2026-09-08 spec/plan. The frozen historical files remain outside the changed-file set:

- `docs/superpowers/specs/2026-09-06-abil-foundation-design.md`
- `docs/superpowers/plans/2026-09-06-abil-f0-shadow-pilot.md`

No production source code, executable controller, machine connection, deployment, credential/provider mutation, or merge was performed by this plan.

## Reviewer activation target

Independent reviewers should review **PR #2 exact current head** and preserve two separate questions:

1. Is the successor product/control architecture internally coherent, bounded, and commercially/technically plausible?
2. Does the defined immediate R2 boundary correctly preserve the frozen R1 findings while avoiding premature coupling that would obstruct later coexistence-first control reconstruction?

Reviewers should not treat the broader product architecture as authorization to implement write-capable commissioning, PLC proxy execution, vendor-project generation, direct remote-I/O control, or a production deterministic runtime.

## Next engineering frontier

After independent architecture review converges, the next source subject should convert the previously failed frozen F0 contract into a corrected successor R2 substrate contract that satisfies the admitted R1 findings while remaining aligned with this broader product architecture.

That corrected R2 contract should remain an early learning/telemetry substrate: it should not prematurely implement the later write-capable commissioning or deterministic-control stages merely because the long-term product now includes them.
