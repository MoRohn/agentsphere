<p align="center">
  <img src="../../assets/sections/03-skills.svg" alt="Skills" width="100%">
</p>

# Playbook · Skills and craft

Choose one skill and one engine from the catalogs. Review them. Make one small artifact.

| | |
| --- | --- |
| Path | Power user |
| Time | About an hour, plus whatever the renderer needs |
| You need | [Creative toolkits](../03-prompting-skills/creative-toolkits.md) |
| Produces | A reviewed choice, and one short artifact or a written rejection of the pack |

## 1. Name the artifact before the tool

Write one sentence: "A 10-second title card for agentsphere," or "One scroll section with a headline and a diagram." If you cannot name it, you are collecting tools.

## 2. Pick from the lists, narrowly

| Job | Pick | Leave |
| --- | --- | --- |
| Motion | One engine (the post groups HyperFrames, Remotion, GSAP, Motion, Lottie) and one skill | The other eighteen names |
| A website section | [scrolltide.co](https://scrolltide.co) or one link you open from the [source post](https://x.com/himanshubuildss/status/2108540618553356666) | The other nine, until this one has taught you something |

The names and the unresolved links are on the concept page. Only [claude-motion](https://github.com/whaleyxbt/claude-motion) was resolved for the motion list.

## 3. Review before install

Answer on a note, from the files, not from the README's adjectives.

| Question | Answer you can accept |
| --- | --- |
| What does the install command execute? | You read it |
| Which commit will you pin? | A specific revision |
| What tools does the skill tell the agent to call? | A list you would show a teammate |
| Does any line tell the agent to ignore other instructions? | If yes, stop |
| Does the environment you will use contain production keys? | It should not |
| What is the renderer, and where does the output file go? | You can point at both |

The motion post says to check each repo before you install ([B9](https://x.com/N01ennn/status/2108182955671580771), per post). This table is the check. More context: [supply chain](../07-security/gateway-and-supply-chain.md).

## 4. Write a small brief

```text
Artifact: 10-second title card.
On screen: the word agentsphere, the tagline, the three orbit nodes.
Skill: the one you reviewed.
Engine: the one you reviewed.
Checks: duration, readable type on a dark ground, no extra logos.
Done when: a file exists and you have watched it.
```

Put the brief in a file. Point the agent at the skill. Keep your standing rules in the system prompt, not inside the brief.

## 5. Watch the trajectory

| Keep | Rework |
| --- | --- |
| It followed the skill's checks | It invented a second framework halfway |
| The output is the file you named | The output is a description of a file |
| You can see timing or layout decisions | The prompt was only "make it premium" |

If the pack fails the review in step 3, the artifact for this playbook is the rejection note. That counts. You practiced the gate.

## Check yourself

1. How many engines are you allowed to add before the first artifact exists?
2. Which motion URL can you cite from the export without opening the post?
3. What is a successful outcome if the skill tells the agent to ignore its other rules?

## Sources

- [B9](https://x.com/N01ennn/status/2108182955671580771) and [B5](https://x.com/himanshubuildss/status/2108540618553356666), per post.
- The review table and the brief are synthesis.

## Continue

- [Operate agents](operate-agents.md)
- [Motion and web stacks](../08-case-studies/motion-and-web-stacks.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [Sources](../../sources/bookmarks.md)
