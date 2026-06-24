# Heartbeat operations

Public-safe notes for recurring OpenClaw agent heartbeat setup.

## Why heartbeats exist

Heartbeats are periodic agent turns for lightweight progress, monitoring, and follow-up. They should be boring: do useful work when there is something real to do, otherwise stay quiet.

Use heartbeat when:

- the cadence can drift a little;
- the agent benefits from its own workspace context;
- the update should route to the current/last chat surface;
- the work is small enough to finish inside a normal agent turn.

Use cron/task flow instead when exact timing, isolation, retries, or long-running work matters.

## Current public-safe setup

| Agent | Purpose | Cadence | Visibility rule |
| --- | --- | --- | --- |
| Lotus | Product/build progress | 30 minutes | Post shipped work, cursor, and assumptions; otherwise `HEARTBEAT_OK`. |
| Glyphie | Monitoring/research progress | 30 minutes | Post concise source/feed updates and assumptions; otherwise `HEARTBEAT_OK`. |
| Techie | Infra operations watch | 2 hours during daytime | Post only useful infra/security/channel updates; otherwise `HEARTBEAT_OK`. |

Private deployment details such as channel IDs, account IDs, tokens, and exact local config paths stay out of this repo.

## Recommended per-agent config shape

```json5
{
  "heartbeat": {
    "every": "30m",
    "target": "last",
    "lightContext": true,
    "isolatedSession": true,
    "skipWhenBusy": true,
    "prompt": "Read HEARTBEAT.md in the agent workspace. Follow it strictly. Post useful updates and assumptions to the configured chat target; if nothing needs attention, reply HEARTBEAT_OK."
  }
}
```

Notes:

- `target: "last"` is the safest public template because the real channel may be Discord, Slack, or another configured chat surface.
- For explicit channel delivery in a private deployment, set `target`, `to`, and `accountId` there, not in this public repo.
- `lightContext` + `isolatedSession` keeps recurring token cost down and prevents old chat history from steering scheduled work.
- `skipWhenBusy` avoids piling heartbeat work on top of active agent tasks.

## HEARTBEAT.md contract

Each active heartbeat agent should have a tiny `HEARTBEAT.md` in its private workspace. Keep it small enough for cheap recurring runs.

Required behavior:

1. Read the heartbeat checklist.
2. Do one small, safe unit of due work if there is one.
3. Post a visible update only when something meaningful changed or a human decision is needed.
4. Include assumptions made during the turn.
5. Reply exactly `HEARTBEAT_OK` when there is nothing useful to say.

## Restore checklist

Use this when moving config between machines or after config cleanup:

1. Inspect current agent list and heartbeat state.
2. Confirm each target agent has a non-empty `HEARTBEAT.md` if API calls should run.
3. Apply per-agent heartbeat blocks; avoid replacing the whole config file.
4. Validate OpenClaw config.
5. Restart/reload the gateway if the deployment requires it.
6. Verify status shows the expected heartbeat cadences.
7. Trigger or observe one heartbeat event before declaring success.

## Public-safety rules

Do not commit:

- token values or secret provider payloads;
- numeric channel/account/user IDs;
- raw `openclaw.json` from a private host;
- private workspace memory or session transcripts;
- surprise-sensitive project details.

Commit instead:

- cadence and behavior templates;
- public-safe responsibilities;
- runbooks and validation steps;
- sanitized examples.
