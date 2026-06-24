# Runbook: install Miette as a local OpenClaw agent

This runbook turns Bonbon Bureau's public-safe Miette files into a private local OpenClaw workspace.

It is intentionally conservative: inspect first, copy files second, and do not edit live OpenClaw config in this repo.

## Inputs

- source: `miette/`
- target agent id: `miette`
- target workspace: OpenClaw's active workspace root plus `/miette/`, if using the multi-agent workspace layout

## Safety rules

- Do not commit private workspace files to this public repo.
- Do not copy secrets, sessions, credentials, or auth profiles.
- Do not overwrite an existing Miette workspace without reviewing its contents first.
- Keep `~/.openclaw/openclaw.json`, `~/.openclaw/agents/*`, credentials, sessions, and auth profiles out of Git.

## Standard workspace files

OpenClaw workspace docs describe these common files:

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- optional `memory/YYYY-MM-DD.md`
- optional `MEMORY.md` for private long-term memory

Bonbon Bureau currently provides public-safe Miette files:

- `miette/README.md`
- `miette/IDENTITY.md`
- `miette/SOUL.md`
- `miette/AGENTS.md`
- `miette/USER.md`
- `miette/ROUTING.md`
- `miette/ESCALATION.md`

## Procedure

1. Inspect current local state.

   ```bash
   find ~/.openclaw/workspace -maxdepth 3 -type d -name miette -print
   find ~/.openclaw/agents -maxdepth 2 -type d -name miette -print
   ```

2. If no Miette workspace exists, create one.

   ```bash
   mkdir -p ~/.openclaw/workspace/main/miette/memory
   ```

3. Copy only public-safe agent files into the private workspace.

   ```bash
   cp miette/AGENTS.md ~/.openclaw/workspace/main/miette/AGENTS.md
   cp miette/SOUL.md ~/.openclaw/workspace/main/miette/SOUL.md
   cp miette/USER.md ~/.openclaw/workspace/main/miette/USER.md
   cp miette/IDENTITY.md ~/.openclaw/workspace/main/miette/IDENTITY.md
   cp miette/ROUTING.md ~/.openclaw/workspace/main/miette/ROUTING.md
   cp miette/ESCALATION.md ~/.openclaw/workspace/main/miette/ESCALATION.md
   ```

4. Add local-only files if needed.

   ```bash
   cat > ~/.openclaw/workspace/main/miette/TOOLS.md <<'LOCAL'
   # TOOLS.md - Local Notes

   Keep Miette-specific local tool notes here. Do not commit secrets.
   LOCAL

   cat > ~/.openclaw/workspace/main/miette/HEARTBEAT.md <<'LOCAL'
   <!-- Keep empty unless Miette needs scheduled heartbeat work. -->
   LOCAL
   ```

5. Register or bind the agent through the normal OpenClaw configuration flow for the deployment.

   Keep config changes private. If adding bindings, inspect existing config first and preserve existing accounts/routes.

6. Verify by starting a private Miette session and asking for a routing-only task.

   Expected behavior:

   - Miette routes product work to Lotus.
   - Miette routes infra/secrets/channel work to Techie.
   - Miette routes monitoring/source-checking work to Glyphie.
   - Miette keeps ambiguous coordination work.

## Rollback

If the workspace was newly created and has no private state yet, move it aside rather than deleting it:

```bash
mv ~/.openclaw/workspace/main/miette ~/.openclaw/workspace/main/miette.disabled.$(date +%Y%m%d%H%M%S)
```

If config was changed, revert using the deployment's normal config history/backup process.
