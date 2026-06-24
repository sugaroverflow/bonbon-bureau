# Runbook: restore agent heartbeats

Use this when moving OpenClaw agents or after config cleanup accidentally disables recurring heartbeats.

## Inputs

- Agent IDs that should heartbeat.
- Desired cadence per agent.
- Public-safe behavior for each agent's `HEARTBEAT.md`.
- Private chat routing details, if explicit delivery is required.

## Procedure

1. Inspect current state before editing:

   ```bash
   openclaw status
   openclaw config get agents.list
   ```

2. Confirm whether any agent already has a heartbeat block. In OpenClaw, if any `agents.list[]` entry has a heartbeat block, only agents with heartbeat blocks run heartbeats.

3. Update only the per-agent heartbeat paths. Do not rewrite the whole config file.

   Public-safe template:

   ```json5
   {
     "every": "30m",
     "target": "last",
     "lightContext": true,
     "isolatedSession": true,
     "skipWhenBusy": true,
     "prompt": "Read HEARTBEAT.md in the agent workspace. Follow it strictly. Post useful updates and assumptions to the configured chat target; if nothing needs attention, reply HEARTBEAT_OK."
   }
   ```

4. Make sure the agent workspace has a non-empty `HEARTBEAT.md` when heartbeat calls should run. A comments-only heartbeat file intentionally suppresses scheduled API calls.

5. Validate and apply:

   ```bash
   openclaw config validate
   openclaw status
   ```

6. If status still shows old cadence after a config write, restart/reload the gateway using the deployment's normal OpenClaw restart path.

7. Verify the status row shows the intended cadence, for example:

   ```text
   Heartbeat: 30m (main), 30m (glyphie), 2h (techie)
   ```

8. Observe or trigger one heartbeat and check that quiet cycles produce `HEARTBEAT_OK` rather than noisy filler.

## 2026-06-24 restoration note

A config move left Lotus and Glyphie heartbeats disabled. Techie restored:

- Lotus: 30 minute cadence, visible shipped-work/cursor/assumption updates.
- Glyphie: 30 minute cadence, visible monitoring/feed/assumption updates.
- Techie: kept existing infra cadence separate.

The live deployment used private routing state; this repo records only the reusable public-safe pattern.
