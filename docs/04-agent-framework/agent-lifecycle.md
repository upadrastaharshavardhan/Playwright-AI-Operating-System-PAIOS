# Agent Lifecycle

## Executive Summary
Defines how agents are instantiated, scoped, executed, and retired within the kernel's task execution model.

## Lifecycle Diagram

```mermaid
stateDiagram-v2
    [*] --> Instantiated
    Instantiated --> Scoped: assigned role + permissions
    Scoped --> Active: executing task(s)
    Active --> Idle: task complete, session persists
    Idle --> Active: new task assigned
    Idle --> Retired: session TTL expired
    Retired --> [*]
```

## References
- [../03-ai-runtime/agent-runtime.md](../03-ai-runtime/agent-runtime.md)
