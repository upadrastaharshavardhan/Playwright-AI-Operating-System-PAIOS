# Distributed Architecture

## Executive Summary
PAIOS scales horizontally across three independent axes: kernel task throughput, agent concurrency, and browser execution parallelism.

## Scaling Model

```mermaid
graph LR
    LB[Load Balancer] --> K1[Kernel Node 1]
    LB --> K2[Kernel Node 2]
    K1 --> EB[(Event Bus Cluster)]
    K2 --> EB
    EB --> W1[Worker Pool 1]
    EB --> W2[Worker Pool 2]
    EB --> W3[Worker Pool N]
    W1 --> BR[(Browser Executor Pool)]
    W2 --> BR
    W3 --> BR
```

## Consistency Model
Kernel state is strongly consistent (single writer per task via optimistic locking); memory engine writes are eventually consistent across regions to support multi-region deployments.

## Failure Domains
Each worker pool is an independent failure domain; a crashed browser executor does not affect kernel or other pools (see [docs/02-kernel/scheduler.md](../02-kernel/scheduler.md) for retry semantics).

## References
- [physical-architecture.md](physical-architecture.md)
- [scalability.md](scalability.md)
