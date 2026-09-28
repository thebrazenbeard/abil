# ABIL Appliance OS Baseline Research

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO OS OR PRODUCT SELECTION AUTHORITY**

Date: 2026-09-13

Parent research PR: Draft PR #4

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Question

What Linux baseline best supports the **first** ABIL control-capable laboratory / product-qualification work without prematurely locking the eventual appliance OS?

The current candidate set has included Tiny Core/CorePure64 because its small, RAM-oriented, remasterable system is attractive for an appliance. The runtime/compliance research adds a competing concern: the first control-capable platform should minimize unsupported OS/runtime integration while ABIL is still proving the reconstruction and deterministic-execution boundaries.

## Current evidence

### Tiny Core / CorePure64 remains active

Tiny Core remains actively released in 2026. The x86_64 release tree contains CorePure64 17.0 and TinyCorePure64 17.0 images dated February 2026.

Tiny Core's own documentation emphasizes that it is **not a turn-key operating system**. Its design loads the base system into RAM and uses extensions plus explicit persistence mechanisms. The project describes Core as suitable for servers/appliances/custom systems.

This has real appliance advantages:

- tiny mutable base surface;
- clean boot from a known image;
- explicit application-extension composition;
- easy remaster/recovery concepts;
- strong separation between base image and persistent application/data state when deliberately engineered.

It also has real first-product costs:

- ABIL would own substantially more distro integration and extension packaging;
- persistent machine/model/evidence/authority state needs a deliberately engineered storage model rather than assuming ordinary root-filesystem semantics;
- vendor runtime/driver packages may assume a conventional Debian/RedHat-style userland;
- industrial driver/vendor test matrices are less likely to include Tiny Core;
- the small base does not itself solve secure updates, signed images, rollback, storage corruption, or deterministic timing.

Sources:
- https://www.tinycorelinux.net/17.x/x86_64/release/
- https://www.tinycorelinux.net/concepts.html
- https://www.tinycorelinux.net/downloads.html

### Debian 13 is the conservative qualification baseline

Debian's current stable release is Debian 13 `trixie`. Debian explicitly describes stable as its production release and primarily recommended distribution.

Debian 13 currently provides a signed `linux-image-rt-amd64` package using PREEMPT_RT, alongside the ordinary signed amd64 kernel. This gives ABIL a vendor-maintained path for both ordinary development and real-time kernel experiments without creating a custom kernel-distribution story on day one.

CODESYS Control for Linux SL currently lists **Debian- and RedHat-based 64-bit Linux** as supported platforms. The CODESYS store also explicitly says other distributions may be used at the user's discretion but are not part of the product release and related tests.

This distinction matters: Debian does not make ABIL deterministic or certified by itself, but it reduces unsupported integration variables while the execution contract is being qualified.

Sources:
- https://www.debian.org/releases/
- https://packages.debian.org/stable/kernel/linux-image-rt-amd64
- https://store.codesys.com/en/codesys-control-linux-sl-1.html

### Ubuntu Core 26 is a serious later appliance option, not an automatic first runtime target

Ubuntu Core 26 was released in May 2026 and is a minimal immutable Ubuntu appliance OS built on Ubuntu 26.04 LTS. Canonical currently advertises transactional/appliance-oriented image composition and up to 15 years of security maintenance.

Those properties fit a commercial ABIL appliance better than a hand-maintained mutable general-purpose distro in several respects:

- immutable base/image model;
- managed update/rollback concepts;
- long security-maintenance window;
- production embedded/appliance focus.

However, Ubuntu Core's snap/image model is materially different from a conventional Debian/RedHat installation. CODESYS' current Linux SL product requirements describe a conventional Linux runtime deployment with required shared libraries, SSH-assisted deployment, privilege proxy, and device-bound licensing. That is not evidence that Ubuntu Core is unsupported, but it **is** evidence that compatibility should be proven rather than assumed.

Source:
- https://documentation.ubuntu.com/core/uc26/

## Baseline comparison

