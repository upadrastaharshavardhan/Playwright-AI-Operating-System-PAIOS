# Graph Model

## Executive Summary
PAIOS models the engineering domain as a property graph: typed nodes (entities) connected by typed, directed edges (relationships), queryable via both traversal and semantic similarity.

## Diagram

```mermaid
graph LR
    REQ[Requirement] -->|covered_by| TEST[Test]
    TEST -->|executed_as| EXEC[Execution]
    EXEC -->|produced| FAIL[Failure]
    FAIL -->|root_caused_by| RC[Root Cause]
    TEST -->|belongs_to| COMP[Component]
    COMP -->|owned_by| TEAM[Team]
    RELEASE[Release] -->|includes| EXEC
```

## References
- [entities.md](entities.md)
- [relationships.md](relationships.md)
