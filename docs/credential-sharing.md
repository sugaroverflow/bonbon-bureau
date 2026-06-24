# Credential sharing between agents

Bonbon Bureau agents should share *capabilities*, not raw credentials.

A capability is a named permission to perform a bounded action, such as:

- read a public issue tracker
- post to one Discord channel
- use one model provider profile
- check one deployment status endpoint
- rotate one application credential

The secret value stays in the private credential system. Public docs only name the capability and the expected verification behavior.

## Principles

1. **Least privilege** — grant only the action the agent needs.
2. **Per-agent references** — prefer separate keyRefs/env names for each agent, even when they point to the same upstream service.
3. **No shared raw values in chat** — agents never pass tokens to each other through transcripts, docs, or handoff packets.
4. **Verify by use** — confirm a credential with a harmless action, not by printing or comparing the value.
5. **Revocation is part of the design** — every shared capability needs an owner and a rollback path.
6. **Public repo stays abstract** — use placeholder names like `EXAMPLE_API_KEY` and `<channel-id>`.

## Recommended shape

```yaml
capability: discord-channel-post
owner: techie
consumer: miette
provider: private-config
secret_reference: envprov:EXAMPLE_DISCORD_TOKEN
scope:
  service: discord
  action: post-message
  target: <channel-id>
verification:
  method: harmless-use
  expected: message send succeeds in an approved test channel
revocation:
  method: remove keyRef or disable provider token
  owner: techie
notes: public-safe placeholder only
```

## Sharing model

Prefer this order:

1. **Delegation** — Miette asks the specialist agent to act; Miette never receives the credential.
2. **Bounded capability** — Miette gets a narrow keyRef for a specific action.
3. **Shared upstream credential** — only when the provider cannot create scoped credentials; document the risk and rotate plan.

Avoid broad shared credentials unless there is no practical alternative.

## Handoff packet rule

Handoffs may include:

- capability name
- intended action
- target placeholder or public identifier
- verification method
- responsible owner

Handoffs must not include:

- raw token/password/API key values
- private credential manager item paths unless intentionally public
- local private config paths
- raw transcripts containing secrets

## Example handoff language

Good:

```text
Miette needs the ability to ask Techie to post a deployment status update. Use capability `discord-status-post`; Techie owns the credential and verifies by sending an approved test message.
```

Bad:

```text
Here is the bot token; Miette can paste it into her config.
```

## Review questions before granting

- Which agent needs this capability?
- Can the specialist do the action instead of sharing access?
- What exact service/action/target is needed?
- Is there a scoped token or role available?
- How will we verify without exposing the secret?
- Who owns rotation and revocation?
- What should happen if the agent is disabled?

## Public/private boundary

Public Bonbon Bureau repo:

- capability names
- placeholder keyRef shapes
- safety rules
- runbooks
- verification patterns

Private OpenClaw config/credential store:

- real keyRefs
- real provider item paths
- raw secret values
- account IDs if sensitive
- binding IDs if sensitive
