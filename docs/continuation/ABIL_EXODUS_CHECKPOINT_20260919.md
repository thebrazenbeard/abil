# ABIL Chat Exodus Checkpoint — 2026-09-19

Status: **STARTING_SNAPSHOT — FRESHNESS REQUIRED BEFORE EFFECT**

This repository checkpoint retires the temporary ChatGPT conversation that had been used as an ABIL-oriented execution terminal before broadening into a cross-repository portfolio sweep.

The conversation is not an ABIL worker identity, memory store, authority source, or required continuation surface.

## Durable reconstruction

Primary repository:
`thebrazenbeard/abil`

Fresh main at retirement:
`0812d9780ce1648820269fa142a43e17030ef793`

Current representative ABIL draft subjects:
- PR #2 — control-reconstruction successor architecture — `712d5b30b45ba9299dcfce0599878cb81db70e8f`
- PR #3 — R2 non-actuating substrate design — `1da5bc57b0228178300f6ba966d97d1dce807dc1`
- PR #6 — fail-closed write-capability admission — `b191822ecbc95ce120384acf1c17289b4b834033`
- PR #19 — integration claim lattice — `7583807ef1b0900c336bdff1b52824ec72791056`
- PR #25 — protected-head witness semantic primitive — `7e760c0f1bd4384a079948a20dba1cdef188f0dc`

PRs #4–#25 are largely independent/orthogonal research and design subjects stacked from the same architecture base. They are **not** one disposable chronological repair stack. Do not bulk-close them merely because later PR numbers exist.

## Current highest-value ABIL frontier

The highest-value research frontier exposed in this chat is PR #25's `ProtectedHeadWitness` semantic primitive.

Its purpose is to close the non-forking/current-head semantic gap across replay, evidence, trust, and governance-root state before downstream physical dispatch relies on those heads.

The next runtime should fresh-read:
1. PR #25 exact head/reviews;
2. the dependency lattice in PR #19;
3. write-admission boundary PR #6;
4. architecture/design anchors PR #2/#3;
5. current Bus coordination.

Then continue only the still-valid exact-head frontier.

## Authority boundary

This checkpoint grants no new authority.

Patrick remains required for protected effects including merge/canonical promotion, production deployment, machine connection/write authority, credential/provider mutation, paid infrastructure, and other materially irreversible effects unless a fresher exact authorization exists.

Research/source/test/review work remains distinct from implementation, install, runtime effect, qualification, and closure.

## Chat dechatification

ABIL does not require a permanent ABIL chat.

Future ABIL workers/reviewers may execute in temporary ChatGPT contexts, Work tasks, API runtimes, CLI sessions, model invocations, subagents, or other authorized terminals.

Their durable role, source subject, authority, assignment, evidence, and outputs must live in GitHub/Bus.

Cross-system Exodus architecture and the retiring terminal's portfolio checkpoint are in:
- Bus Draft PR #141
- branch: `work/exodus-dechatify-runtime-v1-20260919`
- checkpoint: `docs/checkpoints/EXODUS_PORTFOLIO_TERMINAL_2026-09-19.md`

No current ABIL operation should require this retired conversation's URL, title, conversation ID, hidden state, or accessibility.

## Future interface owner

Primary continuation interface:
`BT2 Coordinator`

Vera may use ABIL state for cross-project synthesis, but ABIL engineering/research dispatch should be reconstructed from this repository and the Bus rather than from a permanent worker chat.

Exact next directive:

`ABIL::RESTORE_FROM_DURABLE_STATE::FRESH_CHECK_PR25_AND_DEPENDENCY_LATTICE`
