# Runbook: route a task

Purpose: make routing boring and inspectable.

## Steps

1. Summarize the task in one public-safe sentence.
2. Classify the category.
3. Decide ownership:
   - **handoff** if the specialist should own the next response
   - **bounded_help** if Operator should synthesize the final response
4. Create a handoff packet using `TASK_SCHEMA.yaml`.
5. Send only the minimum context needed.
6. Track status: routed → in_progress → waiting/blocked/done.
7. Escalate if blocked or owner is ambiguous.

## Default routes

- product / taste / building → Lotus
- infra / credentials / safety → Techie
- monitoring / source checks → Glyphie
- ambiguous / cross-domain → Operator
