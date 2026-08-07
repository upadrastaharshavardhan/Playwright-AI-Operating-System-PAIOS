# Framework Integration

## Executive Summary
PAIOS generates and executes standard Playwright Test (TypeScript/Python) files, meaning output is always a normal, human-readable Playwright suite — not a proprietary DSL — ensuring engineers can read, debug, and directly edit any PAIOS-generated test.

## Design Principle
Generated code must be indistinguishable in structure and quality from what a senior QA engineer would hand-write, per [best practices in test-memory](../05-memory-engine/test-memory.md).

## References
- [locator-engine.md](locator-engine.md)
