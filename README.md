# Bonbon Bureau 🍬

**A tiny, sugar-powered control plane for a household of OpenClaw agents: dispatch, status, handoffs, and just enough robotics bureaucracy.**

Bonbon Bureau is an experimental pattern for running a small factory of AI agents as trusted collaborators

The core idea:

```text
Human
  ↓
Operator / dispatcher
  ├─ routes product/taste/building work → named specialist agents
  ├─ routes infra/secrets/safety work    → infra specialist agents
  ├─ routes monitoring/source work       → monitoring agents
  └─ may later route local chores        → Candyland
```

## Names

- **Bonbon Bureau** — the server/setup of named agents and the operator control plane.
- **Candyland** — future local factory / worker-hive environment for boring chores.
- **Jellybean Junction** — possible future connector between Bonbon Bureau and Candyland.

## What this repo is

This repo is a scaffold for: 

- multi-agent operating conventions
- agent roster and responsibilities
- handoff/task schemas
- OpenClaw setup notes
- a small LangGraph-style dispatcher prototype
- public-safe runbooks and decision records

## Initial architecture

Bonbon Bureau leans on OpenClaw for the agent runtime and uses a dispatcher layer only where structure helps.

```text
OpenClaw = agent runtime, workspaces, sessions, bindings, tools
LangGraph = optional Operator routing/state machine
GitHub repo = public source of truth for docs/schemas/runbooks
1Password/env/keyRefs = private credential source of truth, outside this repo
```

Start with boring, legible pieces. Add cleverness only when it earns its keep.
