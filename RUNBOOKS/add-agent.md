# Runbook: add a named agent

Purpose: add a new specialist agent to Bonbon Bureau without blurring boundaries.

## Checklist

1. Define the agent's domain.
2. Define what should **not** be routed to the agent.
3. Create or update the public roster entry.
4. Create the OpenClaw agent/workspace privately.
5. Add workspace identity/persona/instructions.
6. Configure channel/account bindings privately, if needed.
7. Verify routing with a harmless test prompt.
8. Add a decision record if the agent changes the architecture.

## Public/private split

Public repo:

- role
- domain
- generic routing rules

Private config:

- tokens
- account IDs
- channel IDs
- workspace paths if sensitive
