# LLM Routing

## Executive Summary
Routes reasoning requests across multiple LLM providers based on task complexity, latency requirements, and cost, with automatic failover if a provider is degraded.

## Routing Policy Example

| Task Type | Preferred Model Tier | Fallback |
|---|---|---|
| Simple locator repair | Small/fast model | Mid-tier model |
| Test generation from requirements | Mid-tier model | Large model |
| Release-readiness reasoning | Large model | Large model (secondary provider) |

## References
- [../02-kernel/resource-manager.md](../02-kernel/resource-manager.md)
