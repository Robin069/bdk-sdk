"""Governance Domain models.

Based on the ``2023-10-01-preview`` account API spec with adjustments for
the ``2023-12-01-preview`` behaviour observed from live requests/responses.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

ContainerType = Literal["Domain", "Collection"]

DomainEnvironment = Literal["Prod", "Test"]

CreatedByType = Literal["User", "Application", "ManagedIdentity", "Key"]

DomainProvisioningState = Literal[
    "Unknown", "Creating", "Moving", "Deleting", "Failed", "Succeeded"
]


# ---------------------------------------------------------------------------
# Shared / read-only sub-models
# ---------------------------------------------------------------------------


class SystemData(BaseModel):
    created_by: str | None = Field(default=None, alias="createdBy")
    created_by_type: CreatedByType | None = Field(default=None, alias="createdByType")
    created_at: datetime | None = Field(default=None, alias="createdAt")
    last_modified_by: str | None = Field(default=None, alias="lastModifiedBy")
    last_modified_by_type: CreatedByType | None = Field(default=None, alias="lastModifiedByType")
    last_modified_at: datetime | None = Field(default=None, alias="lastModifiedAt")

    model_config = {"populate_by_name": True}


class Identity(BaseModel):
    principal_id: str | None = Field(default=None, alias="principalId")
    tenant_id: str | None = Field(default=None, alias="tenantId")
    type: Literal["None", "SystemAssigned", "UserAssigned"] | None = None

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# Domain response model (GET / list)
# ---------------------------------------------------------------------------


class Domain(BaseModel):
    name: str
    friendly_name: str | None = Field(default=None, alias="friendlyName")
    container_type: ContainerType | None = Field(default=None, alias="containerType")
    environment: DomainEnvironment | None = None
    description: str | None = None
    provisioning_state: DomainProvisioningState | None = Field(
        default=None, alias="provisioningState"
    )
    system_data: SystemData | None = Field(default=None, alias="systemData")
    identity: Identity | None = None
    merge_info: dict[str, Any] | None = Field(default=None, alias="mergeInfo")

    model_config = {"populate_by_name": True}


class DomainList(BaseModel):
    value: list[Domain]
    count: int | None = None
    next_link: str | None = Field(default=None, alias="nextLink")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# DomainSpec — creation / update body (used with PUT)
# ---------------------------------------------------------------------------


class DomainSpec(BaseModel):
    """Input spec for creating or updating a governance domain.

    Accepts a flat dict for YAML loading::

        {"name": "my-domain", "friendlyName": "My Domain"}

    The ``name`` field is used as the URL path key and is excluded from the
    API request body by the resource client.
    """

    name: str = Field(description="Domain name used as the URL path key")
    friendly_name: str | None = Field(
        default=None, alias="friendlyName", description="Human-readable display name"
    )
    container_type: ContainerType = Field(default="Domain", alias="containerType")
    environment: DomainEnvironment = Field(default="Prod")
    description: str | None = None

    model_config = {"populate_by_name": True}

    def model_dump(
        self,
        *,
        mode: str = "python",
        include=None,
        exclude=None,
        by_alias: bool = True,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = True,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> dict[str, Any]:
        return super().model_dump(
            by_alias=by_alias,
            exclude_unset=False,  # always include default fields
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            exclude={"name"},
            warnings=warnings,
        )
