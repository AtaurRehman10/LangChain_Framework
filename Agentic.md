# 6-Month Roadmap: Becoming a Production Agentic AI Engineer
### Python + FastAPI · AI Integration · DevOps · System Design

---

## How to use this roadmap

**Calibration.** This assumes you already think like a senior backend engineer — you've shipped payment integrations, webhooks, OAuth2, BullMQ queues, WebSocket progress, Redis caching, and multi-tenant architecture. So this roadmap does **not** re-teach backend fundamentals. It does three things instead:

1. **Translates** your Node/NestJS instincts into idiomatic async Python + FastAPI (fast — you'll move through this in weeks, not months).
2. **Goes deep** on the genuinely new layer: LLMs, RAG, agents, workflow orchestration, and the system-design problems they create (non-determinism, token cost, streaming, durable long-running tasks, agent memory).
3. **Rounds out** DevOps so you can ship and operate it like a production system.

**Pace.** Built for ~10–15 focused hrs/week alongside a job. If you have more, compress; less, stretch. Every week is *learn + build* — you never just read.

**Philosophy.** Projects-first. One backend skeleton you build in Month 1 becomes the spine of everything else, and everything converges into one capstone. Publish as you go (GitHub + short write-ups) — it doubles as your portfolio and supports your AI/research career direction.

---

## You already know this — here's the Python equivalent

| You know (Node / NestJS) | Python / FastAPI equivalent |
|---|---|
| NestJS | FastAPI |
| TS types & interfaces | Python type hints + Pydantic v2 |
| class-validator / DTOs | Pydantic models |
| NestJS DI (providers) | FastAPI `Depends()` |
| Prisma / Mongoose | SQLAlchemy 2.0 (async) + Alembic |
| BullMQ | ARQ (async-native) → Celery (heavyweight) |
| Socket.IO | FastAPI WebSockets + SSE |
| Redis | Redis (same) |
| npm / pnpm | uv (or pip / poetry) |
| Jest | pytest |
| ESLint / Prettier | ruff |

---

## The stack you'll master (reference)

| Layer | Tools |
|---|---|
| **Language / tooling** | Python 3.12+, `uv` (env+deps), `ruff` (lint+format), `mypy` (types) |
| **Web framework** | FastAPI, Uvicorn (+Gunicorn in prod), Pydantic v2, pydantic-settings |
| **HTTP / async** | `httpx` (async), `asyncio`, `anyio` |
| **Database** | PostgreSQL, SQLAlchemy 2.0 async + asyncpg, Alembic |
| **Vector search** | pgvector (start) → Qdrant (scale); hybrid search (BM25 + dense) |
| **Cache & broker** | Redis |
| **Task queue** | ARQ (≈ your BullMQ) → Celery (the heavyweight standard) |
| **LLM providers** | Anthropic (Claude), OpenAI; Ollama / Groq for cheap/local iteration |
| **Agent frameworks** | **Pydantic AI** (typed, FastAPI-style — your primary), **LangGraph** (orchestration & durable state), OpenAI Agents SDK / Claude Agent SDK (provider-native) |
| **Tool integration** | **MCP** (Model Context Protocol — the tool standard) |
| **RAG** | LlamaIndex or Haystack (retrieval layer) or roll-your-own on pgvector; Ragas (eval) |
| **Embeddings** | OpenAI `text-embedding-3`; open: BGE / sentence-transformers |
| **Eval & observability** | Pydantic Logfire / LangSmith, OpenTelemetry (GenAI conventions), Ragas, Prometheus + Grafana, Sentry |
| **Testing** | pytest, pytest-asyncio, httpx `AsyncClient` |
| **DevOps** | Docker + docker-compose, GitHub Actions, AWS (ECR + App Runner/ECS Fargate/EC2, RDS, ElastiCache, Secrets Manager), Terraform (basics) |

> **Why Pydantic AI as your primary agent framework:** it's built by the Pydantic team (the validation layer under FastAPI) and brings FastAPI-style ergonomics — typed inputs, typed tool signatures, typed outputs, dependency injection — to agent code. It's the most natural on-ramp given your FastAPI goal. You'll add **LangGraph** for stateful/durable orchestration where the workflow itself is the product.

---

## Month-by-month overview

| Month | Theme | Headline project |
|---|---|---|
| **1** | Modern Python + production FastAPI foundations | Reusable production FastAPI backend template |
| **2** | LLM integration + RAG | Production RAG API (streaming, hybrid search, citations, evals) |
| **3** | Agents & tools (the core) | Tool-using agent (MCP tools, memory, guardrails, tracing) |
| **4** | Agentic workflows & orchestration | Durable multi-agent workflow orchestrator (queued, HITL) |
| **5** | DevOps & production hardening | The whole system containerized, CI/CD-deployed to AWS, observable |
| **6** | Capstone | Production-style agentic AI platform, end to end |

---

# Month 1 — Modern Python + Production FastAPI Foundations

**Goal:** Convert your backend skills into idiomatic async Python + FastAPI, and build a reusable production-grade backend skeleton you'll reuse all 6 months.

### Week 1 — Modern Python fluency (move fast)
- **Learn:** Python 3.12 idioms; type hints + `mypy`; Pydantic v2 vs dataclasses; **async/await** (event loop, coroutines, tasks, `gather`); context managers; `uv` for envs/deps; `src/` project layout; `ruff`.
- **Build:** An async CLI that calls 2–3 public APIs **concurrently** with `httpx` + `asyncio.gather`, validating responses with Pydantic v2. Wire up `uv` + `ruff` + `mypy` + `pytest` from day one.
- **System design:** layered architecture (router → service → repository), 12-factor config.

### Week 2 — FastAPI core
- **Learn:** routing, request/response models, `Depends()` dependency injection, `APIRouter`, middleware, exception handlers, lifespan events, pydantic-settings, auto OpenAPI; async vs sync endpoints.
- **Build:** A REST API (e.g. notes/tasks service) — full CRUD, layered architecture, typed schemas, centralized error handling, config management, request-logging middleware.
- **System design:** REST design (resources, status codes, pagination, versioning), DTO/schema separation, DI patterns.

### Week 3 — Persistence & migrations
- **Learn:** PostgreSQL + SQLAlchemy 2.0 **async** ORM + asyncpg; session-per-request via DI; Alembic migrations; connection pooling; repository pattern; transactions.
- **Build:** Add Postgres to the Week 2 API with async SQLAlchemy + Alembic; seed data; repository layer; Redis cache on one hot endpoint (cache-aside).
- **System design:** data modeling, indexing, connection pooling, caching strategy, N+1 avoidance.

### Week 4 — Auth, testing, hardening → ship the skeleton
- **Learn:** JWT/OAuth2 password flow, argon2 hashing, RBAC via dependency guards, rate limiting (`slowapi`), structured logging (`structlog`), pytest + pytest-asyncio + httpx `AsyncClient`, fixtures, coverage; CORS + security headers.
- **Build:** Add auth + RBAC + rate limiting + structured logging + a real test suite. Extract everything into a **"FastAPI production starter" template repo** — your reusable foundation.
- **System design:** authn/authz, rate limiting, **idempotency keys**, API reliability basics.

> ✅ **Milestone:** Production-ready FastAPI backend template.

---

# Month 2 — LLM Integration + RAG

**Goal:** Add AI to your backend cleanly, then build a production RAG API.

### Week 5 — LLM integration fundamentals
- **Learn:** chat completions (system/user messages, temperature, max tokens, stop); provider SDKs (Anthropic, OpenAI); async calls; **streaming via SSE**; token counting & cost; **structured outputs** (Pydantic-validated); failure handling (timeouts, retries, rate limits); run a local model with Ollama for free iteration.
- **Build:** An LLM service layer in your template — a `/chat` SSE-streaming endpoint, a **provider abstraction** (swap Anthropic/OpenAI/Ollama), token+cost logging, retry/backoff, and a structured-extraction endpoint returning Pydantic-validated JSON.
- **System design:** calling slow external APIs (async, timeouts, **circuit breaker**), streaming/SSE architecture, **semantic + response caching**, provider rate-limit handling, **cost/token budgeting**.

### Week 6 — Embeddings & vector search
- **Learn:** embeddings (dimensionality, similarity); embedding models (`text-embedding-3`, open BGE/sentence-transformers); **pgvector** (HNSW vs IVFFlat, distance ops); chunking; metadata filtering.
- **Build:** A semantic search API: ingest → chunk → embed → store in pgvector → query with similarity + metadata filters. Add **hybrid search** (BM25 + vector).
- **System design:** vector search architecture, index selection (HNSW vs IVFFlat), hybrid retrieval, when to move pgvector → Qdrant. *(Rule of thumb in 2026: pgvector is enough for the majority of workloads under ~10M vectors; reach for Qdrant when you need fast filtered search or sub-10ms latency at scale.)*

### Week 7 — RAG pipeline
- **Learn:** RAG architecture (retrieve → augment → generate); chunk/overlap tuning; re-ranking; context-window management; grounding & citations; retrieval framework (LlamaIndex/Haystack) vs roll-your-own; handling "I don't know."
- **Build:** A full RAG API — upload docs (PDF/markdown), **async/queued ingestion**, retrieval + re-ranking, grounded answers **with citations**, streaming. Built on your pgvector store.
- **System design:** ingestion pipelines (async/queued), document processing at scale, retrieval-quality vs latency tradeoffs, embedding/retrieval caching.

### Week 8 — RAG evaluation & productionizing
- **Learn:** RAG eval with **Ragas** (faithfulness, answer relevance, context precision/recall); building eval sets; LLM observability (Logfire/LangSmith); guardrails (input validation, output filtering); prompt-injection basics.
- **Build:** Add a Ragas eval harness with a test set; wire tracing; add guardrails; improve retrieval. **Deploy this RAG API live** (Render/Railway/Fly.io) — your first public AI service.
- **System design:** observability for AI (traces/metrics), eval-driven development, guardrails architecture.

> ✅ **Milestone:** Production RAG API — streaming, hybrid search, citations, evals, tracing, deployed.

---

# Month 3 — Agents & Tools (the core differentiator)

**Goal:** Build real tool-using, multi-step-reasoning agents.

### Week 9 — Agent fundamentals & tool calling
- **Learn:** what an agent is (LLM + tools + loop + memory); function/tool calling; the **ReAct** loop (reason → act → observe); typed tool schemas; **when *not* to use an agent** (prompt chaining, routing, parallelization often beat agents — read Anthropic's *Building Effective Agents*). Adopt **Pydantic AI** as your primary framework.
- **Build:** A single tool-using agent with Pydantic AI: 2–3 typed tools (calculator, web-search API, a DB-query tool over your Postgres). Expose via a FastAPI endpoint that **streams intermediate steps**.
- **System design:** tool execution safety, structured I/O contracts, **idempotency for non-deterministic calls**, per-tool retry/timeout.

### Week 10 — MCP (the tool standard) + more capable agents
- **Learn:** **Model Context Protocol (MCP)** — now the industry-standard way agents connect to tools/data (donated to the Linux Foundation in late 2025, supported by Anthropic, OpenAI, Google); MCP servers vs clients; consuming and **building your own** MCP server; tool-design best practices (narrow scope, clear descriptions, useful error messages back to the model).
- **Build:** Build a **custom MCP server** exposing your app's DB / an external API. Connect your agent to it + 1–2 existing MCP servers. Refactor the agent to use MCP tools.
- **System design:** capability/tool architecture, MCP as integration layer, secure tool access (auth, scoping, **sandboxing**), multi-tenant tool isolation.

### Week 11 — Agent memory & state
- **Learn:** memory types — short-term/conversation, episodic, semantic, procedural; session management; persisting agent state; vector store as long-term memory; **context compaction** for long conversations.
- **Build:** Add memory to your agent — conversation sessions (Redis/Postgres), long-term memory via pgvector, context compaction. A stateful chat agent that remembers across sessions.
- **System design:** stateful service design, session storage, memory architecture, **concurrency/race conditions** in agent state.

### Week 12 — Reliability & evaluation for agents
- **Learn:** agent failure modes (loops, hallucinated tools, runaway cost); guardrails (max steps, cost/token caps, output validation); **agent evals** (trajectory + task-success); prompt-injection & tool-use security; agent observability (OpenTelemetry **GenAI semantic conventions**, finalized 2026 — trace every tool call, token, decision).
- **Build:** Harden the agent — step/cost limits, tool-call validation, full **trajectory tracing**, a task-success eval suite, and **human-in-the-loop approval** for sensitive tools.
- **System design:** reliability for non-deterministic systems, cost controls, observability, security (injection defense, sandboxing).

> ✅ **Milestone:** Production-grade tool-using agent — MCP tools, memory, guardrails, tracing, evals — behind a FastAPI API.

---

# Month 4 — Agentic Workflows & Orchestration

**Goal:** Multi-step workflows, multi-agent systems, durable long-running execution.

### Week 13 — Workflow orchestration with LangGraph
- **Learn:** **LangGraph** (the production standard for stateful agent workflows): nodes/edges, state, conditional branching, cycles, **checkpointing/persistence**, time-travel debugging; mapping a workflow to a state machine; when graph orchestration beats a simple loop.
- **Build:** Re-implement a multi-step workflow as a LangGraph graph — e.g. a research agent: plan → search → read → synthesize → critique → finalize, with branching, retries, and **checkpointed state**.
- **System design:** workflow as state machine, durable execution, checkpointing/recovery, branching/looping control.

### Week 14 — Long-running tasks & queues
- **Learn:** why long agent runs can't live in a request (timeouts, scaling); background queues — **ARQ** (async-native, Redis-based, closest to your BullMQ experience) or Celery; job status tracking; **progress streaming** (WebSocket/SSE — your Socket.IO instinct); job idempotency & retries.
- **Build:** Move long agent workflows into an **ARQ worker**. FastAPI enqueues a job → returns a job ID → client subscribes (WebSocket) for progress → results persisted. Durable, resumable runs.
- **System design:** queue architecture, worker pools, **idempotency**, fan-out/fan-in, backpressure, decoupling API from compute.

### Week 15 — Multi-agent systems
- **Learn:** multi-agent patterns — **supervisor / orchestrator-worker**, role-based crews, handoffs; when multi-agent helps vs hurts (cost, latency, complexity — a 4-agent debate is 20+ LLM calls); coordination & specialization. Compare LangGraph supervisor vs CrewAI (roles) vs OpenAI Agents SDK (handoffs).
- **Build:** A multi-agent workflow — a supervisor routing to specialists (researcher, analyst, writer) over shared state in LangGraph, with HITL checkpoints.
- **System design:** multi-agent coordination, shared state, message passing, concurrency, cost/latency budgeting.

### Week 16 — Human-in-the-loop & advanced control
- **Learn:** HITL patterns (approval gates, **interrupts**, resume); LangGraph interrupts; pausing/resuming durable workflows; audit trails; streaming reasoning to a UI; managing many concurrent runs.
- **Build:** Add durable **pause-for-approval / resume-on-approval** to your orchestrator, with full audit logging. Turn it into a workflow-orchestrator API managing many concurrent runs.
- **System design:** HITL architecture, durable pause/resume, auditability, concurrency at scale, long-running-workflow observability.

> ✅ **Milestone:** Workflow orchestrator — durable, multi-agent, queued, HITL, with progress streaming.

---

# Month 5 — DevOps & Production Hardening

**Goal:** Containerize, automate, deploy, observe, secure, and control costs.

### Week 17 — Docker & containerization
- **Learn:** Docker images/layers, **multi-stage builds**, Python Dockerfile best practices (slim base, `uv`, non-root, layer caching), docker-compose, `.dockerignore`, health checks.
- **Build:** Containerize the agent backend — multi-stage Dockerfile + docker-compose (app + Postgres/pgvector + Redis + ARQ worker) with health checks. One command spins up the whole stack.
- **System design:** containerization, service composition, health checks, local/prod parity.

### Week 18 — CI/CD
- **Learn:** GitHub Actions (workflows, jobs, caching); CI (lint → type-check → test → build); CD (push to registry → deploy); secrets in CI; branch protection. (Lean on your payment-integration testing rigor here.)
- **Build:** Full GitHub Actions pipeline — on PR run `ruff` + `mypy` + `pytest`; on merge build & push image (GHCR/ECR) and deploy. Add **eval gates** (fail the build if RAG/agent evals regress).
- **System design:** CI/CD design, deploy strategies (rolling/blue-green basics), **eval-as-CI-gate**, supply-chain basics.

### Week 19 — Cloud deployment (AWS) + cost control
- **Learn:** AWS for backends — ECR + a compute choice (App Runner / Lightsail / ECS Fargate / EC2); RDS Postgres (with pgvector) + ElastiCache Redis; load balancing; Secrets Manager; **budgets + billing alarms + auto-shutdown for non-prod**. Cheaper learning alt: Render/Railway/Fly.io.
- **Build:** Deploy the full containerized stack to AWS (App Runner or ECS Fargate for API+worker, RDS, ElastiCache). **Set up budgets, billing alarms, and a non-prod auto-stop first.** Secrets via Secrets Manager.
- **System design:** cloud architecture, managed vs self-hosted, load balancing, secrets management, **cost/capacity planning**, scaling policies.

> ⚠️ Given your past AWS billing surprises: do the **budget + billing alarm + cost-anomaly alert** in the first hour, before you deploy anything. Tag non-prod resources and schedule them off overnight.

### Week 20 — Observability, monitoring & security
- **Learn:** the three pillars (logs, metrics, traces) **+ LLM-specific** (token usage, tool calls, latency, cost/request via OpenTelemetry GenAI conventions); Prometheus + Grafana; Sentry; alerting; security (prompt-injection defense, secrets, dependency scanning, input/output validation, PII handling, rate limiting & abuse protection).
- **Build:** Full observability stack — OTel tracing (incl. LLM/agent spans) → Logfire/LangSmith/Grafana; dashboards (latency, cost, error rate, tokens); Sentry; alerts on cost/error thresholds. Run a security pass (injection tests, secret scan, dependency audit, rate limits).
- **System design:** observability architecture, SLOs/alerting, AI security architecture, cost monitoring, incident readiness.

> ✅ **Milestone:** Your agent backend is containerized, CI/CD-deployed to AWS, fully observable, secured, and cost-controlled.

---

# Month 6 — Capstone: Production Agentic AI Backend

**Goal:** Combine everything into one cohesive, portfolio-grade system — then polish and present.

### Week 21 — Capstone design & scaffolding
- **Do:** Scope it, then write a **system design doc** — requirements, architecture diagram, data model, API design, agent/workflow design, scaling & reliability plan, cost plan, observability plan. Start the repo from your Month-1 template.
- **Build:** Architecture + scaffolding (FastAPI, Postgres/pgvector, Redis, ARQ worker, Docker, CI skeleton, observability wiring); define the agent/workflow design.
- **System design:** end-to-end design, capacity planning, failure-mode analysis.

### Week 22 — Capstone core: AI + agents
- **Build:** RAG over ingested data; the multi-agent workflow (orchestrator + specialists + MCP tools); durable long-running execution via the queue; memory; streaming; HITL approval. Structured outputs and grounded answers throughout.

### Week 23 — Capstone hardening: DevOps + reliability
- **Build:** Multi-stage Docker; full CI/CD with eval gates; deploy to AWS with budgets/alarms; observability (traces/metrics/dashboards/alerts); security pass; **load test**; rate limiting; graceful degradation; the eval suite (RAG + agent task-success) wired as a CI gate.
- **System design:** reliability/scalability review, load testing, graceful degradation, rollback.

### Week 24 — Polish, document, present
- **Do:** README + architecture docs + demo; record a walkthrough; write a **technical case-study blog post** (great for portfolio and your AI/research direction); document tradeoffs and "what I'd do next." Optionally open-source it.

---

## The Capstone (in detail)

**A production-style Agentic AI backend** — a multi-agent platform with full AI integration and a complete DevOps pipeline. Below is domain-flexible; specialize it however you like (a research assistant, a customer-support agent, an ops copilot — you could even point it at a real domain you know, like product/market research for ZARAKI, or a support agent over a Bleaum-style knowledge base).

**What it does**
- Ingests documents/data into a **RAG knowledge base** (chunk → embed → pgvector, hybrid search, citations).
- Exposes a **chat + task API**. An **orchestrator agent** can: answer grounded questions over the KB; run **multi-step research** using tools (web search, internal DB queries, calculations, external APIs via **MCP**); and execute **workflows** ("research X → analyze → draft report → save").
- Runs long tasks **durably** via an ARQ queue with **resumability + progress streaming** (WebSocket/SSE).
- **Human-in-the-loop** approval gates for sensitive actions, with audit trails.
- **Per-tenant isolation** (lean on your Bleaum multi-tenant experience).

**Architecture**

```
Client ──> FastAPI (API gateway: auth, RBAC, rate limit, SSE/WebSocket)
              │
              ├── LLM service layer (provider abstraction: Claude/OpenAI/Ollama)
              ├── RAG service (pgvector hybrid retrieval + re-ranking + citations)
              ├── Agent/orchestration (Pydantic AI agents + LangGraph workflows)
              │        └── Tools via MCP server(s)  ─── sandboxed, scoped, audited
              └── enqueue long jobs ──> Redis ──> ARQ worker pool
                                                    └── durable, checkpointed runs
Data:   PostgreSQL + pgvector  ·  Redis (cache + broker + sessions)
Observe: OpenTelemetry (incl. GenAI spans) → Logfire/LangSmith + Grafana + Sentry
Deploy:  Docker → GitHub Actions (lint/type/test/eval gate) → AWS (ECR + App Runner/Fargate, RDS, ElastiCache, Secrets Manager)  ·  budgets + alarms
```

**How each month feeds in**
- **M1** → the FastAPI spine, auth, persistence, testing.
- **M2** → RAG knowledge base + streaming + provider abstraction + evals.
- **M3** → the agent loop, MCP tools, memory, guardrails.
- **M4** → durable multi-agent workflows, queue, HITL.
- **M5** → Docker, CI/CD, AWS deploy, observability, security, cost control.
- **M6** → assembled, hardened, load-tested, documented, deployed.

**Definition of done**
1. Live on AWS, reachable, with budgets + alarms active.
2. CI/CD: every merge runs lint + types + tests + **eval gate**, then deploys.
3. Observable: dashboards for latency, error rate, **token cost**, tool-call traces.
4. Reliable: long tasks survive worker restarts (checkpointing); per-tool retries; graceful degradation.
5. Secure: auth + RBAC, rate limiting, injection-tested, secrets managed, tool sandboxing.
6. Evaluated: RAG metrics (Ragas) + agent task-success suite, both gating CI.
7. Documented: architecture doc, README, demo, case-study write-up.

---

## Milestones & portfolio checklist

- [ ] **M1** — Reusable production FastAPI starter template (auth, DB, migrations, tests, logging, config)
- [ ] **M2** — Production RAG API (streaming, hybrid search, citations, Ragas evals, tracing) — *deployed live*
- [ ] **M3** — Tool-using agent (MCP tools, memory, guardrails, trajectory tracing, evals)
- [ ] **M4** — Durable multi-agent workflow orchestrator (queued, checkpointed, HITL, progress streaming)
- [ ] **M5** — Full DevOps: Dockerized, CI/CD to AWS, observability, security pass, cost controls
- [ ] **M6** — Capstone: production agentic AI platform + technical case-study write-up

**Core references** (search these by name):
- Anthropic — *Building Effective Agents* (agent design patterns — read in Month 3)
- Anthropic Cookbook (Claude agent recipes)
- FastAPI official docs (the best framework docs you'll find)
- Pydantic AI docs · LangGraph docs · Model Context Protocol (MCP) docs
- Ragas docs (RAG evaluation) · OpenTelemetry GenAI semantic conventions
- Chip Huyen — *AI Engineering* (O'Reilly) for the systems view

---

*Adjust freely — if a week clicks fast, pull the next one forward; if a concept fights you, give it the extra days. The arc matters more than the calendar.*