# Relationships

## Executive Summary
Canonical edge types connecting entities.

| Edge | From → To | Semantics |
|---|---|---|
| `covered_by` | Requirement → Test | Requirement is tested by |
| `executed_as` | Test → Execution | Test produced this execution |
| `produced` | Execution → Failure | Execution resulted in failure |
| `root_caused_by` | Failure → RootCause | Diagnosed cause |
| `belongs_to` | Test → Component | Ownership mapping |
| `similar_to` | Failure → Failure | Semantic similarity edge (see [semantic-links.md](semantic-links.md)) |

## References
- [entities.md](entities.md)
