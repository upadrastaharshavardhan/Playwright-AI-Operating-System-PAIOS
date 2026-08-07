# Failure Memory

## Executive Summary
The highest-leverage memory domain: stores failure signatures (stack trace shape, error message pattern, DOM state at failure) linked to root causes, so recurring failures across teams and time are recognized rather than re-diagnosed from scratch.

## Failure Signature Matching
Uses semantic similarity (see [docs/07-semantic-search/similarity.md](../07-semantic-search/similarity.md)) over stack traces and error messages to match new failures against historical signatures, surfacing prior root causes automatically.

## References
- [../06-knowledge-graph/README.md](../06-knowledge-graph/README.md)
