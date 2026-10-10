# Source dossier

> **Editorial note.** This file is the seed research note, kept raw. Bookmark IDs in section 1 are the source of truth. The theme list in section 2 swaps B7 (Antigen, security) and B8 (LittleBit, compression). The guide follows section 1. Performance figures and product claims stay marked **per post**.

# agentsphere — Research Dossier (seed)

Source: @blerbznews X bookmarks. X API gives no bookmark timestamps, so I filtered by post date >= 2026-10-08 (Oct 8–10, 2026). The 10 matches are also the 10 most recent bookmarks in order. Claims below come from the posts and are unverified; cite them as 'per post'.

## 1. Bookmarks

### B1. @oliviscusAI — 2026-10-10
- URL: https://x.com/oliviscusAI/status/2108786434991923251
- Links: https://x.com/oliviscusAI/status/2108786434991923251/video/1

> Microsoft just changed the game 🤯
> 
> They've open-sourced bitnet.cpp, a 1-bit LLM inference framework.
> 
> It let's you run 100B parameter models on your local CPU without GPUs.
> 
> - 6.17x faster inference
> - 82.2% less energy on CPUs
> 
> 100% Open Source. https://t.co/rSXJSTh36P

### B2. @fleyta88 — 2026-10-09
- URL: https://x.com/fleyta88/status/2108619644399415565
- Links: https://x.com/fleyta88/status/2108619644399415565/video/1, https://twitter.com/gippp69/status/2106744347836153989

> this is certified f**king gold
> 
> Andrej Karpathy just showed a cleaner way to build research agents, and it kills the dumbest loop in AI:
> 
> search → answer → forget → search again
> 
> he basically turns memory into a real system:
> 
> raw sources stay raw  
> the agent reads them once  
> turns the useful parts into linked wiki pages  
> then checks the wiki first every time a new question comes in
> 
> so the loop changes:
> 
> > question comes in  
> > wiki gets searched first  
> > gaps send the agent back to source material  
> > the answer gets written back into the wiki  
> > the system leaves the next run smarter than the last one
> 
> that’s the trick
> 
> the “memory” is not buried in some giant chat transcript anymore
> 
> it lives in files the agent can actually work with:
> > pages it can read  
> > links it can follow  
> > notes it can update  
> > gaps it can spot  
> > stale claims it can fix
> 
> after enough runs, you stop getting one-off answers
> 
> you get an actual knowledge base
> 
> that’s why this feels bigger than just “better RAG”
> 
> a normal research agent can handle 100 questions and leave behind 100 dead chats
> 
> Karpathy’s setup can handle the same 100 questions and leave behind a research system that compounds
> 
> the architecture is stupidly simple:
> 
> > raw/ = source of truth  
> > wiki/ = maintained knowledge  
> > schema = rules for how the whole thing gets updated
> 
> search still matters
> 
> it just stops being the whole product
> 
> that’s the part I’d steal immediately:
> 
> don’t make the agent remember harder
> 
> make it write something worth remembering

### B3. @ai_explorer25 — 2026-10-10
- URL: https://x.com/ai_explorer25/status/2108746842620014807
- Links: none

> Best 15 accounts to follow in AI:
> 
> @karpathy = LLMs king
> @steipete = built openclaw
> @gregisenberg  = startup ideas king
> @rileybrown= vibecode king
> @jackfriks = solo apps king
> @levelsio= startups king
> @marclou = startups king
> @EXM7777  = AI ops + systems king
> @eptwts   = AI money twitter king
> @ai_explorer25= AI queen
> @godofprompt  =prompt king
> @vasuman   = AI agents king
> @AmirMushich = AI ads king
> @0xROAS = AI UGCs king
> @egeberkina = AI images king
> 
> Follow them all and learn.

### B4. @ClaudeDevs — 2026-10-09
- URL: https://x.com/ClaudeDevs/status/2108591328732856655
- Links: https://x.com/ClaudeDevs/status/2108591328732856655/video/1

> Claude Managed Agents dynamic workflows are now available in public beta. It's a new type of multiagent orchestration, built for your most ambitious workloads.
> 
> A lead agent writes a plan that runs across many agents in phases, combining the results at the end. https://t.co/hEExShsVku

