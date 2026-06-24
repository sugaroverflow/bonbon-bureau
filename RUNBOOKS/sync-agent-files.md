# Runbook: sync public-safe agent files

Use this when Bonbon Bureau's public agent files should be refreshed from private workspace files.

## Rule

Summarize and redact. Do not copy raw private workspace files directly into this public repo.

## Procedure

1. Inspect the private source files.
2. Identify durable public-safe content:
   - name
   - role
   - vibe
   - responsibilities
   - routing boundaries
   - safe operating rules
3. Remove private content:
   - secrets or tokens
   - account/channel IDs
   - local machine paths
   - private personal details
   - surprise/project-sensitive motives
   - raw sessions or memory dumps
4. Update the matching public file in the agent directory.
5. Run checks:

   ```bash
   python3 scripts/check.py
   grep -RInE '[0-9]{9,}|TOKEN|SECRET|/home/|/Users/' lotus techie glyphie miette docs RUNBOOKS patterns fixtures || true
   ```

6. Commit with a message that makes the public-safe nature explicit.
