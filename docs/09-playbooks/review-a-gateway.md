<p align="center">
  <img src="../../assets/diagrams/gateway-routing.svg" alt="Gateway routing" width="100%">
</p>

<p>
  <img src="../../assets/badges/level-power.svg" alt="Power user" height="28">
</p>

# Playbook · Review a gateway

Decide whether a local model gateway is allowed to see your prompts. The worked example is the OmniRoute post. The checklist fits the next gateway someone sends you.

| | |
| --- | --- |
| Path | Power user |
| Time | About an hour, longer if you read the code |
| You need | [Gateways and routing](../02-tools-mcp/gateways-and-routing.md) and [supply chain](../07-security/gateway-and-supply-chain.md) |
| Produces | A note with a decision: use, use only on a sandbox repo, or do not use |

## 1. Start from the claim sheet

Write the claims you are being sold. For OmniRoute, copy them from the [concept page](../02-tools-mcp/gateways-and-routing.md) and mark each one unverified until you have looked. If the link you were given is a shortened URL, open the post yourself. Do not install from a name you searched and hoped was the same project.

## 2. Answer the eight questions

| # | Question | Your note |
| --- | --- | --- |
| 1 | Which commit or image are you reviewing? | |
| 2 | Where are keys stored, and can the process print them? | |
| 3 | List every host the process talks to, besides the provider. | |
| 4 | What is written to logs? Paste a redacted sample. | |
| 5 | On a 429, what exactly is retried, and to which account? | |
| 6 | Whose keys are configured? Did you create them? | |
| 7 | Do the provider terms allow this routing? | |
| 8 | What is the blast radius if the proxy is malicious or buggy? | |

A "0 telemetry" sentence in a post does not answer question 3. An AES-256-GCM mention does not answer question 2 until you see the call.

## 3. Watch one real request

Point a scratch project at the gateway. Send a prompt that contains a canary phrase you can search for, not a secret. Then look:

| Look at | You are checking |
| --- | --- |
| The provider dashboard | The request arrived where you thought |
| The proxy log | The canary is stored the way you accept |
| The fallback, if you can trigger a failure safely | The retry did not fan out to an account you did not intend |

Do not burn a pile of accounts to "see the fallback." One deliberate, permitted failure is enough to understand the path.

## 4. Decide

| Decision | When it is honest |
| --- | --- |
| Use | You can name the commit, the hosts, the key store, and the terms |
| Sandbox only | The code looks fine and you have not finished the log and terms checks |
| Do not use | You cannot find the source, the keys are not yours, or the terms say no |

Write the decision in your team wiki, with the date and the commit. That is the memory pattern. The next person should not have to trust the chat where you said "seems legit."

## 5. If you also turn on compression

Keep the pre-compression prompt in a redacted trace for a day. Compare task success on two or three prompts you care about. A smaller request that fails the task is more expensive. The post's 15–95% range is not your measurement.

## Check yourself

1. Which question does "local-first" fail to answer by itself?
2. What do you send instead of a real secret when you want to see a log?
3. Where does the decision get written?

## Sources

- [@Bober_smart](https://x.com/Bober_smart/status/2108293657552117850) — the claims under review, per post.
- The eight questions and the decision table are synthesis.

## Continue

- [Research agent](research-agent.md)
- [Local gateway case study](../08-case-studies/local-gateway.md)

---

[Map](../README.md) | [Paths](../learning-paths.md) | [Glossary](../glossary.md) | [References](../references.md)
