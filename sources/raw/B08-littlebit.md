# B8 · LittleBit

| | |
| --- | --- |
| ID | B8 |
| Author | [@thesupermannx](https://x.com/thesupermannx) |
| Posted | 2026-10-08 |
| URL | https://x.com/thesupermannx/status/2108098865073410484 |
| Distilled in | [Efficient inference](../../docs/05-runtime-infra/efficient-inference.md) |

## What to take from it

Samsung's LittleBit, described in the post as sub-1-bit compression of a 13B model to under 1 GB, with XOR replacing matrix math and an 11.6x speedup. The paper's mechanism is latent factorization and binarized factors, which the inference page contrasts with the XOR sentence.

## Claims to keep marked

| Claim | Status |
| --- | --- |
| 13B under 1 GB, 0.1 bits per weight, 11.6x vs FP16 | Per post. The paper's abstract is close, with different qualifiers. |
| Bitwise XOR as the core operation | Per post. Diverges from the paper's description. |

## Links in the export

- https://x.com/thesupermannx/status/2108098865073410484/photo/1

## Original post text

The same string is the `text` field in [`bookmarks.json`](../bookmarks.json). It is copied here so the companion stands alone. Informal language is the post's.

<details>
<summary>Original text</summary>

Samsung open-sourced a method that shrinks 13B parameter LLM into less than 1 GB.

It's called "LittleBit"

Instead of storing AI weights as standard numbers, they used latent factorization to crush them down to extreme sub-1-bit levels.

In some configurations, they hit 0.1 bits per weight.

But here is where the architecture gets crazy.

When you compress an AI this much, you can stop doing math.

Instead of forcing the hardware to do heavy floating-point multiplication, LittleBit replaces the core computation with a bitwise XOR operation.

It swaps complex matrix math for basic sign flips.

The results rewrite the rules of model deployment:

• Unlocks a massive 11.6x inference speedup relative to standard FP16 models.

• Radically reduces memory footprint and loading bandwidth.

• Maintains robustness in extreme sub-0.5 bit regimes where previous compression methods catastrophically fail.

This is not a clever optimization.

It is the blueprint for running massive, state-of-the-art AI locally on cheap, resource-constrained devices.

</details>
