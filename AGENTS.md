# AGENTS.md — bdk-sdk

## Quickstart

```bash
# Environment auto-activates via direnv (layout uv). Python 3.13+ required.
uv sync                # install deps + dev deps
uv run pytest          # all tests with coverage
uv run pytest tests/test_session.py::TestPurviewClient::test_init_populates_state  # single test
uv run ruff check src/ tests/         # lint
uv run ruff format src/ tests/        # format (DO before committing)
```

## Critical: import-time env vars

`src/bdk_sdk/session.py` reads `AZURE_TOKEN_URL`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_RESOURCE` **at module import time** (not lazily). If any is missing the import itself raises `ValueError`. Tests handle this in `tests/conftest.py` by setting dummy values via `os.environ.setdefault` at module top, before any test module imports execute. If you add a new `_require_env("SOME_VAR")` at module level, add a corresponding dummy to conftest.

## Tooling

| Tool | Config | Notes |
|------|--------|-------|
| Package manager | `uv` (`uv.lock`, `uv_build`) | `uv run`, `uv sync`, `uv add --dev` |
| Python | `>=3.13` (`.python-version: 3.13`) | Uses `str \| None` syntax |
| Lint/format | `ruff` | line-length 99, double quotes, 4-space indent |
| Tests | `pytest` + `pytest-cov` | Coverage to HTML at `tests/artifacts/htmlcov` |
| Codegen | `datamodel-code-generator` (>=0.64) | Generate pydantic v2 models from OpenAPI specs |

No CI or pre-commit hooks exist. Run lint + format + tests locally.

## Architecture

Current state (`session.py`): `PurviewBaseClient` eagerly authenticates on `__init__`, bakes one api-version into the session. This is being refactored per the plan below.

**Planned architecture** (see `.cursor/plans/purview_sdk_foundation_20b3ffca.plan.md`):

```
Settings (pydantic-settings) → PurviewSession (lazy-auth transport)
  → PurviewResourceClient (generic CRUD base)
    → DataSourceClient (concrete, /scan @ 2023-09-01)
```

Module layout target:
- `config.py` — `Settings` class (endpoint + AZURE_* vars), removes import-time globals
- `auth.py` — auth/crypto helpers moved from `session.py`
- `session.py` — `PurviewSession` (lazy auth, URL building, 401-refresh-retry)
- `resource.py` — `PurviewResourceClient` (apply/get/delete/list)
- `models/_generated/scanning.py` — committed codegen output, **exclude from coverage**
- `models/datasource.py` — `DataSourceSpec` wrapper
- `loader.py` — `load_spec(path, model)` YAML → pydantic
- `datasources.py` — `DataSourceClient`

## Codegen

API specs are vendored in `api-specs/purview/`. The specs are Swagger 2.0 and must be
converted to OpenAPI 3.0 before codegen. To regenerate models:

```bash
# Step 1: Convert Swagger 2.0 definitions to OAS 3.0 components/schemas
# The converter flattens allOf chains, converts discriminators to oneOf, and fixes $ref paths.
python3 scripts/convert_swagger_to_oas3.py \
  api-specs/purview/data-plane/scanning/stable/2023-09-01/scanningService.json \
  /tmp/oas3_spec.json

# Step 2: Generate pydantic v2 models
uv run datamodel-codegen \
  --input /tmp/oas3_spec.json \
  --input-file-type openapi \
  --output src/bdk_sdk/models/_generated/scanning.py \
  --output-model-type pydantic_v2.BaseModel \
  --use-annotated \
  --enum-field-as-literal all
```

Generated models are committed. Exclude `models/_generated` from coverage in `pyproject.toml` pytest `addopts` when added.

## Conventions

- All HTTP calls must be mocked in tests — no live network.
- Use `pydantic>=2.13` with `model_validate`, `model_dump(by_alias=True, exclude_none=True, exclude_unset=True)` for serialization.
- JWT tokens use `expires_on` (integer timestamp), not `expires_in`.
- Tests use `FakeResponse` from conftest fixture (not `responses` or `httpx`).
- Use `monkeypatch` for environment variables and time, `mock` for network calls.
