# Bonbon Bureau 🍬

**A tiny, sugar-powered control plane for a household of OpenClaw agents: dispatch, status, handoffs, and just enough robotics bureaucracy.**

Bonbon Bureau is an experimental pattern for running a small factory of AI agents as trusted collaborators

The core idea:

```text
Human
  ↓
Miette / Operator-dispatcher
  ├─ routes product/taste/building work → named specialist agents
  ├─ routes infra/secrets/safety work    → infra specialist agents
  ├─ routes monitoring/source work       → monitoring agents
  └─ may later route local chores        → Candyland
```

## Names

- **Bonbon Bureau** — the server/setup of named agents and the operator control plane.
- **Candyland** — future local factory / worker-hive environment for boring chores.
- **Jellybean Junction** — possible future connector between Bonbon Bureau and Candyland.
- **Idea Pantry** — parking lot for future ideas, sketches, and maybe-later architecture.

## What this repo is

This repo is a scaffold for: 

- multi-agent operating conventions
- agent roster and responsibilities
- handoff/task schemas
- OpenClaw setup notes
- a small LangGraph-style dispatcher prototype
- public-safe runbooks and decision records
- portable agent PR attribution conventions

## Conventions

- [ROADMAP.md](ROADMAP.md) — phased plan for building the Bureau.
- [docs/openclaw-integration.md](docs/openclaw-integration.md) — mapping to OpenClaw runtime concepts.
- [docs/secrets-pattern.md](docs/secrets-pattern.md) — public-safe credential handling pattern.
- [docs/credential-sharing.md](docs/credential-sharing.md) — capability-based credential sharing between agents.
- [docs/langgraph-routing-spike.md](docs/langgraph-routing-spike.md) — router spike shape and non-goals.
- [docs/router-validation.md](docs/router-validation.md) — dependency-free fixture checks for routing behavior.
- [docs/agent-files.md](docs/agent-files.md) — public-safe copies of agent workspace files.
- [RUNBOOKS/install-miette.md](RUNBOOKS/install-miette.md) — install Miette locally from public-safe files.
- [patterns/](patterns/) — recurring task patterns distilled from real agent work.
- [fixtures/tasks/](fixtures/tasks/) — public-safe router fixtures based on those patterns.
- [docs/agent-pr-conventions.md](docs/agent-pr-conventions.md) — how Bonbon Bureau agents label/describe PRs across repos.
- [docs/idea-pantry.md](docs/idea-pantry.md) — parking lot for future ideas and maybe-later architecture.

## Initial architecture

Bonbon Bureau leans on OpenClaw for the agent runtime and uses a dispatcher layer only where structure helps.

```text
OpenClaw = agent runtime, workspaces, sessions, bindings, tools
LangGraph = optional Miette routing/state machine
GitHub repo = public source of truth for docs/schemas/runbooks
1Password/env/keyRefs = private credential source of truth, outside this repo
```

Start with boring, legible pieces. Add cleverness only when it earns its keep.
