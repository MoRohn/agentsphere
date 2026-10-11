<p align="center">
  <img src="../../assets/diagrams/gateway-routing.svg" alt="A local gateway between clients and providers" width="100%">
</p>

# Gateways and supply chain

A local proxy holds your keys and sees your prompts. A skill pack runs in your agent's name. Both are supply chain, even when the README says the words "local" and "open source."

| | |
| --- | --- |
| Path | Operator |
| Time | About 15 minutes |
| You need | [Gateways and routing](../02-tools-mcp/gateways-and-routing.md) and [threat model](threat-model.md) |

## What you will be able to do

- Review a gateway with eight questions.
- Review a skill or MCP server with six questions.
- Keep provider terms in the picture next to the architecture.

## Gateways

The OmniRoute post claims a local-first design, AES-256-GCM for keys, zero telemetry, and requests that go to providers rather than through an extra cloud ([B6](https://x.com/Bober_smart/status/2108293657552117850), per post). Those are the right topics for a review. They are not the review.

| Question | Why you ask it |
| --- | --- |
| Can you read the source of the build you are running? | A name in a post is not a commit you have |
| Where do keys sit at rest, and who can read that store? | "Encrypted locally" still needs a look at the code path |
| Does any request go anywhere besides the provider you chose? | Telemetry, updates, and "anonymous" stats are easy to miss |
| What is logged, and is the log redacted? | The proxy sees the prompt |
| What happens on a 429? | Fallback is a feature and also a way to spray a prompt across accounts |
| Whose accounts are attached? | Keys you issued, on terms you accept |
| Does pooling free tiers match those terms? | A routing trick can still be a terms breach |
| Can you point only a test repo at it first? | Limit the blast radius while you watch a day of traces |

> [!WARNING]
> **Free tokens and "leaked" builds.** The post frames a leak and a very large free-token number as the news. Do not hunt leaked credentials. Do not treat a giveaway figure as capacity you own. If the software is legitimate, you can find a repository, build it, and use accounts you control.

The hands-on list is the [gateway playbook](../09-playbooks/review-a-gateway.md).

## Skills, MCP servers, and design packs

The motion post's useful security line is to check each repository before you install ([B9](https://x.com/N01ennn/status/2108182955671580771), per post). The website-library post invites you to paste prompts and source into an agent ([B5](https://x.com/himanshubuildss/status/2108540618553356666), per post). Pasting is safer than executing, and it is still how untrusted text enters the window.

| Question | A careful answer |
| --- | --- |
| What does install run? | You can say, because you read it |
| Which commit? | Pinned, not a floating default branch |
| What tools does the skill tell the agent to use? | Listed, and narrower than your personal shell |
| Does the skill ask to be trusted over other instructions? | You reject packs that tell the agent to ignore its standing rules |
| Where does it phone home? | You looked |
| Can it see production keys? | Not in the environment where you try it |

## Compression and traces

A compressor that rewrites history before the provider sees it also rewrites your audit trail, unless you store the pre-compression prompt. Keep that copy in a redacted trace if you need to debug a weird answer. The 15–95% band from the gateway post is a claim about savings, not a claim about fidelity.

## Check yourself

1. Why is "0 telemetry" a claim to test rather than a feature to repeat?
2. What is wrong with attaching a free-tier account you do not control?
3. Which sentence in the motion post is the supply-chain rule?

## Sources

- [B6](https://x.com/Bober_smart/status/2108293657552117850) — gateway security claims, per post.
- [B9](https://x.com/N01ennn/status/2108182955671580771) — check repos before install, per post.
- [B5](https://x.com/himanshubuildss/status/2108540618553356666) — paste prompts and source into an agent, per post.
- The question lists are synthesis.

## Continue

- Practice: [Review a gateway](../09-playbooks/review-a-gateway.md)
- Previous: [Find, review, fix, retest](find-fix-retest.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
