# Security Policy

## Reporting a Vulnerability

The PAIOS maintainers take security seriously across all layers of the operating system — kernel, AI runtime, memory engine, agent framework, plugin SDK, and enterprise connectors.

If you discover a security vulnerability, **do not open a public issue**. Instead:

1. Email **security@paios-project.dev** with a detailed description.
2. Include reproduction steps, affected versions, and potential impact.
3. If possible, include a proof-of-concept that does not cause harm to shared infrastructure.

We aim to acknowledge reports within **48 hours** and provide a remediation timeline within **7 days**.

## Supported Versions

| Version | Supported |
|---|---|
| 1.x (current) | ✅ |
| 0.x (pre-release) | ⚠️ Best effort |

## Disclosure Policy

We follow a **coordinated disclosure** model. Once a fix is available, we will publish a security advisory referencing the CVE (where applicable), the affected components, and upgrade instructions. Reporters are credited unless they request anonymity.

## Security Domains

See [`docs/17-security/README.md`](docs/17-security/README.md) for the full security architecture, including the authentication model, RBAC, audit logging, and the policy engine that governs autonomous agent actions.

## Scope

In scope: PAIOS kernel, AI runtime, agent framework, memory engine, knowledge graph, plugin SDK, and official enterprise connectors.

Out of scope: third-party plugins published to the marketplace by external authors (see [`docs/18-marketplace/README.md`](docs/18-marketplace/README.md) for third-party plugin security review policy).
