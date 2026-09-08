# ABIL

**Adaptive Brownfield Intelligence Layer**

ABIL is a proposed adaptive reconstruction and control platform for existing industrial equipment and other brownfield physical systems.

The product principle is simple:

> Do not replace a functioning machine just because its software, documentation, vendor support, or tribal knowledge is obsolete. Learn the machine that actually exists.

ABIL should work with surviving controls by default, but it is ultimately intended to reconstruct and replace ordinary brownfield control logic when the existing control system cannot remain viable.

## Product concept

A representative recovery case looks like this:

1. A machine remains mechanically useful, but its HMI/control PC, PLC project, supervisory software, or vendor support becomes unavailable or impractical to recover.
2. An ABIL appliance is connected to the surviving control network and appropriate industrial interfaces.
3. ABIL inventories reachable controllers, remote I/O, drives, sensors, valve manifolds, fieldbus nodes, and communication relationships without treating names or metadata as proven functional meaning.
4. If the existing PLC logic still works, ABIL observes it and uses it as evidence rather than immediately replacing it.
5. During guided commissioning, a technician manually exercises known machine functions through a constrained action path and identifies or confirms the purpose of devices, signals, solenoids, sensors, and sequences.
6. ABIL records operator-supplied semantics separately from relationships learned from timing, state changes, and repeated machine behavior.
7. ABIL builds and revises a machine-specific behavioral/control model.
8. ABIL synthesizes a candidate automation model and validates it through replay, simulation, and shadow comparison before it gains machine authority.
9. When practical, the existing PLC may remain as a deterministic execution proxy or permanent execution target.
10. When the ordinary PLC/control logic is unsupported, locked, unreliable, failed, uneconomic to preserve, or otherwise unsuitable, ABIL may replace its function with a separately qualified deterministic control runtime that talks directly to remote I/O and field devices.
11. The ABIL appliance can then become the permanent supported control computer for that installation.

The default strategy is therefore **replacement-capable, coexistence-first**.

## Current status

**Foundation / research / architecture. No production control code exists yet.**

The repository currently contains the product thesis, architecture boundaries, validation strategy, competitive reality check, the frozen first F0 learning-substrate design, and a successor control-reconstruction architecture. Claims remain hypotheses until demonstrated empirically.

The successor architecture is ready for independent review. The immediate review target is the architecture/documentation itself plus the shape of the corrected R2 early-substrate contract; it is not authorization to build write-capable commissioning or production control yet.

## Product direction

The initial commercial target is brownfield industrial equipment with some combination of:

- legacy or unsupported HMI/SCADA/control software;
- unavailable, locked, stale, or undocumented PLC projects;
- PLC/PAC/remote-I/O/drive/sensor networks;
- accumulated machine-specific quirks and modifications;
- operational knowledge concentrated in a small number of experienced people;
- obsolete controller or fieldbus hardware that is difficult to support;
- equipment that is too valuable, specialized, or mechanically healthy to replace simply for controls modernization.

ABIL should still begin technically in **read-only shadow mode**. The first proof is that it can learn useful machine-specific structure without exhaustive semantic hand-mapping. That is a qualification stage and commercial wedge, not the final product boundary.

## Architectural stance

ABIL is not Noema and is not required to satisfy Noema's research-purity constraints. It may use whichever combination of system identification, time-series learning, causal inference, rules, databases, language models, vision models, and Noema-derived mechanisms best serves the industrial problem.

The product should keep these responsibilities distinct:

1. **Industrial discovery and adapters** — acquire telemetry, topology, configuration, and protocol-specific evidence from PLCs, remote I/O, drives, sensors, HMIs, historians, databases, files, cameras, and vendor interfaces.
2. **Machine-model learning and semantic grounding** — learn dynamics, delays, regimes, relationships, uncertainty, and change while keeping human-supplied semantics distinct from learned structure.
3. **Operator commissioning and diagnostics** — support guided manual commissioning, technician confirmations/corrections, evidence inspection, predictions, diagnostics, and proposed tests.
4. **Control-model synthesis and validation** — produce inspectable candidate states, transitions, commands, permissives, timing expectations, alarms, recovery paths, and ordinary non-safety interlocks; validate them before promotion.
5. **Deterministic control runtime** — execute only an approved promoted control artifact with explicit I/O scheduling, timers, watchdogs, ordinary permissives/interlocks, alarms, and protocol-specific runtime behavior.
6. **Independent safety/action authority** — constrain write-capable operation and preserve independent safety systems. A learner or LLM does not get unrestricted output authority simply because it can propose a command.

