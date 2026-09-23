> **License:** Source-visible, not open source. Original material is proprietary. Commercial use, redistribution, hosted-service use, and commercial derivative products require written permission. See [LICENSE](LICENSE) and [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Separately identified third-party components retain their own licenses.

# ABIL

**Adaptive Brownfield Intelligence Layer**

ABIL is a proposed adaptive intelligence layer for existing industrial equipment and other brownfield physical systems.

The product thesis is simple:

> Do not replace a functioning machine just because its software, documentation, vendor support, or tribal knowledge is obsolete. Learn the machine that actually exists.

ABIL is intended to run alongside existing controls rather than replace them. It should ingest available operational signals, build a continually revised model of the particular system it is attached to, detect meaningful change, predict likely outcomes, expose uncertainty, and eventually recommend or execute tightly bounded actions through explicit safety controls.

## Concept

Client's equipment has a fucked OS → client realizes HMI control system for automated equipment is no longer supported → client calls me → I disconnect their PC from the system & network/wire in an ABIL mini-PC, ABIL mini-PC maps network and nodes, determines what those things to, and gives you manual controls over the equipment → ABIL mini-PC studies and learns the system while you manually activate and define the functions/purpose of the node/solenoid/sensor/whatever → ABIL mini-PC semi-automatically creates new automation control software to run the line → ABIL mini-PC becomes permanent replacement for original control OS

## Current status

**Foundation / research / architecture. No production control code exists yet.**

This repository currently records the product thesis, architecture boundaries, validation strategy, competitive reality-check, and first implementation plan. Claims remain hypotheses until demonstrated empirically.

## Product direction

The initial commercial target is brownfield industrial equipment with some combination of:

- legacy or unsupported software;
- incomplete or stale documentation;
- PLC/PAC/remote-I/O/drive/sensor networks;
- accumulated machine-specific quirks and modifications;
- operational knowledge concentrated in a small number of experienced people;
- equipment that is too valuable, specialized, or mechanically healthy to replace simply for software modernization.

ABIL should begin in **read-only shadow mode**. The first useful product is not autonomous control; it is a system that can learn enough about a real installation to make predictions and surface useful machine-specific structure without requiring exhaustive semantic hand-mapping.

## Architectural stance

ABIL is not Noema and is not required to satisfy Noema's research purity constraints. ABIL may use whichever combination of system identification, time-series learning, causal inference, rules, databases, language models, vision models, and Noema-derived mechanisms best serves the industrial problem.

The product should keep four responsibilities distinct:

1. **Industrial adapters** — acquire signals from PLCs, historians, HMIs, drives, sensors, cameras, databases, files, or vendor interfaces.
2. **Adaptive learning core** — learn dynamics, operating regimes, delays, anomalies, uncertainty, and changing relationships over time.
3. **Operator interface** — expose predictions, evidence, uncertainty, history, and recommended tests or actions in language a technician can use.
4. **Safety/action gateway** — independently constrain any future write-capable behavior. No learning component gets unrestricted control authority merely because it can issue a command.

## Commercial differentiation target

ABIL should not be another generic anomaly detector.

The differentiating target is:

> **Learn how this particular system works, keep learning as it changes, and help a human distinguish competing explanations rather than merely announcing that something looks abnormal.**

A successful ABIL system should eventually be able to answer questions such as:

- What changed about this machine relative to its own history?
- Which signals are genuinely predictive rather than merely correlated?
- What operating regimes has the system learned?
- Which relationship appears to have drifted?
- What evidence would distinguish the leading explanations?
- Has a formerly reliable sensor or proxy become misleading?
- Did a tooling, operator, material, maintenance, or process change create a new regime?
- What bounded action or observation would most reduce uncertainty?

## Development ladder

1. Synthetic/headless industrial process environment.
2. Offline recorded-telemetry replay.
3. Live read-only shadow deployment on a real isolated system.
4. Operator-facing prediction and diagnostic assistance.
5. Human-supervised discriminating tests or interventions.
6. Tightly allowlisted bounded autonomy only after evidence justifies it.

The repository intentionally does not begin with rendered 3D environments, a general-purpose autonomous agent, or direct control of production equipment.

## Documents

- `docs/PRODUCT_THESIS.md` — problem, customer, value proposition, and differentiation.
- `docs/ARCHITECTURE_BOUNDARIES.md` — system boundaries and non-negotiable separations.
- `docs/FIELD_VALIDATION_ROADMAP.md` — staged route from simulation to live shadow mode.
- `docs/COMPETITIVE_REALITY_CHECK.md` — what is already commoditized and where ABIL must be different.
- `docs/superpowers/specs/2026-09-06-abil-foundation-design.md` — current architecture/product design.
- `docs/superpowers/plans/2026-09-06-abil-f0-shadow-pilot.md` — first implementation plan.

## Naming

**ABIL = Adaptive Brownfield Intelligence Layer.**

Working phrase: **Make old systems able.**
