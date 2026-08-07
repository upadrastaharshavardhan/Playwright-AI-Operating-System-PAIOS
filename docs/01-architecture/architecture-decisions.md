# Architecture Decision Records (ADRs)

## ADR-001: Kernel excludes AI reasoning logic
**Status:** Accepted. **Rationale:** Keeps the kernel small, testable, and stable; reasoning evolves far faster than scheduling primitives and should not force kernel redeploys.

## ADR-002: Event bus over direct RPC for cross-plane communication
**Status:** Accepted. **Rationale:** Decouples subsystem deployment lifecycles and enables replay-based recovery.

## ADR-003: Agent hierarchy modeled on organizational structure, not flat swarm
**Status:** Accepted. **Rationale:** Clear ownership and escalation paths outperform flat multi-agent coordination at enterprise scale; see [docs/04-agent-framework/coordination.md](../04-agent-framework/coordination.md).

## ADR-004: Knowledge graph as the source of explainability
**Status:** Accepted. **Rationale:** Every autonomous decision must cite graph-linked evidence rather than an opaque model score.

## References
- [../19-research/README.md](../19-research/README.md)
