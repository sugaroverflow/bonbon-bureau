# Secrets pattern

Bonbon Bureau is public. Secrets live elsewhere.

## Rules

- No secrets in Git.
- No raw credential values in docs, issues, PRs, commits, or examples.
- Prefer 1Password, env providers, key references, or environment variables.
- Verify credentials by using them safely, not by printing them.
- Keep private OpenClaw config outside this repo.

## Public-safe example

```text
op://OpenClaw Agents/Example/api_key
${EXAMPLE_API_KEY}
<redacted>
```

Use fake item names unless the real item name is intentionally public.

## Recommended flow

1. Document the required capability, not the secret value.
2. Store the credential in the private credential manager.
3. Reference it through a keyRef/env var in private config.
4. Add a runbook explaining how to verify the integration without exposing the value.
5. If a secret is exposed, rotate it first, then clean up docs/history.

## Verification examples

Good:

```text
Run a harmless API call and confirm HTTP 200.
```

Bad:

```text
Print the token and compare it in chat.
```
