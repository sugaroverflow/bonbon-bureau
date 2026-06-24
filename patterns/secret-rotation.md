# Pattern: application secret rotation

## Based on real work

Techie rotated an application database credential, updated dependent runtime environments, redeployed the app, smoke-tested a public route, and removed temporary secret files.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- rotate a password/token/key
- database credential change
- update deployment environment variables
- redeploy after secret change
- smoke-check after credential rotation

## Safe handoff context

Include:

- affected service/app
- credential purpose, not value
- environments to update
- smoke test target
- rollback concern

Exclude:

- raw secret values
- temporary secret file contents
- provider console screenshots containing secrets

## Checklist

1. Identify all consumers of the secret.
2. Rotate the secret at the source.
3. Update each runtime/deployment environment.
4. Redeploy or restart affected services.
5. Smoke-test a harmless endpoint or action.
6. Remove temporary files.
7. Report verification without exposing values.
