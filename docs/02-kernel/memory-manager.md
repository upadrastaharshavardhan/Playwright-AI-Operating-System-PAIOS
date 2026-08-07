# Kernel Memory Manager

## Executive Summary
Not to be confused with the [Memory Engine](../05-memory-engine/README.md) (engineering knowledge), the kernel Memory Manager governs the in-process memory budget for task execution contexts — allocation, garbage collection triggers, and OOM protection.

## Design Goals
Prevent a single large test suite generation task from exhausting node memory and affecting co-located tasks.

## References
- [resource-manager.md](resource-manager.md)