### B5. @himanshubuildss — 2026-10-09
- URL: https://x.com/himanshubuildss/status/2108540618553356666
- Links: https://scrolltide.co, https://x.com/himanshubuildss/status/2108540618553356666/video/1

> 10 goldmines for anyone building websites with AI 👀
> 
> 1. 👑 https://t.co/RlChWqggj8 
> 600+ award-winning prompts + full source code for 3D and scroll-driven sites. 100+ 3D scenes, 200+ interactive gradients, 200+ UI components. Copy the prompt. Paste into Claude, Cursor or Lovable. Launch live.
> 
> 2. https://t.co/9FlWM4hqJb - hand-picked sites with serious craft
> 3. https://t.co/qeCSncdyPP - the sites that actually won
> 4. https://t.co/wl4RgkJCgh - real app flows from real products
> 5. https://t.co/ZNFmqbqGsp - every UI component, across design systems
> 6. https://t.co/p6pXo8hFRn - community components, ready to drop in
> 7. https://t.co/nxASYyVHLH - animated components, big visual impact
> 8. https://t.co/MIhQHgyUPK - motion components, ready to paste
> 9. https://t.co/u7On2CIuL1 - shaders to study and remix
> 10. https://t.co/nk12i7IbXV - the best way to learn 3D on the web
> 
> Save this 🔖 you'll need it before your next project.
> 
> Which one would you build first?

### B6. @Bober_smart — 2026-10-08
- URL: https://x.com/Bober_smart/status/2108293657552117850
- Links: https://x.com/Bober_smart/status/2108293657552117850/video/1, https://twitter.com/bober_smart/status/2103462864870686848

> HOLY SH*T! The person who leaked this online is a real freaking madman! Now everyone can get 800 million tokens for AI agents for free
> 
> The OmniRoute repository is blowing up GitHub. It is a local high-performance AI gateway that combines free limits from dozens of providers into a single continuous API stream
> 
> Project architecture and key technical specifications:
> 
> Interface and Integration: Provides a single OpenAI-compatible API endpoint. Natively connects to Cursor, VS Code (via Copilot / Cline / Aider) Claude Code, and custom scripts
> 
> Connection Scale: Supports 350+ providers and 90+ services with free limits (Google AI Studio, Groq, Cerebras, SambaNova, OpenRouter, GitHub Models, Mistral AI, etc.)
> 
> 18 Routing Strategies & Auto-Fallback: Custom switching system. On a ⁠429 Too Many Requests⁠ error or quota depletion, the gateway seamlessly redirects the request to the next model in the chain within milliseconds
> 
> Dual Context Compression (RTK + Caveman): Built-in engines cut unnecessary logs, syntax, and message history by 15–95% saving token volume before sending the request
> 
> Security (Local-first & 0 Telemetry): All API keys are locally encrypted using the AES-256-GCM algorithm. Data goes directly to providers, bypassing third-party clouds
> 
> Agent Protocols (MCP & A2A): Full support for Model Context Protocol (MCP) and Agent-to-Agent architecture for automated model pool management
> 
> Launch Options: CLI (⁠npm⁠), Docker container, Electron desktop app, and PWA
> 
> https://t.co/aSAnBgx9HT

### B7. @antigenco — 2026-10-08
- URL: https://x.com/antigenco/status/2108334286978113634
- Links: https://x.com/antigenco/status/2108334286978113634/video/1

> Introducing Antigen: the offensive security agent that maps, exploits, and secures your attack surface.
> 
> It probes your system like a hacker, ships fixes for your team's review, and tests again to ensure all vulnerabilities are patched. https://t.co/ej2wytDEAw

### B8. @thesupermannx — 2026-10-08
- URL: https://x.com/thesupermannx/status/2108098865073410484
- Links: https://x.com/thesupermannx/status/2108098865073410484/photo/1

