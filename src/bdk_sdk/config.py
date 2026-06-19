from __future__ import annotations

import os
from urllib.parse import urlparse

from pydantic import BaseModel, model_validator


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} is not set")
    return value


class Settings(BaseModel):
    endpoint: str
    tenant_id: str
    client_id: str
    resource: str
    token_url: str

    @model_validator(mode="after")
    def _validate_token_url(self) -> "Settings":
        try:
            result = urlparse(self.token_url)
            valid = all([result.scheme, result.netloc])
            if not valid:
                raise ValueError(f"token_url is not a valid URL: {self.token_url}")
        except ValueError:
            raise ValueError(f"token_url is not a valid URL: {self.token_url}")
        return self

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            endpoint=_require_env("AZURE_PURVIEW_ENDPOINT"),
            tenant_id=_require_env("AZURE_TENANT_ID"),
            client_id=_require_env("AZURE_CLIENT_ID"),
            resource=_require_env("AZURE_RESOURCE"),
            token_url=_require_env("AZURE_TOKEN_URL"),
        )
