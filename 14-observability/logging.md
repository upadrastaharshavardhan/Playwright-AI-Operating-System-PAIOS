# Logging

## Executive Summary
All components emit structured (JSON) logs with a consistent schema: `timestamp, component, taskId, agentId, level, message, context`, enabling correlated queries across the full request lifecycle.

## References
- [distributed-tracing.md](distributed-tracing.md)
