#!/usr/bin/env python3
"""Route one public-safe fixture by its title."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "langgraph-router" / "router.py"


def title_from_fixture(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"')
    raise SystemExit(f"no title field found in {path}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: route_fixture.py fixtures/tasks/<name>.yaml", file=sys.stderr)
        return 2
    fixture = (ROOT / argv[1]).resolve()
    try:
        fixture.relative_to(ROOT)
    except ValueError:
        print("fixture must be inside this repo", file=sys.stderr)
        return 2
    title = title_from_fixture(fixture)
    return subprocess.run([sys.executable, str(ROUTER), title], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
