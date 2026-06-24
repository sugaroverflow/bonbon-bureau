# Router validation

Bonbon Bureau keeps the first router deliberately small and dependency-free.

## Check command

```bash
python3 scripts/check.py
```

The checker:

- compiles `langgraph-router/router.py`
- confirms `patterns/` and `fixtures/tasks/` exist
- checks each fixture has the expected `TASK_SCHEMA.yaml` fields
- checks each fixture's `source_pattern` exists
- routes each fixture title through the router
- fails if routed owner/category diverges from the fixture

## Why this matters

The fixtures are based on real repeated work from the server, so they act as regression tests for Miette's routing behavior. If the router starts sending Discord setup to Glyphie or monitoring checks to Techie, the check should catch it.

## Dependency rule

No PyYAML or LangGraph dependency is required for this stage. Frameworks can come later once the behavior is clear.
