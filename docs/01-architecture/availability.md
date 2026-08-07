# High Availability

## Executive Summary
PAIOS targets 99.9% control-plane availability for enterprise deployments, with graceful degradation of autonomous features when dependent LLM providers are unavailable.

## HA Design
- Kernel: active-active across 3+ nodes with leader election for task assignment.
- Event Bus: replicated log (Kafka-compatible, min ISR 2).
- Memory Engine: read replicas per region; writes to primary with async replication.

## Degradation Modes
If the AI Runtime's upstream LLM provider is unavailable, the kernel continues executing already-generated tests and queues new planning tasks rather than failing the pipeline (see [docs/03-ai-runtime/llm-routing.md](../03-ai-runtime/llm-routing.md) for provider failover).

## References
- [distributed-architecture.md](distributed-architecture.md)
