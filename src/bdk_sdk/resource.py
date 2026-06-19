from __future__ import annotations

from pydantic import BaseModel

from .session import PurviewSession


class PurviewResourceClient:
    """Generic CRUD client for a Purview REST resource.

    Subclasses override class attributes and inherit ``apply``, ``get``,
    ``delete``, and ``list``.
    """

    base_path: str
    api_version: str
    resource_path: str
    spec_model: type[BaseModel]
    create_verb: str = "PUT"

    def __init__(self, session: PurviewSession) -> None:
        self.session = session

    # ------------------------------------------------------------------
    # Path helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _name_from_spec(spec: BaseModel) -> str:
        return getattr(spec, "name")

    def _list_path(self) -> str:
        return self.resource_path.rsplit("/{", 1)[0]

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------

    def apply(self, spec: BaseModel) -> dict | None:
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        path = self.resource_path.format(name=self._name_from_spec(spec))
        return self.session.request(
            self.create_verb, self.base_path, path, self.api_version, json=body
        )

    def get(self, name: str) -> dict | None:
        path = self.resource_path.format(name=name)
        return self.session.request("GET", self.base_path, path, self.api_version)

    def delete(self, name: str) -> dict | None:
        path = self.resource_path.format(name=name)
        return self.session.request("DELETE", self.base_path, path, self.api_version)

    def list(self) -> dict | None:
        return self.session.request("GET", self.base_path, self._list_path(), self.api_version)
