<p align="center">
  <img src="../../assets/diagrams/gateway-routing.svg" alt="Gateway routing diagram" width="100%">
</p>

# Case study · Local gateway

OmniRoute, as one post describes it: a local OpenAI-compatible router in front of a large pool of providers.

| | |
| --- | --- |
| Path | Power user |
| Source | [B6](https://x.com/Bober_smart/status/2108293657552117850) |
| Posted | 2026-10-08, @Bober_smart |
| Concept | [Gateways and routing](../02-tools-mcp/gateways-and-routing.md) |

## The situation

The post says a local gateway pools free limits from many providers, speaks one API that coding agents already use, falls back when a provider returns 429 or runs out of quota, compresses context, stores keys locally, and speaks MCP plus an agent-to-agent setup. It also leads with a leak and a huge free-token number.

## Claims

Every product row is per post. The full table is on the [concept page](../02-tools-mcp/gateways-and-routing.md). The claims most often repeated without a source in the room:

| Claim | Keep it tied to |
| --- | --- |
| 350+ providers, 90+ services, 18 strategies | The post. The strategies are not named |
| 15–95% compression via RTK and Caveman | The post. The engines are not specified here |
| AES-256-GCM and zero telemetry | The post. Not an audit |
| 800 million free tokens, via a leak | The post's hook. Not a capacity plan |

The project link in the post was not resolved. An earlier status by the same author: [twitter.com/bober_smart/status/2103462864870686848](https://twitter.com/bober_smart/status/2103462864870686848).

## What to steal

The picture: many hosts, one local endpoint, explicit fallback, keys that do not have to sit in a third-party proxy. Then verify it with the [review playbook](../09-playbooks/review-a-gateway.md).

## What to leave

The leak framing. Any plan to aggregate accounts you do not control. Any percentage you have not measured.

## Sources

- [B6](https://x.com/Bober_smart/status/2108293657552117850)

## Continue

- Next study: [Motion and web stacks](motion-and-web-stacks.md)
- Security: [Gateways and supply chain](../07-security/gateway-and-supply-chain.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
