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


class TestCreate:
    def test_posts_with_correct_path_and_body(self, client, session):
        spec = BusinessDomainSpec.model_validate(_VALID_SPEC)
        result = client.create(spec)
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "POST"
        assert call["base_path"] == "/datagovernance/catalog"
        assert call["path"] == "/businessdomains"
        assert call["api_version"] == "2026-03-20-preview"
        assert call["json"]["name"] == "Sales"
        assert call["json"]["parentId"] == "00000000-0000-0000-0000-000000000001"


class TestUpdate:
    def test_puts_with_domain_id_in_path(self, client, session):
        spec = BusinessDomainSpec.model_validate(_VALID_SPEC)
        result = client.update("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", spec)
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "PUT"
        assert call["path"] == "/businessdomains/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        assert call["json"]["name"] == "Sales"


class TestGet:
    def test_gets_with_domain_id(self, client, session):
        result = client.get("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/businessdomains/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        assert call["json"] is None


class TestDelete:
    def test_deletes_with_domain_id(self, client, session):
        result = client.delete("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "DELETE"
        assert call["path"] == "/businessdomains/bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"


class TestList:
    def test_lists_businessdomains(self, client, session):
        result = client.list()
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/businessdomains"
