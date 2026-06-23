"""Client for Unified Catalog business domain operations.

Endpoints: ``POST /businessdomains``, ``PUT /businessdomains/{domainId}``,
``GET /businessdomains/{domainId}``, ``DELETE /businessdomains/{domainId}``,
``GET /businessdomains``.

API version: ``2026-03-20-preview``.
"""

from __future__ import annotations

from uuid import UUID

from .models.catalog import BusinessDomainSpec
from .session import PurviewSession

BASE_PATH = "/datagovernance/catalog"
API_VERSION = "2026-03-20-preview"


class BusinessDomainClient:
    """Client for governance business domains under ``/datagovernance/catalog``."""

    def __init__(self, session: PurviewSession) -> None:
        self.session = session

    def create(self, spec: BusinessDomainSpec) -> dict | None:
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        return self.session.request("POST", BASE_PATH, "/businessdomains", API_VERSION, json=body)

    def update(self, domain_id: str | UUID, spec: BusinessDomainSpec) -> dict | None:
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        return self.session.request(
            "PUT",
            BASE_PATH,
            f"/businessdomains/{domain_id}",
            API_VERSION,
            json=body,
        )

    def get(self, domain_id: str | UUID) -> dict | None:
        return self.session.request(
            "GET",
            BASE_PATH,
            f"/businessdomains/{domain_id}",
            API_VERSION,
        )

    def delete(self, domain_id: str | UUID) -> dict | None:
        return self.session.request(
            "DELETE",
            BASE_PATH,
            f"/businessdomains/{domain_id}",
            API_VERSION,
        )

    def list(self) -> dict | None:
        return self.session.request(
            "GET",
            BASE_PATH,
            "/businessdomains",
            API_VERSION,
        )
