# Autonomous Testing: Levels of Autonomy for Quality Engineering

## Abstract
Borrowing the "levels of autonomy" framing from autonomous vehicles, this whitepaper defines five levels of testing autonomy and argues that organizations should adopt PAIOS incrementally across this spectrum rather than jumping directly to full autonomy.

## Levels of Autonomy

| Level | Name | Description |
|---|---|---|
| 0 | Manual | Human writes and maintains all tests |
| 1 | Assisted Generation | AI drafts tests from human-written requirements |
| 2 | Assisted Maintenance | AI repairs broken locators, humans approve |
| 3 | Supervised Autonomy | AI generates, maintains, and executes tests; humans review release decisions |
| 4 | Full Autonomy | AI makes release-readiness decisions within policy bounds, escalating only exceptions |

## Why Incremental Adoption Matters
Jumping directly to Level 4 without built-up [Engineering Memory](Engineering%20Memory.md) and calibrated [Confidence Engine](../docs/03-ai-runtime/confidence-engine.md) scoring risks misplaced trust. PAIOS's [Policy Engine](../docs/17-security/policy-engine.md) allows organizations to configure autonomy level per product area independently.

## References
- [../docs/03-ai-runtime/confidence-engine.md](../docs/03-ai-runtime/confidence-engine.md)
- [../docs/17-security/policy-engine.md](../docs/17-security/policy-engine.md)
