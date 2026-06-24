# 2026-06-24: OpenClaw plus LangGraph

## Status

Accepted

## Context

Bonbon Bureau needs a popular orchestration tool/library, but should preserve named OpenClaw agents as trusted collaborators.

## Decision

Use OpenClaw as the multi-agent runtime foundation. Use LangGraph as an optional dispatcher/supervisor layer for Operator workflows.

## Consequences

- OpenClaw remains responsible for workspaces, sessions, tools, channel routing, and agent identity.
- LangGraph can add structured routing, state, retries, and human-in-the-loop checkpoints.
- Bonbon Bureau avoids becoming a second competing agent identity system.
