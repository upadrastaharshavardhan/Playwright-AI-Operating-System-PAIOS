# Kernel Runtime

## Executive Summary
The kernel runtime is the process supervisor that executes dispatched tasks in isolated contexts (containers or lightweight sandboxes), enforcing timeouts and resource limits.

## Execution Model
Each task runs in an isolated execution context with a bounded CPU/memory envelope and a hard wall-clock timeout, preventing a single runaway task (e.g., an infinite Playwright wait) from starving the pool.

## References
- [resource-manager.md](resource-manager.md)
- [execution-engine.md](execution-engine.md)
