# Recurring task patterns

These patterns are distilled from real tasks performed by agents on this server, then redacted into public-safe form.

They are not synthetic sample stories. They are the workflows Bonbon Bureau should learn to route cleanly.

## Pattern set

- `envprov-keyref-migration.md` — move a credential reference to envprov/keyRef and verify without printing the value.
- `secret-rotation.md` — rotate an application/database secret and smoke-test the dependent app.
- `discord-agent-account.md` — configure a separate Discord account/channel binding for an agent.
- `gateway-health-audit.md` — inspect gateway/channel/security status and summarize findings.
- `plugin-version-update.md` — pin/update a plugin, restart safely, and verify loaded version.
- `secret-scanning-guardrails.md` — add or review gitleaks/pre-commit guardrails.
- `monitoring-agent-setup.md` — set up a monitoring/research agent with scoped posting and source-check duties.

## Source rule

Keep these public-safe:

- use placeholder IDs like `<guild-id>` and `<channel-id>`
- use fake credential names like `EXAMPLE_API_KEY`
- describe verification behavior, not secret values
- do not copy raw transcripts, local paths, or private config
