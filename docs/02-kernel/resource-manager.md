# Resource Manager

## Executive Summary
Arbitrates three scarce resources across the system: browser executor capacity, LLM provider quota, and CPU/memory per node.

## Resource Arbitration Model

| Resource | Arbitration Strategy |
|---|---|
| Browser Executors | Fixed pool with autoscaling; FIFO with priority preemption |
| LLM Quota | Token-bucket per tenant, with burst allowance |
| CPU/Memory | Cgroup-enforced limits per execution context |

## References
- [scheduler.md](scheduler.md)
- [../03-ai-runtime/llm-routing.md](../03-ai-runtime/llm-routing.md)
