"""Tests for ``bdk_sdk.catalog.BusinessDomainClient``."""

from __future__ import annotations

import pytest

from bdk_sdk.catalog import BusinessDomainClient
from bdk_sdk.models.catalog import BusinessDomainSpec


class _RecordingSession:
    def __init__(self):
        self.calls = []

    def request(self, method, base_path, path, api_version, *, json=None, params=None):
        self.calls.append(
            {
                "method": method,
                "base_path": base_path,
                "path": path,
                "api_version": api_version,
                "json": json,
                "params": params,
            }
        )
        return {"ok": True}


@pytest.fixture
def session():
    return _RecordingSession()


@pytest.fixture
def client(session):
    return BusinessDomainClient(session)


_VALID_SPEC = {
    "name": "Sales",
    "parentId": "00000000-0000-0000-0000-000000000001",
    "description": "Sales domain",
}


# ---------------------------------------------------------------------------
# Class attributes
# ---------------------------------------------------------------------------
class TestBusinessDomainClientAttrs:
    def test_base_path(self):
        assert BusinessDomainClient.base_path == "/datagovernance/catalog"

    def test_api_version(self):
        assert BusinessDomainClient.api_version == "2026-03-20-preview"

    def test_resource_path(self):
        assert BusinessDomainClient.resource_path == "/businessdomains/{name}"

    def test_spec_model(self):
        assert BusinessDomainClient.spec_model is BusinessDomainSpec


# ---------------------------------------------------------------------------
# apply (create)
# ---------------------------------------------------------------------------
class TestApplyCreate:
    def test_posts_when_no_id(self, client, session):
        spec = BusinessDomainSpec.model_validate(_VALID_SPEC)
        assert spec.id is None

        result = client.apply(spec)
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "POST"
        assert call["path"] == "/businessdomains"
        assert call["api_version"] == "2026-03-20-preview"
        assert call["json"]["name"] == "Sales"
        assert call["json"]["parentId"] == "00000000-0000-0000-0000-000000000001"


# ---------------------------------------------------------------------------
# apply (update)
# ---------------------------------------------------------------------------
class TestApplyUpdate:
    def test_puts_when_id_set(self, client, session):
        spec = BusinessDomainSpec.model_validate({"id": "aaaa-aaaa-aaaa-aaaa", **_VALID_SPEC})
        result = client.apply(spec)
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "PUT"
        assert call["path"] == "/businessdomains/aaaa-aaaa-aaaa-aaaa"
        assert call["json"]["name"] == "Sales"


# ---------------------------------------------------------------------------
# add / update (aliases)
# ---------------------------------------------------------------------------
class TestAddUpdate:
    def test_add_is_alias_for_apply(self, client, session):
        spec = BusinessDomainSpec.model_validate(_VALID_SPEC)
        client.add(spec)
        call = session.calls[-1]
        assert call["method"] == "POST"

    def test_update_is_alias_for_apply(self, client, session):
        spec = BusinessDomainSpec.model_validate({"id": "bbbb-bbbb-bbbb-bbbb", **_VALID_SPEC})
        client.update(spec)
        call = session.calls[-1]
        assert call["method"] == "PUT"


# ---------------------------------------------------------------------------
# get / delete / list (inherited from PurviewResourceClient)
# ---------------------------------------------------------------------------
class TestInherited:
    def test_get(self, client, session):
        result = client.get("aaaa-aaaa-aaaa-aaaa")
        assert result == {"ok": True}
        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/businessdomains/aaaa-aaaa-aaaa-aaaa"

    def test_delete(self, client, session):
        result = client.delete("aaaa-aaaa-aaaa-aaaa")
        assert result == {"ok": True}
        call = session.calls[-1]
        assert call["method"] == "DELETE"
        assert call["path"] == "/businessdomains/aaaa-aaaa-aaaa-aaaa"

    def test_list(self, client, session):
        result = client.list()
        assert result == {"ok": True}
        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/businessdomains"
