<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/diagrams/wiki-memory-dark.svg">
  <img src="../../assets/diagrams/wiki-memory-light.svg" alt="Wiki memory" width="100%">
</picture>
</p>

<p>
  <img src="../../assets/badges/level-power.svg" alt="Power user" height="28">
</p>

# Playbook · Research agent

Stand up the smallest version of raw, wiki, and schema. Use it on a question you actually have.

| | |
| --- | --- |
| Path | Power user |
| Time | About 90 minutes the first time |
| You need | [Wiki memory](../01-agent-patterns/wiki-memory.md) |
| Produces | A folder layout, five rules, and one page written from a real source |

This is synthesis on top of [@fleyta88](https://x.com/fleyta88/status/2108619644399415565). The post names the three pieces. The files below are a concrete way to keep them. They are not a recovered Karpathy repository.

## 1. Make the folders

```text
research/
  raw/                 evidence, append-only
    inbox/             posts, pdfs, clips, as they arrived
  wiki/                maintained pages
    index.md
    log.md             one line per run: date, question, pages touched
  SCHEMA.md            the rules below
```

Keep `raw/` boring. A file's name can include the date and the author. Do not summarize inside `raw/`. The summary is a wiki page.

## 2. Write the schema on one screen

Put these rules in `SCHEMA.md`. Edit them when they fail you. Do not keep a second copy in a chat.

1. Search `wiki/` before opening `raw/`.
2. If the wiki answers, say so in `log.md` and stop.
3. If it does not, read the smallest raw set that could answer, then write or update one page.
4. Every non-obvious claim on that page has a source path or URL, and a status: established or per post.
5. Gaps are a heading, not an absence. Stale claims get corrected in place, with the new source, and the old source stays linked.
6. `raw/` is not rewritten to match the conclusion.
7. Stop when the page exists and the log line is written. A second pass needs a new question.

## 3. Give the agent a standing prompt

Short on purpose:

```text
You are maintaining research/wiki using research/SCHEMA.md.
Search the wiki before the raw files.
Write the answer back into a page before you stop.
Mark claims you cannot verify as per post.
Do not invent URLs, numbers, or repository names.
```

The procedure lives in the schema. The prompt only points at it. That split is [prompts and skills](../03-prompting-skills/prompts-and-skills.md).

## 4. Run one question

Pick a question you cannot answer from memory. A good first question, if you are using this repository as the corpus: "What does the OmniRoute post claim about keys, and what has this guide refused to confirm?"

Watch the trajectory.

| You want to see | You want to stop the run if |
| --- | --- |
| A wiki search first | It opens raw files before looking |
| One page updated | It answers only in the chat |
| A gap written down | It fills the gap with a plausible URL |
| A log line | It starts a second, unrequested research pass |

## 5. Ask the same question tomorrow

The second run is the eval. It should search the wiki and get cheaper. If it re-reads everything, the page is in the wrong shape: the answer is buried, or the title would not match a search. Fix the page, not the model. The regression cases live in [evals](../06-evals/index.md).

## 6. Cite it the way this guide does

When the source is someone else's post, link the status, mark the claim **per post**, and add the post to [Social references & inspirations](../references.md) if it shaped a page. The rules are in [CONTRIBUTING](../../CONTRIBUTING.md). Your personal wiki can be looser. The moment other people will read it, use the same claim labels.

## Check yourself

1. Which directory is append-only?
2. What does the second run have to do differently from the first?
3. Where do the rules live, and where do they not live?

## Sources

- [@fleyta88](https://x.com/fleyta88/status/2108619644399415565) — the three-piece pattern, per post.
- The folder names, the seven rules, and the prompt are synthesis.

## Continue

- [How agents remember](../01-agent-patterns/how-agents-remember.md)
- [Skills and craft](skills-and-craft.md)
- [Compounding wiki case study](../08-case-studies/compounding-wiki.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
