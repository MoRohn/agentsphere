# B1 · bitnet.cpp

| | |
| --- | --- |
| ID | B1 |
| Author | [@oliviscusAI](https://x.com/oliviscusAI) |
| Posted | 2026-10-10 |
| URL | https://x.com/oliviscusAI/status/2108786434991923251 |
| Distilled in | [Efficient inference](../../docs/05-runtime-infra/efficient-inference.md), [case study](../../docs/08-case-studies/local-inference.md) |

## What to take from it

Microsoft open-sourced bitnet.cpp, described as a 1-bit LLM inference framework that runs very large models on CPU. The post gives two performance figures and says the project is fully open source.

## Claims to keep marked

| Claim | Status |
| --- | --- |
| 1-bit inference framework, open source | Per post. Official project is linked from the inference page as background. |
| 100B-parameter models on a local CPU without GPUs | Per post |
| 6.17x faster inference | Per post. The paper reports a range whose top end matches this on x86. |
| 82.2% less energy on CPUs | Per post |

## Links in the export

- https://x.com/oliviscusAI/status/2108786434991923251/video/1

## Original post text

The same string is the `text` field in [`bookmarks.json`](../bookmarks.json). It is copied here so the companion stands alone. Informal language is the post's.

<details>
<summary>Original text</summary>

Microsoft just changed the game 🤯

They've open-sourced bitnet.cpp, a 1-bit LLM inference framework.

It let's you run 100B parameter models on your local CPU without GPUs.

- 6.17x faster inference
- 82.2% less energy on CPUs

100% Open Source. https://t.co/rSXJSTh36P

</details>
