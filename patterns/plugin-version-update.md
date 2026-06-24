# Pattern: plugin version update

## Based on real work

Techie pinned and updated an OpenClaw plugin, restarted the gateway, verified loaded and recorded plugin versions, and noted a remaining metadata warning separately from actual version drift.

## Route

- owner: `techie`
- category: `infra`
- ownership: `handoff`

## Signals

Route here when a request mentions:

- plugin update
- pinned install
- version drift
- inspect plugin
- restart gateway after plugin change

## Safe handoff context

Include:

- plugin name
- target version
- restart requirement
- verification command/output shape

Exclude:

- package registry tokens
- unrelated plugin config
- private install metadata dumps

## Checklist

1. Inspect current loaded/recorded version.
2. Install the explicitly requested/pinned version.
3. Restart/reload if required.
4. Verify loaded and recorded versions.
5. Separate real version drift from legacy metadata warnings.
