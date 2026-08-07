# Planner

## Executive Summary
Decomposes a high-level goal into an ordered, dependency-aware plan of sub-tasks assignable to specific agent tiers.

## Example Plan Decomposition
Goal: "Ensure checkout flow is release-ready."
1. Query memory for prior checkout-flow failures (Worker).
2. Identify code diff impact via Knowledge Graph (Squad).
3. Generate/update affected Playwright tests (Worker).
4. Execute regression suite (Worker pool).
5. Aggregate results into quality score (Release Intelligence).

## References
- [reasoner.md](reasoner.md)
