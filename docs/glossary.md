<p align="center">
  <img src="../assets/sections/00-foundations.svg" alt="Foundations" width="100%">
</p>

# Glossary

Short definitions in the sense this guide uses them. A **per post** row is vocabulary that arrived in a cited post.

| | |
| --- | --- |
| Path | Explorer |
| Time | Dip in as you read |
| You need | Nothing |

### A2A / agent-to-agent

Agents delegating work to other agents. The OmniRoute post claims support for an agent-to-agent architecture (**per post**, [B6](https://x.com/Bober_smart/status/2108293657552117850)). Industry protocols exist for this; the post does not name a spec version.

### Agent

A model running in a loop toward a goal, with tools, memory, and a stop condition. See [what is an agent](00-foundations/what-is-an-agent.md).

### Agent host

The application a person uses: an IDE, a terminal, a chat product, a script.

### Agent loop

Perceive, plan, act, observe, remember, then stop or continue. See [the loop](00-foundations/the-agent-loop.md).

### AES-256-GCM

An established authenticated encryption mode. The OmniRoute post claims local API keys are encrypted with it (**per post**).

### Context window

The text the model can see on one call. It is finite. Anything that must outlive the call has to be stored elsewhere.

### Context compression

A gateway step that shortens logs, syntax, or history before the request is sent. The OmniRoute post names two engines, RTK and Caveman, and claims cuts of 15–95% (**per post**). This guide does not define those engine names beyond the post.

### Eval

A repeatable check that an agent still does the job. Task success, trajectory quality, and cost per success are the three this guide starts with. See [evals](06-evals/index.md).

### Fallback

Routing the same request to the next model or provider after an error or an empty quota. HTTP 429 (Too Many Requests) is the status the OmniRoute post names.

### Gateway

A local or remote service that exposes one API and forwards calls to many model providers. See [gateways](02-tools-mcp/gateways-and-routing.md).

### Human review gate

A person accepts a change before it lands. Central to the [security loop](07-security/find-fix-retest.md).

### Lead agent

The agent that writes the plan and later combines results. Worker agents do slices of that plan. **Per post** for Claude Managed Agents ([B4](https://x.com/ClaudeDevs/status/2108591328732856655)); the pattern itself is taught as synthesis on top of that report.

### MCP (Model Context Protocol)

An open protocol for connecting an agent host to tools and data sources. Established. The OmniRoute post also claims MCP support (**per post**).

### Memory

State the next step, or the next run, can use. In this guide, durable memory is a file the agent can open, not only the chat transcript. See [wiki memory](01-agent-patterns/wiki-memory.md).

### OpenAI-compatible API

An HTTP API that accepts the same kind of chat request a client already sends to OpenAI's API, so the client can change its base URL. Established idea. OmniRoute claims to offer one (**per post**).

### Per post

A claim that comes from a cited post and is not independently verified in this guide. See [how to read](how-to-read.md).

### Phase

A stage in a multi-agent plan. Later phases can read earlier results. The merge happens after the last phase.

### Plan-and-execute

Write a plan, carry out the steps, and revise the plan when an observation surprises you. See [patterns](01-agent-patterns/react-and-plan-execute.md).

### Prompt injection

Untrusted text (a web page, a ticket, a file) that tries to steer the model into using its tools. Named here as a threat, without procedures. See [threat model](07-security/threat-model.md).

### RAG

Retrieval-augmented generation: fetch passages and put them in the context window. Useful, and different from a wiki the agent maintains between runs.

### Raw source

Material kept as it arrived. In a research wiki, the `raw/` folder. In this guide, the original post, linked from the page that uses it.

### ReAct

The established pattern of interleaving a bit of reasoning with an action and an observation, associated with the ReAct line of work. See [patterns](01-agent-patterns/react-and-plan-execute.md).

### Schema

The rules for how the wiki is updated: what may be edited, what must be cited, when a page is stale. In this repo, [CONTRIBUTING](../CONTRIBUTING.md).

### Skill

A packaged procedure the agent can load: steps, checks, and sometimes code. A skill is narrower than a system prompt and easier to review. See [prompts and skills](03-prompting-skills/prompts-and-skills.md).

### Stop condition

The rule that ends the loop: the goal is met, the budget is spent, a person takes over, or a step has failed twice.

### Tool

A function the model may call: search, read a file, run a test, open a ticket. Tools have a name, a schema, a side effect, and a permission.

### Trajectory

The sequence of steps an agent took, not only the final answer. Evals that read trajectories catch lucky answers.

### Wiki

Maintained, linked pages. Searched before raw sources. Updated before the run ends.

## Continue

- [What is an agent](00-foundations/what-is-an-agent.md)
- [Social references & inspirations](references.md)

---

[Map](README.md) | [Paths](learning-paths.md) | [Glossary](glossary.md) | [References](references.md)
