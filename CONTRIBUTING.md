# Contributing

agentsphere grows when someone adds a bookmark and writes it back into the guide. This file is the schema: the rules for how raw sources become maintained pages. The short checklist, meant to sit open while you edit, is [sources/ADDING_BOOKMARKS.md](sources/ADDING_BOOKMARKS.md).

The shape of the repo is the shape of the memory pattern in [wiki memory](docs/01-agent-patterns/wiki-memory.md).

| Path | Role | You may |
| --- | --- | --- |
| `sources/raw/` and `sources/bookmarks.json` | Source of truth | Append a bookmark. Leave old text alone. |
| `docs/` | Maintained knowledge | Add a page, correct a stale claim, add a link. |
| `assets/` | Diagrams and identity | Add or update a figure when the architecture changes. |
| `CHANGELOG.md` | History of the guide | Add an entry for every distilled change. |

## Principles

1. **Raw stays raw.** The post text in `sources/bookmarks.json` is the archive. A readable companion lives in `sources/raw/`. Do not silently rewrite either one to match a later conclusion.
2. **The wiki is allowed to change.** When a later source corrects an earlier page, edit the page and leave a dated note. Link both sources.
3. **Cite the URL.** Every claim that comes from a bookmark points at the post. Use the bookmark ID (`B11`, `B12`, …).
4. **Mark the claim.** Use **Established**, **Per post**, or **Synthesis**, as defined in [how to read](docs/how-to-read.md). A number, a repo count, a speedup, or a product feature from a post is **per post** until a primary source is opened and named.
5. **Do not invent the missing link.** Shortened `t.co` URLs in a post are not reconstructed by guessing. If the export already resolved a URL, use that. Otherwise send the reader to the post.
6. **One idea, one home.** Prefer updating an existing page to opening a near-duplicate. A case study may retell a bookmark, and it should link to the concept page rather than fork the explanation.
7. **Search the guide first.** Before you add a page, look in [the map](docs/README.md), the [glossary](docs/glossary.md), and the [bookmark index](sources/bookmarks.md).
8. **Security stays high level.** Name threats, review gates, and supply-chain checks. Do not add exploit procedures, payloads, or steps for abusing provider quotas.
9. **Keep the visual system.** New figures use the palette and the header/footer pattern in [the style guide](docs/style-guide.md). Diagrams that explain an architecture exist twice: an SVG in `assets/diagrams/` and a Mermaid block on the page. Both must render on GitHub.
10. **Leave the next run smarter.** Update the bookmark index, the learning path if the sequence changed, the glossary if you introduced a term, and the changelog.

## Add a bookmark

1. Give it the next ID. The seed uses `B1` through `B10`. Continue at `B11`.
2. Append the object to `sources/bookmarks.json`. Keep the fields `id`, `author`, `created`, `url`, `links`, and `text`. `links` holds only URLs that were actually resolved.
3. Add `sources/raw/B11-short-slug.md` using the template in [ADDING_BOOKMARKS](sources/ADDING_BOOKMARKS.md).
4. Add a row to `sources/bookmarks.md`, including every page that will cite it.
5. Decide where the knowledge goes:
   - **Update** an existing concept page when the bookmark extends a topic the guide already teaches.
   - **Add** a page when the topic is new. Put it in the closest section, and add it to that section's `index.md` and to [docs/README.md](docs/README.md).
   - **Appendix** low-signal lists (accounts, link dumps without a method) in [community](docs/community.md) or a short case-study note, and say why they are low-signal.
6. On the concept page, write the idea in the guide's voice. Put the post's figures in a claim table. Link the post. If you checked a paper or an official repo, link that too and say what it supports.
7. If the bookmark changes an architecture the guide draws, update the SVG and the Mermaid block together. See the [diagram atlas](docs/diagrams.md).
8. Add a case-study page only when the story is useful on its own. Otherwise a section in an existing case study is enough.
9. Update [CHANGELOG.md](CHANGELOG.md) under `Unreleased`, then move that text into a version section when a batch ships.
10. Read the page on GitHub's preview, or locally, and confirm the SVG and the Mermaid block both render. Confirm every new relative link resolves.

## Page template

Copy this shape. It is what makes the guide feel like one book.

```markdown
<p align="center">
  <img src="../../assets/sections/0N-name.svg" alt="Section title" width="100%">
</p>

# Page title

One sentence a newcomer can repeat.

| | |
| --- | --- |
| Path | Explorer, Builder, Operator, or Power user |
| Time | About N minutes |
| You need | The previous page, or "nothing" |

## What you will be able to do

- Outcome, in the reader's hands

## Body

Teach the idea. Use a table for claims.

> [!NOTE]
> **Per post.** What was claimed, who said it, and the URL.

## Check yourself

1. A question the page answers.
2. A question that should send the reader back to a source.
3. A question about what this guide refuses to invent.

## Sources

- [B11](url) — author, date. One line on what was taken from it.

## Continue

- Previous: …
- Next: …

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [Sources](../../sources/bookmarks.md)
```

Section landing pages use the section SVG. Deep pages in the same section may reuse it or use the relevant diagram.

## Voice

Write to a capable reader who is new to the term you are defining. Define it on first use. Prefer short sections and tables. Keep hype in the source archive, and keep the page in plain sentences.

State the claim you mean. "The post reports a 6.17x speedup" is a different sentence from "Inference is 6.17x faster."

## Diagrams on GitHub

- SVG files are images. Reference them with an `<img>` tag and a real `alt`. Give them their own background so they read on GitHub's light and dark themes.
- Keep SVG self-contained: no scripts, no external fonts, no `foreignObject`. Use presentation attributes (`fill`, `stroke`, `font-family`) so a sanitizer that drops `<style>` still leaves a picture.
- Use `Segoe UI, Helvetica, Arial, sans-serif`.
- Mermaid blocks sit in a ` ```mermaid ` fence at the root of the page, not indented under a list. Stick to `flowchart`, `sequenceDiagram`, and `stateDiagram-v2`. Quote labels that contain parentheses, slashes, or colons. Do not use `end` as a node id.
- After a diagram change, open the file on GitHub and look at it. A diagram that only renders locally is unfinished.

## Palette

| Name | Hex | Use |
| --- | --- | --- |
| Deep space | `#0B0F1A` | Backgrounds |
| Electric indigo | `#6C5CE7` | Lead, planning, links |
| Cyan | `#00D1FF` | Perception, tools, focus |
| Signal mint | `#2EF2A6` | Memory written back, done, safe-to-proceed |
| Soft white | `#E6EAF2` | Primary text on the dark art |
| Slate | `#8B97B3` | Secondary text on the dark art |

The wordmark is lowercase `agentsphere`. The mark is a wireframe sphere with three linked nodes. On the banner, that sphere sits between `agent` and `sphere` as the brand's orbit glyph. Full notes: [style guide](docs/style-guide.md).
