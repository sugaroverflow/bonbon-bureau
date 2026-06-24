# Fixtures

`fixtures/tasks/` contains public-safe routing fixtures derived from real repeated work performed by agents on this server.

Each fixture should:

- use `TASK_SCHEMA.yaml` shape
- point to a `patterns/*.md` source pattern
- use placeholder/public-safe context only
- avoid raw local paths, private IDs, secrets, or transcript dumps
- route consistently through `scripts/check.py`

Run:

```bash
python3 scripts/check.py
python3 scripts/route_fixture.py fixtures/tasks/secret-rotation.yaml
```
