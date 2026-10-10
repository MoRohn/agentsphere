# Adding a bookmark

Open this beside the files you are editing. The reasons for each step live in [CONTRIBUTING](../CONTRIBUTING.md).

## Checklist

- [ ] Next ID assigned (`B11`, then `B12`, …)
- [ ] Object appended to [`bookmarks.json`](bookmarks.json) with `id`, `author`, `created`, `url`, `links`, `text`
- [ ] `links` contains only URLs the export actually resolved
- [ ] Companion written at `sources/raw/B11-slug.md` from the template below
- [ ] Row added to [`bookmarks.md`](bookmarks.md), with every page that cites it
- [ ] Existing pages searched before a new page was created
- [ ] Concept page updated or added, with a claim table
- [ ] **Per post** used for anything not checked against a primary source
- [ ] Shortened links left unexpanded
- [ ] Glossary, map, and learning path updated if the reader would otherwise get lost
- [ ] SVG and Mermaid updated together if an architecture changed
- [ ] [CHANGELOG](../CHANGELOG.md) updated
- [ ] Relative links and both diagram forms checked

## Raw companion template

Save as `sources/raw/B11-short-slug.md`.

```markdown
# B11 · Short title

| | |
| --- | --- |
| ID | B11 |
| Author | [@handle](https://x.com/handle) |
| Posted | YYYY-MM-DD |
| URL | https://x.com/handle/status/… |
| Resolved links | none, or a real list |
| Distilled in | [Page](../../docs/…/page.md) |

## What to take from it

Three to six sentences. The idea, not the hype.

## Claims to keep marked

| Claim | Status |
| --- | --- |
| … | Per post |

## Original post text

The archive copy is the `text` field in [`bookmarks.json`](../bookmarks.json). Paste it below so a reader can open one file. Do not clean it up.

> pasted text
```

## Where a bookmark usually goes

| If the post is about | Update |
| --- | --- |
| Memory, notes, wikis, RAG | [wiki memory](../docs/01-agent-patterns/wiki-memory.md) |
| Tools, MCP, routing, gateways | [tools](../docs/02-tools-mcp/index.md) |
| Prompts, skills, design stacks | [skills](../docs/03-prompting-skills/index.md) |
| Many agents, plans, phases | [orchestration](../docs/04-multi-agent/orchestration.md) |
| Cloud, local, models, cost | [runtime](../docs/05-runtime-infra/index.md) |
| Tests, scores, regressions | [evals](../docs/06-evals/index.md) |
| Safety, review, keys, supply chain | [security](../docs/07-security/index.md) |
| A list of people | [community](../docs/community.md) |
| A story worth retelling | [case studies](../docs/08-case-studies/index.md) |
| A procedure the reader can run | [playbooks](../docs/09-playbooks/index.md) |

A single bookmark often updates one concept page and adds a row to an existing case study. That is the expected case.
