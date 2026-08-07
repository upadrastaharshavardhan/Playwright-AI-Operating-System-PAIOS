# 02 · Kernel

## Overview
The PAIOS kernel is the foundational scheduling and execution substrate — the layer everything else is built on. It contains no AI reasoning logic; its sole responsibility is reliably scheduling, executing, and supervising quality engineering tasks.

## Purpose
Give engineers building or extending PAIOS a precise reference for kernel internals.

## Folder Contents
| Document | Description |
|---|---|
| [kernel-overview.md](kernel-overview.md) | Kernel responsibilities and boundaries |
| [scheduler.md](scheduler.md) | Task scheduling algorithm |
| [runtime.md](runtime.md) | Kernel runtime execution model |
| [memory-manager.md](memory-manager.md) | Kernel-level memory (not the Memory Engine) |
| [resource-manager.md](resource-manager.md) | CPU/browser/LLM-quota resource arbitration |
| [state-machine.md](state-machine.md) | Task lifecycle state machine |
| [task-manager.md](task-manager.md) | Task queue and dependency management |
| [security-manager.md](security-manager.md) | Kernel-level security enforcement |
| [execution-engine.md](execution-engine.md) | Task execution and the kernel API |

## Navigation
Previous: [01 · Architecture](../01-architecture/README.md) · Next: [03 · AI Runtime](../03-ai-runtime/README.md)

## References
- [Root ARCHITECTURE.md](../../ARCHITECTURE.md)
