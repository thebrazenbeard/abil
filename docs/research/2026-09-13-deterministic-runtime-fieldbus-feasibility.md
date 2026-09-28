# Deterministic Runtime and Fieldbus Feasibility Spike

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-13

Research branch: `research/industrial-runtime-feasibility-20260913`

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

ABIL's product architecture intentionally allows several permanent execution targets: surviving PLC, PLC proxy, conventional controller output, or a direct deterministic ABIL runtime. This spike asks a narrower engineering question:

> If ABIL eventually needs to become the ordinary controller on an industrial PC, what parts of that execution stack are realistically available today, and which parts should ABIL avoid reinventing in the first direct-control implementation?

This is feasibility research, not a product-selection decision. Nothing here authorizes live machine access, write capability, commissioning, runtime implementation, procurement, licensing, deployment, or promotion.

## Executive finding

The direct-control product thesis is technically plausible without ABIL first inventing a universal PLC runtime or universal fieldbus implementation.

The strongest near-term engineering posture is:

1. preserve the current **coexistence-first** path and use surviving PLCs where practical;
2. define ABIL's generated control model against a narrow deterministic-execution-target contract rather than one hard-coded runtime;
3. qualify a commercially supported Linux soft-PLC / protocol-card path as an early broad-coverage execution target;
4. use open protocol stacks selectively where their exact role and license fit the product;
5. treat a wholly ABIL-owned deterministic runtime as a later target that must earn its timing, protocol, restart, fault, security, and lifecycle claims independently.

This reduces the largest avoidable risk: coupling the novel reconstruction problem to simultaneous reinvention of mature industrial communications and PLC runtime machinery.

## Evidence snapshot

### Linux real-time substrate

Current Linux kernel documentation describes PREEMPT_RT as transforming the kernel into a real-time kernel by making most kernel execution preemptible, using priority-inheritance-aware locking and threaded interrupts. It also documents real-time scheduling behavior such as `SCHED_FIFO`.

Implication for ABIL: Linux is a credible host for deterministic-control experiments and products, but PREEMPT_RT / `SCHED_FIFO` is **not itself a timing qualification**. ABIL still needs target-specific worst-case cycle/jitter/load, driver, IRQ, memory, storage, thermal, and fault evidence.

Sources:
- https://docs.kernel.org/core-api/real-time/
- https://docs.kernel.org/core-api/real-time/theory.html
- https://docs.kernel.org/core-api/real-time/differences.html

### CODESYS Control for Linux SL

CODESYS currently ships a 64-bit Linux soft-PLC runtime. Its published Linux SL fieldbus list includes:

- CANopen Manager / Device;
- EtherCAT Master;
- EtherNet/IP Scanner / Adapter;
- Modbus TCP Master / Slave;
- Modbus Serial Master / Slave;
- PROFIBUS Master;
- PROFINET Controller / Device.

The product also supports integration of existing C code, external functions, local I/O, external event tasks, and persistent memories. The current product page identifies Hilscher cifX / netX hardware requirements for its listed PROFIBUS-master and PROFINET-controller paths.

Implication for ABIL: this is the clearest current evidence that the broad execution side of the product can initially be **bought/integrated rather than invented**. ABIL could generate a conventional deterministic control artifact or bounded interface for a proven runtime while retaining its own reconstruction, evidence, authority, coverage, and promotion planes.

Caution: product availability does not establish ABIL qualification. Licensing, runtime redistribution, hardware support, deterministic behavior on the selected appliance, protocol conformance, offline lifecycle, update control, and security must be reviewed separately.

Source:
- https://store.codesys.com/en/codesys-control-linux-sl-1.html

### Hilscher cifX / netX protocol offload

Hilscher's current cifX PC-card family is explicitly aimed at PC-based automation. Hilscher states that the protocol stack runs autonomously on the card and exchanges process data with the host through dual-port memory or DMA. Its portfolio provides Linux drivers and a common API across industrial Ethernet and fieldbus protocols.

Most relevant to ABIL's brownfield thesis, current Hilscher products include active DeviceNet Master/Slave PC cards, including M.2, Mini PCI Express, low-profile PCIe, and other form factors. Hilscher identifies a separate master license for at least some DeviceNet products.

Implication for ABIL: **DeviceNet does not require ABIL to write a DeviceNet scanner stack from scratch**. A protocol-offload card is a plausible first-class execution adapter for an industrial mini-PC, and the same architectural pattern can isolate protocol timing/state machines from the ABIL host runtime.

This also suggests an appliance design constraint worth keeping open: the eventual ABIL hardware should not be selected so tightly around tiny consumer form factors that it cannot expose a supported industrial communication module/card path.

