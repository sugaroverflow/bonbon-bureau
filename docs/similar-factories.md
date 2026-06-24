# Similar factories and orchestration patterns

Bonbon Bureau is not trying to become a generic agent framework. It is a small, public-safe control plane for a household of named OpenClaw agents. Still, nearby projects and patterns are useful guardrails for the phased plan.

## Nearby patterns worth borrowing

### LangChain / LangGraph multi-agent patterns

LangChain's multi-agent docs frame the core choice as context engineering: decide which agent sees which context, and avoid multi-agent complexity when one agent with tools is enough. Its pattern list maps well to Bonbon Bureau vocabulary:

- **subagents**: Miette stays in charge and calls specialists as bounded helpers
- **handoffs**: a specialist owns the next response or task thread
- **skills**: a single agent loads domain procedures on demand
- **router**: classify a request and send it to one or more specialists
- **custom workflow**: use LangGraph when deterministic state and checkpoints matter

Bonbon takeaway: keep Phase 3 rule-based first, then graduate only the pieces that need state, checkpoints, or explicit routing graphs.

Source: <https://docs.langchain.com/oss/python/langchain/multi-agent>

### OpenAI Agents SDK orchestration

OpenAI's agent orchestration guidance makes the ownership distinction explicit:

- use **handoffs** when a specialist should take over the work
- use **agents-as-tools** when the manager should keep final-answer ownership
- give each specialist a narrow job and split only when different instructions, tools, or policy are needed

The SDK's tracing model also highlights what production-ish Bureau runs should record: agent spans, tool calls, handoffs, guardrails, and custom events.

Bonbon takeaway: add an ownership field and trace/status vocabulary before making the dispatcher more autonomous.

Sources:

- <https://developers.openai.com/api/docs/guides/agents/orchestration>
- <https://openai.github.io/openai-agents-python/tracing/>

### Microsoft AI agent orchestration patterns

Microsoft's Azure Architecture Center summarizes common multi-agent coordination patterns: sequential, concurrent, group chat, handoff, and manager-led/magentic orchestration. It also stresses starting with the lowest complexity that works, because multi-agent systems add coordination overhead, latency, cost, and failure modes.

Bonbon takeaway: every phase should have an exit criterion proving the extra coordination earned its keep.

Source: <https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns>

### Microsoft Agent Framework

Microsoft Agent Framework separates individual agents from graph-based workflows. Its overview positions workflows as the right tool when multiple agents/functions must coordinate, steps are well-defined, checkpointing matters, or humans need to stay in the loop.

Bonbon takeaway: Miette should remain a named agent, while repeatable Bureau procedures can become workflow-shaped artifacts around her.

Source: <https://learn.microsoft.com/en-us/agent-framework/overview/>

### CrewAI crews

CrewAI's crew abstraction is useful as a vocabulary reference: a crew combines agents, tasks, process flow, manager agent/LLM, memory, callbacks, rate limits, and output logging.

Bonbon takeaway: the Bureau roster should stay more personal and OpenClaw-native than a generic crew, but task lists, process labels, callbacks/status updates, and manager-vs-worker language are worth mirroring where they clarify the plan.

Source: <https://docs.crewai.com/concepts/crews>

## Design pressure from the comparison

1. **Do less agent orchestration than the name suggests.** Start with docs, schemas, fixtures, and manual routing. Add autonomous routing only where repetition proves it useful.
2. **Keep ownership visible.** Every route should say whether Miette keeps ownership, hands off, or asks a bounded specialist/tool for help.
3. **Separate runtime from workflow.** OpenClaw owns identities, workspaces, sessions, tools, and bindings. Bonbon Bureau owns conventions, schemas, runbooks, status, and safe handoff packets.
4. **Make observability boring early.** Even before LangGraph, log/record route decisions, handoff packets, status changes, blockers, and escalation points in public-safe terms.
5. **Human-in-the-loop is a feature, not a delay.** Escalation and approval boundaries should be first-class, especially around credentials, config, external writes, and private data.
6. **Candyland remains later.** The comparison confirms that worker factories are tempting scope creep. Bonbon Bureau should first become a good control plane for existing named agents.
