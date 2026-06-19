"""Tests for ``bdk_sdk.models.domain`` models."""

from __future__ import annotations

import pytest

from bdk_sdk.models.domain import Domain, DomainList, DomainSpec


# ---------------------------------------------------------------------------
# DomainSpec
# ---------------------------------------------------------------------------
class TestDomainSpec:
    def test_valid_minimal(self):
        spec = DomainSpec.model_validate({"name": "my-domain", "friendlyName": "My Domain"})
        assert spec.name == "my-domain"
        assert spec.friendly_name == "My Domain"

    def test_defaults_populated(self):
        spec = DomainSpec.model_validate({"name": "d", "friendlyName": "f"})
        assert spec.container_type == "Domain"
        assert spec.environment == "Prod"

    def test_snake_case_input(self):
        spec = DomainSpec.model_validate(
            {"name": "d", "friendly_name": "Hello", "description": "desc"}
        )
        assert spec.friendly_name == "Hello"
        assert spec.description == "desc"

    def test_name_required(self):
        with pytest.raises(Exception):
            DomainSpec.model_validate({"friendlyName": "x"})

    def test_model_dump_excludes_name(self):
        spec = DomainSpec.model_validate({"name": "n", "friendlyName": "f"})
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        assert "name" not in body
        assert body["friendlyName"] == "f"

    def test_model_dump_includes_defaults(self):
        spec = DomainSpec.model_validate({"name": "n", "friendlyName": "f"})
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        assert body["containerType"] == "Domain"
        assert body["environment"] == "Prod"

    def test_custom_environment(self):
        spec = DomainSpec.model_validate({"name": "n", "friendlyName": "f", "environment": "Test"})
        body = spec.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        assert body["environment"] == "Test"


# ---------------------------------------------------------------------------
# Domain (response)
# ---------------------------------------------------------------------------
_VALID_RESPONSE = {
    "name": "h79pnq",
    "friendlyName": "bdk-test",
    "systemData": {
        "createdBy": "user-id",
        "createdByType": "User",
        "createdAt": "2026-06-19T08:56:56.382Z",
        "lastModifiedBy": "user-id",
        "lastModifiedByType": "User",
        "lastModifiedAt": "2026-06-19T08:56:56.382Z",
    },
    "provisioningState": "Succeeded",
    "containerType": "Domain",
    "environment": "Prod",
}


class TestDomain:
    def test_parses_actual_response(self):
        d = Domain.model_validate(_VALID_RESPONSE)
        assert d.name == "h79pnq"
        assert d.friendly_name == "bdk-test"
        assert d.provisioning_state == "Succeeded"
        assert d.container_type == "Domain"
        assert d.environment == "Prod"

    def test_parses_system_data(self):
        d = Domain.model_validate(_VALID_RESPONSE)
        assert d.system_data is not None
        assert d.system_data.created_by == "user-id"
        assert d.system_data.created_by_type == "User"

    def test_optional_fields_none(self):
        d = Domain.model_validate({"name": "x", "provisioningState": "Succeeded"})
        assert d.friendly_name is None
        assert d.system_data is None


# ---------------------------------------------------------------------------
# DomainList
# ---------------------------------------------------------------------------


class TestDomainList:
    def test_parses_list(self):
        dl = DomainList.model_validate({"value": [_VALID_RESPONSE]})
        assert len(dl.value) == 1
        assert dl.value[0].name == "h79pnq"

    def test_with_count_and_next_link(self):
        dl = DomainList.model_validate(
            {"value": [_VALID_RESPONSE], "count": 1, "nextLink": "https://..."}
        )
        assert dl.count == 1
        assert dl.next_link == "https://..."
