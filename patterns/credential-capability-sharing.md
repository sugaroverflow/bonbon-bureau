# Pattern: credential-backed capability sharing

## Source

Recurring need: one agent needs another agent's credential-backed capability, but raw secrets should not move through chat, docs, or public repos.

## Public-safe shape

- name the capability
- name owner and consumer agents
- describe service/action/target scope with placeholders
- prefer delegation over shared credentials
- verify by harmless use
- document revocation before granting access

## Routing

Owner: Techie

Category: infra

Reason: credential boundaries, keyRefs, channel/account access, and revocation are infrastructure/security work.

## Fixture ideas

- "let Miette request status posts without seeing the Discord token"
- "give Glyphie read-only access to a monitored source"
- "allow Lotus to trigger a deploy status check through Techie"
