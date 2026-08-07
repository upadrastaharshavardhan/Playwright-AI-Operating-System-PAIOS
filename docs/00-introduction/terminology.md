# Terminology

Canonical glossary used consistently across all PAIOS documentation.

| Term | Definition |
|---|---|
| **Kernel** | The core scheduling and execution substrate of PAIOS. See [docs/02-kernel](../02-kernel/README.md). |
| **Agent** | An autonomous or semi-autonomous unit of work with a defined role in the organizational hierarchy. |
| **Chief QA Officer (CQO) Agent** | The top-level strategic agent responsible for organization-wide quality posture. |
| **Director Agent** | An agent owning a quality domain (functional, performance, security, accessibility). |
| **Squad Agent** | An agent owning a specific feature or product area. |
| **Worker Agent** | An agent executing a discrete task (e.g., generating one test, analyzing one failure). |
| **Engineering Memory** | The durable, structured record of tests, executions, failures, and releases. See [docs/05-memory-engine](../05-memory-engine/README.md). |
| **Knowledge Graph** | The entity/relationship graph linking code, tests, requirements, and failures. See [docs/06-knowledge-graph](../06-knowledge-graph/README.md). |
| **Quality Score** | A quantified, explainable measure of release confidence. See [docs/12-release-intelligence/quality-score.md](../12-release-intelligence/quality-score.md). |
| **Policy Engine** | The subsystem enforcing what autonomous actions agents are permitted to take. See [docs/17-security/policy-engine.md](../17-security/policy-engine.md). |
| **Workflow DSL** | The domain-specific language used to define orchestrated quality workflows. See [docs/13-workflow-engine/workflow-dsl.md](../13-workflow-engine/workflow-dsl.md). |
| **Reflection Engine** | The AI runtime component that critiques and revises agent plans before execution. See [docs/03-ai-runtime/reflection-engine.md](../03-ai-runtime/reflection-engine.md). |

## References

- [comparison.md](comparison.md)
