# Pattern: gateway health and exposure audit

## Based on real work

Techie performed read-only OpenClaw/gateway security checks: loopback binding, token auth, Discord connectivity, SSH exposure, firewall state, update timers, disk encryption state, and OpenClaw security audit warnings.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- gateway status
- channel status
- exposure audit
- firewall/SSH review
- OpenClaw security audit
- healthcheck

## Safe handoff context

Include:

- scope of audit
- read-only expectation
- specific systems to inspect
- reporting format

Exclude:

- raw tokens
- private IP/account details unless necessary and approved
- exploit instructions beyond defensive remediation

## Checklist

1. Confirm read-only scope.
2. Inspect OpenClaw status and channel status.
3. Inspect gateway binding/auth posture.
4. Inspect host exposure basics.
5. Summarize warnings by severity.
6. Recommend reversible next actions.
