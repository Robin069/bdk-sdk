"""Tests for ``bdk_sdk.auth`` auth/crypto helpers.

These tests were migrated from the old ``test_session.py`` and updated to
pass a ``Settings`` instance instead of relying on module globals.
"""

from __future__ import annotations

import uuid
from unittest import mock

import jwt
import pytest
import requests
from cryptography.hazmat.primitives import hashes

from bdk_sdk import auth


# Module-internal helpers, aliased here for convenience.
_base64url = auth._base64url
_load_pem_private_key = auth._load_pem_private_key
_load_pem_certificate = auth._load_pem_certificate


# ---------------------------------------------------------------------------
# get_kerberos_session
# ---------------------------------------------------------------------------
class TestGetKerberosSession:
    def test_returns_requests_session(self):
        result = auth.get_kerberos_session()
        assert isinstance(result, requests.Session)

    def test_returns_fresh_session_each_call(self):
        assert auth.get_kerberos_session() is not auth.get_kerberos_session()


# ---------------------------------------------------------------------------
# _base64url
# ---------------------------------------------------------------------------
class TestBase64Url:
    def test_strips_padding(self):
        assert _base64url(b"any carnal pleasure.") == "YW55IGNhcm5hbCBwbGVhc3VyZS4"

    def test_is_url_safe(self):
        encoded = _base64url(b"\xfb\xff")
        assert encoded == "-_8"
        assert "+" not in encoded and "/" not in encoded and "=" not in encoded

    def test_empty_input(self):
        assert _base64url(b"") == ""


# ---------------------------------------------------------------------------
# _load_pem_private_key / _load_pem_certificate
# ---------------------------------------------------------------------------
class TestLoaders:
    def test_load_rsa_private_key(self, rsa_key_and_cert):
        key_path, _cert_path, private_key, _cert = rsa_key_and_cert
        loaded = _load_pem_private_key(key_path)
        assert loaded.public_key().public_numbers() == private_key.public_key().public_numbers()

    def test_load_non_rsa_key_raises_type_error(self, ec_key_path):
        with pytest.raises(TypeError, match="Expected an RSA private key"):
            _load_pem_private_key(ec_key_path)

    def test_load_certificate(self, rsa_key_and_cert):
        _key_path, cert_path, _private_key, cert = rsa_key_and_cert
        loaded = _load_pem_certificate(cert_path)
        assert loaded.fingerprint(hashes.SHA256()) == cert.fingerprint(hashes.SHA256())


# ---------------------------------------------------------------------------
# get_client_assertion
# ---------------------------------------------------------------------------
class TestGetClientAssertion:
    FROZEN_NOW = 1_700_000_000

    @pytest.fixture
    def frozen(self, monkeypatch):
        fixed_uuid = uuid.UUID("12345678-1234-5678-1234-567812345678")
        monkeypatch.setattr(auth.time, "time", lambda: self.FROZEN_NOW)
        monkeypatch.setattr(auth.uuid, "uuid4", lambda: fixed_uuid)
        return fixed_uuid

    def _decode(self, token, public_key, settings):
        return jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            audience=settings.token_url,
            options={"verify_exp": False, "verify_nbf": False},
        )

    def test_claims(self, settings, rsa_key_and_cert, frozen):
        key_path, cert_path, private_key, _cert = rsa_key_and_cert
        token = auth.get_client_assertion(settings, key_path, cert_path)
        decoded = self._decode(token, private_key.public_key(), settings)

        assert decoded["iss"] == settings.client_id
        assert decoded["sub"] == settings.client_id
        assert decoded["aud"] == settings.token_url
        assert decoded["nbf"] == self.FROZEN_NOW
        assert decoded["exp"] == self.FROZEN_NOW + 600
        assert decoded["jti"] == str(frozen)

    def test_headers_and_x5t(self, settings, rsa_key_and_cert, frozen):
        key_path, cert_path, _private_key, cert = rsa_key_and_cert
        token = auth.get_client_assertion(settings, key_path, cert_path)
        headers = jwt.get_unverified_header(token)

        assert headers["typ"] == "JWT"
        assert headers["alg"] == "RS256"
        assert headers["x5t"] == _base64url(cert.fingerprint(hashes.SHA1()))

    def test_custom_validity_seconds(self, settings, rsa_key_and_cert, frozen):
        key_path, cert_path, private_key, _cert = rsa_key_and_cert
        token = auth.get_client_assertion(settings, key_path, cert_path, validity_seconds=30)
        decoded = self._decode(token, private_key.public_key(), settings)
        assert decoded["exp"] == self.FROZEN_NOW + 30

    def test_signature_verifiable_with_public_key(self, settings, rsa_key_and_cert, frozen):
        key_path, cert_path, private_key, _cert = rsa_key_and_cert
        token = auth.get_client_assertion(settings, key_path, cert_path)
        from cryptography.hazmat.primitives.asymmetric import rsa

        wrong_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        with pytest.raises(jwt.InvalidSignatureError):
            self._decode(token, wrong_key.public_key(), settings)

    def test_non_rsa_key_raises_type_error(self, settings, ec_key_path, rsa_key_and_cert):
        _key_path, cert_path, _private_key, _cert = rsa_key_and_cert
        with pytest.raises(TypeError, match="Expected an RSA private key"):
            auth.get_client_assertion(settings, ec_key_path, cert_path)


# ---------------------------------------------------------------------------
# get_access_token
# ---------------------------------------------------------------------------
class TestGetAccessToken:
    def test_posts_expected_payload_and_returns_json(self, settings, monkeypatch, fake_response):
        expected = {"access_token": "abc", "expires_on": 123456}
        response = fake_response(json_data=expected)
        post = mock.Mock(return_value=response)
        monkeypatch.setattr(auth.requests, "post", post)

        result = auth.get_access_token(settings, "the-assertion")

        assert result == expected
        post.assert_called_once_with(
            url=settings.token_url,
            data={
                "tenant": settings.tenant_id,
                "client_id": settings.client_id,
                "resource": settings.resource,
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "client_assertion": "the-assertion",
                "grant_type": "client_credentials",
            },
        )

    def test_calls_raise_for_status(self, settings, monkeypatch, fake_response):
        response = fake_response(json_data={"access_token": "abc", "expires_on": 1})
        monkeypatch.setattr(auth.requests, "post", mock.Mock(return_value=response))

        auth.get_access_token(settings, "the-assertion")

        assert response.raise_for_status_called is True

    def test_propagates_http_error(self, settings, monkeypatch, fake_response):
        response = fake_response(raise_exc=requests.HTTPError("boom"))
        monkeypatch.setattr(auth.requests, "post", mock.Mock(return_value=response))

        with pytest.raises(requests.HTTPError, match="boom"):
            auth.get_access_token(settings, "the-assertion")
