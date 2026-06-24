# Runbook: share a credential-backed capability

Use this when one Bonbon Bureau agent needs access to a credential-backed action.

This runbook is safe to work through as a design exercise without changing live OpenClaw config. Stop before the private-config steps if agents are busy or a restart would be disruptive.

## Inputs

- requesting agent
- owning agent
- capability name
- service/action/target scope
- verification method
- revocation owner

## Procedure

1. Decide whether sharing is actually needed.

   Prefer delegation: the requesting agent asks the owning specialist to perform the action.

2. Define the capability in public-safe terms.

   ```yaml
   capability: example-status-post
   owner: techie
   consumer: miette
   service: example-service
   action: post-status
   target: <approved-target>
   verification: harmless-use
   revocation_owner: techie
   ```

3. Choose the safest access model.

   - best: owning agent keeps credential and performs action
   - good: requesting agent gets a narrow keyRef/env var
   - risky: multiple agents share one broad upstream credential

4. Document the private-config change that would be needed, but do not apply it yet.

   ```text
   consumer agent: miette
   config location: private OpenClaw config
   key reference: envprov:EXAMPLE_CAPABILITY_TOKEN
   restart required: yes/no/unknown
   ```

5. Define verification without exposure.

   Examples:

   - send an approved test message
   - make a read-only API call
   - check HTTP status from a safe endpoint
   - list metadata without printing secret values

6. Define revocation.

   Examples:

   - remove the keyRef from the consumer agent
   - disable the scoped token upstream
   - rotate the upstream credential
   - remove channel/account binding

7. Only after review, apply the private config change during a safe window.

   Inspect existing config first and preserve unrelated settings. Do not overwrite config wholesale.

## Output template

```yaml
capability: example-status-post
status: proposed
owner: techie
consumer: miette
scope:
  service: example-service
  action: post-status
  target: <approved-target>
access_model: delegation
private_change_needed: none
verification:
  method: harmless-use
  expected: approved test action succeeds
revocation:
  owner: techie
  method: remove delegated action or keyRef
safety_notes:
  - no raw secret values in handoffs
  - no live config changes until approved window
```
