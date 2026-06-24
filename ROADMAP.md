# Roadmap

Bonbon Bureau should stay small, public-safe, and grounded in real repeated work. This roadmap tracks the multi-phase plan without pulling Candyland into scope too early.

## Planning inputs

The phased plan is informed by nearby agent-factory/control-plane patterns, summarized in [docs/similar-factories.md](docs/similar-factories.md):

- start with the lowest orchestration complexity that works
- keep context and ownership boundaries explicit
- distinguish manager-keeps-control calls from true handoffs
- add workflow/checkpoint machinery only after route/status behavior is proven
- treat human review and public-safe observability as core features

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
- `docs/similar-factories.md`

Exit criteria:

- Someone can read the repo and understand Bonbon Bureau in five minutes.
- Public/private boundaries are clear.
- Agent responsibilities are legible.
- Similar-factory research has been distilled into Bureau-specific guardrails, not copied as generic framework sprawl.

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
- Miette can distinguish:
  - **handoff**: a specialist should own the next response or task thread
  - **bounded assist**: Miette stays responsible and asks a specialist/tool for help
  - **clarify/escalate**: Fatima or a policy boundary must decide

## Phase 3: Rule-based routing spike

Goal: prove the dispatcher shape before adding production complexity.

Artifacts:

- `langgraph-router/router.py`
- `docs/langgraph-routing-spike.md`
- `scripts/route_fixture.py`
- `scripts/check.py`
- `.github/workflows/check.yml`

Exit criteria:

- Input task/request becomes route + rationale + handoff packet.
- No external writes.
- Router output validates as JSON.
- Fixture validation runs without dependency installation.
- Rule-based version works before framework version.
- Router output includes explicit ownership mode: handoff, bounded assist, clarify, or escalate.

## Phase 4: OpenClaw integration plan

Goal: map the architecture to real OpenClaw mechanics.

Artifacts:

- `docs/openclaw-integration.md`
- `RUNBOOKS/install-miette.md`
- `RUNBOOKS/sync-agent-files.md`

Exit criteria:

- Workspace boundaries are documented.
- Session/binding strategy is documented.
- Required tools and permissions are documented.
- Private config remains outside the repo.
- The plan clearly says OpenClaw owns runtime concerns: identities, workspaces, sessions, tools, bindings, and private state.

## Phase 5: Secrets and credential-sharing pattern

Goal: make the safe path the easy path.

Artifacts:

- `docs/secrets-pattern.md`
- `docs/credential-sharing.md`
- `RUNBOOKS/secret-safety.md`
- `RUNBOOKS/share-credential-capability.md`
- `patterns/credential-capability-sharing.md`
- `fixtures/tasks/credential-capability-sharing.yaml`

Exit criteria:

- No secrets in Git.
- Credentials are referenced through 1Password/envprov/keyRefs or environment indirection.
- Verification happens by use, not by printing values.
- Credential-sharing tasks require explicit capability boundaries, owner, approver, and rollback notes.
- Credential/config tasks default to human review before live changes.

## Phase 6: Real task pattern library

Goal: seed routing from tasks agents on this server have actually performed.

Artifacts:

- `patterns/`
- `fixtures/tasks/`
- `fixtures/README.md`
- `docs/router-validation.md`

Exit criteria:

- Repetitive tasks are described as public-safe patterns.
- Router fixtures are based on those patterns, not synthetic sample tasks.
- Fixtures cover infra, monitoring, product/infra handoff, credential, and channel-routing cases.
- Private IDs, local paths, secrets, and raw transcripts are excluded.
- Each pattern states when Miette should keep ownership versus hand off.

## Phase 7: Status ledger and observability

Goal: make Bureau work inspectable before making it more autonomous.

Why this phase exists:

Comparable frameworks emphasize tracing, callbacks, status, and checkpoints. Bonbon Bureau should capture those benefits in a public-safe, tiny form before adopting heavier runtime machinery.

Artifacts:

- `STATUS_SCHEMA.yaml`
- `RUNBOOKS/update-status.md`
- `docs/status-ledger.md`
- `fixtures/status/`

Exit criteria:

- A task can move through intake, routed, active, blocked, escalated, done, and archived states.
- Status entries record route decision, owner, ownership mode, blocker, escalation reason, and next action.
- Status records are safe to share publicly by default.
- The status shape can later map to OpenClaw sessions, GitHub issues/PRs, or a LangGraph checkpoint without redesign.

## Phase 8: LangGraph/workflow dispatcher spike

Goal: test whether a workflow layer earns its keep after rules, fixtures, and status are stable.

Artifacts:

- `langgraph-router/graph_router.py` or equivalent spike
- `docs/workflow-dispatcher-spike.md`
- comparison notes against the rule-based router

Exit criteria:

- The workflow reproduces existing fixture outcomes.
- The workflow adds at least one useful capability the rule router lacks: checkpointing, retryable state, multi-step clarification, fan-out/fan-in research, or structured human review.
- It preserves Miette's named-agent identity instead of creating a second identity system.
- It remains read-only by default; external writes require explicit approval.
- If it does not beat the simple router, the repo records that decision and keeps the simpler path.

## Phase 9: Human-review and external-write gates

Goal: make risky boundaries boring and explicit.

Artifacts:

- `RUNBOOKS/external-write-gates.md`
- `RUNBOOKS/human-review.md`
- `DECISIONS/` record for approval boundaries

Exit criteria:

- The plan distinguishes internal reversible work from external/destructive/privacy-sensitive work.
- Tasks involving secrets, production config, public posts, messages, pushes, or scheduler changes name the review gate before execution.
- Handoff packets include what was verified, what would change, rollback notes, and the exact approval needed where applicable.

## Phase 10: Candyland/Jellybean Junction review

Goal: decide whether the local worker-factory idea is still worth pursuing.

Artifacts:

- `docs/candyland-readiness-review.md`
- `docs/jellybean-junction-options.md`

Exit criteria:

- Bonbon Bureau can reliably route and track existing named-agent work first.
- At least three real task classes need local worker/factory execution rather than named-agent handoff.
- The connector boundary is clear enough that Candyland cannot absorb secrets, private memory, or live config by accident.
- If not ready, Candyland stays in the Idea Pantry.
