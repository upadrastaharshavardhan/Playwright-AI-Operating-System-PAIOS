# Execution Engine

## Executive Summary
The execution engine is the kernel's task-dispatch API surface — the boundary where tasks enter the system and results exit.

## API

```http
POST /v1/tasks
{
  "type": "generate_test | execute_test | analyze_failure | score_release",
  "priority": "high | normal | low",
  "payload": { ... },
  "idempotencyKey": "string"
}
```

```http
GET /v1/tasks/{taskId}
```

## References
- [../01-architecture/component-model.md](../01-architecture/component-model.md)
