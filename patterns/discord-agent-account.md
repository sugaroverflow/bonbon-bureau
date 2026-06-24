# Pattern: Discord agent account setup

## Based on real work

Techie configured separate Discord accounts for agents, added envprov allowlist entries, scoped guild/channel access, preserved the default account, restarted the gateway, and verified connectivity.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- Discord bot/account setup
- channel binding
- requireMention behavior
- agent-specific Discord routing
- gateway restart after channel config

## Safe handoff context

Include:

- agent id
- intended channel purpose
- whether mentions are required
- whether DM access is allowed
- verification expectation

Exclude:

- bot token value
- private channel IDs unless intentionally public-safe placeholders
- raw gateway config containing secrets

## Checklist

1. Confirm the agent and desired channel scope.
2. Add/verify the credential reference through envprov/keyRef.
3. Configure the account and binding without clobbering existing accounts.
4. Preserve default account behavior.
5. Restart/reload gateway if required.
6. Verify channel status/probe.
7. Send only an approved test message if external posting is allowed.
