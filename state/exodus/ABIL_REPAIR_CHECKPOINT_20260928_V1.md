# ABIL Repair Checkpoint — 2026-09-28 V1

This checkpoint supersedes chat/session-dependent restoration as the current
repository repair handoff.

Canonical source baseline before the repair branch:

thebrazenbeard/abil@13b989be46a986c95c75612e332779a75c0f0f1f

That baseline already contains the integrated successor architecture and R2
non-actuating substrate design through the later canonical integration commits.
Historical draft PRs #2 and #3 are therefore not pending architecture changes.

The 2026-09-28 repair branch:

- preserves canonical architecture files from the baseline;
- recovers only files absent from canonical main across historical PRs #4-#26;
- classifies recovered research as historical/non-normative evidence;
- preserves the V1/V2 Exodus and ephemeral execution records as provenance;
- adds a source-bound consolidation manifest;
- adds a repository-integrity validator and GitHub Actions health gate.

No recovered artifact grants production-control, commissioning, deployment,
write, promotion, or safety authority. ABIL remains a foundation/research/
architecture repository with no production control implementation on main.

For exact recovered-file provenance, use:

docs/research/CONSOLIDATION_MANIFEST_20260928.json

For current repository-health qualification, run:

py -3 scripts/validate_repository.py on Windows, or
python scripts/validate_repository.py on Python 3.12 environments.
