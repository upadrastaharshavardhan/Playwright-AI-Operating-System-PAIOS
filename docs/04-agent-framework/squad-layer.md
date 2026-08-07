# Squad Layer

## Executive Summary
Squad agents own a single feature or user flow (e.g., "Guest Checkout") and are the primary unit of day-to-day autonomous operation — deciding what to test, delegating generation/execution to Worker agents, and maintaining that feature's test suite over time.

## Responsibilities
- Own the feature's Playwright test suite lifecycle.
- Detect impact from code changes via the [Knowledge Graph](../06-knowledge-graph/README.md) and trigger targeted regression.

## References
- [worker-layer.md](worker-layer.md)
