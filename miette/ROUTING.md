# Miette routing rules

## Ownership modes

### Handoff

Use when the specialist should own the next response or implementation.

Examples:

- Techie owns an infra/safety change.
- Lotus owns product taste or writing direction.
- Glyphie owns monitoring/source-checking work.

### Bounded help

Use when Miette should keep ownership and ask a specialist for a contained answer.

Examples:

- Miette needs a one-paragraph summary from Glyphie.
- Miette needs Techie to sanity-check a public/private boundary.

## Routing table

| Signal | Route |
| --- | --- |
| product, UX, copy, taste, strategy | Lotus |
| secrets, credentials, OpenClaw admin, infra, gateway | Techie |
| monitoring, source checks, alerts, recurring signals | Glyphie |
| unclear owner, cross-domain, blocked | Miette |

## Tie-breakers

1. Safety-sensitive tasks go to Techie.
2. Taste-sensitive tasks go to Lotus.
3. Ongoing watch/check tasks go to Glyphie.
4. Multi-domain tasks stay with Miette until split into handoffs.
