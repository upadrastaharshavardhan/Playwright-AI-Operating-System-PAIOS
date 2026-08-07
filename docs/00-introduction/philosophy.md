# Design Philosophy

## Executive Summary

PAIOS's design philosophy borrows deliberately from operating systems research rather than from web-testing-framework conventions. This document lays out the first principles that every subsystem's design must satisfy.

## First Principles

### 1. The Kernel Is Small and Stable

Following the Unix philosophy, the [PAIOS kernel](../02-kernel/README.md) does one thing — schedule and execute quality engineering tasks reliably — and does not itself contain AI reasoning logic. Reasoning lives in the [AI Runtime](../03-ai-runtime/README.md), a layer above.

### 2. Memory Is Structural, Not Incidental

Memory is not a logging afterthought; it is a queryable, structured subsystem ([Memory Engine](../05-memory-engine/README.md)) that every agent decision must consult before acting.

### 3. Agents Mirror Organizational Structure

The [Agent Framework](../04-agent-framework/README.md) is deliberately modeled on how real QA organizations are structured — Chief QA Officer, Directors, Departments, Squads, Workers — because this hierarchy has already been proven to scale human coordination, and it produces more legible autonomous coordination than a flat swarm of undifferentiated agents.

### 4. Explainability Is Non-Negotiable

Every score, recommendation, or autonomous action must be traceable to the evidence that produced it, via the [Knowledge Graph](../06-knowledge-graph/README.md).

### 5. Governance Is Layered, Not Global

Rather than a single "autonomous mode" switch, every layer — kernel, agent, workflow — has its own policy boundary (see [docs/17-security/policy-engine.md](../17-security/policy-engine.md)), so organizations can adopt autonomy incrementally and per-domain.

## Anti-Patterns We Explicitly Reject

- A single opaque "AI does everything" black box with no intermediate observability.
- Memoryless agents that re-derive the same conclusions every run.
- Flat multi-agent swarms with no clear ownership or escalation path.

## References

- [mission.md](mission.md)
- [../01-architecture/architecture-decisions.md](../01-architecture/architecture-decisions.md)
