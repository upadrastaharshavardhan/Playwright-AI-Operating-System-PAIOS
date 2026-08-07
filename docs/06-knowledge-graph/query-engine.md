# Query Engine

## Executive Summary
Exposes a graph query API (Cypher-like) used by the AI Runtime's [Memory Retrieval](../03-ai-runtime/memory-retrieval.md) component and by human-facing dashboards.

## Example Query
```cypher
MATCH (f:Failure)-[:root_caused_by]->(rc:RootCause)
WHERE f.componentId = "checkout-service"
RETURN rc, count(f) AS occurrences
ORDER BY occurrences DESC
```

## References
- [graph-model.md](graph-model.md)
