# Scalability

## Executive Summary
PAIOS scales along three independent dimensions: kernel task throughput (thousands of tasks/minute), agent concurrency (hundreds of concurrent agent sessions), and browser execution parallelism (thousands of concurrent Playwright contexts via autoscaled executor pools).

## Scaling Levers

| Dimension | Lever | Bottleneck |
|---|---|---|
| Kernel throughput | Add kernel nodes | State store write contention |
| Agent concurrency | Add agent pool replicas | LLM provider rate limits |
| Execution parallelism | Add executor pool nodes | Browser resource (CPU/memory) per container |

## References
- [distributed-architecture.md](distributed-architecture.md)
- [../../benchmarks/](../../benchmarks/)
