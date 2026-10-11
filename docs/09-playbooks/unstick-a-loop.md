<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/diagrams/agent-loop-dark.svg">
  <img src="../../assets/diagrams/agent-loop-light.svg" alt="The agent loop" width="100%">
</picture>
</p>

<p>
  <a href="../../paths/explorer/README.md"><img src="../../assets/badges/level-explorer.svg" alt="Explorer" height="28"></a>
  &nbsp;
  <a href="../../paths/builder/README.md"><img src="../../assets/badges/level-builder.svg" alt="Builder" height="28"></a>
  &nbsp;
  <a href="../../paths/operator/README.md"><img src="../../assets/badges/level-operator.svg" alt="Operator" height="28"></a>
  &nbsp;
  <a href="../../paths/power-user/README.md"><img src="../../assets/badges/level-power.svg" alt="Power user" height="28"></a>
</p>

# Playbook · Unstick a loop

When a run thrashes, stalls, or invents facts, change the step that is thin. Do not start by swapping the model.

| | |
| --- | --- |
| Path | Any path, once you have a trace |
| Time | About 30 minutes |
| You need | [The agent loop](../00-foundations/the-agent-loop.md) |
| Produces | A one-line diagnosis and the single change you will try next |

The failure modes are established. This order of fixes is synthesis.

## 1. Write what you saw, not what you felt

One sentence: "It searched the web twelve times for the same fact and then named a repository." Or: "It wrote an outline for twenty minutes and never called a tool." If you cannot say what the tools returned, save a trace first. A vibe is not a diagnosis.

## 2. Match it to a thin step

| What you see | Thin step | Change this first |
| --- | --- | --- |
| The same search every session | Remember | A page the next run must open |
| Steps continue after the goal is met | Stop | Done-when, and a maximum step count |
| It declares success it did not check | Observe | A required read of the tool result, including errors |
| Outlines of outlines, no tool call | Act | A rule that a plan step ends in one tool call |
| "Do the whole project" as one step | Plan | Split until each act has one observation |
| A URL, number, or repo name with no source | Instructions | "Gaps are written. URLs are copied, not searched into existence." |
| It obeys a sentence inside a web page, README, or ticket | Instructions | Treat retrieved text as data. A person accepts writes. |
| It spends quota in a tight retry | Stop | A budget, and no retry you have not described |

Pick one row. Two changes at once teach you nothing.

## 3. Make the smallest edit

Put the change in the skill or the schema, not in a longer pep talk.

| Edit | Example |
| --- | --- |
| A check | "Stop if the page has no source URL for a number." |
| A file | The wiki page that should have existed yesterday |
| A budget | "At most eight tool calls, then write the gap and stop." |
| A gate | Writes wait for a person. Reads stay available. |

Leave the model alone until the same task fails with the new check in place. Then you have evidence the step was not the problem.

## 4. Re-run only that task

Use the sheet in [score a run](score-a-run.md). Compare the new trace to the sentence you wrote in step 1. Pass means the thin step changed, not that the prose got warmer.

If it fails the same way, the check is in the wrong layer. A rule the page can overwrite will not hold. Standing rules stay in the system prompt or the skill. The [threat model](../07-security/threat-model.md) is the short version of that habit.

## 5. Write the diagnosis where the next person will look

One line in the log or on the wiki page: date, symptom, thin step, change. The next stuck run should start from that line. A fix that lives in a chat is the forgetful loop again.

## Checklist

- [ ] The symptom is a sentence with a tool or an artifact in it.
- [ ] You named one thin step.
- [ ] You changed one check, file, budget, or gate.
- [ ] You did not change the model in the same edit.
- [ ] You re-ran the same task.
- [ ] The diagnosis is written down.

## Check yourself

1. Why is "try a larger model" the second experiment, not the first?
2. Which row matches a run that reports a URL you cannot open?
3. Where does the one-line diagnosis go?

## Sources

The loop's failure table is on [the agent loop](../00-foundations/the-agent-loop.md). Prompt injection, as a threat name, is on the [threat model](../07-security/threat-model.md). This playbook's order of fixes is synthesis.

## Continue

- [Score a run](score-a-run.md)
- [Write a skill](write-a-skill.md)
- [Find, review, fix, retest](../07-security/find-fix-retest.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
