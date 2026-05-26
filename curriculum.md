# Weather App — 9-Day FastAPI Curriculum

A step-by-step plan to rebuild every concept from the blog project in a fresh
weather app. One focused part per day.

---

## What We're Building

A weather API that:

- Fetches live weather from an external API
- Stores search history in PostgreSQL
- Has user accounts with JWT authentication
- Includes tests, security middleware, and a Dockerfile

Every concept from the blog project, rebuilt deliberately, one at a time.

---

## Day 1 — Project Setup & First Endpoints

- Initialize project with `uv`, set up `pyproject.toml`
- Create `main.py` with `/` and `/health` routes
- Run with uvicorn, explore Swagger UI
- **Concept focus:** project structure, the ASGI server, auto-generated docs
- **Deliverable:** a running API with two working endpoints

## Day 2 — Calling the External Weather API

- Add `httpx`, set up an async client with lifespan
- Build a `/weather?city=` endpoint that geocodes a city and fetches live weather
- **Concept focus:** async/await, external API calls, chained requests, error handling
- **Deliverable:** an endpoint returning real weather data

## Day 3 — Pydantic Schemas

- Define request/response models for weather data
- Add validation (city name length, query constraints)
- Use `response_model` to shape and filter output
- **Concept focus:** Pydantic, data validation, separating internal vs external data shapes
- **Deliverable:** clean, validated, well-typed responses

## Day 4 — Database Setup (PostgreSQL + SQLAlchemy)

- Create a `weather_app` PostgreSQL database and user
- Set up async engine, session, `get_db` dependency
- Define a `SearchHistory` model; create tables via lifespan
- **Concept focus:** ORM models, async sessions, dependency injection, connection management
- **Deliverable:** app connected to PostgreSQL with one table

## Day 5 — CRUD Routes (Search History)

- Save every weather lookup to the database
- Routes: list all searches, get one by ID, delete a search
- **Concept focus:** full CRUD, `select()` queries, `scalars()`, proper status codes, 404 handling
- **Deliverable:** weather searches persisted and retrievable

## Day 6 — User Accounts & JWT Authentication

- `User` model, registration with password hashing
- Login route issuing JWT tokens, `OAuth2PasswordBearer`
- Protect routes; tie search history to the logged-in user
- **Concept focus:** authentication, hashing, JWT, `Depends` for auth, per-user data
- **Deliverable:** registration, login, and protected endpoints

## Day 7 — Security Middleware

- Add security headers middleware (X-Frame-Options, CSP, HSTS)
- Add rate limiting and request-size-limit middleware
- Configure CORS and TrustedHost
- **Concept focus:** middleware, the `call_next` pattern, middleware ordering, cross-cutting concerns
- **Deliverable:** a hardened API

## Day 8 — Testing with pytest

- Set up `conftest.py` with fixtures (test DB, client, sample user)
- Write tests for weather, CRUD, and auth routes
- Use a separate test database; mock the external weather API
- **Concept focus:** fixtures, dependency overrides, test isolation, mocking external calls
- **Deliverable:** a passing automated test suite

## Day 9 — Dockerize the Application

- Write a hardened Dockerfile (non-root user, layer caching, healthcheck)
- Add `.dockerignore`
- Write `docker-compose.yml` to run FastAPI + PostgreSQL together
- **Concept focus:** containerization, image layers, secrets at runtime, multi-container apps
- **Deliverable:** a fully containerized, runnable project

---

## How We Work Each Day

1. Say **"Day N"** when ready to start that part
2. Concepts are taught with code and the reasoning behind each piece
3. Build it, then hit the **checkpoint** (a concrete "does it work" test)
4. Reply **"done"** — and stop there for the day
5. Next day: a quick recap, then the new part

---

## Tips for the 9 Days

- **Commit to Git after each day** — `git commit -m "Day N: ..."`. Nine clean
  commits show steady, consistent work on GitHub.
- **Keep a `notes.md`** in the project — write what each concept does in your
  own words. Teaching it to yourself locks it in.
- **Don't skip the checkpoints** — they catch problems early, while small.
- **If something breaks, paste the full error** — debug before moving on.

---

## End Result (Day 9)

- A complete, production-shaped FastAPI project on GitHub
- A genuine second project for the resume
- Every blog concept reinforced through deliberate repetition

---

## Progress Tracker

- [ ] Day 1 — Project Setup & First Endpoints
- [ ] Day 2 — Calling the External Weather API
- [ ] Day 3 — Pydantic Schemas
- [ ] Day 4 — Database Setup
- [ ] Day 5 — CRUD Routes
- [ ] Day 6 — User Accounts & JWT Authentication
- [ ] Day 7 — Security Middleware
- [ ] Day 8 — Testing with pytest
- [ ] Day 9 — Dockerize the Application