> Samsung open-sourced a method that shrinks 13B parameter LLM into less than 1 GB.
> 
> It's called "LittleBit"
> 
> Instead of storing AI weights as standard numbers, they used latent factorization to crush them down to extreme sub-1-bit levels.
> 
> In some configurations, they hit 0.1 bits per weight.
> 
> But here is where the architecture gets crazy.
> 
> When you compress an AI this much, you can stop doing math.
> 
> Instead of forcing the hardware to do heavy floating-point multiplication, LittleBit replaces the core computation with a bitwise XOR operation.
> 
> It swaps complex matrix math for basic sign flips.
> 
> The results rewrite the rules of model deployment:
> 
> • Unlocks a massive 11.6x inference speedup relative to standard FP16 models.
> 
> • Radically reduces memory footprint and loading bandwidth.
> 
> • Maintains robustness in extreme sub-0.5 bit regimes where previous compression methods catastrophically fail.
> 
> This is not a clever optimization.
> 
> It is the blueprint for running massive, state-of-the-art AI locally on cheap, resource-constrained devices.

### B9. @N01ennn — 2026-10-08
- URL: https://x.com/N01ennn/status/2108182955671580771
- Links: https://github.com/whaleyxbt/claude-motion, https://x.com/N01ennn/status/2108182955671580771/video/1, https://twitter.com/n01ennn/status/2107826459804840072

> this is pure f*cking treasure
> 
> Netflix engineers posted 20 GitHub repos that turn your Opus 5.5 into a f*cking motion empire:
> 
> built for Opus 5.5
> 
> 1. claude-motion: taste, checks its own frames, sound written in code. the author built it for Opus 5.5  
> https://t.co/TtBtU2nVrN
> 
> 2. claude-motion-design: HTML, Playwright and ffmpeg, no Remotion. the demo was made on Opus 5.5  
> https://t.co/iOsyrWUvKE
> 
> 3. motion-graphics-skills: 13 skills for launch videos. the README tells you to run it on Opus 5.5  
> https://t.co/yNZhCZO8wT
> 
> 4. claude-remotion-skill: a Remotion editor from one prompt. captions, B-roll, sound  
> https://t.co/immhzwVP5i
> 
> 5. klik-anim-skill-creation: the laws of animation and camera, built on Opus  
> https://t.co/XWqUnn4v7o
> 
> 6. hyperframes-motion-reel-skill: a showreel cut to the beat at 120 BPM, on HyperFrames  
> https://t.co/E96s10io4Q
> 
> 7. product-launch-motion: a full launch film. voice-over, camera, color grade  
> https://t.co/VBfllJ6j1K
> 
> 8. animate: a short clip in one canvas file, storyboarded as it goes  
> https://t.co/xafT2UPXUe
> 
> 9. motion-design-skills: timing, color, typography, logos, Remotion  
> https://t.co/gKUqO9P2Xe
> 
> 10. hyperframes-student-kit: 14 skills and 406 motion graphics cards  
> https://t.co/fJmzb9I5z0
> 
> the engines these skills render with
> 
> 11. hyperframes: HTML to MP4. the one almost everyone installs  
> https://t.co/4rIffGKusx
> 
> 12. remotion: video written in React  
> https://t.co/o5zRdBgcS0
> 
> 13. remotion skills: the official Remotion skills for your agent  
> https://t.co/EieoL5Quaq
> 
> 14. GSAP: the timelines HyperFrames runs on. skills: npx skills add greensock/gsap-skills  
> https://t.co/LYRTAx5wvF
> 
> taste and everything around it
> 
> 15. motion-design-skill: motion principles that work with any engine  
> https://t.co/Vgr318UX9h
> 
> 16. awesome-motion-design-agent-skills: a map of GSAP, Remotion, Lottie and Rive skills  
> https://t.co/hF0ZxWyjcI
> 
> 17. motion-graphics: B-roll built straight from your transcript  
> https://t.co/Gwi9SKlS9C
> 
> 18. motion-dev-animations-skill: web animation on https://t.co/V19R87wQid, not video  
> https://t.co/YOL7zHaCB5
> 
> 19. motion: Motion itself, formerly Framer Motion  
> https://t.co/Jp9AReFaWe
> 
> 20. lottie-web: when you need Lottie, not MP4  
> https://t.co/TEG0FY4vFg
> 
> the stack in one line: Opus 5.5 writes the code, a skill sets the timing and the camera, an engine renders the MP4.
> 
> check each repo before you install. save this.

