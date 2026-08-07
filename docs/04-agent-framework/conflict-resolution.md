# Conflict Resolution

## Executive Summary
When two Squad agents disagree (e.g., about whether a shared component's change is in-scope for their feature), the conflict escalates to their shared Department/Director parent for resolution, following a deterministic escalation path rather than negotiation between peer agents.

## Resolution Policy
1. Attempt automatic resolution via Knowledge Graph precedent (has this exact conflict occurred before?).
2. If unresolved, escalate to shared parent agent.
3. If still unresolved after N escalations, route to human review.

## References
- [coordination.md](coordination.md)
