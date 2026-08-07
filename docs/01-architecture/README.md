# 01 · Architecture

## Overview
This section defines PAIOS's system, logical, physical, and distributed architecture: how components are organized, how they communicate, how the system is deployed, and the key architectural decisions and trade-offs behind those choices.

## Purpose
To give engineers implementing or extending PAIOS a precise architectural reference that the kernel, AI runtime, and every domain subsystem conform to.

## Folder Contents

| Document | Description |
|---|---|
| [system-overview.md](system-overview.md) | End-to-end system view |
| [layered-architecture.md](layered-architecture.md) | The 8-layer model in depth |
| [logical-architecture.md](logical-architecture.md) | Component and module boundaries |
| [physical-architecture.md](physical-architecture.md) | Deployment units and infrastructure |
| [distributed-architecture.md](distributed-architecture.md) | Multi-node scaling model |
| [component-model.md](component-model.md) | Component contracts and interfaces |
| [communication.md](communication.md) | Inter-component communication patterns |
| [event-driven.md](event-driven.md) | Event bus and pub/sub design |
| [deployment-topology.md](deployment-topology.md) | Reference deployment topologies |
| [architecture-decisions.md](architecture-decisions.md) | ADRs (Architecture Decision Records) |
| [availability.md](availability.md) | High-availability design |
| [scalability.md](scalability.md) | Scaling strategy and limits |

## Architecture
See [system-overview.md](system-overview.md) for the canonical diagram.

## Navigation
Previous: [00 · Introduction](../00-introduction/README.md) · Next: [02 · Kernel](../02-kernel/README.md)

## References
- [Root ARCHITECTURE.md](../../ARCHITECTURE.md)
