# LangGraph router prototype

This is a tiny, dependency-light prototype of the routing logic Bonbon Bureau might later implement with LangGraph.

It intentionally starts as plain Python so the schema and behavior are easy to inspect before adding runtime complexity.

## Try it

```bash
python3 langgraph-router/router.py "rotate a credential safely"
python3 langgraph-router/router.py "draft product copy for a new feature"
```

## Later

Replace the rule-based classifier with a LangGraph graph:

```text
intake → classify → choose_route → prepare_handoff → checkpoint/status
```
