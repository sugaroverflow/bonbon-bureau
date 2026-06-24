# Architecture

Bonbon Bureau is a control-plane pattern for named personal agents.

## Design principles

1. **Named agents are trusted collaborators, not disposable workers.**
   They keep continuity, taste, domain judgment, and personality.
2. **The Operator routes; it does not replace specialists.**
   It should classify, hand off, track status, and escalate.
3. **OpenClaw owns agent runtime concerns.**
   Workspaces, sessions, tools, channel routing, and per-agent state stay in OpenClaw.
4. **LangGraph is optional structure around routing/state.**
   Use it for dispatcher workflows, not as a second identity system.
5. **Public docs, private secrets.**
   This repo can contain architecture and runbooks, but never credentials or raw personal data.

## Components

### OpenClaw multi-agent runtime

Each agent should have its own:

- workspace
- identity/persona files
- memory boundaries
- tool/skill conventions
- state/session store
- channel/account binding where needed

### Operator

Operator is the control-plane agent. It decides:

- who should handle a task
- whether a task needs clarification
- whether a specialist should own the next response
- what is blocked
- what needs escalation

### LangGraph dispatcher

A small dispatcher graph can provide repeatable routing:

```text
intake → classify → choose route → prepare handoff → record status
```

Use handoffs when a specialist should take over. Use bounded specialist calls when Operator should retain ownership.

### Candyland boundary

Candyland is intentionally out of near-term scope. It represents a future local worker/factory environment for chores and utility jobs.

### Jellybean Junction boundary

Jellybean Junction is a possible future connector between Bonbon Bureau and Candyland.

## Data boundaries

Public in this repo:

- generic architecture
- schemas
- non-sensitive runbooks
- example task routes
- public-safe agent domains

Private elsewhere:

- credentials
- tokens
- production config
- personal transcripts
- private channel IDs
- hostnames/IPs unless deliberately public
