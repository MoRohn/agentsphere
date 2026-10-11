<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="agentsphere. The living field guide to the agent era." width="100%">
  </picture>
</p>

<p align="center">
  <a href="CHANGELOG.md">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/badges/version-dark.svg">
      <img alt="version 0.3.0" src="assets/badges/version-light.svg" height="28">
    </picture>
  </a>
  &nbsp;
  <a href="docs/learning-paths.md">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/badges/paths-dark.svg">
      <img alt="four learning paths" src="assets/badges/paths-light.svg" height="28">
    </picture>
  </a>
  &nbsp;
  <a href="docs/references.md">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/badges/references-dark.svg">
      <img alt="social references and inspirations" src="assets/badges/references-light.svg" height="28">
    </picture>
  </a>
</p>

# agentsphere

**The living field guide to the agent era.** Start as a beginner. Leave able to design an agent's memory, tools, orchestration, runtime, and security, and able to tell a sourced claim from a rumor.

The pages in [`docs/`](docs/README.md) are the guide. Posts, articles, and repositories that shaped them are collected in [Social references & inspirations](docs/references.md). A claim from a post stays linked and marked. A claim from a paper or a project page is marked separately.

## Start here

If you are new, do these three and stop. You will have a definition, a loop, and one page you wrote yourself.

1. [What is an agent](docs/00-foundations/what-is-an-agent.md)
2. [The agent loop](docs/00-foundations/the-agent-loop.md)
3. [Your first agent](docs/09-playbooks/first-agent.md) — forty minutes, no API key

| If you need to | Open |
| --- | --- |
| Explain an agent to someone else | [Foundations](docs/00-foundations/index.md) |
| Leave notes the next run can search | [Wiki memory](docs/01-agent-patterns/wiki-memory.md), then the [research playbook](docs/09-playbooks/research-agent.md) |
| Move a procedure out of a giant prompt | [Write a skill](docs/09-playbooks/write-a-skill.md) |
| Choose laptop or cloud for a real task | [Operate agents](docs/09-playbooks/operate-agents.md) |
| Decide whether a gateway can see your prompts | [Review a gateway](docs/09-playbooks/review-a-gateway.md) |
| Tell whether a change helped | [Score a run](docs/09-playbooks/score-a-run.md) |
| Stop a run that thrashes or invents facts | [Unstick a loop](docs/09-playbooks/unstick-a-loop.md) |

## Choose a path

| Path | Start here if you | Read | You will be able to |
| --- | --- | --- | --- |
| **Explorer** | are new to agents | [Foundations](docs/00-foundations/index.md), the [glossary](docs/glossary.md), and [the loop](docs/00-foundations/the-agent-loop.md) | explain an agent, its loop, and its memory |
| **Builder** | want to make one | [Tools and MCP](docs/02-tools-mcp/index.md), [skills](docs/03-prompting-skills/index.md), and [wiki memory](docs/01-agent-patterns/wiki-memory.md) | design a research agent that writes pages back |
| **Operator** | run agents for a team | [Cloud and local](docs/05-runtime-infra/cloud-and-local.md), [orchestration](docs/04-multi-agent/orchestration.md), [evals](docs/06-evals/index.md), and [security](docs/07-security/index.md) | pick a runtime and name the risks |
| **Power user** | want the practice | [Playbooks](docs/09-playbooks/index.md), [case studies](docs/08-case-studies/index.md), and [contributing](CONTRIBUTING.md) | run a playbook on real work and write the result down |

Sequences, timing, and a readiness check for each path: [Learning paths](docs/learning-paths.md).

## Map

| | Section | What it covers |
| --- | --- | --- |
| 00 | [Foundations](docs/00-foundations/index.md) | Definition, the loop, memory, tools, planning |
| 01 | [Agent patterns](docs/01-agent-patterns/index.md) | ReAct, plan-and-execute, wiki memory, how agents remember |
| 02 | [Tools and MCP](docs/02-tools-mcp/index.md) | Tools, Model Context Protocol, gateways |
| 03 | [Prompting and skills](docs/03-prompting-skills/index.md) | Prompts, skill packs, creative stacks |
| 04 | [Multi-agent](docs/04-multi-agent/index.md) | Lead agents, phases, merging results |
| 05 | [Runtime and infra](docs/05-runtime-infra/index.md) | Cloud and local runs, efficient inference |
| 06 | [Evals](docs/06-evals/index.md) | How to tell that an agent got better |
| 07 | [Security](docs/07-security/index.md) | Threat model, review gates, supply chain |
| 08 | [Case studies](docs/08-case-studies/index.md) | Posts and projects, with the claim kept separate from the pattern |
| 09 | [Playbooks](docs/09-playbooks/index.md) | Checklists and worked examples, from a first agent card to a scored run |

