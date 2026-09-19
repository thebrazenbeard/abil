# Deterministic Execution Topology Matrix

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO HARDWARE OR RUNTIME SELECTION**

Date: 2026-09-13

Parent research PR: Draft PR #4

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Question

Where should ABIL's eventual deterministic ordinary-control execution live relative to the adaptive/intelligence plane?

The decision is not binary `PLC versus PC`. Several topologies can satisfy the existing `DeterministicExecutionTarget` idea, with materially different fault containment, protocol burden, lifecycle cost, and field flexibility.

This document compares them without selecting a product or authorizing implementation.

## Current evidence that constrains the answer

Linux PREEMPT_RT is a credible deterministic-control substrate, but kernel documentation makes clear that real-time behavior depends on kernel configuration, scheduling, threaded interrupts, priority inheritance, CPU/workqueue/IRQ placement, and workload-specific measurement. `PREEMPT_RT present` is not itself a cycle-time qualification.

CODESYS Control for Linux SL currently provides an IEC 61131-3 soft PLC on 64-bit Linux with broad fieldbus support. Its current store page describes it as having **soft real-time properties** and as suitable for applications without hard demands on real-time behavior. The current product also:

- runs by default under a dedicated unprivileged Linux user;
- separates elevated operations into a PrivilegeProxy;
- supports CANopen, EtherCAT, EtherNet/IP, Modbus, PROFIBUS, and PROFINET roles;
- uses specific Hilscher hardware for its published PROFIBUS Master and PROFINET Controller paths;
- binds an IEC application to one CPU core in the ordinary Linux SL product;
- explicitly does not release that product for containers/VMs.

Hilscher's current cifX family executes the industrial protocol stack autonomously on the PC card and exchanges process data with the host through dual-port memory or DMA. A current M.2 DeviceNet product supports Master or Slave operation.

Those facts support a useful design principle: **protocol execution, deterministic control execution, and adaptive intelligence do not have to share one software process or even one processor to behave as one ABIL product.**

Sources:
- https://cdn.kernel.org/doc/html/latest/core-api/real-time/theory.html
- https://cdn.kernel.org/doc/html/latest/core-api/real-time/kernel-configuration.html
- https://store.codesys.com/en/codesys-control-linux-sl-1.html
- https://www.hilscher.com/products/pc-cards-for-industrial-ethernet-fieldbus/m2/cifx-m3042100bm-dnf

## Topology A — existing PLC as deterministic execution target

```text
ABIL intelligence / reconstruction
        |
        | bounded semantic/proxy contract
        v
Existing PLC
        |
        v
fieldbus / remote I/O
```

### Advantages

- strongest reuse of proven machine-specific deterministic behavior;
- smallest new fieldbus/runtime surface owned by ABIL;
- clean learner-versus-executor fault boundary;
- preserves existing scan timing, device configuration, and fieldbus ownership;
- often easiest rollback path;
- ideal for early coexistence-first field validation.

### Costs / limitations

- depends on surviving controller/project/interface capability;
- may require an engineered proxy interface that the legacy system does not expose today;
- cannot solve cases where the controller itself is failed, locked beyond usable integration, or obsolete beyond support;
- some legacy PLCs cannot provide a clean semantic-command boundary without project modification.

### Research disposition

Best first **field execution** topology when the existing controller can remain authoritative. It should be treated as a valid permanent terminal mode, not just a stepping stone.

## Topology B — one industrial PC, commercial soft PLC, protocol offload where useful

```text
industrial PC
  +---------------- intelligence services
  +---------------- protected promotion/authority state
  `---------------- commercial soft PLC runtime
                          |
                    protocol stack/card
                          |
                        I/O
