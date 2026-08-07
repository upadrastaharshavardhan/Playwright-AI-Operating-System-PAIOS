# Confidence Engine

## Executive Summary
Assigns a calibrated confidence score (0.0–1.0) to every agent decision, combining model self-reported certainty, historical accuracy of similar past decisions (from memory), and evidence completeness.

## Escalation Threshold
Decisions below the configured confidence threshold (default 0.75) are routed to human review via [docs/13-workflow-engine/human-approval.md](../13-workflow-engine/human-approval.md) rather than executed autonomously.

## References
- [../12-release-intelligence/quality-score.md](../12-release-intelligence/quality-score.md)
