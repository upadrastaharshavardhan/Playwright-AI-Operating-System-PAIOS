# Retry Strategy

## Executive Summary
Distinguishes genuine failures from flaky failures using historical flakiness scores from [Test Memory](../05-memory-engine/test-memory.md); a test with a high historical flakiness score gets a different retry/quarantine policy than a normally stable test that just failed.

## References
- [../05-memory-engine/test-memory.md](../05-memory-engine/test-memory.md)
