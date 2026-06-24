# Agent PR conventions

Bonbon Bureau agents may help prepare pull requests across different projects and repositories. Attribution should be visible without requiring separate bot accounts or noisy commit trailers.

## Convention

### PR title

Add the preparing agent at the end of the PR title:

```text
Add secret safety runbook [Techie]
Draft product copy examples [Lotus]
Add source monitor notes [Glyphie]
```

### PR labels

Use labels to make agent involvement searchable:

```text
bonbon-factory
agent:agentName
```

Other examples:

```text
bonbon-factory
agent:techie
agent:lotus
agent:glyphie
agent:miette
```

### PR description

Include a short Bonbon Bureau block:

```md
## Bonbon Bureau

Prepared by: Techie
Routed by: Miette
Mode: agent-assisted
Human owner: @sugaroverflow
Human review required before merge: yes
```

Use `agent-authored` instead of `agent-assisted` when the agent prepared most of the diff.

## Not required

- No separate GitHub bot account is required.
- No commit trailer is required.
- No agent should merge on its own unless a repository explicitly opts into that workflow.

## Why

This keeps attribution public, cute, and searchable while avoiding extra credential management and pretending agents are separate GitHub users.
