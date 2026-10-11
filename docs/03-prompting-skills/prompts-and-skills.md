<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/03-skills-dark.png">
  <img src="../../assets/sections/03-skills-light.png" alt="Prompting and skills" width="100%">
</picture>
</p>

<p>
  <a href="../../paths/builder/README.md"><img src="../../assets/badges/level-builder.svg" alt="Builder" height="28"></a>
</p>

# Prompts and skills

Put stable procedure in a skill, facts in a file, and secrets in a store the prompt cannot casually reprint.

| | |
| --- | --- |
| Path | Builder |
| Time | About 15 minutes |
| You need | [Memory, tools, and planning](../00-foundations/memory-tools-planning.md) |

## What you will be able to do

- Name the four layers of instruction an agent is actually following.
- Decide what belongs in a skill instead of a longer system prompt.
- Review a third-party skill before it runs.

## Four layers

| Layer | Changes | Holds | Example |
| --- | --- | --- | --- |
| **System prompt** | Rarely | Role, safety rules, definition of done | "You maintain a wiki. Cite sources. Mark per-post claims." |
| **Skill** | When the job type changes | Steps, checks, formats for one kind of work | "To cite a source, follow this checklist." |
| **Task** | Every run | The goal for this run | "Update the gateway page from a new source." |
| **Context** | Every step | Files, tool results, the plan | The raw post, the current page |

A single prompt that tries to be all four becomes a novel. The model then attends to the novel's adjectives and misses the checklist. The layers also have different reviewers. A system prompt is a policy. A skill is a procedure. A task is a ticket. Context is evidence.

> [!TIP]
> **Established.** Instructions that must be true on every run belong above the task. Facts that change belong in files the agent reads, because editing a file is easier to review than editing a prompt from memory.

## What a skill contains

A useful skill is short enough to read in one sitting:

- When to use it, and when not to.
- Inputs it expects (paths, URLs, a brief).
- Steps, in order, each ending in something you can see.
- Checks it runs on its own output.
- Tools it is allowed to call.

The motion-design post is a catalog of skills aimed at one job: an agent writes the code, a skill sets timing and camera, an engine renders a video ([@N01ennn](https://x.com/N01ennn/status/2108182955671580771), per post). The catalog itself is the [creative toolkits](creative-toolkits.md) page. The pattern is the point, and it travels: code from the model, constraints from the skill, an artifact from a real renderer.

## Installing a skill is running code

A skill file is instructions. Many skill packs also tell the agent to execute setup commands or to import a repository. That is a supply-chain decision, the same family as installing a dependency.

The motion post says to check each repository before you install (per post). Take that sentence, and leave the rest of the hype. The checks are in [gateways and supply chain](../07-security/gateway-and-supply-chain.md) and in the [craft playbook](../09-playbooks/skills-and-craft.md).

## Secrets and standing orders

A prompt is a poor vault. Anything the model can see, a tool result or a later page can echo. Put API keys in the environment or a local secret store, and let a tool use them without returning the secret in the observation. The OmniRoute post claims local encryption of keys ([@Bober_smart](https://x.com/Bober_smart/status/2108293657552117850), per post). Whether a given gateway does that is something you verify, not something you paste into a system prompt as a wish.

## Check yourself

1. Which layer should hold "cite the URL," and which should hold today's source?
2. What five headings do you want on a skill before you trust it?
3. Why is "check the repo before you install" a security step and not only a taste step?

## Sources

- Established practice for separating standing instructions, procedures, tasks, and evidence.
- [@N01ennn](https://x.com/N01ennn/status/2108182955671580771) — 2026-10-08. Skills plus an engine, and the advice to check repos, per post.
- [@Bober_smart](https://x.com/Bober_smart/status/2108293657552117850) — local key encryption, per post, unverified.

## Continue

- Next: [Creative toolkits](creative-toolkits.md)
- Practice: [Write a skill](../09-playbooks/write-a-skill.md)
- Previous: [Gateways and routing](../02-tools-mcp/gateways-and-routing.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
