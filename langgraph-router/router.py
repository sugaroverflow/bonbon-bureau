#!/usr/bin/env python3
"""Tiny public-safe routing prototype for Bonbon Bureau.

This is deliberately boring: keyword routes first, framework later.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class Route:
    category: str
    owner: str
    ownership: str
    reason: str


ROUTES: list[tuple[set[str], Route]] = [
    ({"secret", "credential", "token", "gateway", "infra", "cron", "routing", "security"}, Route("infra", "techie", "handoff", "Infrastructure, credentials, or safety language detected.")),
    ({"product", "copy", "design", "taste", "feature", "strategy", "build"}, Route("product", "lotus", "handoff", "Product, creative, or building language detected.")),
    ({"monitor", "watch", "source", "check", "alert", "status"}, Route("monitoring", "glyphie", "handoff", "Monitoring or source-checking language detected.")),
]

DEFAULT = Route("coordination", "miette", "bounded_help", "No specialist route was obvious; keep coordination with Miette.")


def classify(text: str) -> Route:
    lowered = text.lower()
    for keywords, route in ROUTES:
        if any(word in lowered for word in keywords):
            return route
    return DEFAULT


def handoff_packet(text: str) -> dict:
    route = classify(text)
    now = datetime.now(timezone.utc).isoformat()
    return {
        "id": "bb-example",
        "title": text[:80],
        "requester": "example",
        "status": "proposed",
        "owner": route.owner,
        "priority": "normal",
        "category": route.category,
        "context": text,
        "desired_output": "Route this task and prepare the next action.",
        "next_action": f"Send to {route.owner} with minimal necessary context.",
        "blocked_on": None,
        "created_at": now,
        "updated_at": now,
        "handoff": {
            "from": "miette",
            "to": route.owner,
            "reason": route.reason,
            "ownership": route.ownership,
            "included_context": text,
            "excluded_context": "Secrets, raw transcripts, and irrelevant private details.",
            "safety_notes": "Public-safe example packet only.",
        },
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: router.py <task text>", file=sys.stderr)
        return 2
    print(json.dumps(handoff_packet(" ".join(argv[1:])), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
