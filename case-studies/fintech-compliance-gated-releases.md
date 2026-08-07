# Case Study: Fintech Compliance-Gated Releases

## Context
A fintech company configured the [Policy Engine](../docs/17-security/policy-engine.md) to require human approval for any autonomous release decision touching PCI-scoped services, while allowing full autonomy elsewhere.

## Outcome
Non-regulated services achieved Level 3–4 autonomy ([Autonomous Testing whitepaper](../whitepapers/Autonomous%20Testing.md)) while regulated services retained mandatory human sign-off, all governed by a single consistent policy configuration.

## References
- [../docs/17-security/policy-engine.md](../docs/17-security/policy-engine.md)