```

### Advantages

- one appliance while keeping a mature IEC execution environment;
- broad protocol coverage can be bought/integrated rather than created by ABIL;
- protocol-offload cards can move fieldbus state machines and timing away from general host software;
- mature engineering/runtime tools can reduce first-product risk;
- provides a realistic target for generated IEC artifacts or a narrow generated interface.

### Costs / limitations

- same physical host still creates shared power, kernel, storage, thermal, and hardware-failure modes;
- soft-PLC real-time guarantees must match the actual machine class; current CODESYS Linux SL should not be assumed to satisfy hard real-time control merely because it is a PLC runtime;
- licensing/update/toolchain behavior becomes part of product lifecycle;
- ABIL must protect active artifact / authority state against both its own intelligence plane and vendor runtime tooling paths;
- component certification/conformance evidence has exact scope and does not automatically apply to the assembled appliance.

### Research disposition

Strong candidate for the first **replacement-capable product experiment**, especially when paired with a protocol-offload card for awkward brownfield networks. Requires exact timing and failure-mode qualification before any production claim.

## Topology C — one industrial PC, native ABIL deterministic runtime, protocol offload

```text
industrial PC
  +---------------- intelligence services
  +---------------- protected authority/artifact loader
  `---------------- native ABIL deterministic executor
                          |
                  protocol offload card
                          |
                        I/O
```

### Advantages

- ABIL owns the deterministic artifact model and runtime semantics without also reimplementing every fieldbus;
- protocol card can isolate protocol stack complexity and preserve a common host API across networks;
- one appliance and tighter control of artifact activation, rollback, transaction evidence, and execution receipts;
- creates a path to a genuinely ABIL-owned controller without immediately owning the lowest protocol layers.

### Costs / limitations

- ABIL now owns scheduler/task semantics, I/O image semantics, timers, watchdogs, task overrun behavior, persistent retain/state behavior, restart/resync, diagnostics, online lifecycle, and deterministic regression testing;
- PREEMPT_RT and CPU affinity are ingredients, not evidence that the finished runtime meets the target envelope;
- product/controller qualification surface grows materially;
- native runtime defects can directly affect production outputs.

### Research disposition

Plausible **second-generation** direct-control target after ABIL has already proven reconstruction and authority semantics against an existing/commercial deterministic executor.

## Topology D — one industrial PC, native runtime plus host-resident open protocol stacks

```text
industrial PC
  +---------------- intelligence
  +---------------- native deterministic executor
  `---------------- host protocol stacks/drivers
                          |
                        NIC/CAN
                          |
                         I/O
```

### Advantages

- maximum implementation control and vendor independence;
- potentially lowest recurring software/runtime license cost;
- highly inspectable for lab work;
- useful for protocols such as Modbus and selective EtherCAT/CANopen paths where mature open stacks exist.

### Costs / limitations

- ABIL simultaneously owns controller runtime, OS/driver timing, protocol state machines, recovery/interoperability, conformance, security maintenance, and product lifecycle;
- protocol-organization licensing/conformance obligations remain where applicable even if source code is open;
- largest attack surface for regressions and field incompatibility;
- easiest topology in which novel reconstruction work becomes buried beneath commodity controller/network engineering.

### Research disposition

Excellent **laboratory pressure test** and possibly appropriate for selected mature/simple protocols. Poor default for the first broad production replacement product.

## Topology E — ABIL intelligence appliance plus separate deterministic companion

```text
ABIL intelligence appliance
        |
        | authenticated bounded execution contract
        v
Deterministic companion controller
        |
        v
