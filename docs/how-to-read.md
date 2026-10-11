<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/diagrams/knowledge-flow-dark.svg">
  <img src="../assets/diagrams/knowledge-flow-light.svg" alt="Six moves: question, notes, sources, write back, reflect, next run." width="100%">
</picture>
</p>

<p>
  <img src="../assets/badges/level-explorer.svg" alt="Explorer" height="28">
  &nbsp;
  <img src="../assets/badges/level-builder.svg" alt="Builder" height="28">
  &nbsp;
  <img src="../assets/badges/level-operator.svg" alt="Operator" height="28">
  &nbsp;
  <img src="../assets/badges/level-power.svg" alt="Power user" height="28">
</p>

# How to read agentsphere

The pages teach. The labels tell you how much weight a sentence can hold.

| | |
| --- | --- |
| Path | Every path starts here if you will quote the guide |
| Time | About 8 minutes |
| You need | Nothing |

## Three labels

| Label | Use it when | Example |
| --- | --- | --- |
| **Established** | The point is widely documented practice, or you have opened a paper or an official project page and are describing what that page says | The agent loop is perceive, plan, act, observe, remember, stop |
| **Per post** | The point appears in a cited post and this guide has not independently verified it | A gateway "supports 350+ providers" |
| **Synthesis** | This guide is organizing sources into a recommendation, a table, or a path | Which learning path to follow |

A sentence can carry two labels. "The post reports 6.17x. The bitnet.cpp paper reports a range that reaches 6.17x on x86." The first clause is per post. The second is established, because it points at the paper.

> [!NOTE]
> **Per post** means the claim is kept on purpose. Social posts are how this guide hears about new work. They are a weak place to stop.

## What a citation looks like

Inline, name the author and link the status:

[@fleyta88](https://x.com/fleyta88/status/2108619644399415565) describes a research agent that searches a wiki before it searches the web (per post).

At the bottom of a page, the source list names the author and links the post:

- [@fleyta88](https://x.com/fleyta88/status/2108619644399415565) — 2026-10-09. Wiki-memory loop.

The full list is [Social references & inspirations](references.md).

## What this guide will not fill in

- Destination URLs that a post left shortened.
- Benchmarks the post stated and no primary source here confirms.
- The unnamed "18 routing strategies," the bodies of the unnamed motion repositories, or the feature lists of products that were only @-mentioned.
- Exploit steps, payloads, or instructions for drawing down other people's free quotas.

When a primary source and a post disagree, the page says so and links both. The [LittleBit](05-runtime-infra/efficient-inference.md) page is the worked example: the post describes a bitwise XOR core, and the paper describes binarized factors plus scaling.

## How the repository is the example

| Piece | In the Karpathy-style story | In this repo |
| --- | --- | --- |
| Raw | `raw/` | The original post, linked from the page |
| Wiki | `wiki/` | [`docs/`](README.md) |
| Schema | rules for edits | [CONTRIBUTING.md](../CONTRIBUTING.md) |

You are encouraged to read a page, open the post, and correct the page if the distillation drifted. That correction is the system working.

## Check yourself

1. Which label belongs on a speedup that appears only in a post?
2. Where does the explanation live, and where do you open the original post?
3. What should you do with a shortened link the post did not expand?

## Continue

- Next: [Learning paths](learning-paths.md)
- Map: [All sections](README.md)

---

[Map](README.md) | [Paths](learning-paths.md) | [Glossary](glossary.md) | [References](references.md)
