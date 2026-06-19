"""Tests for ``bdk_sdk.config.Settings``."""

from __future__ import annotations


import pytest

from bdk_sdk.config import Settings


class TestSettings:
    def test_from_env_populates_fields(self, settings):
        assert settings.endpoint == "https://purview.example.com"
        assert settings.tenant_id == "test-tenant-id"
        assert settings.client_id == "test-client-id"
        assert settings.resource == "https://purview.example.com"
        assert settings.token_url == "https://login.example.com/tenant/oauth2/token"

    def test_from_env_raises_when_var_missing(self, monkeypatch):
        monkeypatch.delenv("AZURE_PURVIEW_ENDPOINT", raising=False)
        with pytest.raises(ValueError, match="AZURE_PURVIEW_ENDPOINT is not set"):
            Settings.from_env()

    def test_invalid_token_url_raises(self, monkeypatch):
        monkeypatch.setenv("AZURE_TOKEN_URL", "invalid-url")
        with pytest.raises(ValueError, match="not a valid URL"):
            Settings.from_env()

    def test_empty_token_url_raises(self, monkeypatch):
        monkeypatch.setenv("AZURE_TOKEN_URL", "")
        with pytest.raises(ValueError, match="not a valid URL"):
            Settings.from_env()

    def test_direct_construction(self):
        s = Settings(
            endpoint="https://e",
            tenant_id="t",
            client_id="c",
            resource="r",
            token_url="https://token",
        )
        assert s.endpoint == "https://e"
