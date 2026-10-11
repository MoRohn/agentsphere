<p align="center">
  <img src="../../assets/sections/00-foundations.svg" alt="Foundations" width="100%">
</p>

# Memory, tools, and planning

Three different jobs get blurred into "the context window." Separating them is the practical skill in this section.

| | |
| --- | --- |
| Path | Explorer, and the start of Builder |
| Time | About 15 minutes |
| You need | [The agent loop](the-agent-loop.md) |

## What you will be able to do

- Put a fact in the right store: the window, a file, or a retrieval index.
- Describe a tool as a contract, not as a vibe.
- Write a plan as an artifact the loop can revisit.

## Three stores

| Store | Lifetime | Good for | Weak for |
| --- | --- | --- | --- |
| **Context window** | This call | The goal, the last observation, a short plan | A month of decisions |
| **Files the agent maintains** | As long as you keep them | Conclusions, links, open questions, corrections | Raw evidence you must not rewrite |
| **Retrieval** | As long as the index does | Finding a passage in a large corpus | Being the place a conclusion is maintained |

Retrieval, including the pattern usually called RAG, fetches passages into the window. It does not, by itself, maintain a conclusion. A wiki page is a conclusion with links back to the passages. You will often want both: search to find, pages to remember. The argument for taking pages seriously is [wiki memory](../01-agent-patterns/wiki-memory.md).

> [!TIP]
> **Established.** The window is finite. Stuffing it with the entire history feels like memory until a later call drops the early turns. Durable memory is whatever the next run can open on purpose.

## A tool is a contract

| Clause | Question to answer before you add the tool |
| --- | --- |
| Name | Can the model tell this tool from its neighbor? |
| Schema | What arguments are required, and what do they mean? |
| Side effect | Does it read, or does it also write, send, or delete? |
| Permission | What is the smallest scope that still does the job? |
| Result | What will the observe step actually see, including on failure? |

A shell that can do anything will be asked to do anything, including things a page of untrusted text suggested. Narrow tools are easier to review and easier for the model to choose among. How those tools are attached to a host, including MCP, is [tools and MCP](../02-tools-mcp/tools-and-mcp.md).

## A plan is a written thing

Planning is step 2 of the loop, made visible. For a two-step task, the plan can be a sentence. For a task that will run while you are away, the plan should be a file:

- The goal, in one sentence.
- The steps, each small enough to observe.
- What "done" means.
- What the agent must not do.
- Where the notes go.

A lead agent that writes this kind of plan, then hands phases to other agents, is the pattern reported for Claude Managed Agents ([B4](https://x.com/ClaudeDevs/status/2108591328732856655), per post). The full treatment is [orchestration](../04-multi-agent/orchestration.md).

## How the three fail together

A beautiful plan with no tool still cannot open the file. A powerful tool with no memory repeats itself tomorrow. A full memory with no stop condition keeps "improving" the page after it was good. When you debug an agent, say which of the three you are looking at before you change the prompt.

## Check yourself

1. Where should a raw source live, and where should the conclusion live?
2. Name the five clauses of a tool contract.
3. What belongs on a plan that will run while you are away?

## Sources

- Established practice for context windows, retrieval, and tool use.
- [B2](https://x.com/fleyta88/status/2108619644399415565) and [B4](https://x.com/ClaudeDevs/status/2108591328732856655) are the posts that extend memory and planning. Their claims are detailed on the linked pages.

## Continue

- Next: [ReAct and plan-and-execute](../01-agent-patterns/react-and-plan-execute.md)
- Previous: [The agent loop](the-agent-loop.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