The intelligence/commissioning plane may keep learning. It must not continuously or implicitly rewrite the running deterministic controller.

## Existing PLC strategy

ABIL should treat an existing PLC as potentially useful in several roles:

- evidence/configuration source;
- deterministic execution proxy;
- permanent execution target;
- replaceable legacy controller.

ABIL should not assume it can or should overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other vendor projects. Vendor-project rewriting is a target-specific migration path. The universal goal is to reconstruct and support the machine's ordinary control function, not to depend on modifying proprietary internals.

## Commercial differentiation target

ABIL should not become another generic anomaly detector, historian dashboard, AI manual explainer, or conventional one-off control migration.

The differentiating target is:

> **Learn how this particular machine works, ground enough of that understanding through targeted technician interaction to reconstruct its control behavior, validate the reconstruction, and preserve or replace the surviving control stack with the least disruptive supportable path.**

A successful ABIL system should eventually be able to answer and act on questions such as:

- What devices and signals are actually present?
- Which relationships are learned from behavior and which were supplied by a human or vendor project?
- What changed relative to the machine's own history?
- Which signals are genuinely predictive rather than merely correlated?
- What operating regimes and sequence relationships has the system learned?
- What evidence would distinguish competing explanations?
- What bounded observation or commissioning action would reduce uncertainty?
- Can the existing PLC remain the best execution target?
- If not, can the reconstructed control model be promoted into a deterministic ABIL runtime that reproduces the required ordinary machine behavior?

## Development and capability ladder

1. Synthetic/headless learning environment.
2. Recorded-telemetry replay.
3. Live passive discovery and read-only shadow mode.
4. Operator-facing diagnostics and evidence review.
5. Guided semantic commissioning.
6. Bounded manual controls through an independently constrained action path.
7. Reconstructed machine/control model.
8. Generated candidate control artifact.
9. Replay, simulation, and shadow validation.
10. Existing-PLC execution-proxy mode where useful.
11. Supervised cutover to a validated control artifact.
12. Direct remote-I/O control when replacement is required and separately qualified.
13. Permanent ABIL runtime with ongoing diagnostics and learning outside deterministic execution authority.

Passing one stage does not imply authority for the next.

## Safety boundary

Ordinary control reconstruction does not automatically include safety-system reconstruction.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired protective interlocks, drive safety functions, and other independent safety systems remain authoritative unless a separate explicitly engineered safety project changes that contract. ABIL may observe safety state and respect it as a prerequisite, but observed machine behavior is not sufficient evidence to infer or recreate certified safety requirements.

## Likely product form

The long-term physical product is likely an industrial edge appliance rather than an APK or ordinary desktop application: a rugged/fanless mini-PC, appropriate industrial Ethernet/fieldbus interfaces, bootable install/recovery media, a small Linux-based appliance OS, persistent machine/deployment state, commissioning tools, and a deterministic control runtime.

The exact Linux distribution, real-time strategy, first fieldbus, HMI framework, and controller runtime remain open engineering decisions.

## Documents

- `docs/PRODUCT_THESIS.md` — living problem, customer, value proposition, migration strategy, and end-product thesis.
- `docs/ARCHITECTURE_BOUNDARIES.md` — living system boundaries, coexistence roles, control-synthesis separation, deterministic runtime, and safety limits.
- `docs/FIELD_VALIDATION_ROADMAP.md` — staged route from simulation through permanent control replacement.
- `docs/COMPETITIVE_REALITY_CHECK.md` — what is already commoditized and what the stronger reconstruction thesis must prove.
- `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md` — successor product/control architecture.
- `docs/superpowers/plans/2026-09-08-abil-control-reconstruction-product-architecture.md` — documentation implementation plan for the successor architecture.
- `docs/superpowers/specs/2026-09-06-abil-foundation-design.md` — frozen narrower first technical slice retained as historical provenance.
- `docs/superpowers/plans/2026-09-06-abil-f0-shadow-pilot.md` — frozen first F0 implementation plan retained as historical provenance.

## Naming

**ABIL = Adaptive Brownfield Intelligence Layer.**

Working phrase: **Make old systems able.**
