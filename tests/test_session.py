"""Tests for ``bdk_sdk.session.PurviewSession``.

All HTTP calls are fully mocked — no live network.
"""

from __future__ import annotations

from pathlib import Path
from unittest import mock

import pytest
import requests

from bdk_sdk.session import PurviewSession


@pytest.fixture
def session_mocks(monkeypatch):
    """Patch all collaborators of PurviewSession."""
    ns = mock.Mock()
    future = 1_800_000_000

    ns.tokens = [
        {"access_token": "tok-0", "expires_on": future},
        {"access_token": "tok-1", "expires_on": future + 3600},
        {"access_token": "tok-2", "expires_on": future + 7200},
    ]
    ns.get_client_assertion = mock.Mock(return_value="assertion")
    ns.get_access_token = mock.Mock(side_effect=list(ns.tokens))
    ns.kerberos = requests.Session()
    ns.get_kerberos_session = mock.Mock(return_value=ns.kerberos)
    ns.request = mock.Mock(return_value=mock.Mock(status_code=200, content=b"{}"))

    monkeypatch.setattr("bdk_sdk.session.get_client_assertion", ns.get_client_assertion)
    monkeypatch.setattr("bdk_sdk.session.get_access_token", ns.get_access_token)
    monkeypatch.setattr("bdk_sdk.session.get_kerberos_session", ns.get_kerberos_session)
    monkeypatch.setattr(ns.kerberos, "request", ns.request)
    return ns


@pytest.fixture
def purview_session(settings, session_mocks):
    return PurviewSession(settings, Path("key.pem"), Path("cert.pem"))


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------
class TestPurviewSessionInit:
    def test_does_not_authenticate_eagerly(self, settings):
        with mock.patch("bdk_sdk.session.get_client_assertion") as gca:
            PurviewSession(settings, Path("k"), Path("c"))
            gca.assert_not_called()

    def test_stores_config(self, settings, purview_session):
        assert purview_session.settings is settings
        assert purview_session.private_key_path == Path("key.pem")
        assert purview_session.certificate_path == Path("cert.pem")

    def test_token_starts_none(self, purview_session):
        assert purview_session._access_token is None
        assert purview_session._expires_at is None

    def test_check_expired_true_when_expires_at_none(self, purview_session):
        purview_session._access_token = "token"
        purview_session._expires_at = None
        assert purview_session._check_expired() is True


# ---------------------------------------------------------------------------
# Lazy authentication
# ---------------------------------------------------------------------------
class TestPurviewSessionAuth:
    def test_first_request_triggers_auth(self, purview_session, session_mocks):
        resp = session_mocks.request.return_value
        resp.json.return_value = {"result": "ok"}
        resp.content = b'{"result":"ok"}'

        result = purview_session.request("GET", "/scan", "/datasources", "2023-09-01")
        assert result == {"result": "ok"}

        session_mocks.get_client_assertion.assert_called_once()
        session_mocks.get_access_token.assert_called_once()
        assert purview_session._access_token == "tok-0"

    def test_second_request_uses_cached_token(self, purview_session, session_mocks):
        session_mocks.request.return_value.json.return_value = {"a": 1}
        purview_session.request("GET", "/scan", "/a", "v1")

        session_mocks.get_client_assertion.reset_mock()
        session_mocks.get_access_token.reset_mock()
        session_mocks.request.return_value.json.return_value = {"b": 2}

        purview_session.request("GET", "/scan", "/b", "v1")

        session_mocks.get_client_assertion.assert_not_called()
        session_mocks.get_access_token.assert_not_called()

    def test_expired_token_refreshes(self, purview_session, session_mocks, monkeypatch):
        session_mocks.request.return_value.json.return_value = {"a": 1}
        purview_session.request("GET", "/scan", "/a", "v1")

        # Make token appear expired
        monkeypatch.setattr("bdk_sdk.session.time.time", lambda: purview_session._expires_at + 1)

        session_mocks.get_access_token.reset_mock()
        session_mocks.request.return_value.json.return_value = {"b": 2}

        purview_session.request("GET", "/scan", "/b", "v1")

        session_mocks.get_access_token.assert_called_once()
        assert purview_session._access_token == "tok-1"


