<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/00-foundations-dark.png">
  <img src="../assets/sections/00-foundations-light.png" alt="Foundations" width="100%">
</picture>
</p>

<p>
  <a href="../paths/explorer/README.md"><img src="../assets/badges/level-explorer.svg" alt="Explorer" height="28"></a>
</p>

# Glossary

Short definitions in the sense this guide uses them. A **per post** row is vocabulary that arrived in a cited post.

| | |
| --- | --- |
| Path | Explorer |
| Time | Dip in as you read |
| You need | Nothing |

### A2A / agent-to-agent

Agents delegating work to other agents. The OmniRoute post claims support for an agent-to-agent architecture (**per post**, [@Bober_smart](https://x.com/Bober_smart/status/2108293657552117850)). Industry protocols exist for this; the post does not name a spec version.

### Agent

A model running in a loop toward a goal, with tools, memory, and a stop condition. See [what is an agent](00-foundations/what-is-an-agent.md).

### Agent card

A one-page sketch of an agent you might run: the six parts, a stop rule, and one traced task. The exercise is [your first agent](09-playbooks/first-agent.md).

### Agent host

The application a person uses: an IDE, a terminal, a chat product, a script.

### Agent loop

Perceive, plan, act, observe, remember, then stop or continue. See [the loop](00-foundations/the-agent-loop.md).

### AES-256-GCM

An established authenticated encryption mode. The OmniRoute post claims local API keys are encrypted with it (**per post**).

### Compaction

Summarizing a context window that is about to fill, then continuing from that summary. It is a property of a long run, not a gateway that shortens a request before it is sent. The summary must not be the only copy of the decision. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Context window

The text the model can see on one call. It is finite. Anything that must outlive the call has to be stored elsewhere. In the memory split this guide uses, the window is working memory.

### Context compression

A gateway step that shortens logs, syntax, or history before the request is sent. The OmniRoute post names two engines, RTK and Caveman, and claims cuts of 15–95% (**per post**). This guide does not define those engine names beyond the post. Distinct from compaction, which summarizes a window the agent is already in.

### Episodic memory

A stored trace of what happened: steps, tool results, and reflections on those runs. It lives outside the window, in a log or a note the next run can search. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Eval

A repeatable check that an agent still does the job. Task success, trajectory quality, and cost per success are the three this guide starts with. See [evals](06-evals/index.md).

### Execution harness

The runtime around a foundation model: observation, context, control, action, state, and verification. The model proposes. The harness decides what it sees, what it may do, and whether the run holds. See [harness engineering](01-agent-patterns/harness-engineering.md).

### Fallback

Routing the same request to the next model or provider after an error or an empty quota. HTTP 429 (Too Many Requests) is the status the OmniRoute post names.

### Gateway

A local or remote service that exposes one API and forwards calls to many model providers. See [gateways](02-tools-mcp/gateways-and-routing.md).

### Harness engineering

Designing the runtime as a first-class object, matched to the task, rather than treating agent quality as a property of the model alone. The four eras and the six parts are [harness engineering](01-agent-patterns/harness-engineering.md).

### Hosted agent

A closed product that runs the harness for you: the computer, the memory, and the approval gate. The current reading is [hosted agents](10-hosted-agents/index.md).

### Human review gate

A person accepts a change before it lands. Central to the [security loop](07-security/find-fix-retest.md).

### Lead agent

The agent that writes the plan and later combines results. Worker agents do slices of that plan. **Per post** for Claude Managed Agents ([@ClaudeDevs](https://x.com/ClaudeDevs/status/2108591328732856655)); the pattern itself is taught as synthesis on top of that report.

### MCP (Model Context Protocol)

An open protocol for connecting an agent host to tools and data sources. Established. The OmniRoute post also claims MCP support (**per post**).

### Memory

State the next step, or the next run, can use. Working memory is the window and dies with the call. Episodic, semantic, and procedural memory are files. See [how agents remember](01-agent-patterns/how-agents-remember.md). The folder layout is [wiki memory](01-agent-patterns/wiki-memory.md).

### OpenAI-compatible API

An HTTP API that accepts the same kind of chat request a client already sends to OpenAI's API, so the client can change its base URL. Established idea. OmniRoute claims to offer one (**per post**).

### Per post

A claim that comes from a cited post and is not independently verified in this guide. See [how to read](how-to-read.md).

### Phase

A stage in a multi-agent plan. Later phases can read earlier results. The merge happens after the last phase.

### Plan-and-execute

Write a plan, carry out the steps, and revise the plan when an observation surprises you. See [patterns](01-agent-patterns/react-and-plan-execute.md).

### Procedural memory

A stored way of working: a skill, a schema, or a checklist. Reviewed like code, loaded when the job matches. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Prompt injection

Untrusted text (a web page, a ticket, a file) that tries to steer the model into using its tools. Named here as a threat, without procedures. See [threat model](07-security/threat-model.md).

### RAG

Retrieval-augmented generation: fetch passages and put them in the context window for this call. That is a load. It becomes memory only when the conclusion is written back. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Raw source

Material kept as it arrived. In a research wiki, the `raw/` folder. In this guide, the original post, linked from the page that uses it.

### ReAct

The established pattern of interleaving a bit of reasoning with an action and an observation, associated with the ReAct line of work. See [patterns](01-agent-patterns/react-and-plan-execute.md).

### Reflection

A judgment about a run, stored where the next run will see it before repeating the mistake. A critique that no later step reads is not one. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Schema

The rules for how the wiki is updated: what may be edited, what must be cited, when a page is stale. In this repo, [CONTRIBUTING](../CONTRIBUTING.md).

### Semantic memory

A maintained statement of what is true, with a source, and an explicit gap when you do not know. In this guide, a wiki page. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Skill

A packaged procedure the agent can load: steps, checks, and sometimes code. A skill is narrower than a system prompt and easier to review. See [prompts and skills](03-prompting-skills/prompts-and-skills.md).

### Stop condition

The rule that ends the loop: the goal is met, the budget is spent, a person takes over, or a step has failed twice.

### Tool

A function the model may call: search, read a file, run a test, open a ticket. Tools have a name, a schema, a side effect, and a permission.

### Verification and governance

The harness part that checks and constrains a run: tests, approval gates, sandboxes, rollback, budgets, and an audit trail. A prompt that says "be careful" is not this part. See [harness engineering](01-agent-patterns/harness-engineering.md) and the [threat model](07-security/threat-model.md).

### Trajectory

The sequence of steps an agent took, not only the final answer. Evals that read trajectories catch lucky answers.

### Wiki

Maintained, linked pages. Searched before raw sources. Updated before the run ends.

### Working memory

The context window for this call. Rebuilt every time. If a fact has to survive, it does not live only here. See [how agents remember](01-agent-patterns/how-agents-remember.md).

### Write-back

Saving a conclusion outside the window so a later run can open it without the transcript. A search result is not a memory until this happens.

## Continue

- [What is an agent](00-foundations/what-is-an-agent.md)
- [Social references & inspirations](references.md)

---

[Map](README.md) | [Paths](learning-paths.md) | [Glossary](glossary.md) | [References](references.md)
