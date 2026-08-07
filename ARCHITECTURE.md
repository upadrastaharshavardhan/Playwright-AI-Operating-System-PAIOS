# ARCHITECTURE

This document provides the condensed, top-level architectural summary of PAIOS. For full detail, see [`docs/01-architecture/README.md`](docs/01-architecture/README.md) and the subsystem-specific documents linked throughout.

## Layered System Model

PAIOS is organized into eight architectural layers, each with a clear responsibility boundary and a well-defined interface to the layers above and below it.

```mermaid
graph TB
    subgraph L8["Layer 8 — Enterprise Integration"]
        A1[Azure DevOps] --- A2[GitHub/GitLab] --- A3[Jira/Confluence] --- A4[Slack/Teams] --- A5[Kubernetes]
    end
    subgraph L7["Layer 7 — Marketplace & Plugin SDK"]
        B1[Plugin Runtime] --- B2[Agent Marketplace] --- B3[Template Registry]
    end
    subgraph L6["Layer 6 — Workflow & Release Intelligence"]
        C1[Workflow Engine] --- C2[Release Readiness] --- C3[Risk Analysis]
    end
    subgraph L5["Layer 5 — Domain Intelligence"]
        D1[Browser Intelligence] --- D2[UI Intelligence] --- D3[API Intelligence]
    end
    subgraph L4["Layer 4 — Knowledge & Memory"]
        E1[Knowledge Graph] --- E2[Memory Engine] --- E3[Semantic Search]
    end
    subgraph L3["Layer 3 — Agent Framework"]
        F1[Chief QA Officer] --- F2[Directors] --- F3[Departments] --- F4[Squads] --- F5[Workers]
    end
    subgraph L2["Layer 2 — AI Runtime"]
        G1[Planner] --- G2[Reasoner] --- G3[Reflection Engine] --- G4[LLM Routing]
    end
    subgraph L1["Layer 1 — Kernel"]
        H1[Scheduler] --- H2[Execution Engine] --- H3[State Machine] --- H4[Resource Manager]
    end

    L8 --> L7 --> L6 --> L5 --> L4 --> L3 --> L2 --> L1
```

| Layer | Responsibility | Documentation |
|---|---|---|
| 1. Kernel | Process scheduling, execution, resource arbitration | [docs/02-kernel](docs/02-kernel/README.md) |
| 2. AI Runtime | Planning, reasoning, reflection, model routing | [docs/03-ai-runtime](docs/03-ai-runtime/README.md) |
| 3. Agent Framework | Organizational hierarchy and coordination | [docs/04-agent-framework](docs/04-agent-framework/README.md) |
| 4. Knowledge & Memory | Durable engineering knowledge | [docs/05-memory-engine](docs/05-memory-engine/README.md), [docs/06-knowledge-graph](docs/06-knowledge-graph/README.md) |
| 5. Domain Intelligence | Browser, UI, and API understanding | [docs/08-browser-intelligence](docs/08-browser-intelligence/README.md) |
| 6. Workflow & Release | Orchestration and release confidence | [docs/13-workflow-engine](docs/13-workflow-engine/README.md), [docs/12-release-intelligence](docs/12-release-intelligence/README.md) |
| 7. Marketplace & SDK | Extensibility | [docs/16-plugin-sdk](docs/16-plugin-sdk/README.md) |
| 8. Enterprise Integration | External system connectors | [docs/15-enterprise](docs/15-enterprise/README.md) |

## Request Lifecycle (Sequence Overview)

```mermaid
sequenceDiagram
    participant U as Engineer / CI Trigger
    participant K as Kernel Scheduler
    participant AR as AI Runtime
    participant AF as Agent Framework
    participant ME as Memory Engine
    participant PE as Playwright Engine
    participant RI as Release Intelligence

    U->>K: Submit quality task (e.g. "validate checkout flow")
    K->>AR: Schedule planning cycle
    AR->>ME: Retrieve relevant engineering memory
    ME-->>AR: Prior tests, failures, known flaky patterns
    AR->>AF: Delegate to appropriate Director/Squad agent
    AF->>PE: Generate and execute Playwright tests
    PE-->>AF: Execution results, traces, artifacts
    AF->>ME: Persist execution + failure memory
    AF->>RI: Contribute to release readiness signal
    RI-->>U: Quality score + go/no-go recommendation
```

## Cross-Cutting Concerns

- **Security** is enforced at every layer boundary via the policy engine — see [docs/17-security](docs/17-security/README.md).
- **Observability** instruments every kernel task, agent action, and workflow step — see [docs/14-observability](docs/14-observability/README.md).
- **Extensibility** is available at Layers 5–8 via the Plugin SDK — see [docs/16-plugin-sdk](docs/16-plugin-sdk/README.md).

## References

- [docs/01-architecture/system-overview.md](docs/01-architecture/system-overview.md)
- [docs/01-architecture/layered-architecture.md](docs/01-architecture/layered-architecture.md)
- [VISION.md](VISION.md)
