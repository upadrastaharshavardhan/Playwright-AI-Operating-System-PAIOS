# Coordination Strategy

## Executive Summary
PAIOS uses hierarchical coordination (each agent reports to exactly one parent) rather than flat swarm coordination, because it produces clear ownership, bounded blast radius for errors, and a natural escalation path mirroring real organizations.

## Why Not a Flat Swarm
Flat multi-agent swarms without hierarchy tend to produce redundant work, unresolvable disagreements, and no clear accountability for a given feature's quality — problems PAIOS's hierarchy is explicitly designed to avoid. See [../19-research/multi-agent-research.md](../19-research/multi-agent-research.md).

## References
- [conflict-resolution.md](conflict-resolution.md)
