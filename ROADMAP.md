# Roadmap

Bonbon Bureau should stay small, public-safe, and grounded in real repeated work. This roadmap tracks the multi-phase plan without pulling Candyland into scope too early.

## Phase 1: Bureau scaffold

Goal: make the concept crisp and public-talk-friendly.

Status: in progress

Artifacts:

- `README.md`
- `ARCHITECTURE.md`
- `ROSTER.yaml`
- `TASK_SCHEMA.yaml`
- `RUNBOOKS/`
- `DECISIONS/`
- `docs/agent-pr-conventions.md`
- `docs/idea-pantry.md`

Exit criteria:

- Someone can read the repo and understand Bonbon Bureau in five minutes.
- Public/private boundaries are clear.
- Agent responsibilities are legible.

## Phase 2: Miette workspace

Goal: define the Operator agent as a real named collaborator.

Artifacts:

- `miette/README.md`
- `miette/AGENTS.md`
- `miette/IDENTITY.md`
- `miette/ROUTING.md`
- `miette/ESCALATION.md`

Exit criteria:

- Miette knows what to route, what to keep, and when to escalate.
- Miette has an explicit “do not replace specialists” rule.
- Miette can prepare handoff packets using `TASK_SCHEMA.yaml`.

## Phase 3: LangGraph routing spike

Goal: prove the dispatcher shape before adding production complexity.

Artifacts:

- `langgraph-router/router.py`
- `docs/langgraph-routing-spike.md`

Exit criteria:

- Input task/request becomes route + rationale + handoff packet.
- No external writes.
- Router output validates as JSON.
- Rule-based version works before framework version.

## Phase 4: OpenClaw integration plan

Goal: map the architecture to real OpenClaw mechanics.

Artifacts:

- `docs/openclaw-integration.md`

Exit criteria:

- Workspace boundaries are documented.
- Session/binding strategy is documented.
- Required tools and permissions are documented.
- Private config remains outside the repo.

## Phase 5: Secrets pattern

Goal: make the safe path the easy path.

Artifacts:

- `docs/secrets-pattern.md`
- `RUNBOOKS/secret-safety.md`

Exit criteria:

- No secrets in Git.
- Credentials are referenced through 1Password/envprov/keyRefs or environment indirection.
- Verification happens by use, not by printing values.

## Phase 6: Real task pattern library

Goal: seed routing from tasks agents on this server have actually performed.

Artifacts:

- `patterns/`
- `fixtures/tasks/`

Exit criteria:

- Repetitive tasks are described as public-safe patterns.
- Router fixtures are based on those patterns, not synthetic sample tasks.
- Fixtures cover infra, monitoring, and product/infra handoff cases.
- Private IDs, local paths, secrets, and raw transcripts are excluded.
