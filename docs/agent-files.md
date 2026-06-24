# Agent files

This repo includes public-safe versions of each Bonbon Bureau agent's workspace files.

These files are meant to show the shape of the agent household without exposing private runtime state.

## Included files

Each agent directory may include:

- `IDENTITY.md` — name, role, vibe, emoji
- `SOUL.md` — durable operating personality and boundaries
- `AGENTS.md` — workspace/routing instructions
- `USER.md` — public-safe human/context preferences
- additional role-specific files, such as Miette's `ROUTING.md` and `ESCALATION.md`

## Redaction rule

Public copies should preserve:

- agent name and role
- broad responsibilities
- routing boundaries
- tone/personality
- safe operating rules

Public copies should remove:

- raw secrets or tokens
- private account/channel IDs
- local machine paths unless intentionally generic
- private personal details
- surprise/project-sensitive context
- raw session or memory dumps

The public-safe copy should be useful for a talk, demo, or repo reader. It should not be enough to reconstruct private infrastructure.
