# Memory Retrieval

## Executive Summary
The interface the AI Runtime uses to query the [Memory Engine](../05-memory-engine/README.md) and [Semantic Search](../07-semantic-search/README.md) subsystems for context relevant to the current plan step.

## Retrieval Strategy
Hybrid retrieval: structured queries against the Knowledge Graph for precise relationships (e.g., "tests linked to this component") combined with vector similarity search for fuzzy relevance (e.g., "failures similar to this stack trace").

## References
- [../07-semantic-search/retrieval.md](../07-semantic-search/retrieval.md)
