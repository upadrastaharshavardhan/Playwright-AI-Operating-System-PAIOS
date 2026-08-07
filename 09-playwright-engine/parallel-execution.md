# Parallel Execution

## Executive Summary
Tests are sharded and executed in parallel across the autoscaled browser executor pool, with intelligent sharding that groups tests by shared fixture/setup cost to minimize total wall-clock time.

## References
- [../01-architecture/distributed-architecture.md](../01-architecture/distributed-architecture.md)
