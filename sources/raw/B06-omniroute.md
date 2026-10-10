# B6 · OmniRoute

| | |
| --- | --- |
| ID | B6 |
| Author | [@Bober_smart](https://x.com/Bober_smart) |
| Posted | 2026-10-08 |
| URL | https://x.com/Bober_smart/status/2108293657552117850 |
| Distilled in | [Gateways](../../docs/02-tools-mcp/gateways-and-routing.md), [case study](../../docs/08-case-studies/local-gateway.md) |

## What to take from it

A local OpenAI-compatible gateway that, per the post, pools free provider limits, falls back on 429 or quota errors, compresses context, encrypts keys locally, and supports MCP and agent-to-agent routing. The opening hook is a leak and a large free-token number.

## Claims to keep marked

| Claim | Status |
| --- | --- |
| Architecture rows (endpoint, clients, provider counts, 18 strategies, compression, AES-256-GCM, telemetry, MCP, launch options) | Per post |
| 800 million free tokens and the leak framing | Per post. Not a plan of record. |
| Project URL | Shortened in the post. Not guessed. |

## Links in the export

- https://x.com/Bober_smart/status/2108293657552117850/video/1
- https://twitter.com/bober_smart/status/2103462864870686848

## Original post text

The same string is the `text` field in [`bookmarks.json`](../bookmarks.json). It is copied here so the companion stands alone. Informal language is the post's.

<details>
<summary>Original text</summary>

HOLY SH*T! The person who leaked this online is a real freaking madman! Now everyone can get 800 million tokens for AI agents for free

The OmniRoute repository is blowing up GitHub. It is a local high-performance AI gateway that combines free limits from dozens of providers into a single continuous API stream

Project architecture and key technical specifications:

Interface and Integration: Provides a single OpenAI-compatible API endpoint. Natively connects to Cursor, VS Code (via Copilot / Cline / Aider) Claude Code, and custom scripts

Connection Scale: Supports 350+ providers and 90+ services with free limits (Google AI Studio, Groq, Cerebras, SambaNova, OpenRouter, GitHub Models, Mistral AI, etc.)

18 Routing Strategies & Auto-Fallback: Custom switching system. On a ⁠429 Too Many Requests⁠ error or quota depletion, the gateway seamlessly redirects the request to the next model in the chain within milliseconds

Dual Context Compression (RTK + Caveman): Built-in engines cut unnecessary logs, syntax, and message history by 15–95% saving token volume before sending the request

Security (Local-first & 0 Telemetry): All API keys are locally encrypted using the AES-256-GCM algorithm. Data goes directly to providers, bypassing third-party clouds

Agent Protocols (MCP & A2A): Full support for Model Context Protocol (MCP) and Agent-to-Agent architecture for automated model pool management

Launch Options: CLI (⁠npm⁠), Docker container, Electron desktop app, and PWA

https://t.co/aSAnBgx9HT

</details>
