# Router validation and CI

Date: 2026-06-24

## Decision

Bonbon Bureau will keep the initial router validation dependency-free and run it in GitHub Actions on pushes to `main` and on pull requests.

## Rationale

The router is currently a small rule-based spike. A lightweight check is enough to catch drift between real task fixtures and expected owner/category routing without adding framework or YAML dependencies too early.

## Consequences

- `scripts/check.py` is the source of truth for fixture validation.
- The CI workflow only needs Python.
- LangGraph and stricter schema validation can be added later if the rule-based version stops being enough.
