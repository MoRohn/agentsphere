# B2 · Wiki memory

| | |
| --- | --- |
| ID | B2 |
| Author | [@fleyta88](https://x.com/fleyta88) |
| Posted | 2026-10-09 |
| URL | https://x.com/fleyta88/status/2108619644399415565 |
| Distilled in | [Wiki memory](../../docs/01-agent-patterns/wiki-memory.md), [case study](../../docs/08-case-studies/compounding-wiki.md) |

## What to take from it

A research-agent workflow attributed to Andrej Karpathy. Raw sources stay raw, useful parts become linked wiki pages, and the wiki is searched first. Answers are written back so the next run is smarter. The post names raw/, wiki/, and a schema.

## Claims to keep marked

| Claim | Status |
| --- | --- |
| Attribution to Karpathy and the demonstration | Per post. No primary URL in the export. |
| raw/ , wiki/ , schema | Per post |
| Search the wiki first; gaps return to sources; write the answer back | Per post |
| Bigger than better RAG | Per post, as the poster's judgment |

## Links in the export

- https://x.com/fleyta88/status/2108619644399415565/video/1
- https://twitter.com/gippp69/status/2106744347836153989

## Original post text

The same string is the `text` field in [`bookmarks.json`](../bookmarks.json). It is copied here so the companion stands alone. Informal language is the post's.

<details>
<summary>Original text</summary>

this is certified f**king gold

Andrej Karpathy just showed a cleaner way to build research agents, and it kills the dumbest loop in AI:

search → answer → forget → search again

he basically turns memory into a real system:

raw sources stay raw  
the agent reads them once  
turns the useful parts into linked wiki pages  
then checks the wiki first every time a new question comes in

so the loop changes:

> question comes in  
> wiki gets searched first  
> gaps send the agent back to source material  
> the answer gets written back into the wiki  
> the system leaves the next run smarter than the last one

that’s the trick

the “memory” is not buried in some giant chat transcript anymore

it lives in files the agent can actually work with:
> pages it can read  
> links it can follow  
> notes it can update  
> gaps it can spot  
> stale claims it can fix

after enough runs, you stop getting one-off answers

you get an actual knowledge base

that’s why this feels bigger than just “better RAG”

a normal research agent can handle 100 questions and leave behind 100 dead chats

Karpathy’s setup can handle the same 100 questions and leave behind a research system that compounds

the architecture is stupidly simple:

> raw/ = source of truth  
> wiki/ = maintained knowledge  
> schema = rules for how the whole thing gets updated

search still matters

it just stops being the whole product

that’s the part I’d steal immediately:

don’t make the agent remember harder

make it write something worth remembering

</details>
