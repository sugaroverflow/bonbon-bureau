# Miette escalation policy

Escalate to Fatima when:

- a task would take external action on Fatima's behalf
- a task needs credentials, permissions, or account changes
- a routing decision is ambiguous and could leak private context
- a specialist reports a blocker that needs human judgment
- a PR is ready for merge or needs human review

Do not escalate when:

- a safe internal lookup can resolve the question
- the task can be routed with public-safe context
- a reversible documentation update can be prepared as a PR

When escalating, include:

- what happened
- current owner
- blocker or decision needed
- recommended next action
