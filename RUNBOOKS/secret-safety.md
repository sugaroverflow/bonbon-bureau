# Runbook: secret safety

Purpose: keep Bonbon Bureau safe while remaining public.

## Rules

- Never commit secrets.
- Never paste secrets into issues, docs, commits, or transcripts.
- Prefer key references over raw values.
- Verify secrets by using them, not printing them.
- Redact logs before sharing.

## Public examples

Use placeholders like:

```text
op://OpenClaw Agents/Example/api_key
${EXAMPLE_API_KEY}
<redacted>
```

Never use a real item path if the item name itself is sensitive.
