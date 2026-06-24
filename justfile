# Bonbon Bureau helper commands

status:
    git status --short

route TASK:
    python3 langgraph-router/router.py "{{TASK}}"

check:
    python3 -m py_compile langgraph-router/router.py
    python3 langgraph-router/router.py "rotate a credential safely" >/tmp/bonbon-route-check.json
    python3 -m json.tool /tmp/bonbon-route-check.json >/dev/null
    python3 langgraph-router/router.py "configure a Discord account for Glyphie" | python3 -m json.tool >/dev/null
    python3 langgraph-router/router.py "check whether monitored sources changed" | python3 -m json.tool >/dev/null
    test -d patterns
    test -d fixtures/tasks
