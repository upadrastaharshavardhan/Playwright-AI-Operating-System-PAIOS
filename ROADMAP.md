# Roadmap

This roadmap tracks the engineering evolution of PAIOS across kernel maturity, agent capability, and enterprise readiness. It is organized into horizons rather than fixed dates, since AI runtime capability is a moving dependency.

## Horizon 0 — Foundation (Current)

**Goal: A working kernel, a working single-agent runtime, and a working Playwright execution engine.**

- [x] Kernel scheduler, state machine, and execution engine design finalized ([docs/02-kernel](docs/02-kernel/README.md))
- [x] Core memory engine schema: test memory, execution memory, failure memory ([docs/05-memory-engine](docs/05-memory-engine/README.md))
- [x] Playwright engine integration: fixtures, locator engine, retry strategy ([docs/09-playwright-engine](docs/09-playwright-engine/README.md))
- [ ] Single-agent test generation from natural language requirements
- [ ] Basic knowledge graph construction from repository analysis

## Horizon 1 — Multi-Agent Organization

**Goal: The full agent hierarchy operating cooperatively on a real codebase.**

- [ ] Chief QA Officer agent: strategic planning across product areas
- [ ] Director-layer agents: functional, performance, security, accessibility domains
- [ ] Department and Squad layer agents mapped to product/feature boundaries
- [ ] Inter-agent communication protocol and conflict resolution ([docs/04-agent-framework/conflict-resolution.md](docs/04-agent-framework/conflict-resolution.md))
- [ ] Policy and permission enforcement for autonomous actions ([docs/17-security/rbac.md](docs/17-security/rbac.md))

## Horizon 2 — Engineering Memory at Scale

**Goal: Memory that compounds usefully across years of codebase history.**

- [ ] Full knowledge graph with semantic linking across tests, requirements, and code ([docs/06-knowledge-graph](docs/06-knowledge-graph/README.md))
- [ ] Vector-based semantic search and duplicate test detection ([docs/07-semantic-search](docs/07-semantic-search/README.md))
- [ ] Memory pruning and ranking to prevent unbounded growth ([docs/05-memory-engine/memory-pruning.md](docs/05-memory-engine/memory-pruning.md))
- [ ] Cross-repository memory federation for platform teams

## Horizon 3 — Release Intelligence

**Goal: Trustworthy, explainable autonomous release-readiness recommendations.**

- [ ] Quality score model combining test results, risk analysis, and historical failure data ([docs/12-release-intelligence/quality-score.md](docs/12-release-intelligence/quality-score.md))
- [ ] Go/no-go recommendation engine with full evidence traceability
- [ ] Human-in-the-loop approval workflows for high-risk releases ([docs/13-workflow-engine/human-approval.md](docs/13-workflow-engine/human-approval.md))

## Horizon 4 — Enterprise & Ecosystem

**Goal: Production-grade enterprise deployment and an open plugin ecosystem.**

- [ ] Full enterprise connector suite (Azure DevOps, GitHub, GitLab, Jira, Jenkins, Kubernetes) — [docs/15-enterprise](docs/15-enterprise/README.md)
- [ ] Plugin SDK v1.0 with marketplace publishing pipeline — [docs/16-plugin-sdk](docs/16-plugin-sdk/README.md)
- [ ] SOC 2 / enterprise security certification track — [docs/17-security](docs/17-security/README.md)
- [ ] Public agent and template marketplace — [docs/18-marketplace](docs/18-marketplace/README.md)

## Governance Evolution

Early development follows a maintainer-led model. As Horizon 2 completes, we intend to establish a Technical Steering Committee with representation from major enterprise adopters, in line with practices from projects like Kubernetes and Istio.

## References

- [VISION.md](VISION.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
