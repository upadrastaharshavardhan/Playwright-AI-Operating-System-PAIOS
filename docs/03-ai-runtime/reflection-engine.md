# Reflection Engine

## Executive Summary
Implements a self-critique pass over every proposed plan or action before execution, checking for: contradiction with known engineering memory, missing edge cases, and policy violations.

## Reflection Checklist
- Does this action contradict a previously recorded root cause in [Failure Memory](../05-memory-engine/failure-memory.md)?
- Does this test duplicate an existing test (checked via [Duplicate Detection](../07-semantic-search/duplicate-detection.md))?
- Does this action require permissions the current agent role lacks ([RBAC](../17-security/rbac.md))?

## References
- [confidence-engine.md](confidence-engine.md)
