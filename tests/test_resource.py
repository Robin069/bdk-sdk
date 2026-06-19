"""Tests for ``bdk_sdk.resource.PurviewResourceClient``."""

from __future__ import annotations


import pytest
from pydantic import BaseModel, Field

from bdk_sdk.resource import PurviewResourceClient


class _FakeSession:
    """A fake PurviewSession that records calls."""

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
        return {"response": "ok"}


class _TestSpec(BaseModel):
    name: str = Field(description="Resource name")
    value: str = "default"


class _TestClient(PurviewResourceClient):
    base_path = "/api"
    api_version = "v1"
    resource_path = "/things/{name}"
    spec_model = _TestSpec


@pytest.fixture
def client():
    return _TestClient(_FakeSession())


# ---------------------------------------------------------------------------
# apply
# ---------------------------------------------------------------------------
class TestApply:
    def test_serializes_spec_and_issues_put(self, client):
        spec = _TestSpec(name="my-thing", value="hello")
        result = client.apply(spec)

        assert result == {"response": "ok"}
        call = client.session.calls[-1]
        assert call["method"] == "PUT"
        assert call["base_path"] == "/api"
        assert call["path"] == "/things/my-thing"
        assert call["api_version"] == "v1"
        assert call["json"] == {"name": "my-thing", "value": "hello"}

    def test_excludes_none_and_unset_by_default(self, client):
        spec = _TestSpec(name="t")
        result = client.apply(spec)
        assert result == {"response": "ok"}

        call = client.session.calls[-1]
        # name is always set, value is unset so should be excluded
        assert call["json"] == {"name": "t"}


# ---------------------------------------------------------------------------
# get
# ---------------------------------------------------------------------------
class TestGet:
    def test_issues_get_with_name_in_path(self, client):
        result = client.get("my-thing")

        assert result == {"response": "ok"}
        call = client.session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/things/my-thing"

    def test_no_body_in_get(self, client):
        client.get("x")
        call = client.session.calls[-1]
        assert call["json"] is None


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------
class TestDelete:
    def test_issues_delete_with_name_in_path(self, client):
        result = client.delete("my-thing")

        assert result == {"response": "ok"}
        call = client.session.calls[-1]
        assert call["method"] == "DELETE"
        assert call["path"] == "/things/my-thing"


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------
class TestList:
    def test_strips_trailing_variable_segment(self, client):
        result = client.list()

        assert result == {"response": "ok"}
        call = client.session.calls[-1]
        assert call["method"] == "GET"
        assert call["path"] == "/things"

    def test_custom_create_verb(self, client):
        class _PutClient(PurviewResourceClient):
            base_path = "/api"
            api_version = "v1"
            resource_path = "/things/{name}"
            spec_model = _TestSpec
            create_verb = "POST"

        c = _PutClient(_FakeSession())
        spec = _TestSpec(name="x")
        c.apply(spec)
        call = c.session.calls[-1]
        assert call["method"] == "POST"
