# Test Memory

## Executive Summary
Stores every test PAIOS has ever generated or observed: its intent, the requirement it covers, its locator strategy, its historical pass/fail record, and its flakiness score.

## Schema (Simplified)

```json
{
  "testId": "string",
  "intent": "string",
  "requirementIds": ["string"],
  "locatorStrategy": "object",
  "flakinessScore": "float",
  "lastExecutions": ["ExecutionRef"]
}
```

## References
- [execution-memory.md](execution-memory.md)
