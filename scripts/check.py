#!/usr/bin/env python3
"""Dependency-free checks for Bonbon Bureau.

Validates the tiny router and the public-safe task fixtures without requiring PyYAML.
"""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "langgraph-router" / "router.py"
FIXTURES = ROOT / "fixtures" / "tasks"
PATTERNS = ROOT / "patterns"

REQUIRED_TOP_LEVEL = {
    "id",
    "source_pattern",
    "title",
    "requester",
    "status",
    "owner",
    "priority",
    "deadline",
    "category",
    "context",
    "desired_output",
    "next_action",
    "blockers",
    "blocked_on",
    "created_at",
    "updated_at",
    "handoff",
}


def parse_simple_fixture(path: Path) -> dict[str, str]:
    """Parse the top-level scalar fields we need from our deliberately simple YAML."""

    fields: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        if not raw or raw.startswith("#") or raw.startswith(" "):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def route(text: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(ROUTER), text],
        check=True,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
    )
    return json.loads(result.stdout)


def check_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    fields = parse_simple_fixture(path)
    missing = sorted(REQUIRED_TOP_LEVEL - set(fields))
    if missing:
        errors.append(f"missing top-level fields: {', '.join(missing)}")
        return errors

    pattern = ROOT / fields["source_pattern"]
    if not pattern.exists():
        errors.append(f"source_pattern does not exist: {fields['source_pattern']}")

    packet = route(fields["title"])
    if packet["owner"] != fields["owner"]:
        errors.append(f"router owner {packet['owner']!r} != fixture owner {fields['owner']!r}")
    if packet["category"] != fields["category"]:
        errors.append(f"router category {packet['category']!r} != fixture category {fields['category']!r}")

    for key in ("blockers", "handoff"):
        if key not in fields:
            errors.append(f"missing required field {key}")

    return errors


def main() -> int:
    errors: list[str] = []

    py_compile.compile(str(ROUTER), doraise=True)

    if not PATTERNS.is_dir():
        errors.append("patterns/ is missing")
    if not FIXTURES.is_dir():
        errors.append("fixtures/tasks/ is missing")

    fixtures = sorted(FIXTURES.glob("*.yaml"))
    if not fixtures:
        errors.append("no fixture YAML files found")

    for fixture in fixtures:
        fixture_errors = check_fixture(fixture)
        for error in fixture_errors:
            errors.append(f"{fixture.relative_to(ROOT)}: {error}")

    if errors:
        print("Bonbon Bureau check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Bonbon Bureau check passed: {len(fixtures)} fixtures validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
