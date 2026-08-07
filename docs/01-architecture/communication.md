# Communication Patterns

## Executive Summary
PAIOS components communicate via three patterns: synchronous RPC for request/response (e.g., a Worker agent requesting a memory query), asynchronous events for state changes (e.g., "test execution completed"), and shared state reads for high-frequency lookups (e.g., current task status).

## Pattern Selection Guide

| Use Case | Pattern |
|---|---|
| Agent requests a memory query | Synchronous RPC |
| Test execution completes | Async event |
| Kernel checks task status | Shared state read |
| Release Intelligence aggregates results | Async event subscription |

## References
- [event-driven.md](event-driven.md)