Sources:
- https://www.hilscher.com/products/pc-cards-for-industrial-ethernet-fieldbus
- https://www.hilscher.com/products/pc-cards-for-industrial-ethernet-fieldbus/m2/cifx-m3042100bm-dnf
- https://www.hilscher.com/na/products/pc-cards-for-industrial-ethernet-fieldbus/low-profile-pci-express/cifx-70e-dn

### EtherCAT

IgH/EtherLab maintains an open-source EtherCAT master for Linux and recommends its stable branch for production systems. Its documentation describes native and generic Ethernet drivers, multiple masters/domains, and compatibility with Linux real-time approaches including RT-Preempt/PREEMPT_RT-class operation.

Implication for ABIL: EtherCAT is a credible candidate for an ABIL-owned or tightly integrated protocol path rather than requiring a commercial soft-PLC in every case.

Caution: the IgH master is GPL-licensed. Product/legal integration needs an explicit license architecture review before ABIL relies on it in a distributed appliance.

Sources:
- https://etherlab.org/en_GB/ethercat
- https://docs.etherlab.org/ethercat/1.6/pdf/ethercat_doc.pdf
- https://docs.etherlab.org/ethercat/1.7/doxygen/index.html

### EtherNet/IP

EIPScanner is an MIT-licensed C++ EtherNet/IP scanner implementation supporting explicit messaging, point-to-point implicit messaging, and discovery on Linux/macOS/Windows.

Implication for ABIL: open-source EtherNet/IP tooling is sufficient to support useful discovery, lab work, configuration evidence, and some scanner/control experiments.

Caution: its published feature set is not equivalent to a universal production scanner/master qualification. In particular, the explicit `implicit messaging (only point-to-point)` limitation means ABIL should not infer broad brownfield production coverage from library existence. A commercial scanner stack/runtime may remain the safer early field path.

Source:
- https://github.com/nimbuscontrols/EIPScanner

### Modbus TCP / RTU

libmodbus provides portable client/server APIs for Modbus over serial RTU and Ethernet TCP.

Implication for ABIL: Modbus is a strong first direct-I/O laboratory target because the software path is comparatively simple, inspectable, and portable. It is useful for validating ABIL's deterministic-runtime, command-transaction, ownership, restart, and adapter contracts before harder fieldbuses.

Caution: Modbus protocol support alone says nothing about the deterministic timing or machine-safety suitability of a particular control loop.

Source:
- https://libmodbus.org/reference/

### CANopen

Lely's CANopen stack recommends Linux as a development platform and includes tools capable of constructing master/slave processes over Linux SocketCAN. Its configuration tooling exposes master timing and heartbeat concepts.

Implication for ABIL: CANopen is another realistic open Linux path for laboratory and possibly qualified product adapters.

Caution: CANopen support must not be conflated with DeviceNet merely because both use CAN at lower layers. ABIL should model them as distinct protocol capabilities.

Sources:
- https://opensource.lely.com/canopen/docs/installation/
- https://opensource.lely.com/canopen/docs/cmd-tutorial/
- https://opensource.lely.com/canopen/docs/dcf-tools/

### PROFINET

RT-Labs P-Net is a PROFINET **IO Device** implementation, not evidence of a general PROFINET Controller path. RT-Labs states that it runs on Linux/RTOS/bare metal and implements PROFINET RT Class 1, with a GPL evaluation path and commercial production licensing.

Implication for ABIL: open PROFINET components exist, but a device stack does not solve ABIL's controller role. For early controller-side coverage, CODESYS + qualified hardware or another commercial controller stack is the more credible path.

Source:
- https://rt-labs.com/product/p-net/

### OpenPLC Runtime v4

OpenPLC Runtime v4 is active in 2026 and describes a headless PLC runtime with a C/C++ execution core, IEC 61131-3 program support, `SCHED_FIFO` real-time priority, Linux support, an I/O plugin system, and current v4 releases. Its predecessor v3 was archived/EOL in April 2026, so v3 should not be used as current architecture evidence.

Implication for ABIL: OpenPLC v4 is useful as a **lab comparator and potential pluggable execution target**. Its inspectability also makes it valuable for experiments that compare ABIL's own runtime ideas against an existing PLC scan engine.

Caution: do not promote it to the default field runtime from repository claims alone. ABIL would need to audit its exact scan/timing behavior, restart/activation semantics, plugin isolation, update/control plane, fieldbus support, security, licensing, and fit with ABIL's protected promotion/authority architecture. The current project metadata reports an MIT license, but dependency/plugin/toolchain licenses still need a full product license review.

Sources:
- https://github.com/Autonomy-Logic/openplc-runtime
- https://autonomylogic.com/runtime
- https://github.com/Autonomy-Logic/openplc-runtime/releases

## Protocol-path feasibility matrix

