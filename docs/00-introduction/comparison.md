# Comparison

## PAIOS vs. Traditional Frameworks and AI Testing Tools

| Capability | Selenium/Cypress/Playwright (raw) | AI Test-Gen Plugins | PAIOS |
|---|---|---|---|
| Browser automation | ✅ | ✅ (via underlying framework) | ✅ (via [Playwright Engine](../09-playwright-engine/README.md)) |
| One-shot AI test generation | ❌ | ✅ | ✅ |
| Persistent engineering memory | ❌ | ❌ | ✅ [Memory Engine](../05-memory-engine/README.md) |
| Multi-agent coordination | ❌ | ❌ | ✅ [Agent Framework](../04-agent-framework/README.md) |
| Autonomous test maintenance | ❌ | Partial | ✅ [Locator Engine](../09-playwright-engine/locator-engine.md) |
| Release-readiness reasoning | ❌ | ❌ | ✅ [Release Intelligence](../12-release-intelligence/README.md) |
| Explainable decisions | N/A | ❌ | ✅ [Knowledge Graph](../06-knowledge-graph/README.md) |
| Enterprise policy governance | ❌ | ❌ | ✅ [Security](../17-security/README.md) |

## Positioning Statement

PAIOS is not a competitor to Playwright — it is built **on top of** Playwright as its execution layer (see [docs/09-playwright-engine/README.md](../09-playwright-engine/README.md)). PAIOS competes with the *manual coordination layer* that currently sits above every automation framework: the humans deciding what to test, maintaining tests, and judging release safety.

## References

- [why-paios.md](why-paios.md)
