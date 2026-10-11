<p align="center">
  <img src="../../assets/sections/05-runtime.svg" alt="Runtime and infra" width="100%">
</p>

<p>
  <img src="../../assets/badges/level-operator.svg" alt="Operator" height="28">
</p>

# Efficient inference

Agents call models in a loop, so the cost of one forward pass is paid many times. Smaller, cheaper inference is why a local CPU, a laptop, or a fleet of agent runs can be in the conversation at all.

| | |
| --- | --- |
| Path | Operator |
| Time | About 20 minutes |
| You need | Comfort with the idea that a model's weights can be stored at lower precision |

## What you will be able to do

- Explain why agent workloads care about inference cost.
- Separate the bitnet.cpp post from the project's own paper and README.
- Separate the LittleBit post's mechanism story from the paper's.

## Why agents notice

A chat product pays for one reply. An agent pays for every step: plan, tool choice, observation, rewrite. Memory and orchestration multiply calls again. Three established reasons to care where the model runs:

| Reason | What you gain if the model can run nearby or cheaply |
| --- | --- |
| Cost | A long trajectory stays affordable |
| Latency | Tool loops feel interactive |
| Data boundary | Prompts that cannot leave a machine have a place to go |

Compression and 1-bit designs are one route. A gateway in front of cheap hosted models is another, covered in [gateways](../02-tools-mcp/gateways-and-routing.md). They solve different constraints.

## bitnet.cpp

**Established.** [bitnet.cpp](https://github.com/microsoft/BitNet) is Microsoft's open-source inference framework for 1-bit LLMs, including BitNet b1.58 models. The project documents CPU and GPU inference. Its README presents BitNet-b1.58-2B-4T, a 2.4B-parameter model, as the official model to try. The paper ["1-bit AI Infra"](https://arxiv.org/abs/2410.16144) reports CPU speedups ranging from 2.37x to 6.17x on x86, and 1.37x to 5.07x on ARM, across model sizes.

**Per post.** [@oliviscusAI](https://x.com/oliviscusAI/status/2108786434991923251) says Microsoft open-sourced bitnet.cpp, that it runs 100B-parameter models on a local CPU without GPUs, that inference is 6.17x faster, and that it uses 82.2% less energy. The post's project link is shortened. The GitHub link above is the official project.

| Figure | Where it stands |
| --- | --- |
| Open-source 1-bit inference framework | Established. Official repo. |
| 6.17x faster | The post states it as the result. The paper states a **range** on x86 whose top end is 6.17x. |
| 82.2% less energy | Per post. Not restated from the sources above. |
| 100B parameters on CPU, no GPU | Per post. The official README's headline model is 2.4B. |

> [!NOTE]
> **Read the range, not the slogan.** A speedup that is 6.17x at the top of a published range is a different fact from "inference is 6.17x faster" as a single number you can expect on your machine. Measure the model you actually run.

## LittleBit

**Established.** LittleBit is a Samsung Research compression method. The paper is [LittleBit: Ultra Low-Bit Quantization via Latent Factorization](https://arxiv.org/abs/2506.13771) (NeurIPS 2025). Code is at [SamsungLabs/LittleBit](https://github.com/SamsungLabs/LittleBit). Samsung's [research write-up](https://research.samsung.com/blog/LittleBit-Ultra-Low-Bit-Quantization-via-Latent-Factorization) describes the idea at the same altitude as the abstract: weight matrices are approximated by low-rank factors, those factors are binarized, and learned scales put magnitude back. The abstract's headline results include about 0.1 bits per weight, Llama 2 13B compressed to under about 0.9 GB, and a potential 11.6x inference speedup relative to FP16 at the kernel level.

**Per post.** [@thesupermannx](https://x.com/thesupermannx/status/2108098865073410484) says Samsung open-sourced a method that shrinks a 13B model to less than 1 GB, hits 0.1 bits per weight in some configurations, replaces the core math with a bitwise XOR and "sign flips," reports an 11.6x speedup against FP16, and holds up below 0.5 bits where earlier methods fail. The post links a photo, not a paper.

| Piece | Post | Paper and Samsung write-up |
| --- | --- | --- |
| Sub-1-bit, including 0.1 bits per weight | Yes | Yes, as the target regime |
| 13B model under 1 GB | "Less than 1 GB" | "Under 0.9 GB" for Llama 2 13B, in the abstract |
| 11.6x versus FP16 | Stated as the result | "Potential" speedup, described at kernel level |
| Core operation | Bitwise XOR, sign flips, "stop doing math" | Binarized factors and scaling. The forward pass is smaller binary matrix multiplies plus scales, not an XOR network |

The XOR sentence is the post's mechanism. It is the sentence to stop repeating. Sign-valued factors do make a multiply cheaper. That is not the same claim as "the model no longer does math."

## What a power user does with both

1. Open the repository and the abstract before quoting a number.
2. Write down the model size, the hardware, and the baseline the number was measured against.
3. Treat a social post as a pointer. Treat the paper's range, and its caveats ("potential," "kernel level"), as the thing you cite.
4. For an agent, measure cost per successful task, not tokens per second in isolation. A faster model that needs more retries can lose. That measurement is an [eval](../06-evals/index.md).

## Check yourself

1. What does the bitnet.cpp paper give you that the post's "6.17x" does not?
2. Which LittleBit mechanism is safe to repeat, and which belongs only to the post?
3. Why is the official 2.4B model relevant to the post's 100B sentence?

## Sources

- [@oliviscusAI](https://x.com/oliviscusAI/status/2108786434991923251) — 2026-10-10. bitnet.cpp claims, per post.
- [microsoft/BitNet](https://github.com/microsoft/BitNet) and [arxiv 2410.16144](https://arxiv.org/abs/2410.16144) — official project and paper. Established.
- [@thesupermannx](https://x.com/thesupermannx/status/2108098865073410484) — 2026-10-08. LittleBit claims, per post.
- [arxiv 2506.13771](https://arxiv.org/abs/2506.13771), [SamsungLabs/LittleBit](https://github.com/SamsungLabs/LittleBit), and the [Samsung Research blog](https://research.samsung.com/blog/LittleBit-Ultra-Low-Bit-Quantization-via-Latent-Factorization) — paper and primary write-up. Established.

## Continue

- Case study: [Local inference](../08-case-studies/local-inference.md)
- Next: [Evals](../06-evals/index.md)
- Previous: [Cloud and local](cloud-and-local.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
