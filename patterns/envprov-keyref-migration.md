# Pattern: envprov/keyRef migration

## Based on real work

Techie migrated an OpenClaw auth profile from an inline/plain setting to an `envprov`/keyRef-style secret reference, then verified the secret audit outcome without printing the value.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- envprov
- keyRef / SecretRef
- auth profile migration
- plaintext secret cleanup
- secret audit findings

## Safe handoff context

Include:

- config field to migrate
- desired environment variable or keyRef name, if safe
- verification command or expected behavior
- rollback concern, if any

Exclude:

- raw secret values
- full private config dumps
- shell history with secrets

## Checklist

1. Inspect current config without printing secret values.
2. Confirm the target env var/keyRef name exists or is expected.
3. Patch config to reference the provider/keyRef.
4. Restart/reload only if required.
5. Verify by audit or harmless use.
6. Record outcome and any expected residual warnings.
