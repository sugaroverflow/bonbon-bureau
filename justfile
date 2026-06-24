# Bonbon Bureau helper commands

status:
    git status --short

route TASK:
    python3 langgraph-router/router.py "{{TASK}}"

route-fixture FIXTURE:
    python3 scripts/route_fixture.py "{{FIXTURE}}"

check:
    python3 scripts/check.py
