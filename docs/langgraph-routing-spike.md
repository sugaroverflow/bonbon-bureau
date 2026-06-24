# LangGraph routing spike

The first router should prove the shape before adding framework complexity.

## Input

A task/request in plain language, preferably drawn from `fixtures/tasks/`.

```text
rotate a credential safely
```

## Output

A route, rationale, and handoff packet shaped like `TASK_SCHEMA.yaml`.

```yaml
owner: techie
category: infra
ownership: handoff
reason: Infrastructure, credentials, channels, or safety language detected.
```

## Current implementation

`langgraph-router/router.py` is intentionally rule-based. This keeps routing behavior visible while the Bureau vocabulary settles.

The seed fixtures are based on real repeated work from this server: envprov/keyRef migration, application secret rotation, Discord agent account setup, gateway health checks, plugin version updates, secret-scanning guardrails, and monitoring/source checks.

## Later LangGraph shape

```text
intake → classify → choose_route → prepare_handoff → checkpoint/status
```

Possible state fields:

- request
- classification
- selected_owner
- ownership_mode
- rationale
- handoff_packet
- safety_notes

## Non-goals for the spike

- no external writes
- no cross-repo mutation
- no private transcript access
- no automatic PR creation
- no synthetic happy-path flow
