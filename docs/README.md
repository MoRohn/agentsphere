<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../assets/banner-dark.png">
    <img src="../assets/banner-light.png" alt="Agentsphere. AI agents repository." width="100%">
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

# Guide map

Start with the [harness](01-agent-patterns/harness-engineering.md), a [learning path](learning-paths.md), or the section that matches the job in front of you. The posts, articles, and repositories behind the pages are in [Social references & inspirations](references.md).

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/diagrams/landscape-dark.svg">
  <img src="../assets/diagrams/landscape-light.svg" alt="The agent landscape, with the harness across the middle." width="100%">
</picture>
</p>

The products people rent sit beside that map: [Hosted agents](10-hosted-agents/index.md).

| | |
| --- | --- |
| Five minutes | The [harness picture](01-agent-patterns/harness-engineering.md): name the model, then one other part |
| New here | [How to read a claim](how-to-read.md), [what is an agent](00-foundations/what-is-an-agent.md), then the harness |
| Building | [Harness engineering](01-agent-patterns/harness-engineering.md), [wiki memory](01-agent-patterns/wiki-memory.md), and the [research playbook](09-playbooks/research-agent.md) |
| Operating | [Harness engineering](01-agent-patterns/harness-engineering.md), [cloud and local](05-runtime-infra/cloud-and-local.md), and [security](07-security/index.md) |
| Stuck | [Unstick a loop](09-playbooks/unstick-a-loop.md), then [score a run](09-playbooks/score-a-run.md) |

## Sections

### [00 · Foundations](00-foundations/index.md)

What an agent is, the loop, and how memory, tools, and planning share the work.

- [What is an agent](00-foundations/what-is-an-agent.md)
- [The agent loop](00-foundations/the-agent-loop.md)
- [Memory, tools, and planning](00-foundations/memory-tools-planning.md)

### [01 · Agent patterns](01-agent-patterns/index.md)

The harness is the frame. The other pages are ways of stressing one part of it.

- [Harness engineering](01-agent-patterns/harness-engineering.md)
- [ReAct and plan-and-execute](01-agent-patterns/react-and-plan-execute.md)
- [Wiki memory](01-agent-patterns/wiki-memory.md)
- [How agents remember](01-agent-patterns/how-agents-remember.md)

### [02 · Tools and MCP](02-tools-mcp/index.md)

How an agent touches the world, and how one API can front many models.

- [Tools and MCP](02-tools-mcp/tools-and-mcp.md)
- [Gateways and routing](02-tools-mcp/gateways-and-routing.md)

### [03 · Prompting and skills](03-prompting-skills/index.md)

What belongs in a prompt, what belongs in a skill, and two creative stacks.

- [Prompts and skills](03-prompting-skills/prompts-and-skills.md)
- [Creative toolkits](03-prompting-skills/creative-toolkits.md)

### [04 · Multi-agent](04-multi-agent/index.md)

- [Orchestration](04-multi-agent/orchestration.md)

### [05 · Runtime and infra](05-runtime-infra/index.md)

- [Cloud and local](05-runtime-infra/cloud-and-local.md)
- [Efficient inference](05-runtime-infra/efficient-inference.md)

### [06 · Evals](06-evals/index.md)

A primer on outcome, trajectory, and cost. The survey reading of SWE-bench Verified is on [harness engineering](01-agent-patterns/harness-engineering.md).

### [07 · Security](07-security/index.md)

- [Threat model](07-security/threat-model.md)
- [Find, review, fix, retest](07-security/find-fix-retest.md)
- [Gateways and supply chain](07-security/gateway-and-supply-chain.md)

### [08 · Case studies](08-case-studies/index.md)

One distillation for each cluster of posts.

### [09 · Playbooks](09-playbooks/index.md)

Hands-on recipes. Start with [your first agent](09-playbooks/first-agent.md) if the sections above are still vocabulary.

- [Your first agent](09-playbooks/first-agent.md)
- [Research agent](09-playbooks/research-agent.md)
- [Write a skill](09-playbooks/write-a-skill.md)
- [Skills and craft](09-playbooks/skills-and-craft.md)
- [Operate agents](09-playbooks/operate-agents.md)
- [Review a gateway](09-playbooks/review-a-gateway.md)
- [Score a run](09-playbooks/score-a-run.md)
- [Unstick a loop](09-playbooks/unstick-a-loop.md)

### [10 · Hosted agents](10-hosted-agents/index.md)

Closed products, read from official pages: Grok Bot, Muse, Dots, Claude Cowork, and computer use in Copilot Studio. Each one is placed on the six harness parts.

## Reference

| Page | Use it for |
| --- | --- |
| [Learning paths](learning-paths.md) | A sequence and a readiness check |
| [Glossary](glossary.md) | A term in one or two sentences |
| [How to read](how-to-read.md) | The three claim labels |
| [Community](community.md) | The account list from [@ai_explorer25](https://x.com/ai_explorer25/status/2108746842620014807) |
| [Diagram atlas](diagrams.md) | Every SVG and its Mermaid twin |
| [Style guide](style-guide.md) | Palette, page anatomy, GitHub rendering |
| [Social references & inspirations](references.md) | Which post, article, or repo shaped which page |

---

[Paths](learning-paths.md) | [Glossary](glossary.md) | [References](references.md) | [Contributing](../CONTRIBUTING.md)
