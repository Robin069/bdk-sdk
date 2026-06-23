"""Client for Unified Catalog business domain operations.

Endpoints:
  Create  → POST  /businessdomains
  Update  → PUT   /businessdomains/{name}
  Get     → GET   /businessdomains/{name}
  Delete  → DELETE /businessdomains/{name}
  List    → GET   /businessdomains

API version: ``2026-03-20-preview``.
"""

from __future__ import annotations

from .models.catalog import BusinessDomainSpec
from .resource import PurviewResourceClient


class BusinessDomainClient(PurviewResourceClient):
    """Client for governance business domains under ``/datagovernance/catalog``.

    Create issues a ``POST`` (no id in the URL — the id is server-assigned),
    while update issues a ``PUT`` (id extracted from ``spec.id``).
    ``add`` and ``update`` are aliases over ``apply``.
    """

    base_path = "/datagovernance/catalog"
    api_version = "2026-03-20-preview"
    resource_path = "/businessdomains/{name}"
    spec_model = BusinessDomainSpec

    @staticmethod
    def _name_from_spec(spec: BusinessDomainSpec) -> str:
        return spec.id or spec.name

    def apply(self, spec: BusinessDomainSpec) -> dict | None:
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        if spec.id:
            path = self.resource_path.format(name=self._name_from_spec(spec))
            verb = "PUT"
        else:
            path = self._list_path()
            verb = "POST"
        return self.session.request(verb, self.base_path, path, self.api_version, json=body)

    def add(self, spec: BusinessDomainSpec) -> dict | None:
        return self.apply(spec)

    def update(self, spec: BusinessDomainSpec) -> dict | None:
        return self.apply(spec)