fieldbus / remote I/O
```

The companion can be an existing PLC, commercial controller, embedded real-time controller, soft-PLC IPC, or future ABIL-owned deterministic module.

### Advantages

- strongest physical/process fault containment between adaptive intelligence and production control;
- intelligence reboot/update/resource spikes need not disturb an already-promoted controller;
- makes the existing architectural rule `learning plane failure must not remove deterministic/manual capability` easier to demonstrate;
- lets ABIL evolve the intelligence appliance independently of the certified/qualified controller lifecycle;
- supports protocol-specific controller modules without changing the reconstruction product.

### Costs / limitations

- additional hardware/BOM, wiring, packaging, update coordination, and support surface;
- authenticated inter-processor protocol becomes safety/reliability-critical ordinary-control infrastructure;
- shared-machine state/version synchronization must be explicit;
- customer may perceive two boxes where one would be simpler.

### Research disposition

Strongest **fault-containment reference architecture**. Even if the final commercial product collapses both roles into one industrial PC, the software contract should remain capable of this topology so separation can be used where machine criticality justifies it.

## Comparative matrix

| Property | A Existing PLC | B Commercial soft PLC same IPC | C Native executor + offload | D Fully native host | E Separate companion |
|---|---:|---:|---:|---:|---:|
| Reuses proven deterministic stack | High | High | Medium | Low | High/variable |
| ABIL owns fieldbus complexity | Low | Low/medium | Low | High | Low/variable |
| ABIL owns runtime scheduler/control semantics | Low | Low | High | High | Variable |
| Intelligence/control physical fault separation | High | Low | Low | Low | High |
| Single-appliance simplicity | Low/depends | High | High | High | Low |
| Broad brownfield protocol path early | Medium | High | High with cards | Low/medium | High/variable |
| Product/conformance burden owned directly | Low | Medium | Medium/high | High | Medium/variable |
| Good first production-oriented path | Yes when PLC survives | Yes, target-dependent | Later | Usually no | Yes for high-containment needs |
| Good lab pressure-test path | Medium | High | High | High | Medium |

## Architecture consequence

ABIL should define deterministic execution as a **replaceable trust-domain interface**, not as a process that is assumed to live inside the intelligence executable.

The contract should be implementable over:

- same-process/same-host test harnesses where allowed for lab use;
- separate processes on one host;
- commercial soft-PLC runtime on one host;
- PCIe/M.2 protocol-offload devices;
- network/local-IPC link to a surviving PLC;
- physically separate companion controller.

A production qualification profile must state which topology is actually used. No qualification may silently transfer from one topology to another merely because the generated control model is the same.

## Required execution-target contract pressure

Regardless of topology, the execution target should eventually expose or bind:

- immutable target/runtime identity;
- active artifact digest and promotion receipt;
- current authority/ownership generation;
- deterministic task/cycle configuration;
- exact input/output or semantic-command namespace;
- startup/activation handshake;
- heartbeat/health semantics that do not masquerade as proof of physical action outcome;
- bounded command transaction IDs and acknowledgement states;
- restart/resynchronization rules;
- retain/persistent state identity;
- watchdog/communications-loss behavior;
- protocol/card/driver/firmware identity;
- qualification/conformance provenance and scope;
- safety-interface/handshake inventory without taking safety ownership;
- execution receipts/diagnostics;
- target-specific fallback and known-good rollback path.

The adaptive plane may propose new artifacts but does not get to mutate those runtime facts unilaterally.

## Appliance-selection consequence

Do not finalize a tiny appliance form factor until at least these questions are answered:

- Does the target need PCIe, M.2 B+M, mini-PCIe, CAN, isolated serial, or another industrial communications expansion path?
- Is one x86 CPU running both intelligence and deterministic execution acceptable for the first target machine's failure/timing envelope?
- Does the chosen soft-PLC/runtime support the needed hard/soft real-time class on the exact OS/hardware?
- Is a protocol-offload card worth the BOM cost to preserve conformance/timing boundaries?
- What persistent storage, watchdog, RTC, power-loss behavior, thermal envelope, and 24 VDC integration are required?
- Is a separate deterministic companion cheaper overall than qualifying a complex shared-host design?

Those are product-selection gates, not reasons to freeze hardware now.

## Recommended sequencing

1. Keep **Topology A** as the preferred real-machine coexistence path wherever a usable PLC survives.
2. Use **Topology B** as the leading production-oriented replacement experiment because it can exercise ABIL's artifact/authority/coverage model without simultaneously inventing a PLC runtime.
3. Keep **Topology E** as the fault-containment reference and support it in the execution-target interface from the start.
4. Prototype **Topology D** cheaply for Modbus/open-stack lab pressure tests, not as an automatic product choice.
5. Move toward **Topology C** only if owning the deterministic executor creates enough strategic value to justify its lifecycle and qualification burden.

## Research disposition

The topology research does not require a PR #2 source change. The current architecture already distinguishes the intelligence plane from deterministic execution and permits existing PLC, conventional controller, and ABIL runtime targets.

The important engineering constraint is to avoid implementation choices that accidentally collapse those logical trust domains into one inseparable process or one untestable host failure domain.

No hardware selection, procurement, license acceptance, implementation planning, machine connection/write, commissioning, certification claim, deployment, merge, or canonical promotion is authorized by this research.