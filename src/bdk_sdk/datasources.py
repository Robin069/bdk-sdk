from __future__ import annotations

from .models.datasource import DataSourceSpec
from .resource import PurviewResourceClient


class DataSourceClient(PurviewResourceClient):
    """Client for data-source resources under ``/scan/datasources``.

    The Purview API exposes a single PUT upsert (no separate create/update),
    so ``add`` and ``update`` are thin aliases over ``apply``.
    """

    base_path = "/scan"
    api_version = "2023-09-01"
    resource_path = "/datasources/{name}"
    spec_model = DataSourceSpec

    def add(self, spec: DataSourceSpec) -> dict | None:
        return self.apply(spec)

    def update(self, spec: DataSourceSpec) -> dict | None:
        return self.apply(spec)
