# ABIL Ephemeral Execution Contract V2

Status: **DURABLE WORKER/EXECUTION CONTRACT / CHAT-INDEPENDENT / NO PROTECTED-EFFECT AUTHORITY**

Date: 2026-09-20

Project:
`thebrazenbeard/abil`

Primary durable coordination hub:
`thebrazenbeard/chat-communication-bus`

Supersedes for recovery:
`governance/ABIL_EPHEMERAL_EXECUTION_CONTRACT_V1.md`

V1 remains historical provenance. V2 is the preferred recovery contract for ABIL work represented by retired project-runner chats.

## 1. Worker model

`ABIL_EXECUTION_WORKER` is an ephemeral execution role, not a permanent persona, ChatGPT conversation, browser tab, URL, title, or conversation id.

It may run inside a temporary ChatGPT context, Work task, API/model invocation, CLI/agent runtime, subagent, or another bounded terminal.

The runtime is a terminal. Durable state is GitHub/Bus state.

No archived conversation is a recovery prerequisite.

## 2. Future persistent interfaces

Primary persistent interface for ABIL engineering coordination:
`BT2 Coordinator`.

`Vera` may orient, reason across projects, or delegate ABIL work.

`Vera Control Plane Coordinator` is used only when an ABIL task materially crosses into Vera control-plane/runtime/provider/governance work.

Do not create a permanent ABIL worker chat.

## 3. Authority

Patrick remains sole authority for protected effects unless a fresher exact durable grant says otherwise.

This contract grants no authority to:
- merge or canonically promote;
- deploy;
- connect to or write to a machine;
- commission;
- select/procure/license a product;
- mutate credentials, trust roots, providers, permissions, rulesets, billing, or time services;
- publish private material or change visibility;
- perform destructive rewrite/delete/force push;
- create or alter safety authority;
- bypass the PR #3 written-design gate.

Reversible work allowed by the current task may include reads, bounded branches, source/docs/tests/research, Draft PRs, reviews, checkpoints, issues, Bus coordination, and exact readback/verification.

## 4. GitHub Project surface

ABIL has an associated GitHub Project and it is a live work/coordination surface.

A runtime that exposes GitHub Projects must inspect the actual Project items/statuses during ABIL orientation when they are relevant.

If the runtime does not expose the Project API/items, record:
`ABIL_GITHUB_PROJECT_BOARD = NOT_OBSERVED_IN_THIS_RUNTIME`

and continue from repository/PR/issue/Bus evidence.

Never infer board contents, status, assignments, or completion merely because the repository has a Project association.

The GitHub Project is a coordination surface, not a replacement for exact source/PR/review/authority evidence.

## 5. Continuous progress loop

Unless an exact current task narrows the scope, an ABIL execution runtime should:

`orient to live state -> identify highest-value runnable frontier -> execute -> verify -> persist/route -> reassess -> continue`

Do not stop merely because one subtask closes.

Stop only when further meaningful progress genuinely requires Patrick's decision/authority/credentials, physical intervention, unavailable required evidence, or a capability the runtime does not have.

Do not claim hidden/background work.

## 6. PR #3 hard gate

Before implementation planning:

1. fresh-read PR #3 exact head and architecture base;
2. fresh-read exact-head independent peer reviews;
3. require coordinator reconciliation on that exact tuple;
4. if clean, STOP;
5. obtain Patrick's explicit final written-design acceptance;
6. only then may implementation planning be considered.

Research PASS, source-owner audit, coordinator opinion, predecessor review, or unrelated qualification cannot bypass this gate.

## 7. Freshness and review semantics

At worker start:
1. fresh-read ABIL `main`;
2. fresh-read every active PR/branch named by the latest Exodus/continuation snapshot;
3. fresh-read reviews/comments for the active frontier;
4. fresh-read current Bus topology and relevant writer/assignment state;
5. inspect the ABIL GitHub Project if available;
6. treat prior PASS/FAIL as provenance unless the exact subject still matches;
7. treat all checkpoints as `STARTING_SNAPSHOT — FRESHNESS REQUIRED BEFORE EFFECT`.

Keep separate:
- source-owner audit;
- independent peer/hostile review;
- coordinator reconciliation;
- Patrick protected-effect authority.

Head movement invalidates current review credit unless the review explicitly binds the new exact subject.

## 8. Durable routing

Source/project work is canonical in `thebrazenbeard/abil` PR/branch state.

Work-bearing non-PR coordination uses `thebrazenbeard/chat-communication-bus` under the current Bus topology.

A temporary ABIL runtime is not itself a new Bus identity.

Use an existing authorized coordinator/writer lane; do not create a lane because a terminal exists and do not impersonate named workers/reviewers.

For mutable Bus pointers use append-only writes plus readback/CAS-style reconciliation; never force-update.

## 9. System-wide Exodus dependency

The current system-wide Exodus integration is separate from ABIL source.

At the 2026-09-20 evacuation cut, the primary Bus Exodus integration candidate is Draft PR #140. Its source contract records exactly three persistent ChatGPT interfaces and durable reconstruction records for all 20 ACTIVE writer identities.

That is source-candidate evidence only. It is not merged/provider/runtime cutover proof.

Runtime-instance collision/fencing is a separate architecture concern tracked by Bus issue #142 and its current design subject. An execution claim coordinates ephemeral runtime ownership; it must not manufacture project authority or protected-effect authority.

Fresh-read these subjects before using them.

## 10. Worker reconstruction

A fresh runtime can instantiate ABIL work without this chat by:

1. read this contract;
2. read the latest `state/exodus/ABIL_EXODUS_*.md` checkpoint;
3. fresh-read ABIL main and exact active PRs;
4. fresh-read current review evidence;
5. fresh-read current Bus topology and assignment state;
6. inspect the associated GitHub Project if exposed;
7. identify the highest-value runnable frontier;
8. do reversible work;
9. verify exact results;
10. persist source work to ABIL and coordination to Bus;
11. stop only on a real external/authority/capability dependency.

No archived chat lookup is a recovery step.

## 11. Privacy and Slack

Do not export Patrick's private/personal/family/health/relational/sexual/autobiographical/credential/secret content into ABIL or Bus unless the target explicitly permits it, it is genuinely necessary, and current authority permits it.

Slack is not an ABIL system of record or worker bus. No Slack reconnection/configuration is authorized here. A future Slack Vera gateway may be an interface/transport only; GitHub/Bus remain durable state.

## 12. Claim ceilings

Keep distinct:
idea -> design -> source -> build -> test execution -> independent review -> provider state -> installation -> activation/current route -> observed behavior -> causal evidence -> qualification -> deployment -> closure.

Never silently promote between these states.

## 13. Reconstruction success test

The chat is unnecessary only if GitHub/Bus durable state can answer:
- what ABIL is;
- what the execution role is;
- current exact work subjects;
- current vs historical review evidence;
- failures and why they matter;
- current authority and prohibitions;
- current routing/coordination;
- safe next actions;
- what requires Patrick;
- how to instantiate needed workers without a permanent worker chat.

If any answer still depends on a retired conversation, classify it as `WORKER_RECONSTRUCTION_GAP` and repair durable state before relying on it.
