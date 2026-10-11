# Changelog

The guide version tracks the pages. Dates are the day the change landed in this repository.

## 0.4.5 — 2026-10-11

- Opened each section in plain language, matching the map cards. The two lists of six parts now say how they differ. Evals, security, and hosted agents define their words in the first paragraph.

## 0.4.4 — 2026-10-11

- Rewrote the README opening in plain language. The four level pills are the first choice. The harness is explained before it is used.
- Every guide page now says where you are and what to open next.
- The level diagram says what you leave with: try one safely, leave a page, leave a score, change one thing.

## 0.4.3 — 2026-10-11

- Rewrote [Explorer](paths/explorer/README.md) in plain language: what an agent is, what one can do today, four products you can try, a ten-minute walkthrough, good instructions, and how to stay safe.
- Replaced the README map with linked cards. Each card has an icon, a plain one-line description, and the section's level pill.

## 0.4.2 — 2026-10-11

- The four README pills link to dedicated guides: [Explorer](paths/explorer/README.md), [Builder](paths/builder/README.md), [Operator](paths/operator/README.md), and [Power user](paths/power-user/README.md). Each guide has its own route, exercises, checklist, and diagram.

## 0.4.1 — 2026-10-11

- Replaced the hand-drawn logo with the owner's artwork. The masthead, the icon, and the marks on section headers are cropped from that art, with the background removed. Light pages use the navy crescent. Dark pages use the white crescent and the glow on `sphere`. The README chooses them with `<picture>`.

## 0.4.0 — 2026-10-11

- Added [Hosted agents](docs/10-hosted-agents/index.md): Grok Bot, Muse, Dots, Claude Cowork, and Copilot Studio computer use, each mapped onto the six harness parts. Facts come from official pages opened on this date. Where two official pages disagree, both are kept. Dollar prices are omitted.
- Linked the section from the README, the guide map, the diagram atlas, the learning paths, harness engineering, and cloud and local.
- Redrew the masthead, section openers, and every diagram at an 830-wide viewBox, with titles at 36px and labels at 16px or larger. Each figure is a transparent light file and a transparent dark file, chosen with `<picture>`.
- Replaced the orb with the robot mark. Light art uses the orange disc and navy crescent. Dark art uses the navy disc and orange glow. The wordmark is outlined `Agentsphere`, with the tagline `AI AGENTS REPOSITORY` between orange rules. The guide palette is navy and orange.

## 0.3.0 — 2026-10-11

- Added a start-here path and a "if you need to" index so a newcomer can move from a definition to a finished agent card.
- Added four playbooks: your first agent, write a skill, score a run, and unstick a loop. Each one ends in a checklist and an artifact.
- Pointed every section at the playbook that practices it. Learning paths now end with that artifact.
- Added a filled wiki page on the memory pattern, and aligned diagram headers with the mark.
- Rebuilt how a research agent keeps what it learns: a six-step loop, a map of working, episodic, semantic, and procedural memory, and a chapter on write-back, reflection, compaction, and when to forget.
- Added harness engineering from Guo et al. 2026: the model-plus-harness thesis, six runtime parts, four eras, task-to-harness matching, and the survey's SWE-bench Verified reading.
- Citations name the author and link the source. Internal reference codes are gone.
- Put harness engineering on the front door: a hero diagram, the landscape map, the four-level journey, and a five-minute start. Level badges mark every guide page.

## 0.2.0 — 2026-10-11

- Redrew the mark and the masthead. The name is one word. Light and dark variants ship together.
- Collected the posts, articles, and repositories that shaped the pages under [Social references & inspirations](docs/references.md).
- Rewrote the contribution guide around pages, citations, and diagrams.

## 0.1.0 — 2026-10-10

First public version of agentsphere.

- Added the field-guide structure: foundations, patterns, tools and MCP, prompting and skills, multi-agent orchestration, runtime, evals, security, case studies, and playbooks.
- Added four learning paths: Explorer, Builder, Operator, and Power user.
- Cited the posts and primary sources the pages rely on. Claims from posts are marked **per post** and linked.
- Added section art and architecture diagrams under `assets/`, with Mermaid twins for the agent loop, wiki memory, MCP, gateway routing, phased orchestration, cloud and local runs, the security loop, and the research loop.
- Evals is a working primer. The references do not yet include an evaluation write-up, so that section teaches established practice.

## Unreleased

Nothing yet. The next entry should name the pages that changed and any new sources.