# ---------------------------------------------------------------------------
# URL building
# ---------------------------------------------------------------------------
class TestPurviewSessionUrlBuilding:
    def test_builds_url_from_endpoint_base_path_and_path(
        self, purview_session, session_mocks, settings
    ):
        session_mocks.request.return_value.json.return_value = {}

        purview_session.request("GET", "/scan", "/datasources/foo", "2023-09-01")

        session_mocks.request.assert_called_once()
        call_args, call_kwargs = session_mocks.request.call_args
        assert call_args[0] == "GET"
        assert call_args[1] == "https://purview.example.com/scan/datasources/foo"

    def test_api_version_added_as_query_param(self, purview_session, session_mocks):
        session_mocks.request.return_value.json.return_value = {}

        purview_session.request("PUT", "/scan", "/datasources/bar", "2023-09-01")

        call_args, call_kwargs = session_mocks.request.call_args
        assert call_kwargs["params"]["api-version"] == "2023-09-01"

    def test_extra_params_merged(self, purview_session, session_mocks):
        session_mocks.request.return_value.json.return_value = {}

        purview_session.request(
            "GET",
            "/scan",
            "/datasources",
            "2023-09-01",
            params={"extra": "value"},
        )

        call_args, call_kwargs = session_mocks.request.call_args
        assert call_kwargs["params"] == {
            "api-version": "2023-09-01",
            "extra": "value",
        }

    def test_json_body_passed_through(self, purview_session, session_mocks):
        session_mocks.request.return_value.json.return_value = {}
        body = {"kind": "AdlsGen2", "properties": {"endpoint": "https://e"}}

        purview_session.request("PUT", "/scan", "/datasources/test", "2023-09-01", json=body)

        call_args, call_kwargs = session_mocks.request.call_args
        assert call_kwargs["json"] == body


# ---------------------------------------------------------------------------
# Response handling
# ---------------------------------------------------------------------------
class TestPurviewSessionResponse:
    def test_returns_parsed_json(self, purview_session, session_mocks):
        expected = {"key": "value"}
        resp = mock.Mock(status_code=200, content=b'{"key":"value"}')
        resp.json.return_value = expected
        session_mocks.request.return_value = resp

        result = purview_session.request("GET", "/scan", "/p", "v1")

        assert result == expected

    def test_returns_none_for_204(self, purview_session, session_mocks):
        resp = mock.Mock(status_code=204, content=b"")
        session_mocks.request.return_value = resp

        result = purview_session.request("DELETE", "/scan", "/p", "v1")

        assert result is None

    def test_returns_none_for_empty_body(self, purview_session, session_mocks):
        resp = mock.Mock(status_code=200, content=b"")
        session_mocks.request.return_value = resp

        result = purview_session.request("GET", "/scan", "/p", "v1")

        assert result is None

    def test_raises_for_status_on_non_401(self, purview_session, session_mocks):
        resp = mock.Mock(status_code=500, content=b"")
        resp.raise_for_status.side_effect = requests.HTTPError("server error")
        session_mocks.request.return_value = resp

        with pytest.raises(requests.HTTPError, match="server error"):
            purview_session.request("GET", "/scan", "/p", "v1")


# ---------------------------------------------------------------------------
# 401 retry
# ---------------------------------------------------------------------------
class TestPurviewSessionRetry:
    def test_401_refreshes_token_and_retries(self, purview_session, session_mocks):
        fail = mock.Mock(status_code=401, content=b"")
        success = mock.Mock(status_code=200, content=b'{"ok": true}')
        success.json.return_value = {"ok": True}
        session_mocks.request.side_effect = [fail, success]

        result = purview_session.request("GET", "/scan", "/p", "v1")

        assert result == {"ok": True}
        assert session_mocks.request.call_count == 2
        # Should have refreshed
        assert session_mocks.get_client_assertion.call_count == 2
        assert session_mocks.get_access_token.call_count == 2

    def test_401_with_expired_token_does_not_double_refresh(
        self, purview_session, session_mocks, monkeypatch
    ):
        # First request succeeds, setting token
        session_mocks.request.return_value.json.return_value = {"a": 1}
        purview_session.request("GET", "/scan", "/a", "v1")

        # Expire the token
        monkeypatch.setattr("bdk_sdk.session.time.time", lambda: purview_session._expires_at + 1)

        # Now the request: token expires → auth (count=2), then 401 → auth again (count=3)
        fail = mock.Mock(status_code=401, content=b"")
        success = mock.Mock(status_code=200, content=b'{"b": 2}')
        success.json.return_value = {"b": 2}
        session_mocks.request.reset_mock()
        session_mocks.request.side_effect = [fail, success]
        session_mocks.get_client_assertion.reset_mock()
        session_mocks.get_access_token.reset_mock()

        result = purview_session.request("GET", "/scan", "/b", "v1")

        assert result == {"b": 2}
        # Two auth rounds: one for expiry, one for 401
        assert session_mocks.get_client_assertion.call_count == 2
        assert session_mocks.get_access_token.call_count == 2
