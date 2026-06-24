# Bonbon Bureau helper commands

status:
    git status --short

route TASK:
    python3 langgraph-router/router.py "{{TASK}}"

check:
    python3 -m py_compile langgraph-router/router.py
    python3 langgraph-router/router.py "rotate a credential safely" >/tmp/bonbon-route-check.json
    python3 -m json.tool /tmp/bonbon-route-check.json >/dev/null
