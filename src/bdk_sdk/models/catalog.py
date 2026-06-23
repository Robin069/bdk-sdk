"""Business Domain (Unified Catalog) models.

Generated from TypeSpec via ``@azure-tools/typespec-autorest`` and
``datamodel-code-generator``, with a hand-written Spec wrapper for
create/update operations.
"""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field

from ._generated.unified_catalog import Domain


class BusinessDomainSpec(BaseModel):
    """Input spec for creating or updating a business domain.

    Accepts a flat dict::

        {"name": "Sales", "parentId": "<uuid>", "description": "..."}

    The ``id`` field (UUID) is assigned server-side on creation and is
    excluded from the API request body.  For update operations the id
    is passed as a separate ``domain_id`` argument to the client.
    """

    name: str = Field(description="Domain name")
    parent_id: str | None = Field(default=None, alias="parentId", description="Parent domain UUID")
    description: str | None = None
    status: str | None = None
    type: str | None = None
    is_restricted: bool | None = Field(default=None, alias="isRestricted")
    thumbnail: dict[str, Any] = Field(default_factory=dict)
    domains: list[dict[str, Any]] = Field(default_factory=list)
    managed_attributes: list[dict[str, Any]] = Field(
        default_factory=list, alias="managedAttributes"
    )

    model_config = {"populate_by_name": True}

    def to_domain_response(self, domain_id: str) -> Domain:
        """Convert to a validated Domain model for deserialising responses."""
        return Domain.model_validate(
            {
                "id": domain_id,
                "name": self.name,
                "parentId": self.parent_id or domain_id,
                "description": self.description,
                "status": self.status or "DRAFT",
                "type": self.type,
                "isRestricted": False if self.is_restricted is None else self.is_restricted,
                "systemData": {},
                "thumbnail": self.thumbnail,
                "domains": self.domains,
                "managedAttributes": self.managed_attributes,
            }
        )
