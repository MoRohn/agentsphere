<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/diagrams/cloud-vs-local-dark.svg">
  <img src="../../assets/diagrams/cloud-vs-local-light.svg" alt="Local and cloud topologies" width="100%">
</picture>
</p>

<p>
  <img src="../../assets/badges/level-power.svg" alt="Power user" height="28">
</p>

# Playbook · Operate agents

Place three tasks. One local, one cloud, one you deliberately do not automate yet.

| | |
| --- | --- |
| Path | Power user |
| Time | About 45 minutes |
| You need | [Cloud and local](../05-runtime-infra/cloud-and-local.md) and [orchestration](../04-multi-agent/orchestration.md) |
| Produces | A one-page placement note a teammate can argue with |

[@ryancarson](https://x.com/ryancarson/status/2108286700468191266) argues that per-seat local licenses fall behind cloud agents, and says not to build your own code factory (per post). This playbook uses the decision table from the concept page, which is synthesis. You can finish the playbook and still disagree with the post.

## 1. Write down the three tasks

Use real work. If you have none handy, these stand in:

| Task | Shape |
| --- | --- |
| A | Fix a typo and a test in a private repo, this afternoon |
| B | Migrate a dull API across twenty call sites, review tomorrow |
| C | Design the memory layout for a research agent your team will use all quarter |

## 2. Score each task

Copy the table. Fill it with "local," "cloud," or "a person."

| Question | A | B | C |
| --- | --- | --- | --- |
| How long will it run? | | | |
| Can this repo sit on someone else's machine? | | | |
| What will you review: live steps, or a diff? | | | |
| Does anyone else need the same setup? | | | |
| Are you trying to learn the loop, or to ship the change? | | | |

A typical, defensible outcome, not a required one:

| Task | Placement | Why this guide would defend it |
| --- | --- | --- |
| A | Local | Short, private, you are in the loop. A cloud run is ceremony |
| B | Cloud | Long, mechanical, the review artifact is a branch |
| C | A person, with a local scratch agent | The deliverable is a schema. Buying a factory does not write your rules |

## 3. If you chose cloud, write the handoff

The handoff is a plan, not a vibe. Minimum:

- Goal and done-when.
- Repo and branch policy.
- Tools the run may use.
- What it must not touch.
- Where the log will be in the morning.

If the work splits, name phases before you name agents. A lead that writes that plan is the pattern in [orchestration](../04-multi-agent/orchestration.md). Whether your vendor matches the Claude Managed Agents post is a docs check, not something this playbook can promise.

## 4. If you chose local, write the boundary

- Which keys are in the environment.
- Whether the agent can push.
- Where the trace goes.
- The stop condition, including a budget.

A local license per person is what the post criticizes. A local loop with a written stop condition is still the right instrument for task A. The post does not contain a counterexample that makes task A cheaper in a cloud queue.

## 5. Say what you will not build

List the factory pieces you are buying or skipping: queue, sandbox, shared credentials, eval harness, merge bot. Skipping them is allowed. Forgetting that they exist is how a weekend prototype becomes an unowned production path.

## Check yourself

1. Which of your three tasks is local because of secrecy or length, and which because you are learning?
2. What has to be on a cloud handoff that a chat message usually omits?
3. What did the post not measure?

## Sources

- [@ryancarson](https://x.com/ryancarson/status/2108286700468191266) — the argument, per post.
- Placements and the handoff list are synthesis.

## Continue

- [Review a gateway](review-a-gateway.md)
- [Evals](../06-evals/index.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
