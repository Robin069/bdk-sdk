# bdk-sdk

Python SDK for [Microsoft Purview](https://learn.microsoft.com/en-us/purview/)
data-plane REST APIs. Uses certificate-based service principal authentication
(JWT client assertion) and pydantic v2 models generated from the vendored
OpenAPI specifications.

## Quickstart

**Requirements:** Python 3.13+, [uv](https://docs.astral.sh/uv/)

```bash
uv sync                            # install deps + dev deps
uv run pytest                      # all tests with coverage
```

### Environment variables

| Variable | Description |
|---|---|
| `AZURE_PURVIEW_ENDPOINT` | Purview account endpoint (e.g. `https://myaccount.purview.azure.com`) |
| `AZURE_TENANT_ID` | Azure AD tenant ID |
| `AZURE_CLIENT_ID` | Service principal application (client) ID |
| `AZURE_RESOURCE` | Token audience, typically `https://purview.azure.com` |
| `AZURE_TOKEN_URL` | OAuth2 token endpoint (e.g. `https://login.microsoftonline.com/{tenant}/oauth2/token`) |

Variables are read at call time via `Settings.from_env()` — not at module import time.

## Architecture

```
Settings ──→ PurviewSession ──→ PurviewResourceClient ──→ DataSourceClient
             (lazy auth,         (generic CRUD base)       (/scan @ 2023-09-01)
              URL building,
              401 retry)
```

| Module | Purpose |
|---|---|---|
| `config.py` | `Settings` — reads Azure env vars, validates the token URL |
| `auth.py` | Certificate loading, JWT client assertion, token acquisition |
| `session.py` | `PurviewSession` — lazy authentication, per-call `api-version`, automatic 401 refresh-and-retry |
| `resource.py` | `PurviewResourceClient` — generic `apply`/`get`/`delete`/`list` base class |
| `models/_generated/` | Codegen pydantic v2 models from vendored Swagger specs (excluded from coverage) |
| `models/datasource.py` | `DataSourceSpec` wrapper over the generated `DataSource` discriminated union |
| `models/domain.py` | `Domain`, `DomainSpec`, and `SystemData` — manually written from live API traces |
| `loader.py` | `load_spec(path, model)` — YAML to validated pydantic |
| `datasources.py` | `DataSourceClient` — concrete client for `/scan/datasources` |

## Usage

### Data Sources

```python
from pathlib import Path
from bdk_sdk import Settings, PurviewSession
from bdk_sdk.datasources import DataSourceClient
from bdk_sdk.loader import load_spec
from bdk_sdk.models.datasource import DataSourceSpec

# 1. Load configuration from environment
settings = Settings.from_env()

# 2. Create an authenticated session (authentication is lazy)
session = PurviewSession(
    settings,
    private_key_path=Path("key.pem"),
    certificate_path=Path("cert.pem"),
)

# 3. Create a data source client
client = DataSourceClient(session)

# 4. Load a data source specification from YAML
spec = load_spec("my-datasource.yaml", DataSourceSpec)

# 5. Upsert the data source
client.apply(spec)

# 6. Other operations
client.get("my-datasource")
client.list()
client.delete("my-datasource")

# add / update are aliases for apply (the API is a single PUT upsert)
client.add(spec)
client.update(spec)
```

### Governance Domains

```python
from bdk_sdk.models.domain import DomainSpec, Domain, DomainList

# Create or update a domain
spec = DomainSpec.model_validate({
    "name": "my-domain",
    "friendlyName": "My Domain",
    "description": "Optional description",
    "environment": "Prod",       # "Prod" (default) or "Test"
})

# Parse an API response
domain = Domain.model_validate(response_json)
print(domain.friendly_name)
print(domain.provisioning_state)

# Parse a list response
domains = DomainList.model_validate(list_response_json)
for d in domains.value:
    print(d.name)

# YAML loading is supported (accepts both camelCase and snake_case)
spec = load_spec("my-domain.yaml", DomainSpec)
```

### YAML specification format

```yaml
# my-datasource.yaml
name: my-adls-gen2
kind: AdlsGen2
properties:
  endpoint: https://mystorage.dfs.core.windows.net/
  collection:
    referenceName: Collection-abc
```

The `kind` field must match one of the values in the `DataSourceType` enum
(`AdlsGen1`, `AdlsGen2`, `AzureStorage`, `AzureSqlDatabase`, `Snowflake`, etc.).

#### Domain YAML

```yaml
# my-domain.yaml
name: my-domain
friendlyName: My Domain
description: Optional description
environment: Prod
```

## Models

Most models in `models/_generated/` are produced by `datamodel-code-generator`
from the vendered Swagger 2.0 specs.  Some models are written manually when
the public spec is out of date or missing operations:

| Model | Source | Notes |
|---|---|---|
| `models/_generated/scanning.py` | Codegen from `scanningService.json` | Excluded from test coverage |
| `models/datasource.py` | Manual wrapper over generated `DataSource` | Adds `name`, excludes readOnly fields |
| `models/domain.py` | Manual | Based on `2023-10-01-preview` spec + live `2023-12-01-preview` traces |

## Development

```bash
uv sync                          # install dependencies
uv run pytest                    # run tests (80 tests, 100% coverage on hand-written modules)
uv run ruff check src/ tests/    # lint
uv run ruff format src/ tests/   # format (run before committing)
```

### Tooling

| Tool | Purpose |
|---|---|
| [uv](https://docs.astral.sh/uv/) | Package management, virtual environment |
| [pytest](https://docs.pytest.org/) + `pytest-cov` | Test runner, coverage to `tests/artifacts/htmlcov/` |
| [ruff](https://docs.astral.sh/ruff/) | Lint + format (line-length 99, double quotes, 4-space indent) |
| [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) | Generate pydantic v2 models from OpenAPI specs |

### Code generation

API specifications are vendored in `api-specs/purview/`. They are
**Swagger 2.0** format and must be converted to OpenAPI 3.0 before code
generation:

```bash
# Convert Swagger 2.0 → OAS 3.0
python3 scripts/convert_swagger_to_oas3.py \
  api-specs/purview/data-plane/scanning/stable/2023-09-01/scanningService.json \
  /tmp/oas3_spec.json

# Generate pydantic v2 models
uv run datamodel-codegen \
  --input /tmp/oas3_spec.json \
  --input-file-type openapi \
  --output src/bdk_sdk/models/_generated/scanning.py \
  --output-model-type pydantic_v2.BaseModel \
  --use-annotated \
  --enum-field-as-literal all
```

Generated models are committed and excluded from test coverage.

### Conventions

- All HTTP calls are mocked in tests — no live network calls.
- Use `pydantic>=2.13` with `model_validate` and
  `model_dump(by_alias=True, exclude_none=True, exclude_unset=True)`.
- JWT tokens use `expires_on` (integer timestamp).
- Tests use `FakeResponse` from `conftest.py` (not `responses` or `httpx`).
- Use `monkeypatch` for environment variables and time, `mock` for network calls.
