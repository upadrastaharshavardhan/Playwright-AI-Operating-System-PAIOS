# Graph Construction

## Executive Summary
The graph is constructed incrementally: static analysis of the repository seeds Component and ownership nodes; every test generation, execution, and failure event from the [event bus](../01-architecture/event-driven.md) appends new nodes/edges in real time.

## References
- [../05-memory-engine/repository-memory.md](../05-memory-engine/repository-memory.md)
