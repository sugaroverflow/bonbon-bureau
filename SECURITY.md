# Security

Bonbon Bureau is intended to be public and talk-friendly. Treat it as a public artifact by default.

## Do not commit

- API keys, OAuth tokens, passwords, session cookies, private keys
- raw chat/session transcripts
- private channel IDs, DMs, emails, phone numbers, or addresses
- personal calendar/email details
- production hostnames, IPs, or internal URLs unless deliberately public
- `.env` files with real values
- screenshots containing private data

## Credential pattern

Use an external credential source such as 1Password, env providers, or key references. Verify credentials by using them safely; do not print them into logs or docs.

## Public-safe docs

Prefer:

- generic examples
- fake IDs
- role descriptions
- diagrams without private routes
- runbooks that describe process without secrets

## If a secret is committed

1. Revoke/rotate it immediately.
2. Remove it from the repo history if needed.
3. Add a regression note to prevent repeats.
