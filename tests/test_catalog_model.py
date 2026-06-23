"""Tests for ``bdk_sdk.models.catalog.BusinessDomainSpec``."""

from __future__ import annotations

import pytest

from bdk_sdk.models._generated.unified_catalog import Domain, PagedDomain
from bdk_sdk.models.catalog import BusinessDomainSpec


# ---------------------------------------------------------------------------
# BusinessDomainSpec
# ---------------------------------------------------------------------------
class TestBusinessDomainSpec:
    def test_minimal_valid(self):
        spec = BusinessDomainSpec.model_validate(
            {"name": "Sales", "parentId": "00000000-0000-0000-0000-000000000001"}
        )
        assert spec.name == "Sales"
        assert spec.parent_id == "00000000-0000-0000-0000-000000000001"

    def test_camelcase_input(self):
        spec = BusinessDomainSpec.model_validate(
            {
                "name": "HR",
                "parentId": "00000000-0000-0000-0000-000000000001",
                "isRestricted": True,
            }
        )
        assert spec.is_restricted is True

    def test_snake_case_input(self):
        spec = BusinessDomainSpec.model_validate(
            {
                "name": "IT",
                "parent_id": "00000000-0000-0000-0000-000000000001",
                "is_restricted": False,
            }
        )
        assert spec.parent_id == "00000000-0000-0000-0000-000000000001"
        assert spec.is_restricted is False

    def test_name_required(self):
        with pytest.raises(Exception):
            BusinessDomainSpec.model_validate({"parentId": "00000000-0000-0000-0000-000000000001"})

    def test_model_dump_for_api_body(self):
        spec = BusinessDomainSpec.model_validate(
            {
                "name": "Sales",
                "parentId": "00000000-0000-0000-0000-000000000001",
                "description": "desc",
                "isRestricted": True,
            }
        )
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        assert body["name"] == "Sales"
        assert body["parentId"] == "00000000-0000-0000-0000-000000000001"
        assert body["description"] == "desc"
        assert body["isRestricted"] is True

    def test_model_dump_excludes_none(self):
        spec = BusinessDomainSpec.model_validate(
            {"name": "Sales", "parentId": "00000000-0000-0000-0000-000000000001"}
        )
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        assert "description" not in body
        assert "isRestricted" not in body

    def test_to_domain_response(self):
        spec = BusinessDomainSpec.model_validate(
            {
                "name": "Finance",
                "parentId": "00000000-0000-0000-0000-000000000001",
                "description": "Finance domain",
                "isRestricted": True,
            }
        )
        domain_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        domain = spec.to_domain_response(domain_id)

        assert domain.name == "Finance"
        assert str(domain.id.root) == domain_id
        assert domain.isRestricted is True
        assert domain.description == "Finance domain"
        assert domain.status.root == "DRAFT"


# ---------------------------------------------------------------------------
# Generated Domain model (read operations)
# ---------------------------------------------------------------------------
_DOMAIN_JSON = {
    "id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    "name": "Sales",
    "status": "DRAFT",
    "parentId": "00000000-0000-0000-0000-000000000001",
    "systemData": {
        "createdBy": "00000000-0000-0000-0000-000000000099",
        "createdAt": "2026-01-01T00:00:00Z",
        "lastModifiedBy": "00000000-0000-0000-0000-000000000099",
        "lastModifiedAt": "2026-01-01T00:00:00Z",
    },
    "thumbnail": {},
    "domains": [],
    "managedAttributes": [],
}


class TestDomainModel:
    def test_parses_response(self):
        d = Domain.model_validate(_DOMAIN_JSON)
        assert d.name == "Sales"
        assert d.status is not None
        assert d.status.root == "DRAFT"

    def test_parses_system_data(self):
        d = Domain.model_validate(_DOMAIN_JSON)
        assert d.systemData is not None


class TestPagedDomain:
    def test_parses_list(self):
        pd = PagedDomain.model_validate({"value": [_DOMAIN_JSON]})
        assert len(pd.value) == 1
        assert pd.value[0].name == "Sales"
