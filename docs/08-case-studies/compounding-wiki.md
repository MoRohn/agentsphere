<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/diagrams/wiki-memory-dark.svg">
  <img src="../../assets/diagrams/wiki-memory-light.svg" alt="Wiki memory diagram" width="100%">
</picture>
</p>

<p>
  <a href="../../paths/power-user/README.md"><img src="../../assets/badges/level-power.svg" alt="Power user" height="28"></a>
</p>

# Case study · Compounding wiki

A retelling of a research agent that leaves pages behind, attributed by the poster to Andrej Karpathy.

| | |
| --- | --- |
| Path | Power user |
| Source | [@fleyta88](https://x.com/fleyta88/status/2108619644399415565) |
| Posted | 2026-10-09, @fleyta88 |
| Concept | [Wiki memory](../01-agent-patterns/wiki-memory.md) |

## The situation

Research agents that only search and answer build a pile of chats. The post says the fix is to treat memory as files: raw sources untouched, a wiki of linked pages, and rules for the update. The next question hits the wiki first. Gaps go back to the sources. The answer is written back.

## Claims

| Claim | Status |
| --- | --- |
| The workflow is Karpathy's, as the poster understands a recent demonstration | Per post. The post has no separate primary URL for the demo |
| raw/ is the source of truth, wiki/ is maintained knowledge, schema is the update rules | Per post |
| The agent reads sources and writes linked pages | Per post |
| The wiki is searched before new source work | Per post |
| A hundred questions can leave a system, rather than a hundred chats | Per post, as the poster's contrast |
| This is "bigger than just better RAG" | Per post, as a slogan. The [concept page](../01-agent-patterns/wiki-memory.md) states a narrower, established distinction |

Related post: [a status by @gippp69](https://twitter.com/gippp69/status/2106744347836153989). This guide has not given that second post its own page.

## What to steal

The three nouns, and the rule that the run is unfinished until a page exists. agentsphere uses them as the linked post, [`docs/`](../README.md), and [CONTRIBUTING](../../CONTRIBUTING.md).

## What to leave

The tone. The missing primary link. Any implication that a wiki replaces search. The post says search still matters.

## Sources

- [@fleyta88](https://x.com/fleyta88/status/2108619644399415565)

## Continue

- Practice: [Research-agent playbook](../09-playbooks/research-agent.md)
- Next study: [Managed workflows](managed-workflows.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