| Criterion | Debian 13 minimal | Tiny Core/CorePure64 17 | Ubuntu Core 26 |
|---|---:|---:|---:|
| Conventional industrial/vendor Linux compatibility | High | Low/unknown | Medium/needs proof |
| CODESYS release-family fit | High | Outside stated tested families | Needs exact proof |
| Signed packaged PREEMPT_RT path | Yes | Custom/integration work | Separate Ubuntu RT path needs product-fit check |
| Minimal appliance image potential | Medium/high with hardening/remastering | Very high | High |
| Immutable/known-good base model | Must be engineered | Native design tendency | Core design goal |
| Package/driver ecosystem | Very high | Small/custom extensions | Ubuntu ecosystem but snap appliance model |
| ABIL-owned distro integration burden | Low/medium | High | Medium/high initially |
| Best use now | qualification/dev baseline | later native appliance experiment | later managed-appliance candidate |

## Research recommendation

### First development / qualification baseline

Use **minimal Debian 13 x86_64** as the leading first control-capable software baseline, with the ordinary signed kernel for general work and the signed Debian PREEMPT_RT kernel for timing experiments where the target requires it.

This is a research recommendation, not a product selection. Its purpose is to minimize unrelated OS work while ABIL qualifies:

- execution-target contracts;
- process/fault separation;
- protocol-card integration;
- artifact activation/authority semantics;
- restart/resynchronization;
- timing/resource behavior;
- evidence capture.

### Tiny Core/CorePure64 role

Keep **CorePure64** in the program as a later appliance experiment, especially if ABIL eventually owns more of the runtime and wants a tiny, boot-to-known-state system.

Do not make it the prerequisite for the first field/control proof. Before product use it would need evidence for at least:

- reproducible signed/remastered image construction;
- secure update/rollback mechanism;
- exact industrial NIC/card/driver support;
- persistent state partitioning and crash consistency;
- log/evidence retention;
- time synchronization;
- watchdog integration;
- device licensing/runtime compatibility;
- PREEMPT_RT or equivalent target timing path if native deterministic control shares the host;
- field recovery procedure.

### Ubuntu Core role

Keep **Ubuntu Core 26** as a later managed-appliance candidate if transactional image updates, secure device lifecycle, and long-term maintenance outweigh the integration cost of its snap/image model.

The first question is not `is Ubuntu Core good?`; it is `can the exact deterministic runtime, protocol hardware, licensing, authority store, and field-recovery model be cleanly qualified inside its confinement/update architecture?`

## Persistent-state architecture consequence

Regardless of distro, ABIL should not store all valuable state as an undifferentiated mutable root filesystem.

At minimum, future appliance design should distinguish:

1. **boot/base image** — reproducible system software;
2. **application/runtime image/artifacts** — versioned executable software;
3. **candidate model/artifact storage** — writable by intelligence plane but not active by implication;
4. **protected active artifact / authority state** — separately integrity-protected and anti-rollback;
5. **machine/deployment evidence/model state** — durable, exportable, versioned;
6. **transaction/ambiguity journal** — survives restart sufficiently to prevent blind physical-command replay;
7. **logs/diagnostics** — bounded and recoverable;
8. **recovery image/configuration** — independently usable when the normal intelligence stack is unavailable.

This decomposition matters more to ABIL than whether `/` is tiny or large.

## Recovery-media consequence

The earlier idea of a bootable recovery USB still makes sense, but a persistent live USB should not be the authoritative permanent controller state.

A cleaner model is:

- installed appliance OS/runtime on internal industrial storage;
- durable deployment/evidence/authority state on explicitly managed persistent partitions/stores;
- bootable signed recovery/install media able to verify/restore the system while preserving or deliberately restoring deployment state according to authority rules;
- no ordinary restore of old disk bytes may resurrect obsolete control authority.

## Decision gates before product freeze

The OS can remain unfrozen until at least these are known:

- first industrial hardware platform;
- first deterministic-execution topology;
- first protocol/card/runtime;
- target cycle/jitter/failure envelope;
- update/connectivity model for deployed customers;
- device licensing model;
- NRTL/CE/customer product requirements;
- secure-boot/TPM/key-storage plan;
- offline recovery/support requirements;
- expected field service lifetime.

Freezing the distro before those facts would optimize the wrong layer.

## Research disposition

The new evidence changes the priority but not the long-term option set:

> **Debian first for control-capable qualification; Tiny Core/CorePure64 remains a later native-appliance candidate; Ubuntu Core remains a later managed immutable-appliance candidate.**

That sequence gives ABIL a boring, vendor-compatible first substrate without abandoning the eventual goal of a small purpose-built appliance.

No PR #2 or PR #3 change is required. No OS selection, procurement, implementation planning, machine connection/write, commissioning, certification claim, deployment, merge, or canonical promotion is authorized by this research.