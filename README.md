# PAIOS - Playwright AI Operating System

> **"The World's First AI Operating System for Quality Engineering"**
>
> From Automation to Autonomy. From Test Execution to Engineering Intelligence.

## Overview

PAIOS is an **operating system for quality engineering** — a layered, agentic runtime that treats test generation, execution, analysis, release confidence, and organizational quality knowledge as first-class kernel responsibilities.

## Architecture (8 Layers)

| Layer | Name | Responsibility |
|-------|------|----------------|
| L1 | **Kernel** | Process scheduling, execution, resource arbitration |
| L2 | **AI Runtime** | Planning, reasoning, reflection, model routing |
| L3 | **Agent Framework** | Multi-agent organizational hierarchy |
| L4 | **Knowledge & Memory** | Durable engineering knowledge graph |
| L5 | **Domain Intelligence** | Browser, UI, and API understanding |
| L6 | **Workflow & Release** | Orchestration and release confidence |
| L7 | **Marketplace & SDK** | Extensibility via plugins |
| L8 | **Enterprise Integration** | External system connectors |

## Quick Start

```bash
# 1. Clone and setup
git clone <repo>
cd PAIOS

# 2. Start infrastructure
docker-compose -f infra/docker/docker-compose.yml up -d

# 3. Install backend dependencies
cd apps/api
pip install -r requirements.txt
uvicorn main:app --reload

# 4. Install frontend dependencies (new terminal)
cd apps/web
npm install
npm run dev

# 5. Open http://localhost:3000
```

## Features

- **AI Test Generation** — Natural language to Playwright tests
- **Self-Healing Engine** — Auto-repair broken locators
- **Root Cause Intelligence** — Automatic failure classification
- **Release Risk Scoring** — Go/No-Go decisions with confidence
- **Knowledge Graph** — Neo4j-powered engineering knowledge
- **Multi-Agent Orchestration** — LangGraph-based agent collaboration

## Tech Stack

- **Frontend**: Next.js 14, React 18, Tailwind CSS, TypeScript
- **Backend**: FastAPI, Python 3.11, SQLAlchemy, AsyncPG
- **AI/ML**: LangChain, LangGraph, OpenAI, Anthropic
- **Database**: PostgreSQL (relational), Neo4j (graph), Redis (cache)
- **Execution**: Playwright (browser automation)
- **Infra**: Docker, Docker Compose

## License

Apache 2.0
