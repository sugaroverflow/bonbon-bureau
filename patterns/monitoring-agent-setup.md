# Pattern: monitoring agent setup

## Based on real work

Glyphie was configured as a monitoring/research agent with scoped Discord posting and source-check duties. Techie owned the infra/channel setup; Glyphie owns the ongoing reading and summaries.

## Route

- initial setup owner: `techie`
- ongoing work owner: `glyphie`
- category: `monitoring`
- ownership: `handoff`

## Signals

Route setup to Techie when a request mentions:

- create/configure monitoring agent account
- Discord/channel/gateway setup for the monitoring agent
- credential reference for the monitoring agent

Route ongoing work to Glyphie when a request mentions:

- watch a source
- check whether anything changed
- summarize a recurring signal
- cite sources

## Safe handoff context

Include:

- source list or channel purpose
- posting cadence
- whether mention is required
- citation expectations

Exclude:

- bot token values
- private surprise/project motives
- raw private notes

## Checklist

1. Split setup from ongoing monitoring.
2. Route account/channel setup to Techie.
3. Route source-checking duties to Glyphie.
4. Require citations for substantive findings.
5. Summarize status without dumping raw transcripts.