Also: [glossary](docs/glossary.md), [how to read a claim](docs/how-to-read.md), [community list](docs/community.md), [diagram atlas](docs/diagrams.md), [social references & inspirations](docs/references.md).

## How a research agent keeps what it learns

An agent remembers only what it writes down outside the context window. The window is working memory: rebuilt every call, and worse at using a fact buried in the middle of a long input than a fact at either end. Episodic memory is the trace of what happened. Semantic memory is a page that says what is true, with a source. Procedural memory is a skill or a checklist. A search that pastes passages into the window is not a fifth kind. It is a load. It becomes memory when the conclusion is written back.

<p align="center">
  <img src="assets/diagrams/knowledge-flow.svg" alt="Six moves: name the question, search notes, read sources, write the page, reflect, and let the next run start from that page." width="100%">
</p>

<p align="center">
  <img src="assets/diagrams/memory-map.svg" alt="Working memory is the context window. Episodic, semantic, and procedural memory live outside it. Retrieval is loaded for one call unless it is written back." width="100%">
</p>

| Memory | Lives | Survives the call? |
| --- | --- | --- |
| Working | The window | No |
| Episodic | Traces, logs, reflections | Yes, if you stored them |
| Semantic | Wiki pages with sources | Yes, if you update them |
| Procedural | Skills and checklists | Yes, if they are files |

The loop in the first figure is how a research agent uses those stores. Name the decision and the done-when. Search notes and past traces before the open web. Read sources without rewriting them. Write one page: answer, evidence, gap. Reflect as a rule the next run will see, and drop what that rule does not need. The next question starts on the page.

Three methods sit on top of that loop.

| Method | The move | Where to read it |
| --- | --- | --- |
| Plan, act, observe | Interleave a step with a check of what the tool returned | [ReAct](https://arxiv.org/abs/2210.03629) |
| Reflection | Store a judgment that changes the next attempt | [Reflexion](https://arxiv.org/abs/2303.11366), [Generative Agents](https://arxiv.org/abs/2304.03442) |
| Notes and compaction | Keep a file outside the window. Summarize the window without making the summary the only copy of the decision | [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |

Five patterns follow from those methods.

| Pattern | Use it when |
| --- | --- |
| Notes first | The question might already have a page |
| One page per question | A stranger should be able to answer tomorrow |
| Claim, source, gap | A number or a product feature is in play |
| Reflection as a rule | The same miss will happen again |
| Compact the trace, keep the note | The window is mostly tool output |

Forget on purpose. Raw logs can go once the conclusion is on the page. A stale page cannot stay beside a newer one. A reflection nobody will read is just more text in the window.

| What you see | Change this |
| --- | --- |
| The same search every session | Write the page |
| A fluent answer with no source | Stop treating retrieval as memory |
| After a summary, it forgot the task | Put the decision in a note |
| The same mistake, plus a long self-critique | Store a rule where the next run looks first |

**Checklist.** Done-when is written first. Notes are searched before the web. The page has an answer, a source, and a gap. The raw source was not edited. Something was dropped on purpose. The next run can start without the transcript.

**A worked pass.** The window is full of test logs and the agent has forgotten the file it was migrating. The note already names `billing/client.ts`. The run writes the failing assertion into the note, leaves the log on disk, and drops the log body from the window. The next run opens the note. It does not reread the morning's logs to recover a filename.

The full argument, the paper list, and a longer example: [How agents remember](docs/01-agent-patterns/how-agents-remember.md).

## How claims are marked

| Mark | Meaning |
| --- | --- |
| **Established** | Widely documented practice, a public paper, or an official project page |
| **Per post** | Stated in a cited post. Kept, linked, and left unverified by this guide |
| **Synthesis** | This guide's own organization of the two |

Read the short rules before you quote a number from these pages: [How to read agentsphere](docs/how-to-read.md).

## Social references & inspirations

The posts, articles, and repositories behind the pages are listed, with the page each one shaped, in [Social references & inspirations](docs/references.md).

## Extend the guide

The writing rules live in [CONTRIBUTING](CONTRIBUTING.md). New material is a page a reader will open, with the source linked and the claim marked.