### B10. @ryancarson — 2026-10-08
- URL: https://x.com/ryancarson/status/2108286700468191266
- Links: none

> If your company or startup is running engineering with everyone using their own license of Codex/CC then you're going to be completely left behind by fast moving teams who are using cloud-based agents.
> 
> Local dev is like banging rocks together and grunting versus being on a rocket.
> 
> Seriously, just pay the money for something like @DevinAI, @AmpCode, @FactoryAI, etc.
> 
> Do NOT try to build your own "code factory".
> 
> Props to @DaleSpoonemore for taking @HelloUntangle to the next level on this. Fun to watch.

## 2. Themes
- **Agent memory and knowledge systems** (B2): Karpathy-style wiki memory. Raw sources are read once and turned into linked wiki pages, and the wiki is checked first on each question. Answers get written back, so it compounds. This is agentsphere's own operating model.
- **Multi-agent orchestration** (B4): Claude Managed Agents dynamic workflows, public beta. A lead agent writes a phased plan that runs across many agents and merges the results.
- **Cloud/background coding agents vs local** (B10): Ryan Carson argues for cloud agents (Devin, Amp, Factory) over per-seat local Codex/Claude Code, and against building your own "code factory".
- **Skills and creative agent toolkits** (B9, B5): Claude motion/animation skill repos (claude-motion etc.) and prompt/component libraries for building websites with AI.
- **Efficient/local inference** (B1, B7): bitnet.cpp 1-bit inference on CPU, and Samsung LittleBit sub-1-bit compression.
- **Gateways and model routing** (B6): OmniRoute, an OpenAI-compatible local gateway that pools free provider limits. Caution: provider ToS and security.
- **Agent security** (B8): Antigen offensive-security agent that maps, exploits, fixes, and retests.
- **Ecosystem/people** (B3): a list of accounts to follow. Low-signal, so it goes in a community appendix.

## 3. Proposed repo architecture
```
README.md                hero banner, logo, badges, nav, learning paths
assets/                  logo.svg, banner.svg, diagrams/*.svg
docs/00-foundations/     what is an agent: loop, tools, memory, planning
docs/01-agent-patterns/  ReAct-style loops, wiki-memory (B2), plan-and-execute
docs/02-tools-mcp/       tools, MCP, gateways/routing (B6)
docs/03-prompting-skills/ prompts, skills packages (B9, B5)
docs/04-multi-agent/     orchestration, lead/worker phases (B4)
docs/05-runtime-infra/   cloud vs local agents (B10), efficient inference (B1, B7)
docs/06-evals/           evaluating agents (stub for future bookmarks)
docs/07-security/        agent threat model, offensive-security agents (B8), gateway risks
docs/08-case-studies/
docs/09-playbooks/       power-user recipes
docs/glossary.md
sources/bookmarks.md     index of every bookmark -> pages that cite it
sources/ADDING_BOOKMARKS.md
CHANGELOG.md, CONTRIBUTING.md
```
The repo should follow the B2 pattern itself: raw sources go in sources/, distilled pages in docs/, and each new bookmark updates the wiki.

## 4. Learning paths
1. **Explorer**: foundations, glossary, agent loop diagram.
2. **Builder**: tools/MCP, prompting/skills, memory patterns.
3. **Operator**: cloud agents, multi-agent orchestration, evals, security.
4. **Power user**: playbooks, case studies, contributing sources back.

## 5. Visual identity brief
- Name treatment: lowercase `agentsphere`, with the "o" in agent space rendered as an orbit/sphere glyph.
- Palette: deep space #0B0F1A, electric indigo #6C5CE7, cyan #00D1FF, signal mint #2EF2A6, soft white #E6EAF2.
- Logo: a wireframe sphere with 3 orbiting nodes (agents) linked by arcs. Flat SVG with a gradient stroke.
- Banner: dark gradient field, sphere on the left, wordmark plus tagline "The living field guide to the agent era".
- Diagrams: (1) agent loop; (2) wiki-memory compounding loop (B2); (3) lead-agent phased orchestration (B4); (4) local vs cloud agent topology (B10); (5) gateway routing (B6); (6) agent security find-fix-retest loop (B8); (7) repo knowledge flow: bookmark -> source -> doc.
