# Pattern: secret-scanning guardrails

## Based on real work

Techie prepared gitleaks-based guardrails: a GitHub Action and local pre-commit hook that run redacted secret detection and fail safely when tooling is missing.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- gitleaks
- pre-commit secret scan
- secret hygiene in a repo
- GitHub Action for secret scanning
- redact findings

## Safe handoff context

Include:

- repository name
- desired enforcement level
- CI vs local hook preference
- review/merge owner

Exclude:

- raw detected secret values
- full unredacted scanner output

## Checklist

1. Inspect existing CI/hooks.
2. Add scanner config or workflow.
3. Make local hooks fail safe and redact output.
4. Run scanner in redacted mode.
5. Leave product-owned changes for product review when appropriate.
