"""Tests for ``bdk_sdk.datasources.DataSourceClient``."""

from __future__ import annotations


import pytest

from bdk_sdk.datasources import DataSourceClient
from bdk_sdk.models.datasource import DataSourceSpec


class _RecordingSession:
    """Records all ``request()`` calls for inspection."""

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
    return DataSourceClient(session)


_VALID_DS = {
    "name": "my-ds",
    "kind": "AdlsGen2",
    "properties": {
        "endpoint": "https://example.dfs.core.windows.net/",
        "collection": {"referenceName": "Collection-xyz"},
    },
}


# ---------------------------------------------------------------------------
# Class attributes
# ---------------------------------------------------------------------------
class TestDataSourceClientAttrs:
    def test_base_path(self):
        assert DataSourceClient.base_path == "/scan"

    def test_api_version(self):
        assert DataSourceClient.api_version == "2023-09-01"

    def test_resource_path(self):
        assert DataSourceClient.resource_path == "/datasources/{name}"

    def test_spec_model(self):
        assert DataSourceClient.spec_model is DataSourceSpec


# ---------------------------------------------------------------------------
# apply
# ---------------------------------------------------------------------------
class TestApply:
    def test_issues_put_with_correct_path_and_body(self, client, session):
        spec = DataSourceSpec.model_validate(_VALID_DS)
        result = client.apply(spec)

        assert result == {"ok": True}
        call = session.calls[-1]
        assert call["method"] == "PUT"
        assert call["base_path"] == "/scan"
        assert call["path"] == "/datasources/my-ds"
        assert call["api_version"] == "2023-09-01"
        assert call["json"]["kind"] == "AdlsGen2"
        assert "name" not in call["json"]


# ---------------------------------------------------------------------------
# add / update (aliases)
# ---------------------------------------------------------------------------
class TestAddUpdate:
    def test_add_is_alias_for_apply(self, client, session):
        spec = DataSourceSpec.model_validate(_VALID_DS)
        client.add(spec)

        call = session.calls[-1]
        assert call["method"] == "PUT"
        assert call["path"] == "/datasources/my-ds"

    def test_update_is_alias_for_apply(self, client, session):
        spec = DataSourceSpec.model_validate(_VALID_DS)
        client.update(spec)

        call = session.calls[-1]
        assert call["method"] == "PUT"
        assert call["path"] == "/datasources/my-ds"


# ---------------------------------------------------------------------------
# get / delete / list
# ---------------------------------------------------------------------------
class TestGetDeleteList:
    def test_get(self, client, session):
        result = client.get("my-ds")
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/datasources/my-ds"

    def test_delete(self, client, session):
        result = client.delete("my-ds")
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "DELETE"
        assert call["path"] == "/datasources/my-ds"

    def test_list(self, client, session):
        result = client.list()
        assert result == {"ok": True}

        call = session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/datasources"
