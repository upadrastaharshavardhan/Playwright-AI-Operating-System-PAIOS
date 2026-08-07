# Contributing to PAIOS

Thank you for your interest in contributing to the Playwright AI Operating System. PAIOS is an ambitious, layered engineering effort, and contributions are welcome across documentation, kernel engineering, agent design, memory systems, connectors, and plugins.

## Ways to Contribute

| Area | Description | Start Here |
|---|---|---|
| Documentation | Improve or extend the technical docs in `docs/` | [docs/00-introduction](docs/00-introduction/README.md) |
| Kernel | Scheduler, runtime, execution engine work | [docs/02-kernel](docs/02-kernel/README.md) |
| Agent Framework | New agent roles, coordination strategies | [docs/04-agent-framework](docs/04-agent-framework/README.md) |
| Connectors | Enterprise tool integrations | [docs/15-enterprise](docs/15-enterprise/README.md) |
| Plugins | Marketplace plugin development | [docs/16-plugin-sdk](docs/16-plugin-sdk/README.md) |
| Research | Experimental agent strategies, benchmarks | [docs/19-research](docs/19-research/README.md) |

## Development Principles

1. **Documentation is a first-class artifact.** Every architectural change must be accompanied by an update to the relevant document under `docs/`. PRs that change behavior without documentation updates will not be merged.
2. **Diagrams before prose where structure matters.** Use Mermaid diagrams to express architecture, sequences, and state machines before or alongside prose explanation.
3. **No breaking changes to the agent permission model without an RFC.** Because PAIOS agents can take autonomous action, changes to `docs/17-security/rbac.md` or `docs/04-agent-framework/permissions.md` require a design review.
4. **Backward-compatible memory schemas.** Changes to the memory engine schema (`docs/05-memory-engine/`) must include a migration path.

## Contribution Workflow

1. Fork the repository and create a feature branch: `git checkout -b feature/<short-description>`.
2. Make your changes, following the style guide below.
3. Run documentation lint checks (Markdown lint, Mermaid syntax validation, link checking).
4. Open a pull request against `main` with a clear description of the change and its motivation.
5. At least one maintainer review is required before merge.

## Documentation Style Guide

- Use GitHub-flavored Markdown.
- Every document should include: Executive Summary, Purpose, Background, Design Goals, Architecture, Diagrams (Mermaid), Examples, Best Practices, Anti-Patterns, Security Considerations, and References.
- Use sentence-case headings.
- Cross-reference related documents using relative links.
- Prefer tables over long prose lists when comparing options.
- All Mermaid diagrams must be syntactically valid — verify with `mmdc --input file.mmd --output test.svg` or an equivalent renderer before submitting.

## Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
docs(kernel): add failure recovery sequence diagram to scheduler.md
feat(agent-framework): introduce squad-level conflict resolution policy
fix(memory-engine): correct pruning TTL default in memory-pruning.md
```

## Governance

PAIOS follows a maintainer-led governance model during its early stages, transitioning toward a technical steering committee as the contributor base grows. See [ROADMAP.md](ROADMAP.md) for the governance evolution plan.

## Code of Conduct

All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## References

- [README.md](README.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [ROADMAP.md](ROADMAP.md)
- [SECURITY.md](SECURITY.md)
