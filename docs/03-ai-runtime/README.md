# 03 · AI Runtime

## Overview
The AI Runtime is the reasoning layer sitting directly above the kernel. It plans, reasons, reflects, retrieves memory, manages context, and routes to LLM providers on behalf of the Agent Framework above it.

## Folder Contents
| Document | Description |
|---|---|
| [runtime-overview.md](runtime-overview.md) | Runtime responsibilities |
| [agent-runtime.md](agent-runtime.md) | Per-agent execution context |
| [planner.md](planner.md) | Task decomposition and planning |
| [reasoner.md](reasoner.md) | Core reasoning loop |
| [reflection-engine.md](reflection-engine.md) | Self-critique before action |
| [confidence-engine.md](confidence-engine.md) | Confidence scoring for decisions |
| [tool-execution.md](tool-execution.md) | Tool-calling infrastructure |
| [memory-retrieval.md](memory-retrieval.md) | Querying the Memory Engine |
| [context-management.md](context-management.md) | Context window budgeting |
| [llm-routing.md](llm-routing.md) | Multi-provider LLM routing and failover |

## Navigation
Previous: [02 · Kernel](../02-kernel/README.md) · Next: [04 · Agent Framework](../04-agent-framework/README.md)