| Target | Credible Linux path now? | Early ABIL posture | Main qualification concern |
|---|---|---|---|
| Modbus TCP/RTU | Yes | Open stack is suitable for early direct-control lab target | Timing/fault behavior belongs to deployment, not protocol library |
| CANopen | Yes | Open Linux stack plausible | Exact master timing, device profiles, recovery, hardware |
| EtherCAT | Yes | Open master or commercial runtime | RT tuning, NIC/driver behavior, licensing, conformance |
| EtherNet/IP | Yes, but open feature coverage is narrower than universal field need | Open stack for discovery/lab; commercial path for first broad field qualification | Implicit-I/O topology, connection behavior, conformance, recovery |
| DeviceNet | Yes via industrial PC communication hardware | Prefer protocol-offload card for initial field path | Hardware lifecycle, DPM/DMA contract, licensing, node/config recovery |
| PROFIBUS | Yes via commercial soft-PLC/communication hardware | Buy/integrate first | Hardware/driver lifecycle, licensing, master configuration |
| PROFINET Controller | Yes via commercial runtime/hardware | Buy/integrate first | RT/IRT class requirements, hardware, conformance, topology/recovery |

## Architectural consequence

ABIL should preserve a deterministic-execution abstraction roughly equivalent to:

```text
ValidatedControlArtifact
        +
DeploymentBinding
        +
CurrentAuthorityGrant
        +
PromotionReceipt
        +
Ownership/Fencing State
        |
        v
DeterministicExecutionTarget
    |- surviving PLC / semantic proxy
    |- commercial Linux soft PLC
    |- qualified protocol-offload runtime
    |- OpenPLC-class IEC runtime
    `- future native ABIL runtime
```

The interface should describe behavior ABIL must prove, not brand-specific implementation details. At minimum it should bind:

- deterministic task/cycle model and timing evidence;
- target I/O/protocol identity;
- exact input/output image or semantic command contract;
- startup/restart/resynchronization behavior;
- watchdog and communication-loss behavior;
- ownership/fencing generation;
- command transaction and ambiguity semantics;
- active artifact identity;
- authority-grant and promotion verification;
- independent safety-interface inventory;
- target-specific fallback behavior;
- resource reservation/isolation from intelligence services;
- diagnostics and execution receipts;
- known-good rollback/recovery path.

This abstraction allows ABIL's novel value—the reconstruction/evidence/coverage/commissioning system—to survive changes in execution technology.

## Recommended first qualification sequence

This research supports the following order once implementation authority eventually exists:

1. **Non-actuating R2** remains first. Do not pull fieldbus/control complexity into the substrate qualification.
2. **Modbus laboratory execution target** for deterministic scan, authority, transaction, restart, ownership, and fault semantics without a difficult industrial stack.
3. **Existing-PLC proxy target** on a real controlled test system to validate ABIL's generated semantic/control interface while leaving field I/O execution with a known controller.
4. **One commercially supported brownfield protocol path**, with DeviceNet + Hilscher especially relevant to the intended legacy-machine wedge.
5. **One high-performance open path**, likely EtherCAT, to determine how much runtime/protocol ownership ABIL should actually internalize.
6. Only then decide whether a native ABIL PLC-style runtime creates enough product value to justify owning the scheduler, I/O image, task model, fieldbus integration, online update, and lifecycle surface permanently.

## Decision impact

No change to PR #2 or PR #3 is required by this spike. The current architecture already says direct-control capability is protocol/interface-specific, permits conventional controller targets, and separates intelligence from deterministic execution.

The useful new conclusion is narrower:

> **Do not make “build our own PLC runtime and every fieldbus stack” a prerequisite for proving ABIL.**

A broad commercial soft-PLC / industrial communication-card path can carry the first production-oriented execution experiments while ABIL proves the part that is actually novel. Open stacks remain valuable for lab qualification, selective product adapters, portability pressure, and avoiding permanent dependence on one vendor.

## Open questions for later decision

These require dedicated evidence rather than assumption:

- Which first protocol best matches the actual ABIL pilot machine and available spare hardware?
- Does the first field appliance need PCIe/M.2 expansion for protocol cards, or can an external gateway satisfy the deployment constraints?
- Should ABIL's first executable control artifact be IEC 61131-3/ST, a vendor-neutral state-machine IR, generated C/C++, or a dual representation?
- Which execution target best supports ABIL's authenticated promotion / immutable-artifact / rollback model without unsafe online mutation paths?
- What runtime and dependency licenses are acceptable for a commercial appliance?
- What worst-case cycle/jitter envelope is actually required by the first machine class?
- Which protocols require third-party conformance/certification before ABIL can responsibly claim production support?

Those are future engineering-selection gates, not assumptions to smuggle into the current written architecture.
