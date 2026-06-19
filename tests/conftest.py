"""Shared pytest fixtures and import-time environment bootstrap.

Tests that call ``Settings.from_env()`` read Azure environment variables at
that point, so we populate dummy values at module top before any test module
import executes.
"""

from __future__ import annotations

import os
from pathlib import Path

# --- Import-time environment bootstrap (must run before module imports) ---
_DUMMY_ENV = {
    "AZURE_PURVIEW_ENDPOINT": "https://purview.example.com",
    "AZURE_TOKEN_URL": "https://login.example.com/tenant/oauth2/token",
    "AZURE_TENANT_ID": "test-tenant-id",
    "AZURE_CLIENT_ID": "test-client-id",
    "AZURE_RESOURCE": "https://purview.example.com",
}
for _key, _value in _DUMMY_ENV.items():
    os.environ.setdefault(_key, _value)


import pytest  # noqa: E402  (import after env bootstrap is intentional)
from cryptography import x509  # noqa: E402
from cryptography.hazmat.primitives import hashes, serialization  # noqa: E402
from cryptography.hazmat.primitives.asymmetric import ec, rsa  # noqa: E402
from cryptography.x509.oid import NameOID  # noqa: E402


@pytest.fixture
def settings():
    """A :class:`bdk_sdk.config.Settings` instance populated from dummy env."""
    from bdk_sdk.config import Settings

    return Settings.from_env()


# ---------------------------------------------------------------------------
# Cryptographic fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def rsa_private_key() -> rsa.RSAPrivateKey:
    """A real 2048-bit RSA private key, reused across the session for speed."""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


@pytest.fixture(scope="session")
def self_signed_cert(rsa_private_key: rsa.RSAPrivateKey) -> x509.Certificate:
    """A self-signed X.509 certificate matching ``rsa_private_key``."""
    import datetime

    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "bdk-sdk-test")])
    now = datetime.datetime(2020, 1, 1, tzinfo=datetime.timezone.utc)
    return (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(rsa_private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=3650))
        .sign(rsa_private_key, hashes.SHA256())
    )


@pytest.fixture
def rsa_key_and_cert(
    tmp_path: Path,
    rsa_private_key: rsa.RSAPrivateKey,
    self_signed_cert: x509.Certificate,
):
    """Write the RSA key + self-signed cert to PEM files in a temp dir."""
    key_path = tmp_path / "key.pem"
    cert_path = tmp_path / "cert.pem"

    key_path.write_bytes(
        rsa_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
    cert_path.write_bytes(self_signed_cert.public_bytes(serialization.Encoding.PEM))

    return key_path, cert_path, rsa_private_key, self_signed_cert


@pytest.fixture
def ec_key_path(tmp_path: Path) -> Path:
    """A non-RSA (EC) PEM private key, to drive the ``TypeError`` path."""
    ec_key = ec.generate_private_key(ec.SECP256R1())
    key_path = tmp_path / "ec_key.pem"
    key_path.write_bytes(
        ec_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
    return key_path


# ---------------------------------------------------------------------------
# HTTP mocking helpers
# ---------------------------------------------------------------------------


class FakeResponse:
    """Minimal stand-in for ``requests.Response`` used in tests."""

    def __init__(
        self,
        json_data: dict | None = None,
        raise_exc: Exception | None = None,
        status_code: int = 200,
        content: bytes = b"",
    ):
        self._json_data = json_data if json_data is not None else {}
        self._raise_exc = raise_exc
        self.status_code = status_code
        self.content = content
        self.raise_for_status_called = False

    def raise_for_status(self) -> None:
        self.raise_for_status_called = True
        if self._raise_exc is not None:
            raise self._raise_exc

    def json(self) -> dict:
        return self._json_data


@pytest.fixture
def fake_response():
    """Factory for building :class:`FakeResponse` objects in tests."""

    def _make(
        json_data: dict | None = None,
        raise_exc: Exception | None = None,
        status_code: int = 200,
        content: bytes = b"",
    ) -> FakeResponse:
        return FakeResponse(
            json_data=json_data,
            raise_exc=raise_exc,
            status_code=status_code,
            content=content,
        )

    return _make
