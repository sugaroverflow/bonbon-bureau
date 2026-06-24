# Public-safe agent files

Date: 2026-06-24

## Decision

Bonbon Bureau will include public-safe copies of the agents' workspace-style files (`IDENTITY.md`, `SOUL.md`, `AGENTS.md`, and `USER.md`) for Lotus, Techie, Glyphie, and Miette.

## Rationale

The repo is intended to be public and conference-talk-friendly. Agent files make the Bureau concrete and demo-able, but raw private workspace files can contain local paths, private context, channel/account IDs, and operational details that do not belong in GitHub.

## Rule

Copy the shape and durable behavior, not private runtime state.

Public copies should preserve personality, responsibilities, boundaries, routing logic, and safe operating rules. They should remove secrets, private identifiers, personal details, surprise/project-sensitive notes, and local machine paths.
