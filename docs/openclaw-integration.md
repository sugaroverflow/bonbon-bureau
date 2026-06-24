# OpenClaw integration plan

Bonbon Bureau should use OpenClaw's native multi-agent features rather than inventing a parallel runtime.

## Agent boundaries

Each named agent should have its own OpenClaw scope:

- workspace
- identity/persona files
- memory files
- session history
- tool/skill conventions
- auth/profile boundaries as appropriate

## Miette's role

Miette is the Operator agent. She routes and coordinates. She should have enough visibility to prepare handoffs, but not broad permission to leak private context between agents.

## Binding strategy

Use OpenClaw channel/account/session bindings to route human-facing messages to the right agent. Keep binding IDs and private channel/account details out of this repo.

## Session strategy

- Miette owns ambiguous or cross-agent requests.
- Specialists own domain-specific work.
- Handoffs should include only the minimum required context.
- Status should be summarized, not copied from raw transcripts.

## Tool strategy

Give Miette tools for:

- reading public Bureau docs
- preparing handoff packets
- checking status where allowed
- opening public-safe PRs only after explicit permission/workflow support

Avoid giving Miette unnecessary credentials or broad private-data access.
