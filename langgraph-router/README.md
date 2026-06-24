# LangGraph router prototype

This is a tiny, dependency-light prototype of the routing logic Bonbon Bureau might later implement with LangGraph.

It intentionally starts as plain Python so the schema and behavior are easy to inspect before adding runtime complexity.

## Try it

```bash
python3 langgraph-router/router.py "rotate a credential safely"
python3 langgraph-router/router.py "draft product copy for a new feature"
python3 scripts/route_fixture.py fixtures/tasks/secret-rotation.yaml
```

## Validate fixtures

```bash
python3 scripts/check.py
```

Fixtures live in `fixtures/tasks/` and are grounded in recurring real tasks from the server.

## Later

Replace the rule-based classifier with a LangGraph graph:

```text
intake → classify → choose_route → prepare_handoff → checkpoint/status
```
