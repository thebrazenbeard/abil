from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", ".repairs", ".worktrees"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

REQUIRED = (
    "README.md",
    "docs/PRODUCT_THESIS.md",
    "docs/ARCHITECTURE_BOUNDARIES.md",
    "docs/CONTROL_AUTHORITY_AND_LIFECYCLE_CONTRACT.md",
    "docs/FIELD_VALIDATION_ROADMAP.md",
    "docs/research/CONSOLIDATION_MANIFEST_20260928.json",
)


def tracked_files(suffix: str):
    for path in ROOT.rglob(f"*{suffix}"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        yield path


def validate() -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in tracked_files(".json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")

    for path in tracked_files(".md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if (
                not target
                or "://" in target
                or target.startswith("mailto:")
                or target.startswith("#")
            ):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(
                    f"missing local link: {path.relative_to(ROOT)} -> {target}"
                )

    manifest_path = ROOT / "docs/research/CONSOLIDATION_MANIFEST_20260928.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = manifest.get("entries", [])
        if manifest.get("entry_count") != len(entries):
            errors.append("consolidation manifest entry_count mismatch")
        for entry in entries:
            relative = entry.get("path")
            if not isinstance(relative, str) or not (ROOT / relative).is_file():
                errors.append(f"consolidation manifest missing path: {relative}")
            if entry.get("classification") != "HISTORICAL_NON_NORMATIVE_EVIDENCE":
                errors.append(f"unexpected consolidation classification: {relative}")
        authority = manifest.get("authority", {})
        for key in (
            "imports_are_runtime_authority",
            "imports_are_production_qualification",
            "imports_are_safety_authority",
            "canonical_architecture_files_overwritten",
        ):
            if authority.get(key) is not False:
                errors.append(f"unsafe consolidation authority flag: {key}")

    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print("ABIL repository validation: PASS")
