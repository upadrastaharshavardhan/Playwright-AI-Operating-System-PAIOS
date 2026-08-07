# Event Schema Specification

```json
{
  "eventId": "uuid",
  "type": "task.scheduled | plan.created | test.generated | execution.completed | failure.detected | release.scored",
  "timestamp": "ISO8601",
  "sourceComponent": "string",
  "payload": "object (type-specific)",
  "traceId": "uuid"
}
```

## References
- [../docs/01-architecture/event-driven.md](../docs/01-architecture/event-driven.md)
