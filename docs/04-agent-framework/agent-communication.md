# Agent Communication Protocol

## Executive Summary
Agents communicate via structured, typed messages over the event bus — delegation requests (parent → child), status reports (child → parent), and escalations (child → parent, marked urgent).

## Message Types
`DelegateTask`, `TaskStatusReport`, `Escalation`, `ConflictNotice`.

## References
- [coordination.md](coordination.md)
- [../01-architecture/event-driven.md](../01-architecture/event-driven.md)
