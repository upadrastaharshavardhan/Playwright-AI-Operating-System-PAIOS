# Benchmark: Kernel Throughput

## Methodology
Measures task dispatch latency and sustained throughput under synthetic load, per [docs/02-kernel/scheduler.md](../docs/02-kernel/scheduler.md) design targets.

## Reference Targets
Sub-second dispatch latency at nominal load; horizontal scaling near-linear up to state-store write contention limits (see [docs/01-architecture/scalability.md](../docs/01-architecture/scalability.md)).

## References
- [../docs/01-architecture/scalability.md](../docs/01-architecture/scalability.md)
