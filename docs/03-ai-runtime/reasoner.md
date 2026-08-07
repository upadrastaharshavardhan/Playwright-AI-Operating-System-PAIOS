# Reasoner

## Executive Summary
The core inference loop that evaluates retrieved evidence (memory, knowledge graph, live DOM/API state) against the current plan step and produces the next concrete action.

## Design Principle
The Reasoner never acts directly — it produces a proposed action that must pass through the [Reflection Engine](reflection-engine.md) and [Confidence Engine](confidence-engine.md) before the Agent Framework executes it.

## References
- [reflection-engine.md](reflection-engine.md)
