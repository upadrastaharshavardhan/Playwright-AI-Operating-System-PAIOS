# Task State Machine

## Executive Summary
Formal definition of every state a kernel task can occupy and the valid transitions between them, ensuring no task can be dispatched twice or lost silently.

## Formal State Model
States: `Submitted, Queued, Scheduled, Running, Completed, Failed, Retrying, Cancelled`.
Invariant: exactly one state at any time; all transitions are logged to the [Audit Log](../17-security/audit-logs.md) and emitted on the event bus.

## References
- [scheduler.md](scheduler.md)
