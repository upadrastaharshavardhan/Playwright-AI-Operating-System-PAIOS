# Physical Architecture

## Executive Summary
Describes how PAIOS's logical modules map onto deployable units: containers, services, and data stores.

## Deployment Units

| Logical Module | Deployment Unit | Notes |
|---|---|---|
| Kernel | `paios-kernel` service | Stateless, horizontally scalable |
| State Store | PostgreSQL / distributed KV store | Kernel state, task queue |
| AI Runtime | `paios-runtime` service | GPU-optional; LLM calls routed externally |
| Agent Framework | `paios-agents` service pool | One pool per agent tier (Director/Squad/Worker) |
| Memory Engine | `paios-memory` service + vector DB | See [docs/05-memory-engine](../05-memory-engine/README.md) |
| Knowledge Graph | Graph database (e.g., Neo4j-compatible) | See [docs/06-knowledge-graph](../06-knowledge-graph/README.md) |
| Playwright Engine | `paios-executors` (containerized browser pool) | Ephemeral, autoscaled |
| Event Bus | Kafka-compatible message broker | Durable event log |

## Reference Deployment (Kubernetes)
See [deployment-topology.md](deployment-topology.md) and [docs/15-enterprise/kubernetes.md](../15-enterprise/kubernetes.md).

## References
- [distributed-architecture.md](distributed-architecture.md)
