# Repository Guidelines

## Project Structure & Module Organization
FastAPI lives under `src/`; `main.py` bootstraps routers from `src/routes/`. Conversation workflows sit in `src/ai_cores/` (chat, diary, remake), shared schemas in `src/models/`, helpers in `src/utils/`, and prompts in `src/config/llm_config.yaml`. Static assets for the lightweight landing page are in `src/static/`. Keep new features modular: add Pydantic models next to their routes, put orchestration inside the matching `ai_cores` module, and register routers in `src/routes/__init__.py`.

## Build, Test, and Development Commands
- `uv sync` — installs Python 3.11 dependencies defined in `pyproject.toml` and `uv.lock`.
- `uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000` — starts the API with hot reload for localhost work.
- `uv run pytest` — runs the Pytest suite (add tests under `tests/`; see below).
- `docker build -t aneuk-ai .` / `docker run -p 8000:8000 --env-file .env aneuk-ai` — container workflow mirroring production.

## Coding Style & Naming Conventions
Use Black-compatible 4-space indentation, explicit type hints, and FastAPI dependency injection as shown in `src/routes/chat.py`. Pydantic request/response objects stay suffixed with `Request`/`Response`, and routers use `snake_case` file names with `router = APIRouter(...)`. Keep config and prompt data in YAML/TXT under `src/config` or `src/utils/dictionary`, loading them through helpers instead of hardcoding. Prefer async functions for all LLM or network calls.

## Testing Guidelines
Pytest plus `httpx.AsyncClient`/`fastapi.testclient` is the expected stack. Mirror the module path inside `tests/` (e.g., `tests/routes/test_chat.py`) and name files/functions `test_*`. Aim for ≥80 % branch coverage around `ai_cores` logic and emotion parsing utilities; stub OpenAI/LangChain calls via fixtures so runs stay deterministic. Run `uv run pytest --maxfail=1 --disable-warnings -q` before every PR.

## Commit & Pull Request Guidelines
Recent history (`git log`) shows short, imperative subject lines such as `Add fallback LLM support...`; follow that pattern, sticking to ≤72 characters and present tense verbs. Each PR should include: problem/solution summary, linked issue or task ID, validation notes (tests, manual endpoint calls like `POST /ai/diary`), and screenshots or sample JSON when the response schema changes. Request review from another backend contributor whenever touching `ai_cores` or auth logic.

## Security & Configuration Tips
Copy `.env-example` to `.env`, fill OpenAI/Google keys, and never commit secrets. The `get_protected_docs` helper and `/test/auth` route show how protected endpoints expect tokens—reuse those utilities instead of reimplementing auth. Keep generated diary/emotion files out of version control.